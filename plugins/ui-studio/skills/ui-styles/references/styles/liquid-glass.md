# Liquid Glass

> Requires current care: Liquid Glass is a specific, evolving Apple platform material
> (introduced WWDC 2025 across iOS/iPadOS 26, macOS Tahoe, and visionOS). Verify current
> Apple Human Interface Guidelines (developer.apple.com/design) before implementing on
> Apple platforms. This skill is grounded in that guidance; details evolve.

## Definition — three distinct things (never conflate)
1. **Authentic platform-native Liquid Glass:** a *dynamic, adaptive material* provided by
   Apple's frameworks. It refracts and reflects surrounding content, adapts its appearance
   to what's behind and to light/dark, responds to motion, and can fluidly change shape.
   Used for the **controls and navigation layer that floats above content** — tab bars,
   toolbars, sidebars, sheets, controls — not as a skin on content itself.
2. **Web implementation inspired by Liquid Glass:** a CSS approximation (layered
   `backdrop-filter`, tint, edge highlights, subtle motion). It can *evoke* the look but is
   **not** the real material and lacks true real-time refraction/adaptivity.
3. **Ordinary glassmorphism:** a static frosted-glass card look (see `glassmorphism.md`).
   Liquid Glass is more dynamic, more adaptive, and specifically a *system control layer*.

**Do not build "Apple clone" interfaces by default, and never claim a CSS approximation is
identical to the native material.**

## Conceptual model
Liquid Glass unifies Apple's platforms around a single adaptive material for the interactive
layer. The core idea: a **distinct "glass" layer of controls floats above a content layer**,
staying legible and contextual by adapting to its surroundings rather than sitting as opaque
chrome. It exists to keep controls present but deferential to content, and to feel alive
(optical depth, highlights, fluid transitions). It works when there is a clear content-vs-
controls separation; it fails when applied to every surface, when it harms legibility, or
when a web knockoff pretends to be the native thing.

## Visual grammar
- **Content vs controls separation:** content is the base layer; Liquid Glass is the
  *floating control/navigation layer*. This separation is the whole concept.
- **Adaptive appearance:** the material responds to the content behind it and to light/dark;
  it isn't a fixed color.
- **Optical depth:** translucency + refraction + specular **highlights** on edges → a sense
  of real glass with thickness, not a flat blur.
- **Layered navigation:** bars, sidebars, and sheets read as glass panes above content.
- **Movement & shape transformation:** on-platform, elements can morph/flow fluidly during
  transitions; on web, keep motion subtle and cheap.
- **Legibility first:** the system preserves text contrast via adaptive vibrancy; a web
  approximation must *manually* guarantee it with tint/scrim.
- **Restraint:** glass on the control layer only; content surfaces stay solid/legible.

## Design tokens (web approximation)
- **Style-defining:** layered translucency, blur radius, saturation, edge/specular highlight,
  adaptive tint, subtle motion, layer shadow.
- **Product-dependent:** brand tint, content/background, type, density.

```css
/* Web *approximation* — not the native material. Guarantee contrast yourself. */
.lg-control {
  background: color-mix(in srgb, var(--lg-tint, #ffffff) 16%, transparent);
  backdrop-filter: blur(20px) saturate(1.6);
  -webkit-backdrop-filter: blur(20px) saturate(1.6);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 6px 24px rgba(0,0,0,.18);
  border-radius: 22px;
}
@supports not (backdrop-filter: blur(1px)) { .lg-control { background: var(--surface-solid); } }
@media (prefers-reduced-transparency: reduce) { .lg-control { background: var(--surface-solid); backdrop-filter: none; } }
@media (prefers-reduced-motion: reduce) { .lg-control { transition: none; } }
```

## Component translation
Apply to the **control layer**: tab/nav bars, toolbars, sidebars, floating action controls,
sheets/popovers, the now-playing or command bar. **Do not** apply to content surfaces,
tables, long text, or every card. On Apple platforms, use the framework material
(SwiftUI/UIKit) rather than reimplementing it.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand mode:** a striking glass nav over rich content
is great. **Product mode:** confine glass to the navigation/control chrome; keep dense
working content solid and legible. Never let the material compromise a task surface.

## When to use
Apple-platform apps wanting native feel (use the real material); web experiences that want an
Apple-inspired floating control layer over rich content; media/lifestyle/premium products.

## When NOT to use
On the web when the background is flat (nothing to refract), on content/data surfaces, on
low-end devices/large regions (blur cost), when text legibility can't be guaranteed, or when
the goal is a plain accessible utility. Don't force it on ordinary sites just to look
Apple-like.

## Anti-patterns
- **Glass on every surface** — Tell: content + controls all translucent. Why: destroys the
  content/controls separation that defines Liquid Glass; contrast chaos. Fix: glass on the
  floating layer only.
- **Excessive floating rounded containers** — Tell: a page of hovering glass pills. Why:
  slop, no hierarchy. Fix: one coherent control layer.
- **Illegible text** — Tell: light text over variable content. Why: no adaptive vibrancy on
  web. Fix: manual tint/scrim to hold the A1 contrast minimum.
- **"It's the same as native"** — Tell: claiming a CSS blur equals Liquid Glass. Why: false;
  lacks real refraction/adaptivity. Fix: call it *inspired-by*; use the framework material on
  Apple platforms.
- **Blur everything, all the time** — Tell: large animated blur regions. Why: performance.
  Fix: limit area, avoid animating blur, provide fallbacks.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
Style hotspots: `../style-router.md` §Accessibility hotspots.

On web you must *manually* guarantee text and
control contrast against the effective background (the native system does this for you).
Honor `prefers-reduced-transparency` (Apple: **Reduce Transparency**) and
`prefers-reduced-motion` (**Reduce Motion**) with solid, static fallbacks. Keep focus rings
visible over glass. Never encode meaning in translucency alone.

## Responsive
Reduce blur radius/area on mobile GPUs; keep the control layer legible over whatever scrolls
behind it; targets at the A7 house floor. Ensure the content-vs-controls separation still reads at every
size.

## Performance
Layered `backdrop-filter` + saturation + highlights is expensive, especially animated or
large. Limit to the control layer; avoid animating blur; provide `@supports`, reduced-
transparency, and reduced-motion fallbacks; test on low-end hardware.

## Implementation guidance
- **Apple platforms:** use the **native material** via SwiftUI/UIKit (the frameworks provide
  Liquid Glass, adaptivity, and accessibility handling). Don't hand-roll it.
- **Web:** treat it as an *approximation* — layered translucency, subtle specular highlight,
  a real background to refract, guaranteed contrast, and all three fallbacks. Encapsulate as
  a `.lg-control` token/variant used only on the control layer.

## Review checklist
- [ ] Clear content-vs-controls separation; glass only on the floating control layer.
- [ ] Text/control contrast guaranteed against the effective background (tint/scrim on web).
- [ ] Reduced-transparency, reduced-motion, and no-`backdrop-filter` fallbacks all present.
- [ ] On Apple platforms, native material used (not a reimplementation).
- [ ] No claim that a web approximation equals the native material.
- [ ] Blur area/cost controlled; focus visible; targets at the A7 house floor.

## Examples
- **Good/native:** an iOS app using the system material for its tab bar and sheets over
  photo content.
- **Good/web:** an Apple-inspired site with a single glass nav floating over a vivid hero,
  white text on a contrast-guaranteeing tint, solid fallback on Reduce Transparency.
- **Bad:** a web dashboard where every card and the content are all glass, thin text over
  changing data, labeled "Liquid Glass, identical to Apple."
