# Radix Dialog with focus management

Radix gives you the WAI-ARIA dialog pattern: focus is trapped while open, Esc closes, and focus
returns to the trigger. Your job: a Title, a sensible initial focus, the safe action first for
destructive dialogs, and reduced motion.

```tsx
"use client";
import { useRef } from "react";
import { Dialog } from "radix-ui";   // or: import * as Dialog from "@radix-ui/react-dialog"
import { X } from "lucide-react";

export function DeleteInvoicesDialog({ count, onConfirm }: { count: number; onConfirm: () => void }) {
  const cancelRef = useRef<HTMLButtonElement>(null);

  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <button type="button" className="btn-danger">Delete {count} invoices</button>
      </Dialog.Trigger>

      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-foreground/40 motion-safe:data-[state=open]:animate-in motion-safe:data-[state=open]:fade-in" />
        <Dialog.Content
          className="fixed left-1/2 top-1/2 w-[min(92vw,28rem)] -translate-x-1/2 -translate-y-1/2 rounded-lg bg-background p-6 shadow-lg
                     focus-visible:outline-2 focus-visible:outline-primary"
          // initial focus on the safe action, not the destructive one (B4)
          onOpenAutoFocus={(e) => { e.preventDefault(); cancelRef.current?.focus(); }}
        >
          <Dialog.Title className="text-lg font-semibold">Delete {count} invoices?</Dialog.Title>
          <Dialog.Description className="mt-2 text-sm text-muted-foreground">
            They will be permanently deleted. This can't be undone.
          </Dialog.Description>

          <div className="mt-6 flex justify-end gap-3">
            <Dialog.Close asChild>
              <button ref={cancelRef} type="button" className="btn-secondary">Cancel</button>
            </Dialog.Close>
            <Dialog.Close asChild>
              <button type="button" className="btn-danger" onClick={onConfirm}>Delete invoices</button>
            </Dialog.Close>
          </div>

          <Dialog.Close asChild>
            <button type="button" aria-label="Close" className="absolute right-3 top-3 grid size-11 place-items-center rounded-md
                                                         focus-visible:outline-2 focus-visible:outline-primary">
              <X aria-hidden className="size-4" />
            </button>
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

Rules:
- `Dialog.Title` is required for the accessible name. If there is truly no description, pass
  `aria-describedby={undefined}` to `Content`; otherwise keep `Dialog.Description`.
- `onOpenAutoFocus` sets the first focus; `onCloseAutoFocus` overrides where focus returns
  (default is the trigger, which is usually right). `onEscapeKeyDown` can intercept Esc, e.g. to
  warn about unsaved changes, but never to trap the user.
- Modals only for short blocking decisions (CL2); prefer undo for reversible actions (B4,
  the destructive-confirm example in the user-first-ux skill).
- The animation utilities in the example (`animate-in`, `fade-in`) assume the
  `tw-animate-css` plugin used by shadcn; otherwise define keyframes in `@theme`. Either way,
  keep them under `motion-safe:`.
- The arbitrary width `w-[min(92vw,28rem)]` is geometry, not a design token; if the system
  defines dialog widths, use the token instead.
