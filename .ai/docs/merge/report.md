# Phase 2 — Report

Inputs: [inventory.md](inventory.md). File:line refs are SOURCE-relative (`plugins/` omitted) or
`ui-ten-fixes/` for the incoming plugin.

## 1. Overlap matrix

D = defines · R = restates (same rule/number, own words or copy) · P = references the owner · — = absent.
Skill columns: **UF** user-first-ux · **UL** ux-laws · **VD** ui-visual-direction · **AC**
ui-accessibility · **CP** ui-ux-copy · **CR** ui-critique · **DS** ui-design-system · **SK**
ui-stack-laravel + ui-stack-next · **SH** ui-studio `references/shared` · **OD** omni-design ·
**SU** ultimate-design-suite (router/foundations/system/motion/review/styles) · **TF** ui-ten-fixes.

| Topic | UF | UL | VD | AC | CP | CR | DS | SK | SH | OD | SU | TF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Priority order / trade-offs | D | R | P | P | — | — | P | P | R (copy) | R (11-level) | — | — |
| Workflow Read→…→Sync | D | R | P | — | — | — | P | P | R (copy) | R | R | R (ui-fix) |
| WCAG contrast | D | R | — | R | — | P | — | R | R (quality-floor) | R | R | R (Rule 06) |
| Touch targets | D | R | — | R | — | — | — | R | R | R | R | — |
| Focus, keyboard, reflow, zoom | D | R | — | R | — | P | — | R | R | R | R | — |
| Reduced motion / flashing | D (M2) | R | P | R | — | — | — | R | R (copy) | R | R | R (Rule 10) |
| Laws of UX (30) | R (U1–U17) | D | P | — | — | P | — | — | R (copy) | — | — | P (Rule 05/08 rationale) |
| Gestalt | R (G1–G5) | D (perception) | P | — | — | P | — | — | R | R | R | R (Rule 08) |
| Nielsen / Norman | D | R (partial) | P | — | — | P | — | — | R | — | — | — |
| Ethics / dark patterns | D | R (guardrails) | — | — | P | — | — | — | R (copy) | R (ecommerce) | — | — |
| UI states matrix | D | R (guardrails) | P | — | — | — | R | R | R (copy, eight states) | R | R | — |
| Forms | D (F) | R (R29, stack) | P | — | — | — | — | R | — | R (forms.md) | — | — |
| Flows: checkout, onboarding, steppers | D (components, ethics) | D (R12–R14) | — | — | — | — | — | — | — | D (ecommerce, mobile) | — | — |
| Microcopy | D (CM) | — | P | R (copy of CM) | D (patterns) | — | — | — | — | R (content-design) | — | — |
| BM/EN localisation | D (IC) | — | — | — | D (BM1–BM8) | — | — | R | — | R (typography i18n) | — | — |
| PDPA / privacy | D | R | — | — | P | — | — | — | R | — | — | — |
| Tokens: spacing | R (L1) | R (R22) | P | — | — | — | D | R | D (visual-system L1) | R | R | R (Rule 03) |
| Tokens: type scale, weights | R (T1–T7) | R (R27) | R | — | — | — | D | R | D (T) | R | R | R (Rule 01/04) |
| Tokens: colour, radius, icons, elevation | R (C, E) | — | R | — | — | — | D | D (stack tokens) | D (C, E) | R | R | R (Rules 05/07/08) |
| Motion durations | R (M1) | — | R | — | — | — | — | — | D (M1) | R | R | R (Rule 10) |
| Visual hierarchy | R (H) | R (R19) | P | — | — | P | — | — | D (H) | R | R | R (Rule 01) |
| Generated-look / anti-slop | R (anti-patterns) | — | P | — | — | P | — | — | D (AD) | R (anti-slop) | R (_shared) | — |
| Visual direction | — | — | D | — | — | — | — | — | D (DP) | R | R (router) | — |
| Named styles (10) | — | — | — | — | — | — | — | — | — | D (styles/) | D (skills) | — |
| Context classifier / dials / brand-vs-product | — | — | — | — | — | — | — | — | — | D | D (_shared) | — |
| Visual polish rules + measurement | — | — | — | — | — | — | — | — | — | R (polish-ui) | — | D |
| Design-system audit | R (discipline) | — | — | — | — | — | D | — | — | R | R | — |
| Critique / review | D (review format) | D (audit format) | — | — | — | D | — | — | — | D (100-pt) | D (design-review) | D (ui-audit) |
| Stack build (Laravel) | — | D (stack notes) | — | — | — | — | — | D | — | D (adapter) | — | R (Blade line) |
| Stack build (Next.js) | — | — | — | — | — | — | — | D | — | R (adapter) | — | — |
| Other stacks (Vue, Svelte, native) | — | — | — | — | — | — | — | — | — | D | — | R (token snippets) |
| Handoff | — | — | — | — | — | — | — | — | — | — | — | — |
| Research | D (Measure) | — | — | — | — | — | — | — | — | — | — | — |

