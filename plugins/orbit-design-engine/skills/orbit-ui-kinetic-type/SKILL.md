---
name: orbit-ui-kinetic-type
description: "Animate cinematic editorial headlines and phrase emphasis inspired by the 92-second vertical checklist video: blurred word replacement, theme-accented italic serif focus, semantic corrective strikethrough and theme-derived marker highlights with stable line layout."
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

# Kinetic type: meaning-led copy transitions

Read `EDITORIAL-VIDEO-OBSERVATIONS.md`, `EDITORIAL-MOTION-PLAYBOOK.md` and stills at 02s, 16s, 20s, 30s, 34s and 87s.

- Structure: prominent sans heading (heavy 700–800), selective italic display serif, a subtle theme-derived highlight behind key phrases, and a semantic correction indicator. All styling inherits existing host theme tokens. Avoid font guessing claims: choose licensed/system fonts available in the current project.
- Use stable typographic slots: reserve a minimum block height before text swaps, prevent CLS, and expose one coherent phrase to assistive tech rather than announcing animated individual words.
- Scene transitions: exit old phrase `opacity/translateY/blur`; enter new phrase after short overlap; stagger italic emphasis by ~80–180ms. Timing recommendation 240–440ms. End in a static readable position.
- Strike-out: draw line across problematic phrase, fade its emphasis and reveal replacement; retain semantic explanation, not colour alone.
- For a real application: no perpetual title changes, no typewriter on forms, no layout-shifting split-letter animation; use for onboarding or guided flows as requested.
- `prefers-reduced-motion`: render final phrase instantly; preserve highlight/underline statically. Test line wrapping, text zoom 200%, font load, i18n, screen reader and small mobile screens.

Implement this as a reusable accessible `AnimatedHeadline` component/state pattern with separate visible layers marked `aria-hidden` and a single accessible current heading, or a short simple CSS transition where a component library is not available.
