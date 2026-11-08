# Claymorphism

## Definition
Claymorphism gives elements a **soft, inflated, 3-D "clay" mass** — thick rounded shapes that
look moldable and tactile, using a **big outer drop shadow plus two inner shadows** (one
light, one dark) to fake volume and a soft top light. It feels friendly, playful, and
approachable.

**Distinguish from:**
- **Neumorphism:** low-contrast, same-surface, subtle; clay is higher-contrast, colorful,
  and clearly a floating 3-D object.
- **Skeuomorphism:** imitates real materials/objects; clay is abstract puffy geometry.
- **Glassmorphism:** translucent; clay is opaque and solid.
- **Flat with big radius:** clay adds the inner/outer shadow volume; a rounded flat card is
  not clay.

Do **not** reduce it to "rounded corners." The inflated volume (inner + outer shadow pair)
and generous mass are the point.

## Conceptual model
Popular in illustration-forward product design (~2021+), 3-D icon sets, and friendly
consumer/education apps. It exists to feel **soft, safe, and fun** — to lower intimidation.
It works for playful brands and light consumer tasks; it fails when applied to serious,
dense, or formal contexts (it reads childish), when every element inflates (visual chaos),
or when shadows accumulate into muddy soup.

## Visual grammar
- **Inflated geometry:** thick, generous radius; shapes look puffed. Chunky buttons, pill
  toggles, rounded cards.
- **Volume shadows:** large soft outer drop shadow + inner light (top) and inner dark
  (bottom) shadows. This pair is the signature.
- **Color:** bright, saturated, friendly — often pastel or candy palettes; strong fills.
- **Light:** soft, from the top; consistent.
- **Depth:** clearly floating objects with obvious mass.
- **Typography:** rounded, friendly, but still legible and high-contrast on the fills.
- **Iconography:** 3-D or soft, matching the puffy language.
- **Motion:** bouncy/springy but restrained; a little squash-and-stretch suits clay.
- **States:** press = slight squash/scale-down; keep it subtle.

## Design tokens
- **Style-defining:** radius (large), outer shadow, inner-light shadow, inner-dark shadow,
  fill saturation, springy motion.
- **Product-dependent:** brand palette, type, spacing, density, content.

```css
.clay {
  background: #7c5cff; color: #fff;
  border-radius: 28px;
  box-shadow:
    0 12px 24px rgba(124,92,255,.35),          /* outer volume */
    inset 0 6px 10px rgba(255,255,255,.35),    /* top inner light */
    inset 0 -8px 10px rgba(0,0,0,.20);         /* bottom inner dark */
}
.clay:active { transform: scale(.97); }
```

## Component translation
Great on: primary buttons, toggles, feature tiles, onboarding illustrations, empty states,
badges, playful hero objects, kids/education controls. Restrain on: tables, dense forms,
long text, data — keep those flat and legible. Inflate a *few* hero objects, not the whole
page.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** playful landing pages, mascots,
onboarding, and consumer marketing can go full clay. **Product mode:** use clay as *accents*
— the primary CTA, an empty-state illustration, an achievement badge — while the working
surfaces stay calm and dense. Clay on a whole operational app looks unserious.

## When to use
Kids/education, games, wellness/lifestyle, playful consumer apps, onboarding, empty/success
states, friendly brands wanting warmth and approachability.

## When NOT to use
Finance/enterprise/medical/legal or any authority-signaling product, data-dense dashboards,
formal tools, accessibility-critical dense forms, or anywhere "fun" undermines trust.

## Anti-patterns
- **Everything is a toy** — Tell: every element inflated. Why: no hierarchy, unserious,
  chaotic. Fix: inflate a few focal objects; flatten the rest.
- **Shadow soup** — Tell: overlapping puffy shadows accumulate into gray mud. Why: kills
  legibility and depth. Fix: cap inflated elements; reduce shadow spread; add space.
- **Childish in the wrong domain** — Tell: clay on a banking/enterprise app. Why: erodes
  trust. Fix: switch to a restrained style or confine clay to onboarding/marketing.
- **Unreadable density** — Tell: chunky components crammed together. Why: mass needs
  breathing room. Fix: increase spacing; fewer, larger objects.
- **Low-contrast pastels** — Tell: pale text on pale clay. Why: fails contrast. Fix:
  high-contrast text; saturate fills enough for legibility.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Hotspots: pastel-on-pastel contrast (guarantee
the A1 contrast minimum text), visible focus rings that survive on saturated fills, pressed state cue beyond
squash (color/label), target size on chunky-but-not-huge controls, reduced motion for bounce.

## Responsive
Big soft shadows and large radii scale down on mobile — reduce shadow spread and mass;
maintain generous spacing so inflated elements don't collide; targets at the A7 house floor; drop
decorative 3-D illustrations that don't fit small screens.

## Performance
Multiple large soft + inner shadows per element are costly at scale; cap inflated elements;
avoid animating `box-shadow` (animate transform/scale); use SVG/optimized raster for 3-D
illustrations and lazy-load them.

## Implementation guidance
Pure CSS (triple `box-shadow` + big radius + saturated fill + `scale` on press). Encapsulate
as an accessible component with real focus/roles. Springy motion via a small transition or a
spring library, gated behind reduced-motion. Tailwind: custom shadow token + `rounded-3xl`.

## Review checklist
- [ ] Inflated volume present (outer + inner-light + inner-dark), not just rounded corners.
- [ ] Clay concentrated on focal objects; content/data stays flat and dense.
- [ ] Text the A1 contrast minimum on fills; focus visible; press cue beyond squash.
- [ ] Domain fit (playful/consumer, not formal/enterprise).
- [ ] Spacing prevents shadow soup; targets at the A7 house floor; reduced-motion honored.

## Examples
- **Good/brand:** a kids' learning app home with a few big puffy category tiles and a bouncy
  primary button.
- **Good/product accent:** a clay success illustration + CTA on an otherwise flat consumer
  app's empty state.
- **Bad:** an enterprise analytics dashboard where every KPI tile, filter, and row is puffy
  clay — unserious, muddy, low-contrast.
