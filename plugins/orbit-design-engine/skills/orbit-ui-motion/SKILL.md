---
name: orbit-ui-motion
description: "Design and implement the full reference-inspired animation and motion layer: sidebar transitions, page reveals, staggered cards, chart morphs, modal entry, drawers, hover states and reduced-motion accessibility."
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

# the enterprise reference motion and micro-interactions — apply on every interactive UI redesign

Read `.ai/uiux/orbit/MOTION-SPEC.md`. These are **original defaults**, not measured animations from the demo.

## Motion inventory
1. On load/navigation: restrained reveal and a short, coherent stagger (max 3–6 visible cards; ~30–55ms increments).
2. Sidebar: synchronized width/label/icon/selection transitions, no text flicker or content jumps.
3. Charts: true data updates with smooth interpolations where meaningful, correct axis state, cancellation on reselect.
4. Overlay: dialog fade/translate, drawer slide and backdrop; keyboard focus begins/returns correctly.
5. Controls: hover/focus/pressed and pending/complete/error states, without motion as sole semantic signal.
6. Data lists: filter state, row expand/reorder transitions, accessible keyboard fallback for drag/drop and reliable persistence.

## Technology
Use CSS for simple transitions; use GSAP only if the project already has it or the effect warrants introducing it with permission. React timelines require cleanup. Alpine/Livewire require DOM lifecycle care. Stop animations at reduced-motion preference.

## Avoid
Constant bobbing, fake spin loading, exaggerated elastic bounces, long page fade, animation while async action is pending without status, rerender loops and GPU-heavy blur on large scrolling surfaces.

## Verification
Capture interaction video where tools permit. Test collapsed nav, chart rapid range switches, modal keyboard close, slow submit and `prefers-reduced-motion: reduce`. Fix visual glitches before reporting complete.

## Video demonstration: concrete choreography

For real UI implementation, additionally read `.ai/uiux/orbit/VIDEO-MOTION-PLAYBOOK.md` and view `.ai/uiux/orbit/assets/video-reference/` images for related page types. Required reference interactions include KPI count and chart entry, gauge progress, card dragging/settle, FLIP-based team filter reflow, coherent chart tooltip, anchored calendar switching, modal + toast acknowledgement, right-side detail drawer and one-token accent theme updates. Estimated timing ranges are targets, not measured facts. Use `orbit-ui-video-motion` for orchestrating these.


## Editorial animation extension (v4)

The 92s explainer adds **word-level kinetic typography, layered card entrances, persistent checklist progress, diagnosis/correction overlays, drawn relationships and a purposeful mascot cameo**. It is not an app tutorial or the enterprise reference footage. Read `MOTION-ROUTING.md`; use `orbit-ui-motion-storytelling` for landing/onboarding/explainer tasks, `orbit-ui-kinetic-type` for editorial words, `orbit-ui-layered-cards` for mock UI illustrations, and `orbit-ui-motion-qa` for frame-by-frame verification. Do not put these expressive effects in CRUD flows by default.

## Latest video: short workspace motion

Read `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` for synchronized metric bar/count transitions, fixed-shell route changes and analytics range switching. Prefer the ordinary application route, *not* editorial headline motion, for admin UI. Coordinate with `orbit-ui-workspace-navigation` and `orbit-ui-metric-choreography`.

## Reference E (v7): diagonal blade state switch

For paired sign-in / signup screens, read `AUTH-TRANSITION-PLAYBOOK.md`, use `orbit-ui-diagonal-wipe`, and verify both directions plus keyboard/reduced-motion states. Unlike simple crossfades, the reference's angled boundary traverses the full **fixed** card while the form sides exchange. Not recommended for everyday CRUD navigation.
