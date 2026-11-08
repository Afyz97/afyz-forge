# Accessibility (A) - WCAG 2.2 AA minimum

A non-negotiable baseline (priority 2). Automated tools are the floor, not the finish line.
This file is the single owner of every accessibility number in user-first-ux and ui-studio;
other skills point here. Criterion numbers and thresholds are WCAG 2.2. WCAG 2.1 audits are
upgraded: 2.2 adds 2.4.11, 2.5.7, 2.5.8 (AA) and 3.2.6, 3.3.7 (A), 3.3.8 (AA), and removes
4.1.1 Parsing.

## Perceivable

| Criterion | Requirement |
|---|---|
| 1.1.1 Non-text content (A) | Every image, icon and control has a text alternative; decoration uses `alt=""` |
| 1.3.1 Info and relationships (A) | Structure (headings, lists, tables, labels) is in the markup, not only in the look |
| 1.4.3 Contrast minimum (AA) | Text >= 4.5:1; large text (>= 24px, or >= 18.66px bold) >= 3:1 |
| 1.4.10 Reflow (AA) | Usable at 320 CSS px wide without two-way scrolling |
| 1.4.11 Non-text contrast (AA) | UI components, focus indicators and meaningful graphics >= 3:1 |

- **A1** Text contrast >= 4.5:1; large text (>= 24px, or >= 18.66px bold), UI components and
  focus indicators >= 3:1. Recommended: about **7:1** for small secondary text (muted greys look
  fine on a designer's monitor and fail in sunlight and on cheap screens). On gradients, test the
  lightest region behind light text.
- **A2** Alt text is meaningful, or `alt=""` for decoration. Video has captions.
- **A3** Content reflows at 320px width, works at 200% zoom and with text-spacing overrides.
  Never disable pinch-zoom (no `maximum-scale=1` / `user-scalable=no`).
- **A4** Nothing relies on colour alone (see C3 in `visual-system.md`).

## Operable

| Criterion | Requirement |
|---|---|
| 2.1.1 Keyboard (A) | Everything works from the keyboard |
| 2.1.2 No keyboard trap (A) | Focus can always leave a component |
| 2.4.3 Focus order (A) | Tab order follows meaning |
| 2.4.7 Focus visible (AA) | The focused element is always visibly marked |
| 2.4.11 Focus not obscured, minimum (AA, new in 2.2) | The focused element is not entirely hidden by sticky headers, footers or overlays |
| 2.5.7 Dragging movements (AA, new in 2.2) | Every drag action also works with a single pointer without dragging |
| 2.5.8 Target size, minimum (AA, new in 2.2) | Targets at least 24x24 CSS px, or enough spacing |

Target size note: some older checklists list 2.5.5 (44x44) as AA. In WCAG 2.1 and 2.2, 2.5.5
Target Size (Enhanced) is **AAA**. These plugins audit 24x24 as the AA requirement and keep 44x44
as the house floor.

- **A5** Everything works by keyboard in a logical order, with no traps.
- **A6** Focus is always visible and **not hidden** behind sticky headers or footers (2.4.11);
  ideally not hidden at all (2.4.12, AAA). Use `scroll-padding-top` for sticky headers. The
  indicator is >= 3:1; >= 2px thick is recommended.
- **A7** Touch targets: AA minimum **24x24px** (2.5.8; smaller only if a 24px circle around each
  target does not overlap its neighbours); house floor **44x44px** (Apple HIG 44pt, Material
  48dp). Dense layouts that go below the house floor name the trade-off.
- **A8** Drag actions have a single-pointer alternative (2.5.7).
- **A9** A skip link to main content. Time limits can be extended.

## Understandable

| Criterion | Requirement |
|---|---|
| 3.1.1 Language of page (A) | `lang` on `<html>` |
| 3.2.1 On focus (A) | Focusing something never triggers a change of context |
| 3.2.6 Consistent help (A, new in 2.2) | Help mechanisms appear in the same place across pages |
| 3.3.1 Error identification (A) | Errors are identified and described in text |
| 3.3.2 Labels or instructions (A) | Inputs have labels or instructions |
| 3.3.7 Redundant entry (A, new in 2.2) | Information already given in the same process is not asked again |
| 3.3.8 Accessible authentication, minimum (AA, new in 2.2) | No cognitive test to log in; paste and password managers allowed |

- **A10** `lang` set on `<html>` (and on inline foreign-language passages).
- **A11** Predictable navigation; help in a consistent location (3.2.6).
- **A12** Do not ask for the same information twice in a process (3.3.7 Redundant Entry).
- **A13** Accessible authentication: no cognitive puzzles; paste and password managers
  allowed (3.3.8).

## Robust

| Criterion | Requirement |
|---|---|
| 4.1.2 Name, role, value (A) | Every UI component exposes its name, role and current state |
| 4.1.3 Status messages (AA) | Status changes are announced without moving focus |
| (4.1.1 Parsing) | Removed in WCAG 2.2; do not report it |

- **A14** Semantic HTML first: `button`, `a`, `label`, `nav`, `main`, headings in order.
- **A15** ARIA only when HTML cannot express it. Names, roles and states are exposed
  (`aria-expanded`, `aria-selected`, `aria-sort`, `aria-current`, `aria-invalid` +
  `aria-describedby` for errors).
- **A16** Status messages use `aria-live` (`polite` for most, `assertive` only for urgent).

Also check media (captions, no autoplay without controls), time limits (can be extended) and
motion (M2 in `visual-system.md`: `prefers-reduced-motion`, nothing flashing more than 3 times
per second).

## Testing
- Keyboard-only pass: Tab, Shift+Tab, Enter, Space, arrows, Esc.
- Screen reader pass: NVDA (Windows) or VoiceOver (macOS/iOS). Check names, roles, headings
  list, live-region announcements.
- axe / Lighthouse as a floor.
- 320px width and 200% zoom pass; forced-colors / high contrast check.
- Full procedure and report format: the `ui-accessibility` skill (`../../ui-accessibility/`).
