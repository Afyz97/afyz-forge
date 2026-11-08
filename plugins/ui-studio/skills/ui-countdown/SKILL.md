---
name: ui-countdown
description: >-
  Designs and builds countdowns and other time-based UI that stay correct: inline and
  large-digit countdowns, multi-ring radial countdowns, milestone / event-phase timelines and
  sticky deadline strips, all derived each tick from an authoritative deadline instant (server
  clock offset, timezone, DST, tab sleep and resume, honest expired state), with progress arcs
  that only show measured quantities and a layered radial countdown reference. Use for "add a
  countdown to the deadline", "submissions close in...", "radial / ring countdown", "event
  phase timeline", "registration closes banner", "the timer is wrong after the tab sleeps",
  "what should happen at zero?". Not for elapsed-time trackers or motion copied from a
  reference video - use orbit-design-engine; not for a reduced-motion or screen-reader audit -
  use user-first-ux.
argument-hint: "<what counts down, and where>"
---

# Countdowns & time-based UI

Motion here communicates the passage of time, not decoration. Style it with the host project's
tokens (ui-design-system owns them); never copy colours or branding from a reference.

## Choose a pattern to match the problem

- **Inline countdown:** compact and legible next to a due date or status.
- **Large digit countdown:** days/hours/minutes/seconds paired with a clear event title, absolute deadline and state.
- **Multi-ring radial countdown:** prominent hero or feature area; concentric animated progress arcs, central primary time unit, optional orbital markers and adjacent smaller numeric time units.
- **Milestone journey:** a horizontal/vertical event-phase timeline with completed, current, and future nodes.
- **Sticky phase strip:** concise summary of the current event period and next transition; avoid obscuring content, particularly on mobile.

Combine patterns only when each serves a separate purpose. A radial countdown can accompany a milestone timeline, but avoid repeating identical information without adding value. On an event or application-window page, the hero, the timeline, the countdown and the primary action must all agree with one deadline; never manufacture a deadline, progress fraction or registration state.

## Reference pattern: layered countdown hero

A recorded event page shows a useful abstract pattern: an event hero above a timeline and a contained countdown panel with a central day count; several concentric curved tracks animate independently; adjacent numeric hours, minutes and seconds remain readable and change over time; subtle background accents add atmosphere. Treat this as **motion and composition guidance only**, not a colour or brand template.

Read [references/layered-countdown.md](references/layered-countdown.md) for the detailed choreography, implementation strategy, and edge-case checklist.

## Motion principles

1. Motion explains a state change, progress, navigation, interaction, or passage of time.
2. Establish a clear hierarchy: meaningful progress first, ambient decoration second.
3. Durations and easing follow M1 in `${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`; keep related elements choreographed without excessive staggering.
4. Avoid incessant pulsing, shimmering, particle noise, or flashing that competes with reading.
5. Prefer transform and opacity for affordable effects; update SVG stroke geometry or a small number of custom properties only when needed.
6. Respect device resources and battery budget; reduced motion and flashing follow M2 in the same file.
7. Distinguish an ongoing countdown from loading progress: a ring must not imply a real percentage when the start time is unknown.

Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

## Countdown engineering (non-negotiable)

1. Establish the authoritative event deadline, start timestamp when relevant, timezone, and timezone-independent instant for calculations. Do not parse ambiguous locale dates or assume browser timezone.
2. Derive `remainingMs = max(0, deadlineEpochMs - authoritativeNowEpochMs)` on every tick, rather than decrementing a mutable counter. If the server supplies time, calculate a clock offset at synchronization and account for browser sleep/focus/resume.
3. Use the elapsed fraction only when the start and end are known. For one full-progress arc use `elapsedFraction = clamp((now - start)/(end-start), 0, 1)`. For per-unit ring fractions use well-defined semantics (seconds within minute, minutes within hour, hours within day); label their meaning.
4. Split remaining seconds consistently into days, hours, minutes and seconds; handle DST, zero, rollover, long horizons, leap days and locale formatting. Clarify calendar days vs exact 24-hour periods when that distinction matters.
5. **Decouple data correctness from rendering smoothness.** Update textual time at second precision only when shown; smoothly interpolate cosmetic arc movement without inventing time.
6. Keep numerals stable (`tabular-nums` or equivalent); prevent reflow as `09` becomes `08`. Provide explicit units and an absolute deadline.
7. Clamp at zero and transition to an accurate expired/closed/started state. If authoritative business status must be rechecked, display an honest pending-verification state rather than claiming a workflow closed solely on the client clock.
8. Avoid an announcement every second in screen readers. Provide an accessible static description with deadline and event name; announce only meaningful milestones/state changes.
9. Pause unnecessary animation when offscreen or hidden; recompute from authoritative time when returning, rather than playing catch-up frames.

## Choreography for radial countdowns

- **Visual anchor:** central remaining-days number and unit; supporting fields for hours/minutes/seconds beside or beneath it.
- **Rings:** concentric arcs that show distinct, named quantities where possible; optional static outer tracks provide context. Do not use multiple rings with arbitrary values.
- **Arc motion:** on time changes, use subtle interpolation to the correct progress value. Never let a looping decorative sweep impersonate remaining time.
- **Orbit accents:** optional small endpoint markers or glints attached to actual arc endpoints; no random sparkles obscuring legibility.
- **Transition:** after deadline, rings settle into a final status graphic and the primary call-to-action updates according to actual product rules.
- **Layout:** at mobile widths, use a stacked or compact radial component; keep text labels readable and avoid rendering a zoomed-out desktop section.

## Milestone/phase timeline

Show previous, current and upcoming phases as distinctly different states. Mark the present only using established start/end dates, not positional guesses. Provide a text equivalent and handle missing, future, and revised milestones. A timeline may appear adjacent to the radial countdown but must agree with the deadline.

## Verification

Test: start and end boundaries; zero; time expired; second/minute/hour/day rollovers; tab suspension and resume; differing client clocks; server time sync; slow devices; responsive layouts; keyboard and screen reader; reduced motion; all CTA actions; timeline/countdown agreement; and whether every ring truly maps to a measured quantity.

Build it in the project's stack with ui-stack-laravel or ui-stack-next.
