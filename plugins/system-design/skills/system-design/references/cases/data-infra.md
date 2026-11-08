# Blueprints: data infrastructure

Distributed message queue, metrics monitoring and alerting, ad-click event aggregation, and the
four building-block designs (key-value store, rate limiter, unique ID generator, consistent
hashing). Mechanism details are in `../../../distributed-patterns/references/`.

---

## Distributed message queue (Kafka-like)

**Scope:** producers send, consumers receive; messages of a few KB; repeated consumption by
different consumer groups; ordering preserved; 2-week retention; configurable delivery
semantics; tunable for throughput or latency; persistent and replicated.

**Model:** topics split into **partitions** hosted on **brokers**. A message lands in a partition
by `hash(key) % partitions` (or producer override); ordering holds within a partition; a
message's position is its **offset**. **Consumer groups** each keep their own offsets; inside a
group, a partition is read by at most one consumer (so consumers per group <= partitions).
Point-to-point semantics = one group; pub/sub = many groups.

**Components:** clients; brokers (partitions and replicas); data storage; state storage
(consumer offsets: small, frequent random read/write, consistent); metadata storage (topic
config: small, rarely changes, consistent); coordination service (ZooKeeper/etcd: broker
membership, controller election).

**Crux 1 - storage:** messages are append-only, read sequentially, never updated. A database
handles mixed heavy read/write poorly; use a **write-ahead log per partition**, split into
segments (only the newest is writable; old ones are read-only and deleted by retention).
Sequential disk I/O is fast even on spinning disks, and the OS page cache serves recent reads.
Keep one immutable message format from producer through broker to consumer so nothing is copied
or re-encoded. Message fields: key, value, topic, partition, offset, timestamp, size, CRC.

**Crux 2 - batching:** batch in producer, broker and consumer. Bigger batches = higher
throughput and latency; for latency-sensitive use, small batches and more partitions.

**Producer:** embed routing in the client library (no extra hop) - it caches the partition
leader map, buffers and batches, and sends to the **leader replica**.
**Consumer:** **pull** (consumer controls its rate, batches aggressively; long polling hides
empty fetches) rather than push (broker would overwhelm slow consumers). The group coordinator
(a broker found by hashing the group name) tracks membership via heartbeats; on join, leave or
missed heartbeats it triggers a **rebalance**: a group leader computes the partition assignment
(round-robin, range) and the coordinator broadcasts it.

**Replication:** each partition has a leader and followers that pull from it. **In-sync replicas
(ISR)** are followers within a configured lag. A message is committed once every ISR member has it.
- `acks=all`: wait for all ISR, safest, slowest.
- `acks=1`: leader only; lost if the leader dies before followers copy.
- `acks=0`: fire and forget; fastest, may lose data.
Spread replicas across brokers and racks or DCs; consumers read from the leader (or a nearby ISR).

**Scaling:** producers and groups scale freely; adding partitions affects only new messages;
removing a partition keeps it readable until retention expires, then rebalances. When adding a
broker, temporarily over-replicate, then drop the extra replica once the new one is in sync.

**Delivery semantics:** at-most-once (commit offset, then process; producer does not retry),
at-least-once (process, then commit; retries may duplicate), exactly-once (idempotent producer +
transactional processing; expensive). See messaging-and-streaming.md.

