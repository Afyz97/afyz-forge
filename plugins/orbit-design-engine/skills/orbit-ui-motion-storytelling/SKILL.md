---
name: orbit-ui-motion-storytelling
description: "Orchestrate cinematic, motion-driven UI storytelling for onboarding, landing pages, feature explainers and vertical short-form product demonstrations. Reads the user-supplied 92-second animated checklist video, choreographs scenes, persistence, progress, feedback and accessible pause/replay."
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

# Motion storytelling director — Reference C

**Use for:** story-like visual demonstrations, onboarding or product marketing. **Do not automatically transform ordinary admin screens into promotional footage.**

Read `references/MOTION-ROUTING.md`, `EDITORIAL-VIDEO-OBSERVATIONS.md` and `EDITORIAL-MOTION-PLAYBOOK.md` from `.ai/uiux/orbit/` (or `~/.ai/uiux/orbit/`). Inspect corresponding `assets/editorial-video-reference/` stills.

## Storyboard and implementation process

1. Identify the audience's task and three to six concepts worth showing; write one insight per scene. Record which aspects must function versus which are illustrative.
2. Build a stable scaffold: headline above, one consistent progress/count indicator, central illustrative mock UI, optional restrained character, soft contextual glow; avoid moving the scaffold between scenes.
3. Set per-scene semantic state: `intro → phrase → UI-card → annotation/action → confirmation → next`. For a demo, provide pause, replay, skip and manual advance. In a real wizard progress is user-initiated only.
4. Choreograph by meaning, not generic zoom: text introduces the question; foreground card demonstrates; pointer/callout highlights the answer; progress updates only upon actual completion.
5. Use host-defined semantic roles for display emphasis, confirmation, warnings, cards and overlays. Adopt the product’s existing theme without introducing a palette.
6. Implement one full 3-scene slice and record it before multiplying to other pages. Compare entrance, hold, exit and shared-element continuity against the supplied video.
7. For accessibility: reduced-motion static states, live-region announcements only for actual step changes, keyboard operations, no focus in decorative overlays, no auto-play of consent actions.

## Delegation

`orbit-ui-kinetic-type` for headline word swapping and highlights; `orbit-ui-layered-cards` for 2.5D illustration + annotation; `orbit-ui-mascot-motion` only for brand-suitable explainers; `orbit-ui-motion-qa` for frame-sequence inspection and performance. If the subject is trust/compliance, consult `orbit-ui-trust-consent-ux` only with domain context.

## Definition of done

Document every scene's trigger, starting/ending state, actual feedback, ease/duration recommendation, pause/reduced-motion branch, and screenshot/video evidence. Never claim frame-exact source reproduction without original assets/project.
