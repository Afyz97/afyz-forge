# Evaluation Report

What was actually run during construction, with results, and what remains to be run.
Honesty over optimism: this records verified checks and clearly marks what is scaffolded but
not yet executed.

## 1. Structural validation — RUN, PASS

A script validated all 15 skills:
- Every `skills/<name>/SKILL.md` exists and has YAML frontmatter.
- `name` matches its parent directory, is lowercase-alphanumeric-with-single-hyphens, ≤64
  chars (spec-compliant).
- `description` is non-empty and ≤1024 chars (all 496–736 chars).

Result: **15/15 valid.**

| Skill | desc length |
|---|---|
| ultimate-design | 736 |
| design-spatial-ui | 620 |
| design-glassmorphism | 616 |
| design-foundations | 603 |
| design-liquid-glass | 604 |
| design-minimalism | 598 |
| design-neumorphism | 586 |
| design-skeuomorphism | 576 |
| design-maximalism | 557 |
| design-review | 552 |
| design-brutalism | 546 |
| design-system-engineering | 532 |
| design-bento-grid | 528 |
| design-claymorphism | 515 |
| design-motion | 496 |

## 2. Trigger keyword coverage — RUN, PASS (static analysis)

Checked descriptions for alias/keyword coverage and non-UI exclusions:
- **All 15** descriptions include a non-UI/backend exclusion clause (verified after
  accounting for YAML line-wrapping).
- **Negative-term guards present** in-body for the highest-risk collisions: `design-minimalism`
  ("minimal API"), `design-brutalism` ("brutal error"), `design-glassmorphism` ("glass
  table" SQL), plus `design-spatial-ui` scopes to XR/immersive/3D (guards "spatial index").
- **Alias coverage** confirmed: e.g. neumorphism→"soft UI/soft-ui/neomorphism";
  glassmorphism→"frosted glass/glass UI"; skeuomorphism→"skeomorphism/skeuomorphic";
  brutalism→"neo-brutalism/neo-brutalist"; liquid-glass→"Apple-style/iOS 26"; spatial→
  "immersive/3D interface/AR/VR/MR/visionOS".

This is static (description-level) analysis. It predicts routing; it does not prove an
agent's runtime selection — see Limitations.

## 3. Deterministic auditor — RUN, PASS

`scripts/design-audit.mjs` was run against `evaluations/fixtures/bad-sample.css` (an
intentionally bad fixture). All 11 rules that should fire on that fixture fired: shadow-stack,
backdrop-filter-density, backdrop-filter-fallback-missing (HIGH), reduced-motion-missing,
focus-removed (HIGH), radius-repetition, important-spiral, zindex-escalation,
purple-blue-gradient, gradient-text, tiny-tap-target — **14 signals**, sorted by severity,
each with why / false-positive-risk / remediation. A regex bug in the purple-blue-gradient
rule (word-boundary before `#`, and 5-vs-6 hex digits) was found and fixed during this run;
re-verified firing on lines 3 and 7.

Auditor scope is deliberately mechanical; it does not attempt taste.

## 4. Baseline-vs-assisted quality comparison — NOT RUN (scaffolded)

The rubric (`evaluations/RUBRIC.md`) and scenario cases (`evaluations/EVALUATIONS.md` §D) are
ready, but paired baseline (no-suite) vs assisted (with-suite) subagent runs were **not
executed** in this build. Recommended procedure:
1. For each §D scenario, run a fresh agent WITHOUT the suite; capture output.
2. Run the same prompt WITH the suite; capture output.
3. Score both with `RUBRIC.md`; confirm the suite raises distinctiveness, style fidelity,
   subject specificity, accessibility, and anti-slop — not merely output length.
4. Where possible, blind the scorer to which is which.

## 5. Visual/browser validation — NOT APPLICABLE HERE

This repository ships skills, not a running application, so there is nothing to render. When
the suite is applied to a real project, use that project's existing browser/screenshot
tooling (per each skill's responsive/performance checklist and the master brief §14) — do
not add a heavy browser dependency just to test.

## Limitations (carried to the README)

- Runtime trigger selection not tested with live subagents (static coverage only).
- No baseline-vs-assisted scoring executed yet.
- No rendered-UI validation (no app in this repo).
- Liquid Glass / spatial guidance tracks fast-moving Apple platforms; verify current HIG.
- Auditor detects mechanics only.

## Recommended next steps (prioritized)

1. Run the §D baseline-vs-assisted comparison with subagents; record scores here.
2. Run live trigger tests for the §A/§B/§C cases (true positives, aliases, true negatives)
   and tune any description that mis-fires.
3. Apply the suite to one real project surface end-to-end and do rendered + a11y validation.
4. Consider adding `references/` splits only where a SKILL.md grows past ~500 lines in use.
