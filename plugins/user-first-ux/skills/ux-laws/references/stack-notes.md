# Stack notes: Laravel Blade + Livewire 4, Tailwind v4 or Bootstrap 5

Implementation of the build rules in `../SKILL.md`. Target sizes: A7 in
`../../user-first-ux/references/accessibility.md`.

- **Project design system first:** many apps wrap Bootstrap or Tailwind in their own classes
  and tokens (e.g. `btn-ds`, `card-ds`, `--space-*`). Read the layout and component CSS, use
  those classes and their sizes, and treat the utilities below as fallbacks. Check real sizes:
  a "small" button variant is often below the A7 house floor.
- **Primary CTA** `[Fitts][Von Restorff]`: Tailwind `inline-flex min-h-11 items-center px-5
  text-base font-semibold` with the brand fill; Bootstrap `btn btn-primary btn-lg`. Exactly one
  per view. Secondary: `border` / `btn-outline-secondary`. Tertiary: link style. Destructive
  goes in a separate "Danger zone" block, never next to Save. Mobile: `w-full sm:w-auto`.
- **Icon buttons** `[Fitts]`: `size-11` hit area (A7 house floor) even when the icon is `size-5`;
  `aria-label` plus a tooltip. Bootstrap: `btn p-2` with an explicit `min-width`/`min-height` at the A7 house floor.
- **Loading** `[Doherty]`: Livewire 4 adds `data-loading` to the element that triggered a
  request, and its docs prefer `data-loading` selectors over `wire:loading`. Button:
  `class="data-loading:opacity-60 data-loading:pointer-events-none"` with
  `<span class="in-data-loading:hidden">Save</span><span class="hidden in-data-loading:inline">Saving…</span>`
  (`in-`/`has-data-loading:` need Tailwind v4). `wire:submit` already disables submit buttons
  and makes inputs read-only while submitting. Keep the button width fixed. Whole sections
  that load slowly: `#[Lazy]` with a `placeholder()` skeleton matching the layout. Bootstrap or
  no Tailwind: `wire:loading.attr="disabled"` + `wire:target="save"`; `wire:loading.delay` avoids spinner flashes.
- **Validation** `[Postel]`: validate on blur with `wire:model.live.blur` (in Livewire 4 plain
  `.blur` only delays client-side sync and sends no request); never `.live` per keystroke.
  Normalise phone and IC before validating; `@error('field')` message directly under the
  input with `aria-invalid` and `aria-describedby`.
- **Sidebar nav** `[Miller][Serial Position][Pareto]`: `<nav aria-label="Main">` with labelled
  groups of ≤ 5–9 links (`<p class="px-3 text-xs font-medium uppercase text-gray-500">`);
  Dashboard first, Settings/Account last; active link via `request()->routeIs('x.*')` with
  `aria-current="page"`; rarely used groups in `<details>`.
- **Stepper** `[Zeigarnik][Goal-Gradient][Uniform Connectedness]`: `#[Url] public int $step = 1;`
  so refresh and Back keep the step; persist a draft per step. Render an `<ol>` of steps
  joined by a line (completed segments filled), `aria-current="step"` on the current one,
  text "Step 2 of 4 · 2 left", and a native `<progress value="2" max="4">`. Bootstrap:
  `.progress` + `role="progressbar"` with `aria-valuenow`. Last step = review + one button.
- **Form chunking** `[Chunking][Proximity][Common Region]`: `<fieldset>` + `<legend>` per
  section of ≤ 7 fields; `space-y-2` label→input, `space-y-6` between fields, `space-y-10`
  between sections (Bootstrap: `mb-1` / `mb-4` / `mb-5`); advanced fields in `<details>`.
- **Tables** `[Working Memory][Flow]`: filters, sort and page in the URL (`#[Url]`); bulk actions
  appear when rows are selected; numbers right-aligned with `tabular-nums`.
- **Modals** `[Flow]`: Livewire/Alpine modals only for short blocking decisions; never on page
  load; Esc closes and focus returns to the trigger.
