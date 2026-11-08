# Motion choreography adapted from uploaded dashboard video

Read `VIDEO-REFERENCE-AUDIT.md` and `MOTION-SPEC.md`. These are **original implementation targets**, not measured source timings. Match the reference's restrained, continuous feel. Every effect must be functional, interruptible, accessible and tied to a real state update.

## Global motion vocabulary (suggested)

| Scenario | Duration target | Easing | Distance / amplitude | Behaviour |
|---|---:|---|---|---|
| Hover/button/focus feedback | 110–170 ms | ease-out | 0–2 px | no bouncing or constant pulsing |
| Tabs/segmented-pill movement | 160–240 ms | ease-out | animated selected background | active text stays crisp |
| KPI values on entry/data refresh | 450–850 ms | ease-out | 0 to actual value **only on true load** | tabular figures, one animation pass, cancel on re-fetch |
| Staggered metric/chart reveal | 270–420 ms | ease-out | Y 7–12 px, opacity 0→1 | 35–55 ms per logical group, cap first 6 |
| Vertical analytics bar growth | 380–650 ms | ease-out | baseline→actual height | stable baseline; do not morph categories |
| Doughnut/radial progress reveal | 500–850 ms | ease-out | stroke-dashoffset | update accessible value instantly |
| Modals & toasts | 160–260 ms | ease-out | dialog Y 8–14 px; toast Y 10 px | backdrop 120–180 ms; do not blur extensive page regions on slow devices |
| Side detail drawer | 210–320 ms | ease-out | horizontal 16–32 px (or full drawer edge) | focus trap; restore focus on close |
| Kanban dragging | immediate direct manipulation | n/a | attached to pointer | insertion hint, translucent placeholder, 180–260 ms settle |
| Team card filter/reflow | 220–350 ms | ease-in-out | FLIP translation between old/new boxes | stable keys, no ghost clicks; stagger new items <=45 ms |
| Calendar month/view switch | 200–330 ms | ease-out | content fade + 6–12 px shift | header/agenda stay aligned, selected date announced |
| Area chart hover crosshair/tooltip | 80–150 ms | ease-out | small tooltip offset | stable at data point, keyboard focus parity |
| Accent theme update | 150–260 ms | linear/ease-out | CSS variable colour transition | all controls/charts/selection markers update together; don't transition all properties |

## Required choreography

**Dashboard load:** frame/layout stable → skeletons while awaiting real data → short KPI number count → chart series growth and radial progress → subtle reveal of secondary cards. Never delay essential interaction until counting ends; for huge or changing numbers, do not animate from zero. When data refreshes, interpolate between old and new values only if comparable.

**Add project dialog:** trigger receives pressed response → background dims (no simulated app state) → centred modal moves into place → focus first input. Confirm: pending action state → backend acknowledgement → close → actual KPI/project list update → succinct toast. Failure: keep modal open with field/general error, no fake success.

**Timer:** clock uses tabular numbers and fixed width. Play/pause/stop animate only the control state; the clock uses monotonic time for elapsed computations, not cumulative setInterval seconds. Persist ongoing session if required; treat page tab visibility/reload carefully. Disable transitions that make time appear inaccurate.

**Kanban reorder:** drag lift (small elevation) → movable card tracks user pointer → drop lane highlights / placeholder occupies target space → on commit cards settle into their new places → column counter updates after actual state mutation. Send to backend with original version; on error restore and notify. Keyboard lift/move/drop/cancel alternative mandatory.

**Team filter:** old card coordinates measured, selected department chip changes, cards removed/inserted and existing cards translate into new positions (FLIP) while opacity changes; new layout should not flash. Scroll anchoring stays reasonable, card focus moves appropriately. Reduced-motion: immediate filter change.

**Calendar:** switch month and view with minimal slide/fade; day selection updates right agenda without page scroll jump. Live-region summary of new month/day for accessibility. Do not animate date-picker dropdown out of sync with selected month.

**Analytics:** visible hover focus ring, crosshair and tooltip for exact data point. Follow pointer only within the plotted region, throttle pointer work if needed. Chart semantics/ARIA and accessible data table are required where appropriate. Tooltip disappears on escape/leave; range switches cancel old animations.

**Theming:** accent selection sets one CSS variable palette at root; active nav, primary buttons, progress fills, chart strokes, contextual overlays and branded timer panel follow the same token. Accent choices persist according to app requirements; enforce readable contrast for all palettes and restore on reload.

## Technique selection

- **CSS** transitions / keyframes for hover, focus, overlays, accent token change, chip selection and simple card reveals.
- **Web Animations API** or stable JS animation library for FLIP/reorder, when needed.
- **Existing chart library** animation hooks for chart/meter updates (never replace analytics with fake images).
- **GSAP optional** for choreographed sequences if already present or properly justified; do not assume the video proves GSAP.
- **Livewire / Alpine:** target real DOM lifecycle and preserve focus; ensure morphing doesn't restart counters on every update.
- **React:** animate keyed components with lifecycle cleanup; prevent double animation on Strict Mode and route remounts.

## Strict motion rules

`prefers-reduced-motion: reduce` removes nonessential motion, while retaining immediate visibility of state changes; keyboard interaction and touch alternatives must work. Keep transforms/opacity on compositor where possible; never repeatedly force layout on scroll. Avoid large backdrop blurs, jank, perpetual glows and bounce. Do not animate unrelated cards just because a single card changed.

## Test scenarios

- First load, populated data, empty and failure states; modal validation and ESC; fast repeated filters; quick drag/cancel/retry; chart hover plus keyboard; timer 10-minute elapsed accuracy after tab backgrounding; theme switch in 4 palettes; browser refresh; 390px wide touch; reduce-motion mode; slow network/rejected backend request. Acknowledge missing browser QA honestly.
