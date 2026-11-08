# Spatial UI

> Requires current care: spatial platforms (Apple visionOS, other AR/VR/MR headsets) evolve
> quickly. Verify current platform guidance (e.g. Apple visionOS Human Interface Guidelines
> at developer.apple.com/design) before building native XR. This skill is grounded in that
> guidance; specifics change.

## Definition — six distinct levels (never conflate)
1. **Conventional 2D UI using depth cues** — shadows, layering, parallax on a flat screen.
   Not spatial computing; just depth as a visual device.
2. **Pseudo-spatial web UI** — 3D transforms, WebGL scenes, faux-parallax on a normal
   website. Evokes space; still a 2D screen experience.
3. **True spatial computing** — content placed in the user's real space with real depth,
   scale, and anchoring (e.g. visionOS windows/volumes/immersive spaces).
4. **AR** — virtual content overlaid on the real environment.
5. **VR** — fully virtual immersive environment.
6. **Mixed reality (MR)** — virtual and real interact (occlusion, physics, passthrough).

**Do not apply true spatial-computing assumptions to an ordinary website.** If a standard web
project asks for "spatial," deliver a web-appropriate interpretation (levels 1–2) unless
genuine XR capabilities are requested — then use the platform's native tools (level 3–6).

## Conceptual model
Spatial computing places UI in **3-D space around the user** instead of on a rectangle. The
organizing ideas are depth, scale, distance, and anchoring; input shifts from click/tap to
**gaze + pinch, hands, and voice**; and **human comfort and ergonomics become first-class
design constraints** (fatigue, motion sickness, neck strain, field of view). It works when
the task genuinely benefits from space (3-D content, presence, multi-window work, immersive
experiences); it fails when it's a gimmick, when it ignores comfort, or when a flat task is
forced into 3-D.

## Spatial grammar (native XR)
- **Windows, volumes, immersive spaces:** 2-D windows for app content; bounded 3-D volumes
  for objects; fully immersive spaces when presence matters. Choose the smallest container
  that fits the task.
- **Depth, scale, distance:** place content at comfortable reading distance and size; use
  depth to organize, not to show off; respect that far/small content is hard to read.
- **Anchoring:** anchor to the world, to a surface, or to the user; decide deliberately
  (world-locked vs head-locked) — head-locked UI that follows the gaze can nauseate.
- **Field of view & comfort zone:** keep primary content within a comfortable FOV; avoid
  forcing large head/eye movement; avoid content too close.
- **Occlusion & environment awareness (AR/MR):** respect real objects, lighting, and depth;
  don't block the user's real world unsafely.
