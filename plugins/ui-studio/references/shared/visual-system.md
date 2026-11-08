# Visual System

Hierarchy, layout, space, typography, colour, elevation, icons and motion, and the **single
owner of every token value** in ui-studio. Visual work is priority 6: it serves the task, it never
overrides honesty, accessibility or usability.

Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

## Contents
1. Hierarchy (H) · 2. Layout (L) · 3. Social & compact patterns (S) · 4. Typography (T) ·
5. Colour (C) · 6. Elevation & surfaces (E) · 7. Icons (I) · 8. Motion (M) · 9. Effects budget ·
10. Token set

## Hierarchy (H)

- **H1** One primary metric or action per view. It gets the largest, boldest treatment
  (e.g. the account balance at display size).
- **H2** Labels sit above values: small, muted, medium weight or uppercase. Values are larger
  and higher contrast. No equal-weight "Label: value" rows.
- **H3** Put a trend next to its value using an icon, a sign, and colour, plus comparison
  context ("+32% vs last month" with an up arrow). Never colour alone.
- **H4** Put the identifier (account number, title) in a header band. Put secondary facts in a
  compact grid under a subtle divider.
- **H5** Squint test: blur the screen. The primary element must still be the first thing seen.
- **H6** 5-second test: a new user can say what the page is and what to do next.
- Build the order with the strongest tools first: size and weight, then space, then contrast,
  then position, then colour last.

## Layout (L)

- **L1** One spacing scale on a 4px grid (`--spacing: 4px`); every gap is a multiple of 4.
  Consistent gutters. Per component, few steps: the Ten Fixes count (≤ 3 rhythm steps + 1
  inset) is in the `visual-polish` skill.
- **L2** Content max-width about 1200-1440px for apps; prose 65-75ch.
- **L3** Mobile-first. Breakpoints where the content breaks, not by device. Primary actions in
  the thumb zone on mobile. Prefer intrinsic sizing (`min()`, `clamp()`, `minmax()`,
  `auto-fit`) and container queries (`@container`) for components that appear in slots of
  different widths.
- **L4** Flat navigation. Avoid nested dropdowns. Mobile bottom nav: 3-5 labelled items. Do not
  hide primary desktop nav in a hamburger.
- **L5** One dominant CTA per section, with a clear primary / secondary / tertiary /
  destructive hierarchy.
- **L6** Balanced layout. Do not overload headers or footers. No carousels for important
  content.
- **L7** Answer the wayfinding questions: *Where am I? What's here? Where can I go?*
- **L8** Mechanics: flexbox for one-dimensional runs, grid for two-dimensional structure; `gap`
  over margins; logical properties (`padding-inline`, `margin-block`) so RTL works. Avoid nested
  scroll areas; keep sticky bars slim and set `scroll-margin-top` on anchor targets.
- **L9** Test widths: 320-360, 390-430, 768, 1024-1280, 1440, 1920+, plus landscape with the
  keyboard open. Render them when browser tooling exists.

## Social & compact patterns (S)

- **S1** Collections of people: overlapping avatar stack with "+N", not wrapped grids.
- **S2** An avatar may overlap a cover image to save a row and anchor the profile.
- **S3** Overlapped elements stay accessible: an `aria-label` with names or a count, and a way
  to open the full list.
- **S4** Secondary actions (Share, More) sit inline with the content they act on.

## Typography (T)

- **T1** Modular scale, ratio 1.2-1.25, defined as rem tokens. Example: 12 / 14 / 16 / 20 /
  24 / 32 px (0.75 / 0.875 / 1 / 1.25 / 1.5 / 2 rem). No ad-hoc sizes. One step outside the
  scale is allowed: `--text-display` for the single hero datum of a view (Ten Fixes Rule 01:
  ≥ 3× body; starter 4.75rem / 76px).
- **T2** Balanced hierarchy steps. A 26px headline over an 11px subheadline fails. Use weight
  as well as size to show level; jump weights meaningfully (400 → 600), do not drift (400 → 500).
- **T3** Body text >= 16px for reading, >= 14px for dense UI. Nothing essential below 12px.
  Line height 1.4-1.6 body, 1.1-1.3 headings; the display hero may go to 1.
- **T4** Buttons use body-scale text. Primary and secondary buttons are the same size and
  differ only in emphasis.
- **T5** At most two type families. `font-display: swap` and system font fallbacks.
- **T6** Tabular numerals (`font-variant-numeric: tabular-nums`) for tables, prices and
  changing numbers. Right-align numbers in columns.
- **T7** Sentence case for UI. Never justify text. No long ALL CAPS text; short labels only,
  with added letter-spacing (this is the one caps role Ten Fixes Rule 04 allows).

Role tokens map onto the scale: caption = `--text-xs`, body = `--text-sm` (dense) or
`--text-md`, title = `--text-md` or `--text-lg`, hero = `--text-display`. At most four sizes per
component.

