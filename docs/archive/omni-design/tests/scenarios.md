# Test Scenarios & Expected Behaviours

Representative tasks the skill must handle well, each with the behavior that indicates success. Use
these to sanity-check the skill (manually, or as prompts for a baseline-vs-assisted comparison).

## S1 — Laravel enterprise admin redesign
Prompt: *"Redesign this program-management dashboard for org admins and program managers. Keep all
functionality."*
Expected: classifies **product mode, high density, high trust**; inspects Blade/stack and preserves
`@csrf`/validation/`@can`/routes/localization; keeps **tables as tables** with sorting/filtering/bulk
actions and density; **no marketing cards**; extends existing system; Bootstrap/AdminLTE vs Tailwind
detected. (`workflows/enterprise-workflow-ui.md`, `adapters/laravel.md`, `references/tables-data-density.md`)

## S2 — Premium public website
Prompt: *"Create a premium technology company landing page."*
Expected: **brand mode**; distinctive direction + **one distinctive move**; strong typography; controlled
motion; **no generic gradient-SaaS template**, no fake logos/metrics; mobile as its own context;
performance-aware. (`references/public-websites.md`, `styles/minimalism.md`/luxury profile)

## S3 — Mobile application
Prompt: *"Design a mobile event-management app."*
Expected: **not a compressed desktop**; thumb ergonomics, bottom nav, safe areas, platform conventions,
permission priming, Dynamic Type / font scaling. (`workflows/mobile-design.md`, `references/mobile-ui.md`)

## S4 — Liquid Glass, selectively
Prompt: *"Apply Apple-style Liquid Glass to this app."*
Expected: glass on the **control/nav layer only**, not content; contrast preserved via scrim; fallbacks
for unsupported/reduce-transparency/reduce-motion; **no blur-everything**; doesn't claim CSS = native.
(`styles/liquid-glass.md`)

## S5 — Accessibility audit
Prompt: *"Audit this checkout page."*
Expected: a11y issues **prioritized**; keyboard, focus, labels, contrast, target size, error recovery;
per-finding severity + evidence + fix; doesn't claim conformance from a glance. (`workflows/audit-ui.md`,
`references/accessibility.md`, `design-audit.md`)

## S6 — High-density expert dashboard
Prompt: *"Improve this operational monitoring dashboard used by experts."*
Expected: **preserves density**; scanability, coordinated views, compact controls; **no giant cards**;
widgets answer real questions; no fabricated data. (`references/enterprise-dashboards.md`)

## S7 — Brutalist campaign site
Prompt: *"Create a brutalist event campaign website."*
Expected: **intentional** brutalist grammar (not broken CSS); classic vs neo distinguished; accessibility
still met (real contrast, focus, responsive). (`styles/brutalism.md`)

## S8 — Add to an existing design system
Prompt: *"Add a new settings page."*
Expected: **inspects existing tokens/components and extends** them; matches conventions; doesn't invent a
parallel system; all states + a11y. (`references/design-systems.md`, `workflows/build-design-system.md`)

## S9 — E-commerce checkout, mobile conversion
Prompt: *"Redesign checkout for mobile conversion."*
Expected: trust, clarity, progress stepper, honest costs (no surprise fees), payment/failure states,
input preserved on error, **no dark patterns**, digital wallets, single-column. (`references/ecommerce.md`)

## S10 — Reference/image to code
Prompt: *"Build this screen from this screenshot."*
Expected: **extracts design grammar** → infers tokens → maps to the project stack → rebuilds responsively
with real content and full states; fixes (not copies) any defects; doesn't clone a real product.
(`workflows/reference-to-code.md`)

## S11 — "Make it less generic / reduce the AI look"
Expected: runs anti-slop; kills default gradients/glass/rounded-everything; introduces a real direction +
one distinctive move; varies section rhythm; replaces fake content. (`references/anti-slop.md`)

## S12 — Hybrid style request
Prompt: *"60% minimalism, 25% bento, 15% liquid glass."*
Expected: one **dominant** (minimalism) + bounded supporting roles; property-ownership map; contradiction
check; glass on control layer only; usability preserved. (`styles/style-router.md` §Hybrids)
