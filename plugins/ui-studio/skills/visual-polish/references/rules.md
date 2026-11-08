# The Ten Fixes — full reference

Source: a before/after redesign of a weather card ("Same data. Ten fixes. A
different app."). The data never changed: city, time, current temperature,
condition, high/low, six hourly slots, four daily ranges. Only decisions changed.

Contents
- 00 The meta-rule: zero new data
- 01 Hierarchy · 02 Alignment · 03 Spacing · 04 Text style · 05 Colour
- 06 Contrast · 07 Icons · 08 Grouping · 09 Show, don't list · 10 Make it alive
- Beyond the ten · Severity scale and scoring

Each rule has: **Why** · **Detect** (what to count) · **Fix** · **Exceptions** ·
**Video** (the before → after it was taught with).

---

## 00 The meta-rule: zero new data

Polish is subtraction and arrangement, not addition. Before proposing anything,
list the data the screen shows. After the fix, the list must be identical. Adding a
chart is fine (Rule 9) only if it encodes data already on screen.

Out of scope for this rulebook, log separately: new features, new copy, new
fields, information architecture changes across screens, and branding.

---

## 01 Hierarchy — the number you came for

**Why.** Every screen exists to answer one question. In a weather card it's "how
warm is it now?". If that answer is the same size as the hour labels, the eye has
to search. A single dominant element ends the search.

**Detect.**
- Identify the primary datum (ask: what would the user glance at for one second?).
- Ratio of hero font size to body font size. Below 2× = fail, 2–3× = warn, ≥ 3× = pass.
- Number of elements competing at the top size. More than 1 hero per card = fail.
- Distinct font sizes per component. More than 4 (hero, title, body, caption) = warn.

**Fix.**
- Promote the hero to `--text-display` (video: 76 px against ~14 px body; ~5×).
- Use a light or regular weight at display size; heavy weights at 60 px+ look loud.
- Demote everything else to a 3–4 step scale. Remove sizes that sit between steps.
- Place the hero top-left or top-centre where reading begins.

**Exceptions.** Dense tools (tables, IDEs, admin lists) may have no single hero;
then the hierarchy is the column header → row, and Rule 1 applies per region.

**Video.** `TEMP 20 px → 76 px`.

---

## 02 Alignment — one left edge

**Why.** Every distinct x-start is a line the eye has to register. Six edges read
as six unrelated things; one edge reads as one object.

**Detect.**
- Within each container, collect the left x of every text/icon block. Count
  distinct values (tolerance ±2 px). 1 = pass, 2 = warn unless tabular, ≥ 3 = fail.
- Mixed `text-align` in one stack (centre title over left body) counts as an edge.
- Indents created by ad-hoc margin-left / padding-left on single children.

**Fix.**
- Give the container one horizontal padding token; remove child-level left offsets.
- Left-align text in stacks. Centre only whole, symmetric blocks.
- For rows, make the first column the shared edge; other columns form a grid.

**Exceptions.** Tabular data (hourly columns, a data table) has column edges by
design; they must sit on a grid with equal tracks. Numeric columns align right.

**Video.** `6 EDGES → 1`.

---

## 03 Spacing — a rhythm, not a scatter

**Why.** Random gaps (7, 10, 13, 18, 22 px) make relationships ambiguous: are two
items related or not? A tiny set of steps lets distance carry meaning — small gap =
same thing, larger gap = next thing.

**Detect.**
- Collect every margin, padding and gap value in the component. Count distinct values.
  3 rhythm steps + 1 container inset (Rule 02) = pass; 5 = warn; ≥ 6 = fail.
- Off-grid values (not a multiple of 4) = warn each.
- Equal gaps between items that belong to different groups (spacing lies about grouping).

**Fix.**
- Pick three steps on a 4 px grid. Video used **4 · 8 · 12**: 4 inside a unit
  (icon ↔ label), 8 between siblings, 12 between groups. Larger layouts can use
  8 · 16 · 24 (+ 32/48 for page sections) but still few steps per component.
- Express them as tokens (`--space-1/2/3`, or Tailwind steps on `--spacing: 4px`; see
  `visual-system.md`) and replace literal values.
- Gap inside a group < gap between groups. Always.

**Exceptions.** Page-level layout may add one or two larger steps. Optical nudges
(1–2 px for icons) are fine if documented.

**Video.** `5 GAP SIZES → 3`, summary "4 · 12 · 8 px only".

---

## 04 Text style — one style

**Why.** Caps, italics, underlines, letter-spacing and colour each shout "I'm
special". When five things shout, nothing is special. Size, weight and opacity
are enough to express every level.

**Detect.**
- Count `text-transform: uppercase`, `font-style: italic`, `text-decoration:
  underline`, wide `letter-spacing` used for emphasis (not links). Any = warn; ≥ 2
  kinds = fail.
- Distinct font families (> 2 = fail; up to two is T5 in `visual-system.md`).
- Distinct weights, not counting the hero's display weight (> 2 = warn; > 3 = fail).

**Fix.**
- Sentence case everywhere ("Partly cloudy", not "PARTLY CLOUDY"; "Wed", not "WED").
- Remove italics and underlines from labels and headings.
- One family (or two clearly contrasting ones, T5), two weights (regular + medium/semibold).
- Express secondary text with opacity or a lighter neutral, not a new style.

**Exceptions.** Links always keep a non-colour cue such as an underline (accessibility, owned
by user-first-ux). Tiny overline labels in caps are a deliberate system choice only if used for
exactly one role: the short muted data label (T7).
Code uses a mono family.

**Video.** `5 STYLES → 1`, summary "no caps, italics or underlines".

---

## 05 Colour — white text, one accent

**Why.** Von Restorff: follow the **ux-laws** skill (user-first-ux plugin) if installed.
Minimum if not: emphasise one thing; if everything is emphasised, nothing is.

**Detect.**
- Distinct hues used on text and icons (ignore neutrals: greys/white/black).
  0–1 = pass, 2 = warn, ≥ 3 = fail.
- Colour used to encode data values without a legend.
- Accent applied to non-interactive, non-key items.

**Fix.**
- Text: one neutral foreground plus 1–2 lighter neutral steps (or opacity).
- Pick one accent (brand or data colour). Use it for the primary action, current
  selection, or the single data encoding (e.g. the range bars in Rule 9).
- Icons inherit `currentColor`.

**Exceptions.** Semantic status colours (error, warning, success) are not accents;
use them only for status, and pair with an icon or text so colour isn't the only
signal. Charts with multiple series may need a categorical palette.

**Video.** `4 COLOURS → 1`, summary "white text, one accent".

---

## 06 Contrast — readable grey

**Why.** Low-contrast secondary text looks "subtle" on a designer's monitor and
unreadable in sunlight, on cheap screens, and for low-vision users. Muted is fine;
illegible is not.

**Detect.**
- Compute WCAG 2.x contrast for each text colour against its actual background
  (including card surfaces and gradients; test the lightest point of a gradient
  for light text).
- Thresholds: below the A1 minimum = fail; between the minimum and the A1 recommended ratio =
  pass, aim higher for small secondary text.
  Accessibility (contrast, targets, focus): follow the **user-first-ux** skill if installed.
  Minimum if not: text ≥ 4.5:1 (large ≥ 3:1), targets ≥ 24×24 px, visible focus.
- Use `scripts/contrast.py` in this skill (`--suggest` finds the nearest grey that passes;
  `--target 7` aims for the recommended ratio).

**Fix.**
- Lighten (dark UI) or darken (light UI) the secondary grey until it meets A1; target the A1
  recommended ratio. Keep it visibly lighter than primary text.
- Never use opacity < 0.6 for informative text on dark surfaces without checking.
- Disabled states are exempt from WCAG but should still be legible.

**Video.** `1.9:1 → 6.7:1`.

---

## 07 Icons — one style, one size

**Why.** Mixed icon sets (filled emoji next to outline glyphs, coloured next to
mono, 14 px next to 22 px) look like clip art. One family at one size per role
looks designed.

**Detect.**
- Icon libraries imported/used (lucide, heroicons, font-awesome, material, emoji,
  ad-hoc SVGs). > 1 = fail.
- Emoji used as UI icons = fail.
- Distinct icon sizes for the same role (> 1 = fail). Distinct stroke widths > 1 = warn.
- Filled + outline mixed in one context = warn.

**Fix.**
- Choose one family and one stroke (e.g. outline 1.5 px): the project's existing icon system
  first; on native platforms the platform set (SF Symbols, Material Symbols). One metaphor per
  concept (never two different "edit" icons).
- One size per role: inline (16–20 px), list (20–24 px), hero (one only, paired with
  the Rule 1 hero; may be 48–64 px).
- Icons use `currentColor` and inherit the text colour; no per-icon colours.

**Exceptions.** One hero illustration/icon per view. Brand logos keep their own style.

**Video.** `8 SIZES → 1`, summary "one style, one size".

---

## 08 Grouping — put related things in cards

**Why.** Common Region and Proximity: follow the **ux-laws** skill (user-first-ux plugin) if
installed. Minimum if not: things inside a shared boundary read as one group; space inside a
group is smaller than space between groups.

**Detect.**
- List the semantic groups on the screen (video: header/now, hourly, weekly).
- Groups without a shared surface or clear separation = warn per group.
- Over-carding: every item in its own card, or cards nested > 1 level = warn.

**Fix.**
- One surface per semantic group. Surface = subtle background step (dark UI:
  +4–8% lightness or `rgba(255,255,255,0.06)`), radius from a single radius token (`--radius-control`),
  padding = the largest spacing step.
- The hero/header may stay on the base surface; secondary groups get cards.
- Separate groups with the group gap (Rule 3), not with divider lines when cards
  already separate them.

**Exceptions.** Very small UIs (a single stat) need no card. Use dividers instead
of cards for long homogeneous lists.

**Video.** `0 CARDS → 2` (hourly card, weekly card).

---

## 09 Show, don't list

**Why.** "17° – 28°" four times is a list the reader must compute in their head.
A range bar on a shared scale shows at a glance which day is warmest, coolest,
and most variable. The numbers stay as labels; the shape does the work.

**Detect.**
- Repeated numeric pairs or series (min–max, start–end, value of total, trend over
  time) rendered only as text, ≥ 3 rows = warn.
- Progress/percentages without a bar. Trends without a sparkline.

**Fix.**
- Ranges → range bars on a **shared** scale across rows (scale = global min/max of
  the visible set, not per row). Label low on the left, high on the right.
- Part-of-whole → progress bar. Trend → sparkline. Comparison → aligned bars.
- Bars use the Rule 5 accent. Track uses a faint neutral.
- Give bars an accessible text equivalent (`aria-label="Wed, low 17°, high 28°"`).

**Exceptions.** One or two values don't need a chart. Exact-value tasks (invoices,
ledgers) stay as tables.

