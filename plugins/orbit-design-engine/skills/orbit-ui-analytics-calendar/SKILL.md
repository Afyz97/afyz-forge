---
name: orbit-ui-analytics-calendar
description: "Implement interactive dashboard analytics and calendar views from uploaded video: theme-based line/area trends, comparison series, crosshair/tooltips, summary cards, month view event pills, right-side day agenda, and animated date/view transitions."
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

# Analytics and calendar interactions

Video evidence: `19-analytics-overview.jpg`, `21-analytics-tooltip.jpg`, `16-calendar.jpg` in `.ai/uiux/orbit/assets/video-reference/`. Read `VIDEO-REFERENCE-AUDIT.md`, `VIDEO-UX-PATTERNS.md`, `VIDEO-MOTION-PLAYBOOK.md`.

Analytics: summary KPIs up top and a spacious, thin line/area chart using the host chart palette; dashed comparison series and actual labels; right-side circular distribution/progress chart if data demands. Pointer hover + keyboard focus reveals a vertical crosshair and floating tooltip at the point, with date and exact numbers. Use chart component's native tooltips/hit-testing, not a manually positioned fake chart. Range changes preserve truthful axis/domain comparisons, cancel old animations, and support empty/error/loading and export/data table view.

Calendar: month grid with small coloured event bars and a connected right-hand agenda/selected-day rail. Header gives next/previous, month selector, and view controls as appropriate. Date change updates agenda and preserves selected state. Use short controlled fade/slide transitions, never animate date content before actual data arrives. Correct timezone, multi-day and overlapping events, screen-reader date labels, arrow-key navigation and small-screen agenda/list fallback are mandatory. Only implement calendar or analytics where project domain calls for them.

## Reference D additional date-range motion

The short video shows period selectors and multiple KPI counts changing while fine theme-aligned sparklines update. Read `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` for interruption-safe period transitions and truthfully synchronized chart+number; review `sequence-analytics.jpg`.
