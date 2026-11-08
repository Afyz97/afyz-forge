# Visual/motion QA against user-provided video

Reference crops are in `.ai/uiux/orbit/assets/video-reference/` after installation (source video is 720×1280 portrait with a horizontal screen recording window). Compare the **internal application crop**, not the title/editorial backdrop. Adapt proportions if target app differs; match style, hierarchy and interaction quality rather than imitating video letterboxing.

## Route × scenario evidence sheet

| Route | Screenshot target | Video reference | Interaction recording |
|---|---|---|---|
| Dashboard | full desktop and mobile, populated metrics | `02-dashboard-stable.jpg` | KPI load, activity chart, gauge, timer |
| Create / edit | centered modal and success/error | `03-add-project-modal.jpg` | open, focus, submit, rollback/error |
| Timer | controls and active state | `05-timer-controls.jpg` | start/pause/stop, accuracy |
| Board | four lanes and card hierarchy | `09-kanban-board.jpg` | pointer drag, keyboard move, persist/revert |
| Team | full and filtered cards | `12-team-entrance.jpg`, `14-team-filtered.jpg` | select filter, card reflow, profile drawer |
| Calendar | month and agenda side rail | `16-calendar.jpg` | next/prev month, day select |
| Analytics | trend and hovered point | `19-analytics-overview.jpg`, `21-analytics-tooltip.jpg` | focus/hover, range change |
| Settings | accent swatches and theme | `26-theme-selector.jpg`, `28-theme-updated.jpg` | accent update throughout all routes |

## Evaluation rubric — 100 points

- Visual structure (20): shell, content density, dashboard composition, consistent hierarchy.
- Palette/typography/surfaces (20): coherent host theme, neutral cards, readable text, appropriate radius/border, distinctive charts.
- Behavioural completeness (25): real board DnD, working filters, modal + feedback, accessible chart tooltip, timer, theme persistence.
- Motion continuity (20): proper entry/exit/reflow, nonjanky data updates, correct interaction timing, no conflicting animations.
- Responsive/accessibility/performance (15): small viewport, keyboard, focus, reduced motion, no layout shift, correct state/error handling.

Score using evidence, and identify unfixed defects. Never claim precise timing or pixel-perfect matching unless measured and directly compared. Keep user workflow/functionality as stronger requirements than animation fidelity.
