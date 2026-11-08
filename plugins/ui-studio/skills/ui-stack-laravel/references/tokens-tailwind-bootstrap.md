# Tokens into Tailwind v4 and Bootstrap 5

## Tailwind v4 (Laravel 12+ default via `@tailwindcss/vite`)

Tokens are CSS variables declared in `@theme`; each namespace generates utilities:

| Token namespace | Generates | Example |
|---|---|---|
| `--color-*` | `bg-*`, `text-*`, `border-*`, `fill-*` | `--color-brand-600` -> `bg-brand-600` |
| `--font-*` | `font-*` | `--font-display` -> `font-display` |
| `--text-*` | `text-*` sizes | `--text-lg: 1.25rem` |
| `--spacing` | the whole spacing scale (multiples) | `--spacing: 4px` keeps everything on the 4pt grid (L1) |
| `--radius-*` | `rounded-*` | `--radius-control` -> `rounded-control` |
| `--shadow-*` | `shadow-*` | keep 2-3 levels (E1) |
| `--breakpoint-*` | responsive variants | `--breakpoint-sm: 40rem` |

Rules:
- A token that references another token goes in `@theme inline { ... }` so utilities resolve
  the value, not the reference.
- To lock the palette to the design system, reset the namespace first: `--color-*: initial;`
  then declare only the system colours. Hardcoded colours then fail to compile instead of
  slipping in.
- Use `:root` (not `@theme`) for variables that should not create utilities.
- Arbitrary values (`w-[13px]`, `text-[#333]`) are a token leak. Acceptable only for one-off
  geometry that is not a design decision (e.g. `grid-cols-[auto_1fr]`) or when referencing a
  token: `rounded-[calc(var(--radius-control)-1px)]`.

Semantic layer (C1): name roles, not hues, for what components consume:

```css
@theme inline {
  --color-surface: var(--color-paper);
  --color-text: var(--color-ink);
  --color-text-muted: color-mix(in oklab, var(--color-ink) 65%, transparent);
  --color-primary: var(--color-brand-600);
  --color-danger: var(--color-danger-600);
}
```

Check contrast for every text/background token pair you define (quality floor) and again
for the dark set (C4).

## Bootstrap 5 (legacy projects)

Map the same tokens into Sass before Bootstrap is imported; never override compiled classes
with hex in views.

```scss
// resources/sass/_variables.scss  (imported before bootstrap)
$primary:   #1f5c4a;
$danger:    #b42318;
$body-color: #1c2421;
$body-bg:    #f7f8f6;

$font-family-sans-serif: "Instrument Sans", system-ui, sans-serif;
$border-radius: .5rem;

// 4pt grid: Bootstrap's default spacer map is already 0/4/8/16/24/48px
$spacer: 1rem;

// Visible focus (Bootstrap 5.3 focus-ring variables)
$focus-ring-width:   .25rem;
$focus-ring-opacity: .5;
```

```scss
// resources/sass/app.scss
@import "variables";
@import "bootstrap/scss/bootstrap";
```

- Runtime theming uses the generated CSS variables (`--bs-primary`, `--bs-body-bg`); dark mode
  uses `data-bs-theme="dark"` on `<html>` (Bootstrap 5.3+).
- Mapping table for migrations (Bootstrap -> Tailwind token):
  `$primary` -> `--color-primary`, `$body-color` -> `--color-text`, `$body-bg` ->
  `--color-surface`, `$border-radius` -> `--radius-control`, `$spacer * .25` -> `--spacing`.
- While both frameworks coexist, scope one of them (e.g. Tailwind `prefix(tw)` on the import)
  so utility names do not collide, and keep a single source for the token values.
