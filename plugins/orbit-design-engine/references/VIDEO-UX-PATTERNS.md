# Video-derived UI patterns and component acceptance criteria

These patterns are **not required everywhere**: apply only where the project's actual workflow calls for them. Preserve domain logic and don't add a tasks/calendar/team module merely to mimic the reference video.

## Shell, surface, spacing and visual hierarchy

Small logo row and search/utility header, narrow permanent sidebar on desktop, selected item marked with coloured stripe/pill, one consistent vertical rhythm. Existing-theme background for dense content and large rounded cards with subtle borders. Top-level pages maintain identical layout container, breadcrumb/title/description/action alignment, and icon style. Keep emphasized actions sparing and focus on content hierarchy.

## Dashboard cards

A top row of four status cards with one dominant filled KPI, others subtle. The reference mixes activity bar chart (some muted hatched placeholder bars), short reminder+CTA, list of projects, team collaboration entries with status pills, radial progress gauge and a emphasized timer tile. Recreate the *composition* as applicable; use real metrics. Animated total increments are optional on verified data changes, not on every render. Responsive order: KPIs → primary chart → urgent reminders/actions → progress → secondary lists.

## Kanban tasks

Visible columns and item counts, light compact cards, colour-coded status/type/priority tags, concise metadata, small avatars and task action menu. Drag card across columns and between positions. Filter chips above board. Preserve correct change history, permissions, concurrency, and keyboard controls; don't convert tasks into fake drag demos.

## Team directory

Filter chip row labelled by department, cards with pastel initial/avatar, name, role, department, a couple of stats, thin progress indicator, `Message` and `Profile` buttons. Filter animates existing cards into new grid slots; a side-panel profile view retains context and focus handling. Do not expose sensitive member information the user lacks permission to view.

## Calendar

Month grid with compact multi-colour event pills and a right-side day/agenda list. Date range and view controls stay pinned in header. Empty/overflow day handling, timezone-aware events, keyboard day navigation, responsive day agenda view for mobile. Motion should link old and new month, not distract.

## Analytics

Summary values above a wide theme-based area/line trend plot with thin line, dashed comparison series, small labels and a radial distribution chart to the right. Interactivity: hover/focus a data point → precise tooltip with date/metrics and vertical guide line; selection/range changes produce a meaningful update and preserve chart axis. Show units and comparison periods honestly.

## Settings and theming

Appearance settings in the video demonstrate how an existing theme selection propagates across controls, alongside a week-start Sunday/Monday segmented control. Only reuse the host application's available themes. Selected swatch gets visible outline; accent propagates to app shell, navigation, buttons, input focus, charts, badges, progress, timer and notification surfaces. Accent storage per user or browser per project requirements; don't assume localStorage satisfies multi-device user preferences.

## Dialogs, feedback and time tracking

Centered small-form dialog with background dimming, clearly defined actions, autofocus and immediate validation. Bottom toast only after genuine success. Right drawer for deep-detail content without navigation loss. Time tracker panel uses large tabular digits, clear play/pause and stop states, large touch targets, contrast-safe action colours, and precise elapsed-time calculation. Guard against accidental destructive stop.

## Design audit

For each route, report: reference pattern selected, actual app data source, UI components reused, interaction states, motion choreography, responsive treatment, keyboard/reduce-motion test, and remaining visual mismatch. Use timestamped video crops from `assets/video-reference/` for any assertion of close visual similarity; don't claim precise pixel matching from a 720px recording.
