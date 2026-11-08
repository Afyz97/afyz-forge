# Task: Consolidate the ai-skills UI/UX plugins and remove redundancy

## Locations

| Name | Path | Access |
|---|---|---|
| `SOURCE` | `~/ai-skills` (GitHub: Afyz97/ai-skills) | **Read-only.** Never create, edit, move or delete anything here. |
| `TARGET` | `~/ai-skills-v2` (change this path if I give you another) | New project. All output goes here. |

`SOURCE` is a Claude Code plugin marketplace. Its catalog is at `.claude-plugin/marketplace.json`, and its plugins are in `plugins/<name>/`. All plugins are Apache-2.0.

The merge is built as a **new project** in `TARGET`. `SOURCE` stays exactly as it is, so it is the backup and the reference for comparing results.

Current UI/UX plugins: `omni-design`, `ultimate-design-suite`, `user-first-ux`, `ux-laws`, `ui-studio`.
Incoming (not yet in the repo): `ui-ten-fixes` (from `ui-ten-fixes.zip`).
Out of scope, do not touch: `system-design`.

## Goal

Reduce the UI/UX plugins to **two plugins, split by job**, with **exactly one owner per topic**:

| Plugin | Job | Absorbs |
|---|---|---|
| `user-first-ux` | How the UI should **behave** for users: priority order, accessibility (WCAG 2.2 AA), ethics and dark patterns, Laws of UX, Gestalt, UI states, flows, forms, microcopy, i18n/BM | `ux-laws` |
| `ui-studio` | How the UI **looks and is built**: tokens and design system, visual direction, visual polish (Ten Fixes), stack builds (Laravel Blade/Livewire/Flux/Filament, Next.js), critique, handoff | `ui-ten-fixes`, plus `omni-design` / `ultimate-design-suite` **if** Phase 2 shows they overlap |

Nothing useful is lost. Duplicates are deleted, not reworded. Every skill triggers on a distinct set of requests.

## Non-negotiable rules

- Follow **Read → Report → Plan → STOP for approval → Implement → Verify → Sync**. Do not edit anything before I approve the plan.
- **`SOURCE` is read-only.** Only read and copy from it. Before Phase 4, record a checksum list of `SOURCE` (`find ~/ai-skills -type f -not -path '*/.git/*' -exec sha256sum {} + | sort -k2`). In Phase 5, prove that nothing changed.
- **Skip git entirely.** Do not run any git command, read-only or not, in either project, and do not run `git init` in `TARGET`. Do not copy `SOURCE/.git` into `TARGET`. Write every git command I will need into markdown files under `TARGET/.ai/docs/prompts/` (see Phase 6).
- Moving this repo's own content between plugins is fine. Do not add new rules or new prose beyond what's needed for pointers, descriptions and conflict resolutions.
- Keep each `SKILL.md` under 500 lines. Push detail into `references/` with a table of contents for files over 300 lines.
- Never reference files across plugins by path. Plugins can be installed separately, so cross-plugin links go by **skill name** with a one-line fallback (see "Cross-plugin references").

---

## Phase 0 — Create the new project and migrate the agent setup

1. Create `TARGET`. Stop if it already exists and isn't empty.
2. **Migrate the agent infrastructure from `SOURCE` to `TARGET` unchanged:**
   - The whole `.ai/` directory, including `.ai/agents/`, `.ai/docs/` and any contract files.
   - The root `agents/` directory, if it exists.
   - The root agent entry files that point into `.ai/`, such as `CLAUDE.md` and `AGENTS.md`, if they exist. The `.ai/` contract depends on them.
   - Copy byte-for-byte. Then search the copied files for absolute paths or repo names that mention `~/ai-skills` or `SOURCE`. **List them in the report; do not edit them yet.** The Plan decides how to update them.
3. Read the migrated `.ai/` contract and follow its conventions (folder layout, report locations, HANDOFF format) for the rest of this task. Where it conflicts with this prompt, this prompt wins for the merge itself; note the conflict.
4. Unzip `ui-ten-fixes.zip` into `TARGET/_incoming/ui-ten-fixes/`. Do not register it in any `marketplace.json`.
5. Create `TARGET/.ai/docs/merge/` for this task's working files: inventory, report, plan and verify.

