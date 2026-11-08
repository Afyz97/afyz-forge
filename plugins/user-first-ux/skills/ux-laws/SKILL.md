---
name: ux-laws
description: >-
  Applies the 30 Laws of UX (Fitts, Hick, Miller, Jakob, Von Restorff, Zeigarnik,
  Goal-Gradient, Peak-End, Gestalt proximity, similarity, common region and more) as checkable
  rules and audits a screen pillar by pillar with Pass/Fail, the exact element and a concrete
  fix, with Blade/Livewire stack notes. Use for "apply Hick's law to this menu", "audit this
  screen against the laws of UX", "which UX law does this break?", "too many choices here",
  "chunk this long form", "where should the primary button go?", "show progress in this
  wizard". Not for a general usability review or flow design - use user-first-ux.
---

# UX Laws

## North star

Good UX reduces how much the user has to think. Every rule below exists to cut a decision,
a memory load, a hunt or a doubt from the user's path. The laws are heuristics, not physics:
they guide judgment, and evidence from real users always overrides them. Priority when
anything competes: **honest > accessible > usable > efficient > consistent > aesthetic**.

This skill is part of the user-first-ux plugin: follow the `user-first-ux` skill's workflow,
priority order and review format; this skill supplies the law rules, the audit and the stack
notes.

## How to work

1. **Read** the screen, its components, tokens, copy and routes. Name the users, their top
   3 tasks and the context (device, frequency, expertise). Unknowns are **hypotheses**, never findings.
2. **Plan** flow first, then structure, then layout, then polish. Before building a decision
   point, count its options and combinations (Hick).
3. **Build** with the rules below, using existing components and tokens.
4. **Self-audit** with the Audit protocol before calling UI work done.
5. **Report** using `references/audit-template.md`, naming any trade-off in one line
   (e.g. "Kept 5 plans: legal requires all tiers shown (Ethics > Hick)").

## Build rules

Each rule is observable: a reviewer can point at the screen and say pass or fail.
Tags name the law; definitions are in the Law index.

### 1. Easy to reach
- **R1** One primary CTA per view: the largest filled control, at least the A7 house floor tall
  (`../user-first-ux/references/accessibility.md`), placed where the
  task ends (after the last field, in the page header, in the mobile thumb zone). Never
  icon-only, never only in an overflow menu, never in a far corner. `[Fitts]`
- **R2** Targets meet A7 (`../user-first-ux/references/accessibility.md`); ≥ 8px between adjacent targets; destructive
  actions never adjacent to the primary. `[Fitts]`
- **R3** Acknowledge every action within 100ms; show the result within 400ms or a skeleton
  or progress indicator; determinate progress over ~10s; block double-submit. `[Doherty]`
- **R4** Accept spaces, dashes, case, `+60` and pasted formats; normalise in the system;
  display one consistent format. `[Postel]`
- **R5** Errors say what happened and how to fix it, next to the field, and keep the user's input. `[Postel]`

### 2. Fewer choices
- **R6** At every decision point (pricing, onboarding, forms, settings) count options ×
  combinations, state the number in your plan, and cut, group or default until it is the
  minimum the task needs. `[Hick]`
- **R7** Mark one honest recommended option or default; put advanced options behind "More
  options" / `<details>`. `[Hick]` `[Cognitive Bias]`
- **R8** More than 3 comparable options get side-by-side comparison with aligned rows;
  more than 15 options in a control get search. `[Choice Overload]`
- **R9** Remove every element that does not support the task on this screen; check each by
  imagining the screen without it. `[Occam]`
- **R10** The top 20% of tasks (from analytics, tickets or the brief; else a hypothesis) get
  the most prominent positions; rare tasks move to secondary places. `[Pareto]`
- **R11** The system absorbs complexity (defaults, inference, autofill, formatting); never
  hide a control the task needs to "simplify". `[Tesler]`

