---
name: system-design
description: >-
  Designs scalable backend systems end to end: a 4-step method (scope and estimate,
  high-level design, deep dive, wrap-up), back-of-the-envelope math, a scale-from-one-server
  ladder and 22 worked blueprints (URL shortener, crawler, notifications, news feed, chat,
  autocomplete, video, file sync, proximity search, nearby friends, maps, message queue,
  metrics, ad-click aggregation, hotel booking, email, object storage, leaderboard, payments,
  wallet, stock exchange). Use for "design X", "how would you architect or scale this",
  "system design interview", "write a design doc or RFC", "estimate QPS, storage or servers",
  "will this handle 1M users", or picking databases, caches, queues and sharding for a new
  service or feature. Not for one mechanism in isolation (distributed-patterns), reviewing an
  existing architecture (system-design-review), or UI layout design.
---

# System Design

## Stance

- Requirements before boxes, numbers before technology. A component earns its place by
  pointing at a requirement or an estimate.
- Start from the simplest design that meets today's numbers, then say what breaks at 10x and
  what you would change. Over-building is a failure, not a bonus.
- Every choice is a trade-off. State the option you rejected and why, in one line.
- Name the hard part early. Most systems have one or two places where the design is actually
  difficult (the crux); spend the depth there, not on the login page.

## Pick the mode

| Mode | When | Output |
|---|---|---|
| **Interview** | "system design interview", practising, whiteboard-style question | Spoken-style walkthrough on a time budget, ends with a recap |
| **Build** | A real product, codebase or RFC | Design doc (template below), fitted to the existing stack |

In **build mode**, read before designing: the dependency manifest (`composer.json`,
`package.json`), database and queue config, existing migrations and any infra files. Reuse what
is already running (for example MySQL + Redis + a queue worker) unless a number proves it
cannot cope. For Laravel projects, map each component with `references/stack-mapping.md`.

## The method

### Step 1 - Scope and estimate (about 15% of the time)

Ask, then write the answers down as numbered assumptions. Never design on a guess you did not
state.

- **Users and features:** who uses it, the 3 must-have use cases, what is explicitly out of
  scope, web/mobile/both.
- **Scale:** DAU or MAU, actions per user per day, read:write ratio, peak factor, growth rate,
  data size per item, retention period.
- **Quality targets:** latency (p99, not average, where users wait), availability (in nines),
  durability, consistency (can a user see stale data? can money or stock go wrong?), ordering.
- **Constraints:** existing stack, third parties (payment providers, push services), budget,
  compliance (PII, card data, data residency).

Then estimate QPS, peak QPS, storage over the retention period, bandwidth and cache memory
using `references/estimation.md`. It also lists calibration numbers from all 22 blueprints so
you can sanity-check results.

### Step 2 - High-level design (about 30%)

1. **API:** the 2-5 core endpoints with method, path, key params and response. Any write that
   moves money, stock or seats carries an idempotency key.
2. **Data model:** the main entities and the queries they must serve. Choose storage from the
   access pattern (table below), not from habit.
3. **Diagram:** boxes and arrows (ASCII or Mermaid). Draw the **write path** and the **read
   path** separately; they usually scale differently.
4. **Walk one request** through each path, numbered step by step.
5. **Checkpoint:** in interview mode, confirm direction before going deeper; in build mode,
   show the high-level design to the user before writing the deep dive.

### Step 3 - Deep dive (about 40%)

Pick the 2-3 cruxes (the case files name them for each problem type). For each one: options,
trade-offs, the choice, and the number or requirement that decided it. Typical cruxes:
fan-out strategy, hot keys, ordering, exactly-once and double-spend, geo lookups, real-time
delivery to stateful connections, and storage layout for huge write volumes.

### Step 4 - Wrap-up (about 15%)

- Bottlenecks and the first thing to break as traffic grows 10x.
- A failure walk: for each stateful component, what happens when it dies and how it recovers.
- Monitoring: the 3-5 metrics and alerts that would page someone (queue lag, p99, error rate,
  reconciliation mismatches, cache hit rate).
- Open questions and deliberate simplifications.

## Choose storage from the access pattern

