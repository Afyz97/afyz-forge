# Anti-patterns Agents Commonly Produce

Flag and fix on sight. Cite the related rule ID in reviews.

## Generic "AI template" look
- Purple/blue gradients, gradient heading text, emoji as icons.
- Everything centred; identical three-column feature grids with no reason.
- Cards inside cards (G3); a shadow on everything (E1).
**Fix:** hierarchy through space and type; one accent; icons only where they aid scanning.

## Labels & names
- Placeholder-only labels (F1).
- Icon-only buttons with no accessible name (B5).
- Tooltips holding essential info (hover is invisible on touch and to many AT users).

## Actions
- Disabled buttons with no explanation (B2).
- "Yes / No" / "OK / Cancel" confirmations (B4).

## Navigation & layout
- Walls of dropdowns in the nav (L4); carousels hiding key content (L6).
- Modals on page load (CL2); infinite scroll with a footer (TB6).

## Forms & errors
- Errors only in toasts (CL3); validation on every keystroke (F5); clearing forms on error (F6).

## Emphasis & colour
- Everything bold or highlighted (U8 Von Restorff misuse).
- Rainbow status colours (C5); meaning by colour only (C3).
- Tiny grey text on grey (A1); hover-only affordances on touch devices (NO1).

## Content
- Lorem ipsum, perfect-length demo data (CM9).
- No empty, loading or error states (ST).

## Motion
- Decorative motion that delays tasks (M1); ignoring reduced motion (M2).
