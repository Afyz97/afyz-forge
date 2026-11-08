# CodeWeave Decision Log - Template

> Copy into a project-specific plan location when the project permits it. Include a stable date and commit SHA. One line item per *observable coupling defect*; group by a common cause. Do not confuse heuristics with proofs.

## Baseline

- Repository / scope:
- Baseline commit / branch:
- Pre-existing working tree changes:
- Project instructions consulted:
- Optional modes: Comments [yes/no], Tests [yes/no], audit-only [yes/no]
- Commands and initial results:
- External contracts, security-sensitive and migration-sensitive areas:
- Explicit exclusions and assumptions:

## System/change map

| Area | Owner/entry point | Public contract | More-stable dependency | Main change reason | Relevant tests |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Decision D-001 - Title, status [proposed/active/verified/deferred]

**Root cause / change driver:**

**Design decision:**

**Alternative rejected and why:**

**Tradeoffs / behavior-preservation requirements:**

**Problems resolved** (specific evidence; one record per symptom):

| ID | Class (hidden/needless/surplus/special) | File:line / call chain | Why current change boundary is wrong | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| P-001 | | | | | |

**Necessary exceptions retained:**

**Implementation slices / affected files:**

**Verification required:**

**Verification observed** (commands, dates, before/after output):

**Result / remaining risk / owner:**

---

## Remaining candidates and blockers

| ID | Evidence or hypothesis | Impact | Why not changed | Verification or next safe action |
| --- | --- | --- | --- | --- |

## Final check

- [ ] Existing changes protected
- [ ] No unexplained behavior/API/permissions/data drift
- [ ] Narrow and broader checks executed or blockers recorded
- [ ] New dependency directions/cycles checked
- [ ] Agent reviews resolved or deferred with reasons
- [ ] No weakened test signal or undeclared skipped checks
- [ ] Handoff status accurately stated
