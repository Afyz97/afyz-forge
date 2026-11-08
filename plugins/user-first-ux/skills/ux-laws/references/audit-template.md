# Audit Template

Use this exact format for every UX audit, whether the user asked for one or it is the
self-check before declaring UI work done.

## Rules for filling it in

- **One row per finding.** A pillar with no findings gets one ✅ row with a short reason.
- **Status:** write the word with the symbol, never the symbol alone: `✅ Pass` · `❌ Fail` ·
  `➖ N/A` (give the reason, e.g. "no multi-step flow").
- **Element** names something a reviewer can point at: visible label plus `file:line`,
  a selector, or a component name. Never "the page" or "some buttons".
- **Issue** is observable ("28px tall, bottom-left, same style as Cancel"), not an opinion ("looks weak").
- **Fix** is concrete enough to implement without guessing: class names, sizes, copy, position.
- **Law** uses the tags from SKILL.md (`Fitts`, `Hick`…); list every law the finding breaks.
- **Severity** (user-first-ux scale): **Critical** blocks the user · **High** misleads ·
  **Medium** slows the user or causes errors · **Low** polish.
- **A pillar passes** only if it has no ❌ rows. **Score** = pillars passed / 6.
- **Verdict:** **Ship** = 6/6 and all guardrails ✅ · **Fix first** = any Critical or High, or a guardrail ❌,
  fixable in place · **Rework** = the flow or structure is wrong (fixes would be redesign).
- Guardrails are reported separately and override the score: a guardrail ❌ is never "Ship".
- **Self-audits of your own work** (built, not yet tested) may not say plain "Ship". Use
  **"Ship after: <checks>"**, listing every not-verified item and open hypothesis that could
  change a result. A self-audit grading everything ✅ with nothing listed as not verified is
  a sign it was not done honestly.
- Anything that could not be checked (live timing, screen reader, real data) is marked
  **not verified**, never ✅.

## Format

```
## UX Audit — <screen name> (<file path>)
Verdict: <Ship / Fix first / Rework>   Score: <x>/6 pillars pass

| Pillar | Status | Element | Issue | Law | Fix | Severity |
|--------|--------|---------|-------|-----|-----|----------|
| Easy to reach | ❌ Fail | "Save" button (form.blade.php:88) | 28px tall, bottom-left, same style as Cancel | Fitts, Von Restorff | min-h-11, after last field, filled primary; Cancel as link | High |

Guardrails: A11y ✅/❌ · Ethics ✅/❌ · States ✅/❌
<one line per guardrail ❌, with element and fix>

Top 3 fixes (highest impact first):
1. …
2. …
3. …

Not verified: <items needing a browser, real device or real data>
Open hypotheses: <assumptions to validate with users, and how>
```

## Worked example

Screen: a member registration form, 14 fields in one column, "Submit" and "Reset" side by
side at the bottom left, both grey, 32px tall; phone field rejects dashes; no success page.

```
## UX Audit — Member registration (resources/views/livewire/register.blade.php)
Verdict: Fix first   Score: 2/6 pillars pass

| Pillar | Status | Element | Issue | Law | Fix | Severity |
|---|---|---|---|---|---|---|
| Easy to reach | ❌ Fail | "Submit" (register.blade.php:142) | 32px tall, grey, identical to "Reset" beside it | Fitts, Von Restorff | Filled primary `min-h-11 px-5`; label "Create account" | High |
| Easy to reach | ❌ Fail | "Reset" (register.blade.php:143) | Destructive action adjacent to Submit; one mis-tap wipes 14 fields | Fitts | Remove Reset; offer "Cancel" as a link away from the primary | High |
| Easy to reach | ❌ Fail | Phone input (register.blade.php:61) | Rejects `012-345 6789` | Postel | Accept spaces/dashes/+60; normalise server-side | Medium |
| Fewer choices | ✅ Pass | — | Only required decisions asked; no plan or add-on choices | — | — | — |
| Shows progress | ❌ Fail | Form + submit flow | No sections or progress; submit redirects to blank list | Zeigarnik, Peak-End | 3 titled sections with "Section 2 of 3"; success page with member no. and next step | Medium |
| Familiar patterns | ✅ Pass | — | Standard inputs, labels above fields | — | — | — |
| Clear hierarchy | ❌ Fail | Field labels (register.blade.php:20-120) | 16px gap label→field equals gap field→field; labels float | Proximity | `space-y-2` label→field, `space-y-6` between fields, `space-y-10` between sections | Medium |
| Less to hold | ❌ Fail | Whole form | 14 fields in one undivided group | Miller, Chunking | `<fieldset>` sections: About you (4), Contact (5), Membership (5) | Medium |

Guardrails: A11y ❌ · Ethics ✅ · States ❌
- A11y: errors not linked to fields → add `aria-invalid` + `aria-describedby`, focus first error.
- States: no loading state on submit → submit via `wire:submit` (auto-disables the button) and show "Creating account…" with `in-data-loading:inline`.

Top 3 fixes (highest impact first):
1. Make "Create account" the single filled primary at the house target floor; remove Reset.
2. Chunk into 3 titled sections with progress; add a success page with member number.
3. Accept flexible phone formats; link errors to fields.

Not verified: submit response time on production; screen-reader announcement of errors.
Open hypotheses: most registrants are on mobile (check analytics); "Membership type" can default to "Ordinary" (check last year's split).
```
