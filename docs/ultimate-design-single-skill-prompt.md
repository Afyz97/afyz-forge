# Master Prompt — Create One Complete Ultimate Design Skill

You are tasked with researching, architecting, implementing, evaluating, and documenting **one complete, production-grade Agent Skill** that can handle the full spectrum of modern digital interface design.

The final result must be a **single installable skill package**, not a collection of separate specialist skills.

The skill must be capable of understanding, selecting, combining, implementing, auditing, and improving interfaces across the following design languages:

- Skeuomorphism
- Neumorphism
- Glassmorphism
- Claymorphism
- Minimalism
- Maximalism
- Brutalism
- Neo-Brutalism where relevant
- Liquid Glass
- Bento Grid
- Spatial UI Design

It must also provide strong cross-style capabilities for:

- visual hierarchy;
- typography;
- color;
- composition;
- spacing;
- layout;
- responsive design;
- accessibility;
- interaction design;
- motion design;
- design systems;
- design tokens;
- component design;
- product UI;
- brand UI;
- dashboards;
- SaaS;
- e-commerce;
- public websites;
- mobile interfaces;
- data-heavy interfaces;
- design critique;
- design QA;
- anti-pattern detection;
- AI-generated UI cleanup;
- frontend implementation;
- browser-based validation;
- iterative refinement.

The target is not a generic “frontend design” prompt.

The target is one highly capable **design intelligence skill** that behaves like a combined:

- design director;
- UI/UX designer;
- design systems engineer;
- interaction designer;
- motion designer;
- accessibility-aware reviewer;
- frontend design engineer;
- visual QA reviewer.

The skill must remain practical for real coding agents such as:

- Claude Code
- Codex CLI
- Agent Skills-compatible tools

---

# 1. PRIMARY GOAL

Create exactly one skill named:

```text
ultimate-design
```

The skill must be able to:

1. inspect an existing project;
2. understand the product and user context;
3. infer the correct design strategy;
4. detect when the user explicitly requests a style;
5. distinguish similar styles correctly;
6. select one dominant design language;
7. combine supporting styles only when justified;
8. preserve useful existing design decisions;
9. redesign weak interfaces;
10. create new interfaces from scratch;
11. translate design intent into production-quality code;
12. adapt to the project’s actual stack;
13. maintain responsiveness;
14. maintain accessibility;
15. maintain performance;
16. maintain implementation quality;
17. evaluate visual output after implementation;
18. detect generic AI-generated UI patterns;
19. refine weak results;
20. explain important design decisions when useful;
21. know when not to apply a fashionable style;
22. avoid making every interface look the same.

The skill must behave as a single expert system with internal style routing.

Do not create one `SKILL.md` per style.

Do not create separate independent skills.

Create one coherent skill package with modular internal references.

---

# 2. INSPECT THE LOCAL ENVIRONMENT FIRST

Before creating the skill:

1. inspect the repository;
2. inspect all existing agent instructions;
3. inspect memory files;
4. inspect current skill conventions;
5. inspect existing `SKILL.md` files;
6. inspect Claude Code configuration;
7. inspect Codex configuration;
8. inspect project documentation;
9. inspect package manifests;
10. inspect current frontend stack;
11. inspect design systems;
12. inspect component libraries;
13. inspect testing infrastructure;
14. inspect browser automation tooling;
15. inspect accessibility tooling.

Pay particular attention to:

```text
.ai/
.ai/agents/
.claude/
.codex/
.agents/
skills/
docs/
CLAUDE.md
AGENTS.md
README.md
```

Do not overwrite existing conventions blindly.

If the repository already contains:

- a skill creator;
- a skill template;
- an evaluation framework;
- browser testing;
- screenshot tooling;
- design linting;
- accessibility testing;

reuse those systems where appropriate.

---

# 3. RESEARCH BEFORE IMPLEMENTATION

When network access is available, perform current research before writing the final skill.

Study the public architecture, documented behavior, strengths, limitations, and evaluation approach of relevant design-oriented AI skills and primary design references.

At minimum investigate:

