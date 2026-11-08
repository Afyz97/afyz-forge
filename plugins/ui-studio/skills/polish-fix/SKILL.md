---
name: polish-fix
description: Fix existing UI with the Ten Fixes rules (Read, Report, Plan, Approve, Implement, Verify, Sync). Runs visual-polish in fix mode.
disable-model-invocation: true
argument-hint: "[path | component] [--rules 01,03,06] [--yes to skip approval]"
---
Use the `ui-studio:visual-polish` skill in **fix** mode on: $ARGUMENTS

- If `--rules` is given, only apply those rules (still in numeric order).
- Stop after the Plan step and wait for approval unless `--yes` is present.
- Keep the data contract identical; verify with the same measurements used in the audit
  (`${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/`).
