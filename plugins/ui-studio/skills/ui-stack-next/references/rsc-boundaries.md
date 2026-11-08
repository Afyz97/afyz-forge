# Server vs client components

## Default: server

Components in `app/` are Server Components unless the file starts with `"use client"`. Keep
data fetching, secrets, heavy formatting and static markup on the server.

## Add `"use client"` only when a component needs

- state or effects (`useState`, `useEffect`, `useReducer`, `useTransition`, `useOptimistic`)
- event handlers (`onClick`, `onChange`, ...)
- browser APIs (`window`, `matchMedia`, `localStorage`, `IntersectionObserver`)
- a Radix primitive or any component that uses context

Push the boundary down to the smallest leaf. A page that shows a table and one "Export" button
stays a server component; only `<ExportButton>` is a client component.

## Patterns

- **Children through the boundary.** A client wrapper (e.g. a Radix `Dialog`) can receive server
  components as `children`; they still render on the server.
- **Server Actions for mutations.** `<form action={createInvoice}>` + `useFormStatus` for the
  pending state + `useActionState` for returned errors. Errors render inline under fields (F5)
  and keep the user's input (F6).
- **Optimistic UI** with `useOptimistic` only for safe, reversible actions, with rollback and a
  message on failure (FP3).
- **Route states.** `loading.tsx` renders a skeleton matched to the final layout (FP2);
  `error.tsx` (a client component) explains what happened and offers a retry (ER4);
  `not-found.tsx` offers a next step.
- **Props across the boundary must be serialisable.** Pass ids and plain data, not class
  instances or functions (except Server Actions).

## Smells

- `"use client"` at the top of a `page.tsx` or `layout.tsx` "to make it work".
- `useEffect` + `fetch` for data the server could have loaded.
- Large icon or date libraries imported into client components when the server could render
  the result.
