# Laws of Cognition & Decision-Making

Memory, mental effort, attention and choice. Read when a screen asks users to decide,
remember, compare or configure: pricing, onboarding, forms, settings, filters, navigation.

Laws are heuristics, not physics. Evidence from real users beats every rule here.

## Contents
1. Hick's Law `[Hick]`
2. Choice Overload `[Choice Overload]`
3. Miller's Law `[Miller]`
4. Chunking `[Chunking]`
5. Cognitive Load `[Cognitive Load]`
6. Working Memory `[Working Memory]`
7. Selective Attention `[Selective Attention]`
8. Cognitive Bias `[Cognitive Bias]`
9. Occam's Razor `[Occam]`
10. Pareto Principle `[Pareto]`
11. Tesler's Law `[Tesler]`

---

## Hick's Law  [Hick]
**Definition:** Decision time grows with the number and complexity of choices (RT = a + b·log₂(n+1)).
**Origin:** William Hick & Ray Hyman, 1952.
**Why it matters:** Every extra option adds evaluation work; at a decision point that work
turns into hesitation and abandonment.
**Rules:**
- At each decision point (pricing, onboarding, forms, settings) count the options **and the
  combinations** the user must evaluate; write the number down. 3 plans × 2 billing terms × 4
  add-ons = 24 paths.
- Cut, group or default until that count is the minimum the task needs.
- Break complex choices into steps; mark one honest recommended option.
- Put advanced settings behind progressive disclosure ("More options", `<details>`).
**Do:** 3 plans, one labelled "Recommended", a monthly/annual toggle, add-ons offered after the plan is chosen.
**Don't:** 4 plans × 3 terms × 5 add-on checkboxes on one screen (60 combinations).
**Audit check:** How many options/combinations must the user weigh at this decision, and could any be removed, grouped, defaulted or deferred?
**Common violations:** every setting on one page · add-ons mixed into plan cards · 10 equally styled filter buttons.
**Misuse warning:** Oversimplifying until users cannot finish the task. Hick does not apply to
lists users scan for a known name (countries, contacts); give those search instead of cutting.

## Choice Overload  [Choice Overload]
**Definition:** Too many options cause paralysis, lower satisfaction and abandonment.
**Origin:** Alvin Toffler, 1970 ("overchoice", *Future Shock*); Sheena Iyengar & Mark Lepper, 2000 (the jam study).
**Why it matters:** When options are many, complex and hard to compare, people defer the choice or regret it.
**Rules:**
- More than 3 comparable options → offer side-by-side comparison (same rows, same order).
- Curate: a clear default or "Most popular" marker (only if true).
- Long catalogues get filters and sort; more than 15 options in a control → searchable combobox.
**Do:** Pricing table where every tier lists the same features in the same rows.
**Don't:** 8 product cards each describing features in different words and order.
**Audit check:** Can the user compare the options directly, and is there a truthful starting suggestion?
**Common violations:** select with 40 unsorted items · plan cards with non-aligned features · no filters on a 200-row catalogue.
**Misuse warning:** The effect is conditional. One meta-analysis found an average effect near
zero (Scheibehenne et al., 2010); another found it reliable when options are complex, the
decision is hard, preferences are unclear, or users want to minimise effort (Chernev et al.,
2015). Do not cut options users need; add comparison and filters when those conditions apply.

## Miller's Law  [Miller]
**Definition:** People hold about 7 ± 2 items in working memory; later research (Nelson Cowan, 2001) suggests about 4 ± 1 chunks.
**Origin:** George A. Miller, 1956 ("The Magical Number Seven, Plus or Minus Two").
**Why it matters:** Flat lists of equal items force users to hold and compare too much at once.
Capacity varies by person, prior knowledge and situation, so design for the low end.
**Rules:**
- Group navigation, settings and form fields into labelled groups of about 5–9 items (fewer is better).
- Never present 15+ equally weighted items in one flat list or grid; group, rank or make it searchable.
- Ask for one decision at a time in complex flows.
**Do:** 18 admin sidebar links split into 4 labelled groups (Content, People, Finance, System).
**Don't:** 15 identical dashboard tiles in a 5×3 grid.
**Audit check:** Is any list, menu or form section longer than ~9 equally weighted items without grouping?
**Common violations:** flat sidebar of 20 links · settings page as one long list of toggles · 12 same-style KPI tiles.
**Misuse warning:** "7" is not a hard cap on menu items. The lesson is chunking, not counting;
a well-grouped list of 20 beats an arbitrary cut to 7.

