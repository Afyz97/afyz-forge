# Laws of Behaviour, Motivation & Memory of Experience

User habits, expectations, motivation and how experiences are remembered. Read when
designing navigation, onboarding, multi-step flows, checkout, success and error moments,
or redesigning something users already know.

## Contents
1. Jakob's Law `[Jakob]`
2. Mental Model `[Mental Model]`
3. Paradox of the Active User `[Active User]`
4. Zeigarnik Effect `[Zeigarnik]`
5. Goal-Gradient Effect `[Goal-Gradient]`
6. Peak-End Rule `[Peak-End]`
7. Parkinson's Law `[Parkinson]`

---

## Jakob's Law  [Jakob]
**Definition:** Users spend most of their time on other sites and expect yours to work the same way.
**Origin:** Jakob Nielsen, 2000 (Alertbox, "End of Web Design").
**Why it matters:** Familiar patterns cost nothing to learn; unfamiliar ones cost every user.
**Rules:**
- Follow conventions: magnifier = search; account and settings menu top-right; logo links
  home; cart → checkout → pay; dropdowns open downward; standard form controls; links look like links.
- Standard icons for standard meanings (gear = settings, trash = delete, × = close); label any icon that is ambiguous.
- When redesigning, keep familiar positions; for major changes let users switch back temporarily.
- Be novel only where the product itself is novel.
**Do:** User avatar top-right opens Profile, Settings, Sign out.
**Don't:** A custom glyph for search; settings only in the footer; a "cart" icon that opens a wishlist.
**Audit check:** Would a user of similar products know where things are and what they do without learning?
**Common violations:** reinvented date pickers · non-standard icons · logout hidden in settings.
**Misuse warning:** Conventions are not an excuse to copy a competitor's bad pattern or dark pattern.

## Mental Model  [Mental Model]
**Definition:** A user's internal belief about how a system works, built from past experience.
**Origin:** Kenneth Craik, 1943; applied to design by Don Norman, 1988.
**Why it matters:** When the UI matches the user's model, they predict outcomes correctly.
**Rules:**
- Use the users' words, not database fields or internal codes ("Staff ID", not `user_ref_no`).
- Structure navigation by user tasks, not by the org chart or the schema.
- Validate the terms and structure with card sorting, support tickets or user language; no data → mark as a hypothesis.
**Do:** Nav "Apply · My applications · Payments" for applicants.
**Don't:** Nav "Module A · tbl_permohonan · Unit Kewangan".
**Audit check:** Are labels and structure in the user's language and task order?
**Common violations:** DB column names as labels · department names as nav · status codes instead of plain states.

## Paradox of the Active User  [Active User]
**Definition:** Users never read manuals; they start using the software immediately.
**Origin:** John Carroll & Mary Beth Rosson, 1987.
**Why it matters:** Guidance that is not in the flow is not seen.
**Rules:**
- Put guidance in context: inline hints, labels, helper text, empty-state instructions, progressive onboarding.
- Empty states teach: what goes here, why it matters, one action to start.
- Never rely on documentation or product tours for core tasks; fix the UI instead.
**Do:** Empty "No invoices yet. Create your first invoice to bill a client." + button.
**Don't:** A 7-step tour on first login explaining an unclear screen.
**Audit check:** Can a first-time user complete the core task without reading anything outside the screen?
**Common violations:** blank tables with "No data" · format rules only in a help page · tours instead of fixes.

