"""Generate the merge map: one row per SOURCE file (+ incoming ui-ten-fixes files).
Usage: python -I mergemap.py SOURCE_ROOT INCOMING_ROOT OUT_MD
Rules are ordered; first match wins. Unmatched files are reported as UNMAPPED (must be zero).
"""
import os, re, sys

SRC, INC, OUT = sys.argv[1:4]
UF, UI, UL = "plugins/user-first-ux/", "plugins/ui-studio/", "plugins/ux-laws/"
OD, US, TF = "plugins/omni-design/", "plugins/ultimate-design-suite/", "plugins/ui-ten-fixes/"
UFS = UF + "skills/user-first-ux/"
STY = UI + "skills/ui-styles/"
VP = UI + "skills/visual-polish/"
VD = UI + "skills/ui-visual-direction/references/"
VS = UI + "references/shared/visual-system.md"
TSM = VD + "typography-structure-motion.md"
OREF = OD + "skills/omni-design/references/"

SAME = object()
R = [
    # ---- root: local state and task inputs
    (r"^\.claude-flow/", None, "exclude", "gitignored local runtime state; stays in SOURCE"),
    (r"^\.claude/", None, "exclude", "gitignored local runtime state; stays in SOURCE"),
    (r"^\.impeccable/", None, "exclude", "gitignored local runtime state; stays in SOURCE"),
    (r"^_source/", None, "exclude", "gitignored ui-studio build input; never shipped"),
    (r"^ui-ten-fixes\.zip$", None, "exclude", "consumed: unzipped to _incoming, merged into ui-studio + stub"),
    (r"^ai-skills-merge-prompt\.md$", ".ai/docs/merge/ai-skills-merge-prompt.md", "move", "task record"),
    (r"^plugins/[^/]+/evals/results/", None, "exclude", "gitignored eval run output; stays in SOURCE"),
    (r"^\.ai/agents/", SAME, "keep", "edits per plan 3.6"),
    (r"^\.claude-plugin/marketplace\.json$", SAME, "keep", "edit: name/owner per Q8, descriptions, stub entries, add ui-ten-fixes stub, metadata 0.10.0"),
    (r"^README\.md$", SAME, "keep", "edit in Phase 6"),
    (r"^docs/(ARCHITECTURE|CATALOG)\.md$", SAME, "keep", "edit in Phase 6 (new layout)"),
    (r"^(LICENSE|\.gitignore|ui-design\.skill)$", SAME, "keep", ""),
    (r"^(docs|evaluations|scripts)/", SAME, "keep", ""),
    (r"^plugins/system-design/", SAME, "keep", "not touched by the merge"),
    (r"^plugins/orbit-design-engine/\.claude-plugin/plugin\.json$", SAME, "keep", "edit: repo URLs (Q2: dedicated plugin)"),
    (r"^plugins/orbit-design-engine/README\.md$", SAME, "keep", "edit: install commands"),
    (r"^plugins/orbit-design-engine/skills/orbit-ui-(director|foundations|components|dashboards|responsive|trust-consent-ux|visual-qa)/SKILL\.md$", SAME, "keep", "edit: description gains Not-for ending; responsive: target line -> pointer"),
    (r"^plugins/orbit-design-engine/", SAME, "keep", "dedicated plugin (Q2)"),
    (r"^plugins/session-orchestrator/(\.claude-plugin/plugin\.json|README\.md)$", SAME, "keep", "edit: repo URL / install commands (Q8)"),
    (r"^plugins/session-orchestrator/", SAME, "keep", "migrated unchanged"),

    # ---- user-first-ux (owner of behaviour)
    (r"^plugins/user-first-ux/\.(claude|codex)-plugin/plugin\.json$", SAME, "keep", "edit: version 1.1.0, new description (3.4), homepage"),
    (r"^plugins/user-first-ux/skills/user-first-ux/SKILL\.md$", SAME, "keep", "edit: description; Visual system + Design-system discipline -> pointers to ui-studio; load table adds sibling skills and domains/"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/accessibility\.md$", SAME, "merge-into", "receives WCAG criterion tables from ui-accessibility/wcag-22-aa.md, A11y-6 spacing exception + 2.4.12 note from ux-laws guardrails, 7:1 recommended (C2), 44 house floor (C1), focus >=2px recommended (C23)"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/components\.md$", SAME, "merge-into", "receives unique bullets from omni forms.md (F), navigation.md (SN), tables-data-density.md (TB)"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/states-feedback\.md$", SAME, "merge-into", "receives States-4 Partial (ux-laws), error altitude + 3 empty kinds wording (omni states.md); ST stays 'at least High' (C4)"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/ethics-privacy\.md$", SAME, "merge-into", "receives Ethics-4 truthful defaults/anchors/progress (ux-laws guardrails)"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/principles\.md$", SAME, "replace-with-pointer", "N/NO kept; G1-G3,G5 and U1-U17 rule text -> ID index pointing to ux-laws law entries (IDs preserved); G4 kept (no law equivalent)"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/visual-system\.md$", SAME, "replace-with-pointer", "H/L/S/T/C/E/M owned by ui-studio -> pointer + fallback; C3 and M2 (a11y) stay here verbatim"),
    (r"^plugins/user-first-ux/skills/user-first-ux/references/checklist\.md$", SAME, "keep", "edit line 16: '44px house floor' (C1)"),
    (r"^plugins/user-first-ux/", SAME, "keep", ""),

    # ---- ux-laws -> user-first-ux/skills/ux-laws ; plugin becomes stub
    (r"^plugins/ux-laws/\.claude-plugin/plugin\.json$", None, "delete", "plugin merged and removed (stubs dropped after verify, 2026-11-08)"),
    (r"^plugins/ux-laws/\.codex-plugin/plugin\.json$", None, "delete", "plugin merged and removed"),
    (r"^plugins/ux-laws/skills/ux-laws/SKILL\.md$", UF + "skills/ux-laws/SKILL.md", "move", "edit: description (3.4); 'if user-first-ux loaded' -> same plugin; Stack notes section -> references/stack-notes.md; R1/R2/R22 numbers -> pointers"),
    (r"^plugins/ux-laws/skills/ux-laws/references/guardrails\.md$", UF + "skills/ux-laws/references/guardrails.md", "replace-with-pointer", "A11y/Ethics/States sections -> pointers to ../../user-first-ux/references/{accessibility,ethics-privacy,states-feedback}.md; unique lines merged there first"),
    (r"^plugins/ux-laws/skills/ux-laws/references/audit-template\.md$", UF + "skills/ux-laws/references/audit-template.md", "move", "edit: severity -> 4-tier (C5)"),
    (r"^plugins/ux-laws/skills/ux-laws/references/laws-interaction\.md$", UF + "skills/ux-laws/references/laws-interaction.md", "move", "edit: Fitts target sizes -> pointer to accessibility.md A7 (C1)"),
    (r"^plugins/ux-laws/skills/ux-laws/references/laws-perception\.md$", UF + "skills/ux-laws/references/laws-perception.md", "move", "edit: Proximity '4/8px steps' -> pointer to ui-studio tokens + fallback (C6)"),
    (r"^plugins/ux-laws/skills/ux-laws/", lambda p: UF + p[len("plugins/ux-laws/"):], "move", ""),

    # ---- ui-studio: files moving to user-first-ux
    (r"^plugins/ui-studio/agents/a11y-auditor\.md$", UF + "agents/a11y-auditor.md", "move", "edit: skills preload user-first-ux:ui-accessibility; numbers -> pointer"),
    (r"^plugins/ui-studio/skills/ui-accessibility/references/wcag-22-aa\.md$", UFS + "references/accessibility.md", "merge-into", "criterion tables + target note merged; A1-A16 duplicate text deleted; file then deleted"),
    (r"^plugins/ui-studio/skills/ui-accessibility/", lambda p: UF + p[len(UI):], "move", "edit: \\${CLAUDE_PLUGIN_ROOT}/references/shared/* -> ../user-first-ux/...; connectors -> by name"),
    (r"^plugins/ui-studio/skills/ui-ux-copy/references/(content|inclusive-context)\.md$", None, "delete", "full duplicate of user-first-ux/references/ (owner)"),
    (r"^plugins/ui-studio/skills/(ui-ux-copy|ui-research|ui-a11y|ui-copy)/", lambda p: UF + p[len(UI):], "move", "edit: shared paths -> ../user-first-ux/...; ui-studio:* -> user-first-ux:*"),
    (r"^plugins/ui-studio/evals/(ui-accessibility|ui-ux-copy|ui-research)/", lambda p: UF + p[len(UI):], "move", "plugins: ['../../..'] still resolves to plugin root"),

    # ---- ui-studio: duplicates of user-first-ux
    (r"^plugins/ui-studio/references/shared/(anti-patterns|checklist|ethics-privacy|states-feedback|ux-principles)\.md$", None, "delete", "full duplicate of user-first-ux reference (owner)"),
    (r"^plugins/ui-studio/skills/ui-visual-direction/examples/", None, "delete", "byte-identical to user-first-ux/examples (owner); SKILL points by name"),
    (r"^plugins/ui-studio/skills/ui-visual-direction/references/components\.md$", None, "delete", "byte-identical to user-first-ux components.md (owner)"),
    (r"^plugins/ui-studio/references/shared/priority-workflow\.md$", SAME, "replace-with-pointer", "priority order + workflow -> pointer to user-first-ux + fallback; keeps ui-studio-only lines (distinctiveness at level 6, token plan, critique in Verify) and updated rule-ID index"),
    (r"^plugins/ui-studio/references/shared/quality-floor\.md$", SAME, "replace-with-pointer", "contrast/target/focus/reflow rows -> one pointer + fallback; tokens-over-values and eight states kept"),
    (r"^plugins/ui-studio/references/shared/severity\.md$", SAME, "replace-with-pointer", "scale owned by user-first-ux -> pointer + 4-line fallback"),
    (r"^plugins/ui-studio/references/shared/visual-system\.md$", SAME, "merge-into", "OWNER of tokens: receives ten-fixes tokens.md (role sizes, icon, surface, radius tokens), omni color/spacing/responsive/performance unique sections; C3/M2 -> pointers"),
    (r"^plugins/ui-studio/references/shared/ai-defaults\.md$", SAME, "merge-into", "receives unique tells from omni anti-slop.md (fabricated metrics, icon-in-square, pill inflation, blobs, identical rhythm); anti-patterns link -> by name"),
    (r"^plugins/ui-studio/references/shared/principles\.md$", SAME, "keep", "edit DP6 'ui-ux-copy' -> user-first-ux by name"),

    # ---- ui-studio: kept skills with edits
    (r"^plugins/ui-studio/\.(claude|codex)-plugin/plugin\.json$", SAME, "keep", "edit: version 1.0.0 (command names change), description (3.4), homepage/repository"),
    (r"^plugins/ui-studio/(README|NOTICE)\.md$", SAME, "keep", "edit Phase 6: skill map, commands, NOTICE provenance (Ten Fixes, omni, suite; user-first-ux no longer absorbed)"),
    (r"^plugins/ui-studio/agents/ui-critic\.md$", SAME, "keep", "edit: N/NO/G/U/A rule IDs come from user-first-ux"),
    (r"^plugins/ui-studio/skills/ui-visual-direction/SKILL\.md$", SAME, "keep", "edit: description sharpened vs visual-polish/ui-styles; examples/components -> user-first-ux by name"),
    (r"^plugins/ui-studio/skills/ui-visual-direction/references/typography-structure-motion\.md$", SAME, "merge-into", "receives unique bullets: omni typography.md, motion.md, checklists/motion.md; suite design-motion; durations per C11"),
    (r"^plugins/ui-studio/skills/(ui-critique|ui-design-system|ui-build|ui-stack-laravel|ui-stack-next|ui-theming)/SKILL\.md$", SAME, "keep", "edit: descriptions/pointers (3.4); restated a11y numbers -> pointers"),
    (r"^plugins/ui-studio/skills/ui-stack-laravel/references/flux-ui-v2\.md$", SAME, "keep", "edit: '>= 4.5:1' -> pointer"),
    (r"^plugins/ui-studio/skills/ui-stack-laravel/references/blade-components\.md$", SAME, "keep", "edit: '= 44px target' -> quality floor pointer"),
    (r"^plugins/ui-studio/skills/ui-stack-next/references/motion-and-focus\.md$", SAME, "keep", "edit: '>= 3:1' -> pointer"),
    (r"^plugins/ui-studio/skills/ui-stack-next/references/tailwind-v4-theme\.md$", SAME, "merge-into", "receives 'no second UI library' line from omni adapters/react-next.md"),
    (r"^plugins/ui-studio/", SAME, "keep", ""),

    # ---- omni-design (Option A)
    (r"^plugins/omni-design/\.claude-plugin/plugin\.json$", None, "delete", "plugin merged and removed (stubs dropped after verify, 2026-11-08)"),
    (r"^plugins/omni-design/\.codex-plugin/plugin\.json$", None, "delete", "plugin merged and removed"),
    (r"^plugins/omni-design/skills/omni-design/SKILL\.md$", STY + "SKILL.md", "merge-into", "context classifier, design dials, style-router table -> ui-styles; operating rules, conflict order, anti-slop, gates deleted (dup)"),
    (r"^plugins/omni-design/skills/omni-design/(README|CHANGELOG)\.md$", lambda p: "docs/archive/omni-design/" + os.path.basename(p), "move", "history; stub README replaces"),
    (r"^plugins/omni-design/skills/omni-design/SOURCES\.md$", "docs/archive/omni-design/SOURCES.md", "move", "provenance; ui-studio NOTICE links it"),
    (r"^plugins/omni-design/skills/omni-design/tests/", lambda p: "docs/archive/omni-design/tests/" + os.path.basename(p), "move", "scenario/trigger prompts kept for reference"),
    (r"^plugins/omni-design/skills/omni-design/styles/style-router\.md$", STY + "references/style-router.md", "move", "router; receives suite style-compatibility + accessibility hotspots"),
    (r"^plugins/omni-design/skills/omni-design/styles/", None, "delete", "shallower duplicate of the suite style skill (kept in ui-styles/references/styles/)"),
    (r"^plugins/omni-design/skills/omni-design/references/accessibility\.md$", None, "delete", "duplicate of user-first-ux accessibility (owner); style hotspots -> ui-styles style-router"),
    (r"^plugins/omni-design/skills/omni-design/references/(content-design|design-foundations|states)\.md$", None, "delete", "duplicate of owner files; unique lines merged (icon policy -> visual-polish Rule 07; hierarchy order -> visual-system H; error altitude -> states-feedback)"),
    (r"^plugins/omni-design/skills/omni-design/references/anti-slop\.md$", UI + "references/shared/ai-defaults.md", "merge-into", "unique tells only; then deleted"),
    (r"^plugins/omni-design/skills/omni-design/references/brand-to-ui\.md$", STY + "references/brand-to-ui.md", "move", ""),
    (r"^plugins/omni-design/skills/omni-design/references/(color|spacing-layout|responsive-design|performance)\.md$", VS, "merge-into", "unique sections only (C/L/effects budget); numbers per C6/C7"),
    (r"^plugins/omni-design/skills/omni-design/references/(typography|motion)\.md$", TSM, "merge-into", "unique bullets only; durations per C11"),
    (r"^plugins/omni-design/skills/omni-design/references/design-audit\.md$", UI + "skills/ui-critique/references/scored-audit.md", "move", "100-point audit, certainty classes; severity -> 4-tier (C5)"),
    (r"^plugins/omni-design/skills/omni-design/references/design-systems\.md$", UI + "skills/ui-design-system/references/token-architecture.md", "move", "token tiers; merged with suite design-system-engineering"),
    (r"^plugins/omni-design/skills/omni-design/references/(ecommerce|enterprise-dashboards|mobile-ui)\.md$", lambda p: UFS + "references/domains/" + os.path.basename(p), "move", "flows/domains are behaviour; restated numbers -> pointers"),
    (r"^plugins/omni-design/skills/omni-design/references/(forms|navigation|tables-data-density)\.md$", UFS + "references/components.md", "merge-into", "unique bullets into F/SN/TB; then deleted"),
    (r"^plugins/omni-design/skills/omni-design/references/(public-websites|reference-to-code)\.md$", lambda p: VD + os.path.basename(p), "move", ""),
    (r"^plugins/omni-design/skills/omni-design/workflows/(audit-ui|build-design-system|create-new-ui)\.md$", None, "delete", "duplicate of ui-critique / ui-design-system / ui-visual-direction + ui-build flows"),
    (r"^plugins/omni-design/skills/omni-design/workflows/enterprise-workflow-ui\.md$", UFS + "references/domains/enterprise-dashboards.md", "merge-into", "workflow steps not already in the reference"),
    (r"^plugins/omni-design/skills/omni-design/workflows/mobile-design\.md$", UFS + "references/domains/mobile-ui.md", "merge-into", "workflow steps not already in the reference"),
    (r"^plugins/omni-design/skills/omni-design/workflows/polish-ui\.md$", VP + "references/rules.md", "merge-into", "optical alignment, borders/radii, heading wraps -> 'Beyond the ten' list"),
    (r"^plugins/omni-design/skills/omni-design/workflows/redesign-existing-ui\.md$", VD + "redesign-existing-ui.md", "move", "preserve-first redesign; dup lines removed"),
    (r"^plugins/omni-design/skills/omni-design/workflows/reference-to-code\.md$", VD + "reference-to-code.md", "merge-into", "steps merged into the reference"),
    (r"^plugins/omni-design/skills/omni-design/adapters/laravel\.md$", UI + "skills/ui-stack-laravel/references/preserve-conventions.md", "move", "@csrf/@error/old()/__()/@can/route()/paginator/Bootstrap-AdminLTE; dup lines removed"),
    (r"^plugins/omni-design/skills/omni-design/adapters/react-next\.md$", UI + "skills/ui-stack-next/references/tailwind-v4-theme.md", "merge-into", "one unique line; rest duplicate of ui-stack-next"),
    (r"^plugins/omni-design/skills/omni-design/adapters/(overview|vue-nuxt-svelte|native-mobile)\.md$", lambda p: VD + "adapters/" + os.path.basename(p), "move", "stacks ui-studio does not cover elsewhere"),
    (r"^plugins/omni-design/skills/omni-design/checklists/(accessibility|implementation|release-gate)\.md$", None, "delete", "duplicate of user-first-ux checklist + ui-studio quality floor"),
    (r"^plugins/omni-design/skills/omni-design/checklists/motion\.md$", TSM, "merge-into", "compositor-only, interruptible"),
    (r"^plugins/omni-design/skills/omni-design/checklists/responsive\.md$", VS, "merge-into", "width test matrix"),
    (r"^plugins/omni-design/skills/omni-design/checklists/pre-design\.md$", STY + "SKILL.md", "merge-into", "classifier checklist"),

    # ---- ultimate-design-suite (Option A)
    (r"^plugins/ultimate-design-suite/\.claude-plugin/plugin\.json$", None, "delete", "plugin merged and removed (stubs dropped after verify, 2026-11-08)"),
    (r"^plugins/ultimate-design-suite/\.codex-plugin/plugin\.json$", None, "delete", "plugin merged and removed"),
    (r"^plugins/ultimate-design-suite/skills/_shared/(accessibility-baseline|anti-ai-slop)\.md$", None, "delete", "duplicate (user-first-ux accessibility; omni anti-slop -> ai-defaults); hotspots + prefers-contrast snippet -> style-router"),
    (r"^plugins/ultimate-design-suite/skills/_shared/brand-vs-product\.md$", STY + "references/brand-vs-product.md", "move", ""),
    (r"^plugins/ultimate-design-suite/skills/_shared/style-compatibility\.md$", STY + "references/style-router.md", "merge-into", "dominant/supporting rule + combinations into §Hybrids"),
    (r"^plugins/ultimate-design-suite/skills/design-(bento-grid|brutalism|claymorphism|glassmorphism|liquid-glass|maximalism|minimalism|neumorphism|skeuomorphism|spatial-ui)/SKILL\.md$",
     lambda p: STY + "references/styles/" + p.split("/")[3][len("design-"):] + ".md", "move", "frontmatter dropped; ../_shared links fixed; contrast/target numbers -> pointer"),
    (r"^plugins/ultimate-design-suite/skills/design-foundations/SKILL\.md$", None, "delete", "duplicate of ui-studio visual-system + principles"),
    (r"^plugins/ultimate-design-suite/skills/design-motion/SKILL\.md$", TSM, "merge-into", "component patterns, gesture response, when no animation; durations per C11"),
    (r"^plugins/ultimate-design-suite/skills/design-review/SKILL\.md$", UI + "skills/ui-critique/references/scored-audit.md", "merge-into", "style-fidelity check + finding format; rest duplicate of ui-critique"),
    (r"^plugins/ultimate-design-suite/skills/design-system-engineering/SKILL\.md$", UI + "skills/ui-design-system/references/token-architecture.md", "merge-into", "token examples (radius/elevation/motion), state tokens"),
    (r"^plugins/ultimate-design-suite/skills/ultimate-design/SKILL\.md$", STY + "SKILL.md", "merge-into", "decision guide, 'when NOT to use a style'; workflow duplicate of ui-build"),
]

