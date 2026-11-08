# Focus, reduced motion and icons in React 19

## Focus

- Style `:focus-visible`, never remove `:focus` outlines without a replacement:
  `focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary`.
- Focus indicator contrast per the quality floor (WCAG 1.4.11). Not hidden under sticky
  headers (2.4.11): set `scroll-padding-top` on `html` equal to the header height.
- After route changes or async steps that replace content, move focus deliberately (e.g. to the
  new heading with `tabIndex={-1}` and `ref.focus()`), and announce status with `aria-live`.
- Never use positive `tabIndex`.

## Reduced motion

Prefer CSS: `motion-safe:` for anything that moves, `motion-reduce:transition-none` on
transitions. When JS drives animation (canvas, scroll effects, motion libraries), read the
preference with a hook:

```tsx
"use client";
import { useSyncExternalStore } from "react";

const query = "(prefers-reduced-motion: reduce)";

export function usePrefersReducedMotion() {
  return useSyncExternalStore(
    (onChange) => {
      const mql = window.matchMedia(query);
      mql.addEventListener("change", onChange);
      return () => mql.removeEventListener("change", onChange);
    },
    () => window.matchMedia(query).matches,
    () => true, // server snapshot: assume reduced until the client knows
  );
}
```

Use it to skip or shorten animation, never to remove the information the animation conveyed.
If the project uses Motion (formerly Framer Motion), its own `useReducedMotion` or
`<MotionConfig reducedMotion="user">` does the same.

Motion budget (DP5): one orchestrated non-user-triggered moment at most; no per-section
fade-ups; no hover transition on every card; avoid `transition-all`.

## lucide-react

```tsx
import { Download, Trash2 } from "lucide-react";

<button type="button" className="inline-flex items-center gap-2">
  <Download aria-hidden className="size-4" /> Download invoice (PDF, 2 MB)
</button>

<button type="button" aria-label="Delete invoice INV-0012" className="grid size-11 place-items-center">
  <Trash2 aria-hidden className="size-4" />
</button>
```

- Import icons by name (tree-shakes); never import the whole set.
- One stroke width and size scale across the product (G2); set them via class or the `size` /
  `strokeWidth` props consistently.
- Icons support a label, they rarely replace one (IC5). Status icons pair with text (C3).
