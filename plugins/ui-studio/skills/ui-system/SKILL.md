---
name: ui-system
description: Shortcut for design-system work - audit, document a component, or extend with a new pattern. Runs the ui-design-system skill.
disable-model-invocation: true
argument-hint: "audit | document <component> | extend <pattern>"
---

Use the `ui-studio:ui-design-system` skill with: $ARGUMENTS

For `audit`, delegate the grep pass (hardcoded hex, arbitrary Tailwind values, inline styles,
off-scale spacing) to the `design-system-auditor` agent, then fill the audit template with its
counts. With no argument, ask which of the three modes is wanted.
