---
name: ui-build
description: Full UI build loop for a brief - plan, self-review, approval gate, build in the detected stack (Laravel or Next.js), copy pass, critique and accessibility check.
disable-model-invocation: true
argument-hint: "<brief>"
---

Brief: $ARGUMENTS

Work inside `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`. Steps:

1. **Read.** Detect the stack: `composer.json` with livewire/flux/filament -> Laravel;
   `package.json` with `next` -> Next.js; otherwise ask. Read existing tokens and components.
2. **Plan.** Run pass 1 and the self-review from `ui-studio:ui-visual-direction` (token plan,
   ASCII wireframes, AD1-AD10 check). If this conversation already holds an approved plan from
   `/ui-studio:ui-plan`, reuse it.
3. **Approve.** Show the reviewed plan and **stop**. Continue only after the user approves.
   (Skip only if the user explicitly said to proceed without asking, and say so.)
4. **Build.** Implement with `ui-studio:ui-stack-laravel` or `ui-studio:ui-stack-next`:
   tokens first, then components with all eight states, then the screen.
5. **Copy.** Replace every placeholder string using `user-first-ux:ui-ux-copy` if installed (EN, and BM if the
   project has `lang/ms` or `messages/ms.json`).
6. **Critique.** Delegate to the `ui-critic` agent (read-only) with the changed files and the
   brief; fix Critical and High findings.
7. **Accessibility.** Check the quality floor and the A-rules with `user-first-ux:ui-accessibility`
   on the changed files; for a running app, delegate to its `a11y-auditor` agent (user-first-ux
   plugin, if installed).
8. **Polish.** Run `ui-studio:visual-polish` (audit mode, then fix what fails); refine, do not
   add (DP8).
9. **Report.** Completed user-first-ux checklist (items not verifiable here marked "not verified"),
   trade-offs named, open hypotheses, files changed. Do not commit.
