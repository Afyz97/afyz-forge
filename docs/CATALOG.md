# Skill Catalog

> **Status 2026-11.** The omni-design and ultimate-design-suite skills listed below the current
> catalog are historical (merged and removed; see `MIGRATION.md` for where each one went).

## Current catalog

| Plugin | Skills (model-invoked) | Commands |
|---|---|---|
| user-first-ux | user-first-ux, ux-laws, ui-accessibility, ui-ux-copy, ui-research | ui-a11y, ui-copy |
| ui-studio | ui-visual-direction, ui-styles, visual-polish, ui-design-system, ui-critique, ui-handoff, ui-stack-laravel, ui-stack-next, ui-theming, ui-canvas-art | ui-plan, ui-build, ui-system, ui-theme, polish-audit, polish-fix, polish-new |
| orbit-design-engine | 26 `orbit-ui-*` skills | — |
| system-design | system-design, distributed-patterns, system-design-review | system-design-interview |
| session-orchestrator | session-orchestrator | — |

## Historical catalog (pre-2026-11)

For each skill: purpose, example triggers, example non-triggers, dependencies, references,
status. Aliases are for discovery only — once triggered, the correct design model applies.

Status legend: **stable** = complete SKILL.md, ready to use; formal subagent trigger-eval
pending (see EVALUATION-REPORT.md).

This repo ships **two plugins** in the `ai-skills` marketplace. Install whichever fits:

| Plugin | Path | Skills | Style |
|---|---|---|---|
| `omni-design` | `plugins/omni-design/` | 1 (self-contained) | one comprehensive adaptive skill |
| `ultimate-design-suite` | `plugins/ultimate-design-suite/` | 15 + `_shared` | modular router + specialists |

They're two architectures of the same capability; enabling both means two design routers may
trigger on one request (harmless, but redundant). See `.ai/agents/architecture.md`.

---

## Plugin: omni-design

### omni-design — adaptive design intelligence (one package) · stable
- **Purpose:** classify product/user/task context and adapt aesthetic + density to fit — a context
  classifier, style router, design dials, WCAG-2.2 accessibility gate, reason-based anti-slop, a
  100-point audit, and framework adapters (Laravel/Blade prioritized). Covers create, redesign,
  audit, polish, design systems, reference-to-code, enterprise/admin, dashboards, e-commerce, mobile.
- **Triggers:** "design/build/redesign this page/dashboard/admin/landing/checkout/component/mobile
  screen," "make it better / less generic / more premium / more accessible," "audit this UI," "clean
  up this AI UI," "build a design system," "convert this screenshot to code," any named style.
- **Non-triggers:** backend, API, database, non-UI; "minimal API," "glass table (SQL)," "brutal
  error," "spatial database," "clay model."
- **Self-contained** — no external dependencies; internal `references/ styles/ workflows/ adapters/
  checklists/ tests/`. Install: `/plugin install omni-design@ai-skills`.

---

## Plugin: ultimate-design-suite

Skills live under `plugins/ultimate-design-suite/skills/`; shared references under
`…/skills/_shared/`. Install: `/plugin install ultimate-design-suite@ai-skills`.

## Core

### ultimate-design — orchestrator & router · stable
- **Purpose:** understand goal, classify brand vs product, choose/adapt a style (or decide
  not to), coordinate specialists, invoke review, resolve style-vs-usability conflicts.
- **Triggers:** "design/build/redesign this page/app/dashboard," "make it less generic /
  more premium," "improve this AI UI," "pick a style," any named style without a clearer
  specialist match.
- **Non-triggers:** backend, API, database, CLI, non-UI refactors.
- **Depends on / routes to:** all other skills. **References:** `_shared/*`.

### design-foundations — cross-style fundamentals · stable
- **Purpose:** hierarchy, typography, spacing, color, layout, states, responsive, a11y,
  perceived quality — the floor under every style.
