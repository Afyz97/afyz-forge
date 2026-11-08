# Storage engines and data layout

## Storage types

| | Block | File | Object |
|---|---|---|---|
| What | Raw volumes (HDD, SSD, network-attached) | Folders and files on top of blocks (NFS, SMB) | Flat namespace of immutable objects over HTTP |
| Mutable | Yes | Yes | No (replace or version) |
| Cost / speed | High / fastest | Medium / fast | Low / slower |
| Scale | Medium | High | Vast |
| For | Databases, VMs | Shared file access | Media, backups, archives, data lakes, static assets |

## Choosing a database by access pattern

- **Relational:** clear relations, joins, transactions, moderate write volume. Default.
- **Key-value / in-memory:** lookups by key, counters, TTL, sorted sets; very low latency.
- **Wide-column (Cassandra, Bigtable, DynamoDB):** huge write volume, queries by partition key with
  rows ordered by a clustering key. Design one table per query; no ad-hoc filters on non-key columns,
  so **denormalise** (separate read and unread email tables, listing tables by bucket).
- **Document:** self-contained JSON documents, flexible schema.
- **Graph:** deep relationship traversal.
- **Time-series:** labelled measurements over time with rollups.
- **Search engine:** full-text and faceted queries, fed asynchronously.

Ask: what does the data look like, read-heavy or write-heavy, are transactions needed, are queries
aggregations (OLAP) or lookups (OLTP)?

## Write-optimised engines

- **Write-ahead log / commit log:** append every write before applying it, for crash recovery.
  Sequential appends are fast even on spinning disks.
- **LSM tree:** writes go to the log and an in-memory table; when full, it is flushed as a sorted
  immutable file (**SSTable**); background **compaction** merges files and drops overwritten or
  deleted entries. Reads check memory, then SSTables newest first, skipping files via **Bloom
  filters**. Used by Cassandra, Bigtable, RocksDB, many search indexes.
- **B-tree** (most relational DBs): update in place; better for read-heavy, random-access workloads.
- **Segmented logs** (message queues): append-only segments; delete whole old segments on retention.

## Many small objects

One file per object wastes disk blocks (a 1 KB object still uses a 4 KB block) and exhausts
inodes. Pack objects into large append-only files (a few GB) and keep a mapping table
`(object_id, file, offset, size)`, for example in an embedded DB on each storage node. Serialise
writes per file; give each core its own open file to avoid lock contention.

## Durability

- **Replication:** N full copies across failure domains (disk, host, rack, zone, region). 3 copies
  costs 200% overhead; simple and fast to read.
- **Erasure coding:** split data into k chunks and add m parity chunks (for example 8+4); any k
  chunks rebuild the data. ~50% overhead for 8+4 with higher durability than 3x replication, but
  reads touch many nodes and encoding costs CPU. Use for cold or bulk data.
- **Checksums** on objects and files detect silent corruption (bit rot); verify on read and in
  background scrubs; repair from replicas or parity.
- Back up the metadata, not just the data: losing the index loses the objects.

## Metadata vs data

Keep metadata (names, owners, ACLs, versions, block lists) in a database and the bytes in a data
store. They scale differently: metadata needs indexes and transactions; data needs cheap capacity
and throughput. Files are often split into **blocks** (e.g. up to 4 MB) referenced by hash, enabling
delta sync and dedupe.

## Lifecycle

- **Versioning:** each write creates a new version (time-ordered ID); a delete writes a **tombstone
  / delete marker**; reads of a deleted key return not found.
- **Multipart upload:** initiate -> upload parts in parallel (each acknowledged with a checksum) ->
  complete with the part list -> server assembles. Resumable and parallel.
- **Garbage collection:** lazily deleted data, orphaned parts from failed uploads, corrupted
  blocks. **Compaction** copies live data into a new file, atomically updates the mapping, then frees
  the old file.
- **Tiering:** move rarely accessed data to cold storage (cheaper, slower to retrieve).
- **Retention for history tables:** move past bookings or old events to cold storage, keep the hot
  table small.

## Time-series data

- Points: `(metric, labels, timestamp, value)`; write-heavy, read in bursts, mostly recent.
- Delta-of-timestamps and value compression shrink storage dramatically.
- **Downsampling** by age (raw 7 days, 1-minute 30 days, 1-hour 1 year).
- Low label cardinality, or indexes explode.
- Purpose-built engines (InfluxDB, Prometheus) beat general SQL for rolling-window queries.

## Low-latency in-process storage

- **mmap** maps a file into memory; writes are memory writes the OS flushes. Placing the file in
  `/dev/shm` keeps it entirely in RAM, giving a very fast shared event store between processes on
  one host.
- **Ring buffers:** fixed-size, preallocated, lock-free queues; pad counters onto separate cache
  lines to avoid false sharing.
- Local embedded stores (SQLite, RocksDB) remove network hops for per-node state.
