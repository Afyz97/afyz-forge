# Visual System

Hierarchy, layout, typography, colour and elevation rules (H1-H6, L1-L7, S1-S4, T1-T7, C1-C5, E1,
M1) and every token value are owned by ui-studio.

Tokens (spacing, type scale, colour, radius, icons, motion): follow the **ui-studio** skill if installed.
Minimum if not: one 4px spacing grid, one modular type scale (1.2–1.25), semantic colour tokens.

Two rules stay here because they are accessibility rules (priority 2):

- **C3** Never convey meaning by colour alone. Pair it with an icon, text or pattern. Charts
  must work for colour-blind users.
- **M2** Respect `prefers-reduced-motion`. Nothing auto-plays > 5s without a pause control.
  Auto-advancing carousels also pause on hover, focus and manual selection, and do not
  auto-advance under reduced motion. No flashing more than 3 times per second.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```
