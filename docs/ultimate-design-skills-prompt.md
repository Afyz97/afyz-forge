# Ultimate Design Skills Suite — Master Creation Prompt

You are tasked with researching, architecting, implementing, testing, and documenting an open, production-grade **Ultimate Design Skills Suite** for AI coding agents.

The suite must work as portable Agent Skills wherever practical, especially with:

- Claude Code
- Codex CLI
- other Agent Skills-compatible coding agents

Do not create a single bloated generic design skill. Build a modular system of specialized skills with progressive disclosure, strong trigger descriptions, shared design reasoning, style-specific expertise, implementation guidance, anti-patterns, review workflows, and evaluations.

---

## 1. PRIMARY OBJECTIVE

Create an expert-level AI design skill ecosystem that can:

1. design new interfaces from scratch;
2. redesign existing interfaces;
3. improve weak or generic AI-generated interfaces;
4. preserve an existing product’s design language;
5. intentionally apply a requested visual style;
6. choose an appropriate visual style when none is specified;
7. combine compatible styles only when justified;
8. review and critique existing UI;
9. implement production-grade UI in the project’s actual stack;
10. distinguish brand/marketing UI from product/application UI;
11. handle responsive behavior;
12. maintain accessibility;
13. maintain interaction quality;
14. maintain performance;
15. maintain implementation quality;
16. avoid common AI-generated design clichés;
17. evaluate whether the resulting interface genuinely matches its intended design language.

The required design families are:

- Skeuomorphism
- Neumorphism
- Glassmorphism
- Claymorphism
- Minimalism
- Maximalism
- Brutalism
- Liquid Glass
- Bento Grid
- Spatial UI Design

Support common aliases and misspellings in skill triggering, including:

- skeuomorphism
- skeomorphism
- skeuomorphic
- neumorphism
- neomorphism
- soft UI
- glass UI
- glassmorphism
- clay UI
- claymorphism
- minimalist
- maximalist
- brutalist
- liquid glass
- Apple-style glass
- bento
- bento grid
- spatial UI
- spatial computing UI
- immersive UI
- 3D interface

Do not blindly equate aliases where the underlying concepts differ. Use aliases for discovery, then apply the correct design model.

---

## 2. FIRST: INSPECT THE LOCAL ENVIRONMENT

Before creating anything:

1. inspect the current repository;
2. read all existing project instructions;
3. inspect memory files;
4. inspect relevant markdown documentation;
5. inspect existing skills;
6. inspect agent-specific configuration;
7. inspect existing design systems;
8. inspect component libraries;
9. inspect package manifests;
10. inspect framework and language versions;
11. inspect current CSS architecture;
12. inspect test infrastructure;
13. inspect browser automation infrastructure;
14. inspect linting and accessibility tooling.

Pay special attention to directories such as:

- `.ai/`
- `.ai/agents/`
- `.claude/`
- `.codex/`
- `skills/`
- `.agents/`
- `docs/`
- project memory files
- `CLAUDE.md`
- `AGENTS.md`
- `README.md`
- existing `SKILL.md` files

Do not overwrite existing skills or conventions without first understanding them.

If this repository already contains a skill creator, marketplace integration, skill template, or evaluation framework, reuse it where appropriate.

---

## 3. RESEARCH CURRENT HIGH-QUALITY DESIGN SKILLS

Before implementation, perform current research when network access is available.

At minimum, study the public structure, documented capabilities, architectural patterns, strengths, limitations, and triggering strategies of relevant projects such as:

- Anthropic `frontend-design`
- Anthropic `skill-creator`
- Anthropic public Agent Skills examples and specification
- Vercel `web-design-guidelines`
- Vercel React best-practice skills where relevant to UI implementation
- Impeccable
- Emil Kowalski design-engineering skill
- UI/UX Pro Max
- other genuinely high-quality and currently prominent UI/UX/design skills discovered during research

Also study primary design guidance where relevant, including:

