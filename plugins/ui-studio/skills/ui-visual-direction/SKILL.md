---
name: ui-visual-direction
description: >-
  Sets the visual direction for a new or reshaped interface and then builds it: grounds it in a
  real subject, writes a token plan (4-6 named hex colours, type roles, ASCII wireframes),
  self-reviews that plan against generic AI-looking defaults (cream + terracotta, purple
  gradients, Inter, identical rounded cards, ALL-CAPS eyebrows), then builds. Use for
  "design/build a landing page, dashboard, hero, section, form or app screen", "make it
  distinctive / less generic / less AI", "redesign the look", "pick fonts and colours", "a
  design plan before code", reference or screenshot to code, public websites. Stack-neutral:
  pair with ui-stack-laravel or ui-stack-next. Not for a named style (ui-styles), reviewing a
  design (ui-critique), deck themes (ui-theming) or posters (ui-canvas-art). Not for fixing the
  look of an existing screen - use visual-polish.
argument-hint: "<brief>"
---

# Visual direction and build

Shared rules live at the plugin root; read them, do not restate them:

- Frame and workflow: `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`
- Principles DP1-DP8: `${CLAUDE_PLUGIN_ROOT}/references/shared/principles.md`
- Defaults to avoid AD1-AD10: `${CLAUDE_PLUGIN_ROOT}/references/shared/ai-defaults.md`
- Quality floor and the eight states: `${CLAUDE_PLUGIN_ROOT}/references/shared/quality-floor.md`
- Visual system rules H/L/S/T/C/E/M: `${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`
- Usability laws N/NO/G/U, components and examples: the **user-first-ux** skill, if installed

## Stance

Act like the lead designer at a studio whose reputation is that no two clients look alike. This
client has already turned down proposals that felt off-the-shelf and is paying for a point of
view. So make committed decisions about colour, type and layout for *this* brief, take a risk
where the brief supports one, and mix what you do well with something you have not tried.

## Before pass 1

Answer the UX brief (`priority-workflow.md`, step 1) and DP1: product, audience, the screen's
one job. If any is missing, propose a concrete answer and confirm it.

## The opening moment

The first screen a visitor sees should lead with whatever is most characteristic of the
subject's world. That might be a headline, a photograph, a motion piece, a live demo or
something to interact with; pick the form that fits. The "huge number, small caption, row of
stats, gradient accent" hero is the stock answer; use it only when it truly is the best one.

## Typography

Details and the full scale rules: `references/typography-structure-motion.md`. In short: one
family or two clearly contrasting ones, chosen on purpose; a real modular scale; measure under
80 characters; when type is the visual, the treatment itself is the design. Avoid AD7.

## Process: two passes, with an approval gate

**Pass 1, plan** (no code yet). Use `references/plan-template.md`:
- Colour: 4-6 named hex values with roles.
- Type: faces and what each one does.
- Layout: one-sentence options plus ASCII wireframes to compare, with alignment stated.
- Principles: what makes this one unmistakably for this subject.

**Self-review.** Hold each choice against the brief and against `ai-defaults.md`. Would this
choice show up on any similar page? If yes, change it and record *what* changed and *why*.
Only a plan that survives this goes forward.

**Approve.** Present the reviewed plan and stop for approval (`priority-workflow.md` step 4).

**Pass 2, build.** Implement from the approved plan, using the stack skill for the framework
(`ui-stack-laravel` or `ui-stack-next`). Watch selector specificity: a section-level class and
a component class often fight over the same padding or margin between sections; decide which
one owns the gap.

**Verify.** Run the critique framework (`ui-critique`), then the quality floor and the
user-first-ux checklist. Final polish: `visual-polish` audit, then DP8: refine, do not add.

## Components, examples and other references

Component rules (buttons B, forms F, pickers P, tables TB, dashboards D, cards/modals/toasts CL,
search/nav SN, onboarding O) and the eight before/after examples (stat card, avatar stack,
assignee picker, product card, signup form, data table, destructive confirm, empty state) are
owned by the user-first-ux skill (`references/components.md`, `examples/`). Follow it if
installed. Minimum if not: one primary action per view, labels above fields, every state
designed.

| Task | Load |
|---|---|
| Public website or landing page | `references/public-websites.md` |
| Screenshot, mockup or live site to code | `references/reference-to-code.md` |
| Redesigning an existing UI (preserve first) | `references/redesign-existing-ui.md` |
| Vue / Nuxt / Svelte, React Native / SwiftUI / Flutter, or stack detection | `references/adapters/` |

## Words inside the design

Use real copy from the start; templated placeholder text gives the game away as fast as a
stock gradient. Write it with the `ui-ux-copy` skill (user-first-ux plugin), if installed.

## Output

Follow the **Build** output in `priority-workflow.md`: UX brief, flow, IA outline, token plan
+ wireframes (then stop for approval), implementation, completed checklist with trade-offs named.
