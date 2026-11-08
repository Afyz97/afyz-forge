---
name: orbit-ui-diagonal-wipe
description: Implement bidirectional diagonal blade/sweep screen transitions with balanced counter-motion, precise clipping, focus-safe state replacement and reduced-motion fallbacks. Use when swapping sign-in and sign-up panels or other deliberately paired states.
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

# Orbit UI — bidirectional diagonal blade

**Trigger:** user asks for the sweeping slanted login/sign-up motion in Reference E or comparable split-card replacement. Read `AUTH-VIDEO-AUDIT.md`, `AUTH-TRANSITION-PLAYBOOK.md`, and examine `.ai/uiux/orbit/assets/auth-reference/` (or `~/.ai/uiux/orbit/`).

## Mechanics; NOT a static design checklist
- Initial state has host-themed sign-in pane at **left**, host-themed hero pane at **right**.
- When 'Create an account' is activated, a **slanted host-theme blade travels right→left** across the card; the branded message crosses to left and the registration form settles on the right.
- 'Sign in' on the register state reverses the traversal **left→right**, restoring sign-in-left/welcome-right.
- Keep the outer card fixed, clipped by its rounded bounds. The diagonal leading edge is sharp and coherent; avoid separate uncoordinated fades or page navigation.
- The video shows HTML/CSS/JS illustrative panels for a skew + counter-skew pattern. That is observed evidence of an idea, **not** a runnable source repository. Use a fresh implementation, e.g. transform/skew with inverse inner transform or clip-path polygons with synchronized reveal. Never paste proprietary video code verbatim.
- Maintain distinct DOM ownership and focus for the forms. Transfer interactivity after the sweep, not during it; catch rapid repeated clicks; cancel or complete transitions on unmount/resize, and handle reduced-motion changes.

## Suggested original motion tokens (not measured source values)
- Full swap: **620–780 ms**, ease `cubic-bezier(.68,0,.22,1)`; slower than ordinary button hover, fast enough for authentication.
- Leading edge: ~10–16% visual lean between top/bottom intersection around midpoint, reversible with direction.
- Supporting text: subtle **120–240 ms** opacity/translation following the blade, never text jank or forced reflow.
- Button/focus: standard ~100–160 ms hover/focus; no hover-only affordance.
- Use composited `transform`/`opacity` where practical; clip-path only over the contained auth card; no huge offscreen blur/shadow animation.

## State-machine tests
`signin -> transitioning-to-signup -> signup -> transitioning-to-signin -> signin` with a single current state. Always verify click spam, tab/shift-tab, input preservation policy, errors, a resized layout, reduced motion and two-direction screenshot frames. Form fields must not drift while the blade is moving unless visibly intended and tested.

## Execution
Prefer existing app styling and animation dependencies; do **not** add GSAP solely for this effect. See `examples/auth-diagonal-wipe-demo.html` for an original no-dependencies implementation. Reproduce the observed **motion language**, not the exact branded artwork.
