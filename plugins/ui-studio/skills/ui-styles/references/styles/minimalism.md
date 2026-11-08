# Minimalism

## Definition
Minimalism removes everything that isn't earning its place so that what remains is clear,
intentional, and precise. It is **reduction in service of hierarchy and content** — not
emptiness. Done well it still has a strong identity: type, spacing, and one or two decisive
choices carry the whole design.

**Reject these false equivalences (they are the main failure modes):**
- minimalism = empty page → *no*, it's editing, not deleting.
- minimalism = all white → *no*, color used sparingly and deliberately is fine.
- minimalism = monochrome → *no*, restraint ≠ absence of color.
- minimalism = Inter everywhere → *no*, that's a default, not a decision; type should carry
  identity.
- minimalism = weak/flat hierarchy → *no*, minimalism demands *stronger* hierarchy.
- minimalism = hide functionality → *no*, hiding needed actions is a usability failure.

## Conceptual model
Rooted in Swiss/International typographic style, Dieter Rams' "less but better," and
editorial design. It exists to **maximize signal** — remove noise so meaning and action are
obvious, and reading is effortless. It works almost everywhere as a base; it fails when
reduction removes needed affordances, when whitespace becomes inefficiency for a task, or
when "clean" becomes "generic and characterless."

## Visual grammar
- **Negative space** as an active tool — grouping, focus, rhythm. Purposeful, not merely
  large.
- **Typography does the work:** a confident type scale, real hierarchy via size/weight/
  spacing, excellent measure (45–75ch), considered detail (tracking on display, tabular
  figures for data). Type *choice* carries identity.
- **Restraint in color:** a tight palette; accent used sparingly so it means something.
- **Precision:** exact alignment, consistent spacing scale, crisp borders/dividers used
  instead of boxes, optical adjustments.
- **Content first:** structure follows meaning; progressive disclosure reveals depth on
  demand rather than dumping everything.
- **Detail quality:** the fewer elements, the more each imperfection shows — polish is
  non-optional.
- **Motion:** subtle, functional; often none.

## Design tokens
- **Style-defining:** generous spacing scale, restrained palette (few roles), strong type
  scale, hairline borders/dividers, minimal elevation.
- **Product-dependent:** brand hue/accent, type family (a real choice), density, content.

## Component translation
Dividers and spacing instead of heavy cards; text buttons and quiet secondary actions;
inputs defined by a single line or subtle border; tables with generous rows and clear
alignment; nav pared to essentials with clear labels. Every element visible must justify
itself — but **needed actions stay discoverable** (don't hide primary functions behind
hover or mystery icons).

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** editorial minimalism — big type, lots
of air, one striking image or idea. **Product mode:** minimalism means *clarity and
efficiency*, not emptiness — tighter density, visible controls, strong scan order; don't
spend a task screen's space on landing-page air.

## When to use
Content/reading products, premium/luxury brands, productivity tools, portfolios, anything
where focus and clarity matter, or as a safe confident default when no style is signaled —
*with* a real identity choice so it isn't generic.

## When NOT to use
When the product genuinely needs high expressiveness/personality that restraint would mute;
when "minimal" is being used to justify hiding necessary functionality; when a task needs
dense information and the minimalist instinct would over-space it.

## Anti-patterns
- **Empty ≠ minimal** — Tell: vast whitespace, thin gray text, nothing to hold onto. Why:
  characterless and hard to scan. Fix: stronger type hierarchy, deliberate focal point,
  real content.
- **Generic minimalism** — Tell: white bg + Inter + one gray + centered — could be any
  product. Why: no identity. Fix: make a distinctive type/color/layout choice.
- **Hidden functionality** — Tell: primary actions behind hover or ambiguous icons. Why:
  discoverability failure. Fix: keep needed actions visible and labeled.
- **Low-contrast "elegance"** — Tell: light-gray text for a refined look. Why: fails
  contrast. Fix: meet the A1 contrast minimum; elegance ≠ faintness.
- **Weak hierarchy** — Tell: everything the same size/weight. Why: minimalism without
  hierarchy is just sparse. Fix: create a clear dominant element and scan order.
- **Over-spacing a task** — Tell: a data screen with hero-level padding. Why: inefficiency.
  Fix: match density to the task.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Hotspots: low-contrast light-gray text (the most
common minimalism failure — meet the A1 contrast minimum), focus states removed "for cleanliness" (keep them
visible), affordance clarity (buttons must look like buttons), and don't rely on subtlety so
extreme that controls disappear.

## Responsive
Minimalism scales gracefully but still needs a *rethink* on mobile, not just reflow: adjust
type scale (fluid `clamp()`), preserve measure, keep primary actions reachable, and ensure
generous desktop space doesn't become wasted mobile scrolling. Targets at the A7 house floor.

## Performance
Usually excellent (few effects). Keep it that way — resist adding gratuitous motion or
imagery. Optimize the few images/fonts you do use; subset fonts.

## Implementation guidance
Semantic HTML with a strong type scale and spacing scale as tokens; dividers/spacing over
boxes; a real (non-default) typeface where the brand allows. Tailwind/CSS: lean on spacing
and type utilities; keep the palette tokenized and tight. Don't reach for cards and shadows
by reflex.

## Review checklist
- [ ] Strong, obvious hierarchy and a clear focal point (not flat sparseness).
- [ ] A real identity choice (type/color/layout) — not generic white+Inter+gray.
- [ ] Needed actions visible and discoverable; nothing critical hidden.
- [ ] Text contrast the A1 contrast minimum; focus states present and visible.
- [ ] Density matches the task (product) or breathes intentionally (brand).
- [ ] Detail polish: alignment, spacing scale, optical adjustments.

## Examples
- **Good/brand:** an editorial portfolio with one bold typeface, decisive whitespace, a
  single accent, and one memorable layout idea.
- **Good/product:** a clean, dense writing app — clear hierarchy, visible controls,
  efficient spacing, high contrast.
- **Bad:** a "minimal" SaaS page that's just a white void, thin gray Inter text, a centered
  headline, and no identity or focal point.
