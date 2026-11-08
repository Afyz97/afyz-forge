---
name: codeweave
description: "Evidence-driven structural refactoring of existing codebases. Use only when explicitly asked to audit architecture, reduce coupling, simplify maintainability, or refactor a repository. Supports audit-only and full-refactor modes; preserves behavior and existing project conventions."
argument-hint: "[optional scope or concern] [--audit-only]"
disable-model-invocation: true
metadata:
  version: "1.0.1"
  category: "software-maintenance"
---

# CodeWeave

**Mission:** Make a repository easier for humans and coding agents to change, understand, and verify. Judge structure by **change reasons**, not by fewer files or prettier abstractions: code that must change together should be discoverable together; code with independent change reasons should be decoupled; code without a defensible purpose should be challenged.

This is a workflow for **existing projects**, not permission to rewrite from scratch, change requirements, or add frameworks. Prioritize low-risk, high-leverage changes backed by evidence. User instructions, repository rules, and project-specific safety constraints take precedence over this skill.

## Invocation and modes

- Default: **full refactor** within the user-selected scope; if none is specified, inspect the whole repository, then implement safe, prioritized slices rather than attempting an unreviewable wholesale rewrite.
- `--audit-only`: map and prioritize problems, create a decision log, and recommend actions **without modifying source code**. If the user requests no files changed, present the log in the response rather than writing it.
- If invocation is only a request to inspect or explain the codebase, use audit-only. Never infer permission for destructive code changes from a casual question.
- If given a specific area, inspect upstream/downstream dependencies enough to avoid local optimizations that hurt the whole system. Do not silently expand the mutation scope.

## 0. Establish choices and safety boundary

Before beginning a full refactor, offer the two optional additions using **these exact descriptions** and ask which to include:

| Addition | What it does |
| --- | --- |
| **Comments** | Remove comments that only restate the code. |
| **Tests** | Remove tests that wouldn't catch a real bug, and fix the ones that fail without one. |

Options: neither, Comments, Tests, both. Do not select on the user's behalf. If the environment cannot collect a response in an unattended run, default to **neither**, state that assumption, and proceed only within already-authorized refactor scope. Refactoring still requires **running, preserving, and where needed adding/adjusting regression tests**; the optional *Tests* addition specifically authorizes curation/removal of existing tests.

Before making edits:

1. Identify the repository root, Git branch, baseline commit, `git status --short`, current diff, and existing untracked/dirty files. Never discard, overwrite, stash, reset, commit, or rebase unrelated user work without authorization.
2. Read relevant project instructions (`AGENTS.md`, `CLAUDE.md`, nested rules) and relevant team knowledge. Where present, read only pertinent files in `.ai/agents/` (architecture, database, conventions, known-fixes and developer-owned subfolders). **Do not edit shared team knowledge** unless explicitly requested.
3. Determine entry points, public contracts, runtime, supported versions, migration/deployment constraints, data integrity, permissions, and integration boundaries. Treat auth, billing, payments, migrations, background jobs, and external APIs as high-risk.
4. Record reproducible *before* evidence: tests, typecheck/build/lint, representative workflows or API outputs, and relevant performance/SQL query behavior. Mark missing tooling, flaky tests, and existing failures separately. Never call a failing baseline green.
5. If substantial uncertainty or dangerous migrations make code edits unsafe, deliver an **audit with blockers** and the smallest safe next slice. Do not disguise incomplete work as completion.

## 1. Build a compact, navigable repository model

Map the codebase before reading everything. Prefer `git ls-files`, targeted file paths, signature/outline views, dependency queries, static analyzers already in the project, and small bounded excerpts. Ignore vendor/generated/build/cache files. Use bundled **read-only** scripts if useful:

```bash
python scripts/repo_audit.py --root . --format markdown
python scripts/git_cochange.py --root . --commits 200
```

Resolve `scripts/` relative to this installed skill directory, not the target repository (`${CLAUDE_PLUGIN_ROOT}/skills/codeweave/scripts/` when installed as a plugin). The reports are **leads, not verdicts**; inspect actual source before declaring a problem. Never paste entire repository files into context just to build the map.

Identify: feature/domain boundaries; import/dependency edges; dependency cycles; repeated decisions/business rules; state ownership and initialization order; copy/paste behavior; public vs private interfaces; oversized change hotspots; critical tests; database and event/queue contracts; co-change patterns in Git. Use the framework-aware guidance in [verification-and-frameworks.md](references/verification-and-frameworks.md).

## 2. Inventory before editing

Ask of each module, function, configuration item, test, and cross-module dependency: **Should these pieces need to change together?** Record exact `path:line`, evidence, impact, root cause, proposed verification, confidence, and risk in the decision log. Classify observations:

- **Hidden links:** duplicated business rules/constants; implicit global or file state; required call order; convention-only coupling; one feature scattered across unrelated layers; copied permissions/validation.
- **Needless links:** unstable internals exposed to callers; dependencies pointing toward more volatile code; a reusable function polluted with one workflow's terms; shallow modules whose interface mirrors their implementation.
- **Surplus:** unreferenced reachable-code candidates, pass-through wrappers, redundant layers, speculative configuration/extension points, repeated adapters. **Prove reachability/usage before removal**, accounting for reflection, DI registration, routing, templates, jobs, framework discovery and external consumers.
- **Special cases:** one-off branches, caller-specific parameters, swallowed exceptions, delays/retries, disabled/skipped tests, feature flags, vendor workarounds. Determine whether each is a real domain rule, boundary contract, operational safeguard, or an architectural symptom. **A valid explicit business exception is not automatically debt.**

