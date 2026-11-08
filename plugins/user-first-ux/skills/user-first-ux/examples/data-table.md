# Example: Data table

Rules: TB1-TB6, T6, SN2, ST, A15

## Before

```html
<table>
  <tr><td>INV-0012</td><td>Syarikat Maju Jaya Sdn Bhd</td><td>1234.5</td><td>2026-09-01</td><td style="color:red">overdue</td></tr>
</table>
```

Problems: no header row or sort state (TB1); numbers left-aligned, unformatted, no unit
(TB2); raw ISO date (TB3); status by colour only (C3); no empty/loading/error states (ST);
filters not in URL (SN2); unusable at 320px (TB4).

## After

```html
<div class="filters" aria-label="Active filters">
  <button type="button" class="chip">Status: Overdue <span aria-hidden="true">x</span><span class="sr-only">Remove filter</span></button>
</div>

<div class="table-wrap">
  <table>
    <caption class="sr-only">Invoices, 128 results, sorted by due date descending</caption>
    <thead>
      <tr>
        <th scope="col">Invoice</th>
        <th scope="col">Customer</th>
        <th scope="col" class="num">Amount (RM)</th>
        <th scope="col" aria-sort="descending"><button type="button">Due date <span aria-hidden="true">v</span></button></th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">INV-0012</th>
        <td data-label="Customer">Syarikat Maju Jaya Sdn Bhd</td>
        <td data-label="Amount (RM)" class="num">1,234.50</td>
        <td data-label="Due date"><time datetime="2026-09-01" title="1 Sep 2026">26 days ago</time></td>
        <td data-label="Status"><span class="status status--danger"><svg aria-hidden="true"><use href="#icon-alert"/></svg> Overdue</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-wrap { overflow:auto; max-block-size:70vh; }
thead th { position:sticky; inset-block-start:0; background:var(--color-surface); z-index:1; }
.num { text-align:end; font-variant-numeric:tabular-nums; }
@media (max-width: 40rem) {
  table, thead, tbody, tr, th, td { display:block; }
  thead { position:absolute; inline-size:1px; block-size:1px; overflow:hidden; clip-path:inset(50%); }
  tr { border:1px solid var(--color-border); border-radius:var(--radius-md); padding:var(--space-3); margin-block-end:var(--space-2); }
  td[data-label]::before { content:attr(data-label); display:block; font-size:var(--text-xs); color:var(--color-text-muted); }
}
```

```js
// Filters, sort and page live in the URL so Back, reload and sharing work.
const params = new URLSearchParams(location.search);
params.set('status', 'overdue'); params.set('sort', '-due'); params.set('page', '1');
history.pushState(null, '', `?${params}`);
```

States:
- Loading: skeleton rows matching column widths (after 300ms).
- Empty (no data): "No invoices yet. Create your first invoice." + button.
- Empty (filtered): "No overdue invoices. Clear filters" button.
- Error: "Couldn't load invoices. Retry" + reference ID; keep current filters.
- Selection: bulk bar "3 selected - Send reminders - Select all 128 results".
