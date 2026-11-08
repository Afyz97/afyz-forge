---
name: orbit-ui-layered-cards
description: "Implement animated 2.5D miniature app cards, floating browser windows, document overlays, permission highlights, line drawings, stacked paper and soft shadows based on the uploaded animated checklist video."
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

# Layered-card motion and annotated UI illusions

Use for product demos, onboarding, explainers, optional empty states and tightly scoped dashboard emphasis. Read `EDITORIAL-MOTION-PLAYBOOK.md`; inspect stills 03s, 06s, 08s, 24s, 28s, 34s, 63s and 69s.

- Canvas: central dominant rounded theme-surface window (browser-dot header, small realistic components, no unreadable faux controls if presented as interactive) over soft gradient bloom, optionally a fanned document card. Background stays calm.
- Choreography: main window scale(.94→1) + translateY(30→0) + opacity, 380–620ms; paper foreground enters 70–130ms later with rotation -5/+6 degrees, soft shadow and a single settling overshoot. Focus cue enters last.
- Diagram: node grouping → line connection draws → active node gains ring; represent *real* data relationships and avoid false security claims.
- UI state transformation: preserve card geometry while internals switch; avoid flashing whole scene to blank. Tooltips/callouts should be anchored to actual targets.
- Production-app adaptation: use one light modal/drawer transition and true inputs/buttons with accessible focus. Do not apply decorative perspective to actionable forms or move submit targets under the pointer.
- Performance: wrapper `transform/opacity`, avoid heavy per-frame box-shadow/large blur; cap overlapping surfaces; test 360px, long strings and reduced motion.

Deliver a reusable `IllustrationCard` composition with variants `browser`, `document`, `dialog`, `flow-node`, `audit-callout` and states `idle`, `entering`, `active`, `resolved`. Make sure noninteractive demos are labelled illustrations.