- Anthropic `frontend-design`
- Anthropic `skill-creator`
- Anthropic public Agent Skills guidance
- Vercel `web-design-guidelines`
- Vercel frontend or React best-practice skills where relevant
- Impeccable
- Emil Kowalski design engineering / motion guidance
- UI/UX Pro Max
- other currently prominent design skills discovered during research

Also inspect authoritative primary sources where relevant:

- W3C WCAG
- platform Human Interface Guidelines
- Apple Liquid Glass guidance
- Apple spatial computing / visionOS design guidance
- browser platform documentation
- framework documentation
- accessibility platform documentation

Evaluate sources rather than assuming named examples are automatically best.

Record:

- source;
- purpose;
- current relevance;
- verifiable popularity signal where available;
- strongest ideas;
- structural patterns;
- trigger patterns;
- evaluation patterns;
- limitations;
- ideas worth adapting.

Do not copy proprietary wording.

Do not clone another skill.

Do not reproduce copyrighted rule databases.

Synthesize original operational guidance.

Respect licenses and attribution requirements.

If network access is unavailable:

- continue;
- use local information;
- document the limitation;
- do not stop the task.

---

# 4. REQUIRED SINGLE-SKILL ARCHITECTURE

Create one skill package structured approximately like:

```text
ultimate-design/
├── SKILL.md
├── references/
│   ├── design-foundations.md
│   ├── style-router.md
│   ├── skeuomorphism.md
│   ├── neumorphism.md
│   ├── glassmorphism.md
│   ├── claymorphism.md
│   ├── minimalism.md
│   ├── maximalism.md
│   ├── brutalism.md
│   ├── liquid-glass.md
│   ├── bento-grid.md
│   ├── spatial-ui.md
│   ├── typography.md
│   ├── color.md
│   ├── layout-composition.md
│   ├── motion.md
│   ├── responsive.md
│   ├── accessibility.md
│   ├── design-systems.md
│   ├── implementation.md
│   ├── anti-ai-slop.md
│   ├── design-review.md
│   ├── style-composition.md
│   ├── product-vs-brand.md
│   └── evaluation.md
├── examples/
│   ├── style-selection.md
│   ├── redesign.md
│   ├── greenfield.md
│   ├── review.md
│   └── hybrid-styles.md
├── scripts/
│   └── ... only when justified
└── assets/
    └── ... only when justified
```

This structure is a target, not a rigid requirement.

Do not create empty files.

Do not create empty directories.

Every reference must serve a real purpose.

The package must remain one skill:

```text
ultimate-design
```

---

# 5. PROGRESSIVE DISCLOSURE

The main `SKILL.md` must be concise, operational, and trigger-focused.

It must not contain every design rule.

It must:

- define the skill;
- define when to use it;
- define the internal workflow;
- define the style-routing logic;
- define mandatory quality gates;
- point to relevant references;
- prevent unnecessary loading of all references.

The skill should load only the relevant knowledge for the current task.

Examples:

- a brutalist landing page should not require deep neumorphism guidance;
- a Laravel admin redesign should not require full spatial UI guidance;
- a Liquid Glass navigation task should load Liquid Glass, accessibility, motion, and implementation guidance;
- a generic redesign request should load foundations, style router, product-vs-brand, anti-AI-slop, and review guidance.

Use progressive disclosure deliberately.

---

# 6. SKILL TRIGGERING

The skill description must make the skill activate for requests involving:

- UI design;
- UX design;
- frontend visual design;
- redesign;
- styling;
- layout;
- responsive interface work;
- landing pages;
- dashboards;
- admin panels;
- SaaS;
- e-commerce;
- mobile UI;
- component design;
- visual polish;
- design systems;
- design tokens;
- accessibility-aware design;
- motion design;
- interaction design;
- design review;
- screenshot-based UI critique;
- AI-generated interface cleanup;
- style transformation.

Include style aliases and common misspellings such as:

- skeuomorphism
- skeomorphism
- skeuomorphic
- neumorphism
- neomorphism
- soft UI
- glassmorphism
- glass UI
- claymorphism
- clay UI
- minimalism
- minimalist
- maximalism
- maximalist
- brutalism
- brutalist
- neo-brutalism
- liquid glass
- Apple-style glass
- bento
- bento grid
- spatial UI
- spatial computing UI
- immersive UI
- 3D interface

