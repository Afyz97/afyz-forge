# Style Router

Choose a design language deliberately; never default to a fashionable one. This file carries a
**compact profile for every style** plus hybrid rules. When you commit to a style that has its own
deep file, load that one too (listed below). Load only the styles you're actually using.

## How to route

1. Run the **context classifier** (SKILL.md): product, user, task, density, expressiveness, trust,
   platform. Classify each surface **brand vs product** — the single biggest treatment switch.
2. **Requested style?** Honor it. Assess fit, adapt it to the product, preserve usability. If it's a
   poor fit, implement it *and* flag the tension with a concrete alternative — don't silently swap it.
3. **No style requested?** Choose from the signals using the router table in SKILL.md and the profiles
   below. When two tie, serve the *primary task*, not the flashier option.
4. **Default when nothing is signaled:** confident **minimalism with identity** — not "modern gradient
   SaaS."

## Brand vs product (inherited by every style)

| | Brand mode | Product mode |
|---|---|---|
| Examples | landing, campaign, portfolio, editorial, pricing | dashboard, admin, SaaS shell, checkout, data tools |
| Goal | persuade/impress in one pass | complete tasks quickly, repeatedly |
| Density | generous, expressive | efficient, dense |
| Motion | can be a feature (restrained) | functional only |
| Novelty tolerance | high (one distinctive move) | low (convention aids speed) |

**Never apply marketing aesthetics to operational software.** Expressive styles (maximalism, clay,
brutalism, skeuomorphism) may go strong in brand mode but drop to **accents** in product mode — apply
them to identity moments (empty states, onboarding, marketing surfaces) and keep working surfaces
(tables, forms) calm and legible. Non-negotiables hold in both modes: contrast, visible focus,
keyboard, real content, reduced motion, clear hierarchy.

---

## Style profiles

Each: **intent · fits · misfits · signature properties · risks · AI failure modes.** Styles marked
**[deep file]** have a dedicated file — load it when you commit.

### Minimalism **[deep file: styles/minimalism.md]**
Intent: reduction to essentials; hierarchy through space and type. Fits: content/products where focus
and calm matter, most product UI, luxury. Misfits: when it hides needed function or density.
Properties: generous space, restrained palette, strong type, few borders, subtle depth. Risks: false
minimalism (empty, low-contrast gray text, hidden affordances). AI fails: whitespace with no
hierarchy; light-gray text; removed focus; generic sameness. **Minimalism must still have identity.**

### Maximalism **[deep file: styles/maximalism.md]**
Intent: controlled abundance; expressive layering. Fits: campaigns, culture, fashion, music, editorial,
creative portfolios. Misfits: most product UI (accents only). Properties: dense layering, expressive
type, pattern, rich color, asymmetry, strong rhythm. Risks: clutter, unreadable type, competing focal
points. AI fails: random noise mistaken for maximalism; no hierarchy; motion overload.

