# E-commerce

Spans both modes: discovery/browse leans brand; cart/checkout is pure product. The whole funnel
optimizes for **finding the right product and completing purchase with trust** — conversion **without
dark patterns**.

## Discovery & browse

- **Product cards** — image (consistent aspect ratio), name, price (clear, with sale price honestly
  shown), and just enough meta to decide. Don't overload; the card's job is to earn a click.
- **Category & search** — fast, forgiving search (typo tolerance, synonyms); **faceted filters**
  (price, size, brand, rating) with visible removable chips and a clear-all; sort options that match
  how people shop. Filter/sort state survives navigation and back.
- **Listing performance** — image-heavy grids need correct sizing, lazy-loading below the fold, and
  no layout shift. See FP4-FP5 in `../states-feedback.md`.

## Product detail page (PDP)

- **Gallery** — multiple real images, zoom, consistent crops; show the product truthfully.
- **Decision info in priority order** — name, price, key variant selection, availability, primary CTA
  above the fold; details, specs, reviews below.
- **Variants** — selecting size/color updates price, image, and availability; disable/mark
  unavailable combinations clearly (not color-only). Never let a user add an out-of-stock variant.
- **Trust on the page** — honest reviews, return/shipping info near the CTA, security cues where they
  reassure. Real content only — no fake review counts.

## Cart

- **Always visible state** — item count, running total, clear line items with thumbnail, quantity
  edit, and remove. Show costs honestly *before* checkout (no surprise fees at the last step — that's
  a dark pattern and it kills trust).
- **Guest vs authenticated** — offer guest checkout; don't force account creation to buy. Persist the
  cart across sessions where possible.

## Checkout (the highest-stakes product surface)

- **Minimize steps and fields** — every field is friction; ask only what's needed; `autocomplete` and
  correct input types everywhere (F4 in `../components.md`). Address autofill, card-type detection.
- **Show progress** — a clear stepper (cart → details → payment → confirm) so users know where they
  are and what's left.
- **Payment states** — design processing, success, and *failure/decline* explicitly; on failure,
  preserve everything entered and explain the next step. Never clear the form.
- **Costs transparent** — taxes, shipping, and fees shown before the final click; totals update live.
- **Confirmation** — clear order confirmation with what happens next (email, shipping, tracking).
- **Errors preserve state** — validation inline; a failed payment doesn't lose the address/cart.

## No dark patterns (both ethical and effective long-term)

Avoid: hidden fees revealed late · pre-checked add-ons/insurance · fake scarcity/countdowns ("2 left!"
when untrue) · confirmshaming ("No thanks, I hate saving money") · forced account creation · obstructed
cancellation. These convert once and lose trust — and increasingly violate law. Persuade with clarity,
real value, and honest urgency only.

## Accessibility & mobile

Mobile checkout is where most revenue and most abandonment happen — design it as the primary case:
big targets, single-column, sticky pay button, minimal typing, digital wallets. Full a11y floor
applies: labels, focus, contrast, non-color status, keyboard (`../accessibility.md`, `../components.md` section 2,
`mobile-ui.md`).

## Common AI failure modes

Surprise fees at the last step · pre-checked extras · fake scarcity/urgency · forced signup · cart
that clears on error · out-of-stock variants addable · color-only availability · desktop checkout
crammed onto mobile · fake reviews/ratings.