Record findings first; no opportunistic edits while scanning. Group symptoms by **shared causes**. Use [decision-log-template.md](references/decision-log-template.md). If a claim lacks evidence, mark `hypothesis`, not `confirmed`.

## 3. Redesign from the actual change drivers

Create a concise target boundary model based on behavior and existing constraints, **not** arbitrary folder structure or fashionable patterns. For each proposed fix:

1. Describe the observed change driver(s) and desired single source of truth.
2. Show which findings this fix resolves and which independent concerns it separates.
3. Check direction: stable domain policy should not depend on change-prone UI, provider details, or infrastructure. Use a narrow interface **only when it removes real independent change pressure**; don't replace simple code with ceremonial indirection.
4. Compare minimal alteration vs larger restructure, including migration cost, readability for developers/agents, operational risk, regression detection, and expected maintenance benefit.
5. Write behavior-preserving acceptance criteria and an executable verification plan. Protect public APIs, persistence meaning, permissions, user-visible behavior and error semantics unless change is explicitly authorized.
6. Rank by risk-adjusted leverage: high-confidence root causes affecting multiple hotspots first; high-risk changes in carefully bounded slices.

For example, prefer centralizing a shared command definition over patching four disconnected switch statements; prefer an explicit boundary over creating a generic service layer for everything. If two concerns genuinely change together, colocation is good; don't split them merely to maximize files.

## 4. Execute in reversible, verified slices

Only in full-refactor mode:

1. Choose one coherent decision-log fix (or tightly related set). State affected interfaces and files; preserve the baseline and existing dirty changes.
2. Implement the **minimum coherent structural change**, updating all real callers, tests, registrations, authorization checks, data contracts, and operational wiring. Prefer existing conventions and dependencies; do not add packages merely for aesthetics.
3. Run narrow tests/checks, then the relevant broader checks. Compare with baseline; investigate new failures. Add characterization/regression tests where behavior is unprotected. For data changes, plan safe migrations and rollback before execution; **do not run destructive production operations**.
4. Verify real behavior at critical boundaries (request/response, database, UI, queues, permissions, CLI). Static checks alone do not prove behavior. Re-run dependency/coupling inspection as appropriate.
5. Update decision-log evidence, remaining hazards, and exact verification results. Keep edits reviewable and avoid mixing unrelated cleanup. Don't automatically commit or push.
6. Repeat on the next highest-leverage confirmed finding until the scoped, worthwhile work is exhausted or a blocker is reached.

**Comments option only:** Remove narration that merely paraphrases self-evident implementation. Keep comments about *external constraints*, security invariants, non-obvious domain reasons, compatibility promises, and why a necessary workaround exists. Do not delete a useful design rationale because it contains the word "why". Remove workaround comments only once the workaround is actually removed.

**Tests option only, and do it last:** Keep tests that detect observable regressions, including integration, security, edge-case, and boundary regressions. Replace implementation-mirroring and internal-detail tests with stronger behavior-based tests **before** removing the weak ones. Remove a test only after proving it is redundant/vacuous, documenting what now covers its risk. A disabled or intermittently failing test is a signal to investigate, not an automatic deletion candidate. Never silently weaken assertions or coverage to turn red into green.

## 5. Independent review, convergence, and handoff

Where agent delegation is supported, use separate **read-only** reviewers to inspect hidden links, needless links, surplus/special cases, and regression/security risk. Give each an explicit scope and require `path:line` evidence, alternatives, risk and confidence. Do not give multiple agents overlapping write access to the same files; the coordinating agent owns integration and verification. If subagents are unavailable, do focused sequential passes. See [review-protocol.md](references/review-protocol.md).

Re-scan changed boundaries and re-run relevant tests. **Convergence means** no remaining *confirmed, worthwhile* issue within the agreed scope that can be safely solved now; no newly introduced dependency cycles or unexplained behavior drift; and verification results explicitly reported. The number of special cases is a **diagnostic**, not a target: valid rules, performance safeguards, and compliance requirements may remain. Avoid churn, speculative abstraction, and endless cleanup loops.

Preferred project artifacts, **only if project conventions permit writing them**:

- `.ai/docs/plans/untangle-codebase-decision-log.md` for observed findings, grouped fixes, evidence, decisions and test commands.
- `.ai/docs/handoffs/untangle-codebase-handoff.md` only if work is blocked or continuing in another session.
- Never overwrite `.ai/agents/` knowledge, existing plans/handoffs, or developer-owned `known-fixes` files merely to record this run.

Final response must state: initial Git state/scope, options chosen, root causes fixed and files changed, verification commands with pass/fail/blocked status, remaining validated findings or blockers, and whether behavior parity was established. Say **partial** when work cannot be proved complete. Do not claim "all fixed" without evidence.
