# Mobile UI

**Mobile is not compressed desktop.** It's a different context: one hand, one focus, on the move,
touch-driven, often interrupted. Design *for* it, and respect platform conventions.

## Ergonomics & touch

- **Thumb reach** — primary actions in the comfortable bottom zone; top corners are a stretch. This
  is why bottom tab bars and bottom sheets win on mobile.
- **Target size** — the house floor in `../accessibility.md` (A7); generous spacing between targets to
  prevent mis-taps. Small text links in a paragraph are hard to hit — give them room.
- **Gestures augment, don't replace** — swipe, pull-to-refresh, long-press are accelerators; always
  keep a visible, tappable path too. Hidden gesture-only actions aren't discoverable.
- **No hover** — never hide essential info or actions behind hover; there is no hover on touch.

## Navigation

- **Bottom tab bar** for 3–5 primary destinations; thumb-reachable, always visible, current tab
  marked (not color-only).
- **Bottom sheets** for contextual actions and secondary content — reachable and dismissible.
- **Back** must be obvious and consistent (platform back + in-app back where needed).
- Don't cram a desktop nav into a hamburger and call it done.

## Layout & input

- **Single column**, content prioritized top-down by importance.
- **Safe areas** — respect notches, home indicators, rounded corners, status bars (`env(safe-area-
  inset-*)` on web; platform safe-area APIs native).
- **Virtual keyboard** — it covers half the screen; keep the focused field and its submit visible;
  scroll focused input into view; use the right keyboard (`inputmode`/`type`, `autocomplete`,
  one-time-code). See F4 in `../components.md`.
- **Orientation** — handle landscape and short heights (keyboard open) without clipping.

## Platform conventions (don't fight them)

- **iOS (HIG)** — SF fonts, SF Symbols, standard nav/tab bars, sheets, expected gestures. Support
  **Dynamic Type** (layouts reflow as text scales) and **VoiceOver** (labels, order, traits).
- **Android (Material)** — Material components, FAB where it fits, system back, adaptive layouts,
  TalkBack. Support font scaling.
- Cross-platform (RN/Expo/Flutter) — adapt to each platform's conventions rather than shipping one
  look on both; use platform-native components where it matters. See the native-mobile adapter in ui-studio's **ui-visual-direction** skill, if installed.

## Onboarding & permissions

- **Progressive onboarding** — show value fast; don't gate the app behind a long tour. Teach in
  context.
- **Permission priming** — explain *why* before triggering the OS prompt (location, notifications,
  camera); ask at the moment of need, not at launch. A denied permission needs a recovery path.

## Motion & performance

Snappy, platform-appropriate transitions; haptics only for real events and only where supported;
respect reduced motion. Budget for mid/low-range devices — heavy effects that fly on a flagship
stutter elsewhere. Motion tokens: the **ui-studio** skill, if installed; performance: FP5 in
`../states-feedback.md`.

## Accessibility

Dynamic Type / font scaling (don't hardcode sizes that clip), screen reader (VoiceOver/TalkBack)
labels and order, contrast, target size, reduced motion, sufficient tap spacing. See `../accessibility.md`.

## Common AI failure modes

Collapsed-desktop layout · tiny targets · gesture-only actions with no visible path · nav hidden in a
hamburger · keyboard covering the focused field · ignored safe areas · one look on both platforms ·
permission prompts at launch with no priming · hardcoded text sizes that break font scaling.

## Order of work

1. Classify the platform (iOS, Android, cross-platform, mobile web), the user's context (one hand,
   on the move, interrupted) and the primary task.
2. Platform conventions, then ergonomics (thumb zone, bottom tabs for 3-5 destinations, sheets).
3. Layout (single column, safe areas, virtual keyboard), gestures with a visible path.
4. Onboarding and permission priming, then motion and performance on a mid-range device.
5. Accessibility (Dynamic Type, screen readers), then sizes within mobile: small and large phones,
   landscape with the keyboard open, tablet.
