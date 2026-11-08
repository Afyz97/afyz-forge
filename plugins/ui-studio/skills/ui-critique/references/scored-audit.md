# Design Audit, Scoring & Review

How to review a UI — your own or an existing one — as a strict, independent, evidence-based critic.
Reviewing your own work critically is a required quality gate (DP7; `../SKILL.md`). Don't skip it because "it
looks fine."

## Reviewer stance

- **Independent** — evaluate as if someone else built it; you're looking *for* problems.
- **Evidence-based** — cite the specific element/selector/line/screenshot, not a vibe.
- **Honest about certainty** — classify each finding:
  - **Objective defect** — measurably wrong (contrast fails A1; no focus state; overflow at 320px;
    fabricated data). Not debatable.
  - **Likely defect** — strong problem given context (density too low for an ops tool; missing empty
    state) but arguable.
  - **Preference** — taste. Report as a suggestion, **never as a defect.** Don't inflate taste into
    findings, and don't dismiss real defects as taste.

## The 100-point scored audit

Score categories, weighted; **adjust weights to context** (an editorial page and an ops dashboard
weight differently — state the weighting you used).

| Category | Default weight |
|---|---|
| Visual hierarchy | 10 |
| Typography | 10 |
| Layout & spacing | 10 |
| Color & contrast | 10 |
| Consistency & design-system integrity | 10 |
| Usability | 10 |
| **Accessibility** | **15** |
| Responsiveness | 10 |
| Interaction & states | 5 |
| Motion quality | 5 |
| Performance-aware design | 5 |
| **Total** | **100** |

Accessibility is weighted highest because its failures exclude users outright. A dramatic-but-unusable
design must not score well; a technically-valid-but-generic one must not automatically score well
either — distinctiveness and fit are part of quality.

## Per-finding report contract

For each finding, report:

- **Finding** — what's wrong, named.
- **Evidence** — where (element/selector/line/screenshot/measured value).
- **Severity** — Critical · High · Medium · Low (user-first-ux scale; polish = Low).
- **Impact** — who it affects and how (task blocked? excluded users? just aesthetics?).
- **Fix** — the concrete corrective action.
- **Style impact** — whether the fix changes the intended visual style (so the author can weigh it).
- **Certainty** — objective defect / likely defect / preference.

## Severity-based prioritization

Rank by roughly **Impact × Frequency × Reach × Fix-confidence**, and fix in this order:

1. Blockers (can't complete the core task; broken functionality).
2. Accessibility failures (exclude users).
3. Task-completion failures (friction that loses users).
4. Information-architecture failures (can't find/understand).
5. Interaction/state failures (missing error/loading/empty).
6. Responsive failures.
7. Consistency issues.
8. Visual polish.

**Don't polish shadows while users can't complete the main workflow.** Fix top-down.

## Conflict resolution (when principles collide)

Resolve using the user-first-ux priority order (pointer and fallback in
`../../../references/shared/priority-workflow.md`). Common calls:

- **Apple-style translucency vs data readability** → readability wins; scrim/solid the surface.
- **Heavy motion vs accessibility** → reduced-motion path + restraint win.
- **Minimalism vs information completeness** → completeness of the *task's* needs wins; find hierarchy,
  don't hide function.
- **Novel layout vs trained-operator speed** → convention wins for expert tools.
- **Design purity vs existing framework/system** → work within the system; propose change explicitly.

## Audit checklist (fast pass)

Hierarchy (squint test) · type from a scale, readable measure/contrast · spacing from one scale ·
color roles + contrast + non-color status · consistency/tokens · all interaction states present ·
empty/loading/error designed · responsive rethink + reflow at 320px + the target house floor · motion
purposeful + reduced-motion · performance of effects · real content · **no slop** (AD1-AD10 in `../../../references/shared/ai-defaults.md`) ·
style fidelity (does it actually achieve the intended style?).

## Common AI failure modes (in reviews)

Reporting taste as defect · missing real accessibility defects · no evidence · no severity ordering ·
"looks fine" self-review · scoring drama over usability · not stating context weighting.

## Style fidelity (named styles)

Does it genuinely realize the intended style, or just one CSS effect of it? (Glass isn't "a
blur"; neumorphism isn't "two shadows"; minimalism isn't "empty"; bento isn't "a grid";
brutalism isn't "ugly font".) Judge against the style file's checklist in the `ui-styles` skill.
If asked "does this qualify as X?", answer with specifics from that file.

## Reviewer red flags (self-check)

- Writing "looks great" without evidence → you haven't reviewed, you've reacted.
- Flagging a gradient/card/dark-theme without checking whether it's justified.
- Certifying accessibility you didn't measure.
- Listing only easy nits and missing the structural hierarchy problem.
- Turning the review into a rewrite instead of findings + fixes.