- W3C WCAG
- platform Human Interface Guidelines
- current Apple guidance for Liquid Glass
- current Apple spatial computing / visionOS design guidance
- browser platform guidance
- framework documentation
- established accessibility documentation

Do not assume the examples listed above are automatically the best merely because they are named here.

Evaluate them.

Look for newer or stronger alternatives.

Record:

- source/project;
- current relevance;
- popularity signal where verifiable;
- distinctive strengths;
- useful architecture;
- useful triggering strategy;
- useful review strategy;
- useful anti-pattern strategy;
- useful evaluation strategy;
- weaknesses or gaps;
- ideas worth adapting.

IMPORTANT:

- Do not copy copyrighted text.
- Do not clone another skill’s wording.
- Do not disguise copied instructions as original work.
- Do not copy proprietary rule databases.
- Respect licenses.
- Synthesize principles into original operational guidance.
- Record attribution where required by the source license.

If network access is unavailable, continue using available local information and explicitly document the research limitation. Do not stop the task.

---

## 4. USE THE OPEN AGENT SKILLS ARCHITECTURE

Follow the current Agent Skills specification unless the local environment requires a compatible adaptation.

Use progressive disclosure.

Each skill should normally contain:

```text
skill-name/
├── SKILL.md
├── references/
│   ├── principles.md
│   ├── implementation.md
│   ├── components.md
│   ├── anti-patterns.md
│   ├── accessibility.md
│   ├── responsive.md
│   └── evaluation.md
├── examples/
│   └── ...
├── scripts/
│   └── ... only when justified
└── assets/
    └── ... only when justified
```

Do not create empty directories merely to satisfy this example.

Keep the main `SKILL.md` concise and operational.

Move deep knowledge into references.

Every reference file must have a clear reason to exist.

Avoid duplicating the same large body of instructions across every skill.

However, preserve portability: a specialized skill must still contain enough critical guidance to function correctly when used independently.

---

## 5. REQUIRED SKILL ARCHITECTURE

Create the following skills unless repository analysis demonstrates a clearly superior architecture.

### A. `ultimate-design`

Purpose:

The main orchestrator and design router.

Responsibilities:

- understand the user’s goal;
- inspect the product context;
- distinguish brand UI from product UI;
- detect whether a style was explicitly requested;
- choose the appropriate specialist skill;
- combine skills only when justified;
- create an aesthetic direction;
- establish design intent;
- coordinate implementation;
- invoke review after implementation;
- resolve conflicts between style and usability;
- preserve project conventions where appropriate;
- avoid arbitrary style mixing.

It must know when NOT to use a particular style.

It must not merely generate a generic “modern UI.”

### B. `design-foundations`

Cross-style design intelligence covering:

- visual hierarchy;
- composition;
- spacing;
- rhythm;
- typography;
- type scales;
- color;
- contrast;
- semantic tokens;
- layout;
- grids;
- alignment;
- balance;
- density;
- affordance;
- feedback;
- interaction states;
- responsive design;
- accessibility;
- motion;
- iconography;
- content hierarchy;
- information architecture;
- perceived quality;
- platform conventions;
- performance implications;
- design-system consistency.

This is not a visual style skill.

It establishes non-negotiable foundations.

### C. `design-system-engineering`

Purpose:

Translate visual direction into maintainable implementation.

Cover:

- design tokens;
- semantic tokens;
- primitive tokens;
- component tokens;
- typography tokens;
- spacing scales;
- radius systems;
- elevation systems;
- transparency systems;
- motion tokens;
- responsive tokens;
- state tokens;
- light/dark themes;
- high-contrast considerations;
- component variants;
- composability;
- API design for UI components;
- avoiding one-off CSS;
- preserving existing systems.

### D. `design-motion`

Use the best principles of high-quality design engineering and motion design.

Cover:

- motion purpose;
- continuity;
- spatial relationships;
- entering/exiting;
- transforms;
- opacity;
- easing;
- duration;
- interruption;
- gesture response;
- state transition;
- modal motion;
- drawer motion;
- toast behavior;
- layout animation;
- hover restraint;
- reduced motion;
- performance;
- when no animation is better.

