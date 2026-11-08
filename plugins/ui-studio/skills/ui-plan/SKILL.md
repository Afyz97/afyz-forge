---
name: ui-plan
description: Produce a visual plan for a UI brief - UX brief, token plan (named hex colours, type roles) and ASCII wireframes with a self-review - without writing any code.
disable-model-invocation: true
argument-hint: "<brief>"
---

Plan only. **Do not write or edit code in this command.**

Brief: $ARGUMENTS

1. Read the repo enough to know the stack (`composer.json`, `package.json`) and any existing
   tokens or components; reuse them in the plan.
2. Answer the UX brief from `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`
   (users, top 3 tasks, context, success, hypotheses). If the brief lacks a subject, audience
   or the screen's job, propose one and ask.
3. Follow pass 1 and the self-review of the `ui-studio:ui-visual-direction` skill, filling its
   `references/plan-template.md`: 4-6 named hex colours with roles, type roles, one-sentence
   layout options with ASCII wireframes and alignment, the one loud element, page principles.
4. Self-review against the brief and AD1-AD10; list what changed and why.
5. End with: open questions, and "Reply `go` (or run `/ui-studio:ui-build`) to build this plan."
