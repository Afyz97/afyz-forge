---
name: ui-canvas-art
description: >-
  Creates original static visual art as a .png or .pdf (poster, print, cover artwork, art
  piece, exhibition or event visual) by first writing a named design philosophy as a .md file
  and then composing a museum-quality canvas with the bundled OFL fonts. Use for "make a
  poster", "design a print", "create an art piece", "album or book cover artwork", "a visual
  for my wall", "an abstract composition", "multi-page art booklet". Not for web pages or app
  UI (ui-visual-direction), slide or document themes (ui-theming), charts or dashboards, or
  editing photos.
argument-hint: "<subject or occasion>"
---

# Canvas art

Deliverables: a philosophy `.md` plus the finished `.png` or `.pdf`. Everything is original;
never imitate a living artist's recognisable work.

## Step 1: write the philosophy

You are founding a small art movement, not filling a layout. The movement speaks through form,
space, colour and composition; images, shapes and patterns do the talking, and words appear
only as small visual accents (roughly nine parts image to one part text).

Rules for the document (detail and example movements: `references/philosophy.md`):
- A name of one or two words.
- Four to six full paragraphs covering: space and form; colour and material; scale and rhythm;
  composition and balance; visual hierarchy. Each topic once, no repetition.
- Keep returning to craft: the piece should read as the result of long, expert, careful work.
- Leave room to interpret: describe the movement in general terms, not the specific artwork.

## Step 2: hide the reference

Find the idea behind the request and weave it in quietly, the way a jazz player quotes another
tune mid-solo: people who know the subject sense it, everyone else simply sees a strong
abstract composition.

## Step 3: make the canvas

Rules: `references/canvas-rules.md`. The non-negotiable: **nothing overlaps and nothing runs
off the edge**; margins and breathing room everywhere.

Fonts: `${CLAUDE_PLUGIN_ROOT}/skills/ui-canvas-art/assets/fonts/` (29 OFL families, each with
its `*-OFL.txt`). Mix them; fetch other OFL fonts only if none fits, and keep their licence.

Rendering in Claude Code: Python (Pillow, reportlab, matplotlib, cairo) or HTML/SVG rendered
to PNG/PDF with Playwright. Check the output image yourself before handing it over.

## Step 4: refine (always)

Assume the user has already replied: "Not perfect enough. It has to be flawless, worthy of a
museum wall." Do **not** add elements. Sharpen what exists until every edge, gap and alignment
is exact. When the impulse is to draw something new, ask instead how the current marks could be
more fully art. Then do a second polish pass.

## More than one page

Each further page follows the same philosophy with its own clear variation, like spreads in
a well-made art book that together tell a story. Deliver as one PDF or several PNGs.

## Hand-over

The final `.pdf` / `.png` files and the philosophy `.md`, side by side.
