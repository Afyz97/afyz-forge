# Stack-specific adaptation

## Laravel Blade / AdminLTE 3 / Bootstrap
- Inspect `resources/views/layouts`, `resources/css` or public CSS, existing AdminLTE templates, Vite/Mix, route names, Blade components, JS packages and DataTables.
- Extend the existing layout and use **existing** Bootstrap/AdminLTE theme variables; do not overwrite their values or introduce a new palette. Prefer host-provided semantic roles over raw CSS settings. Scope any Orbit classes so they inherit the host theme.
- If existing AdminLTE sidebar is structurally adequate, restyle it rather than rebuilding navigation and breaking menu permissions.
- DataTables: retain server-side pagination, sort/filter/column behavior and accessibility; restyle wrappers, header, row actions, empty and loading states.
- Bootbox: preserve confirmation semantics, focus/ESC behavior and real server outcome.
- Keep CSRF, validation bag, session flash, route names, role conditions, localization, permission and print views intact.
- For Alpine/Blade transitions use CSS / Alpine first. If a developer opts into GSAP, respect bundling and prevent double-binding during live updates.

## Livewire / Inertia
- Avoid timeline reinit on every DOM morph; bind to persistent IDs and clean up listeners.
- Keep modal state and data consistency across network roundtrips; protect non-idempotent actions.

## React / TypeScript / Vite
- Prefer current router, component library and state/data layer; extract Shell, Card, Stat, Table, Modal, Chart and Status primitives.
- Use typed props and the existing React theme provider/component library tokens, not repeated inline styling or invented palettes.
- GSAP hooks/lifecycle cleanup on dependency or route change; no perpetual timeline listeners.
- Chart transitions must use real measurements and stable axes/series; provide tabular fallback.

## Across all stacks
- **Mandatory:** read `THEME-INHERITANCE.md` first, preserve existing theme/tenant settings, and ensure auth overlays, charts and motion inherit host semantic styles.
- Keep brand/logo sourced from existing settings or database where applicable. UI adapts to organization branding without changing all pages manually.
- Do not implement cinema or finance features just because the reference has them.
- Performance: bundle size, LCP, INP and scrolling matter as much as visual polish; ensure no CLS from animated widgets.
- Keep the existing accessible component library where possible and theme it rather than replacing working accessible primitives.