## Chunking  [Chunking]
**Definition:** Breaking information into meaningful groups makes it easier to scan and remember.
**Origin:** Builds on Miller, 1956.
**Why it matters:** Grouped information is processed as fewer units.
**Rules:**
- Format long numbers in groups on display: phone `012-345 6789`, IC `900101-14-5678`, account `1234 5678 9012`.
- Split forms longer than ~7 fields into titled sections (`<fieldset><legend>`) or steps.
- Use headings and whitespace to make chunks visible; a chunk needs a label.
**Do:** Registration split into "About you", "Contact", "Membership" sections.
**Don't:** 14 fields in one undivided column.
**Audit check:** Are long numbers, forms and pages visibly broken into labelled groups?
**Common violations:** unformatted 16-digit reference numbers · 14-field single-section form · headings missing between groups.

## Cognitive Load  [Cognitive Load]
**Definition:** The mental effort to use an interface: intrinsic (the task itself) plus extraneous (caused by bad design).
**Origin:** John Sweller, 1988.
**Why it matters:** Extraneous load consumes the capacity users need for their actual task.
**Rules:**
- Remove extraneous load: decorative elements that carry no information, needless steps, inconsistent patterns, jargon.
- Offload work to the system: defaults, autofill, saved state, computed values.
- One task per screen in complex flows; one primary action per view.
**Do:** Address autocompleted from postcode; total computed live.
**Don't:** Ask users to calculate a total or copy a code from another tab.
**Audit check:** Is there anything on screen the user must interpret, calculate or decode that the system could do instead?
**Common violations:** internal codes as labels · decorative illustrations pushing the task below the fold · mixed date formats.

## Working Memory  [Working Memory]
**Definition:** A small, temporary store for information while working on a task.
**Origin:** Term coined by George Miller, Eugene Galanter & Karl Pribram, 1960; multi-component model by Alan Baddeley & Graham Hitch, 1974.
**Why it matters:** It holds roughly 4–7 chunks, each fading within about 20–30 seconds, so
anything users must carry between screens is likely to be forgotten or mistyped. Put the
burden of memory on the system, not the user.
**Rules:**
- Never make users carry information between screens; show the needed context in place
  (order summary visible at payment, applicant name on every review step).
- Recognition over recall: recent items, previous values, visited states, inline hints.
- Never ask for the same information twice in one process (WCAG 3.3.7).
**Do:** Payment step keeps the order summary and delivery address visible.
**Don't:** "Enter the reference number shown on the previous page."
**Audit check:** Does any step rely on the user remembering something shown earlier?
**Common violations:** re-entering an address for billing · codes only shown on a prior screen · no "recent" list in pickers.

## Selective Attention  [Selective Attention]
**Definition:** Users attend only to stimuli relevant to their goal and filter out the rest.
**Origin:** E. Colin Cherry, 1953 (cocktail-party effect); Donald Broadbent, 1958 (filter theory); banner blindness (Jan Benway & David Lane, 1998); change blindness.
**Why it matters:** Ad-like UI is ignored (banner blindness) and subtle changes go unnoticed (change blindness).
**Rules:**
- Never style important information like an ad (top banners, bright boxed promos, sidebars of images).
- Make state changes noticeable: highlight the changed row, inline confirmation, `aria-live` announcement.
- Use emphasis sparingly so it still works when needed.
**Do:** After saving, the edited row briefly highlights and "Saved" appears next to it.
**Don't:** A critical account-suspension notice styled as a colourful promo banner.
**Audit check:** Would the user notice the important message or the change they just caused?
**Common violations:** errors shown only in a dismissible top banner · silent saves · rotating banners holding key info.

