---
name: orbit-ui-visual-qa
description: "Perform screenshot comparison and UI/UX quality gate to verify a redesigned application looks close to the original enterprise sample and functions correctly across screens, themes and motion states. Not for a critique with no reference to compare — use ui-studio's ui-critique."
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

# the enterprise reference visual QA and fidelity scorecard

Read `.ai/uiux/orbit/VISUAL-QA.md`, `REFERENCE-BRIEF.md` and any real screenshot/measurement evidence.

1. Prepare comparable screenshots, ensuring same viewport, theme and state; reference must be a real capture, not an assumed mockup.
2. Audit **structure first**: rail/top-bar proportions, card grid, typography hierarchy, density and vertical rhythm. Then palettes/elevation, icons/interaction styling and finally animations.
3. Score using the weighted rubric from VISUAL-QA.md, citing observed evidence. If reference not captured, use a *design system consistency* audit and explicitly say reference similarity cannot be quantified.
4. Exercise animations and functional interactions: nav collapse, dialog open/close, chart range, filters, search, errors, reduced motion and auth/roles.
5. Identify top 3 gaps, fix them, repeat capture. For multi-page work sample dashboard, list, form and settings; don't accept a polished dashboard alongside inconsistent rest.
6. Produce report: inspected routes, viewports, actual screenshots, scores only where evidenced, blocking issues and residual deviations.

Never claim a pixel-perfect match without inspected original and final rendered screenshots. Never penalize required business identity, accessibility or functional integrity for appearance.

## Video-based screenshot and interaction QA

Read `VIDEO-VISUAL-QA.md` and compare actual target routes against the user-provided 13 cropped reference frames in `assets/video-reference/`. Show both before/after stills **and** evidence of motion interactions where tools allow. Do not mistake the editorial letterbox/title in the source recording for product UI. Score structure, styling, real behaviour, motion and responsiveness; disclose any untested interaction.


## Motion QA extension (v4)

Static screenshot similarity is insufficient for matching the 92-second vertical video. Use `orbit-ui-motion-qa` to capture 0/25/50/75/100% of each meaningful transition, check synchronized entering/exiting elements, persistent anchors, keyboard focus, reduced-motion, low-end device performance and a non-jumping final state. Inspect `.ai/uiux/orbit/assets/editorial-video-reference/` sequence strips for observed examples. Distinguish visual observation from estimated easing/duration.

## Latest workspace video quality gate

Check fixed sidebar/header continuity and route-specific content, metric/bar stagger, analytics change of date range, and Settings entry with the labelled `assets/project-workspace-reference/` frame sequence. See `PROJECT-WORKSPACE-VISUAL-QA.md`.
