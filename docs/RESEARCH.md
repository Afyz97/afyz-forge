# Research Notes — Ultimate Design Skills Suite

> Recorded during construction of this suite. Network access **was** available during
> research; where a specific source could not be machine-read (e.g. JavaScript-rendered
> Apple HIG pages), that limitation is noted and the content is grounded in the author
> model's training knowledge (knowledge cutoff January 2026) plus the canonical URL for
> the reader to verify.

## How to read this document

For each source we record: relevance, distinctive strengths, useful architecture,
triggering/review/anti-pattern/evaluation ideas worth adapting, and gaps. We did **not**
copy wording, rule databases, or proprietary content from any source. All operational
guidance in the skills is synthesized and original.

---

## 1. Agent Skills specification (agentskills.io / anthropics/skills)

- **Verified live.** Confirmed current frontmatter contract: `name` (≤64 chars, lowercase
  `a-z0-9` + single hyphens, no leading/trailing/consecutive hyphens, must match parent
  directory), `description` (≤1024 chars, what + when), optional `license`,
  `compatibility`, `metadata`, `allowed-tools`.
- **Progressive disclosure model:** metadata (~100 tokens) always loaded → SKILL.md body
  (<5k tokens recommended, <500 lines) loaded on activation → `references/`, `scripts/`,
  `assets/` loaded on demand.
- **Adopted:** exact frontmatter format; SKILL.md kept operational; heavy/shared knowledge
  pushed into `references/`; a `scripts/` deterministic auditor; validation via `skills-ref`
  naming rules.
- **Gap:** the spec is format-only — it says nothing about *design* quality. That is the
  entire value this suite adds.

## 2. Anthropic `frontend-design`

- **Relevance:** the closest first-party analog. Establishes that a single skill can lift
  baseline UI quality by encoding taste (typography restraint, spacing rhythm, avoiding
  templated defaults, intentional aesthetic direction).
- **Strength:** strong "don't ship the obvious default" stance; aesthetic-direction framing.
- **Adopted:** the idea of an explicit *aesthetic direction* step (our orchestrator Phase 3);
  the "one distinctive move" heuristic; anti-generic posture.
- **Gap we address:** it is one general skill. It does not carry deep, *named* style systems
  (neumorphism, liquid glass, spatial), nor an independent reviewer, nor style-vs-usability
  arbitration. This suite is a modular system with a router.

## 3. Anthropic `skill-creator` / `writing-skills` (Superpowers)

- **Relevance:** methodology for *how* to write skills, not design content.
- **Adopted:** TDD-for-skills mindset (baseline → skill → close loopholes); description =
  triggering conditions + keywords, not a workflow summary that agents shortcut;
  "one excellent example beats many"; reference files must justify their existence;
  rationalization tables + red-flag lists for discipline skills (used in `design-review`
  and the anti-slop system).
- **Gap:** it is process-only; supplies no design judgment.

## 4. Vercel `web-design-guidelines` / React best-practice skills

- **Relevance:** implementation-quality bar for web/React UI — semantic tokens, avoiding
  one-off CSS, component API design, accessibility defaults, performance of effects.
- **Adopted:** token-first implementation posture in `design-system-engineering`; the
  "no magic numbers / no arbitrary z-index escalation / no `!important` spiral" checklist;
  performance framing for expensive effects (backdrop-filter, shadow stacks).
- **Gap:** framework-leaning and general-modern-aesthetic; not style-pluralistic.

## 5. Impeccable (frontend design/redesign skill)

- **Relevance:** audit-first redesign workflow; treats "make it less generic / bolder /
  quieter" as first-class tasks.
- **Adopted:** the **audit-before-edit** phase (our Phase 2), and the loud↔quiet framing
  used in `design-maximalism`/`design-minimalism` and the orchestrator's direction step.
- **Gap:** single-skill breadth; we split into router + specialists + reviewer.

