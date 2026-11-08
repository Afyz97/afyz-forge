# session-orchestrator

Turns the main Claude Code (or Codex) session into an orchestrator for multi-part work. It
detects what the harness can do, splits the task into session-local roles with self-contained
briefs, routes each role to a model and effort level, delegates to leaf-only workers, and then
verifies, reports and cleans up.

## What it does

1. **Detects the environment**: which harness is running (Claude Code, Codex, other), whether the
   Agent tool accepts per-call `model` and `effort`, whether env variables override them, and
   which version is running. It prints one mode line before planning.
2. **Decomposes the task** into roles tailored to the repo's real stack and files. Briefs are
   temporary files in a gitignored session folder. They are not native subagent definitions, and
   nothing is written to `.claude/agents/`.
3. **Routes each role** by task class: lookups to `haiku`/`low`; implementation to `sonnet`; security,
   migrations, debugging and architecture to `opus`/`high`. It uses aliases, never pinned model IDs.
4. **Delegates** each role to the bundled `role-runner` agent, which has no Agent tool and so cannot
   delegate further. If role-runner is missing it falls back to the built-in `general-purpose` agent.
5. **Collects and verifies** the result files, compares git state before and after, updates the
   session manifest, reports and deletes the session folder.

## Skills and agents

| Component | Invocation | What it does |
|---|---|---|
| `session-orchestrator` (skill) | Automatic, or `/session-orchestrator:session-orchestrator` | The orchestration workflow above |
| `role-runner` (agent) | Dispatched by the skill only | Leaf worker: runs one brief, writes one result file, never delegates, never touches git |

## Safety model

- **Approval gate.** Read-only roles start as soon as the plan is shown, but only when you asked for
  orchestration. Any role that writes project files waits for you to approve the plan.
- **Disjoint ownership.** Parallel writers never share a file. Overlaps run in sequence.
- **Leaf-only workers.** `role-runner` has `disallowedTools: Agent`. In the general-purpose fallback
  the rule goes into the prompt and is checked afterwards.
- **No git mutation by roles.** The orchestrator records `HEAD`, the branch and `git status` before
  writers run. If any of them changed, it stops and reports.
- **Untrusted output.** Result files are read as data. Instructions inside them are reported, not
  followed. Claims are re-checked before they reach you.
- **No secrets.** Briefs and the manifest never contain env values, tokens or `.env` contents.
  Detection reads named variables only.
- **Sanitized paths.** Role and task names become `[a-z0-9-]`, at most 40 characters.

## Requirements

| Capability | Minimum |
|---|---|
| Full routing (per-call model and effort) | Claude Code 2.1.292 |
| Per-call model reliably beats `CLAUDE_CODE_SUBAGENT_MODEL` | Claude Code 2.1.251 |
| role-runner leaf guarantee (`disallowedTools` on plugin agents) | Claude Code 2.1.78 |
| Per-call model at all | Claude Code 2.1.72 |
| Codex | `spawn_agent` available (effort via `reasoning_effort`) |

Older versions and other harnesses still work in one of the degraded modes below.

## Modes

The skill picks one and says so, for example
`Mode: full routing (Claude Code 2.1.312, role-runner agent, no env overrides)`.

| Mode | When | Behaviour |
|---|---|---|
| full routing | Agent tool has `model` and `effort`, no override | model and effort per role |
| model routing only | no per-call `effort`, or `CLAUDE_CODE_EFFORT_LEVEL` set | `effort` omitted on every call |
| effort routing only | no per-call `model`, or `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (or `CLAUDE_CODE_SUBAGENT_MODEL` before 2.1.251) | `model` omitted |
| roles only | neither dimension can be routed | same model; roles, briefs and gates still apply |
| inline | no delegation tool | the main session runs each role itself, one after another |

If the session cannot run a shell, env overrides are reported as unknown. Anything you tell it about
your environment is used instead. Admin caps (`maxEffortLevel`, `availableModels`) cannot be seen,
so the final report notes that routed choices may have been capped.

## Configuration

| Setting | How |
|---|---|
| Temp folder | Default `.session-orchestrator/` at the project root. Override by naming a folder in your request, or with `SESSION_ORCHESTRATOR_DIR` (must resolve inside the project). |
| Model or effort for a role | Say it in the request ("use opus for the migration role"). Your choice beats the routing table. |
| Strongest tier | `opus` by default. Ask for `fable` explicitly if your plan has it. |
| Keep session files | Say "keep the session folder". Failed or partial runs are kept automatically. |

Env variables that override per-call choices, and so switch the mode: `CLAUDE_CODE_EFFORT_LEVEL`,
`CLAUDE_CODE_SUBAGENT_MODEL_FORCE`, and `CLAUDE_CODE_SUBAGENT_MODEL` on versions before 2.1.251.

## Session folder

```
.session-orchestrator/
  .gitignore                 # contains "*": ignores the folder in any repo, your .gitignore is untouched
  20261031-0930-csv-export/
    manifest.md              # task, mode, plan, approval, git baseline, log, outcome
    roles/<role>.md          # one brief per role
    results/<role>.md        # one result per role, fixed sections
```

The session folder is deleted at the end, and the root goes too once it is empty. Folders from
other or crashed sessions are listed and offered for deletion, never removed automatically.

## Install

```
/plugin marketplace add Afyz97/afyz-forge
/plugin install session-orchestrator@afyz-forge
```

Try it:

- "Split this up and use subagents: add a CSV export endpoint, tests and docs."
- "Orchestrate a read-only audit of TODOs, dead code and auth issues."
- "Delegate this refactor; use opus for the schema migration part."

## Layout

```
plugins/session-orchestrator/
  .claude-plugin/plugin.json
  agents/role-runner.md
  skills/session-orchestrator/
    SKILL.md
    references/detection.md   harness, parameter and env detection, modes, cleanup commands
    references/routing.md     tiers, full routing table, precedence, escalation, cost notes
    assets/role-brief.md      brief template with the output contract
    assets/manifest.md        session manifest template
  evals/session-orchestrator/ 3 trigger cases (feature build, read-only audit, effort pinned) + 2 no-trigger
```

## Validate and test

```
claude plugin validate --strict ./plugins/session-orchestrator
claude plugin eval ./plugins/session-orchestrator --ablation none --allow-tools Write Edit --scaffold --trust-plugin
```

`--scaffold` runs each case's `fixture.sh`, which creates a small Node repo in the eval workspace.
It runs as you, outside the sandbox. `--ablation none` skips the no-plugin baseline, where the
`role-runner` agent would not exist. The effort case simulates the env override through the
prompt, because eval runs on native Windows cannot run a shell. A real
`CLAUDE_CODE_EFFORT_LEVEL` check needs an interactive or `claude -p` session. Add `--keep-temp` to
inspect the Agent calls in each run's trace (delete the kept `claude-eval-*` folders afterwards),
and `--case "session-orchestrator--trigger-*"` to run a subset; `--case` takes a simple glob.

## Limitations

- Git safety is detected afterwards, not prevented. A role that ignores its brief and commits is
  caught and reported, not undone.
- The skill cannot see admin model or effort caps, or how an alias maps on Bedrock, Vertex or Foundry.
- Codex support is tested on one read-only audit (Codex CLI 0.164.0): effort routing, delegation and
  reporting worked, but Codex kept briefs in the conversation instead of the session folder when told
  not to change project files. Writer roles on Codex are untested.
- Inline mode gives the same structure and reports, but no isolation and no routing.

Research notes and sources: [docs/research/session-orchestrator.md](../../docs/research/session-orchestrator.md).
