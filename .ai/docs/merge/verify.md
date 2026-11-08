# Phase 5 — Verify

TARGET `c:\laragon\www\afyz-forge` · SOURCE `c:\laragon\www\ai-skills` · run 2026-11-08.
Every check below ran against TARGET. Raw outputs sit next to this file.

## 0. SOURCE untouched — **one harness-written file changed; all content identical**

Recomputed `find ai-skills -type f -not -path '*/.git/*' -exec sha256sum {} + | sort -k2` and
diffed it against `source-checksums.txt` (1,269 files): [source-checksum-diff.txt](source-checksum-diff.txt).

- **1,266 of 1,269 files are byte-identical**, including every plugin, doc and `.ai/` file.
- **1 file differs: `ai-skills/.claude/settings.json`.** No command in this task wrote to it.
  Claude Code itself appends a `permissions.allow` entry there each time you choose "always
  allow" at a permission prompt; its newest entries are the exact commands from this session.
  The file is gitignored local runtime state, was never part of the repo, and was excluded from
  the merge. (The other 2 files under `.claude/` are unchanged.)
- Strictly, the diff is therefore **not empty**. To make the next check pass exactly, approve
  prompts with "allow once", or exclude `.claude/` from the checksum command.

## 1. Validation — pass

- `claude plugin validate --strict` (Claude Code 2.1.316) **passed** for the marketplace (`.`) and all
  9 plugins: user-first-ux, ui-studio, orbit-design-engine, session-orchestrator, system-design, and
  the 4 stubs. Output: [validate-output.txt](validate-output.txt).
- Advice only (does not change the verdict): the 4 stub READMEs have no install line. That is
  deliberate; nobody should install a stub.
- All 25 JSON files in TARGET (outside `_incoming/`) parse, including `marketplace.json` (name
  `afyz-forge`, 9 entries).

## 2. Single owner — pass with listed exceptions

Grep of every owned number across user-first-ux, ui-studio, orbit-design-engine and the stubs:
[single-owner-hits.md](single-owner-hits.md).

| Number | Owner hits | Pointer fallback lines | Other hits |
|---|---|---|---|
| 4.5:1 | 2 (UF `accessibility.md`) | 16 | 0 |
| 3:1 | 4 | 16 | 0 |
| 18.66 | 2 | — | 0 |
| 24×24 | 3 | 16 | 0 |
| 44 (house floor) | 3 | — | 5 |
| ~7:1 | 1 | — | 0 |
| 4 · 8 · 12 | 3 (ui-studio `visual-system.md`, `visual-polish`) | — | 1 |
| 150-300 ms | 1 (`visual-system.md`) | — | 0 |
| 12/14/16/20 scale | 1 | — | 0 |
| 1.2-1.25 ratio | 1 | 2 | 2 |

"Other" hits, all kept on purpose:
- `user-first-ux/skills/user-first-ux/evals/evals.json:105,111` and `…/ux-laws/evals/evals.json:7,12`
  (44px) and `…/user-first-ux/evals/evals.json:50,57` (1.2-1.25): eval expectations, i.e. test
  fixtures that check agent output, not rule statements.
- `user-first-ux/…/examples/avatar-stack.md:30`: `min-block-size:44px` inside an example's CSS.
- `ui-studio/README.md:79`: the README's Ten Fixes summary table.
- Measurement scripts implement the thresholds as constants: `contrast.py` (4.5, 3.0, 7),
  `ui_lint.py` (4.5), `dom_probe.js` (4.5, 3, 18.66, 24). Scripts must compute something;
  changing them would break the verified baseline.

## 3. Paths — pass

- 408 backticked paths checked ([pathcheck-output.txt](pathcheck-output.txt)). **0 broken
  links.** The remaining "unresolved" lines are prose that names the other plugin's files by skill
  (allowed), placeholders (`skills/<name>/`), project paths (`resources/`, `.next/`, `pages/`),
  repo-root paths in NOTICE files, and `/` fragments.
