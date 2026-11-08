# Glassmorphism

## Definition
Glassmorphism is a **material**: a translucent surface that blurs and tints whatever is
behind it, with a subtle bright edge, sitting in a layered stack that implies depth. Its
meaning comes from the **relationship to the background** — remove the background and it's
just a semi-transparent box.

**Distinguish from:**
- **Generic transparent card:** opacity only, no blur, no edge, no layering — not glass.
- **Liquid Glass (Apple):** a dynamic, adaptive *platform* material that refracts/reflects
  and responds to motion/content; glassmorphism is a static web approximation. See
  `liquid-glass.md`.
- **Simple frosted overlay:** a full-screen scrim; glass is a *layered element* with edges.
- **Neumorphism:** opaque same-surface extrusion, no transparency.

Do **not** reduce it to `backdrop-filter: blur()`. Without a considered background, tint,
edge, and contrast plan, blur alone is not glassmorphism — it's a readability problem.

## Conceptual model
Popularized ~2020 (and rooted in iOS/macOS vibrancy and Windows Acrylic). It exists to show
**hierarchy through layering** — a floating panel that's clearly *above* content while
staying connected to it. It works over rich, colorful, or image backgrounds where the blur
has something to do. It fails over flat/plain backgrounds (nothing to blur), when overused
(every surface glass = mush), and whenever text contrast isn't guaranteed.

## Visual grammar
- **Translucency + blur:** semi-transparent fill (`rgba`/`color-mix` ~10–30% opacity) plus
  `backdrop-filter: blur()` (typically 8–20px) and often slight `saturate()` to keep colors
  lively.
- **Edge definition:** a thin light border and/or inner top highlight — glass has edges;
  this is what separates it from a transparent card.
- **Depth & layering:** clearly stacked; soft drop shadow beneath; a background worth
  blurring (gradient, imagery, color field).
- **Tint:** subtle, purposeful; can carry brand or adapt to background.
- **Contrast management:** the hard part — a tint/scrim strong enough to keep text the A1 contrast minimum
  regardless of what's behind it.
- **Typography:** high-contrast, never thin gray-on-busy.
- **Motion:** gentle; parallax between layers can reinforce depth but is optional and costs
  performance.

## Design tokens
- **Style-defining:** surface opacity, blur radius, saturation, edge/border color+opacity,
  inner highlight, layer shadow, tint hue.
- **Product-dependent:** brand tint, the background system, type, spacing, density.

```css
.glass {
  background: color-mix(in srgb, var(--tint, #ffffff) 14%, transparent);
  backdrop-filter: blur(14px) saturate(1.2);
  -webkit-backdrop-filter: blur(14px) saturate(1.2);
  border: 1px solid rgba(255,255,255,.25);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 8px 30px rgba(0,0,0,.18);
  border-radius: 16px;
  color: #fff; /* verify the A1 contrast minimum against the *effective* blurred background */
}
@supports not (backdrop-filter: blur(1px)) { .glass { background: var(--surface-solid); } }
@media (prefers-reduced-transparency: reduce) { .glass { background: var(--surface-solid); backdrop-filter: none; } }
```

## Component translation
Best on **floating layers**: nav bars/headers, sidebars over imagery, modals/sheets,
notification/toast cards, hero cards over a photo, media overlays. Keep it to the layer that
floats; do **not** make base content, tables, or dense forms glass. Never stack glass on
glass (blur compounds into mud).

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** expressive hero glass over rich imagery
is great. **Product mode:** confine glass to the chrome (top bar, command palette, dialog)
over a calm background; keep working surfaces opaque and dense. Ensure the effect survives
whatever real content scrolls behind it.

## When to use
Rich/colorful/photographic backgrounds; a floating control or navigation layer that should
read as "above"; hero and marketing moments; media/entertainment/creative products; overlays
that benefit from seeing context behind them.

## When NOT to use
Flat/plain backgrounds (nothing to blur), text-heavy or data-dense surfaces, accessibility-
critical flows without a guaranteed scrim, low-end devices/large blur regions, or when the
background behind the glass is uncontrolled and could destroy contrast.

## Anti-patterns
- **Glass with nothing behind it** — Tell: blurred panel on a solid flat bg. Why: no depth,
  no point. Fix: give it a background worth blurring or drop the effect.
- **Everything is glass** — Tell: every surface translucent. Why: layering meaningless,
  contrast chaos, perf hit. Fix: one floating glass layer; solid base.
- **Unreadable text** — Tell: light text over a variable/busy blur. Why: contrast fails as
  the background changes. Fix: add tint/scrim to guarantee the A1 contrast minimum; darken/lighten the fill.
- **No edge** — Tell: it looks like a plain opacity card. Why: missing the defining border/
  highlight. Fix: add a thin light border + inner top highlight.
- **Glass on glass** — Tell: stacked translucent layers. Why: compounding blur = mud. Fix:
  make lower layers solid.
- **Excessive floating rounded containers** — Tell: a page of hovering glass pills. Why:
  slop. Fix: reduce to intentional layers.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

Text contrast must hold against the *effective*
(blurred) background — because that background varies, add a tint/scrim so the worst case
still meets the A1 contrast minimum. Provide a solid fallback for `prefers-reduced-transparency` and for no
`backdrop-filter` support. Keep focus rings visible over glass (they can wash out). Don't
encode meaning in translucency alone.

## Responsive
Blur is costlier on mobile GPUs and large regions; reduce blur radius or switch to a
translucent-solid on small screens. Ensure the background system still gives the glass
something to blur at every breakpoint. Targets at the A7 house floor.

## Performance
`backdrop-filter` is one of the most expensive CSS effects, especially over large or
animated regions and when stacked. Limit count and area; avoid animating blur; avoid glass on
scrolling lists; provide `@supports` and reduced-transparency fallbacks; test on low-end
hardware.

## Implementation guidance
CSS `backdrop-filter` + `-webkit-` prefix, a translucent fill via `color-mix`/`rgba`, a thin
border, and a shadow. Always ship the `@supports not` and `prefers-reduced-transparency`
fallbacks. In React/Vue/Svelte/shadcn, make `.glass` a variant token, not a per-component
hack. Tailwind: `backdrop-blur`, `bg-white/10`, `border-white/20` — but still verify
contrast and add fallbacks. Don't claim it equals native platform glass.

## Review checklist
- [ ] There's a real background worth blurring; effect limited to floating layers.
- [ ] Translucency + blur + edge/highlight + layer shadow all present (not opacity-only).
- [ ] Text the A1 contrast minimum against the worst-case blurred background (tint/scrim in place).
- [ ] `@supports` + reduced-transparency fallbacks; focus visible over glass.
- [ ] No glass-on-glass; blur count/area reasonable on mobile.

## Examples
- **Good/brand:** a translucent nav and a hero card floating over a vivid gradient/photo,
  white text on a tint that guarantees contrast.
- **Good/product:** a frosted command palette / dialog over a dimmed app.
- **Subtle:** a glass top bar that tints the content scrolling beneath it.
- **Bad:** a whole dashboard of stacked glass cards on a flat gray page — no depth, muddy,
  failing contrast, slow on mobile.
