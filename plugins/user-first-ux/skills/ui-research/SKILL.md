---
name: ui-research
description: >-
  Plans user research and synthesises the results. Planning: choose a method (interviews,
  usability tests, surveys, card sorting, diary studies, A/B tests) with sample sizes and
  timelines, write a research plan and an interview or test guide. Synthesis: turn interview
  transcripts, session notes, survey CSVs, support tickets, NPS/CSAT comments or app-store
  reviews into themes with prevalence and quotes, insights, opportunities and recommendations.
  Use for "plan a usability test", "write an interview guide", "how many users should we
  test?", "synthesise these interview notes", "affinity map this", "what are users complaining
  about in these tickets?", "find segments in this survey". Not for designing or reviewing
  screens - use user-first-ux.
argument-hint: "plan | synthesize <input>"
---

# User research: plan and synthesise

Arguments: `plan <question or feature>` or `synthesize <files or pasted data>`. With no
argument, decide from the input (raw data -> synthesise; a question -> plan).

## Plan

1. State the decision the research must inform and the objectives.
2. Pick the method from `references/methods.md` (sample sizes and durations are there).
3. Write the plan: objectives, method, participants and recruiting criteria, timeline,
   deliverables (plan, guide, synthesis report, highlight reel of quotes and clips).
4. For interviews or usability tests, write the guide from `references/interview-guide.md`.
5. Frameworks to name in the plan for analysis: affinity mapping, impact/effort matrix,
   journey mapping, jobs to be done.

## Synthesise

Inputs accepted: interview transcripts or researcher notes, survey exports (CSV, or pasted
rows), observations from usability sessions, support tickets, NPS/CSAT comments, app-store
reviews.

Rules:
- **Quote people directly.** Verbatim quotes are what make an insight believable; give each
  theme at least two, tagged with participant IDs.
- **Keep what you saw apart from what you think it means.** "5 of 8 clicked the wrong button"
  is an observation; "the placement is confusing" is an interpretation. Label which is which.
- **Count.** "7 of 10" instead of "most". Report prevalence per theme.
- Do not present guesses as findings; mark them as hypotheses with a way to test them
  (`../user-first-ux/SKILL.md`, Workflow step 1).

Output: `references/synthesis-template.md`.

## Connectors

User-feedback tools add tickets, requests and NPS to cross-check; product analytics confirms
qualitative findings and sizes pain points; a knowledge base holds earlier studies and is where
the report gets published (connector roles: the **ui-studio** connectors reference, if installed; otherwise use what is
connected and never claim a connector was used when it was not).