- A strict pass (every `../` path resolved from the file's own folder) found 6 broken links I had
  written in `principles.md` and `accessibility.md`. They were fixed and re-checked: 0 remain.
  (`system-design/README.md:40` is a pre-existing `...` placeholder.)
- All `${CLAUDE_PLUGIN_ROOT}` references (SKILL.md files, agents, hooks.json) resolve inside their
  plugin. The 41 that reference files had carried were converted to relative paths, per the repo
  convention that only SKILL.md files use the variable.
- **0 cross-plugin paths**: no file references `plugins/<other>/`, and no relative path leaves its
  plugin.

## 4. Scripts — pass

Ran from `plugins/ui-studio/skills/visual-polish/` ([post-merge-scripts.txt](post-merge-scripts.txt))
and diffed against [baseline-scripts.txt](baseline-scripts.txt):

| Target | Before merge | After merge |
|---|---|---|
| `assets/sample-before.html` | 6 fail (01,03,04,05,06,07), 2 warn (02,09), 2 manual | identical |
| `assets/reference-card.html` | 6 pass, 4 manual | identical |
| `contrast.py #3b4658 #101a2c --suggest` | 1.83:1 fail, suggest #9aa6bb (7.1:1) | identical |
| `contrast.py #b4bfcf #0b1220` | 10.07:1 pass | identical |

The only differences are the path labels (`ui-audit/assets/` → `assets/`). The C9 change in
`ui_lint.py` (two font families no longer warn) does not affect either sample, since both use one
family. `playwright_probe.mjs` was not run: Playwright isn't installed here (not verified).

## 5. Sizes — pass

All 55 SKILL.md files: [skill-sizes.md](skill-sizes.md). Largest 266 lines; none above 500. Every
`name` matches its folder, and every description is between 1 and 1,024 characters. The only file
over 300 lines is `visual-polish/references/rules.md` (304), which opens with a contents list.

| Skill | Lines | | Skill | Lines |
|---|---|---|---|---|
| user-first-ux | 153 | | visual-polish | 212 |
| ux-laws | 224 | | ui-styles | 120 |
| ui-accessibility | 57 | | ui-visual-direction | 99 |
| ui-ux-copy | 69 | | ui-design-system | 84 |
| ui-research | 53 | | ui-critique | 62 |
| ui-a11y / ui-copy | 12 / 11 | | polish-audit / fix / new | 15 / 12 / 11 |

## 6. Trigger test (reasoned from the descriptions; `claude plugin eval` not run)

| Prompt | Fires | Other descriptions that also match | Verdict |
|---|---|---|---|
| "Review the signup form for usability problems" | user-first-ux ("review this form/flow for usability") | orbit-ui-auth-forms mentions sign-up *redesigns* (weak); ui-critique now ends "Not for usability … use user-first-ux" | OK, mild |
| "Does this checkout use any dark patterns?" | user-first-ux (quoted trigger) | orbit-ui-trust-consent-ux now ends "Not for a general dark-pattern … review — use user-first-ux" | OK |
| "Apply Hick's law to this menu" | ux-laws (quoted trigger) | none | OK |
| "Is this modal accessible?" | ui-accessibility (user-first-ux plugin) | none (user-first-ux no longer lists WCAG in its triggers) | OK |
| "Write the empty state and error messages in BM and EN" | ui-ux-copy (user-first-ux plugin) | user-first-ux lists "errors" as a topic. Same plugin, so the plugin-level expectation holds | **Ambiguous inside user-first-ux** |
| "This dashboard looks ugly, fix it" | visual-polish (quoted trigger) | ui-visual-direction no longer says "make it look good"; orbit-ui-dashboards now requires a reference | OK |
| "Audit spacing and typography consistency in our components" | **ui-design-system** (picked: "across the codebase or component library", "off-scale spacing") | visual-polish sharpened: "Not for codebase-wide token audits" | OK |
| "Build a member profile card in Blade + Flux" | **ui-stack-laravel** (Blade, Flux) | `ui-build` is a manual command (`disable-model-invocation`), so it cannot fire; run `/ui-studio:ui-build` for the full loop | **Expected skill differs** |
| "Set up design tokens for a Next.js app" | ui-stack-next ("Tailwind v4 @theme tokens") | ui-design-system ("token naming") is audit/document/extend, not setup | OK, mild |
| "Critique this mockup" | ui-critique (quoted trigger) | none | OK |
| "Write the dev handoff spec for this screen" | ui-handoff | none | OK |
| "Design the architecture for a ticketing system" | system-design | no UI description mentions architecture or ticketing | OK |

## 7. Agent infrastructure — pass

- All 4 SOURCE `.ai/` files exist in TARGET. There is no root `agents/`, `CLAUDE.md` or `AGENTS.md` in SOURCE.
- Changed lines: architecture.md 124, context.md 79, conventions.md 30, publishing.md 21. Each
  edit falls in the categories of plan §3.6 (repo/marketplace rename, layout, plugin names,
  ownership rules, install lists).
- Remaining `ai-skills` references in TARGET are intentional: migration notes (`MIGRATION.md`,
  `CHANGELOG.md`, `README.md`, `context.md`), history-labelled docs (`docs/ARCHITECTURE.md`,
  `docs/CATALOG.md`), and **system-design** (`plugin.json` homepage, README install lines). That
  plugin was out of scope; see the open question in the handoff.

## 8. No git — pass

`find . -name .git` in TARGET: nothing. No git command was run in either project.

## 9. Coverage — pass

Regenerated [merge-map.md](merge-map.md) (1,290 rows, 0 unmapped) and checked every row against
TARGET:
- keep and move targets all exist;
- moved and merged sources are gone from their old place;
- deleted and excluded paths are absent.

**0 problems.** Totals: keep 470, move 97, merge-into 39, delete 40, replace-with-pointer 6,
exclude 638 (`.claude-flow`, `.claude`, `.impeccable`, `_source`, gitignored `evals/results`,
`ui-ten-fixes.zip`).

New files that no row produced, all planned: `MIGRATION.md`, `CHANGELOG.md`; READMEs for the 4
stubs; user-first-ux `README.md`, `NOTICE.md`, `licenses/frontend-design.txt` (attribution that
moved with three skills); `skills/ux-laws/references/stack-notes.md` (split out of the ux-laws
SKILL.md).

## Notes and deviations

- **ASCII rule vs pointer format.** `conventions.md` asks for ASCII-only skill files, but the
  prompt's exact pointer form uses `≥`, `×` and `—`. The prompt's form wins for the pointers.
  New descriptions I wrote use ASCII (`-`, `->`).
- **Removed `evals/results/`** run output (22 files) from session-orchestrator and system-design.
  It is gitignored local output, never in the repo; mapped as `exclude`.
- **Not verified here:** `claude plugin eval` trigger runs, the Playwright probe, and how the
  skills behave in a real project.

## Addendum 2026-11-08 — stubs and `_incoming/` removed (owner request after verify)

- Deleted `plugins/ux-laws`, `plugins/ui-ten-fixes`, `plugins/omni-design`,
  `plugins/ultimate-design-suite` (empty stubs) and `_incoming/`. The new marketplace name means
  nobody installs the old names from it; `MIGRATION.md` carries the mapping. This overrides plan
  §3.5 (one-release stubs).
- Updated: `marketplace.json` (5 plugins), `README.md`, `MIGRATION.md`, `CHANGELOG.md`,
  `docs/ARCHITECTURE.md`, `docs/CATALOG.md`, user-first-ux `README.md`, `.ai/agents/*`,
  `.gitignore` (dropped `_incoming/`), git-01/02/03 (no stub commit or tags; 7 commits).
- Re-checked: `claude plugin validate --strict` passes for the marketplace and all 5 plugins;
  merge map regenerated (1,290 rows, 0 unmapped; the stub manifests are now `delete`) and
  coverage shows 0 problems.
