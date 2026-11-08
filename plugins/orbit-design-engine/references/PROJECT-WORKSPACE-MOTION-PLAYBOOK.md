# Reference D — actionable workspace motion playbook

These are **recommended implementation targets**, informed by visual sequences in the 6.175s clip but **not measured source-code values**. Prefer existing Orbit design tokens and the project's current stack.

## Motion choreography and state graph

### Dashboard arrive → metrics settle (first paint with real data)
1. Render stable shell, all heading/label geometry and fixed target chart slots. Never animate the whole browser or top video title.
2. Stagger 3–5 visible KPI cards by 25–55ms; subtle opacity/translate 6–12px, 180–320ms.
3. Count numeric measures to **actual server-provided targets** with ease-out 450–850ms. Only run once on initial meaningful reveal or meaningful data changes, not on every React render/Livewire patch. Preserve sign, currency, decimals, percentages, time units, locale and accessible announcements (announce settled value, not each intermediate frame).
4. Animate the activity bars by scaleY or height from the baseline, with 30–85ms slight stagger; 320–600ms. Hatched/neutral bars represent meaningful placeholders or comparisons, never arbitrary filler if the underlying data is absent.
5. Once primary metrics are legible, bring in reminder/secondary project snippets with 100–200ms fade/translate. Keep click targets active during animation.

### Sidebar navigation → page content
1. On route click immediately update focus/active navigation, preserve persistent sidebar/toolbar position, set `aria-current=page`.
2. If router changes synchronously: old content 100–180ms fade (max 4px translate), then new title within 80–160ms, subsequent sections 30–60ms stagger. Total perceived transition ideally 200–400ms.
3. If data is pending: show the new route title and bounded skeleton immediately, not a featureless blank screen. Avoid blocking input on animation. Async content enters when ready, not according to a hardcoded timer.
4. Cancel prior route animations and stale responses if user switches again. Restore scroll and focus according to router semantics. Avoid page-wide opacity that affects fixed toolbar/sidebar.

### Tasks board / Kanban populate
- Four status columns are illustrated, not mandatory: use statuses defined by the real project.
- Render headers immediately; reveal up to 4 visible columns in 30–65ms stagger after board data is ready. Reveal first 2–4 visible cards with small vertical translation 4–8px over 180–260ms. Long boards: virtualize or skip stagger.
- Animating a board's **entry** is separate from dragging: do **not** assume this 6-second clip demonstrates drag-and-drop. If drag exists, use `orbit-ui-interactive-kanban` from earlier references.
- Keyboard accessible state/status editing and truthfully persisted updates take priority over visual movement.

### Analytics KPI and sparkline transition
- Selector changes real date window, data loading and chart labels as one atomic view model. Show pending status if async.
- Interpolate counters **from previous numeric values if semantically comparable**, not reflexively from zero; if new period has different unit, replace/announce rather than morph deceptively. 450–900ms on deliberate selection; cancel previous animation if another range is selected.
- Line reveal uses SVG stroke-dashoffset or path interpolation when chart lib supports it; 350–700ms. Keep axes/value labels synchronized with series and tooltip. Prefer stable line over perpetual redraw.
- Maintain range selector active thumb and keyboard semantics; include 7D / 30D / 90D only if actual data supports them. Export respects selected range.
- For rapid 30D→90D changes, abort requests or discard stale responses using request id/abort controller, terminate old timeline and use latest target. Reduced motion: instant exact value and chart.

### Settings appearance / optional color switch
- Settings route itself uses the same shell/nav transition as other routes. Do not animate labels independently until form data is available.
- Visible source snippet illustrates persisted root-level accent and a 600ms GSAP spring-like swatch rotation/scale. **Not confirmed as a performed interaction in this clip.** If reproducing: an original, tasteful 220–420ms swatch pop on user-triggered changes; use `transform` and optional subdued spring easing; stop motion for reduced-motion users. Native CSS spring-like transition or GSAP only when justified.
- Store preference via existing user settings or safe local preference as applicable; restore before first paint, make all controls/tokens update and provide textual confirmation. Do not copy `fernly:accent` as a new storage key.

## Accessibility and correctness

- Labels and critical values are always legible without animation; screen readers get final values, not changing intermediates.
- `prefers-reduced-motion: reduce` → no counting tween, chart wipe or page exit/entry translation; instantly render final state with accessible loading and success feedback.
- No hidden save progress, synthetic totals, animated values not matching server, output dependent on pixel/frame rate, phantom task statuses or unimplemented export buttons.
- Avoid compositing the entire content region with heavy blur; keep fixed elements static; support touch, keyboard, low-memory devices and low-end laptops.
- Provide safe cancellation on unmount/route change/rapid filter, keep value formatting correct and show stable skeletons for network latency.

## Preferred stack adapters

- **Laravel Blade + Alpine:** CSS transitions for route panels, Alpine initialized after response; avoid double-running count-up after partial DOM refresh, respect Livewire morph hooks; Cancel `requestAnimationFrame` loop on teardown.
- **React / Inertia:** CSS for shell/view transitions, `requestAnimationFrame` for counters or existing motion library; `useEffect` cleanup with `cancelAnimationFrame` or GSAP context; chart library handles path transitions.
- **AdminLTE / Bootstrap:** retain sidebar/menu ownership, animate content inside without competing with plugin's collapse events.
- **GSAP:** optional; existing installation preferred. On any new dependency, explain bundle and browser support impact, never silently install heavy motion packages.

## Implementation steps for a coding agent

Audit current route/data → choose matched reference states → identify current DOM state machine → implement shared tokens and transition utility → implement count-up and chart draw with cleanup → add sidebar content transitions → verify range switching/cancellation → record screenshots/video of initial, intermediate, settled, repeated click, slow network, reduced motion. Use `orbit-ui-motion-qa` and `orbit-ui-visual-qa` plus `PROJECT-WORKSPACE-VISUAL-QA.md`.

## Standalone implementation sample

Open `.ai/uiux/orbit/examples/workspace-motion-demo.html` locally after installing. Original mock-data demonstration of animated KPI, bar entrances, app-shell routing, Tasks entry, Analytics range-driven counting, settings swatch preference and toast. It is self-contained and deliberately lacks backend persistence for tasks/exports; adapt using real project data and existing routes.
