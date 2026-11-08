# Sources & Synthesis

How `omni-design` was built, what was actually inspected, and how each influence shaped it. This is an
honest record — it distinguishes sources **directly inspected in this session** from sources
**studied via prior documented research** and from **general design knowledge** (training, knowledge
cutoff January 2026). No wording, rule databases, or proprietary content was copied from any source;
all operational guidance here is independently written.

## What was directly inspected in this session

This package was built inside the **Ultimate Design Skills Suite** repository, which already contains
license-clean, originally-synthesized design content. `omni-design` re-architects and extends that
material into a single self-contained package. Directly read and synthesized from:

| Local source (this repo) | Resolved | What it contributed |
|---|---|---|
| `skills/ultimate-design/SKILL.md` (router) | ✅ read | Orchestration loop, brand-vs-product routing, "when NOT to use a style," existing-project safety, decision guide → folded into SKILL.md + style-router. |
| `skills/_shared/anti-ai-slop.md` | ✅ read | The reason-based anti-slop philosophy and detection catalog → `references/anti-slop.md`. |
| `skills/_shared/brand-vs-product.md` | ✅ read | The brand/product mode switch → SKILL.md classifier + style-router. |
| `skills/_shared/accessibility-baseline.md` | ✅ read | WCAG 2.2 floor + style hotspots → `references/accessibility.md`, checklist. |
| `skills/_shared/style-compatibility.md` | ✅ read | Dominant/supporting hybrid rule, property-ownership map → style-router §Hybrids. |
| `skills/design-foundations/SKILL.md` | ✅ read | Hierarchy/type/spacing/color/states fundamentals → `references/design-foundations.md` and split refs. |
| `docs/RESEARCH.md` | ✅ read | The prior research record (below); its findings are carried forward rather than re-fetched. |
| `docs/ARCHITECTURE.md`, `docs/omni-design-master-prompt.md`, `docs/ultimate-design-single-skill-prompt.md` | ✅ read | Structure intent, single-package requirement, scope. |

The existing repo's per-style skills (`design-neumorphism`, `design-liquid-glass`, etc.) were **not**
re-read file-by-file in this session; the style files here were written from the router summaries, the
shared references, the RESEARCH notes, and general design knowledge, then cross-checked for consistency
with the suite's stated positions.

## Sources studied via prior documented research (`docs/RESEARCH.md`)

The master brief lists many external design skills to study. In this session the network was **not**
used to re-fetch them; instead their influence is inherited through the repo's prior research record
(`docs/RESEARCH.md`, which noted network access *was* available when it was written) plus general
knowledge. Recorded honestly so nothing is overclaimed:

| Source | Status in this session | Concept influencing omni-design |
|---|---|---|
| Anthropic `frontend-design` | via RESEARCH.md + training | Intentional aesthetic direction; "one distinctive move"; anti-generic posture. |
| Anthropic `skill-creator` / `writing-skills` | ✅ skill-creator invoked this session | Description = triggers + vocabulary (not a workflow summary); progressive disclosure; references must earn their place. |
| Vercel `web-design-guidelines` | via RESEARCH.md + training | Token-first implementation; no magic numbers / z-index escalation / `!important` spiral; effect performance. |
| Impeccable | via RESEARCH.md + training | Audit-before-edit; loud↔quiet reframing; redesign-as-first-class. |
| Emil Kowalski (design engineering / motion) | via RESEARCH.md + training | Motion restraint; timing/easing/interruption; "when no animation is better." |
| UI/UX Pro Max | via RESEARCH.md + training | Value of enumerating product types + when-to/when-not per style; alias coverage. **No** palette/pairing databases copied. |
| WCAG 2.2 (W3C) | via RESEARCH.md + training | Contrast, focus visible/not-obscured, target size, reflow, text spacing, reduced motion, non-color status. |
| Apple HIG — Liquid Glass / visionOS | via RESEARCH.md + training | Liquid Glass = control layer over content, adaptive vibrancy, Reduce Transparency/Motion; spatial windows/volumes, gaze+pinch, comfort. Pages are JS-rendered; **verify current HIG before native work.** |
| MDN / web.dev (CSS platform) | via RESEARCH.md + training | `backdrop-filter` cost/fallbacks, `prefers-*` queries, compositor-only animation, `color-mix`/custom properties. |