## Phase 1 — Read and inventory

For each of the five plugins plus `_incoming/ui-ten-fixes`, read every file and record:

1. Plugin metadata: `plugin.json` (name, version, description) and the `marketplace.json` entry.
2. Every component: skills (name, description, line count), commands, agents, hooks, `references/`, `scripts/`, `assets/`, `examples/`, `evals/`.
3. The **topics** each file defines rules for, and the **concrete values** it states. Values include contrast ratios, touch-target sizes, spacing grid, type scale, number of weights, radius, icon sizes, motion durations, Core Web Vitals and breakpoints.
4. Every internal path reference, and every use of `${CLAUDE_PLUGIN_ROOT}`.

Read everything from `SOURCE` (and from `TARGET/_incoming/ui-ten-fixes`). Save the inventory to `TARGET/.ai/docs/merge/inventory.md`.

## Phase 2 — Report (write `TARGET/.ai/docs/merge/report.md`)

1. **Overlap matrix:** topics as rows, skills as columns. Mark each cell `defines`, `restates`, `references` or `—`.
2. **Value conflicts:** every topic where two files state different numbers or rules. For example: spacing grid 4·8·12 vs an 8-pt scale, uppercase allowed vs banned, 24 px vs 44 px touch targets, 4.5:1 vs 7:1 targets. Quote file:line for each side.
3. **Trigger collisions:** pairs of skills whose descriptions would both fire on the same prompt. Give an example prompt for each pair.
4. **Verdicts for `omni-design` and `ultimate-design-suite`:** for each, say whether it is mostly duplicate (merge into `ui-studio`), partly unique (merge the unique parts), or a distinct job (keep separate). Support the verdict with the percentage of its topics already covered elsewhere and a list of what is unique.
5. **Unique assets** that must survive: scripts, hooks, agents, evals, examples, fonts, templates.

## Phase 3 — Plan (write `TARGET/.ai/docs/merge/plan.md`), then STOP

### 3.1 Ownership registry

Fill this in. Only the owner states the rule and its numbers. Every other skill points to the owner.

| Topic | Owner (plugin → skill → file) |
|---|---|
| Priority order, trade-off justification | user-first-ux |
| WCAG 2.2 AA: contrast, touch targets, focus, keyboard, motion safety | user-first-ux |
| Laws of UX (all 30) and Gestalt | user-first-ux → references/laws |
| Ethics and dark-pattern bans | user-first-ux |
| UI states matrix, forms, flows, microcopy, BM/EN localisation, PDPA | user-first-ux |
| Tokens: spacing scale, type scale, weights, colour palette, radius, icon sizes, elevation | ui-studio |
| Visual polish: Ten Fixes rules, measurement scripts, numeric targets | ui-studio → visual-polish |
| Stack build recipes (Laravel stack, Next.js) | ui-studio |
| Visual direction, critique, design-system audit, handoff | ui-studio |
| Laws-of-UX implementation notes for Blade/Livewire | user-first-ux → references/stack-notes |

### 3.2 Conflict resolutions

Resolve every conflict from Phase 2 with these rules, and record each decision and its reason:

- **Accessibility values:** the stricter value wins. The minimum and the recommended target are both stated, by user-first-ux only.
- **Token values (spacing, type, radius):** ui-studio's existing scale wins. Ten Fixes keeps its *counting* rules (for example "≤ 3 rhythm steps + 1 inset per component") but expresses them in ui-studio tokens.
- **Rules in tension:** user-first-ux's priority order breaks the tie (honest > accessible > usable > efficient > consistent > aesthetic).
- **If you can't resolve a conflict with these rules,** list it as an open question for me rather than choosing.

### 3.3 Merge map

Write a table with one row per `SOURCE` file: `SOURCE path → TARGET path → action → note`. Paths in `TARGET` mirror `SOURCE` (`plugins/<name>/…`, `.claude-plugin/marketplace.json`). Files not touched by the merge, such as `system-design` and the repo LICENSE, are copied as `keep`.

