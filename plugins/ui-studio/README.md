# ui-studio

A Claude Code plugin for UI work in **Laravel** (Blade, Livewire 4, Flux UI v2, Filament,
Alpine.js, Tailwind CSS, legacy Bootstrap 5, Fabric.js, Vite) and **Next.js** (App Router,
React 19, TypeScript, Tailwind v4, Radix UI, lucide-react).

It owns how a UI **looks and is built**: visual direction with a self-review against generic
AI-looking defaults, named styles, design tokens and design-system audits, visual polish with the
measured Ten Fixes rules, stack-specific implementation, critique, handoff, theming and canvas
art. How the UI **behaves** (priority order, workflow, WCAG, laws of UX, states, copy, research)
is owned by the `user-first-ux` plugin; ui-studio points to it by skill name and keeps a
one-line minimum, so it still works installed alone.

## Install

```bash
# from GitHub
claude plugin marketplace add Afyz97/afyz-forge
claude plugin install ui-studio@afyz-forge

# local development (edits load on /reload-plugins, no version bump needed)
claude plugin marketplace add C:/laragon/www/afyz-forge
claude plugin install ui-studio@afyz-forge
claude plugin validate ./plugins/ui-studio
```

Requirements: Claude Code with plugin support. The hook needs a POSIX shell with
`grep`, `sed` and `awk`. On Windows (e.g. Laragon) that is Git Bash, which Claude Code already
requires; WSL is not needed. Agents use Playwright MCP tools when the Playwright plugin is
installed and fall back to source-only checks otherwise.

## Commands

Plugin skills are namespaced: type `/ui-studio:<name>` (the bare `/<name>` also works when no
other command shares it).

| Command | What it does | Runs |
|---|---|---|
| `/ui-studio:ui-plan <brief>` | UX brief, token plan, ASCII wireframes, self-review. No code. | ui-visual-direction (pass 1) |
| `/ui-studio:ui-build <brief>` | Plan, self-review, **approval gate**, build, copy, critique, a11y check, polish | visual-direction -> stack skill -> (user-first-ux copy + a11y) -> ui-critic -> visual-polish |
| `/ui-studio:ui-system audit\|document\|extend <target>` | Design-system work | ui-design-system (+ design-system-auditor) |
| `/ui-studio:ui-theme <preset\|custom>` | Apply a theme to slides/docs/pages | ui-theming |
| `/ui-studio:polish-audit <path\|url>` | Ten Fixes scored audit, read-only | visual-polish (audit) |
| `/ui-studio:polish-fix <path> [--rules 01,03]` | Apply the Ten Fixes in rule order, approval gate | visual-polish (fix) |
| `/ui-studio:polish-new <what> [stack]` | New component that passes all ten rules | visual-polish (build) |

Moved to `user-first-ux` in 1.0.0: `/ui-a11y`, `/ui-copy` (and the `ui-accessibility`,
`ui-ux-copy`, `ui-research` skills).

## Skill map

Model-invoked (Claude picks them from the request):

| Skill | Use it for |
|---|---|
| `ui-visual-direction` | New UI or a new look: grounding, token plan, anti-default review, build; public websites, reference-to-code, redesign, extra stack adapters |
| `ui-styles` | A named style or hybrid (minimalism, glassmorphism, neumorphism, brutalism, bento, liquid glass, spatial...), context classifier and design dials |
| `visual-polish` | "Looks ugly, fix it": the Ten Fixes rules with measurement scripts; audit / fix / build modes |
| `ui-design-system` | Audit, document or extend tokens and components across a codebase |
| `ui-critique` | Structured visual feedback, 100-point scored audit, style fidelity |
| `ui-stack-laravel` | Blade, Livewire 4, Flux v2, Filament themes, Alpine, Tailwind v4 / Bootstrap 5 tokens, `wire:ignore` for canvas and Fabric.js, preserving Laravel conventions |
| `ui-stack-next` | Tailwind v4 `@theme`, Radix primitives and focus, server vs client boundaries, lucide, reduced motion |
| `ui-handoff` | Engineering spec with stack-aware notes |
| `ui-theming` | 10 presets, custom themes, Anthropic brand (restricted) |
| `ui-canvas-art` | Posters and static art with 29 bundled OFL font families |

Manual only (hidden from auto-routing): `ui-plan`, `ui-build`, `ui-system`, `ui-theme`,
`polish-audit`, `polish-fix`, `polish-new`.

Typical chain for a feature: **(user-first-ux: research, flow) -> visual direction -> stack build
-> (user-first-ux: copy, accessibility) -> critique -> visual polish -> design system -> handoff.**

## Visual polish (Ten Fixes)

