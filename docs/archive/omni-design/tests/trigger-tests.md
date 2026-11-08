# Trigger Tests

Checks that the skill's `description` fires on real design work and stays quiet on non-design work that
merely shares vocabulary. Should-trigger and should-not-trigger cases.

## Should trigger (design work)
- "Redesign this admin dashboard and keep all the functionality."
- "Make this landing page look less generic and more premium."
- "Design a mobile checkout flow for our store."
- "Build a settings page that matches our existing components."
- "Audit this signup form for accessibility and usability."
- "Turn this screenshot into a responsive React page."
- "Make this app feel more native / follow Apple HIG."
- "Apply a bento grid to our product overview."
- "Give this a neumorphic / glassmorphic / brutalist look." (each style)
- "Clean up this AI-generated SaaS page."
- "Set up design tokens and a component system."
- "60% minimalism, 25% bento, 15% liquid glass." (hybrid)
- "This dashboard feels cluttered and hard to scan — improve it."
- "Add dark mode and make sure contrast is fine."

## Should NOT trigger (near-misses sharing vocabulary)
- "Design a **database** schema for orders." (data modeling, not UI)
- "Build a **minimal API** with three endpoints." (backend)
- "Create a **glass table** to join users and sessions." (SQL)
- "Fix this **brutal** off-by-one **error** in the parser." (bug)
- "Set up a **spatial database** / PostGIS index." (backend)
- "Refactor this **clay** 3D **model** loader." (non-UI graphics/asset)
- "Write the **color**-coding logic for our log **levels**." (backend logic)
- "Optimize the **render** performance of this batch job." (compute)
- "Add a **motion** sensor integration to the firmware." (hardware)
- "Improve the **layout** of this Markdown README." (docs, not UI design)

## Notes on triggering
The description front-loads *what + when + style aliases* and explicitly excludes the near-misses above
("minimal API," "glass table (SQL)," "brutal error," "spatial database," "clay model," backend/API/
database/non-UI). If a should-trigger case misses or a should-not-trigger case fires, tune the
description's wording and exclusions — not the skill body.
