# Reference-to-Code & Image-to-Code

Turning a reference (screenshot, mockup, live site, or a design image you generate) into a real,
responsive, maintainable implementation — **extracting the design grammar**, not brittle pixel-tracing.

## The principle

A reference shows *one state, at one width, with placeholder content*. Copying it pixel-for-pixel
gives a fragile, non-responsive, content-fragile result. Instead, **reverse-engineer the system** that
produced it, then rebuild that system in the target stack.

## Extraction procedure

1. **Read the design grammar first** — before any code, identify:
   - the **grid/layout** logic (columns, container width, alignment, asymmetry);
   - the **type system** (families, the scale ratio, weights, hierarchy);
   - the **spacing rhythm** (the base unit, the repeating gaps);
   - the **color roles** (surfaces, text, accent — as roles, not just hexes);
   - **radius, elevation, borders** treatment;
   - the **visual rhythm** (how sections differ, where emphasis lands);
   - the **style** it belongs to (route via `../../ui-styles/references/style-router.md`).
2. **Infer tokens** from the grammar (spacing scale, type scale, color roles) — see
   `../../ui-design-system/references/token-architecture.md`. Build the token layer *first*, then components.
3. **Map to the target framework** — use the project's stack and existing components; don't import the
   reference's framework or a new dependency to match a look. See `adapters/`.
4. **Rebuild responsively** — the reference is one width; design the other contexts yourself
   (L3 and L9 (`../../../references/shared/visual-system.md`)). Reflow, reprioritize, and rethink nav — don't just scale the desktop shot.
5. **Use real content** — replace lorem/placeholder with realistic content; layouts that only work
   with perfect placeholder text are broken. Design the long-text, empty, and error cases.
6. **Add the missing states** — the reference shows default; you owe hover/focus/active/disabled/
   loading/empty/error. See the states matrix in the user-first-ux skill (`states-feedback.md`).

## Don't blindly copy unsuitable behavior

A reference may itself be flawed — low contrast, tiny targets, color-only status, a dark pattern, a
non-responsive layout. Extract what's good; **fix what's broken** rather than faithfully reproducing
defects. If the user wants an exact clone of something inaccessible, implement it *and* flag the
issue with the fix.

## When you generate the reference image yourself

If you produce a design image to work from, treat it as a *direction*, not a spec: it may contain
impossible layouts or inconsistent detail. Extract the grammar, resolve inconsistencies with the
foundations, and implement to a real, accessible, responsive bar.

## Legal & honesty

Don't reproduce a specific company's proprietary layout, copy, imagery, or brand assets to clone their
product. Extract general design principles and express them in this product's identity — see
`../../ui-styles/references/brand-to-ui.md` §Referenced brands.

## Common AI failure modes

Pixel-tracing one width · hardcoded values instead of an inferred token system · placeholder content
that hides broken layouts · no responsive rethink · missing interaction states · faithfully copying a
reference's accessibility defects · importing the reference's framework/deps · cloning a real product.
