# Content & Microcopy (CM)

Copy is interface. Rule IDs use the `CM` prefix to avoid clashing with motion rules `M1-M2`.

- **CM1 Human meaning** - "Only 7 left in stock" beats "In stock: 7".
- **CM2 True** - urgency or scarcity only when it is real and computed. Fake timers and invented
  stock counts are banned (see `ethics-privacy.md`).
- **CM3 Plain language** - about reading grade 8, short sentences, active voice, key words first.
  Cut jargon.
- **CM4 One term per concept** across the whole product. Keep a glossary; do not mix
  "Client" / "Customer" / "Account" for one thing.
- **CM5 Outcome labels** - "Download invoice (PDF, 2 MB)". Links describe their destination;
  never "click here" or "read more" alone.
- **CM6 Scannable headings** that describe the content below them.
- **CM7 Specific numbers** - numerals and exact values ("3 days", not "a few days").
- **CM8 Tone** - friendly and respectful; calmer in serious or error situations. No jokes in
  errors about money, data or health.
- **CM9 Realistic content** - no lorem ipsum in deliverables. Use realistic content, including
  long names, missing data and edge cases.

## Worked example: stock copy

Compute the message from the real count; never hard-code urgency.

| Stock | Copy | Notes |
|---|---|---|
| 0 | "Out of stock. **Notify me** when it's back" (+ link to similar items) | Helpful next step, no dead end |
| 1-5 (real) | "Only 3 left" | True, computed scarcity is fine |
| Plenty (e.g. 250) | "In stock - ships in 1-2 days" | No urgency; the useful fact is delivery |

Thresholds are a product decision; state the one you chose.

## Error copy checklist

- Says what happened, in the user's words.
- Says how to fix it, specifically.
- Does not blame ("You entered an invalid...") or joke.
- Keeps any reference ID visible for support.
