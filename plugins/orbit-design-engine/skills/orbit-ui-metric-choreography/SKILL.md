---
name: orbit-ui-metric-choreography
description: "Create truthful animated dashboard KPI counters, staggered bar entrances, theme-aligned sparklines and date-range data transitions with cleanup and reduced-motion handling as seen in the user-provided workspace video."
---

## Resource lookup (marketplace and standalone installs)

Resolve bundled resources relative to this `SKILL.md`, not the working directory.
If `../../.claude-plugin/plugin.json` or `../../.codex-plugin/plugin.json` exists,
this skill is inside the plugin: use `../../references/` for guide files and
`../../assets/`, `../../examples/`, `../../scripts/` for those resource folders.
In the instructions and bundled guides below, `.ai/uiux/orbit/` and
`~/.ai/uiux/orbit/` are legacy resource aliases: map guide paths to
`../../references/` and `assets/`, `examples/`, `scripts/` paths to the plugin root.
Bare guide filenames also resolve under `../../references/`.
For standalone installs without a plugin manifest, use the project's
`.ai/uiux/orbit/`, then `~/.ai/uiux/orbit/`, as described below.
Write new measurements, screenshots and other task output into the current
project's `.ai/uiux/orbit/reference/`; never write into the installed plugin.

## Mandatory: inherit the host application's theme

- **Never prescribe, introduce, replace, or hardcode any hue, palette, HEX/RGB/HSL value, theme preset, or brand/accent colour.** This rule overrides reference screenshots, reference videos, example CSS, and suggestions elsewhere in this package.
- Before editing UI, discover the application's **existing** theme provider, CSS variables, framework tokens, organization/tenant branding and light/dark modes. Use those settings as the single source of truth for backgrounds, surfaces, text, borders, interactive elements, chart series, focus rings, statuses and motion overlays.
- Preserve the current system's colours exactly unless the user **explicitly** requests a colour change. Do not introduce fallback branded palettes. If the theme exposes no suitable semantic token, reuse an existing styled component or ask for token mapping; do not invent a value.
- For motion and visual reference matching, transfer **structure, hierarchy, spacing, typography, geometry, transitions, timing and interaction behaviour**; map every visual treatment onto current project theme roles instead of copying the reference palette.
- Prefer host semantic components or computed theme tokens. Never overwrite the application's theme variables with example defaults. Ensure theme switching, tenant branding, and accessibility remain intact.

# Metric choreography and range-change motion

Use for KPI cards, analytics, chart widgets and range filters. Read `.ai/uiux/orbit/PROJECT-WORKSPACE-VIDEO-AUDIT.md`, `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` and `PROJECT-WORKSPACE-VISUAL-QA.md`; user-global fallback `~/.ai/uiux/orbit/`.

## Observed reference
At ~0–0.6s dashboard counters step from small to final values with nearby vertical bar entrances. At ~3.3–4.7s Analytics values rise while miniature area lines remain visible and selected period changes. The clip is a fast edited recording, **not a timing specification**. Inspect `sequence-counter.jpg` and `sequence-analytics.jpg`.

## Requirements
- Start from correct target data; do not invent KPI values or persist sample values `24/10/12/2`.
- Format counter values with locale (integers, decimals, percent, currency, duration), preserve accessible final value (`aria-label`/offscreen) without updating screen reader 60 times/sec.
- Trigger on initial meaningful load or changed data period, not on every rerender/scroll/layout event; hide no information from reduced-motion users.
- Use `requestAnimationFrame` or existing motion/chart API; cancel on component unmount and new data; allow instant settlement when tab backgrounded or reduced-motion preference changes.
- Key analytics render to the same selected period/version as data and export. On 30D→90D changes, suppress stale responses and synchronize numeric + chart state; interpolate from previous **comparable** value or reveal final target directly.
- Render bar baseline and fixed geometry first; animate actual bar data to target 320–600ms in restrained stagger. Sparkline uses real series, not random SVG path.
- Empty/error/loading states are real; never show fake zero totals during pending API response.

## QA
Compare initial, progress, final frames and range switches, including interruption. Exercise empty/zero/negative/large numbers and mixed unit formats, back/forward, backend latency, reduced motion, CPU throttle, screen readers.
