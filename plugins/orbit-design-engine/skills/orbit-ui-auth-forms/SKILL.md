---
name: orbit-ui-auth-forms
description: Build expressive yet usable login, registration, and account-recovery screens with accessible dual-panel composition and role-aware context. Use for sign-in/sign-up UI redesigns, transitions, form state, and responsive authentication.
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

# Orbit UI — authentication composition & state

**Trigger:** creating/editing login, register, password reset or invitation acceptance screens. Always consult `.ai/uiux/orbit/AUTH-VIDEO-AUDIT.md` and `AUTH-TRANSITION-PLAYBOOK.md` (fallback `~/.ai/uiux/orbit/`). Use `orbit-ui-diagonal-wipe` if motion like the reference is wanted. This is **Reference E**, a five-second VERSO demo, **not** the original Kinlo website or an instruction to use VERSO branding.

## Reference-driven composition
- A rounded, horizontally split, in-place authentication card has two deliberately contrasting host-theme surfaces: one for the form and one for the branded welcome message. Preserve existing site branding and typography.
- Sign-in: form at left and branded welcome at right. Registration: welcome at left and form at right. Between states, move the boundary with one angled theme-derived sweep instead of abruptly swapping screens.
- Preserve field labels, thin underlines, pill-like existing primary action, restrained host-theme accent treatment, and lightweight supporting copy. No palette values from the reference may be copied.
- Keep the requested site's **own** branding and event/organization details; do not add VERSO, Kinlo or dummy text to production.

## Functional requirements
1. Real sign-in and registration use existing routes/controllers, server-side validation, CSRF, email-verification, rate limiting, password-reset, remember-me and invitation/SSO rules where relevant.
2. Forms are separate genuine `<form>` elements; never make a switch button submit a form. Include autocomplete, type=email, proper label associations, validation error messages, pending and unsuccessful states. Do not animate errors out of view.
3. During transition only the active panel is focusable and exposed to assistive technologies; use `inert`, `aria-hidden`, no autofocus before animation completion, and sensible focus restoration.
4. If auth page embeds event/organization branding, keep it contextual and accessible; do not replicate an unrelated provider's identity.
5. Mobile: stack or simplify the panels; keep the form immediately usable with keyboard and narrow viewport. Reduced-motion: switch immediately with no diagonal sweep.

## Coordination
Call/use `orbit-ui-diagonal-wipe` for the specifically observed skewed blade and `orbit-ui-motion-qa` for rapid reversals, resizing, and reduced motion. Treat `examples/auth-diagonal-wipe-demo.html` as an **original implementation** of the concept, not source recovered from the video.

## Deliverable gate
Demonstrate both directions, correct route wiring, backend errors, keyboard/focus, responsive mode, reduced motion and no accidental form submission during a mode switch. If backend is unavailable, mark the screen as a demo rather than claiming real authentication.
