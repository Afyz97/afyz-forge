# Messaging and stream processing

## Why a queue

Decouples producers from consumers so each side scales, deploys and fails on its own; absorbs
bursts; lets producers return without waiting. Typical first uses: notifications, media
processing, calls to slow third parties, fan-out of one event to many services.

## Models

- **Point-to-point:** each message is processed by one consumer, then removed (classic job
  queues: RabbitMQ, SQS, Laravel queues).
- **Publish-subscribe:** every subscriber group gets every message on a topic (Kafka-style logs,
  Redis pub/sub, SNS).
- A **partitioned log** with consumer groups does both: one group = point-to-point, several groups =
  pub/sub, and messages stay for a retention period so they can be replayed.

## Partitioned log essentials

- **Topic -> partitions -> brokers.** Partition by `hash(key) % partitions`; same key -> same
  partition -> ordered. Choose the key for the ordering you need (`user_id`, `ad_id`, `account_id`).
- **Offsets:** a consumer group tracks its position per partition; restart resumes there.
- **Parallelism:** at most one consumer per partition per group. Create enough partitions up front.
- **Rebalancing:** consumers join or leave -> a coordinator reassigns partitions. Large groups
  rebalance slowly; schedule big changes off-peak.
- **Pull vs push:** pull lets consumers control their pace and batch; push lowers latency but can
  overwhelm slow consumers. Logs use pull with long polling.
- **Batching:** bigger batches = more throughput, more latency. Tune per use case.
- **Replication:** leader per partition, followers pull; **ISR** = followers caught up within a
  lag bound. `acks=all` (durable, slow), `acks=1` (leader only), `acks=0` (may lose). Combine with a
  minimum ISR count.
- **Storage:** append-only segments on disk, sequential I/O, OS page cache; retention by time or size.

## Delivery semantics

| Semantics | Producer | Consumer | Result |
|---|---|---|---|
| At-most-once | No retry (`acks=0`) | Commit offset, then process | May lose; never duplicates. OK for metrics |
| **At-least-once** | Retry until acked (`acks=1/all`) | Process, then commit offset | Never loses; may duplicate. The default |
| Exactly-once | Idempotent producer + transactions | Commit offset atomically with the output, or idempotent output | Costly; needed for billing and money |

Practical exactly-once = **at-least-once + idempotent processing**: dedupe on a message or event ID,
use upserts keyed by a natural ID, or store the consumed offset in the same transaction as the
result.

## Failure handling

- **Retries:** exponential backoff (double the wait each time), with jitter, capped attempts;
  honour `Retry-After` from providers.
- **Retry topic or queue:** move failing messages aside so they do not block the partition.
- **Dead-letter queue:** terminal failures land here for inspection and manual replay. Alert when
  it grows.
- **Poison messages:** malformed input that will never succeed goes straight to the DLQ.
- **Monitoring:** queue depth or consumer lag (for logs, lag in records), processing latency, error
  rate. Scale consumers on lag.
- **Delayed or scheduled messages:** park in internal delay topics or a timing wheel, then release
  (for example "check this payment's status in 30 minutes").
- **Filtering:** tags on messages that brokers filter on beat creating one topic per consumer need.

## Stream processing (aggregation over unbounded data)

**Online vs batch vs streaming:** services answer requests (latency); batch jobs process bounded
input (throughput, e.g. MapReduce); streams process unbounded input continuously (throughput and
latency, e.g. Flink).

**Lambda vs kappa:** lambda runs a batch path and a stream path side by side (two codebases).
Kappa uses one streaming path and recomputes history by replaying raw events through it. Prefer
kappa when the stream engine can handle replays.

**Event time vs processing time**

| | Event time (when it happened) | Processing time (when we saw it) |
|---|---|---|
| Accuracy | Correct bucket | Wrong bucket for late events |
| Risk | Client clocks can be wrong or forged | Server clock is trustworthy |

Use event time when results matter (billing), and handle lateness with **watermarks**: keep each
window open for an extra allowance. Longer allowance = fewer dropped events, more latency. Events
later than that are fixed by **reconciliation** (a batch job recomputing from raw data, typically
end of day).

**Window types:** tumbling (fixed, non-overlapping: per-minute counts), hopping (fixed, overlapping
by a hop), sliding (continuous "last M minutes": top-N), session (gap-based per user activity).

**MapReduce-style DAG:** map (read, clean, route by key) -> aggregate (count in memory per key per
window) -> reduce (merge partial results, e.g. top-N heaps).

**Pre-aggregation for filters (star schema):** precompute counts per dimension value (country,
device) so filtered queries become lookups; cost is more rows.

**State and recovery:** in-memory aggregation state is lost with the node; periodically snapshot
state together with the input offset it covers; a replacement loads the snapshot and replays from
that offset.

**Hot keys:** a popular key overloads one node; split its events over extra nodes and merge
(global-local aggregation), or split distinct-counts.

**Keep raw and aggregated data:** raw for debugging, backfills and recomputation (cold storage);
aggregates for fast queries.

## Metrics pipeline notes

- Pull collection (scrape `/metrics`) vs push (agents send to a collector): pull is easier to debug
  and doubles as a health check; push suits short-lived jobs and complex networks. Big orgs support both.
- Put a log between collectors and the time-series DB to survive DB outages.
- Aggregate at the agent (cheap), in the pipeline (fewer writes, lose raw), or at query time (exact,
  slower).
- Keep label cardinality low.
