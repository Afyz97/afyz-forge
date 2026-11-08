---
name: orbit-ui-director
description: "Coordinate a complete reference-inspired UI/UX redesign across a dashboard, admin panel, Laravel or React application; automatically use for multi-page UI implementation or UI-wide refactoring, routing to design, shell, components, motion and visual QA. Use when the work follows a visual or motion reference (a sample site or video). Not for a design with no reference to match — use ui-studio's ui-visual-direction."
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

# Orbit UI director: consistency across the *whole system*

Read `.ai/uiux/orbit/` in the current project; if not installed there, use `~/.ai/uiux/orbit/` from the user-wide installation.

Use when the user requests a full redesign, adds a new screen into an existing system, asks to match the original enterprise sample, or asks to unify a multi-module application. This is a **coordination skill**; load only specialist skills relevant to actual components changed. 

## Mandatory reading
Read `.ai/uiux/orbit/REFERENCE-BRIEF.md`, `DESIGN-SPEC.md`, `MOTION-SPEC.md` and `IMPLEMENTATION-PLAN.md` where installed. Read any relevant existing `.ai/agents/` knowledge, `AGENTS.md`, and `CLAUDE.md` without altering team knowledge.

## Execution
1. Inventory real routes, roles, layout templates, shared components, existing styles, icons, data flows, charts, navigation and actual screenshot tooling.
2. Determine **fidelity status**: reference browser screenshot available (observed), or public description only (approximated). If browser access works, inspect all representative reference states before implementation; do not substitute guesses for screenshots.
3. Write a compact page matrix: shell, dashboard, table/list, form/detail, analytics/chart, settings/auth, modal/drawer, mobile. List shared primitives and motion in each.
4. Apply `orbit-ui-foundations` to establish coherent tokens. Then `orbit-ui-app-shell`, `orbit-ui-components`/`orbit-ui-dashboards` as appropriate. `orbit-ui-motion` applies to every visible interactive element, even if not explicitly requested.
5. Implement one representative vertical slice (shell + dashboard + table/form) to a high standard, then roll out using shared components. **Do not stop after styling the dashboard** if multiple routes are in scope.
6. Use `orbit-ui-responsive` during implementation, then `orbit-ui-visual-qa` to compare actual pages to captured reference at desktop/mobile sizes.
7. End with a route coverage summary: changed, preserved, tested and untested. Disclose uncertainty about visual similarity if no website reference screenshots were available.

## Hard requirements
- Close *visual grammar* to the sample is the goal, not a generic SaaS makeover. Prioritize shell proportions, visual density, typography, component language, then motion polish.
- Preserve authorization, routing, validation, persistence, exports, locale, user flows and performance; no fictitious backend updates.
- No copying of reference provider’s proprietary source/assets or fixed cinema-specific business features.
- Do not introduce a new CSS framework, router or animation dependency solely for style without a concrete benefit and user authorization.
- Auto-invocation is a model choice; project instructions increase reliability but do not guarantee it. Do not promise a pixel-perfect match from uninspected reference.

## Deliverables
Implemented shared styles/components and screens; a small change log, visual check result and specific remaining mismatches. For audits, provide an actionable, ordered rollout plan instead of pretending code changed.

## Added video reference (v3)

This package now includes observed motion and UI from the user's `299130.mp4`. Treat the video as a **second reference**, not footage of the enterprise reference itself. Before a dashboard/admin redesign read `.ai/uiux/orbit/VIDEO-REFERENCE-AUDIT.md`, `VIDEO-UX-PATTERNS.md`, `VIDEO-MOTION-PLAYBOOK.md`. On any matching UI task, delegate/select: `orbit-ui-video-motion` for comprehensive animated choreography, `orbit-ui-interactive-kanban` for drag boards, `orbit-ui-team-filter-motion` for member directory/filter movement, `orbit-ui-analytics-calendar` for analytics/calendar, `orbit-ui-personalization` for dynamic accent settings, and `orbit-ui-feedback-overlays` for modals/toasts/timers. Use the matching cropped image(s) in `.ai/uiux/orbit/assets/video-reference/` to visually verify specific elements, then report which transitions were actually implemented. Prefer **real interaction fidelity** (data/state/persistence) over static clones. Do not add project-management-only features to unrelated apps.


## Reference C (v4): video-specific motion routing

Read `.ai/uiux/orbit/MOTION-ROUTING.md` (or user-scope counterpart) before deciding how to apply the user's **92-second cinematic UI explainer video**. It is a separate reference from the enterprise reference and the dashboard video. For landing/onboarding/walkthrough scope, call/use `orbit-ui-motion-storytelling`, `orbit-ui-kinetic-type`, `orbit-ui-layered-cards`, optional `orbit-ui-mascot-motion`, plus `orbit-ui-motion-qa`. Review `EDITORIAL-VIDEO-OBSERVATIONS.md`, `EDITORIAL-MOTION-PLAYBOOK.md` and actual stills. If the user instead asks for privacy/consent/cancel UX, use `orbit-ui-trust-consent-ux` with domain evidence and legal-review disclaimer. **Never apply cinematic scene changes to forms/tables unless explicitly requested.**

## Reference D v6 — short project-management clip

When redesigning workspaces, read `PROJECT-WORKSPACE-VIDEO-AUDIT.md` and route task-specific work to `orbit-ui-workspace-navigation` (persistent shell and route entry), `orbit-ui-metric-choreography` (KPI/count-up/date-range redraw), or `orbit-ui-project-workspaces` (full project-management product). Inspect `assets/project-workspace-reference/` labelled motion strips. Treat its on-video code panel as an idea, not proof of executed theme-change animation.

## Reference E (v7): login/signup stage

For any authentication UI request, delegate to `orbit-ui-auth-forms`; for requested **diagonal panel sweep** explicitly add `orbit-ui-diagonal-wipe` and test with `AUTH-VISUAL-QA.md`. Don't force this auth-specific animation into dashboards. A video-derived pattern is a reference, not proof of working login and account creation.
