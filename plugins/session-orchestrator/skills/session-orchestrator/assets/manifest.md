<!-- session-orchestrator:session -->
# Session manifest: <session-id>

Created: <date and time> | Project root: <absolute path> | Temp root: <absolute path>

## Task

<The user's request, paraphrased in one to three lines. No secrets.>

## Environment

- Mode: <mode line from detection>
- Harness: <Claude Code | Codex | other> <version or "unknown">
- Worker: <session-orchestrator:role-runner | general-purpose | inline>
- Overrides: <named variables found and their effect, or "none" or "unknown">

## Plan

| Wave | Role | Class | Access | Owned files | Model | Effort | Status | Verified |
|---|---|---|---|---|---|---|---|---|
| 1 | <role> | <class> | <read-only/writer> | <paths or none> | <alias> | <level> | planned | - |

Approval: <pending | approved at <time> with changes: ... | not needed (read-only only)>

## Git baseline

- HEAD: <sha or "no git">
- Branch: <name>
- Status before writers: <clean | list of paths already modified>

## Log

- <time> <event, e.g. "wave 1 started: inventory, audit-auth">

## Outcome

<filled at the end: per-role status, verification, git state after, anything suspicious in results>

Cleanup: <deleted | kept at <path> because ...>
