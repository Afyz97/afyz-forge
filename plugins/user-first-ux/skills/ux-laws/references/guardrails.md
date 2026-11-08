# Guardrails (checked on every build and every audit)

Guardrails sit above the laws. A law is never applied in a way that breaks one of these.
Read before declaring any UI work done, and for every audit. The rules are owned by the
user-first-ux skill in this plugin; the tags below are what the audit template reports.

| Tag | Owner | Covers |
|---|---|---|
| `[A11y]` | `../../user-first-ux/references/accessibility.md` (A1-A16) | contrast, keyboard, focus, labels, colour alone, targets, motion, semantics, errors, reflow, forms |
| `[Ethics]` | `../../user-first-ux/references/ethics-privacy.md` (EP1-EP7) | banned dark patterns, cancel = signup, total price early, privacy by default, truthful nudges, AI labelling |
| `[States]` | `../../user-first-ux/references/states-feedback.md` (ST, FP, ER) | empty, loading, error, partial, success, availability, content stress |

A guardrail ❌ caps the verdict at "Fix first". Missing empty, loading or error states are at
least **High**. Items that cannot be tested here (screen reader, real device) are reported as
**not verified**, never as passed.
