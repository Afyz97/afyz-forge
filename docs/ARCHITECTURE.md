# Architecture

> **Status 2026-11 — the content below this note is historical.** It describes the earlier
> omni-design / ultimate-design-suite architecture. Those plugins were merged and removed. The
> current structure (two UI plugins split by job — `user-first-ux` and `ui-studio` — plus
> `orbit-design-engine`, `system-design`, `session-orchestrator`) is documented in
> `.ai/agents/architecture.md`, the root `README.md` and `MIGRATION.md`.

> **Repo-level note (current state).** This repository is now a Claude Code marketplace named
> `ai-skills` that ships **two independent plugins** under `plugins/`:
> `omni-design` (one comprehensive, self-contained design skill) and `ultimate-design-suite`
> (the modular router-plus-specialists approach described below). They are two architectures of
> the same capability; users install whichever they prefer, or both. For the repo-wide layered
> view (repo → marketplace → plugin → skill) and conventions, see
> [`.ai/agents/architecture.md`](../.ai/agents/architecture.md). **This document explains the
> _suite's_ internal rationale** — why *it* splits design into multiple cooperating skills.

## Why multiple skills instead of one

A single "design" skill has to be simultaneously a router, a foundations text, a token
system, ten style manuals, and a reviewer. In practice that produces a bloated file that
agents skim and a default "modern gradient SaaS" output — the exact failure this suite
exists to prevent. Splitting the problem gives four wins:

1. **Progressive disclosure.** Only the relevant style manual loads for a task. The agent
   isn't carrying skeuomorphism guidance while building a bento grid.
2. **Separation of concerns.** Routing (which style, brand vs product) is a different job
   from executing a style, which is different again from *reviewing* it. An independent
   reviewer that didn't write the code catches more.
3. **Strong, specific triggers.** Each style's `description` carries its own vocabulary and
   aliases, so "soft UI" reaches neumorphism and "frosted glass" reaches glassmorphism —
   without every design word activating every style.
4. **Portability + DRY.** Each style skill is self-sufficient (carries condensed
   essentials), while deep shared logic (anti-slop, brand-vs-product, accessibility,
   compatibility) lives once in `skills/_shared/` and is cross-linked.

## Layers

```
ultimate-design (router / lead)
      │  classifies brand vs product, chooses/adapts style, decides when NOT to
      ▼
design-foundations ── design-system-engineering ── design-motion   (always-available support)
      │
      ▼
one of 10 style specialists  ── applies the chosen design language
      │
      ▼
design-review (independent)  ── findings: severity · evidence · fix · style-impact
      │
      ▼
scripts/design-audit.mjs     ── mechanical smell signals (optional, deterministic)
```

Shared references (`skills/_shared/`): `anti-ai-slop.md`, `brand-vs-product.md`,
`style-compatibility.md`, `accessibility-baseline.md`.

## Directory tree

```
ai-skills/
├── README.md
├── LICENSE
├── .gitignore
├── .ai/agents/                   # agent context: architecture, conventions, context, publishing
├── .claude-plugin/
│   └── marketplace.json          # marketplace "ai-skills" → lists the two plugins via source paths
├── plugins/
│   ├── omni-design/                          # PLUGIN (name == folder)
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/omni-design/               # ONE self-contained skill
│   │       ├── SKILL.md · README.md · SOURCES.md · CHANGELOG.md
│   │       ├── references/ (22)  styles/ (11)  workflows/ (8)
│   │       └── adapters/ (5)  checklists/ (6)  tests/ (3)
│   └── ultimate-design-suite/                # PLUGIN (name == folder)
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── _shared/                      # cross-skill references (not a skill itself)
│           │   ├── anti-ai-slop.md · brand-vs-product.md
│           │   ├── style-compatibility.md · accessibility-baseline.md
│           ├── ultimate-design/SKILL.md      # router
│           ├── design-foundations/ · design-system-engineering/
│           ├── design-motion/ · design-review/
│           └── design-{skeuomorphism,neumorphism,glassmorphism,claymorphism,
│                        minimalism,maximalism,brutalism,liquid-glass,
│                        bento-grid,spatial-ui}/SKILL.md   # 10 style specialists
├── scripts/
│   └── design-audit.mjs          # deterministic smell auditor (no deps) — shared tooling
├── evaluations/
│   ├── EVALUATIONS.md            # trigger + scenario test cases
│   ├── RUBRIC.md                 # scored design-quality rubric
│   └── fixtures/bad-sample.css   # auditor test fixture (intentionally bad)
└── docs/
    ├── ARCHITECTURE.md · CATALOG.md · RESEARCH.md · EVALUATION-REPORT.md
    ├── ultimate-design-skills-prompt.md      # the suite's original master brief
    ├── ultimate-design-single-skill-prompt.md
    └── omni-design-master-prompt.md          # omni-design's master brief
```

> Each plugin is self-contained. `omni-design` has no external dependencies. The suite's style
> skills reference `../_shared/…` relative to `skills/<skill>/`, so `_shared/` must stay a sibling
> of the style skills inside `plugins/ultimate-design-suite/skills/`.

## Design decisions

- **Descriptions describe what + when + aliases, never a workflow summary.** A description
  that summarizes steps gets followed *instead of* the skill body (a documented Superpowers
  finding). Style descriptions front-load vocabulary and explicitly list non-UI exclusions
  so "minimal API" / "brutal error" / "glass table (SQL)" don't misfire.
- **Portability over centralization, with a shared core.** Each style SKILL.md carries the
  critical anti-slop and brand/product essentials inline so it works installed alone; the
  full versions live in `_shared/` for depth. `_shared` travels with the suite.
- **Accessibility and usability outrank style purity** — a hard rule in every style skill,
  enforced hardest in neumorphism and glass/liquid-glass. Encoded, not implied.
- **The reviewer is independent and evidence-based** — three verdict classes (objective
  defect / likely defect / preference) keep reviews honest and prevent taste being reported
  as defect (or vice-versa).
- **Determinism stays humble** — the auditor flags only mechanical smells and always labels
  them signals, documenting false-positive risk per rule. It never claims to lint taste.

## Distribution

- **Published** at `Afyz97/ai-skills` as a Claude Code marketplace named `ai-skills`.
- **Claude Code plugin/marketplace (primary):**
  ```
  /plugin marketplace add Afyz97/ai-skills
  /plugin install omni-design@ai-skills             # the single comprehensive skill
  /plugin install ultimate-design-suite@ai-skills   # the modular suite
  ```
  Each plugin is defined by `plugins/<name>/.claude-plugin/plugin.json` and mapped from
  `.claude-plugin/marketplace.json` via `plugins[].source: "./plugins/<name>"`. Convention:
  **plugin folder name == plugin `name` == marketplace entry name** (see `.ai/agents/conventions.md`).
- **Portable Agent Skills remain the source of truth** — each skill folder under a plugin's
  `skills/` is agent-agnostic; nothing is Claude-only. Manual install: copy a skill folder from
  `plugins/<plugin>/skills/<skill>/` into your agent's skills directory (keep `_shared/` with the
  suite's style skills).
- **`npx skills add Afyz97/ai-skills`** — generic installer; verify it discovers skills under the
  `plugins/<plugin>/skills/` layout before relying on it (tracked in `.ai/agents/context.md`).
- **Adding another plugin** (design or not) follows the repeatable recipe in
  `.ai/agents/conventions.md`: new `plugins/<name>/` folder + `plugin.json` + `skills/`, then one
  `source` entry in `marketplace.json`.
