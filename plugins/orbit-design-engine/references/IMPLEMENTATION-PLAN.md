# Full-system redesign execution template

## Phase 0 — Inventory
Record framework, route count, layout variants, accessibility risks and key screens: dashboard, list, create/edit, detail, reports, settings and authentication. Read `.ai/agents/architecture.md`, `database.md`, `conventions.md` only when these exist; do not edit them without request.

## Phase 1 — Evidence
First locate the host theme source and record its semantic tokens without altering any actual colour values.
Capture reference screenshots where possible; obtain measurements and interaction inventory; record what is inferred. Capture current target UI at same sizes.

## Phase 2 — Foundations
Map existing host theme tokens and create only missing non-colour layout/motion primitives, shell/sidebar/header, responsive navigation, and existing-mode/organization-branding integration. Never introduce a palette or override host semantic values. Get one representative dashboard and table right before broad application.

## Phase 3 — Rollout
Refactor shared shell and reusable components; migrate screens route by route. Preserve backend, auth, original semantics and tests. Add every state including error/loading/empty and real motion.

## Phase 4 — Verification
Visually inspect, run tests, compare reference and output at three viewport sizes, fix top mismatches, test keyboard + reduced motion. Use `.ai/uiux/orbit/VISUAL-QA.md` and `THEME-INHERITANCE.md`. Exclude reference colours from resemblance scoring.

## Required per-page notes
- Route and user role
- Reference state/screenshot available?
- Information hierarchy and action flow
- Components to reuse
- Transitions and interaction states
- Narrow-screen behavior
- Tests run and unresolved limitations

## Suggested rollout order
App shell -> dashboard -> representative list/table -> form/detail -> secondary workflows -> settings/auth -> responsive/motion QA.
