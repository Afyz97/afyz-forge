# Example: Destructive-action confirm

Rules: B4, CL2, U1, EP1, CM8, ER3

## Before

```html
<div class="modal">
  <p>Are you sure?</p>
  <button class="btn-red">Yes</button> <button>No</button>
</div>
```

Problems: no consequence stated; "Yes / No" labels (B4); no focus management (CL2); danger
button styled like the primary path and placed where the eye lands first.

## Preferred: undo instead of confirm (reversible actions)

```html
<div role="status" aria-live="polite" class="toast">
  3 invoices moved to Trash. <button type="button">Undo</button>
</div>
```
Keep items in Trash for 30 days (ER3). The toast stays >= 5s and pauses on hover/focus.

## When it truly cannot be undone

```html
<dialog id="confirm-delete" aria-labelledby="cd-title" aria-describedby="cd-desc">
  <h2 id="cd-title">Delete 3 invoices?</h2>
  <p id="cd-desc">INV-0012, INV-0013 and INV-0019 will be permanently deleted. This can't be undone.</p>
  <form method="dialog" class="actions">
    <button value="cancel" class="btn btn--secondary" autofocus>Cancel</button>
    <button value="delete" class="btn btn--danger">Delete invoices</button>
  </form>
</dialog>
```

```js
const dlg = document.getElementById('confirm-delete');
const trigger = document.activeElement;
dlg.showModal();                                   // native focus trap + Esc to close
dlg.addEventListener('close', () => {
  if (dlg.returnValue === 'delete') deleteInvoices();
  trigger.focus();                                 // return focus to the trigger
}, { once: true });
```

Notes: initial focus on the safe action; destructive button uses the danger style and a
specific label; no guilt copy.
