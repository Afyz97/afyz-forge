---
name: ui-handoff
description: >-
  Writes a developer handoff spec for a finished design: layout and breakpoints, tokens used,
  components and props, every state and interaction, responsive behaviour, edge cases (empty,
  long text, 100 items, slow network, missing data), motion timings and accessibility notes,
  plus implementation notes for Laravel (Blade, Livewire, Flux, Filament) or Next.js (React,
  Radix, Tailwind v4). Use for "write a handoff", "spec this for the devs", "dev-ready spec",
  "turn this Figma frame or screenshot into a spec", "what do engineers need to build this?",
  "redlines". Not for building it (ui-stack-laravel, ui-stack-next), critiquing it
  (ui-critique), or documenting a reusable component (ui-design-system).
argument-hint: "<path, screenshot or figma-url>"
---

# Developer handoff spec

Input: a Figma link (pull frames and measurements if a design tool is connected), a screenshot,
a file in the repo, or a description. Ask which stack it targets if the repo does not make it
obvious (`composer.json` -> Laravel notes, `package.json` with `next` -> Next notes).

## What the spec covers

- **Visual**: exact measurements (padding, margins, widths), token names, breakpoints and what
  changes at each, variants and states.
- **Interaction**: click and tap targets, hover, transitions with duration and easing, gestures
  (swipe, pinch, long-press) and their non-gesture alternatives (2.5.7).
- **Content**: character limits, truncation rules (with the full text reachable), and the
  empty, loading and error versions of every region.
- **Edge cases**: shortest and longest content, translated strings (+30-40% for BM), slow or
  failing network, absent data, and the list that suddenly holds a hundred entries.
- **Accessibility**: focus order, accessible names, roles and states, keyboard behaviour,
  screen-reader announcements.

## Principles

1. **Leave nothing to guess.** Whatever the spec omits, an engineer will invent; spell it out.
2. **Token names, not numbers.** Write `spacing-md`, not `16px` (quality floor).
3. **All states, every time**: default, hover, active, focus, disabled, loading, error, empty.
4. **Give the reason.** "Collapses to a bottom sheet on mobile because most use is one-handed"
   lets the engineer make the right call when something unforeseen comes up.

## Output

Fill `references/spec-template.md`. Add the stack section from `references/stack-notes.md`.
Mark anything you could not measure as **assumed** and list it under open questions.

## Connectors

With a design tool connected you can read real dimensions, pull token values and export
assets; with a tracker connected, attach the spec to its build ticket and turn each section into
a sub-task
(`${CLAUDE_PLUGIN_ROOT}/references/shared/connectors.md`).