Avoid false triggering.

The skill must not activate merely because a non-design request contains words like:

- “minimal API”
- “glass table”
- “brutal error”
- “spatial database”
- “clay model” in a non-interface context

Create trigger tests.

---

# 7. INTERNAL DESIGN ROUTER

The skill must contain an internal style-selection engine.

Before designing, infer or establish:

- product type;
- audience;
- user goals;
- primary task;
- platform;
- content type;
- information density;
- brand personality;
- emotional target;
- accessibility needs;
- performance constraints;
- current design system;
- existing UI quality;
- requested style;
- implementation stack;
- device context;
- interaction context.

The router must produce an internal decision such as:

```text
Dominant design language:
Supporting design language:
Product mode or brand mode:
Density:
Visual intensity:
Motion level:
Primary risks:
Relevant references to load:
```

Do not expose excessive internal reasoning to the user unless useful.

---

# 8. STYLE SELECTION RULES

When the user explicitly requests a style:

1. honor the request;
2. inspect whether the style is appropriate;
3. adapt the style to the product;
4. preserve usability;
5. preserve accessibility;
6. preserve performance;
7. do not silently replace it with a generic modern design.

When no style is requested:

1. choose intentionally;
2. select a dominant design language only when useful;
3. allow a neutral design-system-led approach;
4. do not default to glassmorphism;
5. do not default to dark mode;
6. do not default to bento grids;
7. do not default to purple gradients;
8. do not default to excessive rounded cards;
9. do not force stylistic novelty onto utility software.

The skill must know when the best choice is:

- restrained;
- conventional;
- system-native;
- content-led;
- product-led;
- editorial;
- expressive.

---

# 9. REQUIRED DESIGN FOUNDATIONS

The skill must have strong cross-style design judgment.

Cover:

## Visual hierarchy

- primary versus secondary actions;
- emphasis;
- scanning;
- reading order;
- grouping;
- salience;
- visual weight;
- hierarchy consistency.

## Typography

- font role selection;
- display versus body;
- readability;
- line length;
- line height;
- weight hierarchy;
- optical sizing;
- variable fonts where appropriate;
- fallback stacks;
- multilingual requirements;
- numeric alignment;
- dense UI typography.

Reject:

- choosing fonts only because they are trendy;
- using one default font for every brand;
- oversized headings without purpose;
- weak body contrast;
- random weight jumps.

## Color

- semantic color roles;
- brand color;
- surface color;
- state color;
- contrast;
- hierarchy;
- light/dark adaptation;
- data visualization;
- color-blind considerations;
- avoiding color-only communication.

## Spacing

- rhythm;
- grouping;
- density;
- scale;
- optical correction;
- responsive spacing;
- consistent token use.

## Layout

- grids;
- alignment;
- flow;
- balance;
- asymmetry;
- reading path;
- responsive transformation;
- content priority.

## Composition

- focal points;
- rhythm;
- tension;
- contrast;
- repetition;
- negative space;
- controlled density.

## Iconography

- consistent family;
- size;
- stroke;
- fill;
- alignment;
- semantic meaning;
- avoiding decorative icon spam.

## Imagery

- subject relevance;
- cropping;
- art direction;
- hierarchy;
- consistency;
- performance.

---

# 10. SKEUOMORPHISM EXPERTISE

The skill must understand:

- physical-world metaphor;
- recognizable affordances;
- tactile controls;
- material cues;
- realistic and semi-realistic depth;
- texture restraint;
- visual familiarity;
- functional metaphor;
- modern skeuomorphic adaptation.

Distinguish:

- meaningful physical affordance

from:

- decorative fake realism.

Know risks:

- excessive ornament;
- outdated metaphors;
- visual noise;
- inaccessible text over texture;
- inconsistent lighting;
- inconsistent physical logic;
- slow rendering.

For implementation, understand:

- layered shadows;
- highlights;
- gradients;
- texture restraint;
- tactile states;
- pressed states;
- realistic interaction feedback.

---

# 11. NEUMORPHISM EXPERTISE

The skill must understand:

