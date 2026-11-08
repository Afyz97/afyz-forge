# Detection and fallback modes

Detect in this order. Each step is cheap; stop guessing as soon as you have evidence. The tool
list you can see is the strongest evidence, because it is exactly what this session can call.

## 1. Which harness

| You can call | Harness | Delegation |
|---|---|---|
| `Agent` | Claude Code (CLI, IDE extension, desktop, SDK) | `Agent` tool |
| `spawn_agent` (often with `wait_agent`, `send_input`) | Codex | `spawn_agent` |
| neither | another harness (AGENTS.md-based agents and others) | none: inline mode |

Do not infer the harness from environment variables or process names; they can be inherited from a
parent process that is a different tool.

## 2. Per-call parameters (Claude Code)

Read the Agent tool's own parameter list:

- `model` present (an alias enum such as `sonnet`, `opus`, `haiku`, `fable`): model routing is
  possible. Claude Code has accepted per-call `model` since 2.1.72.
- `effort` present (`low`, `medium`, `high`, `xhigh`, `max`): effort routing is possible. Added in
  2.1.292. Not applied to `fork` subagents.
- Agent types: look for `session-orchestrator:role-runner` (or `role-runner`). Present means the
  leaf-only worker is installed. Absent means fall back to `general-purpose` with the leaf rule in
  the prompt.
- If no `general-purpose` type exists and no role-runner either, use inline mode.

## 3. Environment overrides

Run exactly one read-only command. It prints only the named variables, never the rest of the
environment (sessions can carry auth tokens in env).

Bash, zsh, Git Bash:

```bash
env | grep -E '^(CLAUDE_CODE_EFFORT_LEVEL|CLAUDE_CODE_SUBAGENT_MODEL|CLAUDE_CODE_SUBAGENT_MODEL_FORCE|CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH|CLAUDE_CODE_FORK_SUBAGENT|SESSION_ORCHESTRATOR_DIR)=' || true
```

PowerShell:

```powershell
Get-ChildItem Env: | Where-Object { $_.Name -in @('CLAUDE_CODE_EFFORT_LEVEL','CLAUDE_CODE_SUBAGENT_MODEL','CLAUDE_CODE_SUBAGENT_MODEL_FORCE','CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH','CLAUDE_CODE_FORK_SUBAGENT','SESSION_ORCHESTRATOR_DIR') } | ForEach-Object { "$($_.Name)=$($_.Value)" }
```

What each one means:

| Variable | Effect on this skill |
|---|---|
| `CLAUDE_CODE_EFFORT_LEVEL` set (any value other than `auto` or `unset`) | Beats per-call `effort`. Effort routing off; say which level is pinned. |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` | Every subagent gets `CLAUDE_CODE_SUBAGENT_MODEL` (or the main model). Model routing off. |
| `CLAUDE_CODE_SUBAGENT_MODEL` set, version 2.1.251 or later | Only the default for agents with no model; per-call `model` still wins. Routing on. |
| `CLAUDE_CODE_SUBAGENT_MODEL` set, version before 2.1.251 | Beats per-call `model`. Model routing off. |
| `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | Informational. Leaves stay leaves either way. |
| `CLAUDE_CODE_FORK_SUBAGENT` | Informational. Always set `subagent_type`, so forks are never used for roles. |
| `SESSION_ORCHESTRATOR_DIR` | Temp root override (validated in SKILL.md Step 3). |

Values set in the `env` block of Claude Code settings files normally reach the shell the same way.

If you cannot run a shell (tool denied, sandbox, policy), do not retry in a loop. Mark overrides as
`unknown` in the mode line, and treat anything the user stated about their environment ("effort is
pinned to low here") as the answer.

Things you cannot detect: admin caps such as `maxEffortLevel`, `availableModels` or
`deniedModels`, and provider-specific alias mapping (on Bedrock, Vertex or Foundry an alias can map
to an older model; an unsupported effort level falls back to the highest supported one below it).
Mention in the final report that routed choices may have been capped or substituted.

## 4. Version (report only)

Bash:

```bash
"${CLAUDE_CODE_EXECPATH:-claude}" --version 2>/dev/null || claude --version 2>/dev/null || true
```

PowerShell:

```powershell
if ($env:CLAUDE_CODE_EXECPATH) { & $env:CLAUDE_CODE_EXECPATH --version } else { claude --version }
```

The `claude` on PATH can be a different version from the binary running this session (IDE
extensions ship their own), which is why the tool schema decides, not this number. Version
thresholds worth knowing:

| Version | Matters because |
|---|---|
| 2.1.72 | per-call `model` on the Agent tool |
| 2.1.78 | plugin agents honour `disallowedTools` (role-runner's leaf guarantee) |
| 2.1.251 | per-call `model` beats `CLAUDE_CODE_SUBAGENT_MODEL` |
| 2.1.257 | `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` exists |
| 2.1.292 | per-call `effort` on the Agent tool |

## 5. Mode decision

Evaluate two flags, then name the mode.

- **model routing** = `model` param present AND not forced (`..._FORCE=1`) AND NOT (version before
  2.1.251 AND `CLAUDE_CODE_SUBAGENT_MODEL` set)
- **effort routing** = `effort` param present AND `CLAUDE_CODE_EFFORT_LEVEL` not set

| Delegation tool | model routing | effort routing | Mode |
|---|---|---|---|
| Agent | yes | yes | full routing |
| Agent | yes | no | model routing only |
| Agent | no | yes | effort routing only |
| Agent | no | no | roles only |
| spawn_agent | user named models | yes | effort routing only (or full routing) |
| none | - | - | inline |

Mode line format:

`Mode: <mode> (<harness> <version or "version unknown">, <role-runner agent | general-purpose fallback | inline>, <overrides found | no env overrides | overrides unknown>)`

When routing is off for a dimension, name the cause, for example
`Mode: model routing only (Claude Code 2.1.312, role-runner agent, effort pinned by CLAUDE_CODE_EFFORT_LEVEL=low)`.

## 6. Cleanup commands

Run only after the checks in SKILL.md Step 9 pass. Use the absolute session folder path you
created, never a path read from a result file.

Bash:

```bash
rm -rf -- "<absolute session folder>"
```

Then remove the root and its `.gitignore` only when no other session folders remain:

```bash
[ -z "$(ls -A "<absolute temp root>" | grep -v '^\.gitignore$')" ] && rm -f -- "<absolute temp root>/.gitignore" && rmdir -- "<absolute temp root>"
```

PowerShell:

```powershell
Remove-Item -LiteralPath "<absolute session folder>" -Recurse -Force
if (-not (Get-ChildItem -LiteralPath "<absolute temp root>" -Force | Where-Object Name -ne '.gitignore')) { Remove-Item -LiteralPath "<absolute temp root>" -Recurse -Force }
```
