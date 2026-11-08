# Migration: ai-skills → afyz-forge (2026-11)

The marketplace moved to a new repo and a new name, and the UI plugins were consolidated into two
plugins split by job: **user-first-ux** (how the UI behaves) and **ui-studio** (how it looks and
is built). `ux-laws`, `ui-ten-fixes`, `omni-design` and `ultimate-design-suite` no longer exist as
plugins; their content lives in those two.

## 1. Re-add the marketplace

```text
/plugin marketplace remove ai-skills
/plugin marketplace add Afyz97/afyz-forge
/plugin install user-first-ux@afyz-forge
/plugin install ui-studio@afyz-forge
```

Then uninstall any of `ux-laws`, `ui-ten-fixes`, `omni-design`, `ultimate-design-suite` you had.
`orbit-design-engine`, `system-design` and `session-orchestrator` keep their names
(`<plugin>@afyz-forge`).

## 2. Skills

| Old | New |
|---|---|
| `user-first-ux:user-first-ux` | `user-first-ux:user-first-ux` (unchanged) |
| `ux-laws:ux-laws` | `user-first-ux:ux-laws` |
| `ui-studio:ui-accessibility` | `user-first-ux:ui-accessibility` |
| `ui-studio:ui-ux-copy` | `user-first-ux:ui-ux-copy` |
| `ui-studio:ui-research` | `user-first-ux:ui-research` |
| `ui-studio:ui-visual-direction`, `ui-design-system`, `ui-critique`, `ui-handoff`, `ui-stack-laravel`, `ui-stack-next`, `ui-theming`, `ui-canvas-art` | unchanged |
| `ui-ten-fixes:ten-fixes-rules` | `ui-studio:visual-polish` (the rulebook) |
| `ui-ten-fixes:ui-audit` | `ui-studio:visual-polish` (audit mode) |
| `ui-ten-fixes:ui-fix` | `ui-studio:visual-polish` (fix mode) |
| `ui-ten-fixes:ui-build` | `ui-studio:visual-polish` (build mode) |
| `omni-design:omni-design` | `ui-studio:ui-styles` (classifier, dials, styles); public sites, reference-to-code, redesign and adapters → `ui-studio:ui-visual-direction`; 100-point audit → `ui-studio:ui-critique`; token architecture → `ui-studio:ui-design-system`; e-commerce, enterprise and mobile playbooks, forms, navigation, tables → `user-first-ux:user-first-ux` |
| `ultimate-design-suite:ultimate-design` | `ui-studio:ui-styles` |
| `ultimate-design-suite:design-minimalism`, `design-maximalism`, `design-brutalism`, `design-skeuomorphism`, `design-neumorphism`, `design-glassmorphism`, `design-claymorphism`, `design-liquid-glass`, `design-bento-grid`, `design-spatial-ui` | `ui-studio:ui-styles` (one file per style) |
| `ultimate-design-suite:design-foundations` | `ui-studio:ui-visual-direction` + the ui-studio visual-system reference |
| `ultimate-design-suite:design-motion` | `ui-studio:ui-visual-direction` (motion section) |
| `ultimate-design-suite:design-system-engineering` | `ui-studio:ui-design-system` |
| `ultimate-design-suite:design-review` | `ui-studio:ui-critique` |

## 3. Commands

| Old | New |
|---|---|
| `/ui-studio:ui-a11y` | `/user-first-ux:ui-a11y` |
| `/ui-studio:ui-copy` | `/user-first-ux:ui-copy` |
| `/ui-studio:ui-plan`, `ui-build`, `ui-system`, `ui-theme` | unchanged |
| `/ui-ten-fixes:ui-audit` | `/ui-studio:polish-audit` |
| `/ui-ten-fixes:ui-fix` | `/ui-studio:polish-fix` |
| `/ui-ten-fixes:ui-new` | `/ui-studio:polish-new` |

## 4. Agents

| Old | New |
|---|---|
| `ui-studio` `a11y-auditor` | `user-first-ux` `a11y-auditor` |
| `ui-studio` `ui-critic`, `design-system-auditor` | unchanged |
| `ui-ten-fixes` `ui-ten-fixes-auditor` | `ui-studio` `ui-ten-fixes-auditor` |

## 5. Rule changes you may notice

- Touch targets: AA minimum 24×24 px, **house floor 44×44 px** (was "aim for 44" in user-first-ux).
- Contrast: minimum unchanged; recommended about 7:1 for small secondary text.
- Missing empty/loading/error states are always at least **High** (ux-laws said Medium).
- ux-laws audits use the four-level severity scale (Critical/High/Medium/Low).
- Ten Fixes: two font families are allowed; links always keep a non-colour cue; Rule 10
  transitions follow ui-studio's 150-300 ms; the hero uses a single `--text-display` token.