- same-surface extrusion;
- embossed states;
- debossed states;
- paired light and shadow;
- soft UI;
- consistent light source;
- surface continuity.

Aggressively prevent:

- invisible controls;
- low contrast;
- ambiguous pressed states;
- everything looking disabled;
- same treatment on every component;
- unreadable forms;
- poor focus indication.

Accessibility must override style purity.

The skill must know when neumorphism should only be used as an accent rather than a full application language.

---

# 12. GLASSMORPHISM EXPERTISE

The skill must understand:

- translucent surfaces;
- background dependency;
- blur;
- layering;
- edge definition;
- tint;
- saturation;
- depth;
- contrast management;
- hierarchy through material.

Distinguish glassmorphism from:

- plain transparency;
- generic frosted cards;
- Liquid Glass;
- opacity-only styling.

Prevent:

- glass everywhere;
- unreadable text;
- blur on every surface;
- excessive compositing;
- arbitrary translucent cards;
- weak hierarchy.

Provide fallback strategies when:

- `backdrop-filter` is unavailable;
- transparency is inappropriate;
- contrast is insufficient;
- performance is weak.

---

# 13. CLAYMORPHISM EXPERTISE

The skill must understand:

- inflated geometry;
- soft dimensional mass;
- chunky forms;
- playful surfaces;
- friendly visual tone;
- controlled inner/outer depth;
- soft 3D illustration.

Prevent:

- every component becoming a toy;
- childish treatment in inappropriate domains;
- excessive shadow stacks;
- low information density;
- unusable forms.

Know appropriate use cases such as:

- playful brands;
- education;
- children-oriented products where suitable;
- illustration-led products;
- friendly onboarding.

Do not assume claymorphism is appropriate for every SaaS interface.

---

# 14. MINIMALISM EXPERTISE

The skill must understand:

- reduction;
- hierarchy;
- restraint;
- purposeful negative space;
- essential content;
- typographic precision;
- progressive disclosure;
- calm interaction.

Reject false minimalism:

- empty pages;
- monochrome by default;
- giant whitespace without purpose;
- hidden functionality;
- weak hierarchy;
- generic template aesthetics;
- defaulting to the same font and layout.

Minimalism must still have identity.

For product UI, preserve:

- task clarity;
- density where necessary;
- state visibility;
- discoverability.

---

# 15. MAXIMALISM EXPERTISE

The skill must understand:

- controlled abundance;
- deliberate layering;
- expressive typography;
- pattern;
- image density;
- color interaction;
- asymmetry;
- visual rhythm;
- editorial composition.

Distinguish maximalism from random clutter.

Require hierarchy.

Prevent:

- uncontrolled noise;
- unreadable type;
- competing focal points;
- animation overload;
- inconsistent visual grammar.

Know when maximalism is more suitable for:

- campaigns;
- cultural events;
- editorial work;
- fashion;
- music;
- creative portfolios;
- brand expression.

Adapt carefully for product UI.

---

# 16. BRUTALISM EXPERTISE

The skill must understand:

- rawness;
- directness;
- exposed structure;
- hard contrast;
- unconventional grids;
- typographic force;
- utilitarian expression;
- anti-polish where intentional.

Distinguish:

- intentional brutalism

from:

- unfinished frontend code;
- broken layout;
- careless spacing;
- inaccessible contrast;
- missing responsive behavior.

Also understand neo-brutalism when relevant.

Do not collapse brutalism and neo-brutalism into one concept.

---

# 17. LIQUID GLASS EXPERTISE

This section requires especially careful current research.

The skill must distinguish:

1. authentic platform-native Liquid Glass;
2. Liquid Glass-inspired web implementation;
3. conventional glassmorphism.

Understand:

- dynamic material;
- content versus controls;
- adaptive appearance;
- optical depth;
- material response;
- layered navigation;
- translucency;
- highlights;
- shape transformation where supported;
- movement;
- hierarchy.

Do not:

- create an Apple clone by default;
- claim CSS approximations are identical to native platform materials;
- place translucent rounded glass on every surface;
- sacrifice readability for visual effect.

For web implementations:

- define glass hierarchy;
- limit blur regions;
- provide fallbacks;
- preserve contrast;
- preserve content hierarchy;
- manage performance.

