# Brand-to-UI & Translating User Intent

Two related jobs: turning a brand/personality into a concrete design system, and turning vague user
requests ("make it more premium") into specific design-system changes.

## Brand → design system

Given a brand (or a personality target), derive the system rather than picking fashionable defaults:

1. **Name the personality** in a few adjectives (e.g. "precise, trustworthy, calm" vs "bold, playful,
   loud"). Everything downstream serves these.
2. **Type** — choose display and body faces that *embody* the adjectives (a precise grotesque vs a
   warm humanist vs an expressive serif). Set the scale and weights. See T1-T7 in `../../../references/shared/visual-system.md`.
3. **Color** — derive roles from brand hues; build perceptually-even ramps; set light/dark; verify
   contrast. The accent is spent sparingly. See C1-C6 in `../../../references/shared/visual-system.md`.
4. **Shape & depth** — radius, borders, and elevation carry a lot of personality: sharp corners read
   precise/serious; soft corners read friendly; heavy shadows read playful/tactile.
5. **Motion character** — calm/minimal for trust; springy/lively for playful. Tokenize it.
6. **Voice** — copy tone matching the adjectives, consistently. See the **ui-ux-copy** skill (user-first-ux plugin), if installed.
7. **One distinctive move** — the single memorable choice that makes it *this* brand and not a template.

Then encode it all as tokens (`../../ui-design-system/references/token-architecture.md`) so it's applied consistently.

## Referenced brands: extract principles, never clone

When a user says "like Stripe / Linear / Notion / Apple / Shopee / Airbnb / Material":

- **Extract the principles** that make it work (Stripe: clarity + generous type + restrained color +
  honest detail; Linear: speed, density, keyboard-first, tight motion; Apple: material depth +
  restraint + typographic confidence).
- **Apply them to this product's** content and brand. Don't reproduce their exact layout, copy, colors,
  or proprietary assets — that's a clone, often a legal/trust problem, and rarely fits.
- **"Like X without copying X"** = adopt X's *reasoning*, express it in *your* identity.

## User intent → dial/token translation

Map plain-language requests to concrete changes (see `../SKILL.md` §Design dials):

| User says | Translate to |
|---|---|
| "more premium / high-end / luxury" | more space, stronger type hierarchy, restrained palette, remove clutter/effects, refine detail; ↑trust-conservatism, ↓density | 
| "reduce the AI look" | kill default gradients/glass/rounded-everything, vary section rhythm, real content, one distinctive move; check AD1-AD10 in `../../../references/shared/ai-defaults.md` |
| "increase density" | ↑density dial: tighter spacing scale usage, compact mode, more per screen; see TB7 in the user-first-ux skill's `components.md`, if installed |
| "less rounded / sharper" | reduce radius token(s) toward 0–4px |
| "more editorial" | stronger type, asymmetry, generous measure, expressive scale; `style-router.md` editorial |
| "calmer / quieter" | ↓motion, ↓accent usage, ↓variance, more space |
| "bolder / louder / more delightful" | ↑variance, ↑brand expression, a distinctive move, considered motion — without breaking hierarchy |
| "more native / follow Apple HIG" | platform components/conventions, `styles/liquid-glass.md`, the user-first-ux mobile playbook |
| "make it more accessible" | run the user-first-ux accessibility floor + fixes (`ui-accessibility`); raise contrast; focus states; targets |
| "preserve current brand" | extract existing tokens, extend not replace; `../../ui-design-system/references/token-architecture.md` |

Confirm the interpretation implicitly by doing it and naming the change ("raised contrast, removed the
gradient, tightened the type scale") rather than asking a round of questions.

## Common AI failure modes

Fashionable defaults instead of brand-derived choices · cloning a referenced product's exact look ·
ignoring the stated personality · treating "premium" as "add effects" (it's usually *remove*) ·
changing everything when the user asked to preserve the brand.
