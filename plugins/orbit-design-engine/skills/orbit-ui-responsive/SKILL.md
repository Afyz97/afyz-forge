---
name: orbit-ui-responsive
description: "Adapt reference-inspired admin interfaces for responsive desktop, tablet and mobile layouts while preserving accessibility, keyboard support, touch targets and reduced motion. Not for a WCAG audit — use user-first-ux's ui-accessibility."
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

# Responsive and accessible enterprise UI

Read `.ai/uiux/orbit/DESIGN-SPEC.md`, `MOTION-SPEC.md` and `VISUAL-QA.md`.

## Breakpoints are content-driven
Test at 1440×900, 1024×768, 768×1024, 390×844, ideally 320×720. Do not assume desktop cards should simply shrink. Change grid proportions, visible column priority, card stacking and shell/drawer configuration. Keep page primary action accessible.

## Touch and keyboard
- Touch targets, focus and tab order: follow the **user-first-ux** skill if installed. Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus; adequate spacing and logical tab order.
- Menu/drawer/modal focus trap and restore; ESC/back semantics, screen-reader roles, live status as appropriate.
- Charts have written/tabular alternatives. Table scroll is contained and signposted; do not force horizontal viewport scrolling.
- Use minimum sufficient contrast, semantic tags/labels; never communicate finance/status by colour only.

## Motion
Respect `prefers-reduced-motion`, limit animation scale on small screens and avoid gesture-only interactions. No parallax obstructing touch, no focus hiding during sidebar slide.

## Exit criteria
No clipped forms or popovers, no inaccessible commands, no table data loss, no broken dialog at 200% zoom. Re-test both themes where applicable.

## Video-specific responsive interaction safeguards

When porting video patterns to small screens: turn the four-column Kanban into horizontal scroll or list mode with keyboard/accessible move actions, change team filter cards into one responsive column, move the calendar agenda below the grid or to list view, anchor analytics hover tooltips within viewport and provide focus/touch alternatives, keep the timer/stop targets touch-safe. Use reduced-motion without suppressing valid interactions.