---

# 18. BENTO GRID EXPERTISE

The skill must understand Bento Grid as an information-composition system.

Not merely:

```css
display: grid;
```

Cover:

- modular grouping;
- hierarchy;
- variable spans;
- content priority;
- scan paths;
- rhythm;
- density;
- responsive regrouping;
- feature emphasis.

Prevent:

- every tile being equal;
- decorative bento with no information logic;
- dashboardification of ordinary pages;
- excessive card borders;
- repetitive modular boxes.

The router must determine whether content genuinely benefits from bento organization.

---

# 19. SPATIAL UI EXPERTISE

This section requires especially careful current research.

Distinguish:

1. 2D interfaces with depth cues;
2. pseudo-spatial web interfaces;
3. true spatial computing;
4. AR;
5. VR;
6. mixed reality.

Understand:

- depth;
- distance;
- scale;
- field of view;
- anchoring;
- windows;
- volumes;
- immersive spaces;
- occlusion;
- comfort;
- discoverability;
- gaze;
- hand interaction;
- pointer interaction;
- voice interaction;
- focus;
- selection feedback;
- spatial audio where appropriate;
- motion comfort;
- environment awareness.

Do not apply true spatial computing assumptions to ordinary websites.

For web projects, use a web-appropriate spatial interpretation unless genuine XR capabilities are requested.

---

# 20. PRODUCT MODE VERSUS BRAND MODE

The skill must explicitly distinguish:

## Product mode

Examples:

- admin systems;
- SaaS;
- dashboards;
- internal tools;
- e-commerce workflows;
- enterprise applications;
- data-heavy software.

Priorities:

- task completion;
- repetition;
- clarity;
- state recognition;
- density;
- accessibility;
- consistency.

## Brand mode

Examples:

- landing pages;
- campaigns;
- portfolios;
- event websites;
- editorial experiences;
- storytelling pages.

Priorities may include:

- expression;
- memorability;
- dramatic composition;
- stronger motion;
- visual experimentation.

Never apply brand-page aesthetics blindly to operational software.

Never reduce brand experiences to generic dashboard cards.

---

# 21. STYLE COMPOSITION ENGINE

The skill may combine styles only when justified.

For every hybrid design:

1. choose one dominant language;
2. choose at most one or two supporting influences;
3. define which properties belong to each;
4. preserve hierarchy;
5. preserve usability;
6. prevent contradiction.

Examples of potentially meaningful combinations:

- minimalism + bento grid;
- glassmorphism + restrained spatial depth;
- claymorphism + playful maximalist accents;
- brutalist structure + minimal interaction;
- skeuomorphic affordances + modern product UI.

These examples are not automatic recommendations.

Create a compatibility matrix.

Include:

- compatible combinations;
- risky combinations;
- usually conflicting combinations;
- conditions under which combinations can work.

Do not create “design soup.”

---

# 22. DESIGN SYSTEM ENGINEERING

The skill must translate visual direction into maintainable implementation.

Cover:

- primitive tokens;
- semantic tokens;
- component tokens;
- color tokens;
- typography tokens;
- spacing scales;
- radius systems;
- elevation systems;
- transparency systems;
- motion tokens;
- responsive tokens;
- state tokens;
- theme tokens;
- dark/light modes;
- high-contrast considerations.

Require:

- reusable primitives;
- component variants;
- semantic naming;
- consistent state handling;
- maintainable APIs.

Avoid:

- one-off CSS;
- random hardcoded colors;
- arbitrary values everywhere;
- unexplained magic numbers;
- duplicated component logic.

---

# 23. MOTION DESIGN

The skill must include strong motion judgment.

Cover:

- motion purpose;
- continuity;
- entering;
- exiting;
- state change;
- layout transition;
- transform;
- opacity;
- easing;
- duration;
- interruption;
- gesture response;
- modal motion;
- drawer motion;
- toast behavior;
- hover restraint;
- reduced motion;
- performance.

Motion must reinforce:

- cause and effect;
- spatial relationship;
- state change;
- hierarchy;
- continuity.

Reject:

