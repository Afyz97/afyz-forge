---
name: ui-critique
description: >-
  Gives structured design feedback on an existing screen, mockup, screenshot, Figma frame, URL
  or UI file (*.blade.php, *.tsx, *.html): first impression, usability, visual hierarchy,
  consistency, an accessibility spot-check and distinctiveness (does it look generic or
  AI-made?), with findings ranked by severity and concrete fixes. Use for "review this
  design/screen/page", "what's wrong with this UI?", "critique my mockup", "feedback on this
  dashboard", "does this look AI-generated?", "why does this feel off?", "rate this landing
  page", or after a build as the self-critique pass. Also a 100-point scored audit and style
  fidelity for named styles. Not for usability or WCAG reviews - use user-first-ux.
argument-hint: "<path, url or screenshot>"
---

# Design critique

Input: a file, URL, screenshot, Figma link or description. If nothing is provided, ask for it.
Also establish: what it is and who it is for, the stage (early exploration, refinement, final),
and any requested focus ("only the navigation"). For a URL or local app, render it (Playwright
when available) and look at it at desktop and 375px widths. For a large review, the
`ui-critic` agent can run this framework read-only in parallel.

Shared: severity `${CLAUDE_PLUGIN_ROOT}/references/shared/severity.md`; defaults
`${CLAUDE_PLUGIN_ROOT}/references/shared/ai-defaults.md`; visual rules
`${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`. Usability laws (N, NO, G, U) and UX
anti-patterns: the **user-first-ux** skill and its `ux-laws` skill, if installed. Scored
100-point audit, certainty classes and style fidelity: `references/scored-audit.md`.

## Framework (in this order)

1. **First two seconds.** What grabs attention first, and should it? What is the gut reaction?
   Is the purpose obvious without reading? (H5 squint test, H6 5-second test)
2. **Usability.** Can the user finish the main task? Is the way around clear? Do interactive
   things look interactive? Any steps that could go? (N1-N10, NO1-NO6, U1-U17)
3. **Hierarchy.** Does the eye travel in a sensible order, and is emphasis where it belongs?
   Is whitespace pulling its weight? Do type sizes and weights create levels? (H1-H4, T1-T7, G1-G5)
4. **Consistency.** Is the design system respected? Do spacing, colour and type stay uniform
   across the screen? Do look-alike elements also act alike? (N4, G2, C5)
5. **Accessibility spot-check.** Contrast, target size, readability, alt text. Anything serious
   goes to the `ui-accessibility` skill (user-first-ux plugin) for a full audit.
6. **Distinctiveness.** Does it fall into any AD1-AD10 default on an axis the brief left open?
   Is the boldness spent on one element (DP3), or spread everywhere? Does structure encode
   meaning (DP4)? Is motion earned (DP5)?

## How to write feedback

- Be precise: "The 'Export' button competes with the primary 'Pay now'", not "it's confusing".
- Give the reason, tied to a rule ID or a user need.
- Offer a concrete alternative, not just the problem.
- Say what works and should be kept.
- Match the stage: early work gets direction, final work gets polish notes.
- Separate what you observed from what you infer (DP7).

## Output

Fill `references/template.md`. Severity from the shared scale; rank by user impact. End with
the top three changes.

## Connectors

With a design tool connected you can open the frames and compare them with the system's
tokens and components; feedback tools let you test findings against real tickets (`${CLAUDE_PLUGIN_ROOT}/references/shared/connectors.md`).
