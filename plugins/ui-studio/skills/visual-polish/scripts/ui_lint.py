#!/usr/bin/env python3
"""Static Ten-Fixes linter. Counts the things the rules care about in source code.

It reads CSS/SCSS/LESS, HTML, Blade, Vue, Svelte, JSX/TSX and Tailwind class strings.
It cannot see rendered layout: rules 02, 08, 09, 10 are only hinted here; use
dom_probe.js (rendered DOM) or screenshots for those.

Usage:
  ui_lint.py PATH [PATH...] [--json] [--component-scope]
    PATH  file or directory (node_modules, vendor, dist, build are skipped)
    --component-scope  also report per-file counts (one file ≈ one component)
"""
import argparse, colorsys, json, os, re, sys
from collections import Counter, defaultdict

EXTS = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".vue", ".svelte",
        ".jsx", ".tsx", ".js", ".ts", ".php", ".twig", ".erb", ".astro"}
SKIP_DIRS = {"node_modules", "vendor", "dist", "build", ".git", ".next", ".nuxt",
             "coverage", "storage", ".svelte-kit", "public/build"}

TW_TEXT = {"xs": 12, "sm": 14, "base": 16, "lg": 18, "xl": 20, "2xl": 24, "3xl": 30,
           "4xl": 36, "5xl": 48, "6xl": 60, "7xl": 72, "8xl": 96, "9xl": 128}
TW_NEUTRAL = {"gray", "slate", "zinc", "neutral", "stone", "white", "black",
              "transparent", "current", "inherit"}
TW_WEIGHTS = {"thin": 100, "extralight": 200, "light": 300, "normal": 400,
              "medium": 500, "semibold": 600, "bold": 700, "extrabold": 800, "black": 900}
ICON_LIBS = {
    "lucide": r"lucide", "heroicons": r"heroicons", "font-awesome": r"fontawesome|font-awesome|\bfa[srlbd]?\s+fa-|\bfa-[a-z]",
    "material": r"material-icons|material-symbols|@mui/icons|mdi[-:]", "feather": r"feather-icons|react-feather",
    "bootstrap-icons": r"bootstrap-icons|\bbi-[a-z]", "phosphor": r"phosphor", "tabler": r"tabler-icons|@tabler/icons",
    "ionicons": r"ionicons|ion-icon", "react-icons": r"react-icons/", "boxicons": r"boxicons|\bbx[sl]?-",
    "remix": r"remixicon|\bri-[a-z]",
}
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\U0001F1E6-\U0001F1FF]")
NAMED = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "orange": (255, 165, 0),
         "yellow": (255, 255, 0), "green": (0, 128, 0), "blue": (0, 0, 255), "gray": (128, 128, 128),
         "grey": (128, 128, 128), "purple": (128, 0, 128), "pink": (255, 192, 203), "gold": (255, 215, 0),
         "silver": (192, 192, 192), "crimson": (220, 20, 60), "tomato": (255, 99, 71), "navy": (0, 0, 128),
         "teal": (0, 128, 128), "cyan": (0, 255, 255), "magenta": (255, 0, 255), "lime": (0, 255, 0)}


def walk(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for f in files:
                if os.path.splitext(f)[1].lower() in EXTS or f.endswith(".blade.php"):
                    yield os.path.join(root, f)


def to_px(v):
    v = v.strip().lower()
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem|em)?", v)
    if not m:
        return None
    n = float(m.group(1))
    return round(n * 16, 2) if m.group(2) in ("rem", "em") else round(n, 2)


def parse_color(v, vars_):
    v = v.strip().lower()
    vm = re.fullmatch(r"var\((--[\w-]+)(?:,\s*([^)]+))?\)", v)
    if vm:
        v = vars_.get(vm.group(1), vm.group(2) or "")
        v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + ((int(h[6:8], 16) / 255) if len(h) == 8 else 1.0,)
    m = re.fullmatch(r"rgba?\(([^)]+)\)", v)
    if m:
        parts = [p for p in re.split(r"[,\s/]+", m.group(1)) if p]
        try:
            r, g, b = (float(p.rstrip("%")) for p in parts[:3])
            a = float(parts[3]) if len(parts) > 3 and not parts[3].endswith("%") else 1.0
            return (r, g, b, a)
        except ValueError:
            return None
    m = re.fullmatch(r"hsla?\(([^)]+)\)", v)
    if m:
        parts = [p for p in re.split(r"[,\s/]+", m.group(1)) if p]
        try:
            h = float(parts[0].replace("deg", "")) / 360
            s, l = float(parts[1].rstrip("%")) / 100, float(parts[2].rstrip("%")) / 100
            r, g, b = colorsys.hls_to_rgb(h, l, s)
            return (r * 255, g * 255, b * 255, 1.0)
        except (ValueError, IndexError):
            return None
    if v in NAMED:
        return NAMED[v] + (1.0,)
    return None