**Video.** `TEXT → RANGE BARS`, summary "the week at a glance".

---

## 10 Make it alive

**Why.** A flat surface says nothing. A background that reflects the data's state
(a sky that matches the weather, a tint for a status, time-of-day lighting)
communicates before any text is read and gives the product personality without
new data.

**Detect.**
- The data has a state (condition, status, time, severity) that the surface ignores = warn.
- Decorative motion unrelated to state, or motion without a `prefers-reduced-motion`
  fallback = fail.

**Fix.**
- Map state → surface: e.g. clear = blue gradient, cloudy = grey-blue, rain = slate,
  night = deep navy; status ok/warn/error = very low-saturation tints.
- Keep it subtle: low saturation, large soft gradients, ≤ 1 slow ambient motion
  (or none). Transitions on state change within M1 (`visual-system.md`).
- Re-verify Rule 6 on the new background (check the lightest region behind text).
- Wrap motion in `@media (prefers-reduced-motion: no-preference)`.

**Exceptions.** Data-dense or professional tools may express "alive" with only a
small status tint or a state-coloured accent edge.

**Video.** `FLAT → LIVE SKY`, summary "a background that matches the weather".

---

## Beyond the ten (final polish pass)

Only once the ten pass and the screen works: optical alignment (icons, punctuation, mixed-size
rows, icon + text baselines); consistent border widths and radii, one shadow logic; no orphans
or awkward wraps in headings; long text, empty, loading, error and zero/overflow numbers render
without layout shift (states owned by user-first-ux).

## Severity scale and scoring

Per-rule verdicts (not severities; the severity scale is owned by user-first-ux):
**pass** (meets target) · **warn** (near target or exception unclear) ·
**fail** (clearly violates) · **n/a** (rule doesn't apply; say why).

Score = passes out of applicable rules, reported as `7/10 (2 warn, 1 fail)`.
Always show the metric that justified each verdict, in the video's format:
`<before metric> → <target>`, e.g. `6 edges → 1`, `1.9:1 → 6.7:1`.
