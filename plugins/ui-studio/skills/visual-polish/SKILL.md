---
name: visual-polish
description: >-
  Fixes how an existing screen or component looks with the Ten Fixes rules - one hero, one left
  edge, a 3-step spacing rhythm, one text style, one accent, readable contrast, one icon set,
  grouped cards, ranges shown as visuals, a state-driven background - measured with bundled
  scripts and reported as before -> after numbers, without changing data. Modes: audit
  (read-only score), fix (apply in rule order), build (tokens-first component that passes). Use
  for "this dashboard looks ugly, fix it", "polish this card", "why does this screen look
  cluttered/amateur?", "make this component look professional". Not for codebase-wide token
  audits - use ui-design-system.
argument-hint: "audit | fix | build <path, url or what to build>"
---

# Visual polish (Ten Fixes)

Core idea: **most ugly screens aren't missing features, they're missing decisions.**
Every fix here changes presentation only. Same data in, same data out. If a fix
seems to need new data, a new feature or new copy, it is out of scope: note it
separately and move on.

Modes: **audit** (read-only report), **fix** (change existing code), **build** (new UI that
passes from the first line). Commands: `/ui-studio:polish-audit`, `/ui-studio:polish-fix`,
`/ui-studio:polish-new`.

## The rules

Apply the rules **in order**. Each one makes the next easier to see: once the hero
is obvious (1) and edges line up (2), spacing problems (3) become visible; once
type is calm (4), colour noise (5) stands out; and so on.

| # | Rule | One-line test | Default target |
|---|------|---------------|----------------|
| 01 | Hierarchy | Can you find the number you came for in under a second? | One hero per view, ≥ 3× body size at `--text-display` (video: 20 px → 76 px) |
| 02 | Alignment | How many left edges does the column have? | 1 shared left edge per container (video: 6 → 1) |
| 03 | Spacing | How many distinct gap values in the component? | 3 values on a 4 px grid, e.g. 4 · 8 · 12 (video: 5 → 3) |
| 04 | Text style | Any caps, italics or underlines used for emphasis? | None; hierarchy by size, weight, opacity (video: 5 → 1) |
| 05 | Colour | How many hues are on the text? | Neutral text + one accent (video: 4 → 1) |
| 06 | Contrast | Lowest text contrast on its real background? | A1 minimum, A1 recommended ratio for secondary text (video: 1.9 → 6.7) |
| 07 | Icons | How many icon families, strokes and sizes? | One family, one stroke, one size per role (video: 8 → 1) |
| 08 | Grouping | Are related items on a shared surface? | One card per semantic group (video: 0 → 2) |
| 09 | Show, don't list | Is a range/comparison only written as text? | Encode it visually, keep numbers as labels |
| 10 | Make it alive | Does the surface reflect the data's state? | Background tied to state, subtle, motion-safe |

Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.

Read `references/rules.md` for each rule's rationale, detection signals, fix recipe,
exceptions and the before/after from the source video. Token values (spacing, type, colour,
radius, icons, motion) come from `${CLAUDE_PLUGIN_ROOT}/references/shared/visual-system.md`;
starter tokens for plain CSS / Blade are in `assets/tokens.css`.

How to use the rules well:
- **Count, don't vibe.** Every rule has a number. Report "5 gap sizes → 3", not
  "spacing feels inconsistent". Numbers make reviews checkable and fixes verifiable.
- **Defaults, not laws.** Each rule lists real exceptions (tables may have a second
  edge; status colours are not accents; links keep a non-colour cue). When you use
  one, say so in a single line.
- **Fix the system, not the instance.** If six cards share a problem, change the
  token or the shared component once.
- **Later rules never break earlier ones.** Rule 10's background must still pass
  Rule 6. Rule 9's bars use the Rule 5 accent, not a new colour.

## Mode: audit (read-only)

Do not edit files in this mode.

1. **Scope and inventory.**
   - Identify the target: a component, a page/route, a screenshot, or the whole app.
     For a whole app, pick the 3-5 highest-traffic screens and audit those; say so.
   - Find the styling system: Tailwind config / `@theme`, CSS variables, SCSS tokens,
     component library (shadcn, Bootstrap, Vuetify, MUI, Filament, Flux). Rules are
     judged against tokens when tokens exist.
   - List the **data** each screen shows (Rule 00). This list is the contract the
     fix must keep.
