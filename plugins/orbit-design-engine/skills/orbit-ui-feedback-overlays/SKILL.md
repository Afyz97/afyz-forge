---
name: orbit-ui-feedback-overlays
description: "Implement polished functional motion for small create/edit modal dialogs, contextual right drawers, genuine success/error toast feedback, and video-style time tracker panels with precise elapsed timers and pause/stop states."
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

# Modal, drawer, toast and timer

Video evidence: `assets/video-reference/03-add-project-modal.jpg`, `05-timer-controls.jpg`, `14-team-filtered.jpg` (side member drawer appears during sequence); read `VIDEO-MOTION-PLAYBOOK.md`.

**Modal:** compact centred surface; foreground sharp against dimmed page; 160–260ms opacity/translate reveal, accessible labelled inputs, focus trap, ESC/cancel, submit disabled/pending state and validation. On submit, mutate authoritative app state first; only then close and display a bottom snackbar/toast of *real* success. On error, stay open and explain what failed. No misleading celebratory feedback.

**Side drawer:** anchored to right with slim rounded corners, 210–320ms horizontal motion; retain context (filter/search/scroll), focus restoration, ARIA dialog or region semantics per implementation, explicit close.

**Timer:** theme-emphasis panel with subtle concentric line texture, large tabular numerals `hh:mm:ss`, legible play/pause and clearly distinguished destructive stop. Time is derived from time origin/elapsed milliseconds, not an incrementing counter susceptible to tab throttling. Play/pause/stop functional, cross-device/session persistence as product requires; confirmations for destructive stop where warranted. Keep controls discoverable to keyboard and touch users.

Test slow network, abort/retry, queued toast announcements, screen-reader messaging, repeated open/close, offscreen focus, elapsed time after browser tab suspension, and reduced motion.
