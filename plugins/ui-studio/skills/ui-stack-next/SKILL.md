---
name: ui-stack-next
description: >-
  Implements and themes UI in Next.js App Router with React 19, TypeScript, Tailwind CSS v4
  (@theme tokens in app/globals.css), Radix UI primitives (radix-ui) and lucide-react icons. Use
  whenever the work touches *.tsx or *.jsx, app/ routes, layout.tsx, page.tsx, a "use client"
  boundary, a Radix Dialog, Popover, DropdownMenu, Tabs or Tooltip, shadcn-style components,
  next/font, or requests like "build this component in Next", "where should the client boundary
  go", "the dialog loses focus", "theme our Tailwind v4 tokens", "add reduced motion to this
  React animation", "icon button needs a label". Covers server vs client components, focus
  management, focus-visible, prefers-reduced-motion and every component state in React. Not for
  Laravel, Blade, Livewire or Filament (ui-stack-laravel) and not for choosing the visual
  direction itself (ui-visual-direction).
argument-hint: "<component, route or task>"
---

# Next.js stack: tokens, primitives, boundaries

Frame: `${CLAUDE_PLUGIN_ROOT}/references/shared/priority-workflow.md`. Floor and the eight
states: `${CLAUDE_PLUGIN_ROOT}/references/shared/quality-floor.md`. Read the project first:
`package.json` (next, react, tailwindcss, radix-ui versions), `app/globals.css`,
`components/`, `components.json` if shadcn is used. Reuse existing primitives before adding one.
If installed versions differ from those named here, check that version's docs.

## Which reference to load

| Task | Load |
|---|---|
| Tokens in Tailwind v4, dark mode, shadcn-style variables, fonts | `references/tailwind-v4-theme.md` |
| Dialog, Popover, Menu: focus management and a11y with Radix | `references/radix-dialog-focus.md` |
| Server vs client components, where state and handlers go | `references/rsc-boundaries.md` |
| Focus rings, reduced motion, lucide icons | `references/motion-and-focus.md` |

## Non-negotiables in this stack

1. **Tokens in `@theme`** (`app/globals.css`); components use utilities or `var(--...)`.
   No hex or arbitrary values in `*.tsx` (the plugin hook warns on these).
2. **Server components by default.** Add `"use client"` only to the smallest leaf that needs
   state, effects, event handlers or browser APIs.
3. **Use Radix for overlay and composite widgets** (dialog, popover, menu, tabs, tooltip,
   select). Do not hand-roll focus traps or roving tabindex.
4. **Every component state** from the quality floor, including `focus-visible`, `disabled`
   with a reason, loading via `useFormStatus` / `useTransition`, and empty and error UI
   (route-level `loading.tsx` and `error.tsx` plus inline states).
5. **Reduced motion** on every animation (`motion-safe:` / `motion-reduce:` or the hook in
   `motion-and-focus.md`).
6. **Icons are not labels.** Decorative lucide icons get `aria-hidden`; icon-only buttons get
   an accessible name (B5).
7. **Locale.** `Intl.NumberFormat` / `Intl.DateTimeFormat` with an explicit locale
   (`en-MY` / `ms-MY`); see the `ui-ux-copy` skill (user-first-ux plugin) for BM/EN strings.

## Minimal example: a form submit button with all states (React 19)

```tsx
"use client";
import { useFormStatus } from "react-dom";
import { Loader2 } from "lucide-react";

export function SubmitButton({ children, disabledReason }: {
  children: React.ReactNode;
  disabledReason?: string;
}) {
  const { pending } = useFormStatus();
  const disabled = pending || Boolean(disabledReason);
  return (
    <div className="flex items-center gap-3">
      <button
        type="submit"
        disabled={disabled}
        aria-describedby={disabledReason ? "submit-why" : undefined}
        className="inline-flex min-h-11 items-center gap-2 rounded-control bg-primary px-4 text-sm font-medium text-primary-foreground
                   transition-colors hover:bg-primary/90 active:bg-primary/80 motion-reduce:transition-none
                   focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary
                   disabled:cursor-not-allowed disabled:opacity-60"
      >
        {pending && <Loader2 aria-hidden className="size-4 motion-safe:animate-spin" />}
        {pending ? "Saving..." : children}
      </button>
      {disabledReason && <p id="submit-why" className="text-sm text-muted-foreground">{disabledReason}</p>}
    </div>
  );
}
```

## Review checklist for a Next.js component

- [ ] Smallest possible `"use client"` surface; no data fetching moved to the client without reason
- [ ] Tokens only; no hex, arbitrary values or inline `style` except dynamic geometry
- [ ] Radix used for overlays; Title present; focus returns to the trigger
- [ ] Every state, including loading, empty and error
- [ ] `focus-visible` styles on every custom interactive element
- [ ] Reduced motion handled; no `transition-all`
- [ ] Icon-only controls named; decorative icons hidden
- [ ] Works at 320px and 200% zoom; targets at the house floor (quality floor)
