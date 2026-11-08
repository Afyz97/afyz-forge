# Brutalism & Neo-Brutalism

## Definition
Brutalism in UI is **raw, direct, and unpolished on purpose** — exposed structure, hard
edges, stark contrast, system/monospace type, and unconventional or deliberately blunt
grids. It rejects the soft, safe, gradient-and-shadow "designed" look in favor of honesty
and force.

Two related but distinct concepts (**don't collapse them**):
- **Brutalism:** stark, minimal-ornament, raw HTML energy, harsh contrast, near-default
  browser aesthetics weaponized.
- **Neo-brutalism:** the popular, more *designed* descendant — thick black borders, hard
  offset (non-blurred) shadows, bright flat color blocks, chunky components. Structured and
  brandable.

**Distinguish intentional brutalism from failure:** brutalism is *chosen* rawness with
control; it is **not** unfinished CSS, broken responsive layouts, inaccessible contrast, or
careless spacing. The difference is intent and consistency.

## Conceptual model
Named after architectural *béton brut* (raw concrete); adopted online as a counter-reaction
to homogenized, template, "safe" web design. It exists to feel **authentic, bold, human,
and anti-corporate**. It works for portfolios, editorial, culture, art, dev-tools with
attitude, and brands that want to stand out; it fails when rawness becomes genuine
brokenness or when the target audience needs comfort and familiarity.

## Visual grammar
- **Hard edges:** little/no border-radius; thick, solid borders (often black).
- **Hard shadows:** offset solid shadows (`box-shadow: 6px 6px 0 #000`), never soft blur.
- **Stark contrast & flat color:** bold blocks, high-contrast pairings, no gradients (or
  deliberately crude ones).
- **Typographic force:** big, heavy, sometimes monospace or default system type; type as a
  structural element.
- **Exposed structure:** visible grids, raw borders, unhidden layout; sometimes intentional
  asymmetry or "wrong" alignment used consistently.
- **Minimal decoration:** function and structure over polish; ornament is suspect.
- **Motion:** blunt, instant, or none; abrupt over smooth.
- **States:** obvious and chunky — pressed shifts the offset shadow, hover flips colors.

## Design tokens
- **Style-defining:** border width (thick), radius (near-0), offset hard-shadow, flat bold
  palette, heavy/mono type, high-contrast pairs.
- **Product-dependent:** brand colors within the flat palette, content, breakpoints.

```css
.brut {
  background: #ffde00; color: #000;
  border: 3px solid #000; border-radius: 0;
  box-shadow: 6px 6px 0 #000;
  font-weight: 800;
}
.brut:active { box-shadow: 2px 2px 0 #000; transform: translate(4px,4px); }
.brut:focus-visible { outline: 3px solid #000; outline-offset: 3px; }
```

## Component translation
Chunky bordered buttons with offset shadows; hard-edged inputs with thick borders and visible
labels; cards as bold bordered blocks; nav as a stark bar; tables with heavy rules. Neo-
brutalism systematizes this into a clean component kit; pure brutalism keeps it rawer. Either
way, keep it *consistent* — inconsistency reads as broken, not brutal.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** brutalism shines — portfolios,
editorial, launches, culture. **Product mode:** neo-brutalism can work as a bold, usable
component system (thick borders + clear states aid affordance), but keep density and contrast
sane for daily use; avoid pure raw brutalism on tools people rely on for hours.

## When to use
Portfolios, editorial/culture/art, dev tools and indie products with attitude, launches,
brands that want to signal confidence and difference; audiences who read the rawness as
intentional.

## When NOT to use
Audiences needing comfort/familiarity (healthcare, finance for broad consumers), dense data
tools where harsh contrast fatigues, or any context where "raw" will be read as "broken."
Never use brutalism as an excuse for inaccessible contrast or careless spacing.

## Anti-patterns
- **Broken masquerading as brutal** — Tell: overlapping/misaligned elements, broken mobile.
  Why: it's just broken. Fix: rawness must be consistent and controlled; fix real breakage.
- **Inaccessible contrast** — Tell: e.g. pure red on black, tiny harsh text. Why: fails
  contrast/legibility. Fix: verify real ratios; brutal ≠ unreadable.
- **Random inconsistency** — Tell: different border widths/shadows/alignments everywhere.
  Why: reads as accident. Fix: systematize the rawness (consistent border, shadow, grid).
- **No hierarchy** — Tell: everything equally loud/bordered. Why: nothing leads. Fix: use
  scale and color weight to create a focal path.
- **Ornament creep** — Tell: gradients, soft shadows, rounded corners sneaking in. Why:
  dilutes the language. Fix: commit to hard edges and flat color.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Brutalism *can* be highly accessible (bold type,
thick borders, obvious focus) — but verify: real contrast ratios (harsh ≠ compliant), visible
focus (a thick solid outline suits the style), keyboard operability, target size, and
readable body measure even with heavy type. Don't confuse aesthetic harshness with contrast
compliance.

## Responsive
Keep it *intentionally* raw at every breakpoint — a broken mobile layout is failure, not
style. Stack the exposed grid deliberately; keep thick borders/shadows proportional; targets
at the A7 house floor; ensure heavy type stays readable on small screens.

## Performance
Generally excellent — flat colors, hard shadows, no blur/gradients. Keep it lean; avoid
heavy web fonts if a bold system/mono stack conveys the same force.

## Implementation guidance
Plain CSS excels here: thick borders, `border-radius: 0`, offset solid `box-shadow`, flat
palette, heavy/mono type, translate-on-press. Neo-brutalism maps cleanly to a component kit
(Button/Card/Input variants). Tailwind: `border-4 border-black shadow-[6px_6px_0_#000]
rounded-none`. Keep it consistent via tokens.

## Review checklist
- [ ] Rawness is consistent and intentional — nothing actually broken or misaligned.
- [ ] Contrast verified (not just "looks harsh"); focus visible; keyboard operable.
- [ ] Clear hierarchy/focal path despite the loud treatment.
- [ ] Hard edges + flat color + offset shadows held consistently (no soft-shadow creep).
- [ ] Mobile is deliberately composed, not a broken desktop; targets at the A7 house floor.

## Examples
- **Good/brand:** a designer portfolio in stark black-on-yellow, thick borders, monospace
  headings, offset shadows, one clear CTA.
- **Good/product:** a neo-brutalist SaaS with a consistent bordered component kit, clear
  states, and verified contrast.
- **Bad:** a site with misaligned overlapping blocks and red-on-black text that's actually
  broken and unreadable, defended as "brutalism."
