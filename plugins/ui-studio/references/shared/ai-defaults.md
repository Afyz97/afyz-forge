# Generated-looking defaults (AD)

These looks appear whatever the subject is, which is exactly what makes them read as
machine-made. None is forbidden: when the brief asks for one, deliver it (DP2). They are
flagged only when they fill an axis the brief left open.

| ID | Default | Exact tells |
|---|---|---|
| AD1 | Warm paper + serif + clay | cream ground around `#F4F1EA`, high-contrast serif display, terracotta accent around `#D97757` (Claude's own brand accent, so it signals "AI made this" on a client brief) |
| AD2 | Dark with one neon | near-black ground with a single acid-green or vermilion accent |
| AD3 | Newspaper cosplay | broadsheet grid, hairline rules, `border-radius: 0`, tight multi-column text |
| AD4 | SaaS card kit | identical rounded cards, one radius for every level of hierarchy, the same grey shadow `rgba(0,0,0,.1)` everywhere, decorative gradient washes |
| AD5 | Template chrome | letter-spaced ALL-CAPS eyebrow over every heading; meta joined with middle dots (`A · B · C`); `WORD — fragment` labels; a slightly tinted near-black (`#0B0B0B`, `#111`) where a chosen dark should be; monospace for small data labels; `→` tacked onto links and buttons |
| AD6 | Artifact-builder reflexes | centred-everything layouts, purple gradients, uniform rounded corners, Inter picked without a reason |
| AD7 | Headline tricks | one word in a headline singled out with italic, bold or colour; labels placed above content that does not need them |
| AD8 | Filler credibility | unsourced stat cards ("10k+ users", "99.9% uptime", "24/7"), invented testimonials or "as seen in" logos, charts of invented data |
| AD9 | Ornament reflexes | an icon in a tinted rounded square on every item, pill badges on everything, decorative blobs and mesh gradients, neon glow with no light logic, 3D tilt for flair |
| AD10 | Section monotony | every section is heading + subhead + 3 cards with the same padding; the hero formula repeated down the page |

## How to use the list

- A pattern is a default only when it is used without a reason: a gradient hero on a creative
  agency site or a bento grid on a real overview can be right. Report the reason-less use, not
  the shape.
- In a plan review (`ui-visual-direction`, pass 1), name any AD item the plan drifts into and
  either justify it from the brief or replace it.
- In a critique (`ui-critique`, distinctiveness step), cite the AD ID.
- Quick test: draft a plan for a similar prompt in your head. If you land on the same palette,
  type and layout, the plan is the default, not a choice.

## Overlap with the UX anti-pattern list

The user-first-ux skill's `anti-patterns.md` (if installed) covers the same family from the usability side (gradient heading text,
emoji icons, cards in cards, shadow on everything, everything centred). Cite the UX rule ID
when the problem hurts the task, and the AD ID when it only hurts identity.

Short uppercase **data labels** above values are allowed (H2, T7). AD5 targets the decorative
eyebrow repeated over every heading, not a muted label that helps scanning.
