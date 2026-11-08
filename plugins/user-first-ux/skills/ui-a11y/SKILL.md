---
name: ui-a11y
description: Shortcut for a WCAG 2.2 AA accessibility audit of a file, component or URL. Runs the ui-accessibility skill.
disable-model-invocation: true
argument-hint: "<path or url>"
---

Use the `user-first-ux:ui-accessibility` skill to audit: $ARGUMENTS

If no target was given, ask for a file path or URL. For a URL or a running app, delegate the
browser passes (keyboard, focus, contrast, 200% zoom) to the `a11y-auditor` agent and merge its
findings into the report.
