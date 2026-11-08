# Adapter: React Native · Expo · SwiftUI · Flutter

Native/cross-platform mobile. The overriding rule: **honor each platform's conventions** (iOS HIG,
Android Material) rather than shipping one look on both. Pair with the mobile playbook in the user-first-ux skill (`domains/mobile-ui.md`) and
the mobile playbook in the user-first-ux skill (`domains/mobile-ui.md`).

## React Native / Expo

- **Components** — `View`/`Text`/`Pressable`/`FlatList`; no CSS — style objects / `StyleSheet` /
  NativeWind (Tailwind-for-RN) / a UI kit (Tamagui, gluestack, RN Paper). Extend the one in use.
- **Tokens** — a shared theme object (colors as roles, spacing, radius, type scale) consumed by all
  components; no hardcoded values scattered in style props. → `../../../ui-design-system/references/token-architecture.md`.
- **Platform adaptation** — `Platform.select`/`Platform.OS` for iOS vs Android specifics; use
  platform-appropriate navigation (bottom tabs, native stack via React Navigation/Expo Router).
- **Safe areas** — `react-native-safe-area-context`; respect notches/home indicator.
- **Lists at scale** — `FlatList`/`FlashList` with virtualization; skeletons for loading.
- **A11y** — `accessibilityLabel`/`accessibilityRole`/`accessibilityState`; support Dynamic Type / font
  scaling (`allowFontScaling`); reduced motion (`AccessibilityInfo`). → the user-first-ux accessibility floor (`ui-accessibility` skill).
- **Motion** — Reanimated / `Animated`; native-driver transforms; haptics via Expo Haptics for real
  events only. → M1 (`../../../../references/shared/visual-system.md`).

## SwiftUI (iOS/Apple)

- **Native-first** — system components, SF fonts, **SF Symbols**, standard nav/tab/sheet patterns. This
  is where **Liquid Glass** (the control layer) belongs — `../../../ui-styles/references/styles/liquid-glass.md`. Verify current HIG.
- **Dynamic Type** — use text styles (`.font(.body)` etc.), not fixed sizes, so layouts scale; test
  large accessibility sizes.
- **VoiceOver** — accessibility labels/traits/values; logical focus order.
- **Layout** — stacks + `Grid`, safe-area aware, adapt to size classes (iPhone/iPad, orientation).
- **Tokens** — a theme (colors via asset catalog / `Color` extensions supporting light/dark, spacing
  constants, a type ramp). Support dark mode via the asset catalog, not hardcoded colors.

## Flutter

- **Widgets** — Material or Cupertino; `ThemeData`/`ColorScheme` is the token system — define seed/roles
  there and let widgets consume it (support `ThemeMode` light/dark). Don't hardcode colors in widgets.
- **Platform feel** — Material on Android, Cupertino widgets on iOS where fidelity matters; adapt, don't
  ship identical.
- **Layout** — `MediaQuery`/`LayoutBuilder` for responsive/safe-area; `textScaleFactor` support so text
  scaling doesn't clip. `Semantics` widgets + labels for screen readers.
- **Motion** — implicit/explicit animations, transform/opacity, honor reduced motion
  (`MediaQuery.disableAnimations`). → M1 (`../../../../references/shared/visual-system.md`).

## Common failure modes (all)

One look on both platforms · hardcoded colors/sizes instead of a theme · fixed text sizes that break
Dynamic Type / font scaling · ignoring safe areas · hidden gesture-only actions · non-virtualized long
lists · missing accessibility labels · permission prompts with no priming (the mobile playbook in the user-first-ux skill (`domains/mobile-ui.md`)).
