# Typography, structure and motion

Complements T1-T7, M1-M2 (`references/shared/visual-system.md` at the plugin root) and
DP4-DP5 (`references/shared/principles.md`).

## Typography

- Type is where most of a page's character comes from. Limit it to one family, or a pair that
  is obviously different (e.g. a grotesque with a slab), never two near-twins.
- Choose faces for this brief, not the family you would grab for any job. Inter, Roboto and
  system-ui by reflex count as AD6.
- Build a deliberate scale in the spirit of Bringhurst's *The Elements of Typographic Style*:
  intentional steps, weights, widths and letter-spacing, not ad-hoc sizes. In product UI the
  ratio is T1's, in rem tokens (`visual-system.md`).
- When a headline or a word is used as an image, its treatment (cut, weight, size, spacing) is
  part of the composition and is designed, not defaulted.
- Measure: keep lines below about 80 characters (prose sweet spot 65-75ch, L2). A serif body can
  run a little longer than a sans body and wants a touch more line-height.
- Tracking: tighten slightly on large display sizes; open it a touch on short caps labels and
  tiny text. Fluid display type with `clamp()` avoids breakpoint jumps.
- Multilingual: check the face covers the scripts and diacritics you need; do not design to
  English string lengths (BM runs longer).
- Performance: subset fonts, prefer a variable font for several weights, `preload` the critical
  faces, ship only the weights you use, and match fallback metrics to avoid layout shift.
- Avoid: emphasising a single word in a headline (AD7), long ALL-CAPS labels (T7), and labels
  above content that would read fine without them (AD7).

## Structure

- Every outline, border, number, eyebrow, divider and label must carry information (DP4). If you
  cannot say what it encodes, remove it.
- Space groups before reaching for lines (G1, G5). Do not nest cards in cards (G3).

## Motion

- Ambient (non-user-triggered) motion: one orchestrated moment at most, such as an entrance
  sequence or a single reveal. Per-section fade-and-rise and a hover transition on every card
  are among the strongest "generated" signals.
- Responsive motion (open, expand, confirm, reorder) is encouraged when it explains where
  something came from or what changed. Durations and easing: M1 in `visual-system.md`.
- Continuity and direction: a moved element stays the same object (layout / shared-element
  transitions, FLIP); things enter from where they live (menu from its button, drawer from its
  edge, toast from the region it reports on).
- Interruptible: never block interaction behind an animation; a second click retargets instead
  of queueing. Gestures track the finger 1:1 and settle with physics.
- Hover is a hint: colour, a 2-4px translate or one shadow step; no lift-and-scale on every card.
- Component patterns: modal backdrop fades and the panel moves a short distance from its origin;
  drawers slide from their edge; dropdowns grow from the trigger; list add/remove/reorder uses
  layout animation; tabs and accordions often read better instant than with a laggy height
  animation; route transitions are a short cross-fade.
- No animation is better for data entry, tables and dense surfaces during a task, for anything
  that delays reaching content, and for transitions seen many times a day.
- Always provide the reduced-motion path (M2). Stack code: `ui-stack-laravel`, `ui-stack-next`.
