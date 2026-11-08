#!/usr/bin/env python3
"""WCAG 2.x contrast checker for Rule 06 (readable grey).

Usage:
  contrast.py FG BG                      # ratio + verdict
  contrast.py FG BG --suggest [--target 7]  # nearest colour (same hue) that meets target
  contrast.py FG BG --alpha 0.6          # FG drawn at opacity over BG

Colours: #rgb, #rrggbb, #rrggbbaa, rgb(r,g,b), rgba(r,g,b,a).
"""
import argparse, colorsys, json, re, sys


def parse(c):
    c = c.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return (r, g, b, a)
    m = re.fullmatch(r"rgba?\(([^)]+)\)", c)
    if m:
        parts = [p.strip() for p in re.split(r"[,\s/]+", m.group(1)) if p.strip()]
        r, g, b = (float(p) for p in parts[:3])
        a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1) if len(parts) > 3 else 1.0
        return (r, g, b, a)
    raise ValueError(f"Unrecognised colour: {c}")


def blend(fg, bg):
    a = fg[3]
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1.0,)


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in c[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    if bg[3] < 1:
        bg = blend(bg, (0, 0, 0, 1))  # assume dark page behind translucent bg
    if fg[3] < 1:
        fg = blend(fg, bg)
    l1, l2 = sorted((lum(fg), lum(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05), fg, bg


def hexify(c):
    return "#" + "".join(f"{round(max(0, min(255, v))):02x}" for v in c[:3])


def suggest(fg, bg, target):
    """Move lightness of fg (keeping hue/sat) away from bg until target is met."""
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in fg[:3]))
    lighter = lum(bg) < 0.18
    step = 0.005 if lighter else -0.005
    while 0 <= l <= 1:
        cand = tuple(v * 255 for v in colorsys.hls_to_rgb(h, l, s)) + (1.0,)
        if ratio(cand, bg)[0] >= target:
            return cand
        l += step
    return (255, 255, 255, 1) if lighter else (0, 0, 0, 1)


def verdict(r, large=False):
    floor = 3.0 if large else 4.5
    if r < floor:
        return "fail"
    return "pass" if r >= 7 or large else "pass (aim ~7:1 for small secondary text)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fg"); ap.add_argument("bg")
    ap.add_argument("--alpha", type=float, help="opacity applied to fg")
    ap.add_argument("--large", action="store_true", help=">=24px or >=18.66px bold")
    ap.add_argument("--suggest", action="store_true")
    ap.add_argument("--target", type=float, default=7.0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    fg, bg = parse(a.fg), parse(a.bg)
    if a.alpha is not None:
        fg = fg[:3] + (a.alpha,)
    r, efg, ebg = ratio(fg, bg)
    out = {"fg": a.fg, "bg": a.bg, "effective_fg": hexify(efg), "effective_bg": hexify(ebg),
           "ratio": round(r, 2), "verdict": verdict(r, a.large)}
    if a.suggest:
        s = suggest(efg, ebg, a.target)
        out["suggestion"] = {"color": hexify(s), "ratio": round(ratio(s, ebg)[0], 2), "target": a.target}
    if a.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"{out['effective_fg']} on {out['effective_bg']}: {out['ratio']}:1  -> {out['verdict']}")
        if a.suggest:
            sg = out["suggestion"]
            print(f"suggest {sg['color']} ({sg['ratio']}:1, target {sg['target']}:1)")
    sys.exit(0 if r >= (3.0 if a.large else 4.5) else 1)


if __name__ == "__main__":
    main()
