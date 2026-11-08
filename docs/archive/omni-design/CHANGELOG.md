# Changelog

All notable changes to `omni-design`. Format loosely follows Keep a Changelog; versioning is SemVer.

## [1.0.0] — 2026-07-07

Initial release. One self-contained, progressively-disclosed design-intelligence skill.

### Added
- **SKILL.md** operational core — role, always-on operating rules, the working loop, a silent
  **context classifier**, the **style router** summary, **design dials**, anti-slop screen, **quality
  gates**, and the **conflict-resolution priority order**, plus a reference-loading map.
- **references/** (22) — foundations (design-foundations, typography, color, spacing-layout,
  responsive-design, accessibility, motion, states, performance, content-design), domains (forms,
  navigation, tables-data-density, enterprise-dashboards, public-websites, ecommerce, mobile-ui), and
  systems/translation (design-systems, brand-to-ui, reference-to-code, design-audit, anti-slop).
- **styles/** (11) — `style-router` (profiles for every named style + hybrid rules) and deep files for
  minimalism, maximalism, brutalism (+neo), skeuomorphism, neumorphism, glassmorphism, claymorphism,
  liquid-glass, bento-grid, spatial-ui.
- **workflows/** (8) — create, redesign, audit, polish, build-design-system, reference-to-code,
  mobile-design, enterprise-workflow-ui.
- **adapters/** (5) — overview (stack detection), laravel (priority), react-next, vue-nuxt-svelte,
  native-mobile.
- **checklists/** (6) — pre-design, implementation, accessibility, responsive, motion, release-gate.
- **tests/** (3) — scenarios, regression-prompts, trigger-tests.
- **README.md**, **SOURCES.md**, **CHANGELOG.md**.

### Design decisions
- Consolidated the brief's ~70-file tree where consolidation improved coherence and context-efficiency
  (documented in SOURCES.md §Structural decisions). No empty files or stubs.
- Accessibility encoded as a hard quality gate (WCAG 2.2-aligned), never overridden by style purity.
- Enterprise/admin and Laravel/Blade treated as first-class, high-density product-mode work.

### Known limitations
- No rendered browser validation performed in this package (checklists + audit stand in).
- Liquid Glass / spatial UI describe fast-moving Apple platform material — verify current HIG before
  native implementation.
- Upstream third-party design skills were not individually re-fetched this session; influence is via
  prior documented research + general knowledge (SOURCES.md is explicit about this).