**Extras:** tag-based filtering at the broker; delayed or scheduled messages via internal delay
topics or a hierarchical timing wheel; retry topics and DLQs; archiving old segments to object
storage; protocols (AMQP, Kafka's binary protocol).

---

## Metrics monitoring and alerting

**Scope:** internal operational metrics (CPU, memory, disk, request rates, queue sizes) for 1,000
pools x 100 hosts x ~100 metrics -> ~10M series; 1-year retention (raw 7 days, 1-minute rollups 30
days, 1-hour rollups after); alerts to email, phone, PagerDuty, webhooks. Logs and tracing are out
of scope. Scalable, low query latency, reliable alerting, flexible.

**Data model:** time series identified by metric name + labels (`cpu.load host=web01
region=us-west`), with (timestamp, value) points; line-protocol format. Write-heavy and constant;
reads are bursty (dashboards, incidents). **Keep label cardinality low** (never a label per user or
request ID).

**Components:** metric sources -> collectors -> (queue) -> time-series DB -> query service ->
alerting and visualisation.

**Crux 1 - pull vs push collection:**

| | Pull (Prometheus-style) | Push (CloudWatch/Graphite-style) |
|---|---|---|
| Debugging | Hit `/metrics` on any host by hand | Missing data could be network or agent |
| Health | No scrape response = host is down | Ambiguous |
| Short-lived jobs | Miss them (need a push gateway) | Fine |
| Complex networks | Collector must reach every host | Hosts reach a load-balanced collector |
| Authenticity | Only configured targets | Must authenticate or allowlist senders |

Large orgs end up supporting both. Pull needs service discovery (etcd/ZooKeeper) for targets and
consistent hashing so each target has exactly one collector. Push uses local agents that can
pre-aggregate, and an autoscaled collector fleet behind a load balancer.

**Crux 2 - pipeline:** put a partitioned log between collectors and the DB so a DB outage does not
lose data; partition by metric name (and labels for scale); stream processors (Flink/Spark)
consume and write. Aggregation can happen in the agent (cheap, simple), in the pipeline (fewer
writes, raw detail lost) or at query time (exact but slower).

**Storage:** use a purpose-built time-series DB (InfluxDB, Prometheus, Timestream); general SQL is
awkward for rolling-window queries and NoSQL schemas for time series are hard to get right. Most
queries (~85% in one large study) hit the last 26 hours, so favour recent data in memory. Delta
encoding and compression shrink storage; **downsample** with age (7d raw, 30d at 1 min, 1y at 1 h);
move old data to cold storage.

**Query service:** optional abstraction plus cache; often dashboards and alerting talk to the DB
directly. Time-series query languages beat SQL for this.

**Alerting:** rules (YAML) loaded into cache -> alert manager evaluates queries on an interval ->
fires alert events that are filtered, merged and deduplicated -> alert state stored (key-value) so
each alert is delivered at least once -> published to a queue -> consumers send to channels.
Restrict who can edit rules. Buy before building: Grafana for dashboards, existing alert managers.

---

## Ad-click event aggregation

**Scope:** 1B clicks/day across 2M ads, growing 30% a year; per-ad click counts for the last M
minutes; top N ads in the last M minutes (N, M configurable, refreshed every minute); filter by IP,
user, country. Results feed billing and real-time bidding, so **correctness** matters; a few
minutes of end-to-end latency is fine. Handle late and duplicate events and partial failures.
**Numbers:** ~10k QPS (peak 50k); 0.1 KB per event -> 100 GB/day, ~3 TB/month.

**API:** `GET /v1/ads/{ad_id}/aggregated_count?from=&to=&filter=`;
`GET /v1/ads/popular_ads?count=&window=&filter=`.

**Data:** keep **both raw events** (source of truth for debugging, backfill and recalculation;
cold storage) **and aggregates** (small and fast for queries): `(ad_id, click_minute, filter_id,
count)` and `(window_size, update_time_minute, most_clicked_ads)`. Both are write-heavy;
a wide-column store suits both (or columnar files on object storage for raw).

**Architecture:** log watcher -> **queue 1** (raw events) -> **aggregation service** -> **queue 2**
(minute counts and top-N) -> DB writer -> aggregation DB -> query service. Raw events are also
written to raw storage. Two queues make it possible to commit results and offsets atomically
(exactly-once end to end).

**Aggregation service as a MapReduce-style DAG:** map nodes read, filter and route events by
`ad_id` -> aggregate nodes count per ad per minute in memory (and keep a heap for top N) -> reduce
nodes merge the partial top-N lists. Filters are handled with a **star schema**: pre-aggregate per
dimension value (country, etc.) so filtered queries are lookups.

**Crux 1 - time:** aggregate by **event time** (accurate; clients may lie or skew) rather than
processing time (reliable clock, wrong bucket for late events). Use **watermarks** to keep a window
open a little longer for stragglers; longer watermark = fewer misses, more latency. Fix what still
slips through with **end-of-day reconciliation** against raw data.
**Windows:** tumbling windows for per-minute counts; sliding windows for top N over M minutes.

**Crux 2 - exactly-once:** duplicates come from client resends (handled by a risk/fraud engine) and
from failures between processing and acknowledging. Commit the consumer offset and the downstream
write together (a distributed transaction), or make the downstream write idempotent (keyed by
window and ad) so replays overwrite rather than add.

**Lambda vs kappa:** lambda keeps separate batch and stream paths (two codebases). This design is
**kappa**: one streaming path; recalculation replays raw data through a separate aggregation
instance into queue 2.

**Scale:** more partitions (create them up front; rebalancing thousands of consumers is slow, so
do it off-peak), consumers, map/aggregate nodes (multi-threading or a resource manager like YARN);
the wide-column DB rebalances itself via consistent hashing. **Hot ads:** an overloaded aggregate
node asks for extra nodes and splits the events among them (or use global-local and split-distinct
aggregation).
**Fault tolerance:** in-memory state is lost when a node dies; snapshot the state with the offset
it covers, and on restart load the snapshot and replay from that offset.
**Monitoring:** end-to-end latency per stage, consumer lag, node resources; reconciliation alerts
on mismatches. Off-the-shelf alternative: raw events in a data lake plus an OLAP store (ClickHouse,
Druid).

---

## Building-block designs

These four are usually components inside a larger design. Mechanisms are explained in the
`distributed-patterns` references; this is the design summary.

**Key-value store** (`put(key, value)`, `get(key)`, small values, highly available, tunable
consistency): consistent hashing with virtual nodes for partitioning; replicate each key to the
next N distinct servers clockwise (in different DCs); quorum reads and writes (N=3, W=R=2 for strong
consistency); vector clocks for conflicting versions; gossip for failure detection; sloppy quorum
plus hinted handoff for temporary failures; Merkle trees for repairing permanent ones. Write path:
commit log -> memtable -> flush to SSTables. Read path: memtable -> Bloom filters -> SSTables. Every
node is identical (no single point of failure); a coordinator node proxies each client request.
Chooses availability (AP) by default; tune W and R toward consistency when needed.
-> partitioning-and-replication.md, storage-engines.md

**Rate limiter** (server-side, many rules, low latency and memory, distributed, clear errors, fails
open): middleware or API gateway in front of services; rules in config files cached by workers;
counters in Redis; token bucket by default. Return `429 Too Many Requests` with limit, remaining
and retry-after headers; drop or queue excess requests. Make the counter update atomic (Lua or
sorted sets) and sync limits across regions eventually. -> traffic-and-caching.md

**Unique ID generator** (64-bit, numeric, roughly time-ordered, 10k+ IDs/s, no single point of
failure): Snowflake layout - sign 1 bit, timestamp 41 bits (ms since a custom epoch, ~69 years),
datacenter 5 bits, machine 5 bits, sequence 12 bits (4,096 IDs per ms per machine). Needs NTP and
clock-skew handling. -> ids-and-hashing.md

**Consistent hashing:** hash servers and keys onto a ring; a key belongs to the first server
clockwise; adding or removing a server moves only the keys in one arc; virtual nodes even out the
load and let bigger servers take more. Used by Dynamo-style stores, Cassandra, Discord, Akamai and
the Maglev load balancer. -> partitioning-and-replication.md
