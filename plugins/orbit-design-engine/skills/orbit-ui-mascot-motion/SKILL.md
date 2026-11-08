---
name: orbit-ui-mascot-motion
description: "Create an optional original branded helper mascot with subtle blink, one-time hop, pose shift and celebration reactions as seen in the user-provided animated checklist explainer; restrict to marketing, onboarding and completion contexts."
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

# Mascot cameo and ambient atmosphere

Use only when requested or consistent with product brand. The supplied video contains a small block-like animated figure; **do not copy its artwork**. Design original mascot assets or use an existing licensed character. See `EDITORIAL-VIDEO-OBSERVATIONS.md`, 00s, 02s, 30s, 84s and 90s stills.

## Motion contract

- Mascot sits outside primary content; remains static while forms and critical actions are read. Blinks or changes expression once during scene entrances. A one-off 3–7px hop, very small 3–6-degree tilt or hand gesture can acknowledge genuine completion.
- Avoid endless bobbing, repetitive dance, overlays near form labels/CTA or animation that hides success/error text.
- Calm gradient bloom and dot-grid are decorative layers; use static gradients for routine UIs and only slow low-cost transforms for explicitly motion-driven landing pages.
- Reduced motion: static pose; `aria-hidden=true` if decorative; no spoken duplicate status. Keep contrast, layout and hit targets unaffected.

Acceptance: the mascot complements the brand rather than replacing correct workflow feedback. If the app has no mascot and no brand rationale, skip this skill and use an ordinary success icon.