## 6. Emil Kowalski — design-engineering / motion

- **Relevance:** the strongest available articulation of *motion restraint* and
  invisible-detail polish (easing, duration, interruption, "when no animation is better").
- **Adopted:** the `design-motion` philosophy — motion must aid comprehension, not decorate;
  hover restraint; reduced-motion as a first-class path; transform/opacity-only for
  compositor-friendliness.
- **Gap:** motion-focused; not a full style system.

## 7. UI/UX Pro Max

- **Relevance:** breadth catalog (styles, palettes, font pairings, product types, UX rules).
- **Adopted (as inspiration, not copied):** the value of enumerating *product types* and
  *when-to / when-not-to* per style; alias/keyword coverage for triggering.
- **Explicitly NOT adopted:** any proprietary palette/pairing database or rule text. Our
  token guidance is strategy-based ("which tokens are style-defining vs product-dependent")
  rather than fixed value tables copied from anywhere.

## 8. Primary design guidance (standards & platform)

- **W3C WCAG 2.2** (verifiable at w3.org/TR/WCAG22): adopted contrast (1.4.3 / 1.4.11),
  focus visible + not obscured (2.4.7 / 2.4.11), target size (2.5.8, 24×24 min), reflow
  (1.4.10), text spacing (1.4.12), reduced motion (animation-from-interactions 2.3.3),
  non-color communication (1.4.1). Every style skill carries a WCAG-aligned accessibility
  section and is instructed **never to claim compliance from visual inspection alone.**
- **Apple Human Interface Guidelines — Materials / Liquid Glass** (developer.apple.com):
  page is JavaScript-rendered and could not be machine-read; content grounded in training
  knowledge of the WWDC 2025 "Liquid Glass" release (iOS/iPadOS/macOS/visionOS): an
  *adaptive material* that refracts and reflects surrounding content, used for the
  **controls/navigation layer floating above content**, not as wallpaper on every surface;
  respects **Reduce Transparency** and **Reduce Motion**; legibility is preserved by the
  system via adaptive vibrancy. The `design-liquid-glass` skill distinguishes authentic
  platform material from web CSS approximations and forbids claiming parity.
- **Apple visionOS / spatial design** (developer.apple.com/visionos): grounded in training
  knowledge — windows, volumes, and immersive spaces; depth/scale/anchoring; gaze+pinch as
  primary input; comfort (avoid rapid motion, keep content in a comfortable field of view);
  ergonomics. Drives `design-spatial-ui`, which separates true XR from pseudo-spatial web.
- **CSS platform guidance** (MDN / web.dev): `backdrop-filter` cost and fallbacks,
  `prefers-reduced-motion`, `prefers-contrast`, compositor-only animation, `color-mix()`
  and custom properties for tokens.

---

## Synthesis decisions (what the research changed)

1. **Modular over monolith** — a router (`ultimate-design`) + shared foundations + 10
   style specialists + an independent reviewer, instead of one general skill. Justified in
   `docs/ARCHITECTURE.md`.
2. **Descriptions carry vocabulary + aliases** but never a workflow summary agents can
   shortcut (Superpowers finding).
3. **Style skills are self-sufficient** (portability) yet cross-link shared references to
   avoid duplicating the anti-slop and brand/product logic 10 times.
4. **Accessibility and usability outrank style purity** — encoded as a hard rule in every
   style skill, most aggressively in neumorphism and glass/liquid-glass.
5. **A deterministic auditor exists but stays humble** — it flags only mechanically
   detectable smells (shadow/blur/radius counts, missing focus, hardcoded colors) and
   never pretends to lint taste.

## Limitations of the research

- Some primary sources (Apple HIG) are JS-rendered and were not machine-read; grounded in
  training knowledge + canonical URLs for reader verification.
- Popularity/adoption signals for third-party skills were not independently quantified.
- No copied text, rule databases, or proprietary palettes from any studied project.