2. **Measure** (use whatever evidence is available, best first).
   - **Rendered DOM** (best): if a dev server or built HTML is available and Node +
     Playwright are installed, run
     `node ${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/playwright_probe.mjs <url|file> "<selector>" audit [--mobile]`.
     Otherwise ask the user to paste `scripts/dom_probe.js` into DevTools and run
     `copy(JSON.stringify(tenFixesProbe('<selector>'), null, 2))`.
   - **Static source**: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/ui_lint.py <paths> --component-scope`.
     Point it at the component's files plus the global CSS/token files.
   - **Screenshot**: inspect visually for Rules 01, 02, 08, 09, 10, and count edges,
     sizes and colours by eye. State that counts are visual estimates.
   - Contrast for specific pairs: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/visual-polish/scripts/contrast.py FG BG --suggest`.
     On gradients, test text against the lightest region behind it.

   Scripts are heuristics. Confirm each automated finding against the code or the
   screenshot before reporting it, and drop false positives (status colours, link
   underlines, tabular column edges, code fonts).
3. **Report.** Use this structure exactly:

```
# Ten Fixes audit — <target>
Score: X/10 applicable (W warn, F fail)   Data contract: <n items, unchanged>

| # | Rule | Now | Target | Verdict | Where |
|---|------|-----|--------|---------|-------|
| 01 | Hierarchy | temp 20px (1.4× body) | ≥3× body | fail | WeatherCard.vue:12 |
...

## Fix order
1. <highest-impact rule first, in rule order unless something blocks> — one line each

## Exceptions applied
- <rule>: <why it doesn't apply here>

## Out of scope (not presentation)
- <feature / data / copy ideas, if any>
```

Keep "Now" and "Target" numeric in the video's style (`5 gap sizes → 3`).
Recommend a fix order, decisively: normally 01→10, but promote 06 (contrast) to
first if anything fails WCAG, because that's an accessibility bug, not polish.
End by offering fix mode (or `/ui-studio:polish-fix`) to apply the plan.

## Mode: fix

Change presentation only. Same data, same behaviour, same copy. Work inside the
user-first-ux workflow (Read → Report → Plan → Approve → Implement → Verify → Sync); if that
skill is not installed, follow those seven steps and stop for approval after Plan.

1. **Read.** Open the target files, shared components, global CSS and token config.
   Note the framework and whether tokens exist. Record the data contract (every value
   the screen displays).
2. **Report.** Run audit mode (or reuse a recent audit). Bring the scored table into the
   conversation.
3. **Plan.** One line per failing rule, in order, each with: the change, the files,
   and the before→after metric. Prefer system-level changes:
   - Missing tokens → add a token layer first (`visual-system.md` §Token set), mapped to
     existing values where possible, so the rest of the plan is "replace literals with tokens".
   - A pattern repeated across components → fix the shared component.
   - Flag anything that touches behaviour, data, or copy as out of scope.
4. **Approve.** Show the plan and stop for the user's go-ahead before editing,
   unless they already said to just apply it. Ask at most one question.
5. **Implement**, rule by rule, in order. Keep each rule's change a separate,
   reviewable step (one commit per rule when using git: `style(ui): 03 spacing rhythm 5→3`).

| Rule | Typical edit |
|------|--------------|
| 01 | Hero to `--text-display` with light weight; collapse other sizes to title/body/caption |
| 02 | One container padding; delete child `ml-*`/`pl-*`/`margin-left`; left-align stacks; grid for columns |
| 03 | Replace every gap/margin/padding with `--space-1/2/3` (or Tailwind `1/2/3` on `--spacing: 4px`); inner gap < group gap |
| 04 | Remove `uppercase`, `italic`, `underline`, wide tracking; sentence-case strings via CSS not by editing copy*; ≤ 2 weights |
| 05 | Text → `--fg` / `--fg-muted`; one `--accent`; icons `currentColor`; status colours only for status |
| 06 | Adjust `--fg-muted` with `contrast.py --suggest --target 7` until it meets A1 everywhere it's used |
| 07 | One icon library, one stroke, `--icon-inline` for repeated icons, one hero icon max; replace emoji |
| 08 | Wrap each semantic group in one card component (`--card`, `--radius-control`, padding `--space-3`/`--inset`) |
| 09 | Repeated ranges/values → range bars / progress / sparkline on a shared scale; numbers stay as labels; add aria-labels |
| 10 | Map the data's state to a surface (`--sky-*`, status tint); M1 transition; reduced-motion fallback |

