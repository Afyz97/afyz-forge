# Example: Product card

Rules: CL1, CM1, CM2, EP1, EP3, T6, FP4, B1

## Before

```html
<div class="card" onclick="go(42)">
  <img src="kettle.jpg">
  <h3>Electric Kettle 1.7L</h3>
  <p>RM89</p>
  <p class="red">HURRY! Only 2 left! Offer ends in 09:59</p>
  <a href="/p/42">View</a> <button>Add</button>
</div>
```

Problems: div with onclick is not keyboard-reachable and nests competing links (CL1, A5);
image has no size (CLS) or alt (FP4, A2); fake countdown and scarcity (CM2, EP1); price
excludes known fees (EP3); "Add" lacks an object (B1).

## After

```html
<article class="product-card">
  <img src="kettle.avif" alt="Stainless steel electric kettle, 1.7 litre" width="320" height="240" loading="lazy">
  <h3 class="product-card__title"><a href="/p/42" class="product-card__link">Electric kettle, 1.7 L</a></h3>
  <p class="product-card__price">RM 89.00 <span class="product-card__note">incl. SST</span></p>
  <p class="product-card__stock"><!-- computed from real stock, see below --></p>
  <button type="button" class="btn btn--secondary">Add to cart</button>
</article>
```

```css
.product-card { position:relative; display:grid; gap:var(--space-2); }
.product-card__link::after { content:""; position:absolute; inset:0; } /* whole card clickable */
.product-card .btn { position:relative; z-index:1; }                   /* button stays its own target */
.product-card__price { font-size:var(--text-lg); font-weight:700; font-variant-numeric:tabular-nums; }
```

```js
function stockCopy(qty) {
  if (qty === 0) return 'Out of stock - <a href="/p/42/notify">Notify me</a>';
  if (qty <= 5)  return `Only ${qty} left`;            // real, computed
  return 'In stock - ships in 1-2 days';               // no urgency when plentiful
}
```

When stock is 0, replace "Add to cart" with "Notify me" and link to similar items.
