# Tailwind v4 tokens in Next.js

## Token file

```css
/* app/globals.css */
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));

/* raw palette from the approved visual plan (placeholders here) */
:root {
  --paper: #f7f8f6;
  --ink: #1c2421;
  --brand: #1f5c4a;
  --brand-ink: #f7f8f6;
  --danger: #b42318;
  --radius: 0.5rem;
}
.dark {
  --paper: #121715;
  --ink: #e6ebe8;
  --brand: #3d9a7d;
  --brand-ink: #0d1210;
}

/* semantic tokens -> utilities (inline because they reference variables) */
@theme inline {
  --color-background: var(--paper);
  --color-foreground: var(--ink);
  --color-muted-foreground: color-mix(in oklab, var(--ink) 65%, transparent);
  --color-primary: var(--brand);
  --color-primary-foreground: var(--brand-ink);
  --color-danger: var(--danger);

  --radius-control: var(--radius);
  --radius-lg: var(--radius);
  --radius-md: calc(var(--radius) - 2px);
  --radius-sm: calc(var(--radius) - 4px);

  --font-sans: var(--font-body);
  --font-display: var(--font-heading);
}

@theme {
  --spacing: 4px; /* 4pt grid (L1) */
}

@layer base {
  body { @apply bg-background text-foreground; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

Notes:
- This is the same shape shadcn/ui uses: role-named variables (`background`, `foreground`,
  `primary` / `primary-foreground`, `muted`, `accent`, `destructive`, `border`, `ring`, ...)
  with a `.dark` override and a radius scale derived from one `--radius` (lg = radius, md =
  radius - 2px, sm = radius - 4px). When a project starts from shadcn's neutral defaults,
  **replace them with the approved palette**; leaving them is AD4/AD6 territory.
- Extend the UI library already in the project (shadcn/ui, MUI, ...); never add a second one.
- Dark mode is a designed palette, not an inversion (C4). Re-check contrast for every pair.
- `--color-*: initial;` inside `@theme` removes Tailwind's default palette so only system
  colours compile. Use it once the system is stable.

## Fonts with next/font

```tsx
// app/layout.tsx
import { Instrument_Sans, Young_Serif } from "next/font/google";

const body = Instrument_Sans({ subsets: ["latin"], variable: "--font-body", display: "swap" });
const heading = Young_Serif({ subsets: ["latin"], weight: "400", variable: "--font-heading", display: "swap" });

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${body.variable} ${heading.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

`lang` is set on `<html>` (A10); for BM pages use `lang="ms"`. Fonts are examples; choose them in
the visual plan (max two families, T5).
