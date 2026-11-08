---
name: distributed-patterns
description: >-
  Explains and chooses between distributed-systems mechanisms, with trade-offs and defaults:
  rate limiting (token bucket, leaky bucket, sliding window), caching and CDN, sharding,
  consistent hashing, replication, CAP, quorum (N/W/R), vector clocks, gossip, Merkle trees,
  Raft, unique IDs (Snowflake, UUID, base62), Bloom filters, message queues (partitions,
  consumer groups, acks, at-least-once vs exactly-once, DLQ), stream windows and watermarks,
  idempotency keys, optimistic vs pessimistic locking, 2PC, TC/C, sagas, event sourcing,
  CQRS, double-entry ledgers, reconciliation, LSM trees, erasure coding, geohash, quadtree,
  WebSocket vs long polling vs SSE, presence. Use for "which rate limiting algorithm",
  "how do I stop double booking or double charging", "exactly-once", "how to shard X",
  "saga or 2PC", "how does consistent hashing work", "pick a pub/sub or queue design". Not for
  designing a whole system (system-design) or reviewing one (system-design-review).
---

# Distributed patterns

Answer the mechanism question directly: what it is, when to use it, the default choice, the
trade-off, and the failure mode. Then show it applied to the user's case. If the user is in a
codebase, ground the answer in their stack (for Laravel, see
`../system-design/references/stack-mapping.md`).

## Which reference to open

| Question is about | Open |
|---|---|
| Load balancing, rate limiting, caching, CDN, stateless tiers | `references/traffic-and-caching.md` |
| Sharding, consistent hashing, replication, CAP, quorum, conflicts, failure detection, consensus | `references/partitioning-and-replication.md` |
| Unique IDs, short codes, content hashing, Bloom filters, dedupe | `references/ids-and-hashing.md` |
| Queues, pub/sub, delivery semantics, retries, DLQ, stream processing, windows, watermarks | `references/messaging-and-streaming.md` |
| Idempotency, locking, overselling, distributed transactions, sagas, event sourcing, ledgers, reconciliation | `references/transactions-and-money.md` |
| Storage engines, WAL, LSM, object vs block vs file, erasure coding, time-series, compaction | `references/storage-engines.md` |
| Geospatial indexes, maps tiles, real-time push, WebSocket, presence, pub/sub fan-out | `references/geo-and-realtime.md` |

## Defaults when nothing argues otherwise

- **Rate limiting:** token bucket per user or key, counters in Redis updated atomically, `429` with
  a retry-after header.
- **Cache:** cache-aside with TTL; on write, update the DB then delete the cache key.
- **Sharding key:** the ID that the main query filters on and that spreads load evenly; consistent
  hashing with virtual nodes for placement.
- **Replication:** single leader with async followers for reads; read-your-writes from the leader
  where it matters; consensus (Raft) only for small critical metadata or money logs.
- **Quorum:** N=3, W=2, R=2 when strong consistency is needed.
- **IDs:** time-sortable IDs (Snowflake for 64-bit integers; ULID or UUIDv7 if 128-bit is fine).
- **Queue semantics:** at-least-once delivery plus idempotent consumers. Exactly-once is
  at-least-once + dedupe, not a magic transport setting.
- **Retries:** exponential backoff with jitter, capped attempts, then a dead-letter queue.
- **Concurrency on contended rows:** optimistic locking or a DB constraint when conflicts are rare;
  pessimistic locks for short, highly contended critical sections; a queue per hot item when
  contention is extreme.
- **Cross-service consistency:** first try to keep the invariant inside one database transaction.
  If you cannot, prefer an orchestrated saga; use TC/C when steps must run in parallel; avoid 2PC
  across services.
- **Money:** integer minor units or decimal strings; idempotency keys; double-entry ledger;
  scheduled reconciliation.
- **Server push:** WebSocket; long polling as fallback; SSE when one-way is enough.
- **Geo search:** geohash cells plus neighbours; quadtree when density varies wildly or you need
  k-nearest.

## Answer shape

1. One-paragraph answer with the recommended option for the user's situation.
2. A small comparison table when there are 2+ real options.
3. The failure mode to guard against and how to detect it (metric or alert).
4. A minimal code or schema sketch in the user's language when it helps (SQL, Redis commands,
   pseudo-code). Keep it short.
