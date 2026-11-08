# Project Context — afyz-forge repo

Background and decisions an AI agent should know before working here. Keeps intent that isn't obvious
from the code alone.

## Purpose

A personal Agent Skills marketplace (`afyz-forge`, owner **Afyz97**, repo `Afyz97/afyz-forge`) that
publishes reusable skills for AI coding agents, installable from any project/device via Claude Code's
plugin system. It began as a design-skills project and is intended to broaden beyond design.

## Current contents

Since the 2026-11 merge (records in `.ai/docs/merge/`), UI work lives in **two plugins split by
job, with exactly one owner per topic**:

1. **`user-first-ux`** — how the UI behaves: priority order, workflow, WCAG 2.2 AA (owner of every
   accessibility number), the 30 Laws of UX and Gestalt (`ux-laws` skill), ethics and dark
   patterns, states, forms, flows (e-commerce, enterprise, mobile), EN/BM microcopy
   (`ui-ux-copy`), user research (`ui-research`), WCAG audits (`ui-accessibility`).
2. **`ui-studio`** — how the UI looks and is built: tokens (owner: `references/shared/
   visual-system.md`), visual direction, named styles (`ui-styles`, from omni-design + the suite),
   visual polish (`visual-polish`, from ui-ten-fixes, with scripts), stack builds (Laravel,
   Next.js), critique, design-system audit, handoff, theming, canvas art. Built originally
   (2026-10-08) from a merged `ui-design` skill (itself a merge of 11 Anthropic skills; source kept
   locally in `_source/`, gitignored, never shipped). Text policy: upstream prose rewritten, facts
   and data kept exactly.
3. **`orbit-design-engine`** — dedicated reference-driven motion and app-shell engine (26 skills,
   own installer); kept separate because its job (matching a site or video reference) is distinct.

Merged and removed: `ux-laws`, `ui-ten-fixes`, `omni-design`, `ultimate-design-suite`. Old → new
mapping: `MIGRATION.md`.

Plus the first non-UI plugin:

6. **`system-design`** (added 2026-10-22) - built from a full read of the 28-chapter
   liquidslr/system-design-notes (System Design Interview vols 1-2). Text policy as for ui-studio:
   prose rewritten, facts and numbers kept (two source arithmetic slips corrected, noted in its
   README). Skills: `system-design` (method + 22 blueprints), `distributed-patterns`,
   `system-design-review`, manual `system-design-interview`.

Plus an agent-workflow plugin:

7. **`session-orchestrator`** (added 2026-10-31) - publicly distributable, so it assumes none of the
   owner's conventions (no `.ai/`, no CLAUDE.md content). Built from the official Claude Code docs,
   the changelog and the Codex source (research in `docs/research/session-orchestrator.md`). Owner
   decisions: a plugin `role-runner` agent with `disallowedTools: Agent` enforces leaf-only roles
   (built-in `general-purpose` is the fallback); read-only roles run freely only when the user asked
   for orchestration; Explore is never used for roles.

Plus a skill-security plugin:

8. **`skill-guard`** (added 2026-11-08) - built and tested in the `Afyz97/ai-skills` playground,
   then copied here (ai-skills keeps its copy; publish polished versions here). Scanner fixes on
   import: UTF-8 output (it crashed on Windows consoles on non-cp1252 evidence), new
   `HID-HOMOGLYPH` rule. Self-check: `python -I plugins/skill-guard/tests/test_scan_skill.py`.

Plus a refactoring plugin, and a merge (both 2026-11-08, from the ai-skills playground):

9. **`codeweave`** - mirrored unchanged from ai-skills (where its `git_cochange.py` Python < 3.12
   compile error was fixed). Kept separate: nothing here covers maintainability refactors
   (`system-design-review` covers scalability and reliability).
10. **`atelier-ux` merged, not mirrored.** Only `atelier-motion-countdown` had no owner here; it
    became `ui-studio:ui-countdown`. Unique lines of navigation, workflow, data-storytelling and
    editorial went into existing user-first-ux / ui-studio references; design-director,
    visual-foundations, responsive-mobile and ux-quality-audit were duplicates;
    `atelier-skill-enhancer` stays in the playground. Map: `MIGRATION.md` §5.

## Key decisions (and why)

- **Two UI plugins split by job, one owner per topic** (2026-11). Before the merge, ui-studio held a
  near-verbatim copy of user-first-ux and five plugins competed for the same prompts. Now only the
  owner states a rule and its numbers; everything else points to it by skill name with a one-line
  fallback, so each plugin still works installed alone.
- **`plugins/<name>/` layout with folder==plugin==entry naming** — chosen by the owner for
  traceability; each plugin is self-contained and independently installable.
- **Marketplace named `afyz-forge`** (general, not design-specific) so future non-design plugins fit.
- (Historical) **Consolidated file structure inside `omni-design`** — the brief suggested ~70 files; we merged where
  it improved coherence/context-efficiency (one `style-router` with per-style profiles + 10 deep files;
  merged inseparable reference topics; adapters grouped by ecosystem). Documented in the skill's
  `SOURCES.md`.
- **Guidance is original/synthesized**; sources were studied (see the skill's `SOURCES.md` and
  `docs/RESEARCH.md`) but not copied. SOURCES.md honestly distinguishes directly-inspected local
  sources from prior-research/general-knowledge influence.

## History / gotchas already resolved

- The repo was published to GitHub; an early commit accidentally tracked `.claude-flow/` runtime logs
  (incl. headless prompt/result logs). History was **rewritten to a clean root** and force-pushed;
  `.gitignore` now excludes local tooling state. Don't reintroduce those files.
- Claude Code marketplace/plugin schema required `owner`/`author` as **objects** (not strings) — fixed.
  Watch for this on any manifest edit (`conventions.md`).
- Folders were reorganized from `skills/*` (single plugin) → `plugins/<plugin>/skills/*` (two plugins).

## Install (reference)

```
/plugin marketplace add Afyz97/afyz-forge
/plugin install user-first-ux@afyz-forge
/plugin install ui-studio@afyz-forge
/plugin install orbit-design-engine@afyz-forge
/plugin install system-design@afyz-forge
/plugin install session-orchestrator@afyz-forge
/plugin install skill-guard@afyz-forge
/plugin install codeweave@afyz-forge
```
Moving from the old `Afyz97/ai-skills` marketplace: `/plugin marketplace remove ai-skills`, then add
`Afyz97/afyz-forge`, and uninstall the merged plugins (ux-laws, ui-ten-fixes, omni-design,
ultimate-design-suite) if you still have them.

## Open follow-ups (nice-to-have, not blocking)

- `npx skills add Afyz97/afyz-forge` discovery may need verification given skills now live under
  `plugins/<plugin>/skills/` rather than a root `skills/`.
- Formal baseline-vs-assisted evaluation of the skills has not been run (scaffolded in `evaluations/`).
- `system-design/.claude-plugin/plugin.json` `homepage` still points to the old `Afyz97/ai-skills`
  repo (that plugin was out of scope for the merge).

See `architecture.md`, `conventions.md`, `publishing.md`.
