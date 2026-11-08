---
name: ui-design-system
description: >-
  Audits, documents or extends a design system across the codebase or component library: tokens
  (colour, type, spacing, radius, shadow, motion), component variants, states and sizes, and
  shared patterns. Use for "audit our
  design system", "find hardcoded colours, arbitrary Tailwind values or off-scale spacing",
  "how consistent are our components?", "document the Button component", "write component
  docs", "do we need a new component for X?", "token naming", "clean up the @theme block,
  tailwind config or _variables.scss", or a design-system score. Produces the Audit, Document or
  Extend template. Not for polishing one screen or component - use visual-polish.
argument-hint: "audit | document <component> | extend <pattern>"
---

# Design system: audit, document, extend

Arguments: `audit` (whole system), `document <component>`, `extend <pattern>`. With no argument,
ask which. Frame: `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`; severity:
`${CLAUDE_PLUGIN_ROOT}/references/shared/severity.md`.

## What counts as the system

| Layer | Contents |
|---|---|
| Tokens | colour (brand, semantic, neutral); typography (size steps, line height, weight); spacing (the scale and the padding inside components); borders (width, radius); elevation (shadow levels); motion (easing, duration); breakpoints; z-index |
| Components | variants (e.g. primary / secondary / ghost); sizes (e.g. sm / md / lg); every state (default, hover, active, focus, disabled, loading, error); behaviour (interaction and animation); accessibility (keyboard and ARIA) |
| Patterns | forms (grouped fields, validation, submitting); navigation (breadcrumbs, tabs, side navigation); showing data (lists, cards, tables); feedback (inline messages, toasts, modal dialogs) |

Token values: `${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`. Token tiers (primitive,
semantic, component), what to tokenize, extending an existing system:
`references/token-architecture.md`. Where tokens live in code: Tailwind v4 `@theme` (`resources/css/app.css` or `app/globals.css`),
Filament panel `theme.css`, Bootstrap `_variables.scss`. Stack details: `ui-stack-laravel`,
`ui-stack-next`.

## Principles

1. **Shared before novel.** The system exists so teams stop rebuilding the same thing; reuse
   beats a fresh invention.
2. **Composable, not rigid.** Components combine; constraints guide without boxing teams in.
3. **Undocumented means missing.** If a variant or rule is not written down, people will not
   find it, so treat it as absent.
4. **Versions and migrations.** A breaking change ships with a migration path.

Scope note: "consistency first" applies to the system layer. The distinct identity the tokens
express is decided once in `ui-visual-direction`; the system then makes it repeatable.

## Discipline

Components consume tokens only. Reuse before creating. Every new component documents variants,
states, accessibility notes and do/don't. Flag hard-coded values, duplicate components and
inconsistent naming.

## Mode: audit

1. Inventory tokens and components (Glob the component folders, read the token file).
2. Count leaks: hardcoded hex, arbitrary Tailwind values (`p-[13px]`, `text-[#333]`), inline
   styles, off-scale spacing (not on the 4pt grid), custom font sizes. The
   `design-system-auditor` agent does this grep pass and returns counts with file:line.
3. Check naming consistency and component completeness (states, variants, docs).
4. Fill `references/audit-template.md`. Score out of 100 and say how you scored it.

## Mode: document

Fill `references/document-template.md` for the named component: purpose and when to use it,
variants, props, states, accessibility (role, keyboard, what a screen reader announces),
do/don't, and a code example in the project's stack.

## Mode: extend

Fill `references/extend-template.md`: the gap, why existing components fall short, the
proposed API, variants, states, tokens used, accessibility, and open questions.

## Working tips

- Start with an audit before documenting or extending.
- Write docs while building, not after.
- Breadth beats polish: 80% of components documented adequately is worth more than ten
  documented perfectly.

## Connectors

A design tool lets you audit naming, variants and token usage in the source files; a knowledge
base holds the current docs and is where updates get published
(`${CLAUDE_PLUGIN_ROOT}/references/shared/connectors.md`).
