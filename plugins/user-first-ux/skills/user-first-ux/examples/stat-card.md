# Example: Account stat card

Rules: H1, H2, H3, H4, T6, C3, TB3

## Before

```html
<div class="card">
  <p>Account No: 1234-5678-90</p>
  <p>Balance: 12450.5</p>
  <p>Change: 32%</p>
  <p>Last Updated: 3 weeks ago</p>
  <p>Type: Savings</p>
</div>
```

Problems: every row has equal weight (H1, H2); balance unformatted and not dominant; "32%"
has no direction, sign or comparison (H3); identifier mixed with facts (H4); relative date
with no absolute date (TB3).

## After

```html
<article class="stat-card" aria-labelledby="acct-title">
  <header class="stat-card__header">
    <h2 id="acct-title" class="stat-card__title">Savings account</h2>
    <span class="stat-card__id">**** 7890</span>
  </header>

  <p class="stat-card__label">Available balance</p>
  <p class="stat-card__value">RM 12,450.50</p>
  <p class="stat-card__trend stat-card__trend--up">
    <svg aria-hidden="true" width="12" height="12" viewBox="0 0 12 12"><path d="M6 2l4 6H2z"/></svg>
    <span>+32%</span> <span class="stat-card__context">vs last month</span>
  </p>

  <dl class="stat-card__facts">
    <div><dt>Account type</dt><dd>Savings</dd></div>
    <div><dt>Last updated</dt><dd><time datetime="2026-09-06" title="6 Sep 2026">3 weeks ago</time></dd></div>
  </dl>
</article>
```

```css
.stat-card__header { display:flex; justify-content:space-between; align-items:baseline; padding-block-end:var(--space-3); }
.stat-card__title  { font-size:var(--text-md); font-weight:600; }
.stat-card__id     { font-size:var(--text-sm); color:var(--color-text-muted); font-variant-numeric:tabular-nums; }
.stat-card__label  { font-size:var(--text-xs); font-weight:500; text-transform:uppercase; letter-spacing:.06em; color:var(--color-text-muted); }
.stat-card__value  { font-size:var(--text-2xl); font-weight:700; font-variant-numeric:tabular-nums; }
.stat-card__trend--up { color:var(--color-success); }
.stat-card__context { color:var(--color-text-muted); }
.stat-card__facts  { display:grid; grid-template-columns:1fr 1fr; gap:var(--space-2) var(--space-4);
                     border-block-start:1px solid var(--color-border); padding-block-start:var(--space-3); margin-block-start:var(--space-4); }
.stat-card__facts dt { font-size:var(--text-xs); color:var(--color-text-muted); }
```

Trade-off named: masked the account number (EP5) even though the full number is "useful";
full number is one tap away on the account page.
