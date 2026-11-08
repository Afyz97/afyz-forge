# Adapters: Detecting & Respecting the Stack

Design decisions are portable; *implementation* must fit the project's actual stack. **Detect the
stack first, use what's there, and never swap frameworks to make a visual change.**

## Detect the stack

Look for the signals before writing code:

- **Manifests** — `package.json` (deps reveal React/Vue/Svelte/Next/Nuxt, Tailwind, component libs),
  `composer.json` (Laravel), `Gemfile`, `pubspec.yaml` (Flutter), `Package.swift` / `*.xcodeproj`
  (SwiftUI), `go.mod`.
- **Config** — `tailwind.config.*`, `postcss.config.*`, `vite.config.*`, `components.json` (shadcn),
  `.storybook/`, theme files.
- **Directory shape** — `resources/views/**.blade.php` (Blade), `app/Livewire/` or
  `app/Http/Livewire/` (Livewire), `src/components/`, `pages/`/`app/` (Next), `pages/`+`nuxt.config`
  (Nuxt), `src/routes/` (SvelteKit).
- **Existing design system** — token files, CSS variables, a component library, repeated class
  patterns. Extend it (`../../../ui-design-system/references/token-architecture.md`).

## Universal rules (all stacks)

- **Use the existing components and conventions** before adding anything new.
- **Semantic HTML first** — native `<button>`, `<a>`, `<label>`, `<table>`, landmarks; reach for ARIA
  only when native won't do. This is the cheapest accessibility win.
- **Token-driven styling** — CSS custom properties or the framework's theme system; no hardcoded hex /
  magic numbers in components. → `../../../ui-design-system/references/token-architecture.md`.
- **Don't add dependencies casually** — a charting/animation/icon library for one small need is a
  smell; check what's already installed.
- **Preserve** functionality, routes, auth, validation, i18n/RTL, and existing states. Inspect before
  editing.

## Pick the adapter

- **Laravel (Blade / Livewire / Alpine / Bootstrap / Tailwind)** → the `ui-stack-laravel` skill (`../../../ui-stack-laravel/references/preserve-conventions.md`) *(priority; the common
  admin/enterprise case)*.
- **React / Next.js (incl. shadcn/ui, Tailwind)** → the `ui-stack-next` skill.
- **Vue / Nuxt / Svelte / SvelteKit** → `vue-nuxt-svelte.md`.
- **React Native / Expo / SwiftUI / Flutter** → `native-mobile.md`.
- **Plain HTML / CSS / JS** — apply the references directly; CSS custom properties for tokens, Grid/
  Flex for layout, native elements, `prefers-*` media queries. No adapter file needed.
- **Bootstrap / AdminLTE** — see the `ui-stack-laravel` skill (`../../../ui-stack-laravel/references/preserve-conventions.md`) (common pairing) — work *within* the grid/utility system
  and component classes; theme via Sass variables/CSS vars; don't fight it with parallel custom CSS.
