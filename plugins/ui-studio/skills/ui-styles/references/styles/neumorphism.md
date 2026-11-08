# Neumorphism (Soft UI)

## Definition
Neumorphism renders controls as if **extruded from a single continuous surface** of the same
color as the background, using a **paired light highlight and dark shadow** to imply the
element is raised (embossed) or recessed (debossed). The whole UI shares one material and
one light source.

**Distinguish from:**
- **Skeuomorphism:** distinct materials/textures/metaphors; neumorphism is one abstract
  monochrome surface.
- **Glassmorphism:** translucent layers over a background; neumorphism is opaque same-color.
- **Flat/minimal:** no extrusion at all.
- **Claymorphism:** inflated, higher-contrast, colorful 3-D blobs; neumorphism is subtle and
  low-contrast.

Do **not** reduce it to "two box shadows." The defining discipline is contrast management,
not the shadow pair.

## Conceptual model
Emerged ~2019–2020 as a soft evolution of flat design + skeuomorphism. Its appeal is calm,
premium, cohesive surfaces. Its fatal flaw is baked in: because elements share the
background color and rely on faint shadows, **contrast is inherently low** — which fights
legibility, affordance, and WCAG. Treat neumorphism as a *limited aesthetic for a few
showcase surfaces*, not a system for operational UI. If you use it, you must actively fight
its default failures.

## Visual grammar
- **Single surface:** background and elements the same base color; slightly off-white or
  off-dark works best (pure white/black kill the effect).
- **Paired shadows:** one light shadow (toward the light source, usually top-left) and one
  dark shadow (opposite). Raised = outer shadows; pressed = inner (inset) shadows.
- **Light-source consistency:** one direction everywhere. Mixed directions read as broken.
- **Radius:** soft, generous, consistent.
- **Color:** low-saturation, low-contrast surfaces — *but* text and icons must break that
  rule to stay legible (see accessibility).
- **Depth:** shallow. Overdeep shadows look muddy.
- **States:** raised (default) → inset (pressed). Must be paired with a non-depth cue.

## Design tokens
- **Style-defining:** base surface color, light-shadow color, dark-shadow color, shadow
  offset/blur, light-source direction, inset vs outset toggle, radius.
- **Product-dependent:** accent color for text/icons/focus (must be high-contrast), type,
  spacing, density.

```css
:root {
  --surface: #e0e5ec;
  --sh-dark: #a3b1c6;
  --sh-light: #ffffff;
  --text: #1f2733;      /* deliberately HIGH contrast against the soft surface */
}
.neu-raised {
  background: var(--surface); border-radius: 16px;
  box-shadow: 6px 6px 12px var(--sh-dark), -6px -6px 12px var(--sh-light);
  color: var(--text);
}
.neu-pressed { box-shadow: inset 6px 6px 12px var(--sh-dark), inset -6px -6px 12px var(--sh-light); }
.neu-raised:focus-visible { outline: 3px solid #2f6fed; outline-offset: 3px; } /* visible, not soft */
```

## Component translation
Safe: hero cards, media players, a calculator, a single showcase toggle, dashboards' *frame*
(not the data). Risky and usually wrong: text inputs, dense forms, tables, primary CTAs
that must pop, anything where users must instantly recognize what's clickable. For inputs,
**add a real border or clear inset + a high-contrast label** or don't use neumorphism there.

## Brand vs product mode
See `../brand-vs-product.md`. Neumorphism suits **brand/showcase** surfaces and calm
consumer apps. In **product mode** it's mostly wrong: keep it to a decorative frame or a
single control and use conventional, high-contrast controls for the working surfaces.

## When to use
Calm consumer apps (meditation, smart-home, music), a showcase/portfolio piece, a single
premium control, light-touch dashboards where the data itself carries contrast.

## When NOT to use
Data-entry forms, dense tables, accessibility-critical products, high-glare environments,
anything needing obvious primary actions, low-DPI/older displays where faint shadows vanish.
When in doubt, don't.

## Anti-patterns (neumorphism fails aggressively — hunt these)
- **Invisible controls** — Tell: you can't tell what's tappable. Why: same color + faint
  shadow = no affordance. Fix: add border/contrast/label; elevate primary actions out of
  the neumorphic treatment.
- **Everything looks disabled** — Tell: active and inactive elements look identical. Why:
  low contrast erases state. Fix: differentiate state with color/opacity/icon, not depth.
- **Ambiguous pressed state** — Tell: can't tell inset from outset at a glance. Why: subtle
  shadow flip. Fix: pair with color/label change; increase inset depth for pressed.
- **Insufficient text contrast** — Tell: gray text on gray surface. Why: fails A1. Fix:
  high-contrast text/icons; the surface stays soft, the *content* does not.
- **Same-surface everything** — Tell: the entire UI is one embossed field. Why: no
  hierarchy. Fix: reserve the effect for a few elements.
- **Unusable forms** — Tell: neumorphic inputs with no border. Why: users can't find fields.
  Fix: bordered/inset fields with visible focus, or drop the style for forms.

## Accessibility (overrides style purity)
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Neumorphism is the suite's highest-risk style.
Mandatory: text/icon contrast the A1 contrast minimum (break the low-contrast surface for content); **visible,
high-contrast focus rings** (not soft); non-text UI contrast the A1 non-text minimum for control boundaries —
which usually means adding a border because shadow-only edges fail; state cues beyond depth;
target size at the A7 house floor; reduced motion on press animations. **If the style can't meet contrast on
a given surface, the style loses, not the user.**

## Responsive
Shadows scale poorly on small/low-DPI screens — reduce offset/blur or switch to bordered
flat controls on mobile. Keep targets at the A7 house floor. Don't rely on hover (touch has none) to reveal
affordance.

## Performance
Every neumorphic element carries two shadows; hundreds of them are expensive and repaint on
theme/scroll. Cap the count; avoid animating `box-shadow` (animate transform or pre-composite);
avoid neumorphism on long lists.

## Implementation guidance
Pure CSS (`box-shadow` pairs + inset for pressed). In component frameworks, wrap as an
accessible `<button>`/`<input>` with real focus and roles — never a bare `<div>`. Tailwind:
express the shadow pair as a custom shadow token. Keep the accent/text/focus colors in
high-contrast tokens, separate from the soft surface tokens.

## Review checklist
- [ ] Every control is recognizably interactive (contrast/border/label, not shadow alone).
- [ ] Text/icon contrast the A1 contrast minimum; focus ring visible and high-contrast; UI boundaries the A1 non-text minimum.
- [ ] Pressed vs raised distinguishable by more than depth.
- [ ] State (active/disabled/selected) legible without relying on the soft effect.
- [ ] Effect limited to a few surfaces; forms are usable; targets at the A7 house floor.
- [ ] One light source; shadow count/perf reasonable; reduced-motion honored.

## Examples
- **Good/showcase:** a single neumorphic music-player card with a high-contrast play icon
  and clear focus ring, on a calm app.
- **Subtle:** one soft toggle in an otherwise flat settings page.
- **Bad:** an entire admin form in gray-on-gray neumorphic fields with no borders — users
  can't find inputs, contrast fails, everything looks disabled.
