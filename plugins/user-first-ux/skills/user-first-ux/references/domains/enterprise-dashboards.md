# Enterprise, Admin & Dashboard UI

This is where most "make it modern" redesigns go wrong. Operational software for trained users
optimizes for **task throughput, scanability, and state visibility** — not for the aesthetics of a
marketing page. Treat this area as first-class; it is the default for Laravel/admin/ERP/CRM work.

## The governing rule

**Do not convert a dense professional system into oversized cards.** Preserve information density.
Earn clarity through hierarchy, alignment, grouping, and consistent components — not through padding
and whitespace that force scrolling and lower throughput. When in doubt, keep it tighter than a
consumer app.

## Design for the expert, not the first-timer

- Users are **trained and repeat** — favor convention, keyboard efficiency, and predictability over
  novelty and discovery. Surprise is a cost here.
- Provide **compact/comfortable density modes**; default expert tools to compact.
- **Keyboard-first affordances** — shortcuts, tab order that follows the task, command palette for
  power tools, `Enter`-to-submit, quick row actions.
- **Progressive disclosure** — advanced options and rare actions tucked away, not removed; the common
  path is fast, the full power is reachable.

## The building blocks

- **Data tables** are the heart — get them right first. Alignment, tabular numbers, sticky headers,
  sorting, filtering (visible removable chips), bulk actions with clear counts, saved views,
  pagination with totals. Full guidance: TB1-TB10 in `../components.md`.
- **Filters & search** — persistent, visible, clearable; advanced/faceted for expert tools; state
  survives navigation.
- **Forms** — dense but legible; inline edit for quick changes; validation and error recovery that
  never lose input. See F1-F11 in `../components.md`.
- **Detail views** — a record's full context: summary header, key facts scannable, related data,
  audit trail/history, contextual actions.
- **Status systems** — a consistent status vocabulary (chips with text + color + optional icon),
  never color-only. Map states to a small palette used the same way everywhere.
- **Dashboards** (see below) — overview and monitoring, not decoration.

## Roles, permissions & multi-tenant reality

- **Role-sensitive UI** — show actions the user can actually perform; disable-with-reason or hide by
  policy consistently (decide one approach). Never render an action that will just 403.
- **Destructive & privileged actions** — confirm, name consequences, log; gate by permission.
- **Audit trails** — who did what when; make history discoverable on records that need accountability.
- **Empty/partial by permission** — design the "you don't have access" and "nothing assigned to you"
  states, not just the full-data view.

## Dashboards specifically

- **Answer a question, don't decorate.** Every widget earns its place by supporting a real decision or
  monitoring need. No fake metric cards, no charts of invented data (that's slop and dishonest).
- **Hierarchy of glance → scan → drill.** Top: the few numbers that matter (with trend/context, not a
  bare number). Middle: charts/tables for patterns. Deep: drill-through to records.
- **Coordinated views** — filters and time ranges apply across related widgets; selecting in one
  updates others where it helps analysis.
- **Right chart for the question** — trend→line, comparison→bar, part-of-whole→ sparingly (bar often
  beats pie), distribution→histogram. Label directly; keep the chart palette a subset of the product
  palette. Don't add a chart where a number or table is clearer.
- **Density is fine** — operators want a lot on one screen; use alignment and grouping to keep it
  scannable rather than spreading it thin.

## Responsive degradation

Enterprise tools are often desktop-first, but tablet/field use is common. Decide what a smaller screen
*must* do (usually: read status, take a few key actions) and design that — don't just reflow a
1600px grid. Tables → priority columns/detail; multi-pane → tabs or drill.

## Common AI failure modes

Cards instead of tables · marketing padding on ops screens · low density that forces scrolling ·
fake metric dashboards · charts of invented data · color-only status · actions shown regardless of
permission · no bulk actions/saved views · no compact mode · surprising, unconventional layouts for
trained users.

## Order of work

1. Classify: product mode, high density, high convention (density and dials: the **ui-styles**
   skill in ui-studio, if installed).
2. Inspect and preserve the data model, permissions, routes, validation and current density.
3. Data surfaces first (tables), then the operator's most repeated task (keyboard, quick row
   actions, inline edit, command palette).
4. Forms and detail views, then roles and permissions, then the status system.
5. Dashboards, then states, then responsive degradation.
6. Accessibility and review (`../accessibility.md`, `../checklist.md`).
