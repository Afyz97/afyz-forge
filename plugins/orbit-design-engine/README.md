# Orbit Design Engine (ODE) — UI/UX & Motion Skills v8.0

**A project-agnostic UI/UX design engine with 26 specialized skills for Claude Code and Codex.**

The design engine is branded to fit the Orbit / AI-OS family, but it is **not tied to Orbit-HQ**: install in any Laravel, React or other web application. It turns real visual/motion references into actionable design and implementation guidance.

## What it contains

- **Visual design:** existing-system theme inheritance, spacing, density, typography, component states, dashboards, navigation, accessibility and responsive behaviour.
- **Operational motion:** micro-interactions, metrics, charts, Kanban drag/drop, calendar and filters, notifications, theme switching.
- **Cinematic motion:** kinetic text, layered floating cards, transitions, coordinated onboarding scenes, optional mascot, progress storytelling.
- **Quality assurance:** match reference **geometry and motion, not its palette**; test existing-theme preservation, reduced motion, keyboard/touch, responsive layouts and data integrity.

### Reference origins (for clarity; not plugin branding)

1. **Enterprise website sample** provided by the user (Kinlo): page and design language. Its live JavaScript UI was not fully rendered during the original audit; exact CSS/font/motion values were not measured. Read `REFERENCE-BRIEF.md` for the source URLs and verification limits.
2. **Short dashboard video** provided by the user (`299130.mp4`): interactive application animation reference. 13 frame captures included.
3. **Long-form animated checklist video** provided by the user: editorial/motion design reference. 25 keyframes and 3 sequence strips included. This is not proof of actual product controls or legal requirements.

4. **Six-second project-management workspace video**: KPI count-up and chart bar entrance, fixed-shell route switches to Tasks/Analytics/Settings, staged Kanban entries, and analytics counters reanimating on date-range selection. Additional `settings.js` code panel presents an optional accent swatch effect but does not visually demonstrate it executing. See `PROJECT-WORKSPACE-VIDEO-AUDIT.md`.

5. **Five-second login/signup animation video**: a two-way diagonal panel sweeps across a rounded card to exchange a sign-in-left / welcome-right arrangement for a welcome-left / registration-right arrangement, then back. The video displays illustrative HTML/CSS/JS; exact code, accessibility or backend behaviour are not verified. See `AUTH-VIDEO-AUDIT.md`.

All extracted clips/frames are internal design references; do not ship them as your application's images. Implementation code and motion tokens are original design interpretations, not a copy of any reference site's source code.

## Mandatory theme rule

**All 26 skills are colour-neutral.** They must discover and inherit the host app’s existing theme rather than introducing any particular palette. This includes components, analytics, charts, login/registration sweeps, settings, splash animations and examples. The screenshots are reference material for geometry and motion, **never palette instructions**. See `references/THEME-INHERITANCE.md`.

## Installation

**From the afyz-forge marketplace (Claude Code):**

```text
/plugin marketplace add Afyz97/afyz-forge
/plugin install orbit-design-engine@afyz-forge
```

After installation, ask to use `orbit-ui-director` for broad UI work, or a specific
`orbit-ui-*` skill for a focused task. The plugin includes all 26 skills and their
references, assets, examples and scripts; no Python installer is needed for this route.
Skills resolve the bundled resources relative to their own installed location.
Marketplace installation provides skills without adding persistent routing blocks
to your project's `AGENTS.md` or `CLAUDE.md`.

**Standalone installation (Claude Code and Codex):**

Unzip and open a terminal **inside `orbit-design-engine/`**. Requires Python 3, no additional packages.

**Per-project (Windows / Laragon):**

```powershell
py -3 install.py --project "C:\laragon\www\your-project" --target both --upgrade
```

**Global default (Claude Code and Codex, all projects):**

```powershell
py -3 install.py --scope user --target both --upgrade
```

**If you already installed the Kinlo-branded v4 package**, migrate safely:

```powershell
py -3 install.py --project "C:\laragon\www\your-project" --target both --upgrade --migrate-kinlo
```

`--migrate-kinlo` removes **only confirmed original, unedited v4 legacy skills** by SHA-256 content checks; preserves modified skills, older nested installs and the old `.ai/uiux/kinlo/` reference archive for your review. The old `CLAUDE.md` / `AGENTS.md` marked blocks are automatically replaced with the new Orbit blocks when rules are enabled, without deleting unrelated instructions. It is safe to rerun. For global legacy migrations use `--scope user --migrate-kinlo`.

`--target claude`, `--target codex`, `--no-rules` and `--scope project|user` are also supported.

## Project files created

```text
PROJECT/
├── CLAUDE.md                           # Orbit UI routing block; user content preserved
├── AGENTS.md                           # Orbit UI routing block; user content preserved
├── .claude/skills/orbit-ui-*/SKILL.md   # 26 standalone skills for Claude Code
├── .agents/skills/orbit-ui-*/SKILL.md   # 26 standalone skills for Codex
└── .ai/uiux/orbit/
    ├── AUTO-APPLY.md
    ├── MOTION-ROUTING.md
    ├── DESIGN-SPEC.md
    ├── MOTION-SPEC.md
    ├── reference and QA guides...
    ├── assets/                          # CSS tokens and video study frames
    ├── examples/auth-diagonal-wipe-demo.html
    ├── examples/editorial-motion-demo.html
    └── scripts/
```

User-scope installs use the same structure beneath your home folder, with `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` as instructions. Start a fresh agent session after installing if skill discovery is cached.

## Skills available

