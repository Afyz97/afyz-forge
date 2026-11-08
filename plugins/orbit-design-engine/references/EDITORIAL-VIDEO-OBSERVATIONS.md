# Reference C: Animated UI checklist explainer — observed evidence

Source: user-supplied 92.47-second vertical MP4, 720×1280 at 30 fps. The video is a **motion-graphics explainer showing imagined product UI** and a numbered compliance checklist; it is neither a recording of the original enterprise website reference nor evidence of those checklist items being universally legally required. Extracted reference stills are in `assets/editorial-video-reference/`. Use for local comparison; do not redistribute the captures without rights.

## Visual grammar — what is actually visible

- **Canvas:** spacious background with subtle dot-grid texture and diffuse theme-derived illumination; intentionally spacious 9:16 portrait composition.
- **Text:** high-contrast heavy headline, centered in the upper part of the canvas. Select phrases are *theme-accent italic serif*, while highlighted terms have a theme-derived translucent band; semantic correction copy indicates disallowed behaviour. Long headings split into 2–3 tightly spaced lines.
- **Cards:** elevated miniature application windows with browser dots, pill controls, muted faux input text, host-theme action buttons, semantically styled success checks. Cards have soft dimensional shadows, rounded corners and small skew/rotation, sometimes stack as a foreground prop over a persistent application frame.
- **Status:** small floating check icon + “Checklist” + narrow theme-accent fill + `n / 35` counter. The tracker remains anchored while scene contents change; the visual system suggests progression and continuity.
- **Character:** small, pixel/block-like character near the lower third; occasional eyebrow/eye/pose changes and small reactions. A supporting narrator rather than the product's main UI.
- **Secondary detail:** sparkling stars, rings and pointer-path marks, semantically styled warnings and focus outlines, scissors/strikethrough treatment, semi-transparent ghosting during changes.

## Temporal / movement observations (approximate timestamps, not source timing)

| Window | Scene and motion observed | Reusable pattern |
|---|---|---|
| 0–2.3s | Word “Claude!” switches into multi-part headline; mascot blinks/wakes and shifts; application window scales into view | Brand/hero entrance; identity-to-message transition |
| 2.3–5s | “legal trouble” enters as a corrective phrase; legal-notice sticker overlays a card then leaves; heading changes | Phrase swap; warning sticker; continuity across scenes |
| 5–9s | Privacy card pops into foreground with tilt; linked terms card joins as a second layer; check/spark cues appear | Layered paper/card reveal; verification pop |
| 9–16s | Cookie dialog, email unsubscribe, retention panel and countdown mockups succeed one another, while progress is persistent | Content replace; anchored frame; staggered inset controls |
| 16–18s | Fake countdown heading gains strike-through; urgency badge becomes the focus | Corrective typography / anti-pattern highlight |
| 18–21s | Alt-label overlay and keyboard focus ring enter; Tab cue travels between inputs | Annotation-to-control, focus-travel storytelling |
| 21–29s | Logo chips, licensing cards and account deletion layers fly/slide into organized groups | Fanned cards; relation diagram; grouped entrance |
| 29–33s | Highlighted dark-pattern warning transforms to respectful cancel; colorful image gains AI-generated pill | Before/after state morph; capsule pop |
| 33–42s | Consent checkbox / policies / refund / cancel / input minimisation flows present a new centered card each scene | Reusable anchored UI template; reveal + actionable focus |
| 42–60s | Reviews, claims, parental consent, acceptance, open-source and marketing permissions; UI examples change in sync with emphasized words | Text–visual coupling; sequential micro-proof |
| 60–76s | Copyright notice, unauthorized AI-training flow, renewals, SDK map, DPA and tracker toggles; diagram lines and pointers explain relations | Diagram orchestration; edge reveal; target highlight |
| 76–83s | Table/list and invoice examples with staggered row appearance and action emphasis | Structured-card reveal; accounting transparency |
| 83–86s | Completed checklist with 35/35 appears; entries condense, highlight row, mascot celebrates | Progress culmination; restraint after completion |
| 86–92.47s | “SAFE” capsule and checklist card grows/populates; legal disclaimer fades in; final lawyer-review reminder | CTA build-up; persistent summary; semantic closing |

### Inferred vs verified

**Verified visually:** layering, visual order, persistent progress, text emphasis and motion direction across sampled frames. **Not verifiable from rendered footage:** whether effects use GSAP, After Effects, CSS or keyframes; exact cubic Bézier curves, duration values, source assets, shadows or fonts. The accompanying implementation settings are recommendations, not extracted original code.

## Core distinction for any coding agent

**An app screen is a work tool; this video is a promotional storyboard.** Borrow the visual hierarchy, controlled state changes, color grammar, motion continuity, labels and success feedback for application UI. Reserve continual headline swaps, scene cuts, roaming mascot and excessive floating layers for *opt-in* landing pages, onboarding, guided demos, explainer sequences and celebration states. Do **not** turn normal admin forms/tables into an animated advertisement.
