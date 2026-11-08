---
name: polish-new
description: Build a new screen or component that passes all Ten Fixes rules. Runs visual-polish in build mode.
disable-model-invocation: true
argument-hint: "<what to build> [stack: tailwind|css|blade|vue|react|svelte|flutter|swiftui]"
---
Use the `ui-studio:visual-polish` skill in **build** mode to create: $ARGUMENTS

Detect the stack from the repo if not stated. Tokens first, then components, then the screen.
Finish with a self-audit table (all ten rules) using
`${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/` and fix anything below pass.
