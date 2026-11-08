---
name: orbit-ui-components
description: "Implement consistent polished reference-inspired tables, filter bars, forms, invoices, badges, buttons, modals, drawers, tabs and stateful enterprise components for admin applications. Not for the usability rules of forms and tables — use user-first-ux."
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

# the enterprise reference enterprise component kit

Read `.ai/uiux/orbit/DESIGN-SPEC.md`, `MOTION-SPEC.md` and `STACK-ADAPTERS.md`.

## Components to build or restyle as needed
- KPI/stat card: value, unit, timeframe, delta, context, optional drilldown. Number changes may animate only if real.
- Table/list: header actions and filters, clear headings, right-aligned quantities, strong row rhythm, semantic status chips, sticky header where useful, non-janky pagination and row action placement.
- Form: labels above controls, groups, helper text, inline errors, validation, save feedback, unsaved-changes guard and thoughtful layout on narrow screens.
- Dialog/drawer: one clear intent, visible close, accessible focus + ESC, destructive confirmation, pending/error/success states.
- Button/chip/tabs/dropdown: consistent height/radius/icons, hover/focus/pressed/disabled states; tab state is obvious and updates actual content.
- Empty/skeleton/error: reusable component that explains state and next action; never display mock data as real.

## Required interaction polish
Subtle hover and focus, dialog fade/scale, drawer slide, row expansion, filter chip state, button loading and success. Respect reduced motion. Support keyboard parity for drag/drop and bulk actions.

## Implementation safeguards
Maintain DataTables and server-side sorting/filtering in legacy projects; preserve CSV/Excel exports, validators, CSRF and permissions. Do not infer new business features from the enterprise reference; map patterns to the user's actual workflows.

## Quality gate
Before completion show all implemented states, responsive table handling and real mutation feedback. Do not ship static placeholder controls.

## Video-backed interactive components

For Kanban cards, FLIP filter chip groups, member profile drawers, form dialogs/toasts and accent selectors, load `VIDEO-UX-PATTERNS.md` and relevant specialist skills (`orbit-ui-interactive-kanban`, `orbit-ui-team-filter-motion`, `orbit-ui-feedback-overlays`, `orbit-ui-personalization`). Replicate subdued outlined surfaces and rounded compact control feel with required states, never fake submissions or no-op interactions.

## Reference E — auth form composition

When working on login/registration components read `AUTH-VIDEO-AUDIT.md` and use `orbit-ui-auth-forms`; ensure accessible input labels, real error and loading states, autocomplete and responsive stacking. Add a diagonal blade only if the authentication design calls for it.
