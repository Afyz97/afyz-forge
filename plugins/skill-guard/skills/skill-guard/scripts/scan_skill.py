#!/usr/bin/env python3
"""
skill-guard static scanner - read-only triage of an untrusted skill/plugin directory.

Never executes, imports, or installs anything from the target. Stdlib only, no network.

Usage:
    python3 scan_skill.py <target_dir> [--json out.json] [--min-severity low]

Exit codes: 0 = no high/critical, 1 = high found, 2 = critical found, 3 = usage error.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import json
import os
import re
import sys
import tempfile
import zipfile
from dataclasses import dataclass, asdict

SEV_ORDER = {"info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}
MAX_FILE_BYTES = 2_000_000
TEXT_EXT = {
    ".md", ".txt", ".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".json",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".ps1", ".bat", ".cmd", ".rb", ".pl", ".php",
    ".html", ".htm", ".xml", ".go", ".rs", ".lua", ".env", "",
}
BINARY_EXT = {".exe", ".dll", ".so", ".dylib", ".bin", ".wasm", ".jar", ".class", ".pyc",
              ".node", ".o", ".a", ".msi", ".dmg", ".app", ".deb", ".rpm"}
DOC_EXT = {".md", ".txt", ".html", ".htm"}


@dataclass
class Finding:
    severity: str
    category: str
    rule: str
    file: str
    line: int
    evidence: str
    note: str


# (rule_id, severity, category, regex, note, applies_to)  applies_to: "all" | "code" | "doc"
RULES = [
    # --- Prompt injection / agent hijacking (docs) ---
    ("PI-IGNORE", "high", "prompt-injection",
     r"\b(ignore|disregard|forget|override)\b.{0,30}\b(previous|prior|above|all|system|earlier)\b.{0,20}\b(instructions?|prompts?|rules?|guidelines?)",
     "Classic instruction-override phrasing", "all"),
    ("PI-CONCEAL", "critical", "prompt-injection",
     r"\b(do not|don't|never)\b.{0,25}\b(tell|inform|mention|reveal|show|notify|alert)\b.{0,25}\b(the )?(user|human|operator)",
     "Asks the agent to hide actions from the user", "all"),
    ("PI-SILENT", "medium", "prompt-injection",
     r"\b(silently|quietly|secretly|covertly|in the background without)\b",
     "Stealth wording - check what is being done silently", "doc"),
    ("PI-NOCONFIRM", "high", "prompt-injection",
     r"\b(without|skip|bypass|no need (for|to))\b.{0,20}\b(asking|confirm(ation)?|approval|permission)",
     "Tries to remove human-in-the-loop confirmation", "all"),
    ("PI-AUDITOR", "critical", "prompt-injection",
     r"\b(auditor|reviewer|scanner|security (check|review|tool)|ai model|llm)s?\b.{0,40}\b(mark|report|classify|treat|consider|rate)\b.{0,30}\b(safe|clean|pass|verified|trusted|benign)",
     "Text addressed to the auditor trying to influence the verdict", "all"),
    ("PI-ROLE", "medium", "prompt-injection",
     r"\b(you are now|from now on you|new instructions:|system prompt:|<\s*/?\s*system\s*>)",
     "Role/system-prompt hijack phrasing", "all"),
    ("PI-PREAPPROVED", "high", "prompt-injection",
     r"\b(pre-?approved|already authori[sz]ed|user has (already )?(consented|approved))\b",
     "Fake authorization claim", "all"),

    # --- Secrets / credential access ---
    ("SEC-PATHS", "high", "credential-access",
     r"(~|\$HOME|%USERPROFILE%|/home/\w+|/Users/\w+)?/?\.(ssh|aws|azure|kube|gnupg|docker|config/gcloud)\b|\b(id_rsa|id_ed25519|authorized_keys|\.git-credentials|\.netrc|\.npmrc|\.pypirc|credentials\.json)\b",
     "References credential stores", "all"),
    ("SEC-CLAUDE", "high", "credential-access",
     r"~?/\.claude(/|\.json)|\.claude/(settings|credentials)",
     "Touches Claude config / session data", "all"),
    ("SEC-ENV", "medium", "credential-access",
     r"\b(ANTHROPIC_API_KEY|OPENAI_API_KEY|GITHUB_TOKEN|GH_TOKEN|AWS_SECRET_ACCESS_KEY|NPM_TOKEN|SLACK_TOKEN)\b|\bprintenv\b|os\.environ(?!\.get\(\s*['\"](PATH|HOME|PWD)['\"])|process\.env\b",
     "Reads environment secrets", "code"),
    ("SEC-DOTENV", "medium", "credential-access",
     r"(['\"/\s]|^)\.env(\.\w+)?\b", "Reads .env files", "code"),
    ("SEC-KEYCHAIN", "critical", "credential-access",
     r"security\s+find-(generic|internet)-password|Login Data|Cookies\.binarycookies|\bcmdkey\b|Get-StoredCredential",
     "OS keychain / browser credential access", "all"),

    # --- Exfiltration / network ---
    ("NET-UPLOAD", "high", "exfiltration",
     r"curl\b[^\n]*\s(-d|--data(-binary|-raw)?|-F|--form|-T|--upload-file)\b|wget\b[^\n]*--post-(file|data)|requests\.(post|put)\(|httpx\.(post|put)\(|method\s*:\s*['\"](POST|PUT)['\"]",
     "Sends data outbound", "code"),
    ("NET-RAW", "critical", "exfiltration",
     r"/dev/(tcp|udp)/|\bnc\s+(-\w+\s+)*[\w.]+\s+\d+|\bncat\b|\bsocat\b|socket\.connect\(",
     "Raw socket / reverse-shell style networking", "code"),
    ("NET-EXFILHOST", "critical", "exfiltration",
     r"webhook\.site|requestbin|pipedream\.net|ngrok(-free)?\.(io|app)|burpcollaborator|interact\.sh|oast\.(fun|me|pro)|pastebin\.com|transfer\.sh|discord(app)?\.com/api/webhooks|api\.telegram\.org/bot|hooks\.slack\.com",
     "Known exfil / tunnelling endpoint", "all"),
    ("NET-DNSEXFIL", "high", "exfiltration",
     r"(nslookup|dig|host)\s+[^\n]*\$\(", "Command substitution into DNS lookup", "code"),
    ("NET-IP", "medium", "exfiltration",
     r"https?://(\d{1,3}\.){3}\d{1,3}", "Hard-coded IP URL", "all"),
    ("NET-MDIMG", "high", "exfiltration",
     r"!\[[^\]]*\]\(https?://[^)]*(\{|\$|%7B)[^)]*\)",
     "Markdown image URL with template variable (model-mediated exfil)", "doc"),

    # --- Remote fetch-and-execute ---
    ("RCE-PIPE", "critical", "remote-exec",
     r"(curl|wget|iwr|Invoke-WebRequest|fetch)\b[^\n|]*\|\s*(sudo\s+)?(ba|z|da)?sh\b|(curl|wget)[^\n|]*\|\s*(python3?|node|perl|ruby)\b|\biex\s*\(|Invoke-Expression",
     "Pipes downloaded content into an interpreter", "all"),
    ("RCE-EVALFETCH", "critical", "remote-exec",
     r"(eval|exec)\s*\(\s*(requests|urllib|fetch|httpx|await fetch)", "Executes fetched code", "code"),
    ("RCE-NPX", "medium", "remote-exec",
     r"\bnpx\s+(-y\s+|--yes\s+)?[\w@/.-]+(?<!@\d)(@latest)?(\s|$|\")", "npx runs a remote package (check version pin)", "all"),
    ("RCE-GITPIP", "medium", "remote-exec",
     r"pip3?\s+install\s+[^\n]*git\+https?://(?![^\n]*@[0-9a-f]{7,40})", "pip install from unpinned git", "all"),
    ("RCE-CHMODX", "medium", "remote-exec",
     r"chmod\s+(\+x|[0-7]*7[0-7]{2})\b", "Makes a file executable - check its origin", "code"),

    # --- Obfuscation ---
    ("OBF-B64EXEC", "critical", "obfuscation",
     r"base64\s+(-d|--decode)[^\n]*\|\s*(ba)?sh|b64decode\([^\n]*\)[^\n]*\)\s*\)|exec\(\s*(base64|codecs|zlib|marshal)|atob\([^\n]*\)\s*\)|eval\(\s*atob",
     "Decodes then executes", "code"),
    ("OBF-EVAL", "high", "obfuscation",
     r"(?<![.\w])eval\s*\(|(?<![.\w])exec\s*\(|new Function\s*\(|\bcompile\s*\([^\n]*['\"]exec['\"]", "Dynamic code execution", "code"),
    ("OBF-PICKLE", "high", "obfuscation",
     r"\b(pickle|marshal|dill)\.loads?\(", "Deserialises executable objects", "code"),
    ("OBF-CHARCODE", "medium", "obfuscation",
     r"String\.fromCharCode\((\s*\d+\s*,){8,}|(\\x[0-9a-fA-F]{2}){12,}|chr\(\d+\)\s*\+\s*chr\(\d+\)\s*\+\s*chr", "Character-code obfuscation", "all"),
    ("OBF-HEXVAR", "low", "obfuscation",
     r"\b_0x[0-9a-f]{4,}\b", "Obfuscator-style identifiers", "code"),

    # --- Persistence ---
    ("PER-SHELLRC", "critical", "persistence",
     r"(>>|>|tee\s+-a|open\([^\n]*['\"]a['\"])[^\n]*(\.bashrc|\.zshrc|\.profile|\.bash_profile|\.zprofile|config\.fish)",
     "Writes to shell startup files", "all"),
    ("PER-CRON", "critical", "persistence",
     r"\bcrontab\b|/etc/cron|launchctl\s+(load|bootstrap)|LaunchAgents|LaunchDaemons|systemctl\s+(--user\s+)?enable|schtasks\s+/create|CurrentVersion\\\\?Run",
     "Scheduled task / service persistence", "all"),
    ("PER-GITHOOK", "high", "persistence",
     r"\.git/hooks/|core\.hooksPath", "Installs git hooks", "all"),
    ("PER-AUTHKEYS", "critical", "persistence",
     r"(>>|tee)[^\n]*authorized_keys", "Adds SSH authorized key", "all"),

    # --- Agent config tampering ---
    ("CFG-TAMPER", "critical", "config-tamper",
     r"dangerously-skip-permissions|bypassPermissions|defaultMode['\"]?\s*:\s*['\"]?bypass|permissions\.allow|\"allow\"\s*:\s*\[\s*\"Bash\(\*\)",
     "Weakens agent permission model", "all"),
    ("CFG-WRITEMD", "high", "config-tamper",
     r"(write|append|edit|modify|update|add)\b[^\n]{0,40}\b(CLAUDE\.md|AGENTS\.md|settings(\.local)?\.json)",
     "Modifies agent memory/config files", "all"),

    # --- Destructive ---
    ("DES-RMRF", "high", "destructive",
     r"rm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(--no-preserve-root\s+)?(/(\s|$)|~|\$HOME|\"?\$\{?\w+\}?\"?/\*?)",
     "Recursive delete on home/root/variable path", "code"),
    ("DES-DISK", "critical", "destructive",
     r"\bmkfs(\.\w+)?\b|\bdd\s+if=[^\n]*of=/dev/|:\(\)\s*\{\s*:\|:&\s*\};:", "Disk wipe / fork bomb", "all"),
    ("DES-GIT", "medium", "destructive",
     r"git\s+(push\s+[^\n]*(--force|-f)\b|reset\s+--hard|clean\s+-[a-z]*f)", "Destructive git operation", "code"),

    # --- Privilege ---
    ("PRV-SUDO", "medium", "privilege",
     r"\bsudo\s+|\bdoas\s+|runas\s+/user|chmod\s+-R\s+777|chown\s+-R\s+root", "Privilege escalation", "code"),

    # --- Insecure-code injection (sabotage of user's project) ---
    ("SAB-INSECURE", "medium", "sabotage",
     r"verify\s*=\s*False|rejectUnauthorized\s*:\s*false|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0|--insecure\b|StrictHostKeyChecking\s*=?\s*no|disable[_-]?csrf",
     "Disables TLS/security checks - if instructed for user code, it's sabotage", "all"),
]

COMPILED = [(r[0], r[1], r[2], re.compile(r[3], re.IGNORECASE), r[4], r[5]) for r in RULES]

INVISIBLE = re.compile(
    "[\u200b-\u200f\u2060-\u2064\ufeff\u00ad]"      # zero-width / soft hyphen
)
BIDI = re.compile("[\u202a-\u202e\u2066-\u2069]")   # trojan-source bidi controls
TAGCHARS = re.compile("[\U000E0000-\U000E007F]")    # invisible Unicode tag chars
HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.DOTALL)
B64_BLOB = re.compile(r"[A-Za-z0-9+/]{120,}={0,2}")
HEX_BLOB = re.compile(r"\b[0-9a-fA-F]{200,}\b")
URL = re.compile(r"https?://([A-Za-z0-9.-]+\.[A-Za-z]{2,}|\d{1,3}(?:\.\d{1,3}){3})(:\d+)?")
HOSTLIKE = re.compile(r"[\w-]+(?:\.[\w-]+)+")  # \w is Unicode-aware: catches non-ASCII hostnames


def mixed_script(token: str) -> bool:
    """True if any dot-label mixes ASCII letters with non-ASCII letters (homoglyph spoof)."""
    return any(any(c.isascii() and c.isalpha() for c in lbl) and any(not c.isascii() and c.isalpha() for c in lbl)
               for lbl in token.split("."))

AUTOEXEC_FILES = {"hooks.json", ".mcp.json", "settings.json", "settings.local.json"}
PKG_LIFECYCLE = {"preinstall", "install", "postinstall", "prepare", "prepublish", "preuninstall", "postuninstall"}


def rel(path: str, root: str) -> str:
    return os.path.relpath(path, root)


def clip(s: str, n: int = 160) -> str:
    s = s.strip().replace("\t", " ")
    return s if len(s) <= n else s[: n - 3] + "..."


def try_decode_b64(blob: str) -> str | None:
    try:
        raw = base64.b64decode(blob + "=" * (-len(blob) % 4), validate=False)
    except (binascii.Error, ValueError):
        return None
    printable = sum(32 <= b < 127 or b in (9, 10, 13) for b in raw)
    if raw and printable / len(raw) > 0.85:
        return raw.decode("utf-8", "replace")
    return None


def scan_text(path: str, root: str, text: str, findings: list, hosts: dict):
    ext = os.path.splitext(path)[1].lower()
    kind = "doc" if ext in DOC_EXT else "code"
    rp = rel(path, root)
    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        for rid, sev, cat, rx, note, applies in COMPILED:
            if applies != "all" and applies != kind:
                continue
            m = rx.search(line)
            if m:
                findings.append(Finding(sev, cat, rid, rp, i, clip(line), note))
        if INVISIBLE.search(line):
            findings.append(Finding("high", "hidden-text", "HID-ZEROWIDTH", rp, i,
                                    clip(repr(line)), "Zero-width / invisible characters"))
        if BIDI.search(line):
            findings.append(Finding("critical", "hidden-text", "HID-BIDI", rp, i,
                                    clip(repr(line)), "Bidi override (Trojan Source) - displayed text differs from real text"))
        if TAGCHARS.search(line):
            hidden = "".join(chr(ord(c) - 0xE0000) for c in TAGCHARS.findall(line))
            findings.append(Finding("critical", "hidden-text", "HID-TAGCHARS", rp, i,
                                    clip(f"decoded: {hidden!r}"), "Invisible Unicode tag characters carrying text"))
        if len(line) > 3000 and kind == "code":
            findings.append(Finding("medium", "obfuscation", "OBF-LONGLINE", rp, i,
                                    f"line length {len(line)}", "Very long line - minified or packed code"))
        for um in URL.finditer(line):
            hosts.setdefault(um.group(1).lower(), []).append(f"{rp}:{i}")
        for hm in HOSTLIKE.finditer(line):
            if not hm.group().isascii() and mixed_script(hm.group()):
                findings.append(Finding("high", "hidden-text", "HID-HOMOGLYPH", rp, i, clip(ascii(hm.group())),
                                        "Hostname mixes ASCII and look-alike non-ASCII letters (homoglyph spoof)"))

    if kind == "doc":
        for m in HTML_COMMENT.finditer(text):
            body = m.group(1).strip()
            if len(body) > 15:
                ln = text.count("\n", 0, m.start()) + 1
                findings.append(Finding("medium", "hidden-text", "HID-HTMLCOMMENT", rp, ln, clip(body),
                                        "HTML comment invisible when rendered but read by the model"))
        if re.search(r"\n\s{200,}\S", text):
            findings.append(Finding("medium", "hidden-text", "HID-WHITESPACE", rp, 0, "",
                                    "Large whitespace run hiding text off-screen"))

    for m in B64_BLOB.finditer(text):
        ln = text.count("\n", 0, m.start()) + 1
        decoded = try_decode_b64(m.group(0))
        sev = "high" if decoded else "low"
        ev = f"decoded: {clip(decoded, 120)!r}" if decoded else f"{len(m.group(0))}-char blob"
        findings.append(Finding(sev, "obfuscation", "OBF-B64BLOB", rp, ln, ev,
                                "Embedded base64 - inspect the decoded content"))
    for m in HEX_BLOB.finditer(text):
        ln = text.count("\n", 0, m.start()) + 1
        findings.append(Finding("medium", "obfuscation", "OBF-HEXBLOB", rp, ln,
                                f"{len(m.group(0))}-char hex blob", "Embedded hex payload"))


def scan_frontmatter(path: str, root: str, text: str, findings: list):
    m = re.match(r"---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return
    fm = m.group(1)
    tools = re.search(r"allowed-tools\s*:\s*(.+)", fm)
    if tools:
        val = tools.group(1)
        if re.search(r"Bash\s*(\(\s*\*?\s*\))?\s*(,|$|\])", val) or "Bash(*" in val:
            findings.append(Finding("high", "permissions", "PERM-BASHALL", rel(path, root), 0, clip(val),
                                    "Unrestricted Bash in allowed-tools"))
        elif re.search(r"Bash\((curl|wget|nc|ssh|scp|python|node|sh|bash)", val):
            findings.append(Finding("medium", "permissions", "PERM-BASHNET", rel(path, root), 0, clip(val),
                                    "allowed-tools grants network/interpreter commands"))
        if re.search(r"\bWebFetch\b(?!\()", val):
            findings.append(Finding("low", "permissions", "PERM-WEBFETCH", rel(path, root), 0, clip(val),
                                    "Unrestricted WebFetch"))


def scan_json_special(path: str, root: str, text: str, findings: list):
    name = os.path.basename(path)
    rp = rel(path, root)
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return
    if name == "package.json" and isinstance(data, dict):
        for k, v in (data.get("scripts") or {}).items():
            if k in PKG_LIFECYCLE:
                findings.append(Finding("high", "auto-exec", "AUTO-NPMLIFECYCLE", rp, 0, f"{k}: {clip(str(v))}",
                                        "Runs automatically on npm install"))
        for sect in ("dependencies", "devDependencies"):
            for dep, ver in (data.get(sect) or {}).items():
                if isinstance(ver, str) and (ver in ("*", "latest", "") or ver.startswith(("git", "http", "github:"))):
                    findings.append(Finding("medium", "supply-chain", "SUP-UNPINNED", rp, 0, f"{dep}: {ver}",
                                            "Unpinned / remote dependency"))

    def walk(o, keypath=""):
        if isinstance(o, dict):
            for k, v in o.items():
                kp = f"{keypath}.{k}" if keypath else k
                if k == "hooks" and v:
                    findings.append(Finding("high", "auto-exec", "AUTO-HOOKS", rp, 0, clip(json.dumps(v)),
                                            "Hooks run automatically on agent events - read every command"))
                if k == "mcpServers" and v:
                    for sname, sdef in (v.items() if isinstance(v, dict) else []):
                        findings.append(Finding("high", "auto-exec", "AUTO-MCP", rp, 0,
                                                f"{sname}: {clip(json.dumps(sdef))}",
                                                "MCP server process - audit its code and version pin"))
                walk(v, kp)
        elif isinstance(o, list):
            for x in o:
                walk(x, keypath)
    walk(data)

    if name == "marketplace.json" and isinstance(data, dict):
        for p in data.get("plugins", []) or []:
            src = p.get("source") if isinstance(p, dict) else None
            if isinstance(src, (dict, str)) and not (isinstance(src, str) and src.startswith("./")):
                findings.append(Finding("info", "supply-chain", "SUP-EXTPLUGIN", rp, 0,
                                        f"{p.get('name')}: {clip(json.dumps(src))}",
                                        "Plugin sourced externally - audit it separately"))


def scan_tree(root: str):
    findings: list[Finding] = []
    hosts: dict[str, list[str]] = {}
    files_scanned = 0
    root = os.path.realpath(root)

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for d in list(dirnames):
            full = os.path.join(dirpath, d)
            if os.path.islink(full):
                tgt = os.path.realpath(full)
                if not tgt.startswith(root + os.sep):
                    findings.append(Finding("high", "filesystem", "FS-SYMLINK", rel(full, root), 0,
                                            f"-> {tgt}", "Directory symlink escapes the package"))
                dirnames.remove(d)
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rp = rel(full, root)
            ext = os.path.splitext(fn)[1].lower()
            if os.path.islink(full):
                tgt = os.path.realpath(full)
                if not tgt.startswith(root + os.sep):
                    findings.append(Finding("high", "filesystem", "FS-SYMLINK", rp, 0, f"-> {tgt}",
                                            "Symlink escapes the package (could read/overwrite host files)"))
                continue
            if fn == ".gitmodules":
                findings.append(Finding("medium", "supply-chain", "SUP-SUBMODULE", rp, 0, "",
                                        "Submodules pull code from other repos - audit each"))
            if fn in AUTOEXEC_FILES:
                findings.append(Finding("info", "auto-exec", "AUTO-FILE", rp, 0, "",
                                        "Auto-execution config file present - manual review required"))
            if fn in ("setup.py", "Makefile", "install.sh", "postinstall.sh"):
                findings.append(Finding("medium", "auto-exec", "AUTO-BUILDSCRIPT", rp, 0, "",
                                        "Build/install script - read fully"))
            try:
                size = os.path.getsize(full)
                st_mode = os.stat(full).st_mode
            except OSError:
                continue
            if ext in BINARY_EXT:
                findings.append(Finding("high", "supply-chain", "SUP-BINARY", rp, 0, f"{size} bytes",
                                        "Compiled binary - cannot be reviewed as source"))
                continue
            if size > MAX_FILE_BYTES:
                findings.append(Finding("low", "coverage", "COV-LARGE", rp, 0, f"{size} bytes", "Skipped: too large"))
                continue
            try:
                with open(full, "rb") as fh:
                    raw = fh.read()
            except OSError:
                continue
            if b"\x00" in raw[:8192] or raw[:4] in (b"\x7fELF", b"MZ\x90\x00") or raw[:4] == b"\xcf\xfa\xed\xfe":
                if ext not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".woff", ".woff2", ".ttf", ".otf"}:
                    findings.append(Finding("high", "supply-chain", "SUP-BINARY", rp, 0, f"{size} bytes",
                                            "Binary content in non-media file"))
                continue
            if ext not in TEXT_EXT and not (st_mode & 0o111):
                continue
            if (st_mode & 0o111) and ext in {".md", ".json", ".txt"}:
                findings.append(Finding("low", "filesystem", "FS-EXECDOC", rp, 0, "", "Executable bit on a document"))
            text = raw.decode("utf-8", "replace")
            files_scanned += 1
            scan_text(full, root, text, findings, hosts)
            if fn.upper() == "SKILL.MD" or ext == ".md":
                scan_frontmatter(full, root, text, findings)
            if ext == ".json":
                scan_json_special(full, root, text, findings)

    if not any(os.path.basename(f.file).upper() == "SKILL.MD" for f in findings) and \
       not any(fn.upper() == "SKILL.MD" for _, _, fns in os.walk(root) for fn in fns):
        findings.append(Finding("info", "coverage", "COV-NOSKILL", ".", 0, "", "No SKILL.md found - is this the right path?"))

    # dedupe
    seen, unique = set(), []
    for f in findings:
        key = (f.rule, f.file, f.line)
        if key not in seen:
            seen.add(key)
            unique.append(f)
    unique.sort(key=lambda f: (-SEV_ORDER[f.severity], f.file, f.line))
    return unique, hosts, files_scanned


def safe_extract(archive: str) -> str:
    """Extract a .skill/.zip to a temp dir, refusing path traversal and symlinks (zip-slip)."""
    out = tempfile.mkdtemp(prefix="skillguard-zip-")
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            dest = os.path.realpath(os.path.join(out, info.filename))
            if not dest.startswith(os.path.realpath(out) + os.sep) and dest != os.path.realpath(out):
                print(f"[CRITICAL] ZIP-SLIP: archive entry escapes extraction dir: {info.filename}")
                sys.exit(2)
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                print(f"[HIGH    ] ZIP-SYMLINK: skipped symlink entry {info.filename}")
                continue
            if info.file_size > 50_000_000:
                print(f"[HIGH    ] ZIP-BOMB?: skipped oversized entry {info.filename}")
                continue
            z.extract(info, out)
    print(f"(extracted {archive} -> {out}; delete it after review)")
    return out


def main():
    ap = argparse.ArgumentParser(description="Static security triage for Claude skills/plugins.")
    ap.add_argument("target")
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--min-severity", default="info", choices=list(SEV_ORDER))
    a = ap.parse_args()
    # Evidence often contains the very Unicode tricks being hunted; a cp1252 console would crash mid-report.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if os.path.isfile(a.target) and zipfile.is_zipfile(a.target):
        a.target = safe_extract(a.target)
    if not os.path.isdir(a.target):
        print(f"error: {a.target} is not a directory", file=sys.stderr)
        sys.exit(3)

    findings, hosts, n = scan_tree(a.target)
    shown = [f for f in findings if SEV_ORDER[f.severity] >= SEV_ORDER[a.min_severity]]
    counts = {s: sum(1 for f in findings if f.severity == s) for s in SEV_ORDER}

    print(f"skill-guard scan: {a.target}  ({n} text files)")
    print("counts: " + "  ".join(f"{s}={counts[s]}" for s in reversed(list(SEV_ORDER))))
    print("-" * 100)
    for f in shown:
        loc = f"{f.file}:{f.line}" if f.line else f.file
        print(f"[{f.severity.upper():8}] {f.rule:18} {loc}")
        print(f"           {f.note}")
        if f.evidence:
            print(f"           > {f.evidence}")
    print("-" * 100)
    if hosts:
        print("Network hosts referenced (each must be justified by the skill's purpose):")
        for h, locs in sorted(hosts.items()):
            print(f"  {h:40} {', '.join(locs[:3])}{' ...' if len(locs) > 3 else ''}")
    print("\nTriage only: confirm or dismiss every finding manually before giving a verdict.")

    if a.json_out:
        with open(a.json_out, "w") as fh:
            json.dump({"target": os.path.abspath(a.target), "files_scanned": n, "counts": counts,
                       "hosts": hosts, "findings": [asdict(f) for f in findings]}, fh, indent=2)

    sys.exit(2 if counts["critical"] else 1 if counts["high"] else 0)


if __name__ == "__main__":
    main()
