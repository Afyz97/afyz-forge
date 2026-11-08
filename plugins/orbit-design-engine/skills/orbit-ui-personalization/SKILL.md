---
name: orbit-ui-personalization
description: "Implement video-inspired application appearance settings: existing application theme settings, global semantic token propagation, visually selected choices, week-start options, accessible contrast and saved theme preferences."
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

# Accent personalization: one change across the entire system

Evidence: `assets/video-reference/26-theme-selector.jpg` and `28-theme-updated.jpg`; read `VIDEO-UX-PATTERNS.md`.

The video demonstrates a setting propagating consistently across dashboard KPIs, primary actions, charts, navigation and timers. **Do not introduce reference theme choices.** Only expose choices that are already defined by the current system. Drive them through the host theme provider and its semantic tokens, not manual element overrides. Use existing preference identifiers (never new palette presets). Give choices accessible labels and clear selected states independent of colour; smoothly transition host-managed visual properties (150–260 ms) only when allowed by reduced-motion preferences. Verify contrast in the host's actual available themes.

Persist preference using the project's account settings if available; browser-only preference is acceptable only if explicitly intended and not wrongly presented as account-wide. Restore before first paint when possible to avoid theme flash. Week-start selection must affect actual calendar calculations, including locale, not just highlight a button. Test theme-token coverage across **every** route and shared component, refresh, new tab, charts/canvas, dark mode where supported, and server-rendered fallback.

## Reference D: source-panel suggestion, not observed settings change

A `settings.js` code panel visibly includes `store.get`/`store.set` for root dataset accent and a `gsap.fromTo` on a swatch with rotation/scale and `back.out` easing plus toast. This animation is **not shown being triggered inside the application** in the 6.175s sample. Treat it as an optional implementation idea, not measured visual evidence. See `PROJECT-WORKSPACE-VIDEO-AUDIT.md` and maintain user preference and reduced-motion semantics.
