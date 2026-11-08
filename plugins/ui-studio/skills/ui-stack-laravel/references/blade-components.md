# Blade component conventions

## Location and naming

- Anonymous components in `resources/views/components/`, kebab-case files, used as
  `<x-stat-card>`. Group by domain with folders (`components/billing/invoice-row.blade.php` ->
  `<x-billing.invoice-row>`).
- One component per concept (CM4 applies to code too): do not create `card`, `panel` and `box`
  for the same thing. Before creating, search `resources/views/components/` and Flux.

## Props, attributes and classes

```blade
{{-- resources/views/components/button.blade.php --}}
@props([
    'variant' => 'primary',   // primary | secondary | danger
    'type' => 'button',
])

@php
$variants = [
    'primary'   => 'bg-primary text-white hover:bg-brand-500',
    'secondary' => 'bg-surface text-text ring-1 ring-text/15 hover:bg-text/5',
    'danger'    => 'bg-danger text-white hover:bg-danger/90',
];
@endphp

<button
    type="{{ $type }}"
    {{ $attributes->class([
        'inline-flex min-h-11 items-center justify-center gap-2 rounded-control px-4 text-sm font-medium',
        'transition-colors motion-reduce:transition-none',
        'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary',
        'disabled:cursor-not-allowed disabled:opacity-60',
        $variants[$variant],
    ]) }}
>
    {{ $slot }}
</button>
```

- `$attributes->class([...])` / `->merge()` so callers can add classes and `wire:` / `x-`
  attributes without breaking defaults.
- Defaults `type="button"` (avoids accidental submits).
- `min-h-11` meets the target house floor (quality floor). Focus is `focus-visible`, never removed.
- Only tokens in class lists; no hex, no arbitrary values.

## Documenting a component

Every shared component gets a doc block or a page following the Document template in
`ui-design-system` (variants, props, states, accessibility, do/don't, example).