Actions:
- `move`: unchanged.
- `merge-into`: unique sections are appended to an existing file.
- `replace-with-pointer`: the duplicate text becomes a one-line reference to the owner.
- `delete`: a full duplicate.
- `keep`: stays in place.

Target layout (adjust names to match what already exists):

```
plugins/user-first-ux/skills/
  ux-build/        ux-review/        ux-laws-audit/   (from ux-laws)
  references/: priority-order, accessibility, laws/ (30 laws), gestalt, ethics,
               states, microcopy, localisation, stack-notes
plugins/ui-studio/skills/
  ui-build/  visual-polish/ (from ui-ten-fixes: rules + audit/fix/build modes + scripts)
  design-system-audit/  critique/  handoff/  visual-direction/
```

Ten Fixes specifics:
- Fold `ten-fixes-rules`, `ui-audit`, `ui-fix` and `ui-build` into **one** `visual-polish` skill with three modes (audit / fix / build). Merge `ui-build` with ui-studio's existing build skill if they overlap.
- Move its scripts to `visual-polish/scripts/`. Update every `${CLAUDE_PLUGIN_ROOT}` path.
- Replace the Rule 06 contrast thresholds with a pointer to user-first-ux, keeping the minimum fallback.
- Replace the Rule 08 and Rule 05 rationale with pointers to the ux-laws content (Common Region, Proximity, Von Restorff). Keep the numeric targets.
- Merge its `tokens.md` into ui-studio's token reference. Drop duplicates.
- Fold its `ui-ten-fixes-auditor` agent into ui-studio's existing read-only agents if one has the same role. Otherwise add it.
- Commands become `/ui-studio:polish-audit`, `/ui-studio:polish-fix` and `/ui-studio:polish-new`, or merge into existing commands if equivalents exist.

### 3.4 New descriptions

Write the new `description` for every remaining skill and both `plugin.json` files. Each description:
- Leads with the job.
- Lists its own triggers.
- Ends with "Not for X — use <skill>" for its nearest neighbour.

user-first-ux should trigger on: usability, flows, forms, accessibility, errors, onboarding, "is this good for users", UX review, laws of UX.

ui-studio should trigger on: look and feel, style, theme, tokens, design system, polish, "looks ugly/amateur", build a screen or component in a named stack, critique, handoff.

### 3.5 Deprecations

