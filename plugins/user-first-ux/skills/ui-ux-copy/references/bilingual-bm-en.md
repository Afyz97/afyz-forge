# Bilingual rules: Bahasa Melayu and English (BM)

Extends IC2 (localisation) in `../../user-first-ux/references/inclusive-context.md`.

## BM1 Sentence case in both languages

Only the first word and proper nouns are capitalised, in BM exactly as in EN:
"Simpan perubahan", not "Simpan Perubahan"; "Log masuk", not "Log Masuk". Product names and
official programme names keep their own casing.

## BM2 One verb per action, the same pair everywhere

Pick one BM verb for each action, record it in the project glossary, and use it in buttons,
toasts, menus, emails and errors alike. The result word follows the action (Simpan ->
"Disimpan", Publish -> "Published" / Terbitkan -> "Diterbitkan").

| Action | EN | BM |
|---|---|---|
| Save | Save | Simpan |
| Cancel | Cancel | Batal |
| Delete | Delete | Padam |
| Edit | Edit | Sunting |
| Create | Create | Cipta |
| Add | Add | Tambah |
| Submit (avoid; name the outcome) | Send / Apply / Pay | Hantar / Mohon / Bayar |
| Search | Search | Cari |
| Download / Upload | Download / Upload | Muat turun / Muat naik |
| Sign in / Sign out | Sign in / Sign out | Log masuk / Log keluar |
| Sign up | Sign up | Daftar |
| Continue / Back | Continue / Back | Teruskan / Kembali |
| Close | Close | Tutup |
| Confirm | Confirm | Sahkan |
| Update | Update | Kemas kini |
| Retry | Try again | Cuba lagi |
| Publish | Publish | Terbitkan |
| Share / Copy | Share / Copy | Kongsi / Salin |

Where a project already uses a different established term (e.g. "Ubah" for Edit), keep it;
consistency beats the table.

## BM3 Plan for longer strings

BM labels often run 30-40% longer than English (IC2). Buttons and table headers must wrap or
grow, never truncate a verb. Test layouts with the longer language; no fixed-width buttons.

## BM4 Never assemble sentences from fragments

Word order differs (BM puts most modifiers after the noun: "fail baharu" for "new file"), so
`"New " + item` breaks. Use whole messages with placeholders: `__('messages.file_created', ['name' => $name])`.

## BM5 Plurals

English needs plural forms ("1 file" / "3 files"); BM normally uses one form with a number
("1 fail", "3 fail"), without reduplication. Use plural-aware messages (`trans_choice`, ICU
`{count, plural, ...}`) so each language gets its own rule.

## BM6 Address and tone

Use "anda" consistently for the user; avoid mixing in "awak" or "kamu". Keep the same
politeness level across both languages. No apology in either language unless the system is at
fault (ER4).

## BM7 Standard spelling

Follow standard BM spelling (DBP) for common UI terms, e.g. "e-mel", "kata laluan",
"pautan", "tetapan", "muat naik". Do not mix English and BM in one label unless the English
term is the established one in that product.

## BM8 Locale formats are not translation

Dates, numbers and currency come from the locale formatter, not from translated strings
(`Intl.DateTimeFormat('ms-MY')`, `Number::currency(..., locale: 'ms_MY')`). DD/MM/YYYY for
Malaysian audiences.

## Where strings live

| Stack | EN | BM |
|---|---|---|
| Laravel | `lang/en/*.php` or `lang/en.json` | `lang/ms/*.php` or `lang/ms.json` |
| Next.js (e.g. next-intl) | `messages/en.json` | `messages/ms.json` |

Set `lang="ms"` / `lang="en"` on `<html>` per locale, and `lang` on inline passages in the other
language (A10).
