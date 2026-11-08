---
name: polish-audit
description: Audit a screen or component against the Ten Fixes rules (read-only, scored report). Runs visual-polish in audit mode.
disable-model-invocation: true
argument-hint: "[path | url | selector] e.g. resources/views/dashboard.blade.php"
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(node:*), Bash(npx playwright:*)
---
Use the `ui-studio:visual-polish` skill in **audit** mode on: $ARGUMENTS

If no target is given, find the main app layout and the 3 most-used views and audit those.
Run the static linter first:
`python3 ${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/ui_lint.py <paths> --component-scope`
If a dev server URL is known, also run
`node ${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/playwright_probe.mjs <url> "<selector>" ten-fixes-audit`.
Do not edit any files. End with the fix order and offer `/ui-studio:polish-fix`.
