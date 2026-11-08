# Phase 1 — Inventory

SOURCE `c:\laragon\www\ai-skills` (read-only) · TARGET `c:\laragon\www\afyz-forge` · date 2026-11-07.
Every file of the five UI/UX plugins and `_incoming/ui-ten-fixes` is listed with its line count in
[inventory-appendix-files.md](inventory-appendix-files.md). Every internal path reference and every
`${CLAUDE_PLUGIN_ROOT}` use (39) is listed in [inventory-appendix-paths.md](inventory-appendix-paths.md).

Read depth: all files of user-first-ux, ux-laws, ui-studio (skills, references, agents, hook, evals
prompts), ui-ten-fixes (incl. scripts) and omni-design references/workflows/adapters/checklists were
read in full. omni-design `styles/*` (10 deep files), `tests/*`, and the suite's 15 `SKILL.md`
bodies were read at heading + stated-value level (they are style-specific; their values are in §3).
Fonts, licences and the theme PDF are binary/legal text and were inventoried, not read.

Other repo plugins (`system-design`, `orbit-design-engine`, `session-orchestrator`) are out of scope.
`orbit-design-engine` is a 26-skill UI/UX plugin that the prompt does not list; see report §3 and Q2.

## 1. Plugin metadata

| Plugin | plugin.json version | plugin.json description (short) | marketplace entry |
|---|---|---|---|
| user-first-ux | 1.0.0 | User-first UX skill: priority order, workflow, Nielsen/Norman/Gestalt/Laws-of-UX, WCAG 2.2 AA, dark-pattern bans, checklist, examples, evals | yes, same wording family |
| ux-laws | 1.0.0 | UX-laws engine: 30 Laws of UX as checkable rules, 6 pillars, guardrails, Pass/Fail audit, Laravel stack notes | yes |
| ui-studio | 0.1.0 | Laravel + Next.js UI studio: visual direction, stack builds, EN/BM copy, design system, handoff, critique, WCAG audit, research, theming, canvas art; absorbs user-first-ux; 3 agents + hook | yes |
| omni-design | 1.0.0 | One adaptive design-intelligence skill: classifier, style router, dials, 22 refs, 11 styles, workflows, adapters, a11y gate, 100-pt audit | yes |
| ultimate-design-suite | 0.2.0 | Router + foundations + system + motion + reviewer + 10 style specialists | yes |
| ui-ten-fixes (incoming) | 1.0.0 | Ten presentation rules; audit, fix, build | not registered (has `marketplace-entry.json`) |

All have `author` objects and Apache-2.0. Each SOURCE plugin also has `.codex-plugin/plugin.json`
(`"skills": "./skills/"`); ui-ten-fixes has none. Marketplace: name `ai-skills`, owner `Afyz97`,
metadata version 0.9.0, 8 plugins.

## 2. Components

### user-first-ux (22 files, 1 skill)
- Skill `user-first-ux` — SKILL.md 163 lines.
- references/ (10): accessibility 41 · anti-patterns 37 · checklist 31 · components 97 · content 38 ·
  ethics-privacy 45 · inclusive-context 27 · principles 69 · states-feedback 42 · visual-system 95.
- examples/ (8): assignee-picker, avatar-stack, data-table, destructive-confirm, empty-state,
  product-card, signup-form, stat-card (39–73 lines each).
- evals/evals.json 143 lines (skill-creator format). No commands, agents, hooks, scripts or assets.

### ux-laws (10 files, 1 skill)
- Skill `ux-laws` — SKILL.md 260 lines (33 build rules R1–R33, audit protocol, law index, Blade/
  Livewire stack notes, law conflicts).
- references/: audit-template 82 · guardrails 77 · laws-behaviour 121 · laws-cognition 185 ·
  laws-interaction 84 · laws-perception 126 (30 laws, each: definition, origin, rules, do/don't,
  audit check, violations, misuse).
- evals/evals.json 51 lines. No commands, agents, hooks.

### ui-studio (276 files, 17 skills)
- Model-invoked skills (11) with line counts: ui-accessibility 57 · ui-canvas-art 63 · ui-critique 63
  · ui-design-system 82 · ui-handoff 52 · ui-research 52 · ui-stack-laravel 104 · ui-stack-next 94 ·
  ui-theming 50 · ui-ux-copy 68 · ui-visual-direction 101.
