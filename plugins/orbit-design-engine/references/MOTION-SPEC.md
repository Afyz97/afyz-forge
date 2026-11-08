# Motion system: functional, polished, consistent

**These durations are recommended originals; the enterprise reference's precise GSAP timelines were not inspected.** Motion should clarify cause and effect, hierarchy and continuity; not compete with the task.

## Timing and easing defaults
- Micro-hover/focus: 120–180ms; `cubic-bezier(.2,.8,.2,1)`.
- Click/pressed/release: 100–160ms, subtle translateY/scale <= 1.01 (avoid layout shift).
- Dropdown, popover, tooltip: 140–220ms opacity + transform 4–8px.
- Modal/dialog/drawer: 200–320ms fade + transform; focus moves after entry, restores after exit.
- Sidebar collapse/expand: 240–340ms; animate width and content transform coherently; hide label overflow, avoid text popping.
- Page content reveal: 240–400ms; stagger 30–55ms between 3–6 cards; keep all usable without animation.
- Chart updates/filter switch: 250–550ms interpolate only when comparing comparable axes; retain legible labels and avoid misleading data morphs.
- Skeleton shimmer: <= 1200ms cycle only for content actually pending; stop once data arrives.
- Success/confirmation: 170–300ms discrete feedback; destructive action remains clear, never playful.

## What to animate
- Navigation: selected marker, icon/label transition, expanded group, responsive drawer.
- Dashboard: KPI values on data change (respect live data), subtle card stagger, chart series transition, filter pill selection.
- Forms: validation reveal, field focus, button loading/success state, optimistic action rollback.
- Tables: subtle row hover, row expansion, sort and filter transitions, status update; never animate hundreds of rows.
- Overlays: backdrop + panel transition with correct focus trap, escape, click-away and announcements.
- Drag-and-drop: placeholder, clear target highlighting, snap-back/commit and keyboard equivalent; persist to backend safely.

## Motion restraint
- No perpetual card floating, continuous bounces, pointless parallax, slow page transitions or excessive spring overshoot.
- Never animate height from auto without measuring; avoid sudden content jump.
- Prefer CSS transitions for states and enter/exit; use GSAP only for orchestrated sequences, chart morphing or complex gesture dynamics when justified by existing stack and bundle budget.
- Animate `transform` and `opacity` where possible. `width` only for limited layout work such as sidebar; respect overflow and measured layout.
- Cancel/revert animations on route change or component unmount; update timeline on reduced-motion changes; no leaked observers/listeners.

## Accessibility
- Respect `@media (prefers-reduced-motion: reduce)` by removing nonessential animation and using instant state changes.
- Do not delay save/approve/submit based on animation.
- Never rely on motion alone to communicate state; include text/icon/live feedback as appropriate.
- Avoid flashing, rapid colour changes and surprise large-area movement.

## Implementation-specific
- React: CSS for simple controls; GSAP context with cleanups when already installed; do not add dependency automatically.
- Laravel + Blade + Alpine: CSS transitions; Alpine `x-transition` and lifecycle; GSAP only with documented real benefit.
- AdminLTE/Bootstrap: avoid stacking animations and interfering with existing collapse/modal events.

## Acceptance demos
- Collapse/expand sidebar 10 times; no jitter or lost focus.
- Open/close modal with pointer and keyboard; focus trap and ESC correct.
- Switch chart range repeatedly; rendered labels correspond to data.
- Slow network save; loading control becomes feedback, no false success.
- Re-run all tests with reduced motion enabled.


## Editorial vs application motion (v4)

For the separate 92-second motion-graphics explainer, see `MOTION-ROUTING.md` and `EDITORIAL-MOTION-PLAYBOOK.md`. The latter's longer scenes and expressive effects are for product storytelling/onboarding only. Ordinary app interactions must retain short, controlled transitions and functional UX.


## Reference D: animated workspace counters and page continuity (v6)

The latest short recording adds observable KPI counters reaching final values as bars rise, clean fixed-shell route transitions, Task board reveal, Analytics counters updating again when date range changes, and Settings screen entry. See `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md`. Recommended targets: counter 450–850ms, bar 320–600ms, page content 200–400ms, visible card stagger 30–65ms, chart path 350–700ms; these are new design estimates, not recovered source timings. Cancel stale tweens and preserve stable shell.

## Reference E: bidirectional auth-state sweep

A two-pane host-theme split-card login switches to registration through a single diagonal blade travelling right-to-left; the welcome and form switch sides; signing in reverses the traverse left-to-right. For this pattern use `orbit-ui-diagonal-wipe`, the precise narrative and evidence caveats in `AUTH-VIDEO-AUDIT.md`, and independent transition recipes in `AUTH-TRANSITION-PLAYBOOK.md`. Default suggested total ~720ms (not measured from source). Keep card bounds stable; never add this theatrical motion to routine navigation by default.
