# Components & Patterns

## Contents
1. Buttons & actions (B)
2. Forms (F) - highest-impact area
3. Pickers & selection (P)
4. Tables & data (TB)
5. Dashboards & data visualisation (D)
6. Cards, lists, modals, toasts (CL)
7. Search & navigation (SN)
8. Onboarding & empty states (O)

## 1. Buttons & actions (B)

- **B1** Labels are verb + object ("Save changes", "Send invoice"), not "OK" / "Submit".
- **B2** If a button is disabled, explain why nearby, or keep it enabled and validate on click.
- **B3** Loading state keeps the button's width, shows a spinner, and blocks double-submit.
- **B4** Destructive actions: prefer **undo** over confirmation. If you must confirm, state the
  consequence ("Delete 3 invoices? This can't be undone.") and label buttons with the action
  ("Delete invoices" / "Cancel"), never "Yes" / "No".
- **B5** Icon-only buttons need an accessible name and a tooltip. Give a visible label to
  anything that is not universally understood.

## 2. Forms (F)

- **F1** Single column. Labels **above** fields. Placeholders are never labels. Exception: short,
  genuinely related pairs (city/postcode, card expiry/CVC). Field width signals the expected input.
- **F2** Mark **optional** fields, not required ones. Better: remove optional fields.
- **F3** Ask only for what you need. Explain why you ask for sensitive data.
- **F4** Correct `type`, `inputmode` and `autocomplete` (`email`, `tel`, `one-time-code`,
  `postal-code`, `name`, `new-password`, `current-password`).
- **F5** Validate on blur or submit, not on every keystroke. Errors inline under the field;
  an error summary at the top of long forms; move focus to the first error (or the summary).
- **F6** Never clear what the user typed on error. Autosave long forms.
- **F7** Accept flexible formats (spaces or dashes in phone, IC or card numbers) and normalise
  them server-side.
- **F8** Choice controls: 2-5 options -> radios or segmented control; 6-15 -> select;
  > 15 -> searchable combobox. Toggles only for settings that apply immediately.
- **F9** Long forms become steps with a progress indicator and a review step before submit.
  Group related fields with `fieldset`/`legend`. Long and mobile forms keep the primary action
  sticky so users never hunt for submit.
- **F10** Passwords: allow paste and password managers, offer "Show password", show the rules
  before the user types.
- **F11** Sensible defaults, but never pre-check marketing consent.

## 3. Pickers & selection (P)

- **P1** Any entity picker (people, records) over ~7 items gets type-ahead search. Choice
  controls follow F8.
- **P2** Avatars or images next to names for recognition.
- **P3** Trigger is a verb with an icon ("Set assignee"), not a vague "Select...". Show recent or
  suggested choices first.
- **P4** Full keyboard support (arrows, Enter, Esc), visible focus, and helpful zero-results
  text ("No one named 'Ali'. Invite them?").

## 4. Tables & data (TB)

- **TB1** Sticky header. Sortable columns show their sort state (`aria-sort`). Filters are
  visible and removable as chips.
- **TB2** Numbers right-aligned, tabular numerals, units in the header. Locale-formatted.
- **TB3** Relative dates ("3 weeks ago") come with the absolute date in a tooltip or
  `<time datetime>`. Correct plurals (`Intl.PluralRules` / `Intl.RelativeTimeFormat`).
- **TB4** On mobile, tables become cards or list rows. Keep the key column visible.
- **TB5** Bulk actions appear when rows are selected, with "Select all N results".
- **TB6** Pagination for goal-oriented lookup. Infinite scroll only for browsing feeds, and
  never when the footer matters.
- **TB7** Density: compact rows for expert tools with a comfortable/compact toggle (row actions
  keep the target floor in `accessibility.md` A7). Zebra striping or row borders, not both.
- **TB8** Column priority: most-scanned columns leftmost; low-value columns behind a column
  picker or detail view. Truncate long cells with the full text reachable. Sticky key column on
  wide tables.
- **TB9** Saved views (filter + sort + columns) for expert users. Inline edit for a single field;
  drawer or modal for multi-field edits.
- **TB10** Wide tables on small screens: horizontal scroll with a pinned key column (when
  comparing across columns), cards per row (when rows are read one at a time), or 2-3 priority
  columns + detail. Never let a table overflow silently.

## 5. Dashboards & data visualisation (D)

- **D1** Every dashboard answers a named question. The primary KPI comes first, with
  comparison context.
- **D2** Chart by question: trend -> line; compare -> bar; part of whole (<= 5 parts) ->
  stacked bar or donut; distribution -> histogram.
- **D3** Label data directly instead of relying on a legend. Remove chart junk. Bar y-axes
  start at zero.
- **D4** Always offer a table or text alternative.

## 6. Cards, lists, modals, toasts (CL)

- **CL1 Cards** - one clear primary action. The whole card can be the link, but then no
  nested competing link.
- **CL2 Modals** - only for short, blocking decisions. Trap focus, close on Esc, return focus
  to the trigger. Never stack modals or open them on page load. Prefer an inline panel or
  drawer for complex editing. Native `<dialog>` with `showModal()` gives most of this for free.
- **CL3 Toasts** - only for non-critical confirmation, announced via `aria-live`, visible
  >= 5s, pausable on hover/focus. Errors that need action are never only a toast.

## 7. Search & navigation (SN)

- **SN1** Search tolerates typos, shows recent and suggested queries, highlights matches.
  Zero results always offers a next step.
- **SN2** Filter, tab and page state live in the URL (deep-linkable, shareable, Back works).
- **SN3** Active nav item clearly marked (`aria-current="page"`). Breadcrumbs for hierarchies
  deeper than two levels.
- **SN4** Choose the pattern from the structure: top bar for few destinations; sidebar for many
  (app shells, admin), collapsible with labels on expand; bottom tab bar for 3-5 mobile
  destinations; drawer only for secondary items; command palette for expert tools, alongside
  visible navigation. Nav order stays stable between pages; label `<nav>` landmarks when there
  is more than one.
- **SN5** Build the nav from an inventory of routes, roles and common destinations, grouped by
  the user's mental model in product language, never by database table names. Switching role
  or workspace keeps the user's task context. Check it from every major screen, deep routes,
  empty states and browser Back/Forward.

## 8. Onboarding & empty states (O)

- **O1** Empty states teach: what goes here, why it matters, and one CTA to start (sample
  data if useful).
- **O2** Progressive disclosure: advanced options when needed, not up front.
- **O3** Product tours do not fix unclear UI. Fix the UI first.