- Command skills (6, `disable-model-invocation: true`): ui-a11y 12 · ui-build 29 · ui-copy 11 ·
  ui-plan 21 · ui-system 12 · ui-theme 11.
- Skill references: ui-accessibility (template, testing, wcag-22-aa 80); ui-canvas-art (canvas-rules,
  philosophy); ui-critique (template); ui-design-system (audit/document/extend templates); ui-handoff
  (spec-template, stack-notes); ui-research (interview-guide, methods, synthesis-template);
  ui-stack-laravel (blade-components, filament-theme, flux-ui-v2, livewire-alpine 104,
  tokens-tailwind-bootstrap); ui-stack-next (motion-and-focus, radix-dialog-focus, rsc-boundaries,
  tailwind-v4-theme); ui-theming (anthropic-brand, presets); ui-ux-copy (bilingual-bm-en 83, content,
  inclusive-context, patterns, template); ui-visual-direction (components 97, plan-template,
  typography-structure-motion) + examples/ (8).
- Plugin-root `references/shared/` (12): ai-defaults · anti-patterns · checklist · connectors ·
  ethics-privacy · principles (DP1–DP8) · priority-workflow · quality-floor · severity ·
  states-feedback · ux-principles · visual-system.
- agents/ (3, read-only): a11y-auditor · design-system-auditor · ui-critic.
- hooks/: hooks.json (PostToolUse Edit|Write|MultiEdit) + check-tokens.sh 113 (warn-only, 10 checks).
- assets: 29 OFL font families (54 `.ttf` + 29 `*-OFL.txt`) in ui-canvas-art; theme-showcase.pdf.
- licenses/ (5 Apache texts) · NOTICE.md 47 · README.md 123.
- evals/: 11 skills × 5 cases (3 trigger, 2 no-trigger) = 55 cases, 110 files (`prompt.md` +
  `graders/skill-(not-)fired.md`, `plugins: ["../../.."]`).

### omni-design (59 files, 1 skill)
- Skill `omni-design` — SKILL.md 188 lines; README 121, CHANGELOG 39, SOURCES 104.
- references/ (22, 46–93 lines): accessibility, anti-slop, brand-to-ui, color, content-design,
  design-audit, design-foundations, design-systems, ecommerce, enterprise-dashboards, forms,
  mobile-ui, motion, navigation, performance, public-websites, reference-to-code, responsive-design,
  spacing-layout, states, tables-data-density, typography.
- styles/ (11): style-router 168 + 10 style files (44–52).
- workflows/ (8), adapters/ (5), checklists/ (6), tests/ (3: scenarios, regression-prompts,
  trigger-tests). No scripts, agents, hooks.

### ultimate-design-suite (21 files, 15 skills)
- Skills: ultimate-design 135 (router) · design-foundations 106 · design-system-engineering 113 ·
  design-motion 100 · design-review 117 · 10 style skills 125–165 (bento-grid, brutalism,
  claymorphism, glassmorphism, liquid-glass, maximalism, minimalism, neumorphism, skeuomorphism,
  spatial-ui).
- skills/_shared/ (4): accessibility-baseline 75 · anti-ai-slop 109 · brand-vs-product 55 ·
  style-compatibility 60. Style skills link `../_shared/…`.
