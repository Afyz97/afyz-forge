# user-first-ux

How a UI **behaves** for its users. One of the two UI plugins in the `afyz-forge` marketplace;
`ui-studio` owns how the UI looks and is built. Each plugin works installed alone: where one needs
the other, it names the skill and gives a one-line minimum.

```bash
claude plugin marketplace add Afyz97/afyz-forge
claude plugin install user-first-ux@afyz-forge
claude plugin validate ./plugins/user-first-ux
```

## What it owns

Priority order (honest > accessible > usable > efficient > consistent > aesthetic), the
Read-Report-Plan-Approve-Implement-Verify-Sync workflow, the severity scale, WCAG 2.2 AA (every
accessibility number lives in `skills/user-first-ux/references/accessibility.md`), the 30 Laws of
UX and Gestalt, ethics and dark patterns, PDPA, UI states, forms, flows, microcopy, BM/EN
localisation and user research.

## Skills

| Skill | Use it for |
|---|---|
| `user-first-ux` | Usability review, flows, forms, onboarding, states, dark patterns, "is this good for users?"; domains for e-commerce, enterprise and mobile; 8 before/after examples |
| `ux-laws` | "Apply Hick's law", audit a screen against the 30 Laws of UX (6 pillars, Pass/Fail, exact element + fix); Blade/Livewire stack notes |
| `ui-accessibility` | WCAG 2.2 AA audit with criterion numbers and severity |
| `ui-ux-copy` | Interface copy in English and Bahasa Melayu |
| `ui-research` | Research plans, interview guides, synthesis |

Commands: `/user-first-ux:ui-a11y <path|url>`, `/user-first-ux:ui-copy <context>`.
Agent (read-only): `a11y-auditor` (keyboard, focus, contrast, targets, reflow, reduced motion;
Playwright when installed).

## Evals

`skills/user-first-ux/evals/evals.json` and `skills/ux-laws/evals/evals.json` (skill-creator
format); trigger cases in `evals/<skill>/` (`claude plugin eval ./plugins/user-first-ux`).

## Moved here in 1.1.0

`ux-laws` (from the former `ux-laws` plugin) and `ui-accessibility`, `ui-ux-copy`,
`ui-research`, `ui-a11y`, `ui-copy`, `a11y-auditor` (from `ui-studio`). See `MIGRATION.md` at the
repository root.

Licence: Apache-2.0.
