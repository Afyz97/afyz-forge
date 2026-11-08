# Brand Mode vs Product Mode (shared)

The single most important context switch in this suite. Every style skill inherits it.
The same visual style is applied *differently* depending on whether the surface is
**brand/marketing** or **product/application**.

## The distinction

| | Brand mode | Product mode |
|---|---|---|
| Examples | landing pages, campaigns, portfolios, editorial, event sites, pricing/marketing | dashboards, admin panels, SaaS app shells, e-commerce workflows, data-heavy tools, internal apps |
| Primary goal | persuade, impress, communicate identity in one pass | let a returning user complete tasks quickly and repeatedly |
| Viewing pattern | scanned once, often on the way in | used daily, for long sessions |
| Density | generous, expressive | efficient, information-dense |
| Motion | can be a feature (with restraint) | functional only — feedback and continuity |
| Novelty tolerance | high — one distinctive move is good | low — surprise is a cost; convention aids speed |
| Success metric | comprehension + emotion + conversion | task completion, error rate, state recognition |

## The rule

**Do not apply marketing-page aesthetics to operational software.** A neumorphic hero on a
portfolio can be beautiful; neumorphic inputs on a data-entry screen are an accessibility
and usability failure. A maximalist campaign can layer texture; a maximalist trading
dashboard is noise.

When a style is expressive by nature (maximalism, claymorphism, brutalism, skeuomorphism),
**brand mode may permit stronger expression; product mode dials it to accents** — apply the
style to identity moments (empty states, onboarding, marketing surfaces) and keep the
working surfaces (tables, forms, dense lists) calm, legible, and conventional.

## How to decide per surface

Ask, for each surface:
1. Is this seen once or used repeatedly?
2. Does the user have a task in progress here?
3. How much information must be legible at a glance?
4. Is recognition (of state, of controls) speed-critical?

More "used repeatedly / task in progress / high density / recognition-critical" → push
toward product-mode restraint even inside a brand-heavy product.

## Mixed products

Most real products contain both. A SaaS marketing site (brand) plus the app (product); a
store's homepage (brand) plus checkout (product). Keep a shared token foundation so they
feel related, but let expression and density differ. The `ui-styles` skill
must classify each surface before choosing treatment.

## Non-negotiables that hold in BOTH modes

- Accessible contrast and visible focus.
- Keyboard operability.
- Real content and honest data (no fake metrics/testimonials).
- Reduced-motion support.
- Clear hierarchy.