Motion must reinforce comprehension rather than decorate every element.

### E. `design-review`

A strict independent reviewer.

It must inspect:

- style fidelity;
- visual hierarchy;
- generic AI patterns;
- excessive cards;
- excessive rounding;
- arbitrary gradients;
- unnecessary glass;
- arbitrary shadows;
- excessive pills;
- weak typography;
- poor spacing;
- inconsistent density;
- weak content hierarchy;
- decorative labels with no meaning;
- fake metrics;
- unnecessary dashboard patterns;
- accessibility;
- responsiveness;
- keyboard interaction;
- focus states;
- interaction feedback;
- motion;
- performance;
- component consistency;
- code maintainability.

The reviewer must provide:

1. findings;
2. severity;
3. evidence;
4. why it matters;
5. exact corrective action;
6. whether correction changes the intended style.

Where possible, distinguish:

- objective defect;
- likely defect;
- subjective preference.

### F. Specialized style skills

Create all of the following:

1. `design-skeuomorphism`
2. `design-neumorphism`
3. `design-glassmorphism`
4. `design-claymorphism`
5. `design-minimalism`
6. `design-maximalism`
7. `design-brutalism`
8. `design-liquid-glass`
9. `design-bento-grid`
10. `design-spatial-ui`

---

## 6. CONTRACT FOR EVERY SPECIALIZED STYLE SKILL

Each style skill must be expert enough to work independently.

Each must include the following sections or equivalent operational structure.

### 6.1 Definition

Explain what the style actually is.

Distinguish it from visually similar styles.

Do not reduce a design language to one CSS effect.

Example of unacceptable reasoning:

- glassmorphism = `backdrop-filter: blur(...)`
- neumorphism = two box shadows
- brutalism = ugly fonts
- minimalism = lots of white
- liquid glass = transparent rounded cards
- bento = a CSS grid
- spatial UI = add 3D transforms

The skill must understand the complete design language.

### 6.2 Historical and conceptual model

Provide enough background to understand:

- why the style exists;
- what visual logic drives it;
- what interaction assumptions it makes;
- where it tends to work;
- where it tends to fail.

Keep history useful and operational, not encyclopedic.

### 6.3 Visual grammar

Define:

- form;
- shape;
- surface;
- material;
- depth;
- borders;
- radius;
- shadows;
- lighting;
- color;
- contrast;
- typography;
- spacing;
- density;
- imagery;
- iconography;
- motion;
- layering;
- composition;
- interaction states.

### 6.4 Design tokens

Provide a token strategy rather than rigid universal values.

Cover:

- color roles;
- surface roles;
- text roles;
- border roles;
- radius;
- elevation;
- blur;
- transparency;
- lighting;
- shadows;
- spacing;
- typography;
- motion.

Explain which tokens are style-defining and which remain product-dependent.

### 6.5 Component translation

Explain how the style applies to:

- buttons;
- inputs;
- cards;
- navigation;
- sidebars;
- modals;
- dialogs;
- dropdowns;
- tables;
- tabs;
- accordions;
- alerts;
- toasts;
- forms;
- charts;
- empty states;
- mobile navigation;
- hero sections;
- pricing sections;
- dashboards;
- e-commerce;
- admin systems.

Do not force the same treatment onto every component.

### 6.6 Brand versus product mode

Every style must distinguish between:

#### Brand mode

Examples:

- landing pages;
- campaigns;
- portfolios;
- editorial experiences;
- event sites;
- marketing pages.

Brand mode may permit stronger expression.

#### Product mode

Examples:

- dashboards;
- admin panels;
- SaaS;
- e-commerce workflows;
- data-heavy systems;
- internal applications.

Product mode must prioritize clarity, repeated use, state recognition, density, and task completion.

Do not apply marketing-page aesthetics blindly to operational software.

### 6.7 When to use

Describe appropriate:

- products;
- audiences;
- contexts;
- emotional goals;
- information density;
- platform situations.