- every element animating;
- long cinematic transitions in productivity software;
- excessive hover movement;
- random bouncing;
- motion without meaning;
- animation that blocks interaction.

Know when no animation is better.

---

# 24. RESPONSIVE DESIGN

The skill must not treat responsiveness as “shrink desktop.”

It must reason about:

- content priority;
- reordering;
- grouping;
- navigation changes;
- touch;
- pointer;
- keyboard;
- density;
- viewport height;
- orientation;
- container behavior.

Cover:

- mobile;
- tablet;
- desktop;
- ultrawide.

For each design style, define how the language transforms.

Examples:

- Bento cards may regroup.
- Glass layers may simplify.
- Maximalism may reduce simultaneous focal points.
- Spatial depth may flatten.
- Neumorphic surfaces may become more explicit.
- Dense product UI may shift interaction patterns.

---

# 25. ACCESSIBILITY

The skill must treat accessibility as a design requirement.

Use current authoritative guidance.

At minimum evaluate:

- text contrast;
- non-text contrast;
- keyboard operation;
- focus visibility;
- focus order;
- semantic structure;
- labels;
- target size;
- zoom;
- reflow;
- reduced motion;
- error communication;
- state communication;
- transparency readability;
- color-only communication.

Style-specific accessibility checks must exist.

Examples:

- neumorphism: state ambiguity;
- glassmorphism: contrast and blur;
- maximalism: cognitive overload;
- minimalism: hidden affordances;
- brutalism: readability;
- Liquid Glass: material contrast;
- spatial UI: comfort and discoverability.

Do not claim complete compliance from automated testing alone.

---

# 26. IMPLEMENTATION INTELLIGENCE

The skill must support the project’s actual stack first.

Potential stacks include:

- HTML
- CSS
- JavaScript
- TypeScript
- Tailwind CSS
- React
- Next.js
- Vue
- Nuxt
- Svelte
- Laravel Blade
- Livewire
- Alpine.js
- shadcn/ui
- SwiftUI
- React Native
- Flutter

The skill must:

- inspect the repository;
- detect the stack;
- use existing architecture;
- use existing components;
- use existing libraries;
- preserve conventions;
- avoid unnecessary dependencies.

Do not replace the project framework without authorization.

Do not pretend stack-specific expertise exists unless meaningful guidance is included.

---

# 27. EXISTING PROJECT SAFETY

When modifying an existing application:

- preserve functionality;
- preserve authorization;
- preserve validation;
- preserve localization;
- preserve RTL support where relevant;
- preserve error states;
- preserve loading states;
- preserve empty states;
- preserve forms;
- preserve workflows;
- preserve responsive behavior.

Do not:

- remove functionality because it complicates design;
- rewrite the whole frontend unnecessarily;
- replace the component system casually;
- introduce large dependencies without justification.

Audit first.

---

# 28. ANTI-AI-SLOP SYSTEM

Create an original anti-pattern framework.

Detect patterns such as:

- gratuitous purple-blue gradients;
- excessive gradient text;
- excessive rounded cards;
- cards inside cards;
- excessive glass;
- random glow;
- default dark SaaS style;
- generic hero layouts;
- fake metrics;
- fake testimonials;
- meaningless dashboards;
- meaningless charts;
- excessive pill badges;
- icon-in-colored-square repetition;
- arbitrary blobs;
- decorative 01/02/03 numbering;
- identical section rhythm;
- excessive centered layouts;
- giant generic headings;
- repetitive feature grids;
- excessive hover movement;
- every element animating;
- unnecessary 3D transforms;
- collapsed desktop mobile layouts;
- excessive empty space;
- fashionable style regardless of context.

Do not ban patterns automatically.

A pattern can be valid when:

- semantically appropriate;
- deliberate;
- contextually justified;
- well executed.

For every detected anti-pattern, define:

- clue;
- severity;
- why it is weak;
- false-positive risk;
- corrective action.

---

# 29. DESIGN WORKFLOW

The skill must follow a deliberate process.

## Phase 1 — Understand

Determine:

- product;
- audience;
- user goal;
- task;
- content;
- constraints;
- stack.

## Phase 2 — Inspect

For existing projects:

