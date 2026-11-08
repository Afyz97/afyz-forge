# Maximalism

## Definition
Maximalism embraces abundance — dense layering, expressive type, color, pattern, and imagery
— but it is **controlled** abundance. The defining discipline is hierarchy: even at high
visual density, the eye still knows where to go first. Maximalism is composed, not cluttered.

**Distinguish maximalism from random clutter:** clutter has no hierarchy, no rhythm, no
intent — just stuff. Maximalism has a clear focal path, deliberate contrast, and a system
underneath the exuberance.

## Conceptual model
A reaction against generic minimalism and template sameness; rooted in editorial/magazine
design, poster art, zines, and expressive brand work. It exists to create **personality,
energy, and memorability**. It works for brand/marketing, culture, fashion, music, events,
and opinionated products; it fails for dense operational tasks, and it fails the moment
hierarchy collapses into noise.

## Visual grammar
- **Deliberate layering & overlap:** elements overlap and interact with intent; depth via
  stacking, not chaos.
- **Expressive typography:** large display type, mixed weights/styles, type as image;
  contrast between a display face and a readable body face.
- **Color interaction:** bold, multi-color palettes used with a system (dominant, secondary,
  accents); high-energy but coordinated.
- **Pattern & texture:** backgrounds, borders, motifs — as structure, not filler.
- **Image density:** many images, but arranged with rhythm and scale contrast.
- **Asymmetry & editorial composition:** intentional off-grid moments, pull quotes, scale
  jumps, varied section rhythm.
- **Rhythm:** strong beat of big/small, loud/quiet, dense/open — this is what prevents
  monotony *and* chaos.
- **Motion:** can be expressive but must not overwhelm; still respects reduced-motion.

## Design tokens
- **Style-defining:** multi-role bold palette, display type scale + weights, pattern/texture
  assets, layering/z-scale, large scale-contrast steps.
- **Product-dependent:** brand identity, content, breakpoints, density.

## Component translation
Heroes and section headers go big and expressive; cards can vary in size and treatment (not
a uniform grid — see `bento-grid.md` if modular); pull quotes, oversized numbers (only
where meaningful), layered imagery. **Keep functional components legible:** forms, nav, and
any data stay clear even inside a loud design — expressiveness lives in the *composition and
identity*, not in breaking the controls.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode** is maximalism's home — campaigns,
editorial, culture, events. **Product mode:** confine maximalism to identity surfaces
(marketing, empty states, onboarding) and keep the working app calm; a maximalist dashboard
is almost always noise. If the product *is* expressive by nature (a music or fashion app),
apply energy to chrome and hero moments, restraint to content.

## When to use
Brand/marketing sites, editorial, fashion/music/culture/events, portfolios that want to be
unforgettable, launches, anything whose goal is personality and impact over efficiency.

## When NOT to use
Dashboards, admin, data-heavy tools, forms, anything used repeatedly for tasks, low-attention
or high-stress contexts, or audiences who need calm and speed.

## Anti-patterns
- **Clutter, not maximalism** — Tell: no focal point; everything competes. Why: hierarchy
  collapsed. Fix: establish one clear dominant element per view; demote the rest.
- **No system** — Tell: random colors/fonts/sizes. Why: reads as broken, not bold. Fix:
  define palette roles, a type system, and scale steps — then be exuberant within them.
- **Monotone density** — Tell: everything equally loud/dense. Why: no rhythm; exhausting.
  Fix: vary scale and quiet/loud; give the eye rest.
- **Illegible text** — Tell: type over busy imagery/pattern. Why: contrast fails. Fix:
  scrims, panels, or clear zones for text.
- **Motion overload** — Tell: everything animating/parallaxing. Why: overwhelming, perf hit,
  motion-sickness. Fix: pick a few moments; respect reduced-motion.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Hotspots: text over busy backgrounds (add
scrims/zones to hold the A1 contrast minimum), color-only meaning in a multi-color palette (add text/icon),
motion overload (reduced-motion path essential), and focus visibility against loud
backgrounds. Density must not defeat keyboard/scan order.

## Responsive
Maximalism must be *recomposed* per breakpoint, not shrunk: reduce simultaneous layers,
resequence overlaps, and protect legibility on small screens. Keep the energy but cut the
element count on mobile; targets at the A7 house floor.

## Performance
Many images, patterns, fonts, and animations add up. Optimize/lazy-load imagery, subset
fonts, cap simultaneous animations, and use compositor-friendly motion. Watch total page
weight.

## Implementation guidance
Grid/flex with intentional overlap (negative margins, `grid` overlap, z-scale); a display +
body type pairing as tokens; a systematized bold palette; optimized imagery. Keep functional
components as clean accessible primitives inside the loud shell. Tailwind/CSS: lean on custom
type/color tokens; don't let utility sprawl hide the system.

## Review checklist
- [ ] Clear focal point and scan order despite density (not clutter).
- [ ] A real system underneath: palette roles, type system, scale steps.
- [ ] Rhythm — variation of loud/quiet, big/small — with rest points.
- [ ] Text legible everywhere (scrims/zones); contrast the A1 contrast minimum.
- [ ] Functional components stay usable; reduced-motion honored.
- [ ] Recomposed (not shrunk) on mobile; imagery/fonts optimized.

## Examples
- **Good/brand:** a music-festival site — oversized type, layered photos, a bold coordinated
  palette, clear "buy tickets" focal action, varied section rhythm.
- **Good/product accent:** an expressive marketing/onboarding flow bolted onto an otherwise
  calm app.
- **Bad:** a "bold" dashboard where every panel is a different loud color and font with no
  focal point — that's clutter, not maximalism.