INC_R = [
    (r"^\.claude-plugin/plugin\.json$", None, "delete", "plugin merged into ui-studio; no stub published"),
    (r"^README\.md$", UI + "README.md", "merge-into", "rules table + tools table -> ui-studio README visual-polish section"),
    (r"^marketplace-entry\.json$", None, "delete", "superseded by the stub entry in marketplace.json"),
    (r"^agents/ui-ten-fixes-auditor\.md$", UI + "agents/ui-ten-fixes-auditor.md", "move", "no same-role agent (ui-critic has no Bash/scripts); edit paths to visual-polish"),
    (r"^commands/ui-audit\.md$", UI + "skills/polish-audit/SKILL.md", "move", "command -> skill with disable-model-invocation (ui-studio convention); paths"),
    (r"^commands/ui-fix\.md$", UI + "skills/polish-fix/SKILL.md", "move", "same"),
    (r"^commands/ui-new\.md$", UI + "skills/polish-new/SKILL.md", "move", "same"),
    (r"^skills/(ten-fixes-rules|ui-audit|ui-fix|ui-build)/SKILL\.md$", VP + "SKILL.md", "merge-into", "one skill, modes audit / fix / build; fix workflow -> user-first-ux pointer"),
    (r"^skills/ten-fixes-rules/references/rules\.md$", VP + "references/rules.md", "move", "edits: Rule 06 -> pointer+fallback; Rule 05/08 rationale -> ux-laws pointers; Rule 03/04/10 in ui-studio tokens (C6, C8, C10, C11)"),
    (r"^skills/ten-fixes-rules/references/tokens\.md$", VS, "merge-into", "token roles merged; duplicate CSS block -> pointer to assets/tokens.css; then deleted"),
    (r"^skills/ui-audit/scripts/ui_lint\.py$", VP + "scripts/ui_lint.py", "move", "edit: Rule 04 families warn only above 2 (C8)"),
    (r"^skills/ui-audit/scripts/", lambda p: VP + "scripts/" + os.path.basename(p), "move", ""),
    (r"^skills/(ui-audit|ui-build)/assets/", lambda p: VP + "assets/" + os.path.basename(p), "move", "unchanged (verify baseline)"),
]