| Area | Skills |
|---|---|
| Coordination | `orbit-ui-director`, `orbit-ui-reference-audit` |
| Visual system | `orbit-ui-foundations`, `orbit-ui-app-shell`, `orbit-ui-components`, `orbit-ui-dashboards`, `orbit-ui-responsive` |
| Application motion | `orbit-ui-motion`, `orbit-ui-video-motion`, `orbit-ui-interactive-kanban`, `orbit-ui-team-filter-motion`, `orbit-ui-analytics-calendar`, `orbit-ui-personalization`, `orbit-ui-feedback-overlays` |
| Cinematic motion | `orbit-ui-motion-storytelling`, `orbit-ui-kinetic-type`, `orbit-ui-layered-cards`, `orbit-ui-mascot-motion` |
| Trust / compliance-related flow UX | `orbit-ui-trust-consent-ux` |
| Workspace motion | `orbit-ui-workspace-navigation`, `orbit-ui-metric-choreography`, `orbit-ui-project-workspaces` |
| Auth motion | `orbit-ui-auth-forms`, `orbit-ui-diagonal-wipe` |
| Verification | `orbit-ui-visual-qa`, `orbit-ui-motion-qa` |

## Example prompts

**Entire application:**

> Use `orbit-ui-director` to audit my application, unify its visual design and implement high-quality interactive UI across the requested pages. Apply appropriate motion design based on the reference library. Preserve existing functionality, routing, validation and role permissions. Verify appearance and interaction behaviour on desktop and mobile.

**Specific screen:**

> Use the Orbit Design Engine to redesign this dashboard. Include shared typography, real-data KPIs, smooth chart transitions, cards, animated feedback states and consistent navigation. Compare it with the reference frames and report what was actually tested.

**Landing and onboarding:**

> Use `orbit-ui-motion-storytelling`, `orbit-ui-kinetic-type` and `orbit-ui-layered-cards` for an expressive guided onboarding sequence. Apply staggered entrances, progress continuity, focus and reduced-motion states. Do not use cinematic autoplay on everyday admin screens.

**Motion verification:**

> Use `orbit-ui-motion-qa` to compare transition sequences rather than static snapshots, including entry, interaction, exit, interrupted animation and reduced-motion alternatives.

## Previously added project-management motion reference (v6)

**What is now covered:** fixed-shell route transitions and loading states, synchronized dashboard KPI + chart-bar entrances, progressive task-board cards, analytics counters/sparklines and 7D/30D/90D period transitions, and settings form entry. **Not demonstrated in the clip:** a swatch preference actually being changed (only code is displayed), functional drag-and-drop, exporting, persistence or reduced-motion support. Implementation targets in `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` are recommended values, not extracted proprietary source code.

There are 16 individual reference crops and 4 multi-frame motion strips in `assets/project-workspace-reference/`. An **original, interactive standalone example** is included at `examples/workspace-motion-demo.html` (no dependencies; mock values clearly labelled).

For this reference specifically ask: **“Use orbit-ui-workspace-navigation and orbit-ui-metric-choreography to bring my dashboards and route transitions close to the supplied short workspace video. Include intermediate-state checks and preserve backend functionality.”**

## What 'automatic' means

The installer adds concise persistent routing guidelines to project `CLAUDE.md` and `AGENTS.md` (or user-scope files). Agent models are **instructed** to consult relevant Orbit UI skills for future frontend tasks. This increases consistency but is **not a deterministic event hook** and cannot guarantee every response loads every skill. Backend-only tasks should not load the UI library. The installer never edits application source code, adds runtime dependencies or changes page styles by itself.

## Versioning and naming

- Plugin: **Orbit Design Engine** (ODE), package folder `orbit-design-engine`
- Skill prefix: `orbit-ui-*`
- Shared reference folder: `.ai/uiux/orbit/`
- Automatic instruction marker: `ORBIT-DESIGN-AUTO-APPLY`
- Latest release: **v8.0.0** (26 skills, previous references retained)

## Authentication-motion reference (v7)

The new user-supplied five-second video shows a **bidirectional diagonal panel** sweeping over a fixed, rounded login/signup card. The form and welcome copy exchange sides. Reference frames and a side-by-side transition strip live at `assets/auth-reference/`.

- `orbit-ui-auth-forms`: visual composition, actual login/registration UX, states, mobile, accessibility and backend preservation.
- `orbit-ui-diagonal-wipe`: two-way diagonal panel choreography, timing, state management and reduced motion.
- `AUTH-VIDEO-AUDIT.md`, `AUTH-TRANSITION-PLAYBOOK.md`, `AUTH-VISUAL-QA.md`: observed evidence, implementation techniques and visual QA.
- `examples/auth-diagonal-wipe-demo.html`: original runnable HTML/CSS/JS demo (no external packages; **local form validation only, no authentication backend**).

To apply this in your application: **“Use orbit-ui-auth-forms and orbit-ui-diagonal-wipe to redesign login and registration with the two-way sweeping diagonal panel from Reference E. Keep my real authentication flows, event branding, validation, accessibility and reduced-motion support.”**

These specialised skills should only activate for related screens, not every dashboard or CRUD form.

## Upgrade note — v8 theme-neutral change

The previous versions contained reference-inspired colour values in some CSS files and demos. Version 8 removes those values from all skill instructions, token sheets and runnable examples. All 26 skills enforce theme inheritance and never ask an agent to replicate reference colours. Production styling always defers to the **existing application's theme**. Reinstall with `--upgrade` to overwrite previous package-owned rules and assets; restart agents so older loaded skill instructions are not reused. Existing app source is not rewritten by the installer.