| Access pattern | Default choice | Seen in |
|---|---|---|
| Transactions, clear relations, money or inventory | Relational (MySQL, PostgreSQL) with ACID | hotel, payment |
| Read-heavy, modest size, rarely changes | Relational + read replicas + cache | proximity, URL shortener |
| Massive append-only writes, read by key in time order | Wide-column (Cassandra-style): partition key + clustering key | chat history, location history, ad clicks, email |
| Hot, short-lived state; counters; TTL; rankings | In-memory store (Redis): TTL, INCR, sorted sets, pub/sub | rate limiter, nearby friends, leaderboard |
| Measurements over time with labels | Time-series DB with downsampling | metrics and alerting |
| Large binary files | Object storage + metadata DB, served through a CDN | video, file sync, email attachments |
| Full-text search | Search index, updated asynchronously from the source of truth | email search |
| Config, membership, leader election | Coordination service (ZooKeeper, etcd) | message queue, Redis pub/sub cluster |
| Event or message streams, replayable | Partitioned log (Kafka-style) | metrics pipeline, ad clicks, wallet commands |
| Relationship traversal | Graph store, or adjacency tables plus cache | friend lists for feed fan-out |

## Signal -> pattern

When you see the signal on the left, reach for the pattern, then read the linked reference in
the `distributed-patterns` skill (`../distributed-patterns/references/`).

| Signal in the requirements | Pattern | Reference |
|---|---|---|
| Reads far outnumber writes | Cache-aside + read replicas + CDN for static files | traffic-and-caching.md |
| Abuse, cost control, fairness | Rate limiter at the gateway (token bucket by default) | traffic-and-caching.md |
| Data no longer fits on one node | Shard on a key that spreads evenly; consistent hashing with virtual nodes | partitioning-and-replication.md |
| One key is far hotter than the rest | Split the hot key, give it its own shard, or switch it from push to pull | partitioning-and-replication.md |
| Unique, time-sortable IDs across many servers | Snowflake-style 64-bit IDs | ids-and-hashing.md |
| Slow or flaky downstream (email, SMS, PSP, transcoding) | Queue + workers + retry with backoff + dead-letter queue | messaging-and-streaming.md |
| Counting or ranking over time windows | Stream aggregation with event time, watermarks, reconciliation | messaging-and-streaming.md |
| Double clicks, retries, double booking, double charge | Idempotency key + unique constraint + optimistic lock or DB constraint | transactions-and-money.md |
| A transaction spans services or shards | Keep it in one DB if you can; otherwise TC/C or saga | transactions-and-money.md |
| Audit, replay, "prove the balance" | Event sourcing + double-entry ledger + reconciliation | transactions-and-money.md |
| Server must push to clients | WebSocket on a stateful tier + service discovery; long polling as fallback | geo-and-realtime.md |
| "Near me" queries | Geohash or quadtree index; cache by cell, not by raw coordinates | geo-and-realtime.md |
| Huge write volume on disk | Append-only log, LSM tree, batching | storage-engines.md |
| Cheap durable storage at petabyte scale | Erasure coding, cold tiers, dedupe | storage-engines.md |

## Blueprint index

Read only the file that matches the problem. Each blueprint gives scope and numbers, API, data
model, flows, the crux and its options, and how it scales and fails.

