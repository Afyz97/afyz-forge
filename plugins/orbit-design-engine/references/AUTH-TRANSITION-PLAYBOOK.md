# Authentication diagonal-sweep motion — implementation playbook

Reference E shows a distinctive panel-wipe switch. Treat this playbook as **derived design instructions**, not reconstructed source.

## Build stages
1. **Shell**: keep rounded viewport stable (no route-change layout shift); size via `min-height`, grid and responsive constraints.
2. **Scenes**: build `signin` and `signup` scenes with reciprocal placement of the host theme’s form and hero surfaces, each containing semantically complete, separately validated forms. Each scene owns a branded editorial message; do not reuse actual credential values across modes accidentally.
3. **Moving seam**: choose one shared diagonal reveal over the *entire inner card*. Can use a skewed `.blade` with a counter-transformed `.blade__inner`, or implement a polygon clip-path reveal over an incoming complete scene. Never animate form widths individually.
4. **Timeline**: animate from one edge to the other with controlled lag for incoming text. At midpoint, majority of old card is occluded by a large diagonal overlay derived from the host theme. Finish by exposing the reverse arrangement. Repeat symmetrically in reverse.
5. **Interaction handoff**: handle switch only from explicit button. While playing, lock repeated activation and temporarily make old/new inactive as appropriate. At `animationend`, set `inert`/`aria-hidden` on outgoing panel, activate and focus the incoming panel.
6. **Form workflows**: validate and submit via real backend; failed credentials keep current form visible, announce errors; never switch modes just because a network call failed.
7. **Reduced motion + mobile**: avoid sweeping on `prefers-reduced-motion: reduce`; directly present the destination form. Constrain translated layers; mobile form should not need horizontal scroll.

## Recommended timing targets (original implementation values)

| Phase | Intended behaviour | Suggested target |
|---|---|---|
| click | immediate button pressed/selection feedback | 0–80ms |
| blade enters | diagonal leading edge becomes visible | 0–120ms |
| traverse | covers old form while new state is revealed | 120–620ms |
| settle | new copy and fields complete entrance; focus transfers | 620–780ms |
| opposite direction | mirrored travel and handoff | ~same duration |

Use `cubic-bezier(.68,0,.22,1)` for a controlled strong ease-in/out. These values were **not measured** from the recorded code.

## Geometry alternatives

**A. Skew/counter-skew.** Absolute positioned oversize overlay translated across the clipping card: outer transform `translateX(...) skewX(...)` (or `skewX(...) translateX(...)` with calibrated geometry); inner layer uses the inverse skew, preventing text from skewing. Need careful stacking order and mobile bounds.

**B. Clip-path reveal (demo implementation).** Stack two complete scenes and animate the visible polygon of the *incoming* scene. At midpoint, the leading edge's top intersection precedes/trails the bottom by ~10–16% of card width. Reverse animation mirrors geometry. Use fixed polygon point counts for interpolation; avoid animating `display`.

## Frame-based QA
Capture: start of switch, ~25%, midpoint, ~75%, settled, reversed midpoint and final. Verify the diagonal edge moves monotonically, form never appears half-clickable, outer frame stays fixed, no flash of source state, and text isn't stretched/skewed. Check both at desktop and 360px width, and turn on reduced motion.

## Technology adaptation
- Laravel Blade: native CSS + modest JS, route forms through existing Laravel auth and CSRF; don't change server endpoints. Blade/Livewire morphing can replace nodes mid-animation: use a stable outer wrapper and cleanup on navigation.
- React: state machine and `animationend`/Web Animations cleanup; avoid stale asynchronous setState after unmount. Let existing auth provider handle credentials.
- No animation library required. GSAP is optional if already in your app, but must respect `prefers-reduced-motion` and `.kill()` timelines when needed.

**See:** `examples/auth-diagonal-wipe-demo.html`, `assets/auth-motion-tokens.css`, `AUTH-VIDEO-AUDIT.md`, `AUTH-VISUAL-QA.md`.
