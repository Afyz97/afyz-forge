---
name: orbit-ui-foundations
description: "Create or improve a coherent reference-inspired interface visual foundation: design tokens, typography, colour modes, spacing, cards, borders, shadows, component states and consistent application-wide styling. Not for a design system with no reference to match — use ui-studio's ui-design-system."
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

# the enterprise reference visual foundations

Read `.ai/uiux/orbit/DESIGN-SPEC.md` and any `reference/MEASUREMENTS.md` actually captured. Reference screenshots override original starter guesses.

## Establish tokens, not one-off styling
- Use tokens for page background, elevated card, muted surface, body/muted text, hairline border, primary/actions, selected, good/warn/danger, focus, radius, spacing, responsive widths and animation durations.
- Reuse CSS custom properties or existing design system theme, scoped to the host app root. `assets/orbit-ui-foundation-tokens.css` provides alias mappings and motion/layout only; map aliases to the real host tokens before use. Never introduce a palette.
- Calibrate typography using rendered screenshots: page headings, section labels, body, table rows, action labels, KPI numbers and locale-aware money. Typography and density are primary visual signals.
- Avoid generic framework defaults that conflict with the installed theme, random gradients, deep shadows everywhere or unreadably tiny fonts. Match observed geometry and interaction evidence while retaining existing project colours.
- Keep consistent radii/border weights, action hierarchy and icon set across all routes.

## Interaction state matrix
Buttons: default/hover/pressed/focus/disabled/loading/success/error. Inputs: empty/filled/focus/invalid/readonly/disabled. Navigation: default/hover/active/expanded/collapsed. Card: static/interactive/skeleton/empty. Provide semantic content, not just colour.

## Integration
Inspect existing Bootstrap/AdminLTE/Tailwind/component library first. Layer tokens rather than re-platforming. Share primitives across dashboard, forms, table and settings. Maintain dark mode, contrast, responsive layout and organization branding where relevant.

## Verify
Compare component snapshots in light and dark mode at mobile and desktop widths. Ensure no duplicate variant styles; record tokens actually implemented and reference confidence.

## Video-derived theme personalization (behaviour only)

The video demonstrates updating multiple UI regions in response to a setting. **Do not reproduce its named swatches or palette.** If the actual product already supports themes or accent options, reuse that existing settings API and the current theme tokens. Otherwise keep the application theme unchanged. `assets/video-interaction-tokens.css` contains motion effects and semantic mappings only; it must never override brand or theme values.
