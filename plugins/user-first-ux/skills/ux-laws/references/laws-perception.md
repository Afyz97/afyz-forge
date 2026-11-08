# Laws of Perception & Visual Organisation

How people see, group and remember what is on screen. Read when working on layout,
hierarchy, spacing, cards, steppers, navigation order, icons or "make it look better".

## Contents
1. Aesthetic-Usability Effect `[Aesthetic-Usability]`
2. Von Restorff Effect `[Von Restorff]`
3. Serial Position Effect `[Serial Position]`
4. Law of Prägnanz `[Prägnanz]`
5. Law of Proximity `[Proximity]`
6. Law of Similarity `[Similarity]`
7. Law of Common Region `[Common Region]`
8. Law of Uniform Connectedness `[Uniform Connectedness]`

---

## Aesthetic-Usability Effect  [Aesthetic-Usability]
**Definition:** Users perceive attractive designs as more usable and tolerate minor issues in them.
**Origin:** Masaaki Kurosu & Kaori Kashimura, Hitachi, 1995.
**Why it matters:** Visual quality builds trust, but it also hides problems from users and from testers.
**Rules:**
- Use one spacing scale, one type scale and a shared alignment grid; no ad-hoc values.
- Polish only after the flow and structure work (priority: usable before aesthetic).
- Judge designs by task success, not by impressions; "users liked it" is not evidence it works.
**Do:** Consistent 8px spacing scale and aligned columns across the dashboard.
**Don't:** A glossy redesign approved because it "looks modern" while users still cannot find Export.
**Audit check:** Is the screen visually consistent, and has the task (not the look) been tested?
**Common violations:** mixed paddings (13px, 18px, 22px) · misaligned form columns · polish shipped over a broken flow.
**Misuse warning:** Beauty masks usability problems in testing; always measure the task.

## Von Restorff Effect  [Von Restorff]
**Definition:** The item that differs from its group is the one noticed and remembered.
**Origin:** Hedwig von Restorff, 1933 (the isolation effect).
**Why it matters:** Emphasis is a limited budget; spending it on everything leaves nothing standing out.
**Rules:**
- Exactly one visually dominant element per decision, normally the primary CTA (filled, colour, weight).
- Every other action is visibly quieter (outline, ghost, link).
- Squint test: blur the screen; the one key element is still the first thing seen.
- Never rely on colour alone to make it differ (add weight, size, icon or label).
- Use motion for emphasis sparingly and respect `prefers-reduced-motion`.
**Do:** One filled "Submit application" button; "Save draft" as outline; "Cancel" as a link.
**Don't:** Three filled brand-colour buttons, bold text and red badges everywhere.
**Audit check:** At this decision, is exactly one element dominant, and is it the right one?
**Common violations:** primary and secondary buttons styled the same · every KPI in accent colour · "NEW" badges on half the nav.
**Misuse warning:** If everything is emphasised, nothing is.

## Serial Position Effect  [Serial Position]
**Definition:** People best remember the first (primacy) and last (recency) items in a series.
**Origin:** Hermann Ebbinghaus, 1885.
**Why it matters:** The middle of lists, menus and copy is where things get lost.
**Rules:**
- Put the most important nav items first and last (e.g. Dashboard first, Settings or Account last).
- Lead copy and lists with the key fact; put the call to action at the end.
- Never bury critical items in the middle of a long list.
**Do:** Mobile bottom nav: Home first, Profile last, frequent tasks between.
**Don't:** "Pending approvals" as the 7th of 12 sidebar links.
**Audit check:** Are the most important items at the start or end?
**Common violations:** alphabetical menus · key warning in the middle of a paragraph · primary task mid-list.

