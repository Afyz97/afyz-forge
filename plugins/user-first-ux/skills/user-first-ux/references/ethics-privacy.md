# Ethics, Trust & Privacy (EP)

Priority 1. Nothing here is traded for conversion, "engagement" or aesthetics. If a request
asks for one of these patterns, decline that part, explain the user harm in one line, and
offer an honest alternative.

## Banned dark patterns (EP1)

| Pattern | Looks like | Honest alternative |
|---|---|---|
| Confirmshaming | "No thanks, I don't like saving money" | "No thanks" |
| Roach motel | Signup in 1 click, cancel by phone only | Cancel in the same place, same effort |
| Fake urgency / scarcity | Resetting countdowns, invented "12 people viewing" | Real, computed deadlines and stock only |
| Pre-checked opt-ins | Marketing box ticked by default | Unticked, clearly labelled |
| Hidden costs | Fees appear at the last checkout step | Total incl. fees and tax shown early |
| Sneak into basket | Add-ons added automatically | Offer, never add without action |
| Forced continuity | Trial silently becomes paid | Reminder before charge; easy cancel |
| Disguised ads | Ads styled as content or buttons | Clearly labelled "Ad" / "Sponsored" |
| Trick questions | Double negatives ("Uncheck to not opt out") | One plain positive statement |
| Nagging | Repeated prompts after "No" | Respect the answer; ask again rarely, if ever |
| Share-by-default privacy | Public profile / data sharing on by default | Private by default |

## Rules

- **EP2** Cancelling or deleting is as easy as signing up (same channel, similar steps).
- **EP3** Show the total price early, including fees and tax.
- **EP4 Privacy by default** - collect the minimum, explain why, granular consent, data
  export and deletion findable. Follow applicable law (e.g. Malaysia PDPA 2010 as amended,
  GDPR where relevant).
- **EP5 Security UX** - session timeouts warn in advance and offer an extension. MFA is
  offered with recovery paths. Never show full sensitive identifiers: mask IC and card numbers
  (e.g. `******-**-1234`, `**** 4242`).
- **EP6 AI features** - label AI-generated content, show sources or confidence where
  possible, let users edit, undo or opt out.
- **EP7 Truthful nudges** - defaults, anchors, progress and urgency are true: a "was" price is a
  real previous price, a head start is a step really done, a recommendation has a reason.

## Delete-account flow (reference pattern)

1. Entry in Settings > Account, as findable as signup.
2. Plain consequence statement: what is deleted, what is kept (e.g. invoices for legal
   reasons) and for how long, whether it can be undone (grace period if any).
3. Offer data export before deleting.
4. Re-authenticate if needed (no puzzles; password manager friendly).
5. Buttons: "Delete my account" / "Keep my account". No guilt copy, no "Are you sure you want
   to abandon us?".
6. Confirmation screen and email stating what happened and the grace-period restore path.
