# Example: Signup form

Rules: F1-F11, IC3, EP1, A13, A15, ER2

## Before

```html
<form>
  <input placeholder="First Name*"> <input placeholder="Last Name*">
  <input placeholder="Email*">
  <input type="password" placeholder="Password*" onpaste="return false">
  <input placeholder="Phone*">
  <input type="checkbox" checked> Send me offers
  <button>Submit</button>
</form>
```

Problems: placeholder labels (F1); forced first/last split (IC3); required asterisks instead
of optional marks (F2); paste blocked (F10, A13); no autocomplete/types (F4); phone probably
not needed (F3); pre-checked marketing (F11, EP1); "Submit" (B1).

## After

```html
<form action="/signup" method="post" novalidate>
  <div class="error-summary" role="alert" tabindex="-1" hidden>
    <h2>Please fix 1 thing</h2>
    <ul><li><a href="#email">Enter an email address like name@example.com</a></li></ul>
  </div>

  <div class="field">
    <label for="name">Full name</label>
    <input id="name" name="name" autocomplete="name">
  </div>

  <div class="field">
    <label for="email">Email</label>
    <p id="email-hint" class="hint">We'll send a link to confirm it's you.</p>
    <input id="email" name="email" type="email" autocomplete="email" inputmode="email"
           aria-describedby="email-hint email-error" aria-invalid="true" value="aisyah@gmail">
    <p id="email-error" class="field-error">Enter an email address like name@example.com</p>
  </div>

  <div class="field">
    <label for="password">Password</label>
    <p id="pw-rules" class="hint">At least 12 characters. Passphrases work well.</p>
    <input id="password" name="password" type="password" autocomplete="new-password" aria-describedby="pw-rules">
    <button type="button" class="link-btn" aria-controls="password" aria-pressed="false">Show password</button>
  </div>

  <div class="field">
    <label for="phone">Mobile number <span class="optional">(optional)</span></label>
    <p id="phone-hint" class="hint">Only used for account recovery.</p>
    <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-hint">
  </div>

  <label class="checkbox"><input type="checkbox" name="marketing"> Email me product news (about once a month)</label>

  <button type="submit" class="btn btn--primary">Create account</button>
  <p class="terms">By creating an account you agree to the <a href="/terms">Terms</a> and <a href="/privacy">Privacy notice</a>.</p>
</form>
```

Behaviour:
- Validate on blur and submit, not per keystroke. On submit error, keep all values, show the
  summary, focus it, and link each item to its field.
- Server normalises phone (`012-345 6789`, `+60 12 345 6789`, `0123456789` all accepted).
- Loading state: button keeps width, shows spinner, `aria-busy`, blocks double submit.
- No first/last split, no character-set validation on names.