- Related root assets: `scripts/design-audit.mjs` (deterministic smell auditor "for the Ultimate
  Design Skills Suite"), `evaluations/` (EVALUATIONS.md, RUBRIC.md, fixtures/bad-sample.css).

### _incoming/ui-ten-fixes (19 files, 4 skills)
- Skills: ten-fixes-rules 44 (+ references/rules.md 292, tokens.md 119) · ui-audit 65 (+ assets
  sample-before.html; scripts ui_lint.py 418, contrast.py 108, dom_probe.js 145,
  playwright_probe.mjs 26) · ui-fix 63 · ui-build 47 (+ assets tokens.css, range-bar.css,
  reference-card.html).
- commands/ (3, legacy `commands/` format): ui-audit, ui-fix, ui-new.
- agents/: ui-ten-fixes-auditor (Read, Grep, Glob, Bash).
- README 68 · plugin.json · marketplace-entry.json.
- Pre-merge script baseline: [baseline-scripts.txt](baseline-scripts.txt) — sample-before: 6 fail
  (01,03,04,05,06,07) / 2 warn (02,09) / 2 manual; reference-card: 6 pass / 4 manual.

## 3. Topics and stated values (per file)

Legend: values are quoted as written. "→" names the file:line.

| Topic | user-first-ux | ux-laws | ui-studio | omni-design | suite | ui-ten-fixes |
|---|---|---|---|---|---|---|
| Priority order | 6 levels honest>…>aesthetic (SKILL:24-31) | same, one line (SKILL:22) | copy (priority-workflow:10-17) | 11-level conflict order (SKILL:166-170) | — | — |
| Workflow | Read→Report→Plan→Approve→Implement→Verify→Sync (SKILL:40) | Read/Plan/Build/Self-audit/Report (SKILL:29-36) | copy (priority-workflow:29) | classify→inspect→direction→system→implement→validate→review | 8 phases (ultimate-design) | same 7 steps (ui-fix:12) |
| Text contrast | 4.5:1, large 3:1 (≥24px / ≥18.66px bold) (accessibility:6) | 4.5:1, large ≥~18.5px bold (guardrails:17) | same as UF (wcag-22-aa:12, quality-floor:10) | same (accessibility:12, color:22) | same (_shared a11y:12) | ≥4.5 floor, **aim ~7:1** small secondary (rules:167, SKILL:24) |
| Non-text / focus | 3:1 (accessibility:6) | 3:1 (guardrails:18) | 3:1 (quality-floor:11) | 3:1, focus **≥2px** (accessibility:14) | same, ≥2px (_shared:16) | icons/UI 3:1 (rules:167) |
| Touch targets | ≥24×24 AA; **aim** 44×44 / 48dp (accessibility:17; checklist:16 "goal 44") | R1 primary ≥44px tall; R2 ≥24, aim 44, ≥8px gap (SKILL:44-47); Fitts ≥44 never <24 (laws-interaction:22) | **house floor 44×44**, AA 24 (quality-floor:12; wcag-22-aa:35-37) | ≥24, prefer ≥44; mobile 44pt/48dp; table rows 36–44 (mobile-ui:10, tables:11) | ≥44 in every style checklist | — |
| Spacing | 4/8-pt scale (visual-system:21) | 4/8px; form 8/24/40 (`space-y-2/6/10`) (SKILL:96,222) | 4pt grid, `--spacing: 4px`; Bootstrap 0/4/8/16/24/48 (tokens-tailwind-bootstrap:12,58); hook flags non-multiples of 4 | 4·8·12·16·24·32·48·64·96 (spacing-layout:5) | 4/8/12/16/24/32/48/64 (foundations:45) | **3 steps per component, 4·8·12** + 1 inset (rules:85-92) |
| Type scale | ratio 1.2–1.25, 12/14/16/20/24/32 rem (visual-system:43); body ≥16 read, ≥14 dense; line-height 1.4–1.6 / 1.1–1.3 (T3) | — | same (copy) | 1.2 dense / 1.25–1.333 editorial; 12·14·16·20·25·31·39·49·61; display lh 1.05–1.25 (typography:20-25) | 1.2–1.333 | hero/title/body/caption **76/17/14/12 px**; hero **≥3× body** (tokens:24-27, SKILL:19) |
| Families / weights | ≤2 families (T5) | — | one family or two contrasting (typography-structure-motion:8) | 1–2 families; weights 400→600→700 | 1–2 | **one family** (>1 warn), two weights (rules:113-119); script: families >1 warn, weights >3 warn/>4 fail |
| Uppercase | short uppercase labels allowed (H2, T7) | sidebar group labels `uppercase` (SKILL:213) | AD5 bans decorative eyebrows; short data labels allowed (ai-defaults:31) | open tracking on caps | — | **no caps** for emphasis; one caps role allowed (rules:110-123) |
| Underline | links distinguishable without colour (NO1) | links underlined (laws-perception:96) | — | — | — | **no underlines**; prose links exempt (rules:118-122) |
| Colour | semantic tokens, 60/30/10, never colour alone, designed dark mode (C1-C5) | — | same + Flux accent pairs 4.5:1 (flux-ui-v2:14-15) | role tokens incl. status -bg/-fg/-border, OKLCH ramps, dataviz palettes | — | neutral text + **one accent** (rules:142-146) |
| Radius | — | — | `--radius-control` 0.5rem (stack-laravel SKILL:78) | radius 0–4px for "sharper" | 6/10/16/999px tokens; style radii 16–28px | single `--radius` 16px (tokens:48) |
| Icon sizes | — | icon `size-5` in `size-11` hit area | lucide `size-4` | one family, one stroke | — | inline 16–20, list 20–24, hero 48–64; tokens 20/56, stroke 1.5 (rules:197-198) |
| Motion | 150–300ms, ease-out in / ease-in out; reduced motion; no flash >3/s (M1-M2) | reduced motion (A11y-7) | same (copy) + DP5 one ambient moment | 100–200 small / 200–350 large (motion.md) | 80–120 feedback / 150–250 / 250–400; tokens 120/200ms | state change **200–400ms**; reference card 300ms (rules:274) |
| Response time / CWV | 100ms, 400ms, 1s, 10s; skeleton >300ms; LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 (states-feedback:20-26) | 100ms / 400ms / 10s (R3) | copy | LCP/CLS/INP framing, no numbers | — | — |
| Breakpoints | content-driven; prose 65–75ch; app 1200–1440px | — | handoff template >1024 / 768–1024 / <768 | test matrix 320–360, 390–430, 768, 1024–1280, 1440, 1920+ | 720px bento example | — |
| States | full ST list; missing empty/error/loading **≥ High** (states-feedback:15) | States-1…7; missing **≥ Medium, High if stuck** (guardrails:66) | eight states (quality-floor:22); ≥ High (severity:16) | full list | — | — |
| Severity | Critical/High/Medium/Low (SKILL:141) | High/Medium/Low (audit-template:16) | Critical/High/Medium/Low (severity.md) | Critical/High/Medium/Low/Polish (design-audit:49) | objective/likely/preference | pass/warn/fail/n-a per rule |
| Choice counts | F8: 2–5 radios, 6–15 select, >15 combobox; P1 picker list >~7 → type-ahead | R8 >3 compare, >15 search; R28 groups 5–9; R29 >~7 fields split | copy | — | — | — |
| Dark patterns | 11 banned (EP1), EP2-EP6 | 10 banned, Ethics-1…5 | copy | ecommerce list | — | — |
| Localisation | IC1-IC6, +30–40% strings, en-MY formats | — | BM1-BM8 (bilingual-bm-en) | multilingual type | — | — |
| Automated a11y coverage | "floor" | — | ~30% (testing:9) | ~30–40% | ~30–40% | — |

Unique-topic notes:
- ui-studio only: DP1–DP8 principles, AD1–AD7 generated-look tells, stack recipes (Flux, Filament,
  Livewire, Fabric.js, Radix, RSC), theming presets, canvas art, research methods, handoff, token hook.
- omni-design only (vs ui-studio/user-first-ux): context classifier, design dials, style router,
  brand-to-ui intent table, 100-point scored audit, e-commerce / enterprise / public-site / mobile
  playbooks, reference-to-code, Vue/Nuxt/Svelte and native-mobile adapters, effects performance.
- suite only (vs omni): deeper per-style files (tokens, component translation, review checklist),
  motion component patterns, token example values.
- ui-ten-fixes only: the ten counted rules with numeric targets, measurement scripts, worked example.

## 4. Internal path references and `${CLAUDE_PLUGIN_ROOT}`

Full list: [inventory-appendix-paths.md](inventory-appendix-paths.md). Summary:
- ui-studio: 31 `${CLAUDE_PLUGIN_ROOT}/references/shared/…` links in SKILL.md files, 1 in
  `ui-canvas-art` (fonts), 1 in `hooks/hooks.json` (33 total; with ui-ten-fixes' 6 = 39 uses). Reference files name plugin-root paths
  (`references/shared/…`, `skills/ui-ux-copy/references/…`).
- ui-ten-fixes: 6 `${CLAUDE_PLUGIN_ROOT}/skills/…` (agent + 3 commands) and relative
  `../ten-fixes-rules/…`, `scripts/…`, `assets/…` in skills.
- user-first-ux / ux-laws: relative `references/…`, `examples/…` only.
- omni-design: relative `references/ styles/ workflows/ adapters/ checklists/` only.
- suite: `../_shared/…` from every style skill.
- No SOURCE file references another plugin by path today.
