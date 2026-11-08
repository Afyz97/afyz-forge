# skill-guard

Audit a third-party skill, plugin or marketplace **before** installing it. Gives a PASS / REVIEW / BLOCK
verdict, with evidence, for a pinned commit SHA.

```
/plugin install skill-guard@afyz-forge
```

Then ask: "should I install github.com/someone/their-skills?" or "is this .skill file safe?".

## What's inside

| Path | Role |
|---|---|
| `skills/skill-guard/SKILL.md` | Workflow: quarantine, scan, manual review, verdict, report, clean up |
| `skills/skill-guard/references/threat-model.md` | 12-section checklist for the manual review |
| `skills/skill-guard/scripts/scan_skill.py` | Read-only static scanner, Python 3.8+ stdlib, no network |
| `tests/test_scan_skill.py` | Scanner self-check: `python -I plugins/skill-guard/tests/test_scan_skill.py` |
| `evals/` | Routing evals: `claude plugin eval ./plugins/skill-guard --ablation none` |

## Known limits

- Regex triage: false positives on docs that *describe* attacks (this plugin scans as critical
  itself), and misses on novel tricks. That's why the manual review step is mandatory.
- Static only: it can't see what a remote payload or an `npx pkg@latest` will download later.
- No provenance lookups (stars, repo age, ownership changes): the reviewer checks those by hand.

## Changes from the original `.skill`

- The scanner forces UTF-8 output. Before, on Windows, evidence containing the Unicode it hunts
  (e.g. Cyrillic homoglyphs) crashed it mid-report with exit 1.
- New `HID-HOMOGLYPH` rule: hostnames that mix ASCII and look-alike non-ASCII letters.
- Docs use ASCII only, show Windows-friendly commands (`python -I`, `mktemp -d`) and give the plugin script path.
