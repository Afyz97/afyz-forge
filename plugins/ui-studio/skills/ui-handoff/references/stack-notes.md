# Stack-aware implementation notes

Add the matching block to the spec. Details and code live in the stack skills.

## Laravel (ui-stack-laravel)

- Tokens: where each new token goes (`@theme` in `resources/css/app.css`, Flux
  `--color-accent*`, Filament `->colors()` or panel `theme.css`, Bootstrap `_variables.scss`).
- Components: which Flux component or existing `<x-...>` Blade component each element maps to;
  anything new is a Blade component in `resources/views/components/`.
- Livewire: which properties bind with `wire:model.blur` vs `.live.debounce`; which actions
  need `wire:loading` / `wire:target`; which regions need `wire:ignore` (canvas, charts,
  editors, Fabric.js).
- Filament: resource/table columns, badges with icon + text, number formatting.
- Strings: keys in `lang/en` and `lang/ms`.

## Next.js (ui-stack-next)

- Tokens: semantic variables in `app/globals.css` (`@theme inline`).
- Server vs client: which components need `"use client"` and why; everything else stays a
  server component.
- Primitives: which Radix primitive each overlay or composite widget uses; initial-focus and
  return-focus targets.
- States: `loading.tsx` / `error.tsx` per route; `useFormStatus` / `useActionState` for forms.
- Icons: lucide names, decorative vs labelled.
- Strings: keys in `messages/en.json` and `messages/ms.json`.
