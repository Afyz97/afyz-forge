# NOTICE

ui-studio is licensed under Apache-2.0 (see the repository `LICENSE`).

## Upstream skills

The guidance in this plugin derives from the eleven skills below, by way of an intermediate
merged skill (`ui-design`). All prose from those sources was **rewritten in new words and
restructured** for this plugin; it is not a copy. Facts and data were kept exactly: WCAG
criterion numbers and thresholds, hex values, theme palettes, font names, research sample
sizes and durations, breakpoint values and technical specifications.

| # | Upstream skill | Publisher | Licence | Used in |
|---|---|---|---|---|
| 1 | frontend-design | Anthropic | Apache-2.0 (`licenses/frontend-design.txt`) | ui-visual-direction, shared principles and ai-defaults, ui-ux-copy |
| 2 | web-artifacts-builder | Anthropic | Apache-2.0 (`licenses/web-artifacts-builder.txt`) | ai-defaults (AD6), ui-stack-next token conventions. Its scripts were not included. |
| 3 | canvas-design | Anthropic | Apache-2.0 (`licenses/canvas-design.txt`) | ui-canvas-art |
| 4 | theme-factory | Anthropic | Apache-2.0 (`licenses/theme-factory.txt`) | ui-theming, `skills/ui-theming/assets/theme-showcase.pdf` (unchanged) |
| 5 | brand-guidelines | Anthropic | Apache-2.0 (`licenses/brand-guidelines.txt`) | ui-theming (Anthropic brand, restricted use) |
| 6 | design:design-system | Anthropic design plugin | no licence file in the source | ui-design-system |
| 7 | design:design-handoff | Anthropic design plugin | no licence file in the source | ui-handoff |
| 8 | design:design-critique | Anthropic design plugin | no licence file in the source | ui-critique |
| 9 | design:accessibility-review | Anthropic design plugin | no licence file in the source | ui-accessibility |
| 10 | design:ux-copy | Anthropic design plugin | no licence file in the source | ui-ux-copy |
| 11 | design:user-research and design:research-synthesis | Anthropic design plugin | no licence file in the source | ui-research |

Items 6-11 carried no licence file, so their content was rewritten with no verbatim sentences.

Since 1.0.0 the skills from rows 9, 10 and 11 (`ui-accessibility`, `ui-ux-copy`, `ui-research`)
live in the user-first-ux plugin, whose `NOTICE.md` repeats their attribution.

## From this repository (2026-11 merge)

- `user-first-ux` (Apache-2.0, same author) was absorbed in 0.1.0 and handed back in 1.0.0: its
  rules now live only in the user-first-ux plugin, which ui-studio points to by skill name.
- `ui-ten-fixes` (Apache-2.0, same author) became the `visual-polish` skill (rules, scripts,
  assets unchanged except where noted in `.ai/docs/merge/plan.md`).
- `omni-design` and `ultimate-design-suite` (Apache-2.0, same author; original synthesized
  guidance) supplied `ui-styles` and several references. Their provenance record is
  `docs/archive/omni-design/SOURCES.md`.

## Fonts

`skills/ui-canvas-art/assets/fonts/` contains 29 font families, each distributed under the
SIL Open Font License 1.1 and shipped unmodified with its own `*-OFL.txt`.
`IBMPlexSerif-OFL.txt` is the IBM Plex family licence (the same text as `IBMPlexMono-OFL.txt`);
`InstrumentSerif-OFL.txt` was taken from the google/fonts repository
(`ofl/instrumentserif/OFL.txt`).

## Not included

The upstream React-artifact tooling (`init-artifact.sh`, `bundle-artifact.sh`,
`shadcn-components.tar.gz`) only works on claude.ai and is not part of this plugin.
