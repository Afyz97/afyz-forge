# Inclusive & Local Context (IC)

- **IC1 Real constraints** - design for low-end Android, slow or metered data, small screens,
  bright sunlight, one-handed use and interruptions. Test on a mid-range phone with throttled
  network.
- **IC2 Localisation**
  - Every string externalised (no concatenated sentences; use ICU/plural-aware messages).
  - Layouts tolerate 30-40% longer text (Malay and German strings often run longer than
    English).
  - RTL-ready logical CSS: `margin-inline-start`, `padding-inline`, `inset-inline-end`,
    `text-align: start`.
  - Locale-aware date, number and currency formats via `Intl` (e.g. `en-MY`: DD/MM/YYYY,
    RM 1,234.50). Never hand-format.
- **IC3 Names** - a single "Full name" field. Do not force a first/last split; many naming
  conventions do not fit (e.g. patronymic "bin/binti" names, mononyms). Do not validate names
  by character set or length minimums. Optionally ask "What should we call you?".
- **IC4 Gender, title and similar fields** - only if truly needed; inclusive, optional options,
  including "Prefer not to say".
- **IC5 Low digital literacy and older users** - clear text labels over icons, larger targets,
  forgiving flows, visible help, no time pressure.
- **IC6 Addresses & phones** - do not force one country's format; accept +60 and local 01x
  forms with spaces or dashes; postcode as text with `inputmode="numeric"`.

```js
new Intl.NumberFormat('en-MY', { style: 'currency', currency: 'MYR' }).format(1234.5); // "RM 1,234.50"
new Intl.DateTimeFormat('en-MY').format(new Date(2026, 8, 27));                        // "27/09/2026"
```
