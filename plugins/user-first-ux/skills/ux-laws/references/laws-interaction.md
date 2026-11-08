# Laws of Interaction & Performance

Motor effort, speed, input tolerance and uninterrupted work. Read when placing or sizing
actions, handling loading and submit states, validating input, or designing long tasks.

## Contents
1. Fitts's Law `[Fitts]`
2. Doherty Threshold `[Doherty]`
3. Postel's Law `[Postel]`
4. Flow `[Flow]`

---

## Fitts's Law  [Fitts]
**Definition:** The time to hit a target depends on its distance and its size.
**Origin:** Paul Fitts, 1954.
**Why it matters:** Small or distant targets cost time and cause mis-taps, worst on touch.
**Rules:**
- One primary action per view, large and close to where attention already is: after the
  last field, in the page header, or in the thumb zone on mobile.
- Never make the primary action tiny, icon-only, hidden in an overflow menu, or tucked in a far corner.
- Touch targets: A7 in `../../user-first-ux/references/accessibility.md` (AA minimum and house
  floor). At least 8px between adjacent targets (Material Design guidance).
- Keep destructive actions away from frequent ones (different position, never adjacent to Save).
- Screen edges and corners are "infinite" targets for OS-level menus on desktop; in web
  content, do not put the primary CTA in a far corner.
**Do:** Full-width "Save invoice" button under the last field on mobile; `min-h-11` (A7 house floor).
**Don't:** Save as a 28px icon inside a top-right "⋯" menu, next to Delete.
**Audit check:** Can the user reach the primary action without hunting, scrolling back or precise aiming?
**Common violations:** primary in an overflow menu · Save beside Delete · 32px row actions on mobile · tiny close icons.
**Misuse warning:** Making every button big removes hierarchy. Size the primary up; keep the rest normal (see Von Restorff).

## Doherty Threshold  [Doherty]
**Definition:** Productivity rises sharply when system response is under about 400ms.
**Origin:** Walter J. Doherty & Ahrvind J. Thadani, IBM Systems Journal, 1982. The 0.1s / 1s / 10s
response-time limits below come from Jakob Nielsen (1993), building on Robert Miller (1968).
**Why it matters:** Waiting breaks attention; users repeat clicks or leave.
**Rules:**
- Acknowledge every action within 100ms (pressed state, spinner on the button).
- Show the result within 400ms, or show a skeleton or progress indicator.
- Show determinate progress (percent or steps, with an estimate) for waits over ~10s, and let users keep working.
- Use optimistic UI only for safe, reversible actions, with rollback and a message on failure.
- Disable double-submit; keep the button width stable while loading.
**Do:** Button shows a spinner and "Saving…", stays the same width, ignores repeat clicks.
**Don't:** A button that does nothing visible for 2 seconds, then submits twice.
**Audit check:** Does every action give feedback within 100ms and a result or progress indicator within 400ms?
**Common violations:** no loading state on submit · full-page spinner for a small update · layout shift when content loads.
**Misuse warning:** Laws of UX notes that a deliberate delay can make a process feel more
thorough. Only show work that is really happening (e.g. "Checking 3 suppliers…"); never pad a
fast response to look busy.

## Postel's Law  [Postel]
**Definition:** Be liberal in what you accept and conservative in what you send.
**Origin:** Jon Postel, 1980 (RFC 761, TCP): "be conservative in what you do, be liberal in what you accept from others" (the Robustness Principle).
**Why it matters:** Rejecting reasonable input blames users for the system's rigidity.
**Rules:**
- Accept varied input formats and normalise them in the system: phone with or without
  dashes, spaces or `+60`; dates in common formats; pasted IC numbers; trailing spaces; any case in email.
- Display output in one clear, consistent format.
- Error messages are specific and recoverable: what happened + how to fix it; keep what the user typed.
**Do:** Accept `012-345 6789`, `0123456789` and `+60123456789`; store E.164; display `012-345 6789`.
**Don't:** "Invalid phone number" because the user typed a dash.
**Audit check:** Will reasonable variations of input be accepted, and are errors specific and recoverable?
**Common violations:** rejecting spaces in card numbers · case-sensitive email matching · clearing the form on error.
**Misuse warning:** Liberal acceptance is not unvalidated acceptance. Normalise first, then
validate strictly on the server and define clear boundaries; input that cannot be interpreted
is rejected with a specific message. (RFC 9413, 2023, documents how unchecked tolerance causes
security and interoperability problems.)

## Flow  [Flow]
**Definition:** A state of full immersion that arises when challenge matches skill and feedback is immediate.
**Origin:** Mihaly Csikszentmihalyi, 1975 (*Beyond Boredom and Anxiety*; popularised in *Flow*, 1990).
**Why it matters:** Interruptions break concentration and cost far more than their own duration.
Too hard leads to frustration; too easy leads to boredom.
**Rules:**
- No unrelated modals, promos, surveys or upsells in the middle of a task.
- Give immediate feedback on each step.
- Match difficulty to expertise: guidance for novices, shortcuts for experts
  (keyboard shortcuts, bulk actions, saved filters) without cluttering the novice view.
**Do:** Bulk-select rows and approve them; keyboard shortcut shown in the button's tooltip.
**Don't:** A newsletter popup halfway through a registration form.
**Audit check:** Can the user complete the task without unrelated interruptions?
**Common violations:** modals on page load · rating prompts mid-checkout · no bulk actions for repetitive admin work.