## Cognitive Bias  [Cognitive Bias]
**Definition:** Systematic errors in thinking: anchoring, framing, default effect, loss aversion, confirmation bias.
**Origin:** Amos Tversky & Daniel Kahneman, 1972–1974 (the heuristics-and-biases research programme).
**Why it matters:** Every default and first number your UI shows steers decisions, intended or not.
**Rules:**
- Set defaults to what most users would choose for their own benefit.
- Make anchors truthful: a "was" price must be a real previous price; a recommendation must be justified.
- Never use bias against the user (see Ethics guardrail).
**Do:** Default delivery = the cheapest option that meets the stated date.
**Don't:** Pre-selected paid insurance; an invented "was RM 299" anchor.
**Audit check:** Which defaults and anchors does this screen set, and do they serve the user?
**Common violations:** pre-ticked add-ons · fake strike-through prices · default plan chosen for revenue, not fit.

## Occam's Razor  [Occam]
**Definition:** Among competing designs, prefer the one with the fewest assumptions and elements.
**Origin:** William of Ockham, 14th century.
**Why it matters:** Every element competes for attention and must be learned.
**Rules:**
- For each element ask: does it support the user's task on this screen? If not, remove it.
- Test the screen with each non-essential element removed; keep the removal if the task still works.
- Prefer one clear control over two overlapping ones.
**Do:** One "Export" button with a format choice inside.
**Don't:** "Export CSV", "Export Excel", "Download", "Print" side by side for the same data.
**Audit check:** Which element could be removed without hurting the task?
**Common violations:** duplicate actions in toolbar and row · decorative icons on every label · redundant helper text.
**Misuse warning:** Removing necessary controls only moves complexity to the user (see Tesler).

## Pareto Principle  [Pareto]
**Definition:** About 80% of effects come from about 20% of causes; most users use a few features.
**Origin:** Vilfredo Pareto, 1896; applied to quality by Joseph Juran.
**Why it matters:** Optimising the few frequent tasks benefits almost everyone.
**Rules:**
- Identify the top tasks from analytics, support tickets or the UX brief; state the source.
  No data → list them as hypotheses.
- Put those tasks in the most prominent positions (top of page, primary nav, dashboard first row).
- Move rare tasks to secondary nav, overflow or settings.
**Do:** Admin home leads with "Pending approvals (12)" because that is the daily task.
**Don't:** Equal-sized tiles for daily and yearly tasks.
**Audit check:** Are the most frequent tasks the most prominent and fastest on this screen?
**Common violations:** alphabetical nav · rare settings in primary nav · frequent action two clicks deep.

## Tesler's Law  [Tesler]
**Definition:** Every system has irreducible complexity; either the system or the user must handle it.
**Origin:** Larry Tesler, Xerox PARC, mid-1980s (Conservation of Complexity).
**Why it matters:** Hiding complexity without absorbing it just transfers work to the user.
**Rules:**
- Absorb complexity in the system: smart defaults, inference (city from postcode), formatting, validation.
- Do not "simplify" by hiding controls the task needs.
- Engineers take the complexity so that users do not have to.
**Do:** Detect card type from the number; prefill the state from the postcode.
**Don't:** Remove the delivery-date picker to "simplify" checkout when users need to choose a date.
**Audit check:** Is complexity handled by the system, or merely hidden from view?
**Common violations:** required info only reachable via an "Advanced" toggle · users asked for data the system already has.
**Misuse warning:** Don't design for an idealised, rational user. Bruce Tognazzini's
counterpoint: when a product gets simpler, users take on harder tasks, so complexity returns
in new places; keep absorbing it.