Not shown (single owner, no overlap): ui-handoff, ui-research, ui-theming, ui-canvas-art (all D in
their own row, nobody else).

## 2. Value conflicts

| ID | Topic | Side A | Side B (and C…) |
|---|---|---|---|
| C1 | Touch target: floor or aim? | user-first-ux/…/accessibility.md:17 "≥ 24x24 (AA); **aim** for 44x44"; checklist.md:16 "goal 44px"; ux-laws/SKILL.md:47 "aim for 44" | ui-studio/references/shared/quality-floor.md:12 "**House floor 44x44**"; ux-laws/SKILL.md:44 "≥ 44px tall" (primary); omni tables-data-density.md:11 rows "≈36–44px"; omni mobile-ui.md:10 "44pt / 48dp" |
| C2 | Contrast target | user-first-ux accessibility.md:6 "≥ 4.5:1" (floor only) | ui-ten-fixes rules.md:167 "4.5–7 = pass; **aim ~7:1** for small secondary text"; SKILL.md:24 |
| C3 | Large bold text threshold | accessibility.md:6, wcag-22-aa.md:12, omni, suite, Ten Fixes: "≥ 18.66px bold" | ux-laws guardrails.md:17 "≥ ~18.5px bold" |
| C4 | Missing-state severity | states-feedback.md:15-16 and ui-studio severity.md:16 "at least **High**" | ux-laws guardrails.md:66 "at least **Medium**; High when stuck" |
| C5 | Severity scale | user-first-ux SKILL.md:141, ui-studio severity.md:7-10: Critical/High/Medium/Low | ux-laws audit-template.md:16, SKILL.md:130: High/Medium/Low; omni design-audit.md:49: + "Polish"; suite: objective/likely/preference; Ten Fixes rules.md:287: pass/warn/fail |
| C6 | Spacing scale | visual-system.md:21 "4/8-point scale only"; tokens-tailwind-bootstrap.md:12 `--spacing: 4px` (4pt grid); Bootstrap 0/4/8/16/24/48 (:58) | Ten Fixes rules.md:90 "**4 · 8 · 12**", ≤3 steps + 1 inset per component (:85); omni spacing-layout.md:5 "4·8·12·16·24·32·48·64·96"; suite foundations:45 "4/8/12/16/24/32/48/64"; ux-laws SKILL.md:222 form gaps 8/24/40 |
| C7 | Type scale | visual-system.md:43 "ratio 1.2-1.25 … 12/14/16/20/24/32" | Ten Fixes tokens.md:24-27 hero 76 / title **17** / body 14 / caption 12; omni typography.md:25 "12·14·16·20·25·31·39·49·61", editorial up to 1.333 (:20) |
| C8 | Hero size ratio | visual-system scale tops at 32px = 2× a 16px body (T1); H1 "display size" | Ten Fixes SKILL.md:19 "hero **≥ 3× body**" (76px) |
| C9 | Font families | visual-system.md:51 T5 "At most two type families"; VD typography-structure-motion.md:8 "one family, or a pair" | Ten Fixes rules.md:113 "> 1 for UI text = warn"; ui_lint.py:347-348 families > 1 → warn |
| C10 | Uppercase | visual-system.md:10 H2 "uppercase" labels OK, :54 T7 short labels OK; ai-defaults.md:31; stat-card.md:48 uses `uppercase`; ux-laws SKILL.md:213 `uppercase` group label | Ten Fixes SKILL.md:22, rules.md:110 "no caps … any = warn" (exception: "exactly one role", :123) |
| C11 | Underline | principles.md:23 NO1 links distinguishable without colour (underline, weight, icon); laws-perception.md:96 "links underlined" | Ten Fixes rules.md:118 "Remove … underlines", exception only "links in running prose" (:122) |
| C12 | Motion durations | visual-system.md:84 M1 "150-300ms" | omni motion.md "100–200 / 200–350ms"; suite design-motion "80–120 / 150–250 / 250–400"; suite tokens 120/200ms; Ten Fixes rules.md:274 "200–400 ms" |
| C13 | Heading line-height | visual-system.md T3 "1.1-1.3 headings" | omni typography.md "1.05–1.25 display"; Ten Fixes tokens.md `--leading-tight: 1` (hero) |
| C14 | Body size | visual-system.md T3 "≥ 16px reading, ≥ 14px dense UI" | Ten Fixes tokens.md:26 body 14px (dense card) |
| C15 | Starter font | ai-defaults.md:14 AD6 "Inter picked without a reason"; typography-structure-motion.md:11 | Ten Fixes tokens.md:35, tokens.css:14, reference-card.html:12 `--font-sans: "Inter"` |
| C16 | Radius | stack skills `--radius-control: 0.5rem` | Ten Fixes `--radius: 16px` (tokens.md:48); suite style radii 16–28px |
| C17 | Focus indicator size | user-first-ux: 3:1 only | omni accessibility.md:14 / suite _shared:16 "aim ≥2px, ≥3:1" |
| C18 | Conflict order | user-first-ux 6-level priority (SKILL.md:24-31) | omni SKILL.md 11-level order (safety→task→a11y→…→novelty) |
| C19 | Automated a11y coverage | ui-accessibility testing.md:9 "roughly 30%" | omni/suite "~30–40%" |
| C20 | Search threshold | components.md:45 P1 "list over ~7 items → type-ahead" | components.md:36-37 F8 / ux-laws R8 "> 15 → searchable combobox" |
| C21 | Ten Fixes internal: weights | rules.md:114 "> 2 warn, > 3 fail (not counting hero)" | ui_lint.py:347-348 "> 3 warn, > 4 fail" (counts hero) — consistent once the hero weight is counted; not a real conflict |