### 6.8 When not to use

Explicitly identify:

- unsuitable product types;
- accessibility conflicts;
- density conflicts;
- performance constraints;
- interaction constraints;
- contexts where another style is better.

### 6.9 Anti-patterns

Create style-specific anti-patterns.

Every anti-pattern should contain:

- name;
- detection clue;
- why it weakens the design;
- corrective strategy.

Avoid vague advice such as “make it look professional.”

### 6.10 Accessibility

For every style:

- maintain readable contrast;
- maintain visible focus;
- maintain keyboard operability;
- maintain meaningful state differentiation;
- avoid color-only communication;
- respect reduced motion;
- provide fallbacks for transparency;
- consider zoom and text resizing;
- consider touch target sizing;
- avoid style purity becoming more important than access.

Target current WCAG guidance appropriate to the project.

Do not falsely claim WCAG compliance based only on visual inspection.

### 6.11 Responsive behavior

Explain how the design language transforms rather than merely shrinks.

Cover:

- mobile;
- tablet;
- desktop;
- ultrawide;
- touch;
- pointer;
- keyboard.

For relevant skills, include spatial or immersive contexts.

### 6.12 Performance

Explain performance risks specific to the style.

Examples:

- multiple backdrop filters;
- huge blur regions;
- expensive shadows;
- excessive compositing;
- continuous animation;
- large textures;
- unnecessary 3D scenes.

Provide graceful fallback strategies.

### 6.13 Implementation guidance

Support the actual project stack first.

Then provide portable patterns where useful.

Potential stacks include:

- semantic HTML/CSS/JavaScript;
- Tailwind CSS;
- React;
- Next.js;
- Vue;
- Nuxt;
- Svelte;
- Laravel Blade;
- Livewire;
- Alpine.js;
- shadcn/ui;
- SwiftUI;
- React Native;
- Flutter.

Do not pretend to support a stack unless meaningful guidance exists.

Do not replace the project’s framework without user authorization.

### 6.14 Review checklist

Each skill must contain a style-specific audit checklist.

### 6.15 Examples

Include examples of:

- good use;
- bad use;
- subtle use;
- expressive use;
- product use;
- brand use.

Examples should demonstrate principles rather than copy commercial interfaces.

---

## 7. STYLE-SPECIFIC REQUIREMENTS

### 7.1 `design-skeuomorphism`

Must understand:

- physical-world metaphor;
- recognizable affordances;
- material cues;
- realistic or semi-realistic depth;
- tactile controls;
- texture restraint;
- functional metaphor;
- visual familiarity;
- modern skeuomorphic adaptation.

Must distinguish:

- useful physical affordance

from:

- decorative fake realism.

Must cover the danger of:

- excessive ornament;
- obsolete metaphors;
- visual noise;
- inaccessible text over texture;
- inconsistent physical logic.

### 7.2 `design-neumorphism`

Must understand:

- same-surface extrusion;
- embossed and debossed states;
- paired light/shadow systems;
- controlled low-contrast surfaces;
- soft UI;
- light-source consistency.

Must aggressively address common failures:

- invisible controls;
- insufficient contrast;
- ambiguous pressed states;
- everything appearing disabled;
- excessive same-surface treatment;
- unusable forms.

Accessibility must override stylistic purity.

### 7.3 `design-glassmorphism`

Must understand:

- translucent surfaces;
- background relationship;
- layered depth;
- blur;
- borders and edge definition;
- tint;
- saturation;
- contrast management;
- hierarchy through material.

Must distinguish glassmorphism from:

- generic transparent cards;
- Liquid Glass;
- simple opacity;
- frosted overlays.

Must provide fallbacks when backdrop filtering is unavailable or inappropriate.

### 7.4 `design-claymorphism`

Must understand:

- inflated soft geometry;
- chunky dimensionality;
- playful mass;
- soft 3D surfaces;
- rounded forms;
- friendly illustration;
- controlled inner/outer depth.

Must prevent:

