---
name: ui-stack-laravel
description: >-
  Implements and themes UI in the Laravel stack: Laravel 13, PHP 8.4, Blade (*.blade.php),
  Livewire 4, Flux UI v2, Filament panels and themes, Alpine.js, Tailwind CSS v4 in
  resources/css/app.css, legacy Bootstrap 5 / SCSS, Fabric.js canvases and Vite. Use whenever
  the work touches a *.blade.php file, app/Livewire, app/Filament, a Flux component
  (<flux:button>, <flux:input>, <flux:field>), a Filament panel theme or ->colors(), wire:model,
  wire:ignore, x-data, or requests like "port this design to Blade/Livewire", "theme the
  Filament panel", "map our tokens to Tailwind or Bootstrap", "the Fabric canvas resets when
  Livewire updates", "add loading and error states to this Livewire form". Turns design tokens
  into Tailwind @theme / Flux accent / Bootstrap SCSS variables and covers every component
  state. Not for Next.js or React code (ui-stack-next) and not for choosing the visual direction
  itself (ui-visual-direction).
argument-hint: "<component, view or task>"
---

# Laravel stack: tokens, components, states

Frame: `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`. Floor and the eight
states: `${CLAUDE_PLUGIN_ROOT}/references/shared/quality-floor.md`. Before writing code, read the
project: `composer.json` (Livewire, Flux, Filament versions), `package.json`, `vite.config.js`,
`resources/css/app.css`, existing `resources/views/components/`. Reuse what exists (rung 2).
If the installed versions differ from those named here, the project wins; check that version's
docs before using an API.

## Which reference to load

| Task | Load |
|---|---|
| Tokens into Tailwind v4, or Bootstrap 5 legacy mapping | `references/tokens-tailwind-bootstrap.md` |
| Flux buttons, inputs, fields, accent theming | `references/flux-ui-v2.md` |
| Filament panel colours, custom theme, CSS hooks | `references/filament-theme.md` |
| Livewire 4 + Alpine patterns, loading/dirty states, Fabric.js or any canvas | `references/livewire-alpine.md` |
| Writing or reviewing Blade components | `references/blade-components.md` |
| Restyling an existing Blade/Livewire app without breaking it (@csrf, @error, `__()`, @can, paginator, Bootstrap/AdminLTE) | `references/preserve-conventions.md` |

## Non-negotiables in this stack

1. **Tokens live in one place.** Tailwind v4: the `@theme` block in `resources/css/app.css`
   (Filament panels: the panel's `theme.css`). Bootstrap legacy: `_variables.scss`. Views use
   utilities or `var(--...)`, never hex or arbitrary values like `p-[13px]`.
2. **Every interactive element has all eight states**, including `focus-visible` and a
   loading state wired to Livewire (`wire:loading`, or Flux's automatic button loading).
3. **Third-party DOM owners sit inside `wire:ignore`.** Fabric.js, chart libraries, date
   pickers, rich-text editors: Livewire must never morph their DOM. Initialise them from Alpine
   and talk to the component through `$wire`.
4. **Reduced motion.** Use `motion-safe:` for any animation utility; keep the global
   reduced-motion rule (M2) in `app.css`.
5. **Locale.** Money and dates are formatted, never concatenated: `Number::currency($amount,
   in: 'MYR', locale: 'ms_MY')` (needs the `intl` extension) or `Intl` on the client. Strings
   go through `__()` / `lang/` files; see the `ui-ux-copy` skill (user-first-ux plugin) for BM/EN rules.
6. **Semantic Blade first.** Real `<button>`, `<a>`, `<label for>`, headings in order. ARIA only
   where HTML cannot express it (A14-A15).

## Minimal token example (Tailwind v4 + Flux)

```css
/* resources/css/app.css */
@import "tailwindcss";
@import "../../vendor/livewire/flux/dist/flux.css";

@custom-variant dark (&:where(.dark, .dark *));

@theme {
  --font-sans: "Instrument Sans", ui-sans-serif, system-ui, sans-serif;

  --color-ink: #1c2421;
  --color-paper: #f7f8f6;
  --color-brand-600: #1f5c4a;
  --color-brand-500: #2a7a62;
  --color-danger-600: #b42318;

  /* Flux reads these three */
  --color-accent: var(--color-brand-600);
  --color-accent-content: var(--color-brand-600);
  --color-accent-foreground: var(--color-paper);

  --radius-control: 0.5rem;
}

@layer theme {
  .dark {
    --color-accent: var(--color-brand-500);
    --color-accent-content: var(--color-brand-500);
    --color-accent-foreground: var(--color-ink);
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

The hex values are placeholders: take the real ones from the approved visual plan.

## Review checklist for a Laravel view

- [ ] No hex, arbitrary Tailwind values or inline `style` in the view (the plugin hook warns on these)
- [ ] Flux / Blade components used before hand-rolled markup
- [ ] Every action shows loading; every form field shows its error (`<flux:error>` or `@error`)
- [ ] Canvas / third-party widgets wrapped in `wire:ignore`, with a text alternative
- [ ] Focus visible on custom controls; no `outline-none` without a `focus-visible:` replacement
- [ ] Strings localised; money and dates locale-formatted
- [ ] Works at 320px and 200% zoom; touch targets at the house floor (quality floor)
