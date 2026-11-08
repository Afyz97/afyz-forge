# Uploaded video: observed interaction evidence

**Reference:** the user-provided `299130.mp4`, approximately 29.6 s, portrait 720×1280, 30 fps. Its central horizontal product footage shows a **project-management dashboard UI**. This is a **second reference**; do not claim that the video shows the original enterprise demo, or confuse its project-management workflows with the enterprise reference's specific product features.

**Evidence:** 13 crops from the user-provided video are in `.ai/uiux/orbit/assets/video-reference/` after installation. The crops omit the external editorial frame and title. They are for private **visual reference**; do not publish or embed them as production UI assets. Timestamps are approximate sample points. For motion, inspect consecutive original frames where accessible; individual stills cannot prove exact easing or implementation technology.

| Seconds | Observable UI / transition | Still | Skill routing |
|---|---|---|---|
| 0–2 | Dashboard appears; metric totals and project chart progress into a populated state; emphasized selected KPI card; other cards use normal host surfaces | `02-dashboard-stable.jpg` | video-motion, dashboards |
| 2–4 | Add Project launches centered host-surface form dialog on muted/softened dashboard; submit closes and confirms change using short bottom notification | `03-add-project-modal.jpg` | feedback-overlays, components |
| 4–7 | Timer card zoomed: theme-emphasized curved-line background, large tabular clock, contrasting pause/play and semantic destructive stop controls; state advances in seconds | `05-timer-controls.jpg` | feedback-overlays |
| 8–11 | Tasks board: four lanes To do / In progress / In review / Done, small theme-surface task cards with labels, status colour, dates, avatars; drag moves a card between columns and counts reflect board state | `09-kanban-board.jpg`, `11-kanban-drop.jpg` | interactive-kanban |
| 11–15 | Team listing enters; department chip filter reduces/rearranges team cards into two visible cards, and member detail opens as right-side panel | `12-team-entrance.jpg`, `14-team-filtered.jpg` | team-filter-motion |
| 16–18 | Calendar month view, daily event pills, right-side selected-day/agenda panel; toolbar view/date controls; changing date/view updates calendar surface | `16-calendar.jpg` | analytics-calendar |
| 19–23 | Analytics summary tiles, thin theme-based area/line chart and percentage/doughnut visualization; close-up of hover state with vertical guide, emphasized dot and floating tooltip | `19-analytics-overview.jpg`, `21-analytics-tooltip.jpg` | analytics-calendar |
| 24–29 | Settings Appearance: the reference’s own theme choices and week-start segmented control; choosing a new option changes navigation, buttons, charts, KPI, timer and focus accents throughout its dashboard (do not copy these options or palettes into another application) | `26-theme-selector.jpg`, `28-theme-updated.jpg` | personalization |

## Visual grammar observed (not source-code values)

- App interior against a saturated *outer* editorial framing in the video; small icon-and-label left sidebar, slim utility/header row and compact dashboard content grid.
- Light neutral canvas, low-contrast card boundaries and rounded corners, little or no heavy shadows.
- Emphasized active areas, CTA buttons, secondary indicators, neutral striped placeholder bars, and avatar treatments. Copy layout and hierarchy only; derive every value from the host theme.
- Compact sans-serif UI typography, dense but legible figures, subtle muted metadata and headers, very small circular icon controls and rounded filter chips.
- App shell stays stable across Dashboard, Tasks, Team, Calendar, Analytics and Settings; content changes in-place.
- Motion is calm and purposeful: data appears, filters rearrange, drawers/dialogs establish hierarchy, cards follow drag location, themes update as a unified system.

## Evidence boundaries

- **Observed:** positions, elements, sequence, theme-setting update, board movement, tooltip, right panel, modal, timer and filter changes.
- **Recommended, not measured:** millisecond durations, easing curves, numeric colours/spacing, FLIP/GSAP/Framer Motion implementation, whether backend persists each change, and what is visible outside recorded frames.
- The video’s surrounding area may be editorial framing rather than the application itself. Never force the sample background or its palette into another app.
- Do not copy the video's brand, its data, its labels, or screenshots into shipping application screens; map patterns to each project's actual routes, modules and domain.