- every component becoming a toy;
- unreadable density;
- excessive shadow accumulation;
- childish styling in inappropriate domains.

### 7.5 `design-minimalism`

Must understand:

- reduction;
- hierarchy;
- restraint;
- purposeful negative space;
- essential content;
- typographic quality;
- precision;
- progressive disclosure.

Must explicitly reject:

- “minimalism = empty page”
- “minimalism = monochrome”
- “minimalism = use Inter everywhere”
- weak hierarchy;
- hidden functionality;
- excessive whitespace that damages efficiency.

Minimalism must still have identity.

### 7.6 `design-maximalism`

Must understand:

- controlled abundance;
- deliberate layering;
- expressive typography;
- pattern;
- image density;
- color interaction;
- asymmetry;
- visual rhythm;
- editorial composition.

Must distinguish:

- maximalism

from:

- random clutter.

Require hierarchy even at high visual density.

### 7.7 `design-brutalism`

Must understand:

- rawness;
- directness;
- exposed structure;
- hard contrast;
- unconventional grids;
- utilitarian or anti-polish expression;
- typographic force;
- deliberate awkwardness where appropriate.

Must distinguish:

- intentional brutalism

from:

- unfinished CSS;
- broken responsive behavior;
- inaccessible contrast;
- careless spacing.

Also consider neo-brutalism where relevant, but do not collapse the two into one concept.

### 7.8 `design-liquid-glass`

This skill requires especially careful current research.

Use current primary platform guidance where available.

Must distinguish:

1. authentic platform-native Liquid Glass;
2. web implementations inspired by Liquid Glass;
3. ordinary glassmorphism.

Must understand concepts such as:

- dynamic material;
- content versus controls;
- adaptive appearance;
- optical depth;
- translucency;
- highlights;
- material response;
- layered navigation;
- hierarchy;
- movement;
- shape transformation where platform capabilities support it.

Do not create “Apple clone” interfaces by default.

Do not claim a CSS approximation is identical to native platform material.

For web implementations:

- preserve text readability;
- provide contrast fallback;
- control blur cost;
- avoid glass on every surface;
- avoid excessive floating rounded containers;
- ensure interface hierarchy remains clear.

### 7.9 `design-bento-grid`

Must understand Bento Grid as an information-composition system, not merely:

```css
display: grid;
```

Cover:

- modular hierarchy;
- variable spans;
- content priority;
- visual rhythm;
- scan paths;
- density;
- card relationships;
- feature emphasis;
- responsive regrouping;
- avoiding repetitive equal cards.

Must determine when the content genuinely benefits from modular grouping.

Do not turn every page into a bento dashboard.

### 7.10 `design-spatial-ui`

This skill requires especially careful current research.

Distinguish:

1. conventional 2D interfaces using depth cues;
2. pseudo-spatial web UI;
3. true spatial computing;
4. AR interfaces;
5. VR interfaces;
6. mixed-reality interfaces.

Cover:

- depth;
- scale;
- distance;
- field of view;
- anchoring;
- windows;
- volumes;
- immersive spaces;
- occlusion;
- comfort;
- discoverability;
- gaze interaction;
- hand interaction;
- voice interaction;
- pointer interaction;
- focus;
- selection feedback;
- spatial audio where relevant;
- motion comfort;
- physical environment awareness.

Do not apply true spatial-computing assumptions to ordinary websites.

For a standard web project, produce a web-appropriate spatial interpretation unless genuine XR capabilities are requested.

---

## 8. ORCHESTRATOR DECISION SYSTEM

The `ultimate-design` skill must use a deliberate decision process.

Before designing, infer or establish:

- product;
- audience;
- primary task;
- platform;
- content type;
- information density;
- brand personality;
- emotional target;
- accessibility requirements;
- performance constraints;
- existing design system;
- requested style;
- implementation stack.

When the user explicitly requests a style:

- honor it;
- assess suitability;
- adapt it to the product;
- do not silently replace it with a generic modern aesthetic.

When the user does not request a style:

