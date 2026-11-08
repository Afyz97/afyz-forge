---
name: ui-ux-copy
description: >-
  Writes and fixes interface words in English and Bahasa Melayu: button and CTA labels, error
  messages, empty states, confirmation dialogs, tooltips, loading text, onboarding steps, toasts,
  form labels and helper text. Use for "what should this button say?", "write the error
  message", "improve this microcopy", "empty state copy", "translate or localise this UI to
  BM", "terjemah label butang", "is this wording clear?", "make this dialog less scary", or when
  reviewing lang/*.php, lang/*.json, messages/*.json or other i18n string files. Returns a
  recommended line, three alternatives with tone, the reasoning, and localisation notes (BM
  length expansion, sentence case in both languages, one verb per action across languages).
  Not for long-form marketing pages, documentation or blog posts, and not for layout or visual
  feedback - use ui-critique.
argument-hint: "<screen, flow or string to write>"
---

# UX copy (EN + BM)

Rules owned elsewhere, linked not repeated:
- Content rules CM1-CM9: `../user-first-ux/references/content.md`
- Inclusive and locale rules IC1-IC6: `../user-first-ux/references/inclusive-context.md`
- Error formula and recovery ER1-ER5: `../user-first-ux/references/states-feedback.md`
- Honest copy, banned dark patterns EP1-EP7: `../user-first-ux/references/ethics-privacy.md`

## Collect first

1. **Where**: the screen, flow or feature, and where the text sits.
2. **Who and in what state**: what the person is trying to do and how they probably feel
   (rushed, worried about money, first visit).
3. **Voice**: formal, friendly, playful or reassuring. If no brand voice is available from a
   knowledge base or the repo, ask once; otherwise default to plain and friendly.
4. **Limits**: character counts, platform conventions, languages required (EN, BM, both).

## What good interface text does

Text exists so the interface can be understood and used; it is part of the design, not a
coat of paint on top. Before writing, decide what this spot must communicate, then find the
shortest honest way to say it.

- **Understandable.** No jargon, nothing ambiguous. Call things by the name users know, not the
  name the codebase uses ("Notifications", never "webhook config"). Describe; do not pitch.
  A precise phrase beats a clever one.
- **Short.** Every word carries meaning; each element has one job.
- **Same word, same thing.** One term per concept everywhere (CM4). An action keeps its verb
  across the whole journey: a "Publish" button produces a "Published" toast. Consistent
  vocabulary is how people learn their way around.
- **Helpful.** Each word moves the user toward their goal.
- **Human.** Conversational, plain verbs, sentence case, active voice. Tone follows brand and
  audience.

Patterns for each element (CTA, error, empty state, confirmation, tooltip, loading,
onboarding) and tone by moment: `references/patterns.md`.

## Bilingual work

Load `references/bilingual-bm-en.md` whenever BM is involved: the verb glossary, sentence case
in BM, expansion allowance, word order and plurals, and how strings live in Laravel and Next.

## Output

Use `references/template.md`: the chosen line, three alternatives with tone and when to use
each, why the chosen line works, and translation/locale notes. For a review of existing strings,
use the review table in `../user-first-ux/SKILL.md` with CM / IC / BM rule IDs.

## Connectors

A knowledge base supplies brand voice, style guide and the existing glossary; a design tool
shows the text in context with real character limits (connector roles: the **ui-studio** connectors reference, if installed; otherwise use what is
connected and never claim a connector was used when it was not).
