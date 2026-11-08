---
name: orbit-ui-video-motion
description: "Implement the specific animated dashboard interactions shown in the user's 29-second reference video: KPI counters, staggered activity bar charts, radial progress, modal/toast choreography, timer controls, board movement, member-card FLIP reflow, chart hover tooltip and accent theme transitions. Trigger automatically on UI animation or interactive dashboard work."
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

# Video-derived dashboard motion

Read `.ai/uiux/orbit/VIDEO-REFERENCE-AUDIT.md` and `VIDEO-MOTION-PLAYBOOK.md`. Reference screenshots live in `.ai/uiux/orbit/assets/video-reference/`. **Observed effect != measured implementation:** timing/easing in the playbook are recommended approximations.

For dashboard UI changes, implement the effects that correspond to real UI affordances; don't make decoration-only animations. On startup, animate verified KPI values once, activity bars in coordinated stagger and radial progress based on actual figures. New data: interpolate or replace, never reset to zero each time the component renders. Support cancellation if filters or routes change.

Trigger delegation when appropriate: `orbit-ui-interactive-kanban` for board dragging; `orbit-ui-team-filter-motion` for FLIP; `orbit-ui-analytics-calendar` for point tooltips and calendar transitions; `orbit-ui-personalization` for accent transitions; `orbit-ui-feedback-overlays` for modal, toast and timer.

Quality gate: compare crops to the uploaded reference, record route state before and after, verify pointer, keyboard, reduced-motion, slow network and backend error. Do not claim exact recreation of source code or motion values.


## Keep the references separate

This skill refers specifically to the **29.6s dashboard video**. For the distinct **92s animated explainer**, see `orbit-ui-motion-storytelling`, `orbit-ui-kinetic-type`, `orbit-ui-layered-cards`, `orbit-ui-motion-qa` and `MOTION-ROUTING.md`. Do not treat the explainer's cinematic transitions as default admin UI effects.

## Additional distinct 6s project-management video

Reference D is a separate short 6.175s recording, not the 29s source described above. For its exact progression refer to `PROJECT-WORKSPACE-VIDEO-AUDIT.md` and `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md`; use `orbit-ui-metric-choreography` for reanimating values on period switches and `orbit-ui-workspace-navigation` for persistent app-shell routing.
