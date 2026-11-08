# Quality floor

The minimum every build meets. Meet it without announcing it; report it in the checklist.

Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

That covers responsive reflow (320px, 200% zoom), visible and unobscured focus, reduced motion,
text and non-text contrast and the touch-target house floor. The house floor for targets is the
one stated by user-first-ux (A7); ui-studio builds to it.

| Area | Floor | Source |
|---|---|---|
| Colour | A deliberate, harmonious palette; meaning never by colour alone | C1-C6 in `visual-system.md` |
| Tokens | Every value from the token set | `visual-system.md` §Token set |

## Tokens over values

Specs and code reference tokens (`spacing-md`, `--color-accent`), never raw values (`16px`,
`#2d8b8b`). Raw values appear only where the token is defined.

## The eight states

Every interactive component specifies: **default, hover, active, focus, disabled, loading,
error, empty**. The longer state list (read-only, permission denied, offline, skeleton,
0/1/many items, content stress) is owned by user-first-ux (`states-feedback.md`, section 1).
