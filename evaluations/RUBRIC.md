# Design Quality Rubric

Score a design 0–3 per dimension. Use for baseline-vs-assisted comparison and for
`design-review`. **Two guardrails override raw totals:**

- A visually dramatic design that is **unusable or inaccessible cannot score "good" overall**
  — usability/accessibility failures cap the total.
- A technically accessible but **visually generic** design **cannot automatically score high
  on design quality** — genericness caps distinctiveness/task-fit.

## Scale
- **0** — absent/broken. **1** — weak/generic. **2** — solid. **3** — excellent/intentional.

## Dimensions

| # | Dimension | 0 | 1 | 2 | 3 |
|---|-----------|---|---|---|---|
| 1 | **Task fit** | wrong for the task | loosely fits | fits | precisely serves the task/user |
| 2 | **Style fidelity** | not the named style | one CSS effect of it | mostly faithful | fully realizes the design language |
| 3 | **Distinctiveness** | template | slightly varied | has a point of view | memorable, one strong justified move |
| 4 | **Subject specificity** | could be any product | vaguely on-topic | on-topic | unmistakably this product |
| 5 | **Hierarchy** | flat/none | weak | clear | effortless 1-2-3 scan |
| 6 | **Typography** | default/arbitrary | okay | good scale & measure | expressive + readable |
| 7 | **Color** | random/off | generic | coherent roles | intentional, brand-true |
| 8 | **Composition** | chaotic/uniform | basic | balanced | composed with rhythm |
| 9 | **Spacing** | magic numbers | inconsistent | on a scale | precise, intentional density |
| 10 | **Interaction** | states missing | some states | all states | polished feedback |
| 11 | **Accessibility** | fails basics | partial | meets floor | robust (verified) |
| 12 | **Responsiveness** | breaks | shrinks | adapts | recomposed per context |
| 13 | **Motion** | gratuitous/janky | decorative | purposeful | purposeful + reduced-motion |
| 14 | **Performance** | heavy/janky | some risk | reasonable | efficient + fallbacks |
| 15 | **Maintainability** | one-off CSS spiral | some tokens | tokenized | clean system, variants |
| 16 | **Anti-slop avoidance** | full of clichés | some | mostly clean | zero unjustified clichés |

Max 48. Report per-dimension scores, not just the total; the total hides a capped failure.

## Interpreting
- **Ship:** no dimension at 0; accessibility ≥2; no capped failure; total ≥36.
- **Fix-then-ship:** isolated 1s with clear fixes; no accessibility/usability 0.
- **Rework:** any accessibility/usability 0, or distinctiveness+task-fit both ≤1 (generic),
  or style fidelity 0 when a style was requested.

## Baseline-vs-assisted use
Run the same prompt with and without the suite; score both; the suite should raise
distinctiveness, style fidelity, subject specificity, accessibility, and anti-slop — **not
merely produce longer output.** If the assisted output is only longer without higher scores,
the skill needs work.
