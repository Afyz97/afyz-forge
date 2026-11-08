---
name: orbit-ui-dashboards
description: "Build reference-inspired action-oriented dashboards and analytics views with interactive charts, KPI cards, breakdowns, pending decisions, data drilldowns and smooth data transitions. Not for a dashboard with no reference to match — use ui-studio's ui-visual-direction."
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

Read `THEME-INHERITANCE.md` before making any colour-bearing CSS or styling changes.

When a referenced `.ai/uiux/orbit/` file is absent from the repository, check the user-wide installation at `~/.ai/uiux/orbit/`.

# the enterprise reference dashboard and analytics language

Read `.ai/uiux/orbit/DESIGN-SPEC.md`, `MOTION-SPEC.md` and `REFERENCE-BRIEF.md`.

## Build a task-centred dashboard
- Opening viewport answers: what is happening, what changed, what needs attention and what can I do now?
- Structure: compact page context and filters -> multi-column KPI cards -> primary analytical visual and urgent/decision queue -> detailed chart/table/activity area.
- Charts must have meaningful axes, range labels, units, legends and accessible data alternative. Switching 7d/12w/12m is a *reference example*, not mandatory if data doesn't support it.
- Drilldown links and filters operate on real dataset and route to meaningful details. Avoid unrelated decorative metric cards.
- Charts and summary cards should align to underlying page grid and tokens. Dense data with breathing room, not oversized empty shapes.

## Motion
Stagger the first 3–6 cards discreetly; animate range switch 250–550ms only when it preserves interpretability. Prefer shape/opacity continuity and honest baselines. Pause/cancel animations on rapid data changes.

## Guardrails
Never fabricate production values, use counts of unpublished/private items beyond permissions or display a successful action before server confirmation. Place financial status, amounts and timeframes in explicit labels and maintain currency/locale formats.

## Verify
At least one populated dashboard, an empty/loading state, time-filter change, chart keyboard interpretation and a mobile layout. Report tests and reference fidelity separately.

## Reference video dashboard enhancements

Read `VIDEO-REFERENCE-AUDIT.md`, `VIDEO-UX-PATTERNS.md` and `VIDEO-MOTION-PLAYBOOK.md`. The user's video dashboard has a distinct first filled KPI card, three quiet KPIs, animated vertical bars with neutral hatch slots, reminder CTA, live project list, team status chips, radial progress gauge and a dark tabular timer. Match the hierarchy and interactions with **actual project data**, not the recorded brand/data. Reference stills: `02-dashboard-stable.jpg`, `05-timer-controls.jpg`, `19-analytics-overview.jpg`. Coordinate with `orbit-ui-video-motion`.

## 6-second workspace reference (v6)

For a compact project or operational dashboard, check `assets/project-workspace-reference/sequence-counter.jpg` and `PROJECT-WORKSPACE-VIDEO-AUDIT.md`. One prominent KPI and three quieter cards start with count-up, while related activity bars grow below. New period charts reanimate to real targets, not sample numbers. Use `orbit-ui-metric-choreography` and `orbit-ui-project-workspaces` only where domain appropriate.