\*If text is stored in caps in the source (e.g. "WED"), change rendering with CSS
or a formatter rather than rewriting data. Ask before editing translation files.

6. **Verify.** Re-run the same measurements as the audit (probe, lint, contrast) and
   show the before→after table. Confirm the data contract is identical. Check
   light/dark mode, mobile width, keyboard focus states and reduced motion. If a
   screenshot tool is available, capture before and after.
7. **Sync.** Summarise what changed per rule, update any design-system docs or
   token README, and list remaining warnings or exceptions.

Guardrails:
- Don't rename props, routes, data keys or public component APIs.
- Don't introduce a new dependency for icons or charts if the project already has
  one that works; range bars are a few lines of CSS (`assets/range-bar.css`).
- If a fix would break another rule (e.g. live background lowers contrast), the
  earlier rule wins; adjust the later fix.

## Mode: build

`assets/reference-card.html` is a complete worked example (the "after" weather
card from the source video) showing every rule at once; open it when you need a
concrete pattern for a card, range bar, or live background. For a full feature build with a
visual plan and approval gate, `/ui-studio:ui-build` runs this mode as its polish step.

1. **Data contract.** List exactly what the UI must show and the single question
   it answers. That answer becomes the hero (Rule 01). If the user hasn't given the
   data, infer the minimum and state it in one line.
2. **Tokens before markup.** Emit the token set for the target stack
   (`visual-system.md` §Token set, stack mapping in `ui-stack-laravel` / `ui-stack-next`), or
   extend the project's existing tokens. Every value used later must come from this set. Copy
   `assets/tokens.css` for plain CSS/Blade projects and replace its placeholder font and palette.
3. **Group.** Split the data into semantic groups (Rule 08). Hero/header on the base
   surface; each secondary group in one card.
4. **Lay out.** One container inset; one left edge per card; columns only for
   tabular data, on an equal-track grid (Rule 02). Gaps: 4 inside a unit, 8 between
   siblings, 12 between groups (Rule 03).
5. **Type & colour.** Hero at `--text-display`, light weight; everything else title,
   body or caption. Sentence case, no italics/underlines (Rule 04). `--fg`,
   `--fg-muted`, one `--accent` (Rule 05). Check `--fg-muted` on every surface with
   `scripts/contrast.py` (Rule 06).
6. **Icons.** One library already in the project (else lucide or heroicons outline),
   `currentColor`, one size per role, at most one hero icon (Rule 07).
7. **Visualise.** Any range, proportion or series with ≥ 3 items gets a visual on a
   shared scale (`assets/range-bar.css`) with the numbers kept as labels (Rule 09).
8. **Alive.** Map the data's state to the surface (`data-state` attribute →
   `--sky-*` or status tint), with reduced-motion fallback; re-check contrast (Rule 10).
9. **Self-audit.** Run the audit-mode measurements on what you built and include the
   ten-row table in your reply. Anything below pass gets fixed before you hand over.

Component kit to generate (adapt names to the stack):
- `Card` — surface, radius, inset; no other styling props.
- `Stat` / `Hero` — the primary datum, label, secondary line.
- `RangeBar` — `min`, `max`, `low`, `high`, accessible label.
- `IconText` — icon + label with `--space-1` gap.
- `LiveSurface` — wraps the view, takes `state`, sets the background.

For Laravel/Blade, generate them as anonymous components in
`resources/views/components/` and put tokens in `resources/css/app.css`.

The read-only `ui-ten-fixes-auditor` agent runs audit mode in parallel for large reviews.
