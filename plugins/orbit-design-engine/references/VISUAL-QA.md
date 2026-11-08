# Visual and behaviour QA gate

## Captures
Reference and implementation screenshots should show the same route, viewport, theme and state. Save in `reference/screenshots/` (actual reference) and `qa/screenshots/` (implementation); name e.g. `dashboard-desktop-light.png`, `dashboard-mobile-menu.png`, `table-filtered.png`, `modal-open.png`. Never fabricate a reference screenshot.

## Priority rubric (score 0–4 for each)
| Category | Weight | Verify |
|---|---:|---|
| Overall composition | 25 | rail/header/grid/content proportions, vertical rhythm, whitespace |
| Component language | 20 | cards, tables, forms, buttons, badges, radii, borders |
| Typography and colour | 15 | hierarchy, scale, contrast, neutrals, semantic accents |
| Motion and interactions | 15 | timing, reveal, collapse, overlays, chart/queue transitions |
| Responsive/mobile | 10 | no overflow, menu/drawer, touch targets, table handling |
| Functional correctness | 10 | real routes and data, auth, safe mutations, reliable feedback |
| Accessibility | 5 | keyboard, focus, contrast, reduced motion, semantics |

Target >85/100 for a close approximation. Do not claim an observed percentage without screenshots and a test record. Do not obscure failed checks with a high aggregate score. Accessibility, permission and data integrity errors block completion regardless of score.

## Test matrix
- 1440×900 and 1024×768 desktop; 768×1024 tablet; 390×844 (optional 320×720) phone.
- Default + sidebar-collapsed + navigation-expanded + mobile drawer.
- Loading + empty + error + populated + filtered + success states.
- Light/dark if supported; accessible focus, keyboard tab cycle, ESC, reduced motion.
- Chart animation integrity, drag-and-drop and accessible fallback, responsive drawers/modals.
- No horizontal page overflow except deliberately contained large table; no clipping at 200% browser zoom.

## Iteration protocol
1. Screenshot baseline of target screen.
2. Compare with observed reference screenshot if available; compare with design spec otherwise.
3. Identify top three mismatches with evidence, not generic advice.
4. Fix and recapture; repeat at least twice for major redesigns where tools allow.
5. Report what was actually tested, screenshot paths, residual defects and the confidence of reference fidelity.

## Definition of Done
A visual redesign isn't complete until critical functions still work, states/motion exist, navigation has continuity, responsive views are usable, and differences are documented. If browsing isn't possible, do code-level QA and explicitly mark screenshot comparison unverified.

## Added v8 host-theme safety gate
Confirm that the app uses its unchanged existing theme across all updated routes and that every new control/overlay/chart responds to the host theme provider. **Do not use the reference palette as a matching criterion.** When computing visual similarity, exclude palette and prioritize geometry, hierarchy, type, responsiveness and motion timings.
