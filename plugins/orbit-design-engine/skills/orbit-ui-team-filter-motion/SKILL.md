---
name: orbit-ui-team-filter-motion
description: "Create a team/personnel directory with video-style department filter chips, pastel avatar cards, card reflow/FLIP motion, progress statistics, context-preserving profile side drawer, keyboard and reduced-motion accessibility."
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

# Animated team filter and member detail

Video evidence: `assets/video-reference/12-team-entrance.jpg`, `14-team-filtered.jpg`; read `VIDEO-MOTION-PLAYBOOK.md` and `VIDEO-UX-PATTERNS.md`.

Pattern: above a card grid place searchable/segmented filter chips (All, departments); each compact card features avatar/initial, name/role, category, factual stats, slim progress indicator, Message and Profile actions. On filter change, *existing cards glide into their new positions*; omitted cards exit cleanly and new cards enter gently. Implement via FLIP/animation layout, keyed objects and efficient measurement, or simpler fade/reflow if library absent. State should never jump to positions that do not match their semantics. Respect stable scroll position, restored focus and no-results state.

Profile button opens right-side details drawer with proper heading, focus trap, ESC/back button and page scroll restoration. Message action must perform a real function or be intentionally hidden; protect private data. Tests: repeated rapid filter switches, card reflow without ghost clicks, focus after filtering focused member, keyboard, narrow screen, reduced motion and large data set/pagination.
