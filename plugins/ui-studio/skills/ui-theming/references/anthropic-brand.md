# Anthropic brand (restricted use)

Use only when the work is branded as Anthropic. On anyone else's product this palette is a
misuse of another company's identity and also the AD1 "AI default" tell.

## Colours

| Role | Name | Hex |
|---|---|---|
| Primary text, dark backgrounds | Dark | `#141413` |
| Light backgrounds, text on dark | Light | `#faf9f5` |
| Secondary neutral | Mid Gray | `#b0aea5` |
| Subtle neutral | Light Gray | `#e8e6dc` |
| Primary accent | Orange | `#d97757` |
| Secondary accent | Blue | `#6a9bcc` |
| Tertiary accent | Green | `#788c5d` |

Non-text shapes rotate through the accents in order: orange, blue, green.

## Type

- Headings: Poppins, 24pt and above, with Arial as fallback.
- Body: Lora, with Georgia as fallback.
- Text colour follows the background: Dark on light grounds, Light on dark grounds.

## In files

pptx via python-pptx: `RGBColor.from_string("D97757")` and so on; apply to shapes, not as text
colour on light grounds unless contrast passes.