### Brutalism / Neo-brutalism **[deep file: styles/brutalism.md]**
Intent: raw, direct, exposed structure, typographic force. Fits: editorial, counter-culture, events,
opinionated brands, dev tools. Misfits: high-trust/safety-critical, dense ops. Properties: hard
contrast, unconventional grids, heavy type, visible structure; **neo-brutalism** adds thick borders,
hard offset shadows, flat bold colors (a distinct, more decorative dialect — don't conflate). Risks:
"raw" used to excuse broken/inaccessible. AI fails: unfinished CSS passed off as brutalism; contrast
too low; no responsive behavior.

### Skeuomorphism **[deep file: styles/skeuomorphism.md]**
Intent: real-world metaphor and tactile affordance. Fits: audio/music, tools, controls, creative apps,
nostalgia. Misfits: information-dense UI, flat product systems. Properties: material texture
(restrained), layered shadow/highlight, realistic pressed states. Risks: ornament as noise, text over
texture, slow rendering. AI fails: decorative fake realism with no functional metaphor; inconsistent
lighting. Best applied to the *one control that benefits*, not everything.

### Neumorphism (soft UI) **[deep file: styles/neumorphism.md]**
Intent: same-surface extrusion; soft embossed/debossed forms. Fits: small showcases, a few controls,
calm consumer accents. Misfits: forms, data entry, anything needing clear state — **accessibility
risk**. Properties: paired light+dark shadow on one surface color, consistent light source. Risks:
invisible controls, low contrast, ambiguous pressed state, "everything looks disabled." AI fails: full
app in neumorphism; unreadable forms; no focus. **Use as an accent; contrast overrides purity.**

### Glassmorphism **[deep file: styles/glassmorphism.md]**
Intent: translucent frosted layers over content, depth via material. Fits: overlays, nav, a hero layer
over rich backgrounds. Misfits: dense tables, critical forms, low-end devices. Properties: `backdrop-
filter: blur`, translucency + tint, defined edge, layering. Risks: text contrast over variable
backgrounds, blur-everything, performance. AI fails: glass on every surface; unreadable text; no
fallback. Distinct from Liquid Glass (a platform material) and plain opacity.

### Claymorphism **[deep file: styles/claymorphism.md]**
Intent: soft inflated 3D mass; friendly, playful. Fits: playful/consumer brands, education, kids,
illustration-led, onboarding. Misfits: serious/dense/professional tools. Properties: chunky rounded
forms, soft inner+outer shadow, pastel palette. Risks: everything a toy, low density, unusable forms,
low contrast. AI fails: clay on every SaaS component; childish tone in wrong domain.

### Liquid Glass **[deep file: styles/liquid-glass.md]**
Intent: Apple's adaptive material for the **controls/navigation layer floating above content**. Fits:
Apple-platform apps, nav/overlays/floating controls. Misfits: content wallpaper, dense data, web
clones claiming parity. Properties: dynamic refractive material, adaptive vibrancy, respects Reduce
Transparency/Motion. Risks: readability, performance, over-application. AI fails: `backdrop-filter` on
every card called "Liquid Glass"; claiming CSS = native; blur everywhere.

### Bento grid **[deep file: styles/bento-grid.md]**
Intent: modular composition of **unequal** tiles by content priority. Fits: overviews, feature
showcases, dashboards' summary zone, product highlights. Misfits: reading flows, equal-weight lists,
"dashboardifying" ordinary pages. Properties: variable spans, clear hierarchy across tiles, rhythm.
Risks: every tile equal (defeats the point), decorative bento with no info logic. AI fails: equal card
grid called bento; borders everywhere; no priority.

### Spatial UI **[deep file: styles/spatial-ui.md]**
Intent: depth, distance, and anchoring for spatial computing (visionOS/AR/VR) — or a restrained
depth-cue interpretation on 2D. Fits: true XR requests; subtle depth on web. Misfits: applying true
spatial assumptions to an ordinary website. Properties: windows/volumes, depth/scale, gaze+pinch,
comfort. Risks: motion sickness, discoverability, targets at distance. AI fails: pseudo-3D tilt on a
normal site; assuming XR input on the web.

---

## Styles without a dedicated file (execute from these profiles)

- **Editorial** — magazine logic: strong typographic hierarchy, generous measure, grid + intentional
  asymmetry, imagery as content. Fits content/brand; product only for reading surfaces. Type carries
  it (`../../ui-visual-direction/references/typography-structure-motion.md`).
- **Swiss / International typographic** — grid discipline, sans type, objective clarity, lots of
  structure. Excellent for dense product UI and data; reads precise and trustworthy.
- **Industrial** — utilitarian, high-density, functional; mono/technical type, muted palette, tight
  grids. Suits ops tools, dev tools, hardware/technical products. Close cousin of Swiss + brutalist
  restraint.
- **Luxury / Premium** — restraint, space, refined type, sparse color, impeccable detail. "Premium"
  is usually *subtraction* — remove clutter and effects, perfect the spacing and type. Not gradients
  and glow.
- **Playful** — warm color, rounded shapes, lively (restrained) motion, friendly copy. Consumer,
  education, social. Overlaps claymorphism; keep hierarchy and usability.
- **Corporate / Institutional** — conventional, trustworthy, predictable; conservative type/color,
  clear structure. Right for finance, government, healthcare, B2B — high trust-conservatism dial.
- **Retro / Futuristic** — era-specific or forward-looking motifs; use only when the brand genuinely
  calls for it; keep them as a considered direction, not a costume over broken foundations.
- **Material-inspired** — Google Material conventions (elevation, motion, components). Natural on
  Android and Material-based systems; adopt its component logic, don't cargo-cult its shadows.
- **Apple HIG-aligned** — native Apple conventions, SF type/symbols, standard components, Liquid Glass
  for the control layer. See `styles/liquid-glass.md` and the mobile playbook in the user-first-ux skill (`domains/mobile-ui.md`), if installed.

For any of these, still ground in `../../../references/shared/visual-system.md` and the a11y floor
(`../../../references/shared/quality-floor.md`).

---

## Hybrids (combine only with a written reason)

Default to **one** style. A single coherent style executed well beats a blend almost every time.
Combine only when a specific need justifies it (e.g. a data product needing minimalist clarity on
working surfaces but a bento overview).

**The dominant/supporting rule** — exactly one dominant + one supporting, never two co-equal:

1. **Dominant** owns layout, type, color, density, default surfaces.
2. **Supporting** contributes a *bounded* property set (only structure, or only an accent material, or
   only motion character).
3. **Property-ownership map** — write down which properties come from which language so they can't
   contradict (e.g. "grid + type from minimal; radius + shadow from clay").
4. **Contradiction check** — the two must not fight over one property (can't be brutalist-hard and
   claymorphic-soft on the same surface).
5. **Hierarchy and usability survive** — if not, cut the blend.

**Tend to work:** minimalism (dominant) + bento (structure) · brutalist structure (dominant) + minimal
interaction (supporting) · skeuomorphic affordance (supporting) inside restrained modern UI · glass
material (supporting) on a spatial/depth model (dominant, control layer only) · clay accent + otherwise
restrained.

**Usually fail:** neumorphism + anything hard-edged/high-contrast · glass + maximalism (blur+density =
mud) · brutalism + claymorphism (hard vs soft contradiction) · two "material" styles at once (glass +
clay + neumorphism — pick one material logic) · anything demanding one surface be both dense and airy.

**Procedure:** name the need one style can't meet → pick dominant + supporting → write the ownership
map → run the contradiction check → prototype one screen → if it reads as two designs bolted together,
revert to one language.

## Accessibility hotspots (where each style tends to fail)

Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

- **Neumorphism** — control affordance and state contrast; pressed vs unpressed ambiguity;
  "everything looks disabled." Contrast overrides purity; often better as an accent only.
- **Glassmorphism / Liquid Glass** — text over variable/blurred backgrounds; add a
  contrast-guaranteeing tint/scrim; fallback for `backdrop-filter` and Reduce Transparency.
- **Minimalism** — low-contrast light-gray text; focus removed "for cleanliness"; hidden
  affordances.
- **Maximalism** — text over busy imagery; motion overload; reduced-motion path essential.
- **Brutalism** — "raw" can still be *too low* contrast (pure red on black); verify real ratios.
- **Claymorphism** — soft pastel low contrast; tiny text on inflated shapes.
- **Skeuomorphism** — text over textures; decorative realism reducing legibility.
- **Bento grid** — reading/focus order across a 2-D grid; sane keyboard traversal.
- **Spatial UI** — comfort, target size at distance, gaze/pinch affordance, motion sickness.

```css
@media (prefers-reduced-transparency: reduce) {
  .glass { background: var(--surface-solid); backdrop-filter: none; }
}
@media (prefers-contrast: more) {
  :root { --border: color-mix(in oklab, currentColor 40%, transparent); }
}
@supports not (backdrop-filter: blur(1px)) {
  .glass { background: var(--surface-solid); }
}
```
