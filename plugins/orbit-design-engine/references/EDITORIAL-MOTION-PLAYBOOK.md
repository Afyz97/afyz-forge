# Editorial kinetic UI motion — implementation recipes

Reference: `EDITORIAL-VIDEO-OBSERVATIONS.md`; storyboard images in `assets/editorial-video-reference/`. Timing below is a **suggested range**, not measured source timing. Durations should be shortened for routine application UI. Prefer named states and semantic transitions, not animation on every rerender.

## The motion grammar

**Scene skeleton:** `message headline` (upper region) + `optional n/N progress pill` + `one dominant illustrative UI card or layered stack` (center) + `optional mascot` (lower region) + `subtle atmosphere` (background). Keep the persistent elements pinned while only message/illustration/state changes. Repeating composition creates comprehension across many steps.

### 1. Kinetic phrase / editorial text reveal
- Trigger: first viewport entry, a storyboard step advance, a user-requested explainer sequence.
- Choreography: old phrase loses prominence through opacity 1→0, blur 0→4–8px, y 0→−8px; new phrase enters opacity 0→1, blur 6→0, y +12→0. Hold line baseline stable to prevent surrounding elements jumping. Introduce theme-accent italic focus phrase 80–180ms after main bold words. Highlight theme-derived highlight ribbon by scaleX(0→1) behind text.
- Recommendation: 240–440ms, easing `cubic-bezier(.2,.8,.2,1)`. Before/after text must be accessible in the DOM; change screen-reader announcement once per step, not for every word.
- App adaptation: heading changes on selected tab, wizard or filter only; no typewriter effect in ordinary headings.

### 2. Floating UI card + 2.5D layered overlay
- Trigger: mock product example enters, drawer preview opens, onboarding progresses.
- Choreography: primary card begins translateY(24–38px), scale(.92–.96), rotate(−2deg→0), opacity 0→1; a supporting document/sticker enters *later* at translateY(+20px), rotate(+4–8deg), and casts higher depth shadow. Foreground highlight follows 100–180ms later. Keep DOM interaction/keyboard order logical regardless of visual stacking.
- Recommended: card 380–620ms; sticker 280–430ms; stagger 70–130ms; ease-out or spring *one* small overshoot, no repeated bounce. Use transform/opacity only. For app modal: 160–250ms and no large rotation.

### 3. Anchored progress and success micro-reaction
- Trigger: actual step completion. Progress fill width changes to real `done/total`; visible integer updates after settled state. Completion check capsule scales .7→1.08→1.0 in 180–320ms. Tiny particles 2–4, max once per completion.
- Semantics: actual progress with `role=progressbar`, `aria-valuenow`, `aria-valuemax` and accessible status; don't pretend verification or saved state before server response. Numeric information must remain visible without animation.

### 4. Corrective typography and visual diagnosis
- Trigger: compare before/after practice or show a detected issue; not used for shameful/error alarm in production.
- Choreography: mark the unsafe term using the host’s semantic warning treatment, draw a line through it over 220–320ms, then reveal replacement phrase; old card becomes pale/ghosted or moves back, corrected UI moves forward. Preserve a clear, static final state and explanation.
- Good for: guided audit reports, interactive tutorials, validation explainers. Never use strike-through as the *only* indication of error.

### 5. Miniature UI control demonstration
- Trigger: highlight permission checkbox, focus traversal, unsubscribe link, tracking toggle, cancellation control.
- Choreography: a glowing ring or cursor travels *to* the control; the control responds in <160ms (press depth, focus ring, check/toggle); confirmation enters only after a true saved response. A line or arrow may be drawn with path-length animation in diagrams.
- For real apps, controls must be real semantic elements, not a video effect. Keyboard/touch interaction must work even without animation.

### 6. Diagram with relationships
- Trigger: visualizing consent, integrations, analytics SDKs, data flow.
- Choreography: root card enters → child nodes stagger 70–140ms → connecting line expands/draws → active route emphasized; nodes should remain legible if movement is disabled.
- Avoid drawing large SVG filters or expensive shadows per frame. Diagram should render as a static meaningful structure before motion begins.

### 7. Mascot cameo (optional)
- Trigger: welcome, tutorial entry, a purposeful warning, successful completion.
- Choreography: one eye blink, a one-time tilt or 3–7px hop, then idle. Use a custom **original** mascot if brand demands it; do not copy supplied character artwork. Hide or avoid decorative mascot in dense professional admin workflows. Keep reading order and focus unaffected.
- On reduced motion: static illustration or icon, zero bobbing.

### 8. Cross-scene choreography
- Rough explainer beat: 0–25% headline; 18–45% card entry; 40–75% callout / illustrative action; 70–100% resolution and progress; deliberately overlap, don't wait for every item to finish. Recommended scene hold 1.8–3.2s **only for an explicitly playing demo**. In interactive UI, progress is user-driven and must never auto-advance while typing, reading or consenting.
- When swapping scene, keep background/progress/brand anchors fixed. Cross-fade old card while new card enters from the same visual region rather than rebuilding the whole canvas.

## Token proposals and usage contexts

| Token | Work UI | Explainer/hero | Notes |
|---|---:|---:|---|
| hover/control feedback | 100–160ms | 120–180ms | Fast, consistent, meaningful |
| tab/filter change | 140–240ms | 240–380ms | Content should remain stable |
| modal/drawer | 160–260ms | 300–460ms | Focus remains correct |
| headline phrase change | rarely | 260–440ms | Avoid layout shifting |
| foreground 2.5D card | rarely | 380–620ms | Decorative, not workflow blocker |
| per-child stagger | 30–60ms | 70–140ms | Cap groups and total wait |
| progress confirmation | 120–220ms | 180–320ms | Never fake actual work |

Use CSS for light effects, Web Animations API or a motion library already in the project for orchestration. If user permits a new dependency, Framer Motion (React) or GSAP timeline are possibilities; do not assume a particular library is installed. Always clean up timeline/event observers on unmount. Prefer `transform`, `opacity`, `clip-path` sparingly; avoid continuous blur of full-screen surfaces, layout-property animation, flashing and excessive bouncing.

## Reduced motion, interaction and accessibility

Use `@media (prefers-reduced-motion: reduce)` to remove translation/parallax/blur, skip staging, retain readable static final states and ensure progress remains truthful. Respect `prefers-reduced-transparency` when feasible. On a video/demo provide pause/replay and never autoplay user-driven form choices. WCAG contrast; don't use hue or motion alone for feedback. Provide true focus state and avoid hidden links in float layers. Verify at 360px wide, desktop, keyboard-only, touch, slow network, and interrupted transitions.