## 3. Trigger collisions

| Pair | Both descriptions match | Example prompt |
|---|---|---|
| user-first-ux ↔ ux-laws | "ANY user interface … build, change, review" in both | "Review this registration form" |
| user-first-ux ↔ ui-visual-direction | UF lists "make this look better / more modern / premium", "redesign", "polish" | "Make this settings page look more modern" |
| user-first-ux ↔ omni-design ↔ ultimate-design | "make it look better / less generic / more premium" | "Redesign our dashboard to look more premium" |
| ux-laws ↔ ui-ten-fixes (ui-fix, ten-fixes-rules) | "make it better/cleaner", "polish" vs "polish, clean up, make this look better" | "Clean up this card" |
| ui-critique ↔ design-review ↔ omni (audit) ↔ ui-audit (Ten Fixes) ↔ ux-laws (audit) | "review/critique/audit this UI" | "Review this dashboard design" |
| ui-critique ↔ ui-audit ↔ ten-fixes-rules | "why does this feel off?" / "looks ugly, cluttered, off" | "Why does this page look so cluttered?" |
| ui-design-system ↔ design-system-engineering ↔ omni ↔ Ten Fixes ui-build | "design system / tokens" in all four | "Set up design tokens for our app" |
| ui-visual-direction ↔ Ten Fixes ui-build ↔ omni ↔ ultimate-design | "design/build/create any new UI / dashboard / widget" | "Build a KPI widget" |
| ui-stack-laravel ↔ Ten Fixes ui-fix/ui-build (both name Blade/Livewire) | stack + build/fix | "Polish this Livewire view" |
| omni-design ↔ ultimate-design ↔ 10 suite style skills | every named style is in omni's description too | "Give the nav a liquid glass look" |
| design-motion ↔ omni-design ↔ orbit-ui-motion | transitions, modals, drawers | "Add transitions to the modal" |
| ui-accessibility ↔ user-first-ux ↔ ux-laws | WCAG appears in all three | "Is this modal accessible?" |
| ui-ux-copy ↔ user-first-ux | UF: "copy on a screen", "honest microcopy" | "Rewrite the error messages on this form" |
| orbit-design-engine (26 skills) ↔ ui-studio / omni | "dashboard", "admin panel redesign", "app shell", "visual QA" | "Redesign the admin dashboard" (orbit-ui-director, orbit-ui-dashboards, ui-visual-direction, omni) |

