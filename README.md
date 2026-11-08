# afyz-forge

A Claude Code plugin **marketplace** (named `afyz-forge`) of Agent Skills for AI coding agents:
UI and UX work split by job, a reference-driven motion engine, system design, agent
orchestration, pre-install skill security and codebase refactoring. Formerly `Afyz97/ai-skills`; upgrading from it: [MIGRATION.md](MIGRATION.md).

## Plugins

| Plugin | Job | Contents |
|---|---|---|
| [`user-first-ux`](plugins/user-first-ux/) | How a UI **behaves** for its users | Priority order (honest > accessible > usable > efficient > consistent > aesthetic), mandatory workflow, usability review, WCAG 2.2 AA audit, 30 Laws of UX + audit, dark-pattern bans, states, forms, flows, EN/BM copy, research. 5 skills, 2 commands, 1 agent. |
| [`ui-studio`](plugins/ui-studio/) | How a UI **looks and is built** | Visual direction, named styles, tokens and design-system audits, visual polish (Ten Fixes with measurement scripts), Laravel (Blade, Livewire 4, Flux UI v2, Filament, Tailwind, Bootstrap 5) and Next.js (React 19, Tailwind v4, Radix) builds, countdowns and time-based UI, critique, handoff, theming, canvas art. 11 skills, 7 commands, 3 agents, a warn-only token hook. |
| [`orbit-design-engine`](plugins/orbit-design-engine/) | Matching a visual or motion **reference** | 26 skills that turn a sample site or video into app shells, dashboards, components, workspace and auth transitions, cinematic motion and visual/motion QA; inherits the host theme; own installer. |
| [`system-design`](plugins/system-design/) | System design (not UI) | 4-step method, estimation, 22 blueprints, distributed-patterns reference, architecture review, mock interviews, Laravel mapping. |
| [`session-orchestrator`](plugins/session-orchestrator/) | Agent orchestration (not UI) | Harness detection, role briefs, model/effort routing, leaf-only role runner, approval gates for writers, verification. |
| [`skill-guard`](plugins/skill-guard/) | Skill security (not UI) | Audits a third-party skill, plugin or marketplace before install: quarantine, read-only stdlib scanner, 12-section threat model, PASS / REVIEW / BLOCK report pinned to a commit SHA. |
| [`codeweave`](plugins/codeweave/) | Refactoring (not UI) | Manual `/codeweave [--audit-only]`: evidence-driven architecture audit and behaviour-preserving refactor of an existing codebase, decision log, read-only repo-map and Git co-change scripts. |

Merged in 2026-11 and removed: `ux-laws` → user-first-ux; `ui-ten-fixes`, `omni-design`,
`ultimate-design-suite` → ui-studio; `atelier-ux` → both (new `ui-studio:ui-countdown`). Where
each skill went: [MIGRATION.md](MIGRATION.md).

**One owner per topic.** Each rule and each number is stated in exactly one place. The other
plugin points to it by skill name and keeps a one-line minimum, so every plugin works installed
alone. Install both UI plugins for the full workflow.

## Installation

```text
/plugin marketplace add Afyz97/afyz-forge
/plugin install user-first-ux@afyz-forge          # behaviour, accessibility, laws of UX, copy, research
/plugin install ui-studio@afyz-forge              # look, tokens, styles, polish, stack builds
/plugin install orbit-design-engine@afyz-forge    # reference-driven motion and app shells (optional)
/plugin install system-design@afyz-forge          # system design (optional)
/plugin install session-orchestrator@afyz-forge   # subagent orchestration (optional)
/plugin install skill-guard@afyz-forge            # audit third-party skills/plugins before install (optional)
/plugin install codeweave@afyz-forge              # architecture audit + behaviour-preserving refactor (optional)
```

**Manual (any agent):** copy the skill folders you want from a plugin's `skills/` directory into
your agent's skills directory (Claude Code: `~/.claude/skills/` or `.claude/skills/`). Copy
user-first-ux skill folders together (they link `../user-first-ux/references/`); ui-studio skills
need the plugin's `references/shared/` folder at the plugin root.

## Usage examples

- "Review the signup form for usability problems." → `user-first-ux`
- "Apply Hick's law to this menu." → `ux-laws`
- "Is this modal accessible?" → `ui-accessibility`
- "This dashboard looks ugly, fix it." → `visual-polish`
- "Make the nav liquid glass." → `ui-styles`
- "Build a member profile card in Blade + Flux." → `ui-stack-laravel` (or `/ui-studio:ui-build` for the full loop)
- "Write the dev handoff spec for this screen." → `ui-handoff`

## Deterministic auditor (optional)

A dependency-free Node script flags **mechanically detectable** smells only (shadow stacks,
backdrop-filter overuse/missing fallback, removed focus, radius repetition, `!important`
spirals, z-index escalation, gradient text, tiny targets). It reports *signals to investigate*,
never verdicts. For measured visual rules use ui-studio's `visual-polish` scripts.

```bash
node scripts/design-audit.mjs [path ...]     # human-readable
node scripts/design-audit.mjs --json src/    # machine-readable
```

## Evaluation

Trigger evals live in each plugin's `evals/` (`claude plugin eval ./plugins/<plugin>`). Older
design-suite cases: [evaluations/EVALUATIONS.md](evaluations/EVALUATIONS.md),
[evaluations/RUBRIC.md](evaluations/RUBRIC.md), [docs/EVALUATION-REPORT.md](docs/EVALUATION-REPORT.md).

## Limitations

- Formal baseline-vs-assisted runs are scaffolded but not executed.
- Liquid glass and spatial UI describe fast-moving Apple platform material; verify current HIG
  before native implementation.
- The deterministic auditor and the Ten Fixes scripts are heuristics; confirm every finding in
  context.

## License

Apache-2.0 ([LICENSE](LICENSE)). Upstream attribution: each plugin's `NOTICE.md`; research notes:
[docs/RESEARCH.md](docs/RESEARCH.md). Changes: [CHANGELOG.md](CHANGELOG.md).
