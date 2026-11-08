---
name: ui-accessibility
description: >-
  Runs a WCAG 2.2 AA accessibility audit of a page, component, file or URL: colour contrast,
  keyboard access and focus order, visible and unobscured focus, target size, form labels and
  error messages, ARIA names, roles and states, screen-reader output, reflow at 320px and 200%
  zoom, reduced motion, drag alternatives and accessible authentication. Use for "is this
  accessible?", "a11y audit", "WCAG check", "check the contrast", "keyboard navigation",
  "screen reader", "focus trap in the modal", "aria-label", "accessibility compliance before
  launch". Outputs findings grouped by perceivable / operable / understandable / robust with
  success-criterion numbers and severity. Not for a general usability review - use
  user-first-ux.
argument-hint: "<path or url>"
---

# Accessibility audit (WCAG 2.2 AA)

The standard is **WCAG 2.2 Level AA**. WCAG 2.1 audits are upgraded: 2.2 adds 2.4.11, 2.5.7,
2.5.8 (AA) and 3.2.6, 3.3.7 (A), 3.3.8 (AA), and removes 4.1.1 Parsing. Accessibility is
priority 2 in the `user-first-ux` skill (`../user-first-ux/SKILL.md`), which also defines the
severity scale.

## Load

- Criteria and the house rules A1-A16: `../user-first-ux/references/accessibility.md`
- How to test, in what order, with which tools: `references/testing.md`
- Report format: `references/template.md`

## Procedure

1. **Scope**: pages, components and states in scope; which ones you can render.
2. **Contrast and keyboard first.** They are the most common failures and block the most
   people. Measure every text/background pair you can (state the ratio and the requirement).
3. **Automated pass** (axe / Lighthouse through Playwright when available). It finds only
   around 30% of problems; never stop there.
4. **Manual passes**: keyboard-only, zoom and reflow, screen-reader reasoning from the
   markup (names, roles, states, live regions, heading order), motion, forms and errors.
5. **Rank** by who is blocked and from what; Critical first.
6. **Report** with criterion numbers. Anything you could not check here (real screen reader,
   real device) is reported as **not verified**, never as passed.

For a URL or running app, the `a11y-auditor` agent can do the browser passes (keyboard, focus,
contrast, 200% zoom) read-only and return findings.

## Common failures to look for first

Low contrast; inputs without labels; things that only work with a mouse; images without
alternatives; focus traps or lost focus in modals; no landmarks; media that autoplays without
controls; time limits that cannot be extended; focus hidden under sticky headers; tiny targets;
drag-only interactions; login puzzles that block password managers.

## Connectors

A design tool lets you check colours, sizes, targets and annotations in the spec; a project
tracker takes one ticket per finding with severity and criterion, linked to a remediation epic
(connector roles: the **ui-studio** connectors reference, if installed; otherwise use what is
connected and never claim a connector was used when it was not).
