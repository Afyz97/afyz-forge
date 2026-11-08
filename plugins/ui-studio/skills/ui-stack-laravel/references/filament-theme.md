# Filament (v5 docs) theming

Check the installed major in `composer.json`; v4 and v5 share this theming model.

## 1. Colours first (no custom CSS needed)

```php
// app/Providers/Filament/AdminPanelProvider.php
use Filament\Support\Colors\Color;

public function panel(Panel $panel): Panel
{
    return $panel
        ->colors([
            'primary' => '#1f5c4a',          // hex, or a Color:: palette such as Color::Emerald
            'danger'  => Color::Rose,
            'success' => Color::Emerald,
            'warning' => Color::Amber,
            'gray'    => Color::Stone,
        ])
        ->font('Instrument Sans');
}
```

Filament generates the full shade ramp from one value. Check text contrast for `primary`
buttons in both light and dark mode after changing it.

## 2. Custom theme (when colours are not enough)

```bash
php artisan make:filament-theme admin
```

This creates `resources/css/filament/admin/theme.css`:

```css
@import "tailwindcss";
@source '../../../../app/Filament/**/*';
@source '../../../../resources/views/filament/**/*';

/* add your own sources if panel pages render your Blade/Livewire components */
@source '../../../../resources/views/components/**/*';
@source '../../../../app/Livewire/**/*';

/* panel-scoped token overrides */
@theme {
  --radius-control: 0.375rem;
}

/* targeted tweaks via Filament's CSS hook classes */
.fi-btn { border-radius: var(--radius-control); }
.fi-ta-text { font-variant-numeric: tabular-nums; } /* T6 for table numbers */
```

Then add `'resources/css/filament/admin/theme.css'` to the `input` array in
`vite.config.js`, register it with `->viteTheme('resources/css/filament/admin/theme.css')`,
and run `npm run build`.

## Rules

- Prefer `->colors()` and panel options over CSS. Use `fi-*` hook classes only for targeted
  tweaks; never restyle Filament internals by deep selectors (they change between versions).
- Keep one token source: if the public site uses `resources/css/app.css` tokens, import the
  shared token file into the panel theme rather than redefining values.
- Tables: numbers right-aligned with tabular numerals (TB2, T6); status badges with icon + text,
  never colour alone (C3).