## Zeigarnik Effect  [Zeigarnik]
**Definition:** People remember uncompleted or interrupted tasks better than completed ones.
**Origin:** Bluma Zeigarnik, 1927; resumption studied by Maria Ovsiankina, 1928.
**Why it matters:** Visible unfinished work pulls people back to complete it.
**Evidence note:** A 2025 meta-analysis (Ghibellini & Meier) found no reliable *memory*
advantage for unfinished tasks, but a robust tendency to *resume* them (the Ovsiankina
effect). The rules below rely on resumption: show what's left and make returning easy.
**Rules:**
- Every flow of 3+ steps and every setup list shows what is done and what remains ("3 of 5 done · 2 left").
- Save progress automatically so users can leave and return ("Continue where you left off").
- Show the resume entry point where users land (dashboard, home).
**Do:** Dashboard card "Complete your profile — 3 of 5 done" with the next item linked.
**Don't:** A wizard with no indicator that resets on refresh.
**Audit check:** Does the user see what is left, and can they resume after leaving?
**Common violations:** no step indicator · progress lost on refresh · resume link hidden in a menu.
**Misuse warning:** Do not weaponise incompleteness: no fake unfinished items, guilt copy or repeated nagging.

## Goal-Gradient Effect  [Goal-Gradient]
**Definition:** Motivation increases as people get closer to a goal.
**Origin:** Clark Hull, 1932 (rat studies, 1934); Ran Kivetz, Oleg Urminsky & Yuhuang Zheng, 2006
(coffee-card study); endowed progress: Joseph Nunes & Xavier Drèze, 2006.
**Why it matters:** Visible progress, especially near the end, keeps people going.
**Rules:**
- Every finish line (setup, profile, application, checkout) has a visible stepper or progress bar.
- Give an honest head start: count steps the user really completed (e.g. "Account created ✓" as step 1). Never fake progress.
- Make the final step the easiest: a review with one button, no new fields.
**Do:** Checkout final step "Review & pay" with a prefilled summary and one button.
**Don't:** Asking for a phone number and a survey on the last step before Pay.
**Audit check:** Is progress visible and honest, and is the last step the easiest?
**Common violations:** no progress on long forms · hardest questions last · percentage bars that start at a made-up 20%.
**Misuse warning:** Laws of UX recommends "artificial progress". In the research, the head
start was a real bonus with the remaining effort shown openly (2 free stamps on a 12-stamp
card). This skill allows only that kind: a step really done or a bonus really granted, never
a percentage that misstates the work left (Ethics guardrail).

## Peak-End Rule  [Peak-End]
**Definition:** People judge an experience by its most intense moment and its end, not the average.
**Origin:** Daniel Kahneman, Barbara Fredrickson, Charles Schreiber & Donald Redelmeier, 1993
("When More Pain Is Preferred to Less: Adding a Better End").
**Why it matters:** One frustrating moment or a flat ending defines how the whole experience
is remembered, and negative moments are recalled more vividly than positive ones.
**Rules:**
- Design the success moment: what happened, a reference number, and a clear next step.
- Make error recovery humane: keep the user's data, explain the fix, offer retry and a support path.
- End every flow on a clear, positive note; never on a blank page or raw redirect.
**Do:** "Application submitted. Reference APP-2026-0142. We'll email you within 3 working days. [View application]"
**Don't:** Redirect to an empty list with a 3-second toast "Success".
**Audit check:** Are the hardest moment and the final moment designed with care?
**Common violations:** success only as a toast · errors that wipe the form · no next step after completion.

## Parkinson's Law  [Parkinson]
**Definition:** Work expands to fill the time available for it.
**Origin:** C. Northcote Parkinson, 1955 (essay in *The Economist*; book 1958).
**Why it matters:** Tasks that feel open-ended feel long; finishing faster than expected delights.
**Rules:**
- Make tasks shorter than users expect: autofill, sensible defaults, saved details, one-click repeat actions.
- Show a realistic time estimate before long tasks ("Takes about 3 minutes").
- Time estimates must be measured or conservative, never optimistic marketing.
**Do:** "Renew membership" pre-fills last year's details: review and pay in one step.
**Don't:** Re-entering 14 fields every year for a renewal.
**Audit check:** Is the task shorter than the user expects, and is its length stated?
**Common violations:** no saved details · no estimate on long forms · repeat tasks treated as new ones.
