# Preserving Laravel conventions while restyling (Blade · Livewire · Alpine · Bootstrap)

The priority adapter — Laravel powers a large share of admin/enterprise/institutional systems:
high-density product-mode work. **Server-rendered by default; respect
that.** Don't convert a Blade app into an SPA to restyle it.

## Detect what you're in

`composer.json` (Laravel), `resources/views/**.blade.php` (Blade), `app/Livewire/` or
`app/Http/Livewire/` + `wire:` attributes (Livewire), `x-data`/`x-on:` (Alpine),
`resources/css`/`tailwind.config.js` (Tailwind) vs Bootstrap/AdminLTE assets. Many admin panels use
**Bootstrap or AdminLTE**, not Tailwind — check before assuming utility classes.

## Preserve Laravel conventions (non-negotiable)

- **Blade structure** — layouts (`@extends`/`@section` or components `<x-...>`), partials, slots. Build
  reusable **Blade components** (`resources/views/components/`) instead of copy-pasting markup; this is
  the Blade-native way to a design system.
- **CSRF** — keep `@csrf` in every form; never strip it while restyling.
- **Validation & errors** — preserve `@error('field')`, `old('field')` repopulation, and the error bag.
  Style error states; don't remove the wiring. Associate errors for a11y (F5 and A15 in the user-first-ux skill).
- **Localization** — keep `{{ __('...') }}` / `@lang`; don't hardcode strings. Leave room for
  translated lengths and RTL (`dir` + logical CSS properties). → logical properties: L8 in `../../../references/shared/visual-system.md`.
- **Authorization** — keep `@can`/`@cannot`/policy gates around actions; **don't render actions the
  user can't perform** (aligns with the enterprise playbook in the user-first-ux skill (`domains/enterprise-dashboards.md`)).
- **Routes & named routes** — keep `route()` / `action` targets and method spoofing (`@method`).
- **Pagination** — Laravel's paginator renders its own views; customize the paginator view rather than
  replacing the mechanism; keep totals.

## Styling approach

- **Tailwind projects** — token mapping: `tokens-tailwind-bootstrap.md`.
- **Bootstrap / AdminLTE projects** — work *within* the grid and component classes; theme via Sass
  variables or CSS custom properties overriding Bootstrap's; don't bolt a parallel custom system on
  top. Restyle by adjusting variables and adding a thin layer, not by fighting the framework.
- **Assets** — Vite (`resources/js/app.js`, `@vite` directive) is the modern default; respect the
  existing build pipeline (Vite vs Mix).

## Interactivity: reach for the lightest tool

Server-rendered Blade + a sprinkle of **Alpine** handles most UI state (dropdowns, modals, tabs,
toggles) without a framework. **Livewire** handles dynamic server-driven components (live tables,
forms, filters) — restyle its Blade templates and preserve `wire:model`/`wire:click`/loading states
(`wire:loading`). Don't introduce React/Vue into a Blade+Livewire app to restyle it.

## The common task: admin/enterprise redesign

This is usually **product mode, high density** — apply the enterprise playbook and TB1-TB10 in the user-first-ux skill. Keep tables as tables (not cards), preserve density, add sorting/filtering/
bulk-actions within Livewire or server params, respect permissions. Livewire loading states map
naturally to skeleton/spinner patterns (the states matrix in the user-first-ux skill).

## Common failure modes

Stripping `@csrf`/validation wiring while restyling · hardcoding strings over `__()` · rendering
actions past `@can` · replacing the paginator · introducing an SPA framework to restyle server-rendered
views · assuming Tailwind when it's Bootstrap/AdminLTE · turning dense admin tables into cards.
