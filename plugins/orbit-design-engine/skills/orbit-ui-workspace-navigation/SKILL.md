---
name: orbit-ui-workspace-navigation
description: "Implement a stable, cohesive application shell with route-specific content exits, loading/reveal choreography, sidebar active-state feedback, and interruption-safe navigation based on the user-supplied 6s project-management video."
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

# Workspace navigation and route transition skill

Use when modifying page navigation, sidebar, tabs, nested workspace menus, or route transitions. Read `.ai/uiux/orbit/PROJECT-WORKSPACE-VIDEO-AUDIT.md`, `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` and `PROJECT-WORKSPACE-VISUAL-QA.md`; for user-scope lookup use `~/.ai/uiux/orbit/`.

## Motion reference D
In the 6.175s video the persistent sidebar/top bar barely move while Dashboard content fades away (around 1.65–1.8s), the Tasks title appears (around 1.95s), then columns populate (2.1–2.65s); similar routes lead to Analytics and Settings. Reconstruct **shell continuity** and a purposeful **old-view → new-header → content-ready** reveal, NOT marketing-style full-scene animation. Examples: `assets/project-workspace-reference/sequence-tasks.jpg`, `sequence-settings.jpg`.

## Implementation contract
1. Preserve sidebar and toolbar DOM/scroll/focus where framework permits. Active marker and `aria-current` move immediately on navigation.
2. Render pending destination context without hiding behind an indefinite full-page fade; use named loading skeletons or accessible status.
3. Animate only route content on actual state transitions (not artificially on every minor state update); content enter typically 180–300ms. Cancel old timelines on quick route changes; keep browser history and URL true.
4. Route-specific secondary cards/board entries may stagger up to 3–6 visible items by 30–60ms; skip animation for long tables.
5. Preserve permission/role checks, server errors, scroll restoration, and keyboard focus. Page cannot become unusable while animation plays.
6. Reduced-motion mode instantly changes states but retains active nav, loading/finished semantics and focus.

## QA
Verify with two click speeds, rapid five-route switches, slow API, empty page, keyboard, mobile navigation and reduced-motion. Compare video frames, especially transition midpoint; never claim exact duration measurements from video alone.
