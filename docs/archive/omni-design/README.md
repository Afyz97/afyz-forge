# omni-design

**One** installable [Agent Skill](https://agentskills.io/specification) that gives an AI coding agent
senior-level, *adaptive* design judgment across the full spectrum of interface work — new UI,
redesign, audit, polish, design systems, accessibility, motion, mobile, enterprise/admin, dashboards,
public sites, e-commerce, and reference-to-code. It classifies the product/user/task context and
**adapts** — an enterprise console, a luxury brand site, a banking form, and a kids' app each get a
different, appropriate design, not one templated look.

Portable and framework-agnostic; works wherever Agent Skills are supported (Claude Code, Codex CLI,
and compatible agents). Extra depth for Laravel/Blade, React/Next, Vue/Nuxt/Svelte, and native mobile.

## Why one package (not a giant prompt, not ten skills)

The knowledge is large, so it uses **progressive disclosure**: a lean operational `SKILL.md` (role,
context classifier, style router, design dials, quality gates, and a reference map) loads on trigger;
everything deep lives in `references/`, `styles/`, `workflows/`, `adapters/`, and `checklists/`, loaded
**only when the task needs it**. A brutalist landing page never carries neumorphism guidance; a Laravel
admin redesign never loads spatial-UI. This keeps the agent's context small while the capability stays
broad.

## Package structure

```
omni-design/
├── SKILL.md            # operational core: classifier · router · dials · gates · reference map
├── README.md · SOURCES.md · CHANGELOG.md
├── references/         # foundations + domains + systems (22 files)
│   ├── design-foundations · typography · color · spacing-layout · responsive-design
│   ├── accessibility · motion · states · performance · content-design
│   ├── forms · navigation · tables-data-density · enterprise-dashboards
│   ├── public-websites · ecommerce · mobile-ui
│   └── design-systems · brand-to-ui · reference-to-code · design-audit · anti-slop
├── styles/             # style-router + 10 deep style files
│   └── minimalism · maximalism · brutalism · skeuomorphism · neumorphism
│       · glassmorphism · claymorphism · liquid-glass · bento-grid · spatial-ui
├── workflows/          # create · redesign · audit · polish · build-design-system
│   └── reference-to-code · mobile-design · enterprise-workflow-ui
├── adapters/           # overview · laravel · react-next · vue-nuxt-svelte · native-mobile
├── checklists/         # pre-design · implementation · accessibility · responsive · motion · release-gate
└── tests/              # scenarios · regression-prompts · trigger-tests
```

## How it works (the loop)

1. **Classify context** (silent) — product, user, task, density, expressiveness, trust, platform;
   brand vs product per surface.
2. **Inspect** existing UI (preserve what works; find the real problems).
3. **Set direction** — choose/adapt an aesthetic, set the design dials, name one distinctive move.
4. **System first** — tokens and states, then screens, in the project's actual stack.
5. **Validate** — responsive, accessibility, motion, performance.
6. **Review** — critique as if someone else built it; fix by severity.

## Key capabilities

- **Context classifier** — no single aesthetic imposed; density/trust drive most decisions.
- **Style router** — profiles for every named style + hybrid rules (one dominant + one supporting,
  property-ownership map). Deep files for the 10 hardest styles.
- **Design dials** — layout variance, density, motion, depth, brand expression, trust-conservatism;
  overridable in plain language ("more premium," "increase density").
- **Enterprise/admin strength** — preserves density, keeps tables as tables, respects permissions;
  Laravel/Blade priority adapter.
- **Anti-AI-slop engine** — reason-based, not shape-banning.
- **Accessibility as a hard gate** (WCAG 2.2-aligned) — never overridden by style.
- **100-point scored audit** with severity-ordered fixes.
- **Framework adapters** — Laravel, React/Next, Vue/Nuxt/Svelte, native mobile.

## Installation

Standard Agent Skill. Copy this `omni-design/` folder into your agent's skills directory:

- **Claude Code** — `~/.claude/skills/omni-design/` (personal) or `.claude/skills/omni-design/`
  (project).
- **Other agents** — wherever they load Agent Skills from; the folder is self-contained.

The skill activates automatically on UI/design requests via its `description`. No configuration needed.

> If/when this repository is published, `npx skills add OWNER/REPO` works too — `OWNER/REPO` is a
> placeholder until a real published location exists; don't run it verbatim.

## Usage examples

```
Use omni-design to redesign this Laravel admin page. Preserve all functionality and optimize
for expert operational use.
```
```
Use omni-design to audit this checkout flow. Prioritize accessibility and conversion without
dark patterns.
```
```
Use omni-design to create a premium public website. Layout variance 7/10, motion 4/10, density 3/10.
```
```
Use omni-design with 60% minimalism, 25% bento, 15% liquid glass.
```

## Modes

- **Audit** — `workflows/audit-ui.md` + `references/design-audit.md` (100-pt scored, severity-ranked).
- **Redesign** — `workflows/redesign-existing-ui.md` (preserve-first).
- **Design system** — `workflows/build-design-system.md` (extract before invent).
- **Create / polish / mobile / enterprise / reference-to-code** — the matching `workflows/` file.

## Limitations

- No live app ships here, so rendered browser/visual validation isn't performed in this package; the
  checklists and audit stand in until the skill is applied to a real project (render real viewports
  when browser tooling exists).
- `liquid-glass` and `spatial-ui` describe fast-moving Apple platform material — verify current HIG /
  visionOS guidance before native implementation.
- Accessibility guidance is WCAG 2.2-aligned; **never claim conformance from inspection alone** — the
  skill states what it verified.
- The skill encodes judgment, not taste-linting — it can't guarantee a design is *good*, only steer
  strongly away from the common failure modes.

## Attribution & license

Apache-2.0. Guidance is original and synthesized — no copied text, rule databases, or proprietary
palettes from any studied project. Sources studied and how they influenced the design:
[SOURCES.md](SOURCES.md).