### 3. Shows progress
- **R12** Every flow of 3+ steps and every setup list shows done vs left ("Step 2 of 4 · 2
  left", "3 of 5 done") and saves partial work so users can resume. `[Zeigarnik]`
- **R13** Every finish line has a visible stepper or progress bar; give an honest head start
  (count real completed steps); the last step is the easiest (review + one button, no new
  fields). `[Goal-Gradient]`
- **R14** Every flow ends on a designed success state (what happened, reference, next step);
  error recovery keeps the user's data and offers retry. `[Peak-End]`
- **R15** No unrelated modals, promos or surveys mid-task; offer expert shortcuts (bulk
  actions, keyboard shortcuts, saved filters) without cluttering the novice view. `[Flow]`

### 4. Familiar patterns
- **R16** Use conventions: magnifier = search; account/settings top-right; logo → home;
  cart → checkout → pay; dropdowns open down; standard form controls; gear/trash/× icons,
  labelled when ambiguous. Be novel only where the product is novel. `[Jakob]`
- **R17** Labels and navigation use the users' words and task order, never DB fields,
  internal codes or the org chart. `[Mental Model]`
- **R18** Guidance lives in context (labels, inline hints, empty-state instructions); core
  tasks never depend on docs or product tours. `[Active User]`

### 5. Clear hierarchy
- **R19** Exactly one visually dominant element per decision; every other action is
  quieter (outline, ghost, link). It must pass the squint test. `[Von Restorff]`
- **R20** Most important items first and last in nav and lists; never bury key items mid-list. `[Serial Position]`
- **R21** Critical information never looks like an ad or banner; changes the user causes are
  visible (row highlight, inline "Saved", `aria-live`). `[Selective Attention]`
- **R22** Spacing encodes grouping: label→field < field→field < group→group, on one spacing scale (ui-studio tokens). `[Proximity]`
- **R23** Same function, same look everywhere; links never look like text, buttons never
  look like tags or badges. `[Similarity]`
- **R24** Related content shares one container with its actions inside it; no cards in
  cards. `[Common Region]`
- **R25** Steps in steppers and timelines are joined by a line; a control is visibly linked
  to what it affects. `[Uniform Connectedness]`
- **R26** Simple shapes, standard icons, whitespace over borders and dividers. `[Prägnanz]`
- **R27** One type scale and one spacing scale, aligned to a grid; polish comes after the
  task works and is never accepted as proof that it works. `[Aesthetic-Usability]`

### 6. Less to hold
- **R28** Group nav, settings and form fields into labelled groups of about 5–9 (fewer is
  better); never 15+ equally weighted items in one flat list or grid. `[Miller]`
- **R29** Forms over ~7 fields are split into titled sections or steps; long numbers are
  shown in groups (`012-345 6789`, `900101-14-5678`). `[Chunking]`
- **R30** One decision per step in complex flows; remove decoration, jargon and
  inconsistencies that add effort without information. `[Cognitive Load]`
- **R31** Never make users carry information between screens: keep context visible (order
  summary at payment), show recent and previous values, never ask twice. `[Working Memory]`
- **R32** Defaults and anchors serve the user (truthful "was" prices, no pre-selected
  paid extras). `[Cognitive Bias]`
- **R33** Make tasks shorter than expected (saved details, one-click repeat) and state a
  realistic time estimate for long ones ("Takes about 3 minutes"). `[Parkinson]`

## Audit protocol

**When:** whenever the user asks for a review or audit, and as a self-check before
declaring any UI work done.

**Order:**
1. **Guardrails first** (`references/guardrails.md`): A11y, Ethics, States. A guardrail ❌ caps the verdict at "Fix first".
2. **Pillars 1–6** in order, checking each rule above against named elements.
3. For any law that needs depth, read its entry in the matching laws file and use its **Audit check** question.
4. Rank findings with the user-first-ux severity scale: **Critical** blocks · **High** misleads ·
   **Medium** slows or causes errors · **Low** polish.
5. Output with `references/audit-template.md`: one row per finding, Pass/Fail/N/A, exact
   element (label + `file:line`), law tags, concrete fix, severity; then the guardrails line,
   the top 3 fixes, what was not verified, and open hypotheses.

An audit without element names and concrete fixes is incomplete. Anything not checkable
statically (timing, screen reader, real data) is reported as **not verified**, never ✅.

## Law index

Read the reference file when a law is central to the task, or when a finding needs depth.

**Cognition & decisions** → `references/laws-cognition.md` (read for pricing, onboarding,
forms, settings, filters, navigation)
- **Hick** — decision time rises with the number and complexity of choices.
- **Choice Overload** — too many options can cause paralysis and abandonment, mainly when options are complex and preferences unclear.
- **Miller** — short-term memory holds about 7 ± 2 items (4 ± 1 chunks); chunk, don't count.
- **Chunking** — meaningful groups are easier to scan and remember.
- **Cognitive Load** — design adds extraneous effort on top of the task's own effort.
- **Working Memory** — a small temporary store; don't make users carry data between screens.
- **Selective Attention** — users ignore ad-like UI and miss subtle changes.
- **Cognitive Bias** — defaults and anchors steer decisions; use them only for the user.
- **Occam** — prefer the design with the fewest elements and assumptions.
- **Pareto** — ~80% of use comes from ~20% of features; optimise those first.
- **Tesler** — complexity can only be moved; the system should absorb it.

**Perception & layout** → `references/laws-perception.md` (read for layout, hierarchy,
spacing, cards, steppers, icons, visual polish)
- **Aesthetic-Usability** — attractive designs feel easier and can mask problems.
- **Von Restorff** — the one item that differs is noticed; emphasise one thing.
- **Serial Position** — first and last items are remembered best.
- **Prägnanz** — people read complex visuals in their simplest form.
- **Proximity** — near things are seen as a group.
- **Similarity** — alike things are seen as related or same-function.
- **Common Region** — things inside a shared boundary are seen as a group.
- **Uniform Connectedness** — visually connected things are seen as most related.

**Interaction & performance** → `references/laws-interaction.md` (read for actions,
buttons, loading, validation, long tasks)
- **Fitts** — target time depends on distance and size.
- **Doherty** — responses under ~400ms keep users productive.
- **Postel** — accept input liberally, output conservatively.
- **Flow** — immersion needs matched challenge, feedback and no interruptions.

**Behaviour & experience** → `references/laws-behaviour.md` (read for navigation,
onboarding, multi-step flows, checkout, success/error moments, redesigns)
- **Jakob** — users expect your product to work like the ones they already use.
- **Mental Model** — match the user's belief about how the system works.
- **Active User** — users never read manuals; guide in context.
- **Zeigarnik** — unfinished tasks pull people back to resume them; show what's left.
- **Goal-Gradient** — motivation rises near the goal; show honest progress.
- **Peak-End** — experiences are judged by the peak and the end.
- **Parkinson** — work expands to fill the time; make tasks shorter than expected.

**Guardrails** → `references/guardrails.md` (read for every audit and before "done")
- **A11y** — WCAG 2.2 AA floor. **Ethics** — no dark patterns. **States** — empty, loading,
  error, partial, success, availability, content stress.

## Stack notes

Laravel Blade + Livewire 4 with Tailwind v4 or Bootstrap 5: `references/stack-notes.md`.

## When laws conflict

- **Hick vs Fitts:** reduce the choices first, then make the remaining ones big and close.
- **Jakob vs Von Restorff:** keep the conventional placement and form; make the primary stand
  out within the convention.
- **Aesthetic-Usability vs usability:** usability wins; polish never hides function.
- **Occam vs Tesler:** remove what is unnecessary, but move necessary complexity into the
  system instead of deleting the control.
- **Zeigarnik / Goal-Gradient vs Ethics:** honest progress only; no fake percentages, no guilt.
  (Laws of UX suggests "artificial progress"; here a head start must be real: a step actually
  done or a bonus actually granted.)
- **Doherty vs Ethics:** never pad a wait to look thorough; show real work, never invented work.
- **Miller vs Pareto:** group the long tail, but never bury a top task inside a group.
- **Fitts and corners:** corners help OS-level desktop menus; in web content the primary CTA is never in a far corner.
- **Any law vs real user data:** data wins. Laws are hypotheses to test.

## Output formats

- **Audit:** `references/audit-template.md`, exactly.
- **Build:** (1) users, top tasks, hypotheses; (2) flow as numbered steps, with the choice
  count for each decision point; (3) implementation; (4) the self-audit in the audit format,
  with any trade-off named.

## Done means

The self-audit shows 6/6 pillars passing and all three guardrails ✅, or every ❌ is
explicitly justified to the user with the trade-off named. Items not verifiable here are
listed as not verified.

## Evals

`evals/evals.json` holds test prompts and expected behaviours for this skill.
