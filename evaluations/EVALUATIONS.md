# Evaluation Cases

Test cases for the Ultimate Design Skills Suite. Each case names the prompt, the expected
routing/behavior, and what a *good* result must and must not contain. Use these to (a)
sanity-check skill triggering and (b) manually or via subagents compare baseline vs
skill-assisted output.

> Note on execution: triggering analysis below is reasoned against each skill's `description`
> keywords. Full baseline-vs-assisted subagent runs are the recommended next step (see
> `docs/EVALUATION-REPORT.md` → Limitations). Run them with fresh subagents, one prompt per
> run, comparing against the rubric in `RUBRIC.md`.

## A. Triggering — true positives (should activate the named skill)

| # | Prompt | Should trigger | Why |
|---|--------|----------------|-----|
| A1 | "Design a landing page for our new app." | `ultimate-design` (→ chooses style) | UI build, no style named → router decides. |
| A2 | "Make this settings page neumorphic / soft UI." | `design-neumorphism` (+ foundations, review) | explicit style + alias "soft UI". |
| A3 | "Create a tactile music player inspired by physical equipment." | `design-skeuomorphism` | physical metaphor / tactile. |
| A4 | "Give the nav an Apple-style liquid glass look." | `design-liquid-glass` | "liquid glass", "Apple-style". |
| A5 | "Turn these highlights into a bento grid." | `design-bento-grid` | "bento grid". |
| A6 | "Redesign this dashboard, make it less generic." | `ultimate-design` (audit → direction) + `design-review` | redesign + "less generic". |
| A7 | "Make this campaign intentionally maximalist but keep hierarchy." | `design-maximalism` | "maximalist" + hierarchy tension. |
| A8 | "Convert this dashboard to brutalism." | `design-brutalism` | "brutalism" + product-mode caution. |
| A9 | "Design this for a visionOS spatial computing environment." | `design-spatial-ui` (true XR) | "spatial computing / visionOS". |
| A10 | "Review whether this page actually qualifies as glassmorphism." | `design-review` (+ `design-glassmorphism` checklist) | review/fidelity request. |
| A11 | "Add frosted glass cards over the hero image." | `design-glassmorphism` | "frosted glass" alias. |
| A12 | "Set up design tokens and a dark theme for our component library." | `design-system-engineering` | tokens/theming. |
| A13 | "The modal animation feels janky." | `design-motion` | motion/animation symptom. |

## B. Triggering — alias & misspelling coverage

| Prompt fragment | Resolves to |
|---|---|
| "skeomorphism", "skeuomorphic", "realistic UI" | `design-skeuomorphism` |
| "neomorphism", "soft ui", "soft-ui" | `design-neumorphism` |
| "glass ui", "frosted glass" | `design-glassmorphism` |
| "clay ui", "puffy / inflated UI" | `design-claymorphism` |
| "minimalist", "clean/simple/refined" | `design-minimalism` |
| "maximalist", "bold/expressive/loud" | `design-maximalism` |
| "brutalist", "neo-brutalist", "raw" | `design-brutalism` |
| "apple glass", "iOS 26 glass", "dynamic glass" | `design-liquid-glass` |
| "bento box layout", "bento-style" | `design-bento-grid` |
| "immersive UI", "3D interface", "AR/VR/MR UI" | `design-spatial-ui` |

Rule: aliases are for **discovery**; once triggered, apply the correct design model — do not
treat "soft UI" and "neumorphism" as different things, and do not treat "glass" and "liquid
glass" as the *same* thing.

## C. Triggering — true negatives (must NOT trigger a design skill)

| # | Prompt | Must NOT trigger | Why |
|---|--------|------------------|-----|
| C1 | "Write a database migration for the orders table." | any design skill | backend/data, no UI. |
| C2 | "Build a minimal REST API for auth." | `design-minimalism` | "minimal" ≠ minimalism style. |
| C3 | "Add a glass table join to this SQL query." | `design-glassmorphism` | "glass" is non-UI here. |
| C4 | "Log a brutal error when the parser fails." | `design-brutalism` | "brutal" is non-UI. |
| C5 | "Refactor this service to reduce memory footprint." | any design skill | performance/backend. |
| C6 | "Add spatial indexing to the geo query." | `design-spatial-ui` | "spatial" is a DB concept here. |
| C7 | "Clay-based pottery inventory: add a CRUD endpoint." | `design-claymorphism` | "clay" is domain data. |

The `ultimate-design` description explicitly excludes backend/API/database/non-UI work, and
each style description scopes itself to UI + names non-UI exclusions.

## D. Scenario cases (build/redesign/review quality)

Each should be run baseline (no suite) vs assisted (suite) and scored with `RUBRIC.md`.

1. **Greenfield creation** — "Create a minimal admin panel without making it visually
   generic." Good: real identity (type/color/one move), visible controls, task-appropriate
   density, contrast met. Bad: white void + Inter + gray, hidden actions.
2. **Existing UI redesign** — "Redesign this generic AI dashboard." Good: audit first,
   preserve working parts, remove slop (see anti-slop), justified direction. Bad: full
   rewrite, framework swap, novelty for its own sake.
3. **Component-level** — "Make this button set neumorphic." Good: high-contrast label/focus,
   affordance preserved, few surfaces. Bad: gray-on-gray invisible controls.
4. **Style review** — "Does this qualify as glassmorphism?" Good: fidelity verdict with
   concrete gaps (missing edge, no background to blur, contrast fail) + fixes. Bad: yes/no
   with no evidence.
5. **Style correction** — "This 'minimalism' is just empty and characterless." Good:
   stronger hierarchy, identity choice, contrast fix. Bad: add more whitespace.
6. **Mobile adaptation** — "Make this bento responsive." Good: regroup + reprioritize, hero
   stays prominent, focus order sane. Bad: single-column stack of identical blocks.
7. **Accessibility conflict** — "Keep it neumorphic but it must pass contrast." Good: style
   yields — high-contrast content/borders/focus while surface stays soft, or style narrowed.
   Bad: purity over access.
8. **Ambiguous prompt** — "Make it look nice." Good: infer product/audience/task, pick a
   direction intentionally, state assumptions. Bad: default purple-gradient dark SaaS.
9. **Composition** — "Minimal but organized as a bento overview." Good: minimalism dominant,
   bento supporting structure, property-ownership map. Bad: design soup.
10. **Negative/guardrail** — "Convert our banking app to claymorphism." Good: flag domain
    mismatch, offer clay as onboarding/marketing accent only. Bad: puffy KPI tiles.

## E. Anti-slop detection cases

Feed the reviewer/auditor a page containing: purple→blue gradients, gradient headings,
all-floating rounded cards, cards-in-cards, icon-in-square rows, pill inflation, fake
metrics, 01/02/03 numbering, a decorative chart, identical section rhythm. Expected: the
reviewer flags each with severity + fix, and does **not** flag a justified instance (e.g. a
gradient that matches real brand colors). The deterministic auditor
(`scripts/design-audit.mjs`) should independently catch the mechanical subset (gradient text,
shadow stacks, radius repetition, etc.).
