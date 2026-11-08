# Routing

Route on what a wrong answer costs and how easily you can check it, not on how big the task looks.
Cheap tiers are right when you can verify the output mechanically; strong tiers are right when the
work has to be discovered or a mistake is expensive to undo.

## Tiers

| Tier | Claude Code alias | Codex | Use for |
|---|---|---|---|
| cheap | `haiku` | inherit model, `reasoning_effort` low or medium | short, checkable output |
| mid | `sonnet` | inherit model, `reasoning_effort` medium or high | implementation and review with a clear spec |
| strong | `opus` | inherit model, `reasoning_effort` high | discovery, high blast radius, hard to reverse |
| strongest (opt-in) | `fable` | user-named model | only when the user asks; it costs more and is not on every plan |

Use aliases, never pinned version IDs. Aliases resolve to the newest model the user's provider and
plan allow; a pinned ID breaks on other providers and goes stale. The Agent tool accepts only
`sonnet`, `opus`, `haiku` and `fable` per call (not `best`, `inherit` or full IDs).

In Codex, models are named by the user's configuration, so vary `reasoning_effort` and leave
`model` unset unless the user named one. In other harnesses (inline mode) routing does not apply.

## Full table

| Task class | Tier | Model | Effort | Rationale |
|---|---|---|---|---|
| lookup, search, inventory, file mapping | cheap | `haiku` | `low` | short output the orchestrator can check |
| summaries, docs and comment drafts | cheap | `haiku` | `medium` | low risk, but prose needs some judgment |
| tests, small isolated fixes | mid | `sonnet` | `medium` | checkable by running it, moderate judgment |
| feature implementation | mid | `sonnet` | `high` | multi-file judgment, verified afterwards |
| refactor within one module | mid | `sonnet` | `medium` | behaviour-preserving, tests check it |
| review of another role's output | mid | `sonnet` | `high` | an independent check needs reasoning, not breadth |
| debugging with unknown root cause | strong | `opus` | `high` | the work has to be discovered, not executed |
| security, auth, secrets, crypto | strong | `opus` | `high` | a missed finding costs the most |
| data or schema migrations | strong | `opus` | `high` | hard to reverse, data-loss risk |
| architecture, cross-cutting design | strong | `opus` | `high` | errors compound across every later role |
| anything unclassifiable | mid | `sonnet` | `medium` | safe middle; say you could not classify it |

Effort levels a model does not support fall back to the highest supported level at or below the
one requested, so `high` is a safe ceiling across providers. Do not route `xhigh` or `max` unless
the user asks: they are slower and costlier, and not every model has them.

## Precedence

1. The user's explicit choice for a role, or for all roles ("use opus for everything").
2. A class rule above.
3. If the mode cannot route a dimension, omit it from the call; the session default or an env
   override applies. Show `(session default)` or `(pinned by env)` in the plan.

## Escalation

When a role fails or its result does not verify:

1. Retry once on the same tier, adding the failure output and the specific gap to the brief. Many
   failures are missing context, not missing capability.
2. Retry once on the next tier up (cheap to mid, mid to strong).
3. Stop. Report what failed and what you tried. Do not loop.

Do not escalate past `opus` to `fable` on your own.

## Cost notes

- Every fresh role agent re-reads a large prefix (system prompt, tool definitions, skill list)
  before doing anything, so a tiny task on a cheap model can still cost more than doing it inline.
  Merge tiny roles.
- Claude Code caps concurrent subagents (20 by default). Keep waves well under that.
- Roles that share model, effort and agent type and start close together can reuse a prompt cache;
  grouping same-model roles in one wave helps.