def apply(rules, rel):
    for pat, tgt, act, note in rules:
        if re.search(pat, rel):
            if tgt is SAME:
                tgt = rel
            elif callable(tgt):
                tgt = tgt(rel)
            return tgt or "—", act, note
    return "UNMAPPED", "UNMAPPED", ""


def files(root, skip_git):
    for d, dirs, fs in os.walk(root):
        if skip_git:
            dirs[:] = [x for x in dirs if not (d == root and x == ".git")]
        for f in fs:
            yield os.path.relpath(os.path.join(d, f), root).replace("\\", "/")


rows, unmapped = [], 0
for rel in sorted(files(SRC, True)):
    t, a, n = apply(R, rel)
    unmapped += a == "UNMAPPED"
    rows.append((rel, t, a, n))
for rel in sorted(files(INC, False)):
    t, a, n = apply(INC_R, rel)
    unmapped += a == "UNMAPPED"
    rows.append(("_incoming/ui-ten-fixes/" + rel, t, a, n))

from collections import Counter
c = Counter(r[2] for r in rows)
with open(OUT, "w", encoding="utf-8") as o:
    o.write("# Merge map (generated by mergemap.py; one row per SOURCE file + incoming)\n\n")
    o.write("Actions: move · merge-into · replace-with-pointer · delete · keep · exclude (local state, never in the repo)\n\n")
    o.write("Totals: " + " · ".join(f"{k} {v}" for k, v in sorted(c.items())) + f" · rows {len(rows)} · UNMAPPED {unmapped}\n\n")
    # collapse the 500+ .claude-flow rows into one row per directory to keep the map readable
    o.write("| SOURCE path | TARGET path | Action | Note |\n|---|---|---|---|\n")
    for rel, t, a, n in rows:
        o.write(f"| `{rel}` | {'`'+t+'`' if t not in ('—',) else '—'} | {a} | {n} |\n")
print(dict(c), "rows", len(rows), "unmapped", unmapped)
