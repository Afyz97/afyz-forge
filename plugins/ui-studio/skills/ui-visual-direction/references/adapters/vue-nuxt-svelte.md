# Adapter: Vue · Nuxt · Svelte · SvelteKit

Shared posture: single-file components, scoped styling, and a reactivity model that already handles
most UI state — respect each framework's idioms, extend the existing component library, token-drive
styling.

## Vue / Nuxt

- **SFCs** (`<template>`/`<script setup>`/`<style scoped>`). Build reusable components with clear
  props/slots; compose over duplicate. `<style scoped>` for component styles; global tokens as CSS
  variables (or the UI lib's theme).
- **UI libraries** — Vuetify, PrimeVue, Naive, Element Plus, Nuxt UI. If one is present, **theme and
  extend it**, don't add a second. Match its component and variant conventions.
- **Nuxt** — file-based routing/layouts; SSR by default (respect it — don't force client-only to
  restyle); `useHead`/SEO meta for semantic/SEO structure on brand pages (`../public-websites.md`);
  `@nuxt/image` for sized, lazy media.
- **State/interactivity** — Vue reactivity + `v-model` cover most UI state; you rarely need extra deps.

## Svelte / SvelteKit

- **Components** (`.svelte`) with component-scoped `<style>` by default — styles don't leak, which
  makes token discipline easy via `:root` CSS variables. Reactivity is built-in and light.
- **SvelteKit** — file-based routing, SSR/SSG; `+page`/`+layout`; keep server rendering where it is.
  Enhanced forms (`use:enhance`) — preserve progressive enhancement and validation while restyling.
- **UI libraries** — Skeleton, shadcn-svelte, Flowbite-svelte, etc.; extend the one in use.

## Universal (both ecosystems)

- **Semantic HTML** and native elements first; ARIA only when needed. → the user-first-ux accessibility floor (`ui-accessibility` skill).
- **Token-driven CSS variables** for color roles, spacing, radius, elevation, motion — theming and dark
  mode become a variable swap. → `../../../ui-design-system/references/token-architecture.md`.
- **All interaction states** as variants; visible focus; designed loading/empty/error.
  → the states matrix in the user-first-ux skill (`states-feedback.md`).
- **Transitions** — Svelte has built-in `transition:`/`animate:`; Vue has `<Transition>`. Use
  transform/opacity, keep them purposeful, honor reduced motion. → M1 (`../../../../references/shared/visual-system.md`).
- **Performance** — sized/lazy images, subset fonts, code-split heavy components, no big libs for small
  needs. → the effects budget (`../../../../references/shared/visual-system.md`).

## Common failure modes

Adding a second UI library instead of theming the existing one · forcing client-only rendering to
restyle SSR pages · global unscoped styles instead of tokens + scoped styles · breaking form
enhancement/validation while restyling · duplicated components instead of props/slots variants.