def hue_family(rgb):
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb[:3]))
    if s < 0.25 or l < 0.08 or l > 0.95:
        return None  # neutral
    deg = h * 360
    for name, hi in (("red", 15), ("orange", 45), ("yellow", 70), ("green", 160), ("cyan", 195),
                     ("blue", 255), ("purple", 290), ("pink", 345), ("red", 361)):
        if deg < hi:
            return name
    return "red"


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def contrast(fg, bg):
    if bg[3] < 1:
        bg = tuple(bg[i] * bg[3] for i in range(3)) + (1.0,)
    if fg[3] < 1:
        fg = tuple(fg[i] * fg[3] + bg[i] * (1 - fg[3]) for i in range(3)) + (1.0,)
    a, b = sorted((lum(fg), lum(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


class Stats:
    def __init__(self):
        self.font_sizes = Counter(); self.spacing = Counter(); self.off_grid = []
        self.decor = defaultdict(list); self.families = Counter(); self.weights = Counter()
        self.text_hues = Counter(); self.hue_locs = defaultdict(list)
        self.icon_libs = Counter(); self.emoji = []; self.icon_sizes = Counter()
        self.aligns = Counter(); self.indents = []; self.contrast = []
        self.radii = Counter(); self.range_text = []
        self.text_colors = []; self.backgrounds = []

    def merge(self, o):
        for k, v in vars(o).items():
            mine = getattr(self, k)
            if isinstance(v, Counter):
                mine.update(v)
            elif isinstance(v, defaultdict):
                for kk, vv in v.items():
                    mine[kk].extend(vv)
            else:
                mine.extend(v)


CSS_DECL = re.compile(r"([a-z-]+)\s*:\s*([^;{}]+)")
CSS_BLOCK = re.compile(r"([^{}]+)\{([^{}]*)\}")
CLASS_ATTR = re.compile(r"""\b(?:class|className|:class)\s*=\s*(?:"([^"]*)"|'([^']*)'|\{`([^`]*)`\})""")
RANGE_TEXT = re.compile(r"\d+\s*°?\s*[–—-]\s*\d+\s*°")


def scan(path, text, vars_):
    s = Stats()
    lines = text.splitlines()

    def loc(idx):
        return f"{path}:{text.count(chr(10), 0, idx) + 1}"

    # CSS declarations (also catches inline style="" and <style> blocks)
    for blk in CSS_BLOCK.finditer(text):
        decls = {}
        for d in CSS_DECL.finditer(blk.group(2)):
            prop, val = d.group(1), d.group(2).strip()
            decls[prop] = val
            where = loc(blk.start(2) + d.start())
            handle_decl(s, prop, val, where, vars_)
        fg = parse_color(decls.get("color", ""), vars_) if "color" in decls else None
        bgv = decls.get("background-color") or decls.get("background")
        bg = parse_color(bgv, vars_) if bgv else None
        if fg and bg:
            s.contrast.append((round(contrast(fg, bg), 2), decls["color"], bgv, loc(blk.start())))
    for m in re.finditer(r'style\s*=\s*"([^"]*)"', text):
        for d in CSS_DECL.finditer(m.group(1)):
            handle_decl(s, d.group(1), d.group(2).strip(), loc(m.start()), vars_)

    # Tailwind / utility classes
    for m in CLASS_ATTR.finditer(text):
        cls = (m.group(1) or m.group(2) or m.group(3) or "").split()
        where = loc(m.start())
        for c in cls:
            handle_tw(s, c.split(":")[-1], where)

    # Icons
    for name, pat in ICON_LIBS.items():
        if re.search(pat, text, re.I):
            s.icon_libs[name] += 1
    if re.search(r"<svg\b", text) and not s.icon_libs:
        s.icon_libs["inline-svg"] += 1
    for m in re.finditer(r"<(?:[A-Z]\w*Icon|[A-Z]\w*|svg|i|ion-icon)\b[^>]*>", text):
        tag = m.group(0)
        for sm in re.finditer(r"\b(?:size|width|height)\s*=\s*[\"'{]?\s*(\d+)", tag):
            if int(sm.group(1)) > 0:
                s.icon_sizes[int(sm.group(1))] += 1
        for sm in re.finditer(r"\b(?:size|w|h)-(\d+(?:\.\d)?)\b", tag):
            s.icon_sizes[float(sm.group(1)) * 4] += 1
    for i, ln in enumerate(lines, 1):
        if EMOJI.search(ln) and not ln.strip().startswith(("//", "#", "*", "<!--")):
            s.emoji.append(f"{path}:{i}")
        if RANGE_TEXT.search(ln):
            s.range_text.append(f"{path}:{i}")
    return s


def resolve(val, vars_, depth=0):
    """Substitute var(--x[, fallback]) using variables found in the scanned files."""
    if depth > 5 or "var(" not in val:
        return val
    def sub(m):
        return vars_.get(m.group(1), m.group(2) or "")
    return resolve(re.sub(r"var\((--[\w-]+)(?:,\s*([^()]+))?\)", sub, val), vars_, depth + 1)


def handle_decl(s, prop, val, where, vars_):
    if prop.startswith("--"):
        return  # token definitions are the palette, not usage
    val = resolve(val, vars_)
    if prop == "font-size":
        px = to_px(val)
        if px:
            s.font_sizes[px] += 1
    elif prop in ("margin", "padding", "gap", "row-gap", "column-gap") or re.fullmatch(r"(margin|padding)-(top|right|bottom|left|inline|block)(-start|-end)?", prop):
        for tok in val.split():
            px = to_px(tok)
            if px is not None and px > 0:
                s.spacing[px] += 1
                if px % 4 and px > 2:
                    s.off_grid.append(f"{where} ({prop}: {val})")
        if prop in ("margin-left", "padding-left", "margin-inline-start"):
            s.indents.append(f"{where} ({prop}: {val})")
    elif prop == "text-transform" and "uppercase" in val:
        s.decor["uppercase"].append(where)
    elif prop == "font-style" and "italic" in val:
        s.decor["italic"].append(where)
    elif prop.startswith("text-decoration") and "underline" in val:
        s.decor["underline"].append(where)
    elif prop == "letter-spacing":
        px = to_px(val.replace("em", "")) if val.endswith("em") else to_px(val)
        if val.endswith("em") and float(re.sub(r"[^\d.\-]", "", val) or 0) >= 0.05:
            s.decor["wide-tracking"].append(where)
    elif prop == "font-family":
        s.families[val.split(",")[0].strip("'\" ").lower()] += 1
    elif prop == "font-weight":
        w = {"normal": "400", "bold": "700"}.get(val, val)
        s.weights[w] += 1
    elif prop == "color":
        c = parse_color(val, vars_)
        fam = hue_family(c) if c else None
        if fam:
            s.text_hues[fam] += 1; s.hue_locs[fam].append(where)
        if c:
            s.text_colors.append((val, c, where))
    elif prop in ("background", "background-color"):
        c = parse_color(val.split()[0] if not val.startswith(("rgb", "hsl")) else val, vars_)
        if c and c[3] == 1:
            s.backgrounds.append(c)
    elif prop == "text-align":
        s.aligns[val] += 1
    elif prop == "border-radius":
        px = to_px(val.split()[0]) if val.split() else None
        if px and px < 999:
            s.radii[px] += 1


def handle_tw(s, c, where):
    neg = c.startswith("-"); c = c.lstrip("-")
    m = re.fullmatch(r"text-(xs|sm|base|lg|[2-9]?xl)", c)
    if m:
        s.font_sizes[TW_TEXT[m.group(1)]] += 1; return
    m = re.fullmatch(r"text-\[(\d+\.?\d*(?:px|rem))\]", c)
    if m:
        s.font_sizes[to_px(m.group(1))] += 1; return
    m = re.fullmatch(r"(?:p|px|py|pt|pr|pb|pl|ps|pe|m|mx|my|mt|mr|mb|ml|ms|me|gap|gap-x|gap-y|space-x|space-y)-(\d+\.?\d*|\[[^\]]+\])", c)
    if m:
        v = m.group(1)
        px = to_px(v[1:-1]) if v.startswith("[") else float(v) * 4
        if px:
            s.spacing[px] += 1
            if px % 4 and px > 2:
                s.off_grid.append(f"{where} ({c})")
        if c.startswith(("pl-", "ml-", "ps-", "ms-")):
            s.indents.append(f"{where} ({c})")
        return
    if c in ("uppercase", "italic", "underline"):
        s.decor[c].append(where); return
    if c in ("tracking-wide", "tracking-wider", "tracking-widest"):
        s.decor["wide-tracking"].append(where); return
    m = re.fullmatch(r"font-(" + "|".join(TW_WEIGHTS) + ")", c)
    if m:
        s.weights[str(TW_WEIGHTS[m.group(1)])] += 1; return
    m = re.fullmatch(r"font-(sans|serif|mono|\[[^\]]+\])", c)
    if m:
        s.families[m.group(1)] += 1; return
    m = re.fullmatch(r"text-([a-z]+)(?:-(\d{2,3}))?(?:/\d+)?", c)
    if m and m.group(1) not in TW_TEXT and m.group(1) not in ("left", "right", "center", "justify", "start", "end", "wrap", "nowrap", "balance", "pretty", "clip", "ellipsis"):
        fam = m.group(1)
        if fam not in TW_NEUTRAL:
            s.text_hues[fam] += 1; s.hue_locs[fam].append(where)
        return
    m = re.fullmatch(r"text-(left|right|center|justify|start|end)", c)
    if m:
        s.aligns[m.group(1)] += 1; return
    m = re.fullmatch(r"rounded(?:-(none|sm|md|lg|xl|2xl|3xl|full))?", c)
    if m:
        s.radii[{"none": 0, "sm": 2, None: 4, "md": 6, "lg": 8, "xl": 12, "2xl": 16, "3xl": 24, "full": 0}[m.group(1)]] += 1


def grade(n, ok, warn):
    return "pass" if n <= ok else ("warn" if n <= warn else "fail")


def report(s, files):
    sizes = sorted(s.font_sizes)
    body = sorted(s.font_sizes.items(), key=lambda kv: -kv[1])[0][0] if s.font_sizes else None
    hero = max(sizes) if sizes else None
    ratio = round(hero / body, 2) if hero and body else None
    decor_kinds = [k for k, v in s.decor.items() if v]
    if s.backgrounds:
        # Approximate: text colours declared without a background are checked against
        # the darkest and lightest opaque backgrounds found (static can't know nesting).
        dark = min(s.backgrounds, key=lum); light = max(s.backgrounds, key=lum)
        paired = {c[3] for c in s.contrast}
        for val, col, where in s.text_colors:
            if where in paired:
                continue
            bg = dark if lum(col[:3] + (1,)) > 0.18 else light
            s.contrast.append((round(contrast(col, bg), 2), val, "~" + "#%02x%02x%02x" % tuple(int(v) for v in bg[:3]), where))
    seen = set(); uniq = []
    for c in s.contrast:
        if (c[1], c[2]) not in seen:
            seen.add((c[1], c[2])); uniq.append(c)
    s.contrast = uniq
    low = sorted([c for c in s.contrast if c[0] < 4.5])
    icon_lib_n = len([k for k in s.icon_libs if k != "inline-svg"]) + (1 if s.emoji else 0)
    weights = len(s.weights)
    rules = [
        ("01 Hierarchy", f"hero/body = {hero}/{body}px = {ratio}x; {len(sizes)} sizes",
         "n/a" if ratio is None else ("fail" if ratio < 2 else "warn" if ratio < 3 or len(sizes) > 4 else "pass")),
        ("02 Alignment", f"{len(s.aligns)} text-align values {dict(s.aligns)}; {len(s.indents)} child-level left offsets",
         "warn" if s.indents or len(s.aligns) >= 3 else "manual"),
        ("03 Spacing", f"{len(s.spacing)} distinct values {sorted(s.spacing)[:12]}; {len(s.off_grid)} off-grid",
         grade(len(s.spacing), 4, 5) if not s.off_grid else ("fail" if len(s.spacing) > 5 else "warn")),
        ("04 Text style", f"decorations: {', '.join(f'{k}×{len(s.decor[k])}' for k in decor_kinds) or 'none'}; "
                          f"{len(s.families)} families; {weights} weights",
         "fail" if len(decor_kinds) >= 2 or len(s.families) > 2 or weights > 4
         else "warn" if decor_kinds or weights > 3 else "pass"),  # up to two families is fine (ui-studio T5)
        ("05 Colour", f"{len(s.text_hues)} text hues {dict(s.text_hues)}", grade(len(s.text_hues), 1, 2)),
        ("06 Contrast", f"{len(s.contrast)} fg/bg pairs checked, {len(low)} below 4.5:1"
                        + (f"; worst {low[0][0]}:1 ({low[0][1]} on {low[0][2]})" if low else ""),
         "manual" if not s.contrast else ("fail" if low else "pass")),
        ("07 Icons", f"libraries {sorted(s.icon_libs)}; emoji ×{len(s.emoji)}; {len(s.icon_sizes)} icon sizes {sorted(s.icon_sizes)}",
         "fail" if icon_lib_n > 1 or s.emoji or len(s.icon_sizes) > 3 else "warn" if len(s.icon_sizes) > 2 else
         ("pass" if s.icon_libs else "n/a")),
        ("08 Grouping", f"{len(s.radii)} radius values {sorted(s.radii)}", "manual" if len(s.radii) <= 2 else "warn"),
        ("09 Show, don't list", f"{len(s.range_text)} text ranges (e.g. 17°–28°)", "warn" if len(s.range_text) >= 3 else "manual"),
        ("10 Make it alive", "needs rendered review", "manual"),
    ]
    details = {
        "off_grid_spacing": list(dict.fromkeys(s.off_grid))[:20], "decorations": {k: v[:10] for k, v in s.decor.items()},
        "accent_hue_locations": {k: v[:8] for k, v in s.hue_locs.items()}, "low_contrast": low[:15],
        "emoji_icons": s.emoji[:10], "left_offsets": s.indents[:15], "text_ranges": s.range_text[:10],
        "font_sizes": dict(sorted(s.font_sizes.items())), "spacing": dict(sorted(s.spacing.items())),
    }
    return {"files_scanned": files, "rules": [{"rule": r, "metric": m, "verdict": v} for r, m, v in rules], "details": details}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--component-scope", action="store_true")
    a = ap.parse_args()
    files = list(walk(a.paths))
    texts = {}
    vars_ = {}
    for f in files:
        try:
            texts[f] = open(f, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;}]+)", texts[f]):
            vars_.setdefault(m.group(1), m.group(2).strip())
    total = Stats(); per = {}
    for f, t in texts.items():
        st = scan(f, t, vars_)
        total.merge(st)
        if a.component_scope:
            per[f] = report(st, 1)["rules"]
    out = report(total, len(texts))
    if a.component_scope:
        out["per_file"] = per
    if a.json:
        print(json.dumps(out, indent=2, default=str)); return
    print(f"# Ten Fixes static lint — {len(texts)} files\n")
    print("| Rule | Metric | Verdict |\n|---|---|---|")
    for r in out["rules"]:
        print(f"| {r['rule']} | {r['metric']} | {r['verdict']} |")
    d = out["details"]
    print("\n## Evidence")
    for k in ("low_contrast", "off_grid_spacing", "decorations", "accent_hue_locations", "left_offsets", "emoji_icons", "text_ranges"):
        if d[k]:
            print(f"\n**{k}**")
            items = d[k].items() if isinstance(d[k], dict) else enumerate(d[k])
            for kk, vv in items:
                print(f"- {vv if isinstance(kk, int) else f'{kk}: {vv}'}")
    if a.component_scope:
        print("\n## Per file")
        for f, rules in per.items():
            bad = [f"{r['rule'][:2]}:{r['verdict']}" for r in rules if r["verdict"] in ("warn", "fail")]
            if bad:
                print(f"- {f}: {', '.join(bad)}")
    print("\n_Static scan only. Confirm 02, 08, 09, 10 and real-background contrast with dom_probe.js or a screenshot._")


if __name__ == "__main__":
    main()