## Law of Prägnanz  [Prägnanz]
**Definition:** People interpret ambiguous or complex images in the simplest form possible, because that takes the least cognitive effort.
**Origin:** Max Wertheimer (railway-crossing lights observation, 1910; Gestalt grouping principles, 1923), with Wolfgang Köhler and Kurt Koffka.
**Why it matters:** Complex shapes and layouts take longer to resolve and get misread.
**Rules:**
- Use simple, unambiguous shapes and widely known icons; label any icon that is not universal.
- Prefer whitespace over borders and dividers to separate content.
- Keep layouts to a few clear regions the eye can resolve at a glance.
**Do:** A plain list with generous spacing and one divider between groups.
**Don't:** Boxes inside boxes with borders, shadows and dividers on every element.
**Audit check:** Can the layout be read at a glance, without decoding shapes or icons?
**Common violations:** custom abstract icons without labels · nested bordered containers · decorative shapes behind content.

## Law of Proximity  [Proximity]
**Definition:** Objects near each other are perceived as a group.
**Origin:** Gestalt psychology (Wertheimer, 1923).
**Why it matters:** Spacing is read as meaning; wrong spacing creates wrong groupings.
**Rules:**
- Spacing encodes relationships: label→its field < field→next field < group→next group.
- Each label sits visibly closer to its own field than to the field above.
- Related controls cluster together; unrelated ones are separated.
- Use one consistent spacing scale. Tokens (spacing, type scale, colour, radius, icons, motion): follow the **ui-studio** skill if installed.
  Minimum if not: one 4px spacing grid, one modular type scale (1.2–1.25), semantic colour tokens.
**Do:** `gap-2` label→input, `gap-6` between fields, `gap-10` between sections.
**Don't:** Equal 16px gaps everywhere, so labels float between two fields.
**Audit check:** Does the spacing alone show which items belong together?
**Common violations:** label equidistant from two inputs · action buttons far from the content they affect · uniform spacing across groups.

## Law of Similarity  [Similarity]
**Definition:** Elements that look alike are perceived as related or as having the same function.
**Origin:** Gestalt psychology.
**Why it matters:** Visual style is a promise about behaviour.
**Rules:**
- Elements with the same function look the same everywhere (all primary buttons, all links, all status badges).
- Different functions look different: links never look like plain text, buttons never look like tags or badges.
- Status colours mean the same thing on every screen.
**Do:** All clickable links underlined in the link colour; badges are non-interactive pills.
**Don't:** Clickable status pills that look identical to non-clickable ones.
**Audit check:** Can the user tell what is clickable, and what kind of thing it is, from its look alone?
**Common violations:** plain-text links · tag-shaped buttons · two styles for the same action on different pages.

## Law of Common Region  [Common Region]
**Definition:** Elements inside a shared boundary are perceived as a group.
**Origin:** Stephen Palmer, 1992.
**Why it matters:** Containers group content more strongly than spacing alone.
**Rules:**
- Use a card, panel or bordered section for each related group (a settings section, a pricing
  tier, a record summary). A shared background tint works as well as a border.
- One level of containers; never cards inside cards.
- The boundary must contain everything that belongs to the group, including its actions.
**Do:** Each pricing tier in its own card, with its button inside that card.
**Don't:** Plan buttons in a row below all cards, detached from their plans.
**Audit check:** Do boundaries match the real groups, with no nesting?
**Common violations:** cards in cards · actions outside the card they act on · one giant card around the whole page.

## Law of Uniform Connectedness  [Uniform Connectedness]
**Definition:** Visually connected elements (lines, shared colour, frames) are seen as more related than unconnected ones.
**Origin:** Stephen Palmer & Irvin Rock, 1994.
**Why it matters:** A connection is the strongest grouping cue, stronger than proximity or similarity.
**Rules:**
- Connect the steps of steppers and timelines with a line; completed segments filled.
- Visually link a control to what it affects (a toggle row highlights its section; a tab joins its panel).
- Do not connect unrelated items with a line or shared background by accident.
**Do:** A 4-step stepper with a line joining the circles; completed steps filled.
**Don't:** Four isolated numbered circles scattered across a header.
**Audit check:** Are elements that belong together connected, and unrelated ones not?
**Common violations:** unconnected step indicators · tabs visually detached from their panel · a decorative line implying a false relationship.