- choose intentionally;
- explain the internal design direction concisely in working notes;
- do not randomly default to glassmorphism;
- do not randomly default to bento;
- do not randomly default to purple gradients;
- do not randomly default to dark mode.

---

## 9. STYLE COMPOSITION

Support hybrid design only when justified.

Create a compatibility guide.

Examples of potentially meaningful combinations may include:

- minimalism + bento grid;
- glassmorphism + spatial depth;
- claymorphism + playful maximalist accents;
- brutalist structure + minimal interaction model;
- skeuomorphic affordances inside restrained modern UI.

These are examples, not automatic recommendations.

For every combination:

1. choose a dominant design language;
2. identify the supporting language;
3. define which properties belong to each;
4. prevent stylistic contradiction;
5. preserve hierarchy;
6. preserve usability.

Do not create “design soup.”

---

## 10. ANTI-AI-SLOP SYSTEM

Create an original anti-pattern framework informed by current public research and existing high-quality design tools, without copying proprietary databases.

Detect patterns such as:

- gratuitous purple-blue gradients;
- excessive gradient text;
- excessive rounded cards;
- nested cards inside cards;
- everything floating;
- excessive glass;
- random glow;
- default dark SaaS aesthetic;
- generic hero structure;
- meaningless statistic cards;
- decorative 01/02/03 numbering with no semantic purpose;
- excessive pill badges;
- icon-in-colored-square repetition;
- arbitrary blobs;
- fake testimonials;
- fake metrics;
- meaningless charts;
- weak copy;
- identical section rhythm;
- giant headline plus generic gradient;
- overuse of centered layouts;
- excessive hover movement;
- every element animating;
- unnecessary 3D transforms;
- mobile layouts that are merely collapsed desktop layouts;
- excessive empty space;
- using one fashionable aesthetic regardless of product.

The detector must not ban a pattern simply because AI frequently uses it.

A pattern is acceptable when:

- semantically appropriate;
- deliberately chosen;
- contextually justified;
- well executed.

---

## 11. DESIGN PROCESS

Every build or redesign workflow should generally follow:

### Phase 1 — Understand

- product;
- user;
- task;
- content;
- constraints;
- stack.

### Phase 2 — Audit

For existing UI:

- inspect current implementation;
- identify strengths;
- identify problems;
- identify design debt;
- preserve what already works.

### Phase 3 — Direction

Define:

- concept;
- mood;
- dominant style;
- typography direction;
- color logic;
- layout logic;
- interaction logic;
- one justified distinctive design move.

Do not redesign merely for novelty.

### Phase 4 — System

Define:

- tokens;
- type scale;
- spacing;
- surfaces;
- radii;
- borders;
- elevation;
- motion;
- responsive behavior.

### Phase 5 — Implement

Use:

- semantic markup;
- existing project architecture;
- maintainable components;
- meaningful content;
- real states.

### Phase 6 — Validate

Check:

- functionality;
- responsiveness;
- accessibility;
- interaction;
- style fidelity;
- performance.

### Phase 7 — Review

Invoke the design reviewer independently.

### Phase 8 — Refine

Fix issues based on severity and evidence.

---

## 12. EXISTING PROJECT SAFETY

When modifying an existing system:

- do not break functionality;
- do not remove features merely because they complicate the design;
- do not rewrite the entire frontend unnecessarily;
- do not replace the established framework casually;
- do not introduce dependencies without justification;
- preserve localization;
- preserve RTL where relevant;
- preserve validation;
- preserve authorization;
- preserve loading states;
- preserve error states;
- preserve empty states;
- preserve responsive behavior.

Inspect before editing.

---

## 13. IMPLEMENTATION QUALITY

Generated UI must be:

- production-oriented;
- maintainable;
- responsive;
- accessible;
- semantically structured;
- consistent with the stack;
- testable.

Prefer:

- CSS variables or framework-equivalent tokens;
- reusable primitives;
- component variants;
- semantic naming;
- clear state handling.

Avoid:

