# Skeuomorphism

## Definition
Skeuomorphism designs digital objects to resemble their real-world counterparts so that
**recognition and affordance transfer** from the physical world: a switch you flip, a knob
you turn, a notepad you write on. The point is *communicated function through familiar
form*, not photorealistic decoration.

**Distinguish from:**
- **Flat/minimal:** removes real-world cues in favor of abstraction.
- **Neumorphism:** extrudes controls from a *single* surface with soft same-color shadows;
  skeuomorphism uses *distinct materials, textures, and light*.
- **Claymorphism:** soft inflated abstract shapes, not real-object metaphors.
- **Decorative realism / "fake realism":** texture and gloss with no functional metaphor —
  the failure mode, not the goal.

Do **not** reduce it to "add a wood texture." A skeuomorphic control must behave and read
like the thing it imitates.

## Conceptual model
Rooted in early GUI (desktop, trash can) and mobile's 2007–2013 era (leather calendars,
felt game tables). It exists because **familiar affordances lower learning cost** — people
know how a dial or toggle works. It works when the metaphor genuinely maps to the function
and the audience recognizes it. It fails when the metaphor is obsolete (a floppy-disk save
icon is borderline; a Rolodex is dead), when ornament outweighs function, or when realism
fights legibility. **Modern skeuomorphism** is restrained: selective tactile cues on the
controls that benefit, clean type and layout elsewhere.

## Visual grammar
- **Material & texture:** subtle, purposeful (brushed metal on a control surface, soft paper
  for a writing area). Texture supports the metaphor; it is not wallpaper.
- **Depth & light:** a *consistent* light source (usually top). Highlights on top edges,
  shadows below; bevels and insets that imply real geometry.
- **Form:** controls shaped like their referents — rounded tactile buttons, grooved sliders,
  recessed screens. Real bezels, seams, and rims where they clarify function.
- **Shadows:** realistic contact/drop shadows (soft, directional), not glow.
- **Color:** material-derived (metal grays, warm woods, screen greens) but still meeting
  contrast on any text.
- **Typography:** normal, legible type placed on clean areas — never body text on texture.
- **Motion:** physical — a switch throws, a knob rotates, a key depresses; short and
  weighty. Motion confirms the tactile metaphor.
- **Interaction states:** pressed = visibly depressed/inset; toggled = physically moved.

## Design tokens
- **Style-defining:** material/texture assets, bevel & inset shadow pairs, edge highlight,
  contact-shadow ladder, light-source direction, radius that matches real objects, tactile
  press-transform.
- **Product-dependent:** brand hue, type family, spacing/density, breakpoints, content.

```css
.control-metal {
  background: linear-gradient(180deg, #f4f5f7, #c9ccd3);
  border-radius: 12px;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.9),        /* top edge highlight */
    inset 0 -2px 3px rgba(0,0,0,.15),          /* inner underside */
    0 2px 4px rgba(0,0,0,.25);                 /* contact shadow */
}
.control-metal:active { box-shadow: inset 0 2px 4px rgba(0,0,0,.35); transform: translateY(1px); }
```

## Component translation
Apply realism **only where a physical metaphor helps** — sliders, toggles, dials, knobs,
step controls, media transport, a signature/drawing surface. Keep tables, forms, nav, and
long text on clean surfaces with legible flat type. Do not emboss every button, input, and
card; that produces noise and kills hierarchy.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode** (a product landing, a museum piece, a
game menu) can go fully tactile and rich. **Product mode** uses skeuomorphism as *targeted
affordance*: the one control users manipulate constantly gets tactile realism; the rest of
the app stays clean and dense.

## When to use
Audio/DAW/instrument UIs, calculators, thermostats/home controls, camera/photo tools, games,
kids/education, nostalgia/brand pieces, any control that benefits from real-world muscle
memory; audiences who recognize the referent.

## When NOT to use
Data-dense dashboards, admin/SaaS with heavy typing and scanning, anything needing high
information density, obsolete/unfamiliar metaphors, low-performance contexts, or when the
texture would sit under text. If the metaphor doesn't map to a real interaction, don't use
it.

## Anti-patterns
- **Decorative fake realism** — Tell: textures/gloss with no functional metaphor. Why: noise
  without benefit. Fix: remove, or tie the material to a real control.
- **Metaphor without behavior** — Tell: a "knob" that's actually a normal button. Why:
  breaks the affordance promise. Fix: make it behave like the referent or restyle it.
- **Obsolete metaphor** — Tell: referents younger users don't recognize (Rolodex, cassette).
  Why: no recognition transfer. Fix: pick a living metaphor or go abstract.
- **Text on texture** — Tell: body text over wood/leather/noise. Why: contrast/legibility
  failure. Fix: put text on a clean inset panel.
- **Inconsistent physics** — Tell: light from different directions across controls. Why:
  reads as fake. Fix: one light source everywhere.
- **Ornament overload** — Tell: every element beveled and shadowed. Why: no hierarchy. Fix:
  reserve depth for interactive/important objects.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Hotspots: text over textured/material surfaces
(guarantee the A1 contrast minimum on a clean panel), pressed/toggled states must also differ by more than
depth (add label/icon/position), visible focus rings that survive on metallic surfaces,
target size on tactile controls, reduced-motion for physical animations, and don't encode
state by material sheen alone.

## Responsive
Tactile controls must remain at the A7 house floor and grabbable on touch; on small screens, reduce texture
detail (it muddies at low DPI zoom) and drop non-essential ornament; keep the *affordance*,
shed the *decoration*. Provide pointer, touch, and keyboard operation for every control.

## Performance
Large texture images and multi-layer inset+drop shadows are the cost. Use small tiled
textures or CSS gradients over raster where possible; cap shadow layers; avoid animating
`box-shadow` (animate transform); lazy-load heavy material assets; provide a flat fallback.

## Implementation guidance
CSS gradients + layered `box-shadow` handle most tactile surfaces without images; add
subtle noise via a tiny tiled PNG or SVG only where needed. In React/Vue/Svelte, encapsulate
tactile controls as accessible components (real `role`, keyboard handlers) that *look*
physical. SwiftUI/Flutter can use gradients, shadows, and material where the platform
supports it. Don't swap the project's framework for realism.

## Review checklist
- [ ] Every realistic element maps to a real interaction (metaphor = behavior).
- [ ] Realism concentrated on controls; content/text on clean, legible surfaces.
- [ ] One consistent light source; consistent physics.
- [ ] Pressed/toggled states differ by more than sheen; contrast met; focus visible.
- [ ] Targets at the A7 house floor; reduced-motion honored; flat fallback for low performance.
- [ ] No decorative-only textures; no obsolete metaphors; text never on texture.

## Examples
- **Good/product:** a mixing app where only the faders and knobs are tactile; the track list
  and menus are clean and dense.
- **Good/brand:** a nostalgic game main menu rendered as a physical console.
- **Subtle:** a single tactile toggle in an otherwise flat settings screen, to signal a
  hardware-like on/off.
- **Bad:** a finance dashboard wrapped in leather with wood-grain cards and embossed KPI
  tiles — texture under data, no metaphor, poor contrast.
