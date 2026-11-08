# Handoff spec template

```markdown
## Build spec: [feature or screen]

### Purpose
[what it does; who uses it and in what situation]

### Layout
[grid, columns, gutters; how it responds]

### Tokens referenced
| Token | Value | Where it is used |
|---|---|---|
| `color-primary` | #[hex] | primary buttons, links |
| `spacing-md` | [n]px | gap between sections |
| `font-heading-lg` | [family, weight, size] | the screen's main heading |

### Building blocks
| Part | Which variant | Inputs / props | Remarks |
|---|---|---|---|

### Behaviour per state
| Part | In this state | Result |
|---|---|---|
| Primary button | Hover | background darkened by 10% |
| Primary button | Loading | spinner, keeps width, disabled |
| Form | Error | field outlined in danger colour, message below, focus moves to first error |

### Breakpoints
| Range | Behaviour |
|---|---|
| Desktop (>1024px) | default layout |
| Tablet (768-1024px) | [what differs] |
| Mobile (<768px) | [what differs] |

### Unhappy paths
Nothing to show: [..] | Very long text: [truncation + where the full text appears] |
Loading: [skeleton or spinner] | Error: [..] | 100+ items: [..] | BM strings: [..]

### Motion
| Element | Trigger | Animation | Duration | Easing | Reduced-motion version |
|---|---|---|---|---|---|

### Accessibility
Focus order: [..] | Accessible names: [..] | Keyboard: [..] | Announcements: [..]

### Implementation notes ([stack])
[from stack-notes.md]

### Open questions / assumed values
[..]
```
