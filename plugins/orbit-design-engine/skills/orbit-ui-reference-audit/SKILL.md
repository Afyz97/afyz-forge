---
name: orbit-ui-reference-audit
description: "Inspect the the enterprise reference UI reference and screenshot fidelity when implementing a close visual match, measuring layout, typography, colours and animations; use before redesigning dashboards or recreating a specific interface."
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

# original enterprise reference capture / evidence-based visual audit

1. Read `.ai/uiux/orbit/REFERENCE-BRIEF.md`. Distinguish **verified public features** from **unverified visual assumptions**.
2. If browser tooling exists, open `https://demo.codeandchill.store/kinlo/#/dashboard`, allow the client-side app to render, inspect theme and browser console, and capture visible UI at 1440×900 and 390×844. Do not claim a screenshot if only a text fetch was made.
3. Survey dashboard; a table/list; form/detail; modal; chart-time selection; expanded and collapsed sidebar; mobile drawer; light and dark where offered. Record screenshot name, viewport, exact observable features and uncertainty.
4. Measure overall composition first: rail width, top bar, page margins, card alignments, grid counts, typography size/weight, border radius, shadows and semantic colours. Then log motion (duration/easing only if captured/observable).
5. Write observed notes to `.ai/uiux/orbit/reference/MEASUREMENTS.md` using `observed / inferred / unknown` tags. Where authorized, screenshots to `reference/screenshots`. Never synthesize them as evidence.
6. Derive visual-gap list: reference screenshot vs actual screen. Fix top 3 structural differences before touching cosmetic details. Use `orbit-ui-visual-qa` to confirm.
7. If the demo cannot load, explain that this is an approximation based on the vendor's descriptions, and proceed with the packaged original design defaults. Don't overclaim precision.

Other site assets/code should not be copied; observing a public UI is not permission to redistribute commercial source. If the user supplies screenshots, prefer these over uncertain web assumptions.

## Uploaded video is a verified local visual source

The updated plugin embeds user-provided video crop samples in `.ai/uiux/orbit/assets/video-reference/` and a timestamp/evidence ledger in `VIDEO-REFERENCE-AUDIT.md`. The video shows a project management dashboard and is **not identified as the enterprise reference**. This provides concrete visual/motion evidence independent of whether the original the enterprise reference URL is browser-accessible. Prefer cropped frame evidence to unsupported claims about exact styles or source libraries.
