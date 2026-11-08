---
name: user-first-ux
description: >-
  Makes a UI work best for its users: usability, flows, forms, onboarding, errors and every UI
  state, judged by a priority order (honest > accessible > usable > efficient > consistent >
  aesthetic) and a Read-Report-Plan-Approve-Implement-Verify-Sync workflow with a blocking
  checklist. Use for "review this form/flow for usability", "is this good for users?", "UX
  review", "does this checkout use dark patterns?", "design the signup/onboarding/checkout
  flow", "what states am I missing?", "make this easier to use", consent, cancel and delete
  flows, PDPA, Malaysian and inclusive context. Not for look, style, tokens or polish - use
  ui-studio.
---

# User-First UX

## Mission

Design, build and review interfaces that are **best for the user**. A beautiful screen that
confuses, excludes, slows down or manipulates people is a failure, however polished it looks.

## Priority order (higher wins)

1. **Honest & safe** - no deception, dark patterns or privacy harm
2. **Accessible** - usable by people with disabilities, on any device or network
3. **Usable** - users complete their task correctly, with few errors
4. **Efficient** - fewest steps, time and thought to reach the goal
5. **Consistent** - matches the system and conventions users already know
6. **Aesthetic & delightful** - polish, personality, motion

Whenever you sacrifice a lower priority for a higher one, **name the trade-off** in one line,
e.g. "Kept the heavier layout because it is clearer on mobile (Usable > Aesthetic)."
If a request asks for level 6 ("make it modern") while level 1-4 is broken (e.g. a broken
checkout), fix the higher level first and say why.

## Workflow (mandatory)

**Read -> Report -> Plan -> Approve -> Implement -> Verify -> Sync**

1. **Read** existing screens, components, design tokens, copy and routes. Then answer the
   **UX brief** before touching pixels:
   - Who are the users? What are their top 3 tasks (jobs-to-be-done)?
   - Context: device, network, language, expertise, frequency of use, stress level?
   - What does success look like (task completed, fewer errors, faster)?
   - No research available? List assumptions as **hypotheses to validate**. Never present
     guesses as findings.
2. **Report** - issues table (format below), ranked by user impact.
3. **Plan** - flow first, then structure (IA), then layout, then visual polish. Never polish
   before the flow and IA are right. Low-fidelity first: describe or wireframe the flow
   before styling.
4. **Approve** - stop and wait for approval before implementing. (Skip only when the user
   explicitly said to proceed without asking; say that you skipped it.)
5. **Implement** - existing tokens and components only. Any new token or component must be
   justified and documented.
6. **Verify** - run the full checklist (`references/checklist.md`), including keyboard,
   screen reader, 320px width, 200% zoom, slow network, and every state.
7. **Sync** - update component docs, tokens and changelog. Record open hypotheses and how to
   test them with users.

Small, well-scoped requests (one component, one copy fix) still follow the workflow, but each
step can be a few lines.

## Core rules summary

Rule IDs are used in review tables. Full detail lives in the references.

**Principles** (`references/principles.md`)
- Nielsen's 10 heuristics as agent rules: status within 100ms, user's words not DB terms,
  undo/cancel/back never lose work, consistency, prevent errors, recognition over recall,
  expert shortcuts, minimalism, recoverable errors, help at point of need.
- Norman: signifiers visible without hover, mapping, feedback, constraints over warnings.
- Gestalt and the 30 Laws of UX: the `ux-laws` skill (rule IDs G and U map to it).

**Visual system** (`references/visual-system.md`) - hierarchy, layout, type, colour and
tokens are owned by ui-studio. C3 (never colour alone) and M2 (reduced motion) stay here.

**Components** (`references/components.md`) - buttons (verb + object), forms (highest
impact), pickers (P1-P4), tables, dashboards, cards/modals/toasts, search/nav, onboarding.

**States & feedback** (`references/states-feedback.md`) - every state, not just the happy
path; response-time bands; Core Web Vitals; error formula: what happened + why + how to fix.

**Content** (`references/content.md`) - CM1-CM9: human, true, plain, specific; no fake urgency;
no lorem ipsum.

**Accessibility** (`references/accessibility.md`) - WCAG 2.2 AA is the floor, not a goal.

**Ethics & privacy** (`references/ethics-privacy.md`) - banned dark patterns; cancel as easy
as signup; total price early; privacy by default; label AI content.

**Inclusive & local** (`references/inclusive-context.md`) - low-end devices, slow data,
localisation, single "Full name" field, locale formats (DD/MM/YYYY, RM 1,234.50).

**Design system discipline** - owned by ui-studio's `ui-design-system` skill. Minimum if it is
not installed: components consume tokens only; reuse before creating.

**Anti-patterns** (`references/anti-patterns.md`) - the generic "AI template" look and other
things agents commonly produce. Flag and fix on sight.

## Which reference to load

Load only what the task needs.

| Task | Load |
|---|---|
| Any review or redesign | `principles.md`, `anti-patterns.md`, `checklist.md` |
| Layout, hierarchy, type, colour, "make it look better" | the **ui-studio** skill (C3, M2 in `visual-system.md`) |
| Building a specific component, form, table, dashboard | `components.md` (+ matching `examples/`) |
| Loading, empty, error, performance | `states-feedback.md` |
| Any copy, labels, errors, stock/price text | `content.md` |
| Anything interactive (always before "done") | `accessibility.md` |
| Signup, checkout, pricing, consent, cancel/delete, AI features | `ethics-privacy.md` |
| Names, addresses, dates, currency, multi-language, low-end devices | `inclusive-context.md` |
| Checkout, cart, product pages | `domains/ecommerce.md` |
| Admin, ERP/CRM, dense dashboards, roles and permissions | `domains/enterprise-dashboards.md` |
| Mobile apps and mobile-first screens | `domains/mobile-ui.md` |

Sibling skills in this plugin: `ux-laws` (laws of UX audit), `ui-accessibility` (WCAG audit),
`ui-ux-copy` (EN/BM microcopy), `ui-research` (research plans and synthesis).

Examples (before -> after code): `examples/stat-card.md`, `avatar-stack.md`,
`assignee-picker.md`, `product-card.md`, `signup-form.md`, `data-table.md`,
`destructive-confirm.md`, `empty-state.md`.

## Output formats

**Review**

| Rule ID | Element / file | Problem | User impact | Fix | Severity |
|---|---|---|---|---|---|

Severity: **Critical** = blocks a task or excludes users; **High**; **Medium**; **Low**.
Rank by user impact. Then: the **top 3 fixes** in order, then **open hypotheses** and how to
test them.

**Build**
1. UX brief (users, top tasks, context, success, hypotheses)
2. Flow (numbered steps)
3. Short IA outline
4. Implementation
5. Completed checklist, with any exceptions justified and trade-offs named

**Measure** (recommend when relevant): task success rate, time on task, error rate, SUS
score, and HEART (Happiness, Engagement, Adoption, Retention, Task success). Five-user
usability tests catch most major issues; repeat them each iteration.

## Done means

Every checklist item in `references/checklist.md` is "yes", or its "no" is explicitly
justified to the user. Any unjustified "no" blocks calling the work done.

## Evals

`evals/evals.json` holds the test prompts and expected behaviours for this skill.