Additional skills named in the brief (Dembrandt, Addy Osmani `frontend-ui-engineering`, `interface-
design`, OilOil, `ui-ux-design-pro`, `mobile-app-ui-design`, `expo-liquid-glass`, Apple skills,
`tailwind-design-system`, `frontend-design-system`, `awesome-copilot` reviewers, `designer-skills`,
Bencium, `refactoring-ui-skill`, wondelai, accesslint, Excalidraw, App-Store-screenshot skills, Theme
Factory, Brand Guidelines, Canvas/Algorithmic Art) were **not individually fetched or inspected** in
this session. Their general principles (many overlap heavily with the sources above — refactoring-UI
hierarchy/spacing heuristics, accessibility auditing, mobile platform conventions, brand-to-UI,
design-system engineering) are reflected through general knowledge, but no claim is made that each
specific repository was studied here. Fetching and per-source study remain a documented next step.

## Source comparison matrix (condensed)

| Influence | Unique strength | Overlap | Kept as | 
|---|---|---|---|
| ultimate-design router | brand/product routing, when-NOT | with brief's classifier | → SKILL.md core |
| anti-ai-slop (shared) | reason-based detection | with review | → `references/anti-slop.md` |
| accessibility-baseline | WCAG floor + style hotspots | with every style | → `references/accessibility.md` (hard gate) |
| style-compatibility | dominant/supporting map | with hybrids | → style-router §Hybrids |
| frontend-design / Impeccable | direction + audit-first | each other | → workflows create/redesign/audit |
| Emil (motion) | restraint, timing | with foundations | → `references/motion.md` |
| Vercel / refactoring-UI | token-first, hierarchy | with systems | → `references/design-systems.md`, foundations |
| Apple HIG | Liquid Glass / spatial | — | → `styles/liquid-glass.md`, `spatial-ui.md` (verify-HIG caveats) |

## Structural decisions (how this differs from the brief's suggested tree)

The brief suggested ~70 files (one per style, one per micro-topic). This package **consolidates where
consolidation improves coherence and context-efficiency** — the brief explicitly rewards "reduce
redundancy" and "don't generate unnecessary files merely for completeness." Concretely:

- **One `styles/style-router.md`** carries compact profiles for *every* named style (minimalism →
  material/HIG) + hybrid rules; the **10 hardest styles** get dedicated deep files. Lightweight styles
  (editorial, Swiss, industrial, luxury, playful, corporate, retro/futuristic, material) are executed
  from router profiles rather than near-empty stubs.
- **References merged** where topics are inseparable: motion+micro-interactions, states+loading/empty/
  error, enterprise+dashboards, systems+tokens, reference+image-to-code, content+icon policy.
- **Adapters grouped** by ecosystem (Laravel priority; React/Next; Vue/Nuxt/Svelte; native mobile) with
  a detection `overview`, instead of 15 thin per-framework files.

Every file carries real, non-redundant guidance; there are no empty files or stubs.

## Licensing & ethics

- Apache-2.0. All guidance independently written; no copied text, rule databases, or proprietary
  palettes/pairings.
- Referenced commercial products (Stripe, Linear, Apple, Shopee, etc.) are handled as **principle
  extraction, never cloning** (`references/brand-to-ui.md`).
- WCAG/HIG are cited as standards to *verify against*, not reproduced.

## Honest limitations of this research

- Upstream third-party skill repositories were not individually fetched/inspected in this session;
  influence is via prior documented research and general knowledge, and is labeled as such above.
- Apple HIG / visionOS material is fast-moving and partly JS-rendered — verify current guidance before
  native implementation.
- Popularity/adoption of third-party skills was not independently quantified.
