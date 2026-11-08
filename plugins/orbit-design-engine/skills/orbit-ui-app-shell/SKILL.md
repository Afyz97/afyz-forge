---
name: orbit-ui-app-shell
description: "Implement a reference-inspired dashboard navigation shell including collapsible sidebar, active menu indicator, responsive drawer, header, search, notifications, logo and user controls with smooth transitions."
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

Read `THEME-INHERITANCE.md` before making any colour-bearing CSS or styling changes.

When a referenced `.ai/uiux/orbit/` file is absent from the repository, check the user-wide installation at `~/.ai/uiux/orbit/`.

# the enterprise reference app shell and navigation

Read `.ai/uiux/orbit/DESIGN-SPEC.md` and `MOTION-SPEC.md`.

## App shell must feel integrated
- Desktop: distinct left rail, grouped menu hierarchy, visual active indicator, clear title/icon rhythm, user area near bottom; slim icon rail when collapsed.
- Header: page context/title, global or scoped search, relevant actions, notifications/profile and theme switch only if supported.
- Mobile: accessible drawer; backdrop; focus trap; ESC closes; touch targets; close after route change; no side-scrolling page.
- Selected navigation item matches current route and roles/permissions; no dead links. Use named routes and existing auth.

## Required motion
- Rail expand/collapse 240–340ms; coordinate width and inner label opacity/translate. Prevent label flicker/overflow.
- Submenu expansion ~180–240ms with preserved focus; avoid transition jumping through auto height without measurement.
- Active indicator follows selection; page content transition subtle and never hides important state.
- Mobile drawer opens with translate/opacity ~220–300ms; restore focus to opener on close. Respect reduced motion.

## Test
Open deep links, refresh in slim mode, change roles/organization, navigate rapidly, use keyboard alone, collapse on 1024px, open mobile drawer on 390px and ensure body scroll lock cleanup.

Use `.ai/uiux/orbit/STACK-ADAPTERS.md` to integrate with existing Laravel/React rather than replacing working shells.

## Video shell consistency across routes

The video keeps a small sidebar/utility header consistent through Dashboard → Tasks → Team → Calendar → Analytics → Settings, and paints the selected route with a primary-colour accent. Match stable shell measurements and preserve the host theme across routes. Use `VIDEO-UX-PATTERNS.md` and the dashboard/board/team/settings crops. Do not imitate the source video's outer editorial backdrop as an application surface.
