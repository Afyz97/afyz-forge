# Auth diagonal wipe — interaction and visual QA

- [ ] Match split composition: form/welcome sides are correct for each mode, background card radius/clipping remains constant.
- [ ] Animate **signin → signup** with diagonal *right-to-left* moving boundary, settle form on right.
- [ ] Animate **signup → signin** symmetrically with a *left-to-right* boundary, settle form on left.
- [ ] Record intermediate 25% / 50% / 75% transition screenshots; don't validate with final frames only.
- [ ] No form fields, labels, secrets or buttons appear broken, skewed, duplicated, clickable when hidden, or mislayered.
- [ ] Prevent double trigger/rapid switch races, cancel/restore when navigating away, and avoid stuck `is-transitioning` state.
- [ ] Only active form exposed to screen reader and keyboard; focus moves to active heading/input after complete, no focus theft while typing.
- [ ] On reduced motion: immediate complete state switch, no half-visible panel. No flashing or excessive blur.
- [ ] On mobile: visible form, no x-scroll, primary action reachable above keyboard, nonessential editorial block reduced.
- [ ] Both forms have `label`, required validation, correct autocomplete and real backend wiring (when production).
- [ ] Error, password-reset, keep-signed-in, pending/loading and failed-submit states behave correctly.
- [ ] Branding uses the app’s context and doesn't import the reference's brand. No fake auth or production exposure of demo data.
- [ ] Annotate QA result with screenshots, viewport, actual tests and limitations (what was not inspected).
