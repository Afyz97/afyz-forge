# Reference evidence and fidelity policy

## Source (external visual inspiration; not the plugin name)
- User reference: https://demo.codeandchill.store/kinlo/#/dashboard
- Product description: https://codeandchill.store/templates/kinlo
- Date of reference review: 2026-10-31

## Verified from public product description
- Domain: finance, payroll, HR back office for a cinema/venue.
- Dashboard aggregates income streams, cash and pending decisions; actions update the rest of the demo immediately.
- Interactive charts support 7-day, 12-week and 12-month views and click-through breakdowns.
- Sidebar collapses into a narrow icon rail; global search, inbox, calendar, light/dark and phone/tablet/desktop variants.
- Workflows include bill approvals, invoice stamps, account transfers, bulk card filing, staff rota drag-and-drop, hiring kanban, approvals and report export.
- Author lists React + Vite, CSS, TypeScript, GSAP and a dedicated `src/motion.ts` in the commercial source package.

## NOT verified in this authoring environment
The live JavaScript demo could not be rendered using the available web retrieval tool, and runtime network resolution blocked browser screenshot capture. Therefore actual fonts, colours, dimensions, precise elevation, chart curves, animation easing/duration, responsive layout and interaction mechanics **have not been observed**. Do not claim a pixel-perfect match or that the values in DESIGN-SPEC are measured from Kinlo.

## Fidelity-first workflow for an agent with browser access
1. Open the user URL, wait for hydration/network idle, account for cookie/theme preferences. Do not assume the fragment route is server-side navigable.
2. Observe 1440×900 desktop and 390×844 mobile; record screenshots of dashboard and at least three other routes (list, form/details, analytics). Also record a sidebar collapsed state, menu/modal open state, and both themes if supported.
3. Inspect real screenshots for: main/rail widths; top bar height; grid alignment; whitespace density; font family/weights/sizes; hierarchy; radius; borders/shadows; icon style; colour usage; charts; overlay positioning; page/element transitions. Add measurements only when directly observable.
4. Where allowed and accessible, record before/after short screen captures of hover, collapse, modal, chart switch, drag/drop and navigation. Respect website terms, do not automate account access or defeat protections.
5. Store **observations** in `reference/MEASUREMENTS.md` with confidence (observed/inferred). Store authorized screenshots in `reference/screenshots/` and compare generated pages against them.
6. Calibrate the original starter values in DESIGN-SPEC from actual evidence; prioritise shape, layout and density first, then colour/typography, then micro-animation.
7. If inaccessible, use the original design system as an approximate direction; make limitations explicit and request screenshots only if the task requires a pixel-level claim.

## Legal / identity boundary
Borrow general visual/interaction principles, not creator's copyrighted CSS/React/GSAP source, logos, name, illustration or distinctive assets. Use the project's own business identity and genuine data. This package does not include proprietary reference provider assets.


## Reference D: additional short workspace video

A user-uploaded **6.175-second vertical recording** demonstrates the Fernly-style project management dashboard with KPI/bar motion, persistent shell transitions to Tasks / Analytics / Settings, analytics range-change counter/line updates and a separately displayed `settings.js` snippet for persisted accent + GSAP swatch feedback. See `PROJECT-WORKSPACE-VIDEO-AUDIT.md`, `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md` and `assets/project-workspace-reference/` for the precise distinctions between video-observed effects and visible but unexecuted code.