| Problem looks like | File | Crux in one line |
|---|---|---|
| URL shortener, paste bin, link tracker | `references/cases/web-services.md` | Base62 of a unique ID vs hash + collision check; 301 vs 302 |
| Web crawler, scraper, link checker | `references/cases/web-services.md` | URL frontier: priority queues in front, per-host politeness queues behind |
| Notifications (push, SMS, email) | `references/cases/web-services.md` | Queue per channel, retries, dedupe by event ID, opt-out settings |
| Typeahead, autocomplete | `references/cases/web-services.md` | Trie with top-k cached per node, rebuilt offline from logs |
| News feed, timeline | `references/cases/social-realtime.md` | Fan-out on write for most, on read for celebrities |
| Chat, messaging, presence | `references/cases/social-realtime.md` | Stateful WebSocket tier, per-channel sequence IDs, multi-device sync |
| Live location of friends | `references/cases/social-realtime.md` | Pub/sub channel per user, fan-out only to nearby online friends |
| Leaderboard, ranking | `references/cases/social-realtime.md` | Sorted set; sharding ranks by score range |
| Video upload and streaming | `references/cases/media-storage.md` | Transcoding DAG, chunked resumable uploads, CDN cost control |
| File sync (Drive, Dropbox) | `references/cases/media-storage.md` | Block-level delta sync, dedupe, conflict handling |
| Object storage (S3-like) | `references/cases/media-storage.md` | Separate metadata from data; replication vs erasure coding |
| Email service | `references/cases/media-storage.md` | Per-user partitioning, async search indexing, deliverability |
| Nearby places search | `references/cases/geo.md` | Geohash vs quadtree vs S2; search the cell plus its 8 neighbours |
| Maps, routing, ETA | `references/cases/geo.md` | Pre-rendered tiles on a CDN; hierarchical routing tiles |
| Message queue, event bus | `references/cases/data-infra.md` | Partitioned append-only log, consumer groups, ISR and acks |
| Metrics, monitoring, alerting | `references/cases/data-infra.md` | Time-series DB, pull vs push collection, downsampling |
| Click or event aggregation, analytics | `references/cases/data-infra.md` | Event time + watermarks, exactly-once, end-of-day reconciliation |
| Key-value store, rate limiter, ID generator, consistent hashing | `references/cases/data-infra.md` | Building blocks: quorum, vector clocks, Snowflake, token bucket |
| Hotel, flight, ticket booking | `references/cases/money-and-booking.md` | Inventory rows per day; idempotent reserve; optimistic locking |
| Payments, checkout | `references/cases/money-and-booking.md` | PSP hosted page, idempotency, ledger, reconciliation |
| Digital wallet, balances | `references/cases/money-and-booking.md` | Event sourcing + Raft + TC/C or saga across shards |
| Exchange, order matching | `references/cases/money-and-booking.md` | Single-threaded deterministic matching behind a sequencer |

New problem not in the list? Find the closest blueprint by its crux (for example a ride-hailing
service is nearby friends + proximity + payments) and combine.

## Scale ladder

For "how do we get from one server to millions of users", follow `references/scaling-ladder.md`.
It orders the moves (split DB, replicate, cache, CDN, stateless web tier, queue, multi-DC,
shard) and gives the signal that justifies each one, so you never add the next rung early.

## Design doc template (build mode)

```
# <System> design
## 1. Context and goals        - problem, users, the 3 use cases, non-goals
## 2. Requirements             - functional; non-functional with numbers (latency p99, availability, consistency)
## 3. Estimates                - assumptions list, QPS/peak, storage/retention, bandwidth, cache
## 4. API                      - endpoints, idempotency, auth, rate limits
## 5. Data model               - entities, keys, indexes, partitioning, chosen store and why
## 6. Architecture             - diagram, write path, read path, numbered request walk
## 7. Deep dives               - each crux: options, trade-offs, decision, deciding number
## 8. Failure modes            - per component: impact, detection, recovery
## 9. Scaling plan             - first bottleneck, what changes at 10x and 100x
## 10. Observability           - metrics, alerts, reconciliation jobs, dashboards
## 11. Security and compliance - authz, PII, secrets, abuse controls
## 12. Open questions and simplifications
```

In interview mode, compress the same order into speech and finish with a 4-line recap: the
design in a sentence, the crux and the choice, the biggest risk, and what you would do next.

## Mistakes to avoid

- Designing before scoping, or scoping without numbers.
- One diagram that mixes the write and read paths so neither can be reasoned about.
- "Use Kafka/microservices/Kubernetes" without a number that needs it.
- Averages instead of peaks; ignoring replication factor in storage estimates.
- Floating-point money, missing idempotency on payment or booking writes, cache as the source
  of truth for balances or stock.
- Picking a shard key that makes the main query fan out to every shard.
- A single coordinator, load balancer, cache node or database with no failover story.
- Silent stateful servers (sessions or uploads on local disk) behind a load balancer.
