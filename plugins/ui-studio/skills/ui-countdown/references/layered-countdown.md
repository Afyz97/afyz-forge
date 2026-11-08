# Layered radial countdown - reusable motion specification

## Reference observation

Observed from a short screen recording of a public recognition/nomination page: a hero and horizontal event-phase timeline sit above a contained countdown area. Several nested curved arcs progress around a central remaining-days label; nearby counters show other time units and update as seconds pass. Small accents around the arcs reinforce the composition. A featured award showcase changes content later in the recording.

The recording is a **reference for layout, behaviour, and motion**, not a request to reproduce its text, colours, identity, or exact artwork.

## Architecture

Use one time model and multiple visual projections:

- `deadlineInstant`: authenticated/specified end instant, not a formatted date string.
- `startInstant` (optional): required for a truthful completion percentage.
- `serverClockOffsetMs` (optional): establishes a corrected wall-clock estimate.
- `remainingMs`: `max(0, deadlineInstant - correctedNowInstant)`.
- `units`: integer day/hour/minute/second values derived from `remainingMs`.
- `overallFraction`: computed only when `startInstant` is known and valid.
- `unitFractions`: explicit modulo fractions with their own labels, if used.
- `phase`: separate, authoritative event status when workflow rules demand server confirmation.

A rendering loop may interpolate between authentic values, but never maintain an independent invented countdown.

## UI composition

1. Short context label and event title.
2. A timeline with completed, current, and upcoming milestone nodes, with accessible text labels and dates.
3. A countdown panel with an eyebrow label (e.g. 'Submissions close in'), central primary unit, radial multi-ring visualization, and smaller time-unit values.
4. Short supporting explanation, explicit deadline including timezone, optional elapsed-window progress *only if both endpoints are known*.
5. A nearby primary action, enabled/disabled according to actual permissions and cutoff rules.
6. An honest state when the deadline is expired or cannot be confirmed.

### Responsive strategy

- Wide screens: central radial figure with supporting units in an adjacent column; timeline spans available width.
- Medium screens: use balanced radial / adjacent units without clipped labels.
- Narrow screens: radial graphic first, units below in a compact grid and timeline as a readable vertical or horizontally scrollable stepper with visible cues. Avoid a miniature desktop site.

## Choreography

- On enter: fade in layout subtly; draw arcs toward current values, with short stagger only if it helps comprehension.
- At each second rollover: update the seconds label instantly and allow a restrained arc transition to the new accurate fraction. Avoid bouncing every second.
- At minute/hour/day rollover: update higher units without moving nearby labels; use numerals with fixed width.
- Continuous decoration: optional slow endpoint glint or restrained rotation, visually separated from the actual measured arc. It must not appear to count down faster or slower than real time.
- At expiration: snap the time model to zero, then settle animations and replace panel content with the true event state.
- Reduced motion: no entrance sweeps, auto-rotation, glints, or automatic gallery transitions. Maintain legible, instantaneous state updates.

## Framework-neutral pseudocode

```js
function getCountdown(deadlineEpochMs, correctedNowEpochMs) {
  const remainingMs = Math.max(0, deadlineEpochMs - correctedNowEpochMs);
  const totalSeconds = Math.ceil(remainingMs / 1000);
  return {
    remainingMs,
    days: Math.floor(totalSeconds / 86400),
    hours: Math.floor((totalSeconds % 86400) / 3600),
    minutes: Math.floor((totalSeconds % 3600) / 60),
    seconds: totalSeconds % 60,
    expired: remainingMs === 0,
  };
}
function elapsedFraction(startEpochMs, deadlineEpochMs, nowEpochMs) {
  if (!(deadlineEpochMs > startEpochMs)) return null;
  return Math.min(1, Math.max(0, (nowEpochMs - startEpochMs) / (deadlineEpochMs - startEpochMs)));
}
```

Use a scheduled update tied to clock boundaries when practical, or a suitably modest interval if implementation simplicity matters. Recompute from the clock on each update and upon visibility/focus/resume. If server time matters, resynchronize periodically through existing application infrastructure.

## SVG approach

- A circular track and progress path may be represented with `stroke-dasharray`, `stroke-dashoffset`, and rotations based on real values.
- Separate radii so individual rings are recognizable. Provide semantic labels or an adjacent legend indicating what each represents.
- Use styles based on semantic theme tokens (`--theme-accent`, `--surface`, etc. are **illustrative placeholder names**, not new prescribed token names); use actual tokens defined in the host project.
- Keep strokes crisp across pixel densities and readable at mobile sizes.
- Keep the time text in accessible DOM rather than depending exclusively on SVG labels.

## Test matrix

- 00:00:01 to 00:00:00; 00:01:00 to 00:00:59; 24h to 23h59m59s.
- Earlier date, far future date, DST and timezone changes.
- Hidden background tab, screen lock, sleep, intermittent network.
- Server and device clock offsets, uncertain authoritative status.
- Narrow phone, large text, low-performance CPU, zoom and landscape.
- Screen reader and reduced-motion mode.
- All timeline labels and countdown units reflect the same data source.
