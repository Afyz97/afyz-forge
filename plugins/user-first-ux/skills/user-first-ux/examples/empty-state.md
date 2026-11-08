# Example: Empty state

Rules: O1, ST, CM5, L5

## Before

```html
<div class="empty">
  <img src="sad-robot.svg">
  <p>No data</p>
</div>
```

Problems: does not say what goes here or why it matters; no next step; decorative image with
no `alt=""`; one message for three different situations.

## After: first use

```html
<section class="empty-state" aria-labelledby="es-title">
  <img src="invoices-illustration.svg" alt="" width="160" height="120">
  <h2 id="es-title">Send your first invoice</h2>
  <p>Invoices you create appear here, with their status, so you can see who has paid and who needs a reminder.</p>
  <a href="/invoices/new" class="btn btn--primary">Create invoice</a>
  <p><a href="/invoices/new?sample=1">Try with sample data</a></p>
</section>
```

## After: no results (filters or search)

```html
<section class="empty-state" role="status">
  <h2>No invoices match "maju jaya" and "Overdue"</h2>
  <p>Check the spelling or remove a filter.</p>
  <button type="button" class="btn btn--secondary">Clear filters</button>
</section>
```

## After: cleared (user finished everything)

```html
<section class="empty-state">
  <h2>All caught up</h2>
  <p>No overdue invoices. We'll show new ones here when they're due.</p>
</section>
```

Each variant has one CTA at most, a heading that says what the situation is, and copy that
explains why the space matters.
