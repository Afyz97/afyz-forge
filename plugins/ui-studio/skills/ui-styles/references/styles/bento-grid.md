# Bento Grid

## Definition
A bento grid arranges **several items of different importance into a modular grid of
variable-sized cells** — like a bento box, where compartments differ in size to fit their
contents. The defining idea is **content priority expressed through span**: the most
important cell is larger; related cells cluster; the whole reads as one composed overview.

**Distinguish from a plain grid:** a uniform grid of equal cards is *not* a bento — bento's
value is the *variation* in size/emphasis and the composed rhythm. It is an
information-composition system, not the CSS declaration `display: grid`.

## Conceptual model
Popularized by Apple's product marketing and adopted widely for feature overviews and
dashboards. It exists to **summarize a set of unequal things at a glance** — to let priority,
grouping, and rhythm do the explaining before a user reads a word. It works when you have
several items of genuinely different weight to present together; it fails when items are all
equal (use a normal grid), when there's really only one thing (don't force a grid), or when
every page becomes a bento by reflex.

## Visual grammar
- **Modular hierarchy:** cells span multiple columns/rows by importance; one or two hero
  cells anchor the composition.
- **Variable spans:** deliberate mix of large/medium/small cells; not a checkerboard.
- **Content priority → size:** span encodes importance; don't size by accident.
- **Scan path & rhythm:** arrange so the eye moves in an intended order; vary cell content
  type (stat, image, text, chart) to create rhythm.
- **Card relationships:** grouped/adjacent cells imply relation; gaps separate groups.
- **Feature emphasis:** the hero cell gets richer content/imagery; supporting cells are
  lighter.
- **Consistency within variation:** shared radius, spacing, and token system so variety
  doesn't become chaos.
- **Responsive regrouping:** the composition *re-flows into a new arrangement*, not a single
  column of identical blocks.

## Design tokens
- **Style-defining:** grid gap, cell radius, span system, cell surface treatment, hero-cell
  emphasis.
- **Product-dependent:** the actual content, palette, type, the underlying visual style
  (bento pairs with minimalism, glass, etc.).

```css
.bento {
  display: grid; gap: 16px;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(120px, auto);
}
.bento > .hero { grid-column: span 2; grid-row: span 2; }  /* priority via span */
.bento > .wide { grid-column: span 2; }
@media (max-width: 720px){ .bento { grid-template-columns: repeat(2,1fr); } .bento>.hero{grid-column:span 2;} }
```

## Component translation
Cells hold varied content: a hero feature (image + headline), a key metric, a small chart, a
short testimonial, a call to action, a media tile. Bento is a *layout system that hosts other
components* — the cells' internal style comes from your chosen visual style and
the token architecture in `ui-design-system`. Don't make every cell identical; don't nest cards inside cells.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** a marketing feature-overview bento with
rich imagery and one hero cell. **Product mode:** a dashboard *home/overview* where widgets
have genuinely different importance — but keep it a scannable summary, and don't bento-ify a
detailed working screen (a data table wants to be a table, not a grid of tiles).

## When to use
Feature/product overviews, landing "everything at a glance" sections, dashboard home
screens, portfolio summaries, comparison of several unequal highlights, app "explore" pages.

## When NOT to use
When items are all equal (use a normal grid/list), when there's only one main thing, for
long-form reading, for detailed data work (tables/forms), or as a default page skeleton.
Don't turn every page into a bento dashboard.

## Anti-patterns
- **Uniform bento (fake bento)** — Tell: all cells the same size. Why: no hierarchy; it's
  just a grid. Fix: vary spans by real priority, or use a plain grid honestly.
- **Random spans** — Tell: sizes not tied to importance. Why: composition reads arbitrary.
  Fix: map span to content priority.
- **Bento everything** — Tell: every section a tile grid. Why: monotony/slop. Fix: use bento
  only where an unequal overview helps.
- **Cards in cells in cards** — Tell: nested containers inside cells. Why: redundant chrome.
  Fix: one boundary per cell; group by gap.
- **Broken reading/focus order** — Tell: DOM order ≠ visual order; keyboard jumps around.
  Why: accessibility failure in a 2-D grid. Fix: order DOM to match intended reading; test
  keyboard traversal.
- **Empty filler cells** — Tell: cells added to "complete the grid" with nothing meaningful.
  Why: content-free. Fix: let the grid be asymmetric; don't invent filler.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Hotspots: **reading and focus order** across a
2-D grid (DOM order should match intended scan order; verify keyboard traversal), don't rely
on position alone for meaning, ensure each cell's internal content meets contrast, and make
interactive cells proper links/buttons with visible focus and targets at the A7 house floor.

## Responsive
The composition must **regroup**, not collapse into identical stacked blocks: reduce columns,
re-assign spans, keep the hero prominent, and preserve the intended priority order on mobile.
Test intermediate widths where spans re-flow awkwardly.

## Performance
Usually cheap (CSS grid). Cost comes from cell *content* — optimize/lazy-load imagery and
charts, especially the hero cell; avoid heavy effects per cell at scale.

## Implementation guidance
CSS Grid with `grid-column/row: span N` (or `grid-template-areas` for a fixed composition).
Map spans to priority explicitly. In React/Vue/Svelte, a `Bento`/`BentoCell` pair with a
`span`/`size` prop keeps it systematic. Tailwind: `grid grid-cols-4 gap-4` + `col-span-2
row-span-2` on the hero. Order DOM to match reading order.

## Review checklist
- [ ] Spans map to real content priority; a clear hero cell anchors it (not uniform).
- [ ] Intended scan path is legible; DOM/focus order matches; keyboard traversal sane.
- [ ] One boundary per cell (no nested cards); no filler cells.
- [ ] Regroups (not single-column collapse) on mobile; hero stays prominent.
- [ ] Interactive cells are real links/buttons with focus; content meets contrast.
- [ ] Bento is used because the content is an unequal overview — not by default.

## Examples
- **Good/brand:** a product page's feature overview — one large hero feature cell, a metric,
  a screenshot, a quote, and a CTA, in a varied grid with clear priority.
- **Good/product:** a dashboard home where the primary KPI spans large and secondary widgets
  are smaller, regrouping cleanly on mobile.
- **Bad:** a page of twelve identical square tiles called a "bento grid" — no hierarchy, just
  a uniform grid with a trendy name.
