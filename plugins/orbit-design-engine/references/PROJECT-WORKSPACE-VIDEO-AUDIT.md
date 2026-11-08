# Reference D — project-management workspace and motion audit (6.175-second clip)

Source: user-uploaded 720×1280, 30fps video; the **middle section** is an embedded project-management application demo. Top promotional title `Project management dashboard` and bottom `settings.js` code sample are editorial video framing, **not** application UI. The app inside the video is labelled *Fernly*. This name is a reference only: do not use as Orbit branding.

## Video-grounded findings — important ordering

| Sample time | Observed states | Motion to preserve |
|---|---|---|
| 0.00–0.60s | Dashboard metrics grow toward final numbers (24 / 10 / 12 / 2 in this sample); activity bars grow into place with coordinated timing; reminder and project snippets become readable | Count-up **on initial arrival**, coordinated chart-bar entrances and secondary content reveal; do not clone the recorded numbers |
| 0.72–1.50s | Dashboard stable; pointer moves over bars/sidebar and selected routes | Hover/focus affordance, no large perpetual movement |
| 1.65–1.95s | Tasks selected in persistent sidebar; previous dashboard content softens/disappears; new Tasks heading appears, initially almost empty | Stable application shell + short **old-view exit / loading / new-view enter** sequence |
| 2.10–2.65s | Four Kanban columns (To do / In progress / In review / Done) and task cards populate progressively | Brief, sequenced column/card reveal; avoid animating huge lists or inventing drag mechanics not seen here |
| 3.10–3.50s | Analytics selected; content begins blank/low-content then four cards render with low/intermediate counts and thin theme-styled sparklines | Progressively reveal summary cards and lines; use real data; show skeleton rather than misleading literal zero while fetching |
| 3.70–4.70s | Date range selected changes (30D then 90D); figures visibly rise again to new target values (recording shows ~646, ~3,532, ~89%, ~3.0d in later state); the trends adjust | **Data change triggers number interpolation and chart redraw**; terminate prior count/lines on rapid switching; do not tween across incomparable units/domains |
| 5.18–5.98s | Settings selected; outgoing Analytics clears; Settings and profile controls appear with staged reveal; Appearance item is targeted near end | Preserve shell; skeleton/fade transition; settings forms gain visibility after content/state is ready |

## Design style seen (but not exact CSS measurements)

- Layered canvas, rounded surfaces, muted body labels and prominent headings.
- Strong selected navigation marker, emphasized primary action, leading KPI panel, progress bars and chart lines; subtle hatched placeholder bar backgrounds.
- Narrow persistent navigation rail at left; slim top toolbar with compact search, notifications and user profile.
- Quiet card boundaries, low contrast borders, compact typography and dense-but-readable spacing; board/list cards with small status pills and avatars.
- Analytic cards arranged two across in demo, with large number, tiny comparative label and thin theme-aligned area sparklines; segment control 7D / 30D / 90D and Export CSV.

## Code visible beneath the product UI — distinguish from tested interactions

A **static code panel** shows `settings.js` appearance code: root-level dataset accent, a project-specific theme-setting read, change handler on `[data-accents]`, `store.set`, `gsap.fromTo` on the adjacent swatch with `scale .6→1`, `rotation -20→0`, `duration .6`, `ease 'back.out(2.5)'`, and a feedback toast. This panel is **visible implementation guidance, not proof that the settings theme change animation is demonstrated inside these six seconds**. In the actual app footage the user opens Settings but does not visibly change theme choice in this particular clip. For design purposes, translate the idea into framework-agnostic, safe implementation; do not copy vendor-specific storage keys or infer missing code infrastructure.

## Evidence hierarchy and limitations

1. Directly visible: changing counters, growing bars, routed content transitions, task-card population, metric re-animation after range change, settings reveal.
2. Suggested by code display only: persisted accent selection, pop feedback/toast, GSAP `back.out` swatch animation.
3. Not verified from this clip: actual production data, data API, drag-and-drop persistence, functional exporting, keyboard behaviour, exact CSS/JS source, frame rate/performance, full mobile layout, and precise motion easing curves.

### Local comparison images

`assets/project-workspace-reference/` contains 16 center-panel stills, four labelled multi-frame sequences, and `frames.json` for exact sample times. Compare at least the intermediate state, not just first/last screenshot. Treat the reference frames as internal study images, not product assets.
