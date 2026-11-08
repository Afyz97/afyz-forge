# Changelog

All notable changes to the afyz-forge marketplace. Versions are per plugin (SemVer).

## 2026-11-08 — consolidation and move to afyz-forge

Marketplace renamed `ai-skills` → `afyz-forge` and moved to the new repo `Afyz97/afyz-forge`
(metadata 0.9.0 → 0.10.0). Records: `.ai/docs/merge/` (inventory, report, plan, merge map,
verify). Upgrade steps: `MIGRATION.md`.

### user-first-ux 1.0.0 → 1.1.0
- Added skills `ux-laws` (from the ux-laws plugin), `ui-accessibility`, `ui-ux-copy`, `ui-research`
  and commands `ui-a11y`, `ui-copy` (from ui-studio), agent `a11y-auditor`, 15 trigger eval cases,
  domain playbooks for e-commerce, enterprise and mobile (from omni-design).
- Now the single owner of priority order, workflow, severity, WCAG numbers, laws of UX, ethics,
  states, forms, flows, microcopy and BM/EN.
- `visual-system.md` and the Gestalt/Laws parts of `principles.md` became pointers (to ui-studio
  and the ux-laws skill); A7 now states a 44×44 px house floor; A1 a recommended ~7:1.
- New README, NOTICE and `licenses/frontend-design.txt`.

### ui-studio 0.1.0 → 1.0.0 (command names changed)
- Removed its copies of user-first-ux (5 shared references, `components.md`, 8 examples) and
  moved `ui-accessibility`, `ui-ux-copy`, `ui-research`, `/ui-a11y`, `/ui-copy`, `a11y-auditor` to
  user-first-ux. `priority-workflow.md`, `quality-floor.md`, `severity.md` are now pointers.
- Added `visual-polish` (Ten Fixes rules, audit/fix/build modes, measurement scripts and assets),
  commands `polish-audit`, `polish-fix`, `polish-new`, agent `ui-ten-fixes-auditor`.
- Added `ui-styles` (context classifier, design dials, style router, 10 style files, brand vs
  product) from omni-design and ultimate-design-suite.
- `visual-system.md` became the single owner of token values (adds `--text-display`, icon and
  surface tokens, colour roles, effects budget); `ai-defaults.md` adds AD8-AD10; new references:
  `ui-critique/references/scored-audit.md`, `ui-design-system/references/token-architecture.md`,
  `ui-stack-laravel/references/preserve-conventions.md`, `ui-visual-direction/references/`
  public-websites, reference-to-code, redesign-existing-ui, adapters/.

### orbit-design-engine 8.0.0 (no version change)
- Kept as a dedicated plugin. Repo URLs updated; seven skill descriptions gain a "Not for … —
  use …" ending; one target-size line points to user-first-ux.

### session-orchestrator 0.1.0 (no version change)
- Repo URL and install commands updated.

### Removed plugins (merged)
- `ux-laws` → user-first-ux; `ui-ten-fixes`, `omni-design`, `ultimate-design-suite` → ui-studio.
  No stubs are published in afyz-forge: the marketplace has a new name, so nobody installs the old
  names from it. Mapping: `MIGRATION.md`.
- omni-design's README, CHANGELOG, SOURCES and tests moved to `docs/archive/omni-design/`.