- `ux-laws` and `ui-ten-fixes` (and any absorbed design suites) are kept for **one release** as stubs:
  - The `plugin.json` description starts with "DEPRECATED — merged into <plugin>; uninstall this and install <plugin>."
  - The stub has **no skills, commands, agents or hooks** (so it can't compete for triggers), and only a README with the migration note.
- Write `MIGRATION.md` at the repo root with an old → new mapping for every skill and command.

### 3.6 Agent infrastructure updates

List every edit needed in the migrated `.ai/`, `agents/`, `CLAUDE.md` and `AGENTS.md` so they describe the new layout: path changes, plugin names, and skill names that were merged or renamed. Keep everything else as it is.

### 3.7 Versions

Bump `user-first-ux` and `ui-studio` by a minor version (a major version if any command name changes). Bump the stubs to `x.y.0-deprecated`.

**STOP here.** Show me the plan summary, the open questions and the merge map, and wait for approval.

---

## Phase 4 — Implement (after approval only)

1. Record the `SOURCE` checksum list to `TARGET/.ai/docs/merge/source-checksums.txt`.
2. Build `TARGET` from the merge map. Copy from `SOURCE`, then edit only the copies in `TARGET`. Go plugin by plugin: system-design (`keep`), user-first-ux, ui-studio, the stubs, then `TARGET/.claude-plugin/marketplace.json`.
3. Apply the ownership pointers. The pointer format is below.
4. Apply the agent-infrastructure updates from 3.6.

### Cross-plugin references

Use this exact form, so each plugin still works when installed alone:

```
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
```

Within the same plugin, use relative paths. Never use a path into another plugin.

## Phase 5 — Verify (write `TARGET/.ai/docs/merge/verify.md`)

0. **`SOURCE` untouched:** recompute the checksum list and diff it against `source-checksums.txt`. It must be identical.
1. **Validation:** all checks run against `TARGET`. `claude plugin validate` passes for every changed plugin and for the marketplace. `marketplace.json` parses.
2. **Single owner:** grep for each owned number (for example `4.5:1`, `24×24`, `44`, `4 · 8 · 12`, the type-scale values). It must appear only in its owner's files, or in the fallback lines inside pointers. List every hit.
3. **Paths:** check every relative path and every `${CLAUDE_PLUGIN_ROOT}` reference. Report zero broken links and zero cross-plugin paths.
4. **Scripts:** run `ui_lint.py` and `contrast.py` from their new location against `visual-polish/assets/sample-before.html` and `reference-card.html`. The results must match the pre-merge output (before: 6 fail / 2 warn).
5. **Sizes:** list the line count of every `SKILL.md`. None may exceed 500 lines.
6. **Trigger test:** for each prompt below, state which skill's description should fire and confirm that no other description also clearly matches. Flag any ambiguity.

| Prompt | Expected skill |
|---|---|
| "Review the signup form for usability problems" | user-first-ux / ux-review |
| "Does this checkout use any dark patterns?" | user-first-ux |
| "Apply Hick's law to this menu" | user-first-ux / ux-laws-audit |
| "Is this modal accessible?" | user-first-ux |
| "Write the empty state and error messages in BM and EN" | user-first-ux |
| "This dashboard looks ugly, fix it" | ui-studio / visual-polish |
| "Audit spacing and typography consistency in our components" | ui-studio / visual-polish or design-system-audit (pick one, sharpen the other) |
| "Build a member profile card in Blade + Flux" | ui-studio / ui-build |
| "Set up design tokens for a Next.js app" | ui-studio |
| "Critique this mockup" | ui-studio / critique |
| "Write the dev handoff spec for this screen" | ui-studio / handoff |
| "Design the architecture for a ticketing system" | system-design (no UI skill should fire) |

7. **Agent infrastructure:** every file in `SOURCE/.ai/` (and in `agents/`, `CLAUDE.md`, `AGENTS.md`) exists in `TARGET`. Files differ only by the edits listed in 3.6. No remaining reference points to `~/ai-skills` unless the plan says it should.
8. **No git:** `TARGET` contains no `.git` directory.
9. **Coverage:** every row of the Phase 1 inventory is accounted for in the merge map, as moved, merged, pointered, deleted or kept. Nothing is silently dropped.

## Phase 6 — Sync

- Update the README of each changed plugin, the repo README and `CHANGELOG.md`.
- Delete `TARGET/_incoming/` only after I confirm `verify.md`.
- **Write the git commands to files instead of running them**, in `TARGET/.ai/docs/prompts/`:
  - `git-01-init.md`: initialise `TARGET` as a repo, add the remote `Afyz97/ai-skills` (or a new repo, with both options shown), and add a `.gitignore` if needed. No commits in this file.
  - `git-02-commits.md`: one commit per logical change (system-design, user-first-ux, ui-studio, stubs, marketplace, agent infrastructure, docs), each with the exact `git add <paths>` and a Conventional Commit message.
  - `git-03-release.md`: version tags per plugin and the push commands. Also show how to replace the contents of the existing GitHub repo with `TARGET`, and how to publish it as a new repo instead. Mark the replacement as destructive.
  - Each file begins with a one-line purpose and the directory to run it from. Commands go in fenced `bash` blocks, in order, with nothing for me to fill in except the marked placeholders.
- End with a **HANDOFF** block (in the format of the migrated `.ai/` contract, if it defines one) containing:
  - the `TARGET` path and a tree of its top two levels;
  - files added, merged, pointered or deleted relative to `SOURCE` (counts and paths);
  - confirmation that `SOURCE` is unchanged (checksum diff empty);
  - open questions;
  - the paths of the three git files, in the order I should run them.