- **Focus & selection feedback:** because gaze targets, elements must show **hover/focus on
  gaze** clearly and provide strong selection feedback (the user can't see a cursor).
- **Motion & comfort:** minimize large/rapid motion, acceleration, and vection; provide
  comfort options; keep transitions gentle.
- **Spatial audio:** use sound to indicate position/feedback where relevant.

## Input models
- **Gaze + pinch (visionOS):** look to target, pinch to select — targets must be large,
  well-spaced, and give clear gaze-focus feedback.
- **Hands/direct touch:** for near content; respect ergonomics (don't make users hold arms
  up — "gorilla arm").
- **Voice:** for commands and text entry; provide affordances and feedback.
- **Pointer/controller:** on headsets that use them; still needs large targets and feedback.
Design for the platform's primary input; don't assume a mouse.

## Design tokens / parameters
- **Style-defining (native):** depth/elevation in real units, comfortable size at distance,
  glass/vibrancy material for windows, gaze-focus emphasis, spatial-audio cues.
- **Web interpretation:** perspective, layered depth/parallax, 3-D transforms or WebXR
  scene, subtle motion, still-flat fallbacks.
- **Product-dependent:** content, brand, and the underlying 2-D style for window content.

## Component translation
Native XR: app content lives in **windows** (use the platform's standard materials and
controls); 3-D objects live in **volumes**; large targets, generous spacing, clear gaze
focus, and ornament restraint. Web interpretation: hero depth/parallax, a 3-D product
viewer, layered scenes — but keep core content readable on a flat screen and provide a
non-3-D path.

## Brand vs product mode
See `../brand-vs-product.md`. **Brand/web:** a spatial *feel* (depth, parallax, a 3-D
hero) can be a memorable marketing device — keep it performant and accessible with a flat
fallback. **Product/native XR:** prioritize comfort, legibility at distance, large gaze
targets, and long-session ergonomics over spectacle.

## When to use
Genuine XR products (visionOS/AR/VR/MR) where space aids the task (3-D content, presence,
multi-window, training, spatial data); web experiences wanting an immersive brand moment
(with restraint and fallback).

## When NOT to use
Ordinary flat tasks forced into 3-D; a normal website treated as true spatial computing; any
context where 3-D harms readability, performance, or accessibility; users prone to motion
sickness without comfort options; forms/data-entry that are simpler in 2-D.

## Anti-patterns
- **True-XR assumptions on a website** — Tell: designing a normal site as if it were
  visionOS. Why: wrong platform/input model. Fix: deliver a web interpretation; reserve XR
  patterns for XR.
- **Gimmick 3-D** — Tell: `rotateX`/perspective tilt and floating cards for flair. Why:
  harms readability and targets, gains nothing. Fix: remove unless depth carries meaning.
- **Comfort ignored** — Tell: rapid motion, head-locked UI, content too close/far. Why:
  fatigue and motion sickness. Fix: gentle motion, world/surface anchoring, comfortable
  distance and FOV.
- **Tiny/tight targets in XR** — Tell: small close-together gaze targets. Why: gaze+pinch
  needs big, spaced targets. Fix: enlarge and space them; strong gaze-focus feedback.
- **No flat fallback (web)** — Tell: content only works in the 3-D scene. Why: excludes
  non-XR/low-power/AT users. Fix: readable 2-D fallback and reduced-motion path.

## Accessibility
Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

Plus XR-specifics: large well-spaced targets;
strong non-color focus/selection feedback for gaze; motion/comfort options and reduced-motion
honored; alternatives to gaze/hand input (voice, pointer, dwell) where the platform allows;
readable size at distance; captions/labels for spatial audio; and a non-immersive fallback on
the web. Motion comfort is an accessibility issue, not a preference.

## Responsive / cross-context
Design for the platform's spatial capabilities; on the web, degrade gracefully: full spatial
(WebXR) → pseudo-spatial (3-D/parallax) → flat 2-D fallback, choosing by capability and by
`prefers-reduced-motion`. Test on device where possible; simulators miss comfort issues.

## Performance
3-D scenes, WebXR, large textures, and continuous motion are expensive and battery-heavy.
Budget polygons/textures; avoid unnecessary continuous animation; provide quality tiers and a
flat fallback; profile on real devices (dropped frames in XR cause discomfort, not just lag).

## Implementation guidance
- **Native XR:** use the platform frameworks (visionOS: SwiftUI/RealityKit windows, volumes,
  immersive spaces; other headsets: their SDKs). Use system materials and standard controls;
  don't hand-roll spatial affordances.
- **Web:** WebXR for real immersion where supported; CSS 3-D/`perspective` or a WebGL/Three.js
  scene for pseudo-spatial; always keep a readable flat layer and a reduced-motion path. Don't
  swap the project's stack for a 3-D engine without authorization.

## Review checklist
- [ ] Correct level identified (2D cues / pseudo-spatial web / true XR) and matched to the
      platform and request — no true-XR assumptions on a plain website.
- [ ] Targets large and well-spaced; strong gaze/selection focus feedback.
- [ ] Comfort: gentle motion, sensible anchoring, comfortable distance/FOV; reduced-motion
      and comfort options honored.
- [ ] Readable at distance; spatial audio captioned/labeled.
- [ ] Web: graceful degradation to a flat, accessible fallback; performance budgeted.
- [ ] Depth carries meaning — not gimmick 3-D.

## Examples
- **Good/native XR:** a visionOS app with a 2-D content window plus a bounded volume for a
  3-D model, large gaze targets, gentle transitions, and comfort options.
- **Good/web interpretation:** a product site with a subtle depth/parallax hero and an
  interactive 3-D viewer, fully usable (and readable) as flat 2-D with reduced motion.
- **Bad:** a marketing site built with tilting perspective cards and forced 3-D that hurts
  readability, called "spatial computing."
