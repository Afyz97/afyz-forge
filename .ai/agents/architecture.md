# Architecture — afyz-forge repo

Context for AI agents working in this repository. Describes how the repo is organized and how the
pieces relate. Keep this file in sync when the structure changes.

## What this repo is

`Afyz97/afyz-forge` is a **Claude Code plugin marketplace** (named `afyz-forge`) that publishes
**Agent Skills** for AI coding agents. UI work is split by job between two plugins with **exactly one owner per topic**: `user-first-ux`
(how the UI behaves) and `ui-studio` (how it looks and is built). Alongside them: the
reference-driven `orbit-design-engine`, the non-UI `system-design` plugin and the
`session-orchestrator` agent-workflow plugin. `ux-laws`, `ui-ten-fixes`, `omni-design` and
`ultimate-design-suite` were merged into the two UI plugins and removed in 2026-11 (see
`MIGRATION.md`). It is designed to grow — non-design plugins can be added alongside.

## The four layers

```
GitHub repo:     Afyz97/afyz-forge                         (what users `/plugin marketplace add`)
  └─ marketplace: afyz-forge                               (.claude-plugin/marketplace.json → "name")
       ├─ plugin: user-first-ux    skills: user-first-ux, ux-laws, ui-accessibility, ui-ux-copy, ui-research (+ commands ui-a11y, ui-copy)
       ├─ plugin: ui-studio        skills: ui-visual-direction, ui-styles, visual-polish, ui-design-system, ui-critique, ui-handoff,
       │                                   ui-stack-laravel, ui-stack-next, ui-theming, ui-canvas-art (+ 7 commands)
       └─ plugin: orbit-design-engine, system-design, session-orchestrator
```

- **Repo** — the GitHub address users add.
- **Marketplace** — one per repo, defined by `.claude-plugin/marketplace.json`; its `name` is `afyz-forge`
  (independent of the repo name). It lists plugins via `plugins[].source` (a relative path to each
  plugin folder).
- **Plugin** — an independently installable unit. Each lives in its own folder under `plugins/`, with
  `plugins/<name>/.claude-plugin/plugin.json` and `plugins/<name>/skills/`. **Folder name == plugin
  name == marketplace entry name** (a hard convention here, for traceability).
- **Skill** — a folder with a `SKILL.md` (frontmatter `name` must match its directory). Claude Code
  auto-discovers every `skills/*/` under a plugin that has a `SKILL.md`.

## Directory tree (current)

```
afyz-forge/
├── .ai/agents/                     # this context (architecture, conventions, context, publishing)
├── .ai/docs/merge/ · .ai/docs/prompts/   # 2026-11 merge records and git command files
├── .claude-plugin/marketplace.json # marketplace "afyz-forge" → 5 plugins
├── plugins/
│   ├── user-first-ux/              # behaviour: priority order, workflow, WCAG, laws of UX, ethics, states, flows, copy, research
│   ├── ui-studio/                  # look and build: tokens, visual direction, styles, polish, stacks, critique, handoff
│   ├── orbit-design-engine/        # reference-driven motion and app-shell engine (own installer)
│   └── system-design/ · session-orchestrator/
├── scripts/design-audit.mjs        # deterministic UI smell auditor (Node, no deps) — shared tooling
├── evaluations/                    # EVALUATIONS.md, RUBRIC.md, fixtures/
├── docs/                           # ARCHITECTURE.md, CATALOG.md, RESEARCH.md, briefs, archive/omni-design/
├── MIGRATION.md · CHANGELOG.md · README.md · LICENSE · .gitignore
```

## The two UI plugins (split by job, one owner per topic)

**`user-first-ux`** owns how the UI behaves. Skills: `user-first-ux` (priority order honest >
accessible > usable > efficient > consistent > aesthetic, the Read-Report-Plan-Approve-Implement-
Verify-Sync workflow, severity scale, blocking checklist, components, states, ethics, inclusive
context, domains for e-commerce / enterprise / mobile, 8 before/after examples), `ux-laws` (30
laws, audit template, Blade/Livewire stack notes), `ui-accessibility` (WCAG 2.2 AA audit),
`ui-ux-copy` (EN/BM), `ui-research`; commands `ui-a11y`, `ui-copy`; agent `a11y-auditor`; trigger
evals in `evals/`. Every accessibility number lives in
`skills/user-first-ux/references/accessibility.md`.