- unexplained magic numbers;
- random one-off colors;
- arbitrary z-index escalation;
- excessive `!important`;
- unnecessary JavaScript for CSS-solvable behavior;
- duplicated style logic;
- inaccessible custom controls.

---

## 14. VISUAL VALIDATION

When browser or screenshot tooling is available:

1. run the application;
2. inspect the actual rendered interface;
3. capture representative viewports;
4. check desktop;
5. check mobile;
6. check intermediate width;
7. interact with important states;
8. inspect overflow;
9. inspect focus;
10. inspect modal/dropdown layering;
11. inspect loading/error/empty states.

Do not consider implementation complete merely because code compiles.

If existing browser automation is available, use it.

Do not add a large browser-testing dependency without checking whether the project already has suitable tooling.

---

## 15. ACCESSIBILITY VALIDATION

Use current authoritative accessibility guidance.

At minimum evaluate:

- text contrast;
- non-text contrast where relevant;
- keyboard operation;
- focus visibility;
- focus order;
- semantic structure;
- labels;
- error association;
- target sizing;
- zoom;
- reflow;
- reduced motion;
- state communication;
- transparency-related readability.

Automated tools are useful but not sufficient.

Never claim complete accessibility compliance solely because an automated scan passes.

---

## 16. EVALUATION FRAMEWORK

Do not stop after writing the skills.

Create an evaluation system.

For each skill, produce test cases across:

1. greenfield creation;
2. existing UI redesign;
3. component-level work;
4. style review;
5. style correction;
6. mobile adaptation;
7. accessibility conflict;
8. ambiguous prompt;
9. negative trigger case;
10. alias/misspelling trigger case where relevant.

Examples:

- “Create a tactile music player inspired by physical equipment.”
- “Make this settings page neumorphic.”
- “Review whether this page actually qualifies as glassmorphism.”
- “Create a minimal admin panel without making it visually generic.”
- “Make this campaign intentionally maximalist while preserving hierarchy.”
- “Convert this dashboard to brutalism.”
- “Use Liquid Glass principles for the navigation, not every content surface.”
- “Reorganize these priorities into a meaningful bento structure.”
- “Design this interface for a true spatial computing environment.”

Create negative tests such as:

- backend-only request must not trigger a design skill;
- database migration must not trigger a design skill;
- “glass table” in a non-UI context must not trigger glassmorphism;
- “minimal API” must not trigger minimalism;
- “brutal error” must not trigger brutalism.

---

## 17. BASELINE COMPARISON

Where practical, compare:

A. agent output without the specialized skill;

against:

B. agent output with the specialized skill.

Use a consistent rubric.

Where the local tooling supports it, perform blind comparison.

Evaluate whether the skill causes a meaningful improvement rather than merely producing longer output.

---

## 18. DESIGN QUALITY RUBRIC

Create a scored rubric covering:

- task fit;
- style fidelity;
- distinctiveness;
- subject specificity;
- hierarchy;
- typography;
- color;
- composition;
- spacing;
- interaction;
- accessibility;
- responsiveness;
- motion;
- performance;
- maintainability;
- anti-pattern avoidance.

Do not let a visually dramatic design score highly when it is unusable.

Do not let a technically accessible but visually generic design automatically score highly for design quality.

---

## 19. TRIGGER QUALITY

Descriptions are critical.

For every skill:

- state what it does;
- state when to use it;
- include relevant user vocabulary;
- include meaningful aliases;
- avoid descriptions so broad that every frontend task triggers every style skill.

Test:

- true positives;
- false positives;
- ambiguous cases.

Optimize triggering based on evidence.

---

## 20. OPTIONAL DETERMINISTIC DESIGN AUDITOR

Investigate whether a deterministic audit script would materially improve the suite.

Possible checks:

- excessive border-radius repetition;
- excessive nested card structures;
- hardcoded colors bypassing tokens;
- missing focus styles;
- excessive backdrop filters;
- excessive blur;
- excessive shadow count;
- missing reduced-motion handling;
- suspiciously tiny targets;
- generic repeated UI motifs.

