# Workflow: Redesign Existing UI

Improving a UI that already exists. **The prime directive: preserve what works and don't break
functionality.** Redesign is surgery, not demolition.

1. **Inspect before touching anything** — read the implementation. Detect the stack, the design system,
   the component patterns, the routes, and the data flow. → `adapters/`.
2. **Identify what to preserve** — working functionality, established conventions the user relies on,
   auth, validation, i18n/RTL, existing loading/error/empty states, useful density. Preserving these
   is not optional. 
3. **Audit the current design** — find the *real* problems (hierarchy, consistency, a11y, IA, states),
   ranked by impact. → `../../ui-critique/references/scored-audit.md`, the `ui-critique` skill.
4. **Classify brand vs product per surface** and set the target direction — usually *extend* the
   existing system, not replace it. → `../../ui-styles/references/style-router.md`, `../../ui-design-system/references/token-architecture.md`.
5. **Rank changes by impact** — fix blockers and accessibility first, polish last
   (`../../ui-critique/references/scored-audit.md` §Severity). Don't repaint the whole app to make one point.
6. **Refactor incrementally** — change within the existing framework and token system; match existing
   conventions; add dependencies only with justification. **Do not rewrite the whole frontend or swap
   frameworks** without authorization.
7. **Verify no functional regressions** — the redesigned flow still works end-to-end: forms submit,
   validation fires, auth holds, routes work, states render. Test, don't assume.
8. **Responsive + accessibility + motion passes** — L3 and L9 (`../../../references/shared/visual-system.md`), the user-first-ux accessibility floor (`ui-accessibility` skill),
   M1 (`../../../references/shared/visual-system.md`).
9. **Anti-slop screen + independent review** — AD1-AD10 (`../../../references/shared/ai-defaults.md`), `../../ui-critique/references/scored-audit.md`.

Special case — **"reduce the AI look" / "make it less generic":** run AD1-AD10 (`../../../references/shared/ai-defaults.md`), kill
default gradients/glass/rounded-everything, introduce a real direction and one distinctive move, vary
section rhythm, replace fake content. Gate: the checklist in the user-first-ux skill (if installed) and `../../../references/shared/quality-floor.md`.
