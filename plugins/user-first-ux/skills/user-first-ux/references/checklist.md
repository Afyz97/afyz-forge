# Verification Checklist

Every item is yes / no. Any "no" blocks "done" unless it is explicitly justified to the user,
with the trade-off named.

- [ ] UX brief answered; assumptions listed as hypotheses
- [ ] Top tasks can be completed in the fewest reasonable steps
- [ ] 5-second test and squint test pass
- [ ] One primary action per view; CTA hierarchy is clear
- [ ] Type scale and spacing tokens only; no ad-hoc values
- [ ] All states from `states-feedback.md` section 1 implemented
- [ ] Forms follow `components.md` section 2; errors are specific and preserve input
- [ ] Keyboard-only pass; focus visible and never obscured
- [ ] Screen-reader pass: names, roles, live regions, heading order
- [ ] Contrast meets A1 (text, large text, UI); nothing relies on colour alone
- [ ] Targets meet A7 (AA minimum and house floor); works at 320px and at 200% zoom
- [ ] `prefers-reduced-motion` and dark mode respected
- [ ] LCP / INP / CLS within targets on a throttled mid-range device
- [ ] No dark patterns; all copy is true; total price visible early
- [ ] Localised strings fit; dates, numbers and currency use the right locale
- [ ] Realistic content, including long, empty and extreme values
- [ ] URL reflects state; Back button works; no lost work

## Reporting the checklist

Paste the list back with each box ticked or left open. For each open box add one line:
why, the user impact, and the follow-up (e.g. "LCP not measured - no device lab here;
run Lighthouse mobile on staging").

Items that cannot be verified in the current environment (screen reader, real device) are
reported as **not verified**, never as passed.