## 4. Verdicts for omni-design and ultimate-design-suite

### omni-design — **partly unique** → merge the unique parts into ui-studio (and the behaviour parts into user-first-ux)

Coverage by user-first-ux + ui-studio + ui-ten-fixes, per topic unit (53 units: SKILL + 22 refs + 11
styles + 8 workflows + 5 adapters + 6 checklists; full = 1, partial = 0.5): refs 12.5/22, SKILL 0.5,
styles 0/11, workflows 5.5/8, adapters 2/5, checklists 4.5/6 → **25/53 ≈ 47 % already covered**.

Unique (must survive): context classifier · design dials · style router + hybrid rules · brand-to-UI
intent table · 100-point scored audit with certainty classes · e-commerce, enterprise/admin, public
website and mobile playbooks · reference-to-code · redesign-preserve-first workflow · Vue/Nuxt/Svelte
and native-mobile adapters · Laravel convention-preservation list (@csrf, @error/old(), __(), @can,
paginator, Bootstrap/AdminLTE) · effects performance budget · colour role triples, OKLCH ramps,
dataviz colour · responsive test matrix · motion vocabulary · scenario/trigger test prompts.

### ultimate-design-suite — **duplicate of omni-design, partly unique vs ui-studio** → merge only its deeper style files and two shared references

- Versus omni-design: ~100 % of its topics exist there (omni's SOURCES.md says it was built from the
  suite). Versus user-first-ux + ui-studio: **4.75/19 units ≈ 25 % covered**.
- Unique vs omni: the 10 style skills are ~3× deeper (tokens, component translation, review
  checklists) · design-motion component patterns and gesture response · design-system-engineering
  token examples · `_shared/brand-vs-product.md` (full version) · `_shared/style-compatibility.md`.
- Duplicates to delete: design-foundations, design-review (except the style-fidelity check),
  `_shared/accessibility-baseline.md`, `_shared/anti-ai-slop.md`, the router workflow.

### Recommendation

One style library in ui-studio, built from the deeper half of each: suite style files + omni router +
suite hybrid/brand-mode references, in a single new skill `ui-styles` (one trigger on named styles
instead of 11). Both plugins become deprecated stubs. **Option B** (keep omni-design as a separate,
distinct-job plugin) is listed as Q1 in the plan.

## 5. Unique assets that must survive

| Asset | Where now | Survives as |
|---|---|---|
| Measurement scripts ui_lint.py, contrast.py, dom_probe.js, playwright_probe.mjs | ui-ten-fixes/skills/ui-audit/scripts | ui-studio/skills/visual-polish/scripts |
| Worked examples sample-before.html, reference-card.html, tokens.css, range-bar.css | ui-ten-fixes assets | visual-polish/assets (unchanged) |
| Token hook check-tokens.sh + hooks.json | ui-studio/hooks | unchanged |
| Agents ui-critic, design-system-auditor | ui-studio/agents | unchanged |
| Agent a11y-auditor | ui-studio/agents | user-first-ux/agents |
| Agent ui-ten-fixes-auditor | ui-ten-fixes/agents | ui-studio/agents (no same-role agent: needs Bash + scripts) |
| Evals: ui-studio 55 trigger cases | ui-studio/evals | 40 stay, 15 move with their skills to user-first-ux/evals |
| Evals: user-first-ux evals.json, ux-laws evals.json | in skills | stay with their skills |
| omni tests/ (scenarios, regression, trigger) | omni-design | docs/archive/omni-design/tests |
| Root evaluations/, scripts/design-audit.mjs | repo root | unchanged (root tooling) |
| 8 before/after examples | user-first-ux (ui-studio copy identical) | user-first-ux only |
| 29 OFL font families + licences, theme-showcase.pdf | ui-studio | unchanged |
| Templates (a11y report, critique, design-system ×3, handoff, plan, copy, synthesis, interview guide, UX audit) | ui-studio, ux-laws | stay with their skills |
| BM/EN glossary BM1–BM8 | ui-studio/ui-ux-copy | moves with ui-ux-copy to user-first-ux |
