# States, Feedback & Error Recovery

## 1. Every component handles every state (ST)

Design and implement all of these, not just the happy path:

- **Interaction**: default, hover, focus-visible, active/pressed, selected
- **Availability**: disabled (with reason), read-only, permission denied, offline
- **Loading**: loading, skeleton, slow network
- **Data**: empty (first use / no results / cleared), partial data, 0 / 1 / many / 10,000 items
- **Outcome**: error (field / section / page), success
- **Content stress**: very long content, overflow, truncation with the full text available,
  translated strings (+30-40% length)

Partial data renders what it has and says what is missing. Empty has three kinds with different
copy: first use (teach + one action), no results (say what was searched, offer to clear
filters), cleared / all done (brief acknowledgement).

When reviewing, list which states are missing. Missing empty, error or loading states is at
least **High** severity.

## 2. Feedback & performance (FP)

- **FP1 Response bands**: < 100ms feels instant; < 1s keeps flow; > 1s needs an indicator;
  > 10s needs a progress bar with an estimate and the option to keep working.
- **FP2** Skeletons for content loads over ~300ms, matched to the final layout. No spinners
  that flash for under 300ms (delay showing them).
- **FP3** Optimistic UI for safe, reversible actions, with rollback and a clear message on
  failure.
- **FP4 Core Web Vitals**: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1. Reserve space for images and
  embeds (`width`/`height` or `aspect-ratio`). Lazy-load below the fold (`loading="lazy"`).
- **FP5** Performance is UX: budget JS, compress images (AVIF/WebP), test on a mid-range
  phone with a throttled network.

## 3. Error prevention & recovery (ER)

- **ER1 Prevent**: constraints, input masks only where they help, defaults, inline hints,
  and confirmation only for irreversible actions.
- **ER2 Message formula**: **what happened + why (if useful) + how to fix**. Plain language,
  never blaming the user, never only an error code.
  - Bad: "Error 422: Invalid input"
  - Good: "IC number should have 12 digits. You entered 11."
- **ER3 Recovery**: undo, trash/restore, version history, autosave and draft restore.
- **ER4 System errors**: keep the user's data, offer a retry, give a support path with a
  reference ID ("Something went wrong on our side. Your draft is saved. Try again, or contact
  support with ref 7F3K-21.").
- **ER5 Right altitude**: inline errors for field validation; a linked summary for multi-error
  submits; a banner for system errors; a full page only for route-level failures (404/500), and
  even those offer a way back.
