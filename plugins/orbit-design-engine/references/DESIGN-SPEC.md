# Orbit Design Engine — Host-theme-first design specification

## Absolute precedence

1. Existing system theme, design tokens, tenant/organization branding and theme switching.
2. Accessibility, contrast, user preferences and reduced-motion settings.
3. Product UX and business requirements.
4. Reference geometry, component composition, typography, timing, interaction and animation.

**Do not specify or copy any colours from screenshots, videos, this package, or sample implementations.** All existing project colour settings remain authoritative. Do not install a new palette, silently change brand colours, inject an alternate theme, or force light/dark mode.

## First action: inspect the existing theme

Before any styling, find the app's theme source (CSS custom properties, framework configuration, theme provider, design-system components, organization branding and stored user preferences). Identify existing semantic roles for:

- Page / canvas and elevated / subdued surfaces
- Primary, secondary and destructive actions and their on-content text
- Main text, muted text, border, input background, interactive focus
- Meaningful status/validation and chart series
- Overlay/scrim and light/dark/tenant variants

Map the roles to the actual **host** tokens; do not reassign theme token values. If a role does not exist, use an existing host-styled component or document the missing token instead of inventing a palette. Browser system colours may be used **only inside standalone demos without a host theme**.

## Recreate structure and motion, not a palette

- App shell: responsive sidebar, top context bar, consistent navigation active/hover/focus states.
- Dashboard: contextual heading, readable KPI cards, asymmetric charts/action queues, meaningful data labels.
- Lists and forms: consistent spacing, controlled density, accessible filters, sorting, validation, errors and loading states.
- Motion: intentional enter/exit/transform animation, continuity across routes, intermediate-frame verification and reduced-motion support.
- Layout suggestions (adapt to current app): expanded rail ~248px; compact rail ~72px; header 64–72px; page padding 24–32px desktop / 16px small screens; component spacing 16–20px.
- Type: prefer the current system's font and size scale; tune hierarchy, weights and wrapping from rendered layouts.
- Controls: minimum appropriate touch target; focus-visible; do not use colour alone to convey status or selected state.

## Invariants / review gates

- Existing colour palette is unchanged after installation and after applying skills.
- All components read the current theme source, including auth motion overlays, charts, toasts, skeletons and focus rings.
- Existing theme and user-selected variants still work; new UI elements respond to theme changes.
- No fixed HEX, RGB/HSL values, named reference palette, new brand variant or fallback theme is added.
- Motion and layout do not interfere with business logic, accessibility or performance.

See `THEME-INHERITANCE.md` for implementation guidance and QA tests.