```
plugins/user-first-ux/
├── .claude-plugin/ · .codex-plugin/ · README.md · agents/a11y-auditor.md
├── skills/user-first-ux/   (SKILL.md + references/ (10 + domains/3) + examples/ (8) + evals/evals.json)
├── skills/ux-laws/         (SKILL.md + references/ (laws ×4, audit-template, guardrails, stack-notes) + evals/)
├── skills/ui-accessibility/ · ui-ux-copy/ · ui-research/ · ui-a11y/ · ui-copy/
└── evals/<skill>/{trigger,no-trigger}-N/
```

**`ui-studio`** owns how the UI looks and is built: 10 model-invoked skills + 7 command skills
(`disable-model-invocation: true`: ui-plan, ui-build, ui-system, ui-theme, polish-audit,
polish-fix, polish-new), 4 read-only agents, a warn-only PostToolUse hook (`hooks/hooks.json` +
POSIX `hooks/check-tokens.sh`), plugin-root shared rules in `references/shared/` (token owner:
`visual-system.md`), the Ten Fixes measurement scripts in `skills/visual-polish/scripts/`, OFL fonts
under `skills/ui-canvas-art/assets/fonts/`, trigger evals in `evals/`, and `NOTICE.md` +
`licenses/` for upstream attribution.

```
plugins/ui-studio/
├── .claude-plugin/plugin.json   ├── agents/ (ui-critic, design-system-auditor, ui-ten-fixes-auditor)
├── skills/ (17)                 ├── hooks/ (hooks.json, check-tokens.sh)
├── references/shared/           ├── evals/<skill>/{trigger,no-trigger}-N/
├── licenses/ · NOTICE.md · README.md
```

**`orbit-design-engine`** is a dedicated reference-driven motion and app-shell engine (26
`orbit-ui-*` skills, reference frames, demos, its own `install.py`). It inherits the host theme and
points to user-first-ux for accessibility numbers.

**`system-design`** is the first non-UI plugin: 3 model-invoked skills (`system-design`,
`distributed-patterns`, `system-design-review`) + 1 manual command skill
(`system-design-interview`), trigger evals in `evals/`, and `NOTICE.md` crediting the
liquidslr/system-design-notes source (prose rewritten, facts kept).

```
plugins/system-design/
├── .claude-plugin/plugin.json   ├── evals/<skill>/{trigger,no-trigger}-N/
├── skills/system-design/        (SKILL.md + references/{estimation,scaling-ladder,stack-mapping}.md + references/cases/ (6))
├── skills/distributed-patterns/ (SKILL.md + references/ (7))
├── skills/system-design-review/ · skills/system-design-interview/
├── NOTICE.md · README.md
```

**`session-orchestrator`** is an agent-workflow plugin: 1 model-invoked skill that turns the main
session into an orchestrator (detect harness and per-call model/effort support, decompose into
session-local role briefs, route by task class, approval gate for writers, verify, clean up), plus 1
leaf-only agent (`role-runner`, `disallowedTools: Agent`) and trigger evals with scaffolded fixture
repos. No hooks, no scripts. Research and sources: `docs/research/session-orchestrator.md`.

```
plugins/session-orchestrator/
├── .claude-plugin/plugin.json   ├── agents/role-runner.md
├── skills/session-orchestrator/ (SKILL.md + references/{detection,routing}.md + assets/{role-brief,manifest}.md)
├── evals/session-orchestrator/{trigger-1..3,no-trigger-1..2}/ (trigger cases: case.yaml + fixture.sh)
├── README.md
```

## Cross-reference rules (do not break)

- **Never reference another plugin by path.** Cross-plugin links go by skill name with a one-line
  fallback (format in `conventions.md`), so each plugin works when installed alone.
- `user-first-ux` sibling skills link `../user-first-ux/references/…` (and `../../user-first-ux/…`
  from a skill's `references/`). Keep the skill folders together.
- `ui-studio` SKILL.md files link shared rules as `${CLAUDE_PLUGIN_ROOT}/references/shared/...`
  (substituted at load); reference files use relative paths. Keep `references/shared/` at the
  plugin root. Ten Fixes scripts: `${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/`.
- `system-design` skills link siblings as `../distributed-patterns/references/...` and
  `../system-design/references/...` (case files use `../../../distributed-patterns/...`). Keep the
  four skill folders together.

See also: `conventions.md` (naming/editing rules), `publishing.md` (git + marketplace workflow),
`context.md` (project history and decisions).
