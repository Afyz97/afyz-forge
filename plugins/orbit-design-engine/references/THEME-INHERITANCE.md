# Theme inheritance and colour-neutral UI implementation

## Hard rule
Orbit Design Engine does **not** select or supply an application's colours. Never copy reference palettes. Never override host colour tokens or create new palette options. Theme source of truth is always the existing application.

## Inspection workflow
1. Identify stack (e.g., Bootstrap/AdminLTE, Tailwind/shadcn, Material UI, Chakra, design-system CSS, native CSS or custom theme provider).
2. Locate authoritative runtime theme tokens and persistence, including user-, company- and tenant-scoped themes.
3. Inventory semantic roles: canvas, surface, subdued surface, foreground, muted foreground, border, primary, on-primary, focus, success, warning, danger, chart series and overlay.
4. Determine theme differences for modes and user changes. Prefer shared components that already solve this.
5. Only then implement geometric styling and motion, referring to those exact project tokens.

## Alias strategy
The optional `assets/orbit-ui-foundation-tokens.css` defines `--ode-*` **aliases** using existing host variables and browser defaults for isolated previews. These aliases do not assign or modify your app's theme variables. Production should map aliases to the system's genuine semantic tokens or skip the stylesheet if native theme classes/components already exist.

Illustrative example (the variable identifiers are placeholders: replace with names discovered in the host project):
```css
.component {
  background: var(--existing-system-surface);
  color: var(--existing-system-foreground);
  border-color: var(--existing-system-border);
}
.component:focus-visible { outline-color: var(--existing-system-focus); }
```

Avoid inventing missing fallback values in production. If a semantic role is missing, prefer an existing styled component or ask the owner to map the role. Do not use screenshots as a palette source.

## Motion-specific integration
- Background wipes should use an existing emphasis/hero surface. The overlay and its text need host-provided contrast pairs.
- KPI highlights, chart strokes, positive/error indicators and progress animations should reuse the app's semantic tokens.
- Theme settings should list **only options the app already supports**. Never inject a sample palette or show misleading choice controls.
- Use `prefers-reduced-motion` (or equivalent host setting) to reduce or remove large motions without losing state changes.

## QA checklist
- Compare before/after computed styles for primary actions, text, page canvas, cards, borders, charts and focus rings across representative screens.
- Confirm no app-level theme configuration or persistence was changed without explicit instruction.
- Test every available light/dark/tenant theme, if any.
- Check contrast, statuses independent of hue, keyboard focus, hover, disabled and loading states.
- Verify the animation at start/midpoint/end and after interruptions, under the current application's active theme.
- Search changed frontend code for new literals and hardcoded visual theme values; if found, replace with host tokens.