- **Triggers:** any UI build/review (used alongside a style). **Non-triggers:** non-UI.
- **References:** `_shared/accessibility-baseline.md`.

### design-system-engineering — tokens & implementation · stable
- **Purpose:** primitive/semantic/component tokens, theming (light/dark/high-contrast),
  scales, variants, component APIs, maintainability, preserving existing systems.
- **Triggers:** "set up design tokens," "theme our components," "dark mode," "stop the
  one-off CSS." **Non-triggers:** non-UI, pure backend config.

### design-motion — purposeful motion · stable
- **Purpose:** what to animate and what to leave still; easing/duration, component motion,
  reduced-motion, performance, when none is better.
- **Triggers:** "animate," "transition," "the modal feels janky," "micro-interactions."
  **Non-triggers:** non-UI; backend job "animation" metaphors.

### design-review — independent reviewer · stable
- **Purpose:** strict review — style fidelity, hierarchy, AI-slop, a11y, responsiveness,
  interaction, motion, performance, maintainability; findings with severity/evidence/fix.
- **Triggers:** "review/critique/audit this UI," "does this qualify as <style>," "find
  generic patterns." **Non-triggers:** backend code review.
- **References:** `_shared/anti-ai-slop.md`, `_shared/accessibility-baseline.md`.

---

## Style specialists

Each follows the §6 contract: definition (+ distinctions), conceptual model, visual grammar,
tokens (style-defining vs product-dependent), component translation, brand vs product,
when/when-not, anti-patterns, accessibility, responsive, performance, implementation, review
checklist, examples. Each references `_shared/*`.

| Skill | Purpose (one line) | Example triggers (incl. aliases) | Example non-triggers |
|---|---|---|---|
| **design-skeuomorphism** | real-world metaphor & tactile affordance | "skeuomorphic/skeomorphism, tactile, realistic, physical control, knob/switch" | "trash can" as data; non-UI |
| **design-neumorphism** | same-surface soft extrusion (soft UI) | "neumorphic/neomorphism, soft UI/soft-ui, embossed" | non-UI |
| **design-glassmorphism** | translucent blurred layered material | "glass UI, frosted glass, frosted cards" | "glass table" in SQL |
| **design-claymorphism** | inflated soft 3-D clay shapes | "clay UI, puffy/inflated, 3D soft" | pottery/clay as data |
| **design-minimalism** | disciplined reduction with identity | "minimalist, clean, simple, refined, less cluttered" | "minimal API" |
| **design-maximalism** | controlled expressive abundance | "maximalist, bold, expressive, loud, vibrant" | non-UI |
| **design-brutalism** | raw, hard-edged, exposed structure | "brutalist, neo-brutalist, raw, hard edges" | "brutal error/bug" |
| **design-liquid-glass** | Apple dynamic adaptive glass control layer | "liquid glass, Apple glass, iOS 26 glass" | ordinary CSS glass → glassmorphism |
| **design-bento-grid** | modular variable-span overview grid | "bento grid/box, modular dashboard grid" | non-UI grid/DB |
| **design-spatial-ui** | true/pseudo spatial & XR interfaces | "spatial UI/computing, immersive, 3D interface, AR/VR/MR, visionOS" | "spatial index" in DB |

---

## Shared references (suite — not skills)

Under `plugins/ultimate-design-suite/skills/_shared/` (the suite's style skills link to these via
`../_shared/…`). Note: `omni-design` does **not** use these — it carries its own equivalents inline.

- `_shared/anti-ai-slop.md` — the AI-cliché catalog (tell → why → fix) + reviewer output
  contract.
- `_shared/brand-vs-product.md` — the brand-mode vs product-mode context switch.
- `_shared/style-compatibility.md` — dominant/supporting rules for justified hybrids.
- `_shared/accessibility-baseline.md` — WCAG 2.2-aligned floor + per-style hotspots.

## Tooling

- `scripts/design-audit.mjs` — deterministic mechanical-smell auditor (signals, not
  verdicts). Used by `design-review`.
