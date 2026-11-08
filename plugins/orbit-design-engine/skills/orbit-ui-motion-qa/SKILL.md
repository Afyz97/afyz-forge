---
name: orbit-ui-motion-qa
description: "Verify fidelity of UI animation and video-inspired motion, not just static screenshots: measure before/during/after states, screen-record transitions, test reduced motion, accessibility, layout shifts and motion continuity against reference frames."
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

# Motion fidelity QA — video and real interactions

Read `references/EDITORIAL-MOTION-PLAYBOOK.md`, `references/EDITORIAL-VIDEO-OBSERVATIONS.md`, and existing `VIDEO-MOTION-PLAYBOOK.md`, `VIDEO-VISUAL-QA.md` when relevant. Use only the reference relevant to the task. See sequence strips in `assets/editorial-video-reference/`.

## Checklist for each motion (required output)

1. **Trigger:** load, click, hover, scroll, completion, filter, validation. Avoid trigger on every rerender.
2. **Frames:** capture at start, ~25%, ~50%, ~75%, complete; capture after rapid repeat and cancellation. Check enter AND exit, opacity, rotation, elevation, clipping, collisions and stable final layout. Compare relevant reference timestamps.
3. **State truth:** real value/content before and after, no fabricated backend state, no phantom consent or fake checklist completion.
4. **A11y:** keyboard, focus trap/return, screen reader status, `prefers-reduced-motion`, touch, high text scaling, no flashing; no animation if user has chosen to reduce motion.
5. **Performance:** no noticeable frame stutter, watch long tasks/paint, memory leaks; prefer compositor-friendly transform/opacity. Check low-end mobile and network latency.
6. **Reproduction quality:** preserve visual hierarchy, scene progression, depth, headline emphasis, overlay anchoring and timing *feel*, not a numerical similarity score fabricated from screenshots.

For each page record `observed reference`, `implementation`, `verified by screen recording yes/no`, `mismatch`, `action`. If browser/recording tools unavailable, state that timing and interactivity couldn't be verified rather than claiming visual fidelity. Do not claim exact source easing.

## Reference D motion-sequence checks

Use `PROJECT-WORKSPACE-VISUAL-QA.md` for 6-second clip: count-up/bar midpoint, Tasks page transition and card arrival, Analytics range change and cancelling in-flight numeric tweens, Settings entry. Compare frame strips; report test evidence honestly.

## Reference E auth QA

For login/signup wipe, read `AUTH-VISUAL-QA.md` and capture the **25%, 50%, 75%** visual states of each direction (start and end alone cannot verify the diagonal). Verify hidden-form inert/focus, click-spam lock, mobile and reduced motion; never claim user accounts were actually created without backend evidence.