| # | Rule | Target |
|---|------|--------|
| 01 | Hierarchy | one hero, ≥ 3× body (20 px → 76 px) |
| 02 | Alignment | one left edge (6 → 1) |
| 03 | Spacing | 4 · 8 · 12 px rhythm (5 → 3) |
| 04 | Text style | no caps, italics, underlines for emphasis (5 → 1) |
| 05 | Colour | neutral text, one accent (4 → 1) |
| 06 | Contrast | the user-first-ux floor, aim higher for secondary text (1.9 → 6.7) |
| 07 | Icons | one style, one size (8 → 1) |
| 08 | Grouping | related items in cards (0 → 2) |
| 09 | Show, don't list | ranges as bars |
| 10 | Make it alive | background reflects the data |

| Script (`skills/visual-polish/scripts/`) | What it measures | Needs |
|---|---|---|
| `ui_lint.py` | font sizes, spacing values & off-grid, caps/italic/underline, weights, text hues, approximate contrast, icon libraries & emoji, text ranges | Python 3 |
| `contrast.py` | WCAG ratio; `--suggest --target 7` finds the nearest passing colour | Python 3 |
| `dom_probe.js` | rendered edges, real contrast on real backgrounds, icon sizes, surfaces | any browser |
| `playwright_probe.mjs` | runs the probe + screenshot headlessly | `npm i -D playwright` |

Try it on the bundled pair: `skills/visual-polish/assets/sample-before.html` (fails 6 rules, warns
on 2) vs `skills/visual-polish/assets/reference-card.html` (passes all measurable ones).

## Agents (read-only)

| Agent | Role |
|---|---|
| `ui-critic` | Runs the critique framework; returns a severity-ranked table |
| `ui-ten-fixes-auditor` | Runs visual-polish audit mode with the scripts; scored, evidence-backed table |
| `design-system-auditor` | Grep pass for hardcoded hex, arbitrary Tailwind values, inline styles, off-grid spacing; fills the audit template |

## Hook (warn only)

`hooks/check-tokens.sh` runs after `Edit` / `Write` / `MultiEdit` on `*.blade.php`, `*.tsx`,
`*.jsx`, `*.css`, `*.scss` (skipping `vendor/`, `node_modules/`, `public/build/`, `storage/`,
`resources/views/vendor/`, `.next/`, `*.min.css`). It never blocks: findings go to Claude as
context, and you see a one-line summary. Set `UI_STUDIO_HOOK=off` to silence it.

| Check | Files | Known false positives |
|---|---|---|
| Hardcoded hex outside token definitions | all | fragment links not using `href=`; hex in strings that are not colours |
| Arbitrary Tailwind values (`p-[13px]`) | markup | legitimate geometry such as `grid-cols-[auto_1fr]` |
| Inline `style` (custom-property-only styles allowed) | markup | dynamic geometry (progress bars, canvas sizing) |
| Outline removed with no `focus-visible` in the file | all | focus styles defined in a base layer elsewhere |
| 3+ elements with hover scale/translate/shadow | markup | genuinely interactive lists |
| `transition-all` / `transition: all` | all | rare |
| Spacing px off the 4pt grid (>2px) | css/scss | intentional optical tweaks |
| `<canvas>` in a Livewire view without `wire:ignore` | blade | plain Blade views that happen to use `wire:` |
| Zoom disabled in viewport meta | markup | none known |
| Positive `tabindex` | markup | none known |

## Shared references

`references/shared/`: `visual-system.md` (owner of every token value: H, L, S, T, C, E, I, M1),
`principles.md` (DP1-DP8), `ai-defaults.md` (AD1-AD10), `quality-floor.md`, `connectors.md`, and
three pointer files to user-first-ux: `priority-workflow.md` (also the rule-ID index),
`severity.md`. Skills link to these; they are not copied into skills.

## Extending

- New skill: `skills/<name>/SKILL.md` (frontmatter `name` = folder name, description under
  1024 chars with triggers and exclusions naming neighbouring skills), body under ~200 lines,
  detail in `skills/<name>/references/`. Link shared rules with
  `${CLAUDE_PLUGIN_ROOT}/references/shared/...`.
- New command: a skill with `disable-model-invocation: true` and an `argument-hint`.
- New hook rule: add a block to `hooks/check-tokens.sh` that appends via `add`; keep it
  warn-only and document its false positives in the table above.
- Trigger tests: `evals/` (run with `claude plugin eval ui-studio@afyz-forge`).
- Validate: `claude plugin validate ./plugins/ui-studio` and `claude plugin validate .`.

## Licence and attribution

Apache-2.0. Upstream skills, rewrite policy and font licences: [NOTICE.md](NOTICE.md) and
`licenses/`.
