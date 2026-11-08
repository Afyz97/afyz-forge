---
name: orbit-ui-interactive-kanban
description: "Design and implement a compact the enterprise reference/video-inspired drag-and-drop kanban task board: columns, task cards, priority labels, counts, animated drop placement, keyboard DnD and reliable saved status changes. Use for task/project/approval/workflow boards."
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

# Task board: smooth, real drag and drop

Video evidence: `assets/video-reference/09-kanban-board.jpg` and `11-kanban-drop.jpg`; read `VIDEO-UX-PATTERNS.md`, `VIDEO-MOTION-PLAYBOOK.md`.

Layout: 4-step configurable pipeline, concise lane headers with live counts, small theme-surface task cards with category/status/priority chips, limited metadata, assigned avatar and an action menu. Preserve project's actual workflow statuses and role rules; do not invent task status columns.

Interactions: pointer drag with clear handle/affordance; card lift ~2–4 px, target-lane highlight, insertion placeholder and smooth settle; update column counts only after actual state change. Touch and keyboard support required: focus card, initiate move, select lane/position, commit/cancel; announce result with aria-live. Moving a card is an actual backend action; handle server rejection by restoring previous location and displaying a useful error. Re-fetch invalidates stale optimistic positions safely. Keep ordering stable on filters/search and concurrent changes; don't animate full board on each update.

Implement using existing React/Laravel Blade/Livewire/Alpine and its drag library if any; introduce dependency only with project approval. Test multiple rapid moves, cancel, drop into empty lane, item counts, stale edit, mobile scrolling, permission denial and reduced motion. Always preserve accessible non-drag move control.
