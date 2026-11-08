# Orbit Design Engine — reference-driven UI/UX — persistent project rule (v6)

## Non-negotiable host-theme preservation
On every UI task, read `THEME-INHERITANCE.md` and the current project's design tokens **first**. Never specify, hardcode, or replace any colour or palette. Screenshots/videos are references for shape, typography, placement, interactions and motion only, not for their colours. Use the current project's actual theme tokens in all components, charts, authentication, overlays, demos and animations. Never introduce preset accent palettes.

**Apply on EVERY task that creates or changes visible web UI**: pages, layouts, navigation, tables, forms, dashboards, charts, dialogs, settings and interaction behaviour. Goal: a cohesive interface close to the original enterprise demo's visual grammar **and** the actual interaction/motion patterns observed in the user-provided dashboard video (`299130.mp4`). These are *different references*.

1. Read `.ai/uiux/orbit/REFERENCE-BRIEF.md`, `DESIGN-SPEC.md` and `MOTION-SPEC.md` as needed. For interactive dashboards, also read **`VIDEO-REFERENCE-AUDIT.md`, `VIDEO-UX-PATTERNS.md`, and `VIDEO-MOTION-PLAYBOOK.md`**, comparing relevant crops in `.ai/uiux/orbit/assets/video-reference/`. Do not claim the video is the original enterprise website reference.
2. Route to `orbit-ui-director` for multi-page redesigns and `orbit-ui-video-motion` for visual interaction. Specialist routing: `orbit-ui-interactive-kanban` (boards), `orbit-ui-team-filter-motion` (filterable cards), `orbit-ui-analytics-calendar` (charts/calendar), `orbit-ui-personalization` (accent theme), `orbit-ui-feedback-overlays` (modal/drawer/toast/timer), along with `orbit-ui-foundations`, `orbit-ui-app-shell`, `orbit-ui-components`, `orbit-ui-dashboards`, `orbit-ui-motion`, `orbit-ui-responsive`, and `orbit-ui-visual-qa` as necessary.
3. Reproduce the **behaviour** as well as the aesthetic: animated metrics based on real values, smooth drag/drop with persistence, cards physically reflowing after filter, correct tooltip per chart point, context-preserving drawer, meaningful success toasts, timer precision and saved accent preference. Never make attractive but nonfunctional controls.
4. Apply one shared design system to **every changed screen**. Prefer the project's existing CSS/UI libraries and `.ai/agents/` rules. Preserve routes, domain workflows, authorization, backend validation, locales, data integrity and performance. Do not add tasks, calendars or time tracking to projects that do not need those features.
5. Respect `prefers-reduced-motion`, contrast, keyboard and touch; don't introduce elaborate motion at the cost of usability. Use sample millisecond durations as estimated targets, not observations from source code.
6. Visually compare applicable pages against local video frames with `VIDEO-VISUAL-QA.md` and original enterprise reference (if accessible). For mobile and desktop, identify mismatches and which interactions were actually tested. Never claim an exact replica from limited recordings.
7. For backend-only changes, ignore the plugin. Automatic loading is a **persistent routing instruction**, not an unconditional invocation guarantee by Claude Code/Codex.

**Priority:** explicit user requirements, correct functionality and accessibility override superficial visual resemblance. Images are user-supplied references for local study, not production assets.


## v4 — additional reference: editorial motion (92s video)

The separate user-supplied ~92-second vertical compliance **motion-graphics explainer** is reference **C**. For any UI task first read `.ai/uiux/orbit/MOTION-ROUTING.md` and choose the appropriate reference. **Do not apply all three reference aesthetics to every screen.**

- For **landing pages, product storytelling, guided onboarding, animated product demonstrations**: consult `orbit-ui-motion-storytelling`, then the relevant `orbit-ui-kinetic-type`, `orbit-ui-layered-cards`, `orbit-ui-mascot-motion`, and `orbit-ui-motion-qa`; review `EDITORIAL-VIDEO-OBSERVATIONS.md` and `EDITORIAL-MOTION-PLAYBOOK.md` with the local `assets/editorial-video-reference/` frames. Motion should have a purposeful semantic sequence; reproduce layering, timed headlines, progress continuity and polished entrances, *not* just a checklist.
- For **ordinary operational UI**: continue to use Orbit UI foundations and the dashboard video interactions, with only restrained animation. No unsolicited flying cards, bouncy mascot, automatic scene changes or distracting copy transitions.
- For **privacy/consent/subscriptions/trust UX**, use `orbit-ui-trust-consent-ux` *only when relevant*. `EDITORIAL-UX-CHECKLIST.md` is an observed video content summary, not legal advice or a universal rulebook; never invent compliance claims/policies.
- For a motion-fidelity claim, verify both **static frames and the sequence between them**; use `orbit-ui-motion-qa`. Clearly state if a real browser/recording was unavailable. Timings are recommended targets, not recovered video source code.

When this package is installed at project scope, styles/assets are `.ai/uiux/orbit/assets/` and references are `.ai/uiux/orbit/`; with user-scope use the same structure under `~/.ai/uiux/orbit/`.


## v6 reference D — 6.175s project workspace recording

For **operational workspace navigation, project dashboards, KPI/analytics motion, task-board initial entrances, Settings page or appearance preferences**, consult `PROJECT-WORKSPACE-VIDEO-AUDIT.md` and `PROJECT-WORKSPACE-MOTION-PLAYBOOK.md`, then route to `orbit-ui-workspace-navigation`, `orbit-ui-metric-choreography`, or `orbit-ui-project-workspaces` as appropriate. Use sampled `assets/project-workspace-reference/` sequences to verify in-between motion with `PROJECT-WORKSPACE-VISUAL-QA.md`. The 6-second clip visually demonstrates KPI counting, bars, route transitions, kanban entrance, analytics period-change counters and settings loading. Its on-screen code panel *describes* an optional accent swatch GSAP effect; that specific interaction is not visibly performed in the clip. Do not automatically introduce project/task features into unrelated products.

## Reference E — 5-second split-card login/signup diagonal swipe (v7)
For **authentication, registration, sign-in, invitation** or specifically requested split-card state transitions, inspect `AUTH-VIDEO-AUDIT.md`, `AUTH-TRANSITION-PLAYBOOK.md` and `assets/auth-reference/`, then route to `orbit-ui-auth-forms` (form composition/state) and `orbit-ui-diagonal-wipe` (two-way angled sweep). Use `AUTH-VISUAL-QA.md` and `orbit-ui-motion-qa` to test *intermediate frames*, reduced motion, keyboard access and actual form validation. Reverse animation must restore the original layout. Source is a separate VERSO HTML/CSS/JS demonstration, **not** the enterprise reference site. Do not add brand-specific demo text or duplicate auth endpoints; the original app's authentication is authoritative.
