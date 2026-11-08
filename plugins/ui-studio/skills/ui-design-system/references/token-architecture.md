# Design Systems & Tokens

Translate visual direction into a **maintainable** system. Tokens turn taste into something a team can
apply consistently and change cheaply. When a project already has a system, **extract and extend it —
don't replace it casually.**

## Token layers (three tiers)

1. **Primitives (raw scales)** — the palette ramps, the type scale, the spacing scale, radii,
   durations. Named by *value* (`--blue-600`, `--space-4`, `--text-lg`). No component references these
   directly.
2. **Semantic tokens** — meaning-named, referencing primitives (`--color-primary`,
   `--surface-raised`, `--text-muted`, `--border`, `--focus-ring`, `--danger-fg`). **Components use
   these.** This layer is what makes theming and dark mode a token swap, not a rewrite.
3. **Component tokens** (optional) — when a component needs its own knobs (`--button-padding-x`,
   `--card-radius`), defined in terms of semantic/primitive tokens.

The discipline: components reference semantic tokens; semantic tokens reference primitives; nothing
hardcodes raw values. A hex or magic number in a component is a smell.

## What to tokenize

Color roles · type scale + weights + line-heights · spacing scale · radii · **elevation** (shadow
set) · **borders** · **transparency/blur** (for glass styles) · **motion** (durations, easings) ·
**state** (hover/active/disabled deltas) · **z-index** layers · breakpoints/container sizes. Theme
variants (light/dark/high-contrast) are the *same semantic names* with different primitive values.

## Which tokens are style-defining vs product-dependent

- **Style-defining** (change these to change the style): radius, elevation/shadow logic, transparency,
  border treatment, motion character, accent behavior.
- **Product-dependent** (set by brand/content/density regardless of style): the color *roles*, type
  families, spacing scale, breakpoints.

Knowing which is which lets you re-skin without breaking structure, and re-brand without breaking style.

## Components & variants

- **Variants over one-offs** — a `Button` with `variant` (primary/secondary/ghost/danger) and `size`,
  each state tokenized. Don't fork a new component to change a color.
- **Every component ships all states** — default/hover/focus/active/disabled/loading and, where
  relevant, error/selected. See the eight states in `../../../references/shared/quality-floor.md`.
- **Semantic naming & stable APIs** — name by role, keep props predictable, compose rather than
  duplicate. Deduplicate logic; a design system's value is that a fix in one place propagates.
- **Document usage** — when to use each component/variant and when not to.

## Theming & modes

Build light/dark/high-contrast on the same semantic layer. Verify each: elevated surfaces still
separate, shadows adapt, accents re-pass contrast, focus stays visible. `prefers-color-scheme` +
optional explicit toggle. See C4 in `../../../references/shared/visual-system.md`; contrast per the quality floor.

## Extending an existing system (do this first, before inventing)

1. **Find it** — token files, Tailwind/theme config, component library, CSS variables, existing
   patterns. Infer the scale behind the ad-hoc values: which spacing values recur, which type
   sizes, which colours map to which roles, what the radius/elevation logic is.
2. **Learn its conventions** — naming, scale, spacing rhythm, how variants are done.
3. **Extend, matching conventions** — add tokens/variants in the existing style; don't introduce a
   parallel competing system.
4. **Only propose replacement** when the current system is genuinely blocking, and then explicitly and
   incrementally — never a silent rewrite.

## Design decision memory

For substantial work, persist decisions so future sessions don't drift: visual direction, tokens,
component patterns, motion/a11y/density policy, prohibited patterns, and intentional exceptions.
Follow the project's existing convention if it has one; otherwise a small `.design/` note
(`DESIGN.md`, `TOKENS.md`, `DECISIONS.md`) is enough. Don't create these when an equivalent already
exists.

## Common AI failure modes

Hardcoded hex/magic numbers in components · one-off CSS instead of variants · duplicated component
logic · replacing an existing system instead of extending it · dark mode as naive inversion · tokens
with no semantic layer (components pointing straight at primitives) · undocumented z-index escalation.

## Systematic states and other stacks

- **State tokens**: derive hover / active / selected / disabled from the base token (e.g. a
  `color-mix` overlay) so states are systematic, not hand-tuned per component.
- **Elevation ladder**: a small numbered set (0-4) from one light source; never a per-element
  shadow.
- **High-contrast mode**: same semantic names, e.g. `@media (prefers-contrast: more)` strengthens
  `--border`.
- **Native stacks** (SwiftUI, Flutter, React Native): mirror the same semantic roles as a typed
  theme object; same three-layer discipline. Values come from `visual-system.md`.
