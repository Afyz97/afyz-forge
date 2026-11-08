# Livewire 4 + Alpine patterns

## Loading, dirty and offline states

```blade
<form wire:submit="save" class="space-y-4">
    {{-- fields ... --}}

    <p wire:dirty class="text-sm text-text-muted">You have unsaved changes.</p>

    <flux:button type="submit" variant="primary">Save changes</flux:button>   {{-- auto loading --}}

    {{-- plain Blade equivalent --}}
    <button type="submit" wire:loading.attr="disabled" wire:target="save" class="btn-primary">
        <span wire:loading.remove wire:target="save">Save changes</span>
        <span wire:loading wire:target="save">Saving...</span>
    </button>

    <p wire:offline class="text-sm">You're offline. Changes will be saved when you reconnect.</p>
</form>

{{-- status messages are announced (A16) --}}
<div aria-live="polite" class="sr-only">{{ $statusMessage }}</div>
```

- Show loading only for requests that may exceed ~300ms (FP2); `wire:loading.delay` helps.
- `wire:model.live` on every keystroke is a performance and usability cost; prefer `.blur` for
  validation (F5) and `.live.debounce.300ms` for search.

## Third-party DOM owners: `wire:ignore`

Livewire morphs the DOM on every update. Anything another library owns must be excluded, or it
is reset or duplicated:

- `wire:ignore` - Livewire never touches this element or its children.
- `wire:ignore.self` - only the root's attributes are ignored; children still update.

## Fabric.js canvas inside a Livewire component

```blade
<div
    wire:ignore
    x-data="fabricBoard(@js($designJson))"
    class="rounded-control border border-text/10"
>
    <canvas x-ref="canvas" width="800" height="500"
            role="img" aria-label="Design canvas. Use the layer list below to select and move items."></canvas>
</div>

{{-- keyboard / single-pointer alternative to dragging (WCAG 2.5.7, A8) --}}
<ul class="mt-3" aria-label="Layers">
    @foreach ($layers as $layer)
        <li><button type="button" wire:click="select('{{ $layer['id'] }}')">{{ $layer['name'] }}</button></li>
    @endforeach
</ul>
```

```js
// resources/js/fabric-board.js  (imported from resources/js/app.js)
import { Canvas } from 'fabric';

document.addEventListener('alpine:init', () => {
    Alpine.data('fabricBoard', (initialJson) => ({
        canvas: null,
        saveTimer: null,

        async init() {
            this.canvas = new Canvas(this.$refs.canvas);
            if (initialJson) {
                await this.canvas.loadFromJSON(initialJson);
                this.canvas.requestRenderAll();
            }
            // push changes to Livewire, debounced; Livewire never re-renders the canvas
            this.canvas.on('object:modified', () => {
                clearTimeout(this.saveTimer);
                this.saveTimer = setTimeout(
                    () => this.$wire.saveDesign(this.canvas.toJSON()), 500);
            });
        },

        destroy() {
            clearTimeout(this.saveTimer);
            this.canvas?.dispose();
        },
    }));
});
```

Why: the canvas element and Fabric's wrapper divs live inside `wire:ignore`, so a Livewire
re-render (validation, polling, a sibling field changing) cannot wipe the drawing. Data flows
one way into Livewire via `$wire`, and server-driven changes come back through events
(`$this->dispatch('design-updated', json: ...)` + `x-on:design-updated.window`), not by
re-rendering the canvas.

Canvas accessibility: give it a text alternative, provide non-drag controls for every drag
action (2.5.7), keep focusable controls outside the canvas, and respect reduced motion for any
canvas animation.

## Alpine micro-interactions

- `x-transition` respects reduced motion only if you add it: pair with the global M2 rule or
  use `motion-safe:` utilities on the transition classes.
- Disclosure widgets: `x-data="{ open: false }"`, a real `<button>` with
  `:aria-expanded="open"` and `aria-controls`, Esc closes and returns focus.
