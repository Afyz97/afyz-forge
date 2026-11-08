# Example: Avatar stack

Rules: S1, S3, A2, A7

## Before

```html
<div class="members">
  <img src="aisyah.jpg"><img src="ravi.jpg"><img src="mei.jpg"><img src="daniel.jpg">
  <img src="farah.jpg"><img src="ahmad.jpg"><img src="lim.jpg"><!-- ...wraps to 3 rows -->
</div>
```

Problems: wrapped grid wastes space (S1); images have no alt; no count; no way to see the
full list; screen readers hear nothing useful (S3).

## After

```html
<button type="button" class="avatar-stack" aria-haspopup="dialog"
        aria-label="12 members: Aisyah binti Rahman, Ravi Kumar, Mei Ling and 9 others. Show all members">
  <img src="aisyah.jpg" alt="" width="32" height="32">
  <img src="ravi.jpg"   alt="" width="32" height="32">
  <img src="mei.jpg"    alt="" width="32" height="32">
  <span class="avatar-stack__more" aria-hidden="true">+9</span>
</button>
```

```css
.avatar-stack { display:inline-flex; align-items:center; min-block-size:44px; padding:0; border:0; background:none; cursor:pointer; }
.avatar-stack > * { inline-size:32px; block-size:32px; border-radius:50%; border:2px solid var(--color-surface); }
.avatar-stack > * + * { margin-inline-start:-8px; }
.avatar-stack__more { display:grid; place-items:center; font-size:var(--text-xs); font-weight:600;
                      background:var(--color-surface-muted); color:var(--color-text); }
.avatar-stack:focus-visible { outline:2px solid var(--color-focus); outline-offset:2px; border-radius:var(--radius-full); }
```

Images use `alt=""` because the button's `aria-label` carries the names once; per-image alt
would be read twice. The button opens a dialog listing all 12 members.
