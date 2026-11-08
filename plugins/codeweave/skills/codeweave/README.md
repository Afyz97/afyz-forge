# CodeWeave - v1.0.1

An evidence-driven, behavior-preserving architecture audit and refactoring **Agent Skill** expanded from the original `untangle-codebase` workflow. Portable `SKILL.md` plus read-only analysis helpers.

## Contents

- `SKILL.md` - activation metadata and complete workflow.
- `references/decision-log-template.md` - durable, evidence-based refactoring decision log.
- `references/review-protocol.md` - optional subagent roles and integration rules.
- `references/verification-and-frameworks.md` - checks and dynamic-discovery hazards.
- `scripts/repo_audit.py` - read-only repository inventory and special-case leads.
- `scripts/git_cochange.py` - read-only Git co-change evidence.

## Installation (copy the **whole** folder)

| Host | Project | Personal |
| --- | --- | --- |
| Claude Code | `.claude/skills/codeweave/` | `~/.claude/skills/codeweave/` |
| Codex / Codex VS Code | `.agents/skills/codeweave/` | `~/.agents/skills/codeweave/` |

Use `/codeweave` for Claude Code; explicitly ask Codex to **use `$codeweave`**. Claude's `disable-model-invocation: true` makes its refactor workflow manually invoked there. Codex may not enforce that Claude-specific frontmatter key; the description also restricts it to explicit requests.

Example prompts:

- `/codeweave --audit-only`
- `/codeweave focus on Laravel controllers, services and stored procedures`
- `Use $codeweave to audit-only the dependency boundaries of this TypeScript app.`
- `Use $codeweave to refactor the repository, preserve existing behavior, and log the evidence.`

Read-only helper examples (paths relative to skill directory):

```bash
python scripts/repo_audit.py --root /path/to/project --format markdown
python scripts/repo_audit.py --root /path/to/project --format json --top 15
python scripts/git_cochange.py --root /path/to/project --commits 150 --min-count 3
```

Python 3.9+ recommended; only standard library modules. Scripts print to stdout and never change project files. Heuristics **cannot replace** source inspection.

The skill honors a project's existing `.ai/agents/` knowledge conventions and only suggests `.ai/docs/plans/` and `.ai/docs/handoffs/` as optional execution artifacts. It does not modify knowledge files automatically.

## Portability note

Unknown/host-specific YAML frontmatter keys may be ignored by some Agent Skills hosts. The main `name` and `description` fields remain portable; Claude-specific invocation controls are intentionally optional.