- inspect current UI;
- inspect implementation;
- identify strengths;
- identify weaknesses;
- identify design debt;
- identify constraints.

## Phase 3 — Route

Choose:

- dominant design language;
- supporting language;
- product or brand mode;
- density;
- visual intensity;
- motion level;
- relevant references.

## Phase 4 — Direction

Define:

- concept;
- mood;
- typography;
- color logic;
- layout logic;
- interaction logic;
- one justified distinctive move.

## Phase 5 — System

Define:

- tokens;
- spacing;
- type scale;
- surfaces;
- radius;
- borders;
- elevation;
- transparency;
- motion.

## Phase 6 — Implement

Use:

- semantic markup;
- existing architecture;
- maintainable components;
- real content;
- real states.

## Phase 7 — Validate

Check:

- functionality;
- responsiveness;
- accessibility;
- style fidelity;
- performance;
- interaction.

## Phase 8 — Review

Perform independent design review.

## Phase 9 — Refine

Fix issues by severity.

---

# 30. DESIGN REVIEW MODE

The same skill must be able to act as a strict reviewer.

Review:

- style fidelity;
- hierarchy;
- typography;
- color;
- spacing;
- density;
- composition;
- responsiveness;
- interaction;
- motion;
- accessibility;
- performance;
- maintainability;
- AI-generated clichés.

Output findings with:

1. finding;
2. severity;
3. evidence;
4. why it matters;
5. exact corrective action;
6. whether correction changes the intended style.

Where possible distinguish:

- objective defect;
- likely defect;
- subjective preference.

The skill must be able to review its own implementation critically.

---

# 31. VISUAL VALIDATION

When browser or screenshot tools are available:

1. run the application;
2. inspect the rendered interface;
3. capture representative screenshots;
4. test desktop;
5. test mobile;
6. test intermediate widths;
7. interact with important states;
8. inspect overflow;
9. inspect focus;
10. inspect modals;
11. inspect dropdowns;
12. inspect loading;
13. inspect errors;
14. inspect empty states.

Do not declare completion merely because code compiles.

If screenshot comparison is available, use it.

---

# 32. OPTIONAL DETERMINISTIC AUDITOR

Investigate whether a small audit script would improve quality.

Possible checks:

- excessive repeated border radius;
- nested card structures;
- hardcoded colors bypassing tokens;
- missing focus states;
- excessive backdrop filters;
- excessive blur;
- excessive shadows;
- missing reduced-motion handling;
- tiny targets;
- repeated generic UI motifs.

Only implement rules that can be detected with reasonable reliability.

Document:

- detection logic;
- false-positive risk;
- severity;
- remediation.

Do not pretend subjective design taste can be fully linted.

---

# 33. EVALUATION FRAMEWORK

Do not stop after writing the skill.

Create evaluations.

Test the skill on:

1. greenfield creation;
2. existing UI redesign;
3. component-level design;
4. style transformation;
5. style review;
6. mobile adaptation;
7. accessibility conflict;
8. ambiguous prompt;
9. negative trigger;
10. hybrid-style request;
11. data-heavy product UI;
12. expressive brand UI.

Include examples such as:

- “Create a tactile music player inspired by physical equipment.”
- “Make this settings page neumorphic.”
- “Review whether this page genuinely qualifies as glassmorphism.”
- “Create a minimal admin panel without making it visually generic.”
- “Make this campaign intentionally maximalist while preserving hierarchy.”
- “Convert this dashboard to brutalism.”
- “Use Liquid Glass principles for navigation, not every content surface.”
- “Reorganize these priorities into a meaningful bento layout.”
- “Design this for a true spatial computing environment.”
- “Improve this generic AI-generated SaaS page.”

Create negative tests:

- backend-only task must not trigger;
- database migration must not trigger;
- “minimal API” must not trigger minimalism;
- “glass table” in a database context must not trigger glassmorphism;
- “spatial database” must not trigger spatial UI.

---

# 34. BASELINE COMPARISON

Where practical compare:

A. agent behavior without the skill;

against:

B. agent behavior with the skill.

Use a consistent rubric.

Evaluate whether the skill improves:

