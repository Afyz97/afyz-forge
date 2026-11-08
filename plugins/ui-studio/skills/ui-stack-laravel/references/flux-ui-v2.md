# Flux UI v2

Flux components take care of hover, active and focus styling; your job is wiring the states
that depend on data: loading, disabled-with-reason, error, empty.

## Accent theming

Flux reads three variables (defined in `@theme`, overridden for `.dark` in `@layer theme`; see
the SKILL.md example):

| Variable | Used for |
|---|---|
| `--color-accent` | primary button backgrounds, accent fills |
| `--color-accent-content` | accent-coloured text (text contrast per the quality floor, on the surface) |
| `--color-accent-foreground` | text on top of an accent fill (text contrast per the quality floor, on the accent) |

Flux's neutral is zinc. To change it, reassign `--color-zinc-50` ... `--color-zinc-950` in
`@theme` to your neutral ramp. Use `:accent="false"` on tabs, navbar or navlist items that
should stay neutral.

## Button with every state

```blade
{{-- default / hover / active / focus: styled by Flux --}}
<flux:button variant="primary" wire:click="publish">Publish post</flux:button>

{{-- loading: automatic for wire:click and type="submit" (spinner + no pointer events) --}}
<flux:button type="submit" variant="primary">Save changes</flux:button>

{{-- disabled, with the reason next to it (B2) --}}
<div class="flex items-center gap-3">
    <flux:button variant="primary" disabled aria-describedby="publish-why">Publish post</flux:button>
    <flux:text id="publish-why">Add a title to publish.</flux:text>
</div>

{{-- destructive: separate from the primary action (U1), specific label (B4) --}}
<flux:button variant="danger" wire:click="confirmDelete">Delete post</flux:button>

{{-- icon-only: accessible name required (B5) --}}
<flux:button square icon="trash" variant="ghost" aria-label="Delete post" />
```

Variants: `outline` (default), `primary`, `filled`, `danger`, `ghost`, `subtle`. Sizes:
`base`, `sm`, `xs` (check `xs` still meets the AA target minimum; prefer `base` on touch).

## Input / field with every state

```blade
<flux:field>
    <flux:label>Email</flux:label>
    <flux:description>We send the receipt here.</flux:description>
    <flux:input
        wire:model.blur="email"     {{-- validate on blur, not per keystroke (F5) --}}
        type="email"
        autocomplete="email"
        icon="envelope" />
    <flux:error name="email" />     {{-- error: message under the field, input keeps its value (F6) --}}
</flux:field>

{{-- optional field marked, not required ones (F2) --}}
<flux:field>
    <flux:label badge="Optional">Mobile number</flux:label>
    <flux:input wire:model="phone" type="tel" autocomplete="tel" />
    <flux:error name="phone" />
</flux:field>

{{-- read-only and disabled --}}
<flux:input label="Staff ID" value="{{ $staffId }}" readonly />
<flux:input label="Company" disabled description="Set by your administrator." />
```

`invalid` forces error styling when the error comes from somewhere other than the validator.
Loading for a field-triggered request: `wire:loading` + `wire:target="email"` on a hint next to
the field.

## Empty and error states around Flux lists

Flux does not invent empty states. Every `@forelse` gets an `@empty` branch that says what goes
here, why it is empty and one action to start (O1), written with the `ui-ux-copy` skill (user-first-ux plugin).
