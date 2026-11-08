# Testing approach

Order matters: start where failures are most common and most harmful.

1. **Contrast.** Every text/background pair, focus indicator and UI boundary. Record
   foreground, background, ratio, requirement.
2. **Keyboard only.** Tab, Shift+Tab, Enter, Space, arrows, Esc. Check order, visibility,
   traps, focus not obscured, focus return after dialogs.
3. **Automated scan.** axe or Lighthouse. Catches roughly 30% of issues; treat it as a floor.
4. **Zoom and reflow.** 200% zoom and 320px width; text-spacing override; forced-colors /
   high-contrast mode.
5. **Screen reader.** NVDA (Windows) or VoiceOver (macOS/iOS): names, roles, states, heading
   list, landmarks, live-region announcements. Without a real screen reader, reason from the
   markup and mark the result **not verified**.
6. **Forms and errors.** Labels, instructions, error text tied with `aria-describedby`, focus
   moves to the first error or the summary, input kept.
7. **Motion and media.** Reduced motion honoured; no autoplay without controls; no flashing.

Fix blockers first, then rank by how many people are affected and how badly. A review cannot
replace testing with people who use assistive technology; recommend it for anything that ships.

## With Playwright MCP (when available)

- `browser_navigate` to the page, `browser_snapshot` for the accessibility tree (names, roles).
- `browser_press_key` Tab repeatedly, snapshotting focus, to record tab order.
- `browser_resize` to 320px width and `browser_evaluate` to set `document.body.style.zoom` or
  check `scrollWidth > clientWidth` for horizontal overflow.
- `browser_emulate_media` to emulate reduced motion and a dark colour scheme (check the tool's
  schema for the exact parameter names).
- `browser_evaluate` with `getComputedStyle` to read colours for contrast maths.