- design quality;
- style fidelity;
- implementation quality;
- reasoning quality;
- responsiveness;
- accessibility;
- anti-pattern avoidance.

Do not reward longer outputs merely for being longer.

---

# 35. QUALITY RUBRIC

Create a scored design-quality rubric covering:

- task fit;
- subject specificity;
- style fidelity;
- distinctiveness;
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

A dramatic but unusable design must not score highly.

A technically valid but generic design must not automatically score highly.

---

# 36. EXAMPLES

Create examples demonstrating:

- explicit style request;
- implicit style selection;
- brand mode;
- product mode;
- redesign;
- greenfield design;
- review;
- style correction;
- hybrid style;
- accessibility override;
- mobile transformation.

Examples must demonstrate principles.

Do not copy commercial interfaces.

---

# 37. DOCUMENTATION

Create:

## `README.md`

Explain:

- purpose;
- capabilities;
- supported styles;
- installation;
- usage;
- compatibility;
- evaluation;
- limitations.

## Skill architecture document

Explain:

- why one skill was chosen;
- progressive disclosure;
- internal routing;
- reference loading.

## Research document

Record:

- projects researched;
- strengths;
- limitations;
- concepts adapted.

## Evaluation report

Record:

- tests;
- baseline;
- skill-assisted output;
- failures;
- improvements.

---

# 38. DISTRIBUTION

Prepare the skill for convenient installation.

Where compatible, support a standard pattern such as:

```bash
npx skills add OWNER/REPO
```

Do not invent an owner or repository URL.

Use placeholders where publication information is unknown.

Keep the core skill portable.

Optional adapters for Claude Code or Codex may be created only when useful.

Do not turn the core skill into a Claude-only implementation.

Do not turn the core skill into a Codex-only implementation.

---

# 39. QUALITY BAR

A weak result would say:

- “Use blur for glassmorphism.”
- “Use shadows for neumorphism.”
- “Use whitespace for minimalism.”
- “Use bright colors for maximalism.”
- “Use boxes for bento.”
- “Use transparency for Liquid Glass.”

That is unacceptable.

The final skill must teach operational design judgment.

It must answer questions such as:

- Is this style appropriate here?
- Which surfaces should use it?
- Which surfaces should remain neutral?
- What creates hierarchy?
- How does it adapt to mobile?
- How do interaction states work?
- What creates accessibility risk?
- What makes the implementation superficial?
- What are the likely AI-generated failure modes?
- How should the same style differ between a dashboard and landing page?
- What should be preserved from the current product?
- How can a design remain distinctive without becoming unusable?

---

# 40. EXECUTION REQUIREMENT

Do the work directly.

Do not only provide a plan.

Do not stop after research.

Do not stop after creating folders.

Do not stop after writing `SKILL.md`.

Proceed through:

1. repository inspection;
2. current research;
3. architecture;
4. skill implementation;
5. reference creation;
6. examples;
7. evaluations;
8. trigger tests;
9. validation;
10. refinement;
11. documentation;
12. final report.

Do not ask for confirmation between phases unless an irreversible external action genuinely requires it.

Use best judgment when details are missing.

---

# 41. FINAL RESPONSE FORMAT

At completion report:

## A. Research performed

Summarize the important skills and primary references studied.

## B. Architecture created

Show the complete directory tree.

## C. Main skill behavior

Explain:

- triggering;
- routing;
- progressive disclosure;
- review mode;
- implementation mode.

## D. Style coverage

Explain how each design family is handled.

## E. Evaluation performed

Show:

- tests;
- results;
- failures;
- improvements.

## F. Files changed

List all created and modified files.

## G. Installation

Provide exact commands that are actually valid.

Do not invent commands that cannot work.

## H. Limitations

State honestly what could not be validated.

## I. Recommended improvements

List only meaningful next steps.

---

# BEGIN NOW

Begin by inspecting the repository, memory/instruction files, current skill architecture, frontend stack, design systems, and existing agent configuration.

Then research current high-quality design skills and authoritative design guidance.

Then create the complete single `ultimate-design` skill with progressive disclosure, internal style routing, implementation intelligence, design review, anti-AI-slop detection, visual validation, and evaluation.
