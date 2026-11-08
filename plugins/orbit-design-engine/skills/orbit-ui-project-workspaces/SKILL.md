---
name: orbit-ui-project-workspaces
description: "Build project-management workspace UIs with compact dashboard KPIs, task boards, analytics and settings using cohesive shell geometry and state-based interaction motion from the user-provided 6s video; do not add unrelated features."
---

## Resource lookup (marketplace and standalone installs)

Resolve bundled resources relative to this `SKILL.md`, not the working directory.
If `../../.claude-plugin/plugin.json` or `../../.codex-plugin/plugin.json` exists,
this skill is inside the plugin: use `../../references/` for guide files and
`../../assets/`, `../../examples/`, `../../scripts/` for those resource folders.
In the instructions and bundled guides below, `.ai/uiux/orbit/` and
`~/.ai/uiux/orbit/` are legacy resource aliases: map guide paths to
`../../references/` and `assets/`, `examples/`, `scripts/` paths to the plugin root.
Bare guide filenames also resolve under `../../references/`.
For standalone installs without a plugin manifest, use the project's
`.ai/uiux/orbit/`, then `~/.ai/uiux/orbit/`, as described below.
Write new measurements, screenshots and other task output into the current
project's `.ai/uiux/orbit/reference/`; never write into the installed plugin.

## Mandatory: inherit the host application's theme

- **Never prescribe, introduce, replace, or hardcode any hue, palette, HEX/RGB/HSL value, theme preset, or brand/accent colour.** This rule overrides reference screenshots, reference videos, example CSS, and suggestions elsewhere in this package.
- Before editing UI, discover the application's **existing** theme provider, CSS variables, framework tokens, organization/tenant branding and light/dark modes. Use those settings as the single source of truth for backgrounds, surfaces, text, borders, interactive elements, chart series, focus rings, statuses and motion overlays.
- Preserve the current system's colours exactly unless the user **explicitly** requests a colour change. Do not introduce fallback branded palettes. If the theme exposes no suitable semantic token, reuse an existing styled component or ask for token mapping; do not invent a value.
- For motion and visual reference matching, transfer **structure, hierarchy, spacing, typography, geometry, transitions, timing and interaction behaviour**; map every visual treatment onto current project theme roles instead of copying the reference palette.
- Prefer host semantic components or computed theme tokens. Never overwrite the application's theme variables with example defaults. Ensure theme switching, tenant branding, and accessibility remain intact.

# Cohesive project-management workspaces

Use for actual project-management or internal operations modules (tasks, projects, analytics, team/workflow). Reference D is a design reference, **not a mandatory feature list**. Read `.ai/uiux/orbit/PROJECT-WORKSPACE-VIDEO-AUDIT.md`, `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md`, `PROJECT-WORKSPACE-VISUAL-QA.md` and `DESIGN-SPEC.md`. User-global installation fallback `~/.ai/uiux/orbit/`.

## Reference breakdown
- Shell: compact left sidebar with active theme marker, top search/profile/notification bar, muted light workspace background, rounded content areas and consistent header actions.
- Dashboard: one emphasized theme-based KPI panel plus quieter summary cards; animated activity bars, reminder/action rail and compact project list.
- Tasks: narrow four-column card board with status headings, badges, assignee indicators; **only entry animations shown in this new video**, earlier reference skill covers actual drag-and-drop.
- Analytics: 2×2 KPI cards with large figures and subtle fine theme-based sparklines; 7D/30D/90D segmented control, export.
- Settings: left secondary section list and right form; apply accessible labels and sensible defaults, persisting actual changes.

## Execution
Inventory the real project domain and roles. Map existing routes to these screen patterns only when meaningful; reuse shared shell, data cards, range control, loading state, settings form. For motion delegate to `orbit-ui-workspace-navigation` and `orbit-ui-metric-choreography`, existing `orbit-ui-analytics-calendar`, `orbit-ui-personalization` and `orbit-ui-interactive-kanban` as applicable. Use existing CSS framework, preserve validation and backend behaviour.

## Avoid
Do not recreate recorded product branding or import copyrighted screenshots as page assets; don't make every system project-management themed. Don't pretend controls, exports, filters, notifications or task transitions are functional without implementing them.

## Acceptance
Dashboard load, task board load, analytics initial + range-change, settings load + save, error/empty/loading, mobile fallback, keyboard and reduced-motion. Compare against the provided reference frame strips and report actual QA.
