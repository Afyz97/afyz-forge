---
name: ui-theming
description: >-
  Applies a ready-made or custom colour-and-font theme to slides, documents, reports or HTML
  pages: 10 presets (Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden
  Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy), a custom
  theme built from the user's inputs, and Anthropic brand colours for Anthropic-branded work
  only. Use for "theme this deck, report or doc", "apply a palette to these slides", "give this
  presentation a colour scheme", "show me the themes", "make a custom theme", "use Anthropic
  brand colours". Not for designing an app's or website's own visual identity from scratch
  (ui-visual-direction) or for posters and art pieces (ui-canvas-art).
argument-hint: "<preset name | custom>"
---

# Theming (presets, custom, Anthropic brand)

For decks, documents, reports and simple pages that need a consistent palette and font pairing.

## Workflow

1. Show the options: the preview `assets/theme-showcase.pdf` (read it, or give the user its
   path to open; never edit it) and the table in `references/presets.md`.
2. Ask which theme to use.
3. Wait for an explicit choice before applying anything.
4. Apply the theme's colours and fonts consistently across every slide or page, keep text
   contrast at the quality floor (check each pairing, some preset pairs fail as
   text colours and must be used only for fills), and keep the theme's identity throughout.

## Fonts: documents vs web

The preset fonts (DejaVu, FreeSans/FreeSerif) are chosen because they are safe on systems that
render pptx and docx. For web work keep the palette but choose type deliberately in
`ui-visual-direction`; the OFL families bundled with `ui-canvas-art` are available.

## Custom theme

When no preset fits, build one from the user's inputs: four named hex colours with roles, a
heading font and a body font, and an evocative name in the style of the presets. Let the user
look it over and approve it before applying it with the workflow above.

## Anthropic brand

Only for work that is branded as Anthropic: `references/anthropic-brand.md`. Never apply that
palette to a user's own product; on a client brief it reads as an AI default (AD1).

## Applying in files

- pptx with python-pptx: `RGBColor.from_string("2D8B8B")` for fills and text.
- docx: set theme colours on styles, not on individual runs.
- HTML/CSS: put the four colours in tokens (`--theme-*`) and reference them; do not scatter hex.
