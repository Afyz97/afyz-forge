# Independent Review Protocol

The coordinator assigns **independent read-only** reviews after the inventory and again after implementation where helpful. Agents are optional; a single agent may do each review sequentially.

## Suggested roles

| Role | Inspect | Return |
| --- | --- | --- |
| Boundary archaeologist | Feature slices, ownership, duplicate rules, implicit globals and sequencing | Confirmed hidden links with call chains and changed-together evidence |
| Dependency reviewer | Import direction, cycles, leaky abstractions, providers, stability assumptions | Needless links and a small boundary proposal |
| Simplification reviewer | Dead-path hypotheses, wrapper churn, speculative flags, special cases | Reachability evidence, legitimate exceptions, safe deletions only |
| Regression reviewer | Tests, externally visible behavior, access control, schema, jobs and compatibility | Missing behavior checks, risk-ranked failures and counterexamples |

## Review request template

"Audit `[scope]` in read-only mode. Identify only high-confidence examples of `[category]`. Include exact `file:line`, actual dependency/call path, why the pieces have different/same change drivers, and possible minimal fix. Distinguish assumptions from confirmed findings. Report real domain exceptions and reasons to **retain** them. Do not edit or propose broad rewrites without proof."

## Resolution rules

- Merge duplicate observations under one design decision; do not count them as separate root causes.
- Reject findings contradicted by runtime entry points, dynamic dispatch, jobs, route discovery, tests or deployment constraints.
- Escalate risk when changing auth, payment, data schema, migrations, concurrency or external contracts.
- Resolve disagreement with code/test evidence; do not choose the most confident agent's opinion.
- Parallelize **inspection**, not overlapping edits. Coordinator holds the file ownership list and is responsible for integration.
- Stop once remaining observations are low-confidence, expected domain rules, out of scope, or not worth risk/cost; document them rather than forcing zero findings.
