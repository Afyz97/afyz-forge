---
name: system-design-review
description: >-
  Reviews an existing architecture, design doc, RFC, diagram or backend codebase for
  scalability, reliability and correctness risks, and returns severity-ranked findings
  (Critical/High/Medium/Low) with evidence, the failure scenario, a fix and the first
  bottleneck. Covers single points of failure, stateful servers behind load balancers, missing
  caching or replicas, sync calls to slow third parties, missing retries/backoff/DLQ,
  non-idempotent payment or booking endpoints, race conditions on stock or balances, float
  money, missing rate limits, bad shard keys, hot keys, missing reconciliation and
  observability gaps. Use for "review my architecture/design doc", "will this scale",
  "what breaks at 10x", "find bottlenecks", "production readiness review", "is this safe
  under load", including Laravel apps (queues, sessions, locks, Horizon). Not for designing a
  new system from scratch (system-design) or UI/code-style reviews.
---

# System design review

Find what will break, in what order, and how to fix it. Evidence over opinion: every finding
points at a line in the doc or a file:line in the code.

## Workflow

1. **Collect.** Read what exists: the design doc or diagram, or in a codebase the dependency
   manifest, `.env.example` and config (database, cache, queue, session, filesystem, broadcasting),
   migrations, routes, controllers or handlers on hot paths, jobs and listeners, scheduler, infra
   files. Note what you could not see.
2. **Model the load.** Restate the top 3 flows (write path and read path). Get or assume the numbers
   (DAU, peak QPS, data growth, read:write) and run a quick estimate with
   `../system-design/references/estimation.md`. Mark assumptions as such.
3. **Walk the checklist** below, flow by flow. For each component also ask: what happens when it is
   slow, when it is down, and when traffic is 10x?
4. **Find the first bottleneck**: the component that saturates first as load grows, with the number
   that says so.
5. **Report** in the format at the end. Rank by severity, then by effort. Do not pad with Low items.

## Severity

| Level | Meaning |
|---|---|
| **Critical** | Data loss, money or stock errors, security hole, or an outage under expected load |
| **High** | Outage or severe degradation under plausible peak or a single failure |
| **Medium** | Degradation, painful operations, or a scaling wall within ~10x growth |
| **Low** | Hygiene and hardening worth scheduling |

## Checklist

**Redundancy and failure**
- Any single instance of: load balancer, database primary without failover, cache node, queue
  broker, coordinator, cron host, WebSocket node?
- Timeouts on every outbound call? Retries with backoff and a cap? Circuit breaking or fallback for
  flaky dependencies?
- Health checks, graceful shutdown, connection draining for stateful servers?
- Backups exist *and* restores are tested; replication across zones or regions where the
  availability target needs it.

**State in the wrong place**
- Sessions, uploads or caches on local disk or in process memory behind a load balancer
  (Laravel: `SESSION_DRIVER=file`, `CACHE_STORE=file|array`, `FILESYSTEM_DISK=local` for user files).
- Scheduled jobs that run on every server instead of once (`->onOneServer()` missing).
- The cache treated as the source of truth for balances, stock or anything that must not be lost.

**Data tier**
- Hot queries without supporting indexes; N+1 queries on list endpoints; unbounded result sets
  without pagination.
- Read-heavy load with no cache or replicas; reads-after-writes served from lagging replicas.
- Growing tables with no retention or archival plan.
- Shard key that forces scatter-gather for the main query, or one tenant/user/item that is a hot key.
- Store mismatched to access pattern (heavy append logs or events in a relational table that is also
  serving OLTP; time series in a generic table).

**Async work**
- Slow or third-party calls (email, SMS, PSP, image/video processing, webhooks out) done inside the
  request (Laravel: `QUEUE_CONNECTION=sync`, `Mail::send` instead of queued mail, `Http::` calls in
  controllers).
- Jobs without retries/backoff, without a dead-letter path (`failed_jobs`) or alerting on it.
- Consumers that are not idempotent although delivery is at-least-once.
- Jobs dispatched inside a DB transaction before commit (workers see missing rows).
- No monitoring of queue depth or consumer lag.

**Correctness (money, inventory, bookings)**
- Write endpoints without an idempotency key and unique constraint (double click, client retry,
  webhook redelivery).
- Check-then-update races on stock, seats or balances without optimistic locking, row locks or a DB
  constraint.
- Money as float/double; currency missing; rounding done ad hoc.
- Cross-service writes with no saga/compensation and no reconciliation.
- Trusting browser redirects over provider webhooks for payment status.
- No ledger or audit trail for balance changes.

**Abuse and security at scale**
- No rate limits on login, signup, OTP, password reset, search, export or other expensive endpoints.
- Clients able to write values the server should compute (scores, prices, balances).
- Large uploads streamed through app servers instead of pre-signed direct uploads.
- PII and card data handling: stored where it should be tokenised; logs leaking secrets.

**Real-time**
- Polling where push is needed, or WebSockets with no reconnection/resync strategy.
- One stateful node holding all connections; no plan for draining or presence fan-out limits.

**Observability and operations**
- No p95/p99 latency, error-rate, saturation or queue-lag metrics; no alerts that page.
- No reconciliation job for money or billing aggregates.
- No load test or capacity number for the first bottleneck.
- Deploys that need downtime; schema migrations that lock big tables.

For each finding, name the pattern that fixes it and point to the reference in
`../distributed-patterns/references/` (traffic-and-caching, partitioning-and-replication,
ids-and-hashing, messaging-and-streaming, transactions-and-money, storage-engines,
geo-and-realtime). For Laravel fixes use `../system-design/references/stack-mapping.md`.

## Report format

```
## Summary
<2-3 sentences: overall risk, the first bottleneck and the number behind it>

## Load model
<assumptions and estimates; mark guesses>

## Findings
| # | Severity | Area | Evidence | What goes wrong | Fix | Ref |
|---|----------|------|----------|-----------------|-----|-----|
| 1 | Critical | Payments | app/Http/Controllers/CheckoutController.php:42 | Double click charges twice: no idempotency key | Client-generated key + unique index; return stored result | transactions-and-money.md |

## What breaks first as traffic grows
1x -> ... ; 10x -> ... ; 100x -> ...

## Top 3 fixes
<ordered by risk removed per unit of effort>

## Not reviewed
<files, systems or numbers you could not see>
```

Keep severities honest: a finding is Critical only if the failure scenario is concrete and
plausible under the stated load. If something looks risky but the evidence is missing, list it
under "Not reviewed" or as a question, not as a finding.
