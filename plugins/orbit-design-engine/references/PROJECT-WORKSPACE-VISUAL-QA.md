# Reference D — visual-and-motion QA acceptance sheet

**Evidence sources:** the user-provided 6.175s clip sampled at 0–6.0s, and local images `assets/project-workspace-reference/` with labelled strips. The product footage occupies the video center; do not compare to promotional title or static code panel.

| Sequence | Reference checkpoints | Acceptance | Negative tests |
|---|---|---|---|
| Dashboard initial | `00-dashboard-initial.jpg`, `01-dashboard-progress.jpg`, `02-dashboard-complete.jpg`, `sequence-counter.jpg` | Correct data appears progressively; animated bars align with real metrics; never jump layout | Reload, cached data, 0 count, negative/decimal, reduced motion |
| Navigation Tasks | `04-route-tasks-transition.jpg`, `05-tasks-heading.jpg`, `06-tasks-board-enter.jpg`, `07-tasks-board-settled.jpg`, `sequence-tasks.jpg` | Sidebar/toolbar static; title immediate; columns settle logically; no blank wait | 200ms / 3s network, 10 rapid route clicks, back/forward, keyboard |
| Analytics selector | `09-analytics-count-start.jpg`, `10-analytics-count-progress.jpg`, `11-analytics-range-shift.jpg`, `12-analytics-count-settled.jpg`, `sequence-analytics.jpg` | All cards/lines/filter labels show same data period; current target is truthful; no stale request | 30D→90D→7D rapid changes; mixed units, empty range, export |
| Settings | `13-route-settings-transition.jpg`, `14-settings-population.jpg`, `15-settings-final.jpg`, `sequence-settings.jpg` | Header/controls reveal; focus/labels/persistence correct | refresh, storage disabled, reduced motion, form error |

**Review method:** use local browser screenshots/recordings if available at at least initial / 25% / 50% / 75% / settled. Track mismatches explicitly: *shell, component geometry, whitespace, colour/contrast, number timing, line timing, skeleton handling, sidebar continuity, interruption, keyboard focus*.

**Report:** `route | reference frames reviewed | features implemented | tests run | observed mismatches | untested`. If no real browser test: describe code-level QA only; do not claim visual or kinetic parity.
