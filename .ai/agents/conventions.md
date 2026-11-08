# Conventions — afyz-forge repo

Rules an AI agent must follow when editing or extending this repo. These are decisions already made;
honor them unless the user explicitly changes them.

## Naming (hard rules)

- **Plugin folder name == plugin `name` (in plugin.json) == marketplace `plugins[].name`.** All three
  must match, always. This is the traceability convention the repo owner requires.
- **Skill folder name == `SKILL.md` frontmatter `name`.** Required by the Agent Skills spec. `name` is
  lowercase `a-z0-9` + single hyphens, ≤64 chars.
- Marketplace `name` is `afyz-forge` (not the repo name, not a plugin name).

## Skill authoring rules

- `SKILL.md` frontmatter needs `name` and `description`; `description` **must be ≤1024 chars** (the
  spec cap — validate after editing). Keep the SKILL.md body operational and under ~500 lines; push
  depth into `references/` / subfolders (progressive disclosure).
- The `description` is the trigger. Front-load *what + when + aliases + exclusions*; do not write it as
  a workflow summary. Include negative triggers (e.g. ui-styles excludes "minimal API," "glass table
  (SQL)," etc.).
- Real content only in guidance — no fabricated metrics/examples. Guidance is original/synthesized;
  **no copied text, rule databases, or proprietary palettes** from other projects (see the skills'
  SOURCES.md / the repo docs/RESEARCH.md).
- ASCII/Latin text only in skill files (a stray CJK char slipped in once and had to be fixed).

## ui-studio specifics

- Commands are skills with `disable-model-invocation: true` (docs prefer skills over `commands/`).
- Severity scale is Critical / High / Medium / Low everywhere (`references/shared/severity.md`).
- WCAG target is 2.2 AA. Accessibility numbers are owned by user-first-ux
  (`skills/user-first-ux/references/accessibility.md`); ui-studio points to it.
- The hook is warn-only and must always `exit 0`; document new rules' false positives in the
  plugin README.
- Validate with `claude plugin validate --strict ./plugins/ui-studio`,
  `claude plugin validate --strict ./plugins/user-first-ux` and `claude plugin validate .`;
  test routing with `claude plugin eval ./plugins/<plugin> --ablation none`.

## One owner per topic (since 2026-11)

- Only the owner file states a rule and its numbers (registry: `.ai/docs/merge/plan.md` §3.1).
- Never reference another plugin by path. Cross-plugin pointer, exactly:
  `Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.`
  `Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.`
- A merged plugin is removed outright; record where its skills went in `MIGRATION.md`.
- Literal non-ASCII is allowed only where it is the data being described (AD5 tells).

## Manifest schema (Claude Code) — the gotchas that already bit us

- `marketplace.json` → `owner` **must be an object** `{ "name": ..., "url": ... }`, NOT a string.
- `plugin.json` → `author` **must be an object** too, NOT a string.
- `plugins[].source` is a **relative path** to the plugin folder, e.g. `./plugins/ui-studio`.
- Validate every JSON edit: `python -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json',recursive=True)]"`.

## Adding a new plugin (the repeatable recipe)

1. `mkdir -p plugins/<name>/.claude-plugin plugins/<name>/skills`.
2. Write `plugins/<name>/.claude-plugin/plugin.json` (name==`<name>`, object `author`, description with
   good triggers, license).
3. Put skills in `plugins/<name>/skills/<skill>/SKILL.md` (+ any references subfolders).
4. Add an entry to `.claude-plugin/marketplace.json` → `plugins[]`: `{ name, source: "./plugins/<name>",
   description, license }`.
5. Keep any shared references *inside* that plugin's `skills/` so relative links resolve when installed
   standalone. A plugin must be self-contained.
6. Commit, push, then `/plugin marketplace update Afyz97/afyz-forge` and `/plugin install <name>@afyz-forge`.

## Existing-project safety (applies when the SKILLS are used, and when editing this repo)

- Don't break the cross-references listed in `architecture.md` (user-first-ux sibling links,
  ui-studio `${CLAUDE_PLUGIN_ROOT}` links, system-design sibling links).
- Don't reintroduce the multi-skill single-plugin layout — the repo is now **plugins/<plugin>/skills/**.
- Keep `.claude-flow/`, `.claude/`, `.impeccable/` **untracked** (see `.gitignore`) — they are local
  runtime state and must never be published.

## Validation quick-commands

- Marketplace/plugin mapping: check each `source` folder has `.claude-plugin/plugin.json` + `skills/`
  with ≥1 `SKILL.md`, and that folder/plugin/entry names match.
- Description length: ensure each `SKILL.md` description ≤1024 chars.
- Link integrity: no reference points at a moved/removed file.

See `architecture.md` for structure, `publishing.md` for the release workflow.
