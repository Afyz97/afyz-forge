---
name: orbit-ui-trust-consent-ux
description: "Audit and improve privacy, consent, cancellation, refund, deletion, subscription transparency, accessibility and nondeceptive UI behaviours shown as checklist themes in the user-provided animated video, without assuming universal legal requirements. Not for a general dark-pattern or privacy review — use user-first-ux."
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

# Trust, consent and humane UX — topic-specific

Read `references/EDITORIAL-UX-CHECKLIST.md`. **Only use on relevant product/privacy/commerce/auth flows**, not as automatic dashboard decoration. The uploaded video is a legal-themed explainer but is not itself legal authority. Confirm jurisdiction, product nature, data processing and actual legal requirements; have legal counsel review policies.

## Design/engineering workflow

1. Inventory actual routes/states for privacy policy, terms, consent, email preferences, tracking, account export/delete, billing, cancel/refund and contact details. Only retain relevant ones.
2. Distinguish required vs optional choices and never precheck optional marketing permission; avoid a bundled consent checkbox that hides meaningful choices. Label actual effects and persist with appropriate audit trail.
3. Verify links open the correct current documents, data limits reflect real backend behavior, cancel/refund routes are real, and UI matches the organization's policies. Don't invent statements such as “SOC 2 certified”, “legally compliant”, or a guaranteed response deadline.
4. Make every control accessible to keyboard, assistive tech and touch. Show success after confirmed persistence, with reversible decisions when supported.
5. Use modest, truthful motion: checked state + inline status, not coercive flashing, false countdown or fake progress.
6. Prepare a report distinguishing `observed behavior`, `issue`, `proposed fix`, `legal review needed`, `implemented/tested`.

If asked for a visual imitation only, copy the communication pattern (clear examples / explicit before-after) without silently adding policies or compliance claims to the product.