Only implement checks that can be detected with reasonable reliability.

Every rule must document:

- what is detected;
- why;
- false-positive risks;
- severity;
- remediation.

Do not pretend subjective taste can be perfectly linted.

---

## 21. DOCUMENTATION

Create:

### Root README

Explain:

- purpose;
- architecture;
- skill list;
- compatibility;
- installation;
- usage;
- examples;
- evaluation;
- limitations.

### Skill catalog

For each skill:

- name;
- purpose;
- trigger examples;
- non-trigger examples;
- dependencies;
- references;
- status.

### Architecture document

Explain why the system uses multiple skills rather than one giant skill.

### Research document

Record the public skill ecosystem researched and what was learned.

### Evaluation report

Record:

- tasks;
- baseline;
- skill-assisted result;
- scores;
- failures;
- changes made.

---

## 22. INSTALLATION AND DISTRIBUTION

Prepare the repository so it can be published and installed conveniently.

Where compatible with the repository and current ecosystem, prepare for installation through a standard skills installer pattern such as:

```bash
npx skills add OWNER/REPO
```

Do not invent an owner or repository URL.

Document placeholders where publication information is unknown.

Also assess whether a Claude Code plugin marketplace wrapper would add value.

Keep the core skills portable.

Do not make the suite Claude-only unless a capability genuinely requires Claude-specific integration.

Do not make the suite Codex-only unless a capability genuinely requires Codex-specific integration.

---

## 23. OPTIONAL HARNESS ADAPTERS

After the portable core is complete, inspect whether useful adapters should be created for:

- Claude Code
- Codex CLI

Examples:

- commands;
- hooks;
- dedicated reviewer agents;
- subagents;
- audit commands.

Only create them when they genuinely improve workflow.

Keep portable knowledge in the skills themselves rather than duplicating it into every adapter.

---

## 24. QUALITY STANDARD

The finished suite must not be a collection of generic style definitions.

A weak result would say:

- “use blur for glassmorphism”
- “use shadows for neumorphism”
- “use whitespace for minimalism”
- “use bright colors for maximalism”

That is unacceptable.

The skills must teach operational design judgment.

They must help an agent answer questions such as:

- Is this style appropriate here?
- Which surfaces receive the style?
- Which surfaces should remain neutral?
- What creates hierarchy?
- How should the style respond on mobile?
- How does pressed state work?
- What breaks accessibility?
- What makes this implementation fake or superficial?
- What are the characteristic AI failure modes?
- How should the implementation change for a dashboard versus landing page?
- What should be preserved from the existing product?
- How can the style remain distinctive without becoming unusable?

---

## 25. EXECUTION REQUIREMENT

Do the work directly.

Do not only provide a plan.

Do not stop after research.

Do not stop after generating folders.

Do not ask for confirmation between phases unless an irreversible external action genuinely requires it.

Proceed through:

1. repository inspection;
2. research;
3. architecture;
4. implementation;
5. specialized skill creation;
6. references;
7. evaluation cases;
8. validation;
9. refinement;
10. documentation;
11. final report.

Use best judgment when details are missing.

---

## 26. FINAL RESPONSE FORMAT

At completion, report:

### A. Research performed

Summarize the important existing design skills and primary references studied.

### B. Architecture created

Show the complete directory tree.

### C. Skills created

For each:

- name;
- purpose;
- trigger behavior.

### D. Key design decisions

Explain major architectural decisions.

### E. Evaluation performed

Show:

- tests;
- results;
- failures;
- improvements.

### F. Files changed

List all created and modified files.

### G. Installation

Provide exact commands that are actually valid for the resulting repository.

Do not invent publication commands that cannot yet work.

### H. Limitations

State honestly what could not be validated.

### I. Recommended next improvements

Prioritize only meaningful improvements.

---

## BEGIN

Begin now by inspecting the repository, its memory/instruction files, existing skills, existing agent configuration, and current frontend architecture.

Then perform research and build the complete suite.
