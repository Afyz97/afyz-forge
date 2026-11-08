# Regression Prompts

Checks against known failure modes. Each is a behavior the skill must **not** regress on. Run after any
edit to the skill; the "Pass =" line is the acceptance condition.

## Slop regressions
- **Rounded-card-everything** — *"Build a features section."* Pass = not every block is a floating
  `rounded-2xl shadow-lg` card; hierarchy through space/type; elevation reserved.
- **Default gradients** — *"Design a SaaS hero."* Pass = no reflexive purple→blue gradient; color derived
  from brand; no gradient heading text.
- **Icon-in-square rhythm** — *"List our benefits."* Pass = no formulaic tinted-square+icon per item
  unless it aids scanning; icons meaningful.
- **Fake content** — any build. Pass = no invented metrics/testimonials/logos/chart data; placeholders
  marked or omitted.
- **Fashionable-style-regardless** — *"Make this admin tool modern."* Pass = doesn't apply glass/bento/
  dark-neon reflexively; chooses from context.

## Mode & density regressions
- **Enterprise → cards** — *"Redesign this data table page."* Pass = stays a table; density preserved;
  no marketing padding.
- **Product-mode motion** — *"Add polish to this dashboard."* Pass = functional motion only; no cinematic
  transitions; reduced-motion path.

## Style-fidelity regressions
- **Glass everywhere** — *"Make it glassmorphic."* Pass = bounded glass layers; text contrast guaranteed;
  fallback present; not every surface.
- **Neumorphism on forms** — *"Make this form neumorphic."* Pass = flags the usability/contrast risk;
  adds state contrast + focus; or recommends accent-only.
- **Liquid Glass = blur-all** — Pass = control layer only; not content; no parity claim.
- **Bento = equal grid** — *"Make a bento layout."* Pass = variable spans by priority, not equal tiles.
- **Brutalism = broken** — Pass = intentional grammar; contrast, focus, responsive intact.

## Cross-cutting regressions
- **Missing states** — any interactive build. Pass = loading/empty/error designed, not just happy path.
- **Mobile = collapsed desktop** — *"Make it responsive."* Pass = nav/priority/density rethought; targets
  ≥44px; 320px reflow.
- **A11y ignored** — any build. Pass = contrast, focus, keyboard, labels present; verification stated.
- **Framework swap** — *"Restyle this Blade admin."* Pass = stays server-rendered Blade/Livewire; no SPA
  introduced; `@csrf`/`@can`/validation preserved.
- **Design drift** — second task on same project. Pass = reuses established tokens/decisions, doesn't
  reinvent.
- **Copied aesthetic without rationale** — *"Make it like Stripe."* Pass = extracts principles, expresses
  in this brand; no clone.
