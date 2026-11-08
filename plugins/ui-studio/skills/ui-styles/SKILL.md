---
name: ui-styles
description: >-
  Applies a named visual style or a reasoned hybrid - minimalism, maximalism, brutalism /
  neo-brutalism, skeuomorphism, neumorphism / soft UI, glassmorphism, claymorphism, Apple-style
  liquid glass, bento grid, spatial / 3D UI - with a context classifier, design dials,
  brand-vs-product mode, per-style tokens, accessibility hotspots and review checklists. Use for
  "make this glassmorphic", "neumorphic settings page", "bento grid for the overview", "liquid
  glass nav", "brutalist portfolio", "60% minimalism, 25% bento", "which style fits this
  product?". Ignore "minimal API", "glass table (SQL)", "brutal error", "spatial database",
  "clay model". Not for choosing fonts and colours without a named style - use
  ui-visual-direction.
argument-hint: "<style name, hybrid or product to classify>"
---

# Styles: classify, route, apply

There is no single correct aesthetic. An enterprise admin console, a luxury brand site, a banking
form and a kids' learning app each need a different design. Choose the style for *this* product,
user and task, and be able to say why in one sentence. A requested style is honoured and adapted,
never silently swapped for a generic look.

Frame: the user-first-ux priority order and workflow (pointer in
`${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`). Tokens:
`${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`. Generated-look tells:
`${CLAUDE_PLUGIN_ROOT}/references/shared/ai-defaults.md`.

## 1. Classify the context (silently, first)

Infer from the request and the codebase; state assumptions where you had to guess.

- **Product type** — marketing site · SaaS app · admin/internal tool · enterprise ops platform ·
  dashboard · e-commerce · checkout · content/editorial · portfolio · mobile app · design system.
- **User type** — general public · first-time visitor · returning customer · trained operator ·
  domain expert · admin/manager/executive · accessibility-dependent · mobile-first.
- **Density** — low (spacious) · medium · high · expert-operational.
- **Visual expressiveness** — restrained · balanced · expressive · experimental.
- **Motion need** — none/minimal · functional · expressive · cinematic.
- **Trust need** — normal · high-trust · safety-critical.
- **Platform** — desktop web · responsive web · mobile web · iOS · Android · tablet ·
  cross-platform · spatial.
- **Mode per surface** — brand or product: `references/brand-vs-product.md`.

Then emit a short internal decision:

```
Mode: brand | product (per surface)   Dominant style: …   Supporting: … (or none)
Dials: variance _/10 · density _/10 · motion _/10 · depth _/10 · brand _/10 · trust-conservatism _/10
Primary risks: …
References to load: …
```

**Density and trust drive most mistakes.** High-density expert tools and high-trust or
safety-critical flows pull hard toward restraint, convention and legibility, not novelty.

## 2. Design dials

Plain-language overrides ("more premium", "increase density", "less rounded", "reduce motion")
map to these. Infer defaults from context; expose them only when useful.

- **Layout variance 1-10** — 1 rigid/conventional → 10 asymmetric/experimental.
- **Visual density 1-10** — 1 spacious → 10 expert-operational.
- **Motion intensity 0-10** — 0 none → 10 expressive system (a reduced-motion path always exists).
- **Visual depth 0-10** — elevation, layering, translucency, figure/ground.
- **Brand expression 1-10** — how loudly identity speaks.
- **Trust conservatism 1-10** — higher = more conventional, predictable, legible.

Defaults by mode: **product** → variance 2-4, density 6-9, motion 1-3, trust 6-9. **brand** →
variance 5-8, density 2-5, motion 3-6, brand 6-9. Starting points, not laws. Request-to-dial
translations: `references/brand-to-ui.md`.

## 3. Route to a style

| Signal | Lean toward | Avoid |
|---|---|---|
| Data-dense product, daily use, task focus | minimalism, Swiss, restrained system, bento for *overview* | maximalism, claymorphism, heavy glass |
| Marketing / identity / first impression | the brand's real personality + one distinctive move | generic dark-SaaS default |
| Playful / consumer / education / kids | claymorphism (as accent), warm maximalism | brutalism, cold minimalism |
| Editorial / opinionated / portfolio | brutalism, maximalism, editorial, Swiss | corporate glass |
| Tactile real-world metaphor (audio, tools) | skeuomorphism on the control that benefits | flat-everything |
| Apple-platform app, controls over content | liquid glass (control layer only) | glass on every surface |
| Overview of many unequal things | bento grid | equal card grid |
| Luxury / premium brand | restraint + type + space | loud gradients, clutter |
| True XR / visionOS / AR / VR | spatial UI (true) | pseudo-3D on an ordinary website |
| Nothing special signaled | confident minimalism **with identity** | "modern gradient SaaS" reflex |

If two styles tie, pick the one that serves the *primary task*, not the flashier one.
Profiles for every named style (including lightweight ones without a file: editorial, Swiss,
luxury, playful, corporate, material) and the hybrid rules: `references/style-router.md`.
Deep files, one per style — load only the one in use:

`references/styles/` · minimalism · maximalism · brutalism · skeuomorphism · neumorphism ·
glassmorphism · claymorphism · liquid-glass · bento-grid · spatial-ui

**One dominant style; combine only with a written reason** (one dominant + one supporting, with
a property-ownership map: `references/style-router.md` §Hybrids).

## 4. When NOT to use a style

- Operational software should not wear marketing aesthetics (`references/brand-vs-product.md`).
- Neumorphism and other low-contrast styles on forms and data entry → usability and
  accessibility risk.
- Heavy glass/blur on low-end devices or large regions → performance risk (effects budget in
  `visual-system.md`).
- True spatial-computing assumptions on an ordinary website → wrong model; produce a
  web-appropriate spatial *interpretation* unless real XR is requested.
- Any style that fights the content's density or the user's task.

## 5. Apply and check

1. Pre-design: context classified and assumptions stated; brand vs product decided per surface;
   existing stack, tokens and components inspected (extend, don't replace); what to preserve
   listed; requested style noted; dials set; the minimal set of references chosen.
2. Encode the style as tokens (radius, elevation, transparency, border, motion character are the
   style-defining ones: `../ui-design-system/references/token-architecture.md`), then build with
   `ui-visual-direction` and the stack skill.
3. Run the style file's own review checklist, its accessibility hotspots
   (`references/style-router.md` §Accessibility hotspots) and **style fidelity**: is the intended
   style actually achieved, not just claimed?
4. Critique with `ui-critique` (its scored audit includes style fidelity).
