# Principles

Core principles written as rules an agent applies, not trivia to cite. The Laws of UX and Gestalt
laws are owned by the `ux-laws` skill; this file keeps their IDs.

## 1. Nielsen's 10 heuristics, as agent rules

| ID | Heuristic | Agent rule |
|---|---|---|
| N1 | Visibility of system status | Every action gets feedback within 100ms. Show where the user is: active nav, breadcrumbs, "Step 2 of 4". |
| N2 | Match the real world | Use the user's words, not database or developer terms ("Staff ID", not `user_ref_no`). Use natural ordering. |
| N3 | User control & freedom | Offer undo, cancel, back, and edit after submit. The browser Back button must never lose work or break state. |
| N4 | Consistency & standards | Same word, icon and position for the same thing everywhere. Follow platform conventions (Jakob's Law). |
| N5 | Error prevention | Prevent errors with constraints, sensible defaults, and accepting the formats people actually type. |
| N6 | Recognition over recall | Show options, recent items and previous values. Never make users remember data between screens. |
| N7 | Flexibility & efficiency | Shortcuts for experts (keyboard shortcuts, bulk actions, saved filters) without cluttering the UI for novices. |
| N8 | Aesthetic & minimalist design | Every element must earn its place. Remove what does not support the task. |
| N9 | Help users recover from errors | Plain-language messages: what happened, why, and exactly how to fix it. |
| N10 | Help & documentation | Contextual help at the point of need, findable in a consistent place. |

## 2. Norman's interaction design

- **NO1 Affordances & signifiers** - clickable things look clickable without hover. Text links
  are distinguishable without colour alone (underline, weight, icon).
- **NO2 Mapping** - controls sit next to what they affect, in a natural layout.
- **NO3 Feedback** - every action has an immediate, visible result.
- **NO4 Constraints** - make invalid actions impossible rather than warning afterwards
  (date pickers that block past dates for bookings, quantity steppers with min/max).
- **NO5 Conceptual model** - the UI reflects how users think the system works, not how the
  database is structured.
- **NO6 Gulfs of execution & evaluation** - make it obvious *what I can do* and *what just
  happened*.

## 3. Gestalt (how people group what they see)

G1, G2, G3 and G5 are owned by the `ux-laws` skill; the IDs stay for review tables.

| ID | Law | Owner entry |
|---|---|---|
| G1 | Proximity | `../../ux-laws/references/laws-perception.md` (Law of Proximity) |
| G2 | Similarity | `../../ux-laws/references/laws-perception.md` (Law of Similarity) |
| G3 | Common region (no cards in cards) | `../../ux-laws/references/laws-perception.md` (Law of Common Region) |
| G5 | Figure/ground & Praegnanz | `../../ux-laws/references/laws-perception.md` (Law of Prägnanz) |

- **G4 Continuity & alignment** - align to a shared grid. Every misalignment reads as meaning.

## 4. Laws of UX

Rules for all 30 laws live in the `ux-laws` skill (`../../ux-laws/references/laws-*.md`). U-IDs map
to its entries:

| ID | Law | Owner file |
|---|---|---|
| U1 | Fitts's Law | `laws-interaction.md` |
| U2 | Hick's Law | `laws-cognition.md` |
| U3 | Miller / Chunking | `laws-cognition.md` |
| U4 | Jakob's Law | `laws-behaviour.md` |
| U5 | Tesler's Law | `laws-cognition.md` |
| U6 | Doherty Threshold | `laws-interaction.md` |
| U7 | Postel's Law | `laws-interaction.md` |
| U8 | Von Restorff | `laws-perception.md` |
| U9 | Serial position | `laws-perception.md` |
| U10 | Peak-end rule | `laws-behaviour.md` |
| U11 | Goal-gradient | `laws-behaviour.md` |
| U12 | Zeigarnik effect | `laws-behaviour.md` |
| U13 | Aesthetic-usability effect | `laws-perception.md` |
| U14 | Pareto (80/20) | `laws-cognition.md` |
| U15 | Occam's razor | `laws-cognition.md` |
| U16 | Cognitive load | `laws-cognition.md` |
| U17 | Selective attention / banner blindness | `laws-cognition.md` |

## Applying them

- Cite the rule ID in review tables (e.g. `N9`, `U8`) so fixes are traceable.
- When two rules pull apart, fall back to the priority order in `SKILL.md` and name the
  trade-off.