```css
:root {
  --text-xs: 0.75rem;  --text-sm: 0.875rem; --text-md: 1rem;
  --text-lg: 1.25rem;  --text-xl: 1.5rem;   --text-2xl: 2rem;
  --text-display: 4.75rem; /* one hero per view only */
  --leading-body: 1.5; --leading-heading: 1.2; --leading-display: 1;
  --weight-regular: 400; --weight-strong: 600; --weight-display: 300;
}
```

## Colour (C)

- **C1** Semantic tokens (`--color-primary`, `--color-danger`, `--color-surface`,
  `--color-text-muted`), never raw hex in components. Roles: surfaces (background, surface,
  raised, overlay), content (text, muted, subtle, on-accent), lines (border, strong, divider),
  interactive (primary, hover, active, focus-ring), status (success, warning, danger, info),
  each status with a `-bg` / `-fg` / `-border` triple so status surfaces stay legible.
- **C2** Roughly 60/30/10 neutral / secondary / accent. One accent, used for the primary action,
  the current selection or the single data encoding. Status colours are not accents.
- **C3** Never colour alone: owned by user-first-ux (accessibility). Minimum: pair colour with
  an icon, text or pattern.
- **C4** Dark mode is a designed palette, not an inversion. Avoid pure `#000` surfaces with
  pure white text; raised surfaces get lighter in dark mode, usually without heavy shadow.
  Re-check contrast for every pair, including each status colour on its own background.
- **C5** Status colours are consistent everywhere (success, warning, danger, info); routine
  states never wear alarm colours.
- **C6** Ramps: build perceptually even 50-950 ramps per hue (OKLCH or `color-mix`), not
  eyeballed hex. Charts: categorical sets that survive colour-blind simulation; sequential and
  diverging ramps that are perceptually uniform (not rainbow); the chart palette is a subset of
  the product palette.

## Elevation & surfaces (E)

- **E1** Elevation shows layering (card < dropdown < modal). Subtle shadows, few levels.
  Not a shadow on everything. Levels: flat content → raised → overlay → modal on a scrim, one
  token per level, one light source.
- **E2** Group with space and alignment first, a shared background second, a border last. One
  surface per semantic group (Ten Fixes Rule 08); a surface is a subtle background step and one
  radius token (`--radius-control` or the project's equivalent).

## Icons (I)

- **I1** One family, one stroke, one size per role: inline 16-20px, list 20-24px, one hero icon
  per view 48-64px. Icons use `currentColor`. Tokens: `--icon-inline`, `--icon-hero`,
  `--icon-stroke`. Rules and detection: Ten Fixes Rule 07 in `visual-polish`.

## Motion (M)

- **M1** Motion must explain something (where it came from, what changed), never just
  decorate. 150-300ms; ease-out to enter, ease-in to exit. Tokenise duration
  (`--dur-fast`, `--dur-base`) and easing (`--ease-out`, `--ease-in-out`) inside that range.
  Animate `transform` and `opacity` only.
- **M2** Reduced motion and flashing: owned by user-first-ux (accessibility). Minimum: respect
  `prefers-reduced-motion`; nothing flashes more than 3 times per second.

## Effects budget

`backdrop-filter: blur()` is costly on large regions and low-end devices: keep it to a few small
surfaces, never stacked, with a solid fallback. Keep a small elevation set instead of layered
shadows on every card. Never animate `width`, `height`, `top`, `left`, `box-shadow` or `filter`
in hot paths. Test effects on a mid-range phone.

## Token set

Every rule above maps to a small, closed set. A value not in the set is a violation.

| Area | Tokens |
|---|---|
| Spacing | `--spacing: 4px` (Tailwind v4) or `--space-1/2/3` = 4/8/12px per component, `--space-4/5` = 16/24px for page layout; `--inset` = one container padding |
| Type | `--text-xs` … `--text-2xl`, `--text-display`; `--leading-*`; `--weight-regular`, `--weight-strong`, `--weight-display`; one `--font-sans` (+ optional display family, T5) |
| Colour | role tokens (C1); `--fg`, `--fg-muted` (≥ the A1 recommended ratio on every surface), one `--accent`, status colours |
| Surfaces | `--surface`, `--card`, `--radius-control` (or `--radius`), `--track` for bars |
| Icons | `--icon-inline`, `--icon-hero`, `--icon-stroke` |
| Motion | `--dur-*`, `--ease-*` within M1 |
| State backgrounds | `--sky-*` or status tints (Ten Fixes Rule 10) |

Starter values for plain CSS / Blade: `skills/visual-polish/assets/tokens.css`. Its font
(`Inter`) and dark palette are placeholders: replace them from the approved visual plan (AD6).
Stack mapping: `ui-stack-laravel` (`tokens-tailwind-bootstrap.md`), `ui-stack-next`
(`tailwind-v4-theme.md`). Token tiers (primitive, semantic, component):
`skills/ui-design-system/references/token-architecture.md`.

Note: motion rule IDs here are `M1-M2` under visual-system; content rules in user-first-ux use
`CM1-CM9` to avoid a clash.
