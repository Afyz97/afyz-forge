# Partitioning, replication and consistency

## Sharding

Split rows across databases by a **shard key**; each shard has the same schema and a disjoint slice.

Choosing the key:
- Spreads data and traffic evenly (high cardinality, no hot values).
- Matches the main query, so a request touches one shard (`user_id` for per-user data, `hotel_id`
  for bookings, `(bucket, object_name)` for object metadata).
- Secondary access patterns get their own denormalised table sharded differently (object listing
  by bucket; read vs unread email tables).

Problems and answers:
- **Resharding** when a shard fills or skews: consistent hashing or many small virtual shards
  mapped onto fewer physical ones, so only a fraction moves.
- **Hot keys (celebrity problem):** dedicated shard, key splitting (`key#0..key#N` and merge on
  read), write-sharding suffixes, or switching that key from push to pull.
- **Cross-shard joins:** denormalise; precompute; or query each shard and merge (scatter-gather,
  which gets slower with more shards and complicates pagination).
- **Range vs hash partitioning:** ranges keep order (range scans, leaderboard score ranges) but
  invite hotspots; hashing spreads load but loses order.

## Consistent hashing

**Problem:** `server = hash(key) % N` remaps almost every key when N changes, causing a storm of
cache misses or data moves.

**Mechanism:** hash both servers and keys onto the same ring (for example SHA-1's 0 .. 2^160-1).
A key belongs to the first server clockwise from its position.
- Adding a server moves only the keys between it and its predecessor (anticlockwise).
- Removing a server moves only its own keys, to the next server clockwise.

**Virtual nodes:** each physical server appears at many points on the ring. More points -> smaller
standard deviation of load. Bigger machines get more virtual nodes (heterogeneity).

**Used in:** Dynamo-style stores, Cassandra, Discord, Akamai, the Maglev load balancer, Redis pub/sub
channel placement, crawler host assignment, metrics collector assignment.

## Replication

- **Single leader:** writes to the leader, async followers serve reads. Simple; followers lag.
  On leader failure, promote a follower (possibly missing the last writes; recover or accept).
- **Read-your-writes:** after a user writes, read their data from the leader for a while, or use
  sticky sessions to the leader within the request.
- **Multi-leader / leaderless:** accept writes in several places; must detect and resolve conflicts.
- Replicate across **failure domains** (racks, zones, regions), not just machines.
- For money and order books, avoid stale reads: read from the leader, or use a consensus-replicated
  store where followers do not lag behind committed data.

## CAP

When the network partitions (it will), a replicated system must choose:
- **CP:** refuse some requests to stay consistent (payments, wallets, email metadata, bookings).
- **AP:** keep answering and reconcile later (location updates, feeds, presence, metrics, carts).
"CA" is not an option for a distributed system because partitions cannot be ruled out.

**Consistency models:** strong (every read sees the latest write), weak (may not), eventual (replicas
converge given time). Pick per data type, not per system.

## Quorum consensus (leaderless replication)

N replicas; a write succeeds after W acknowledgements; a read waits for R responses.

| Setting | Effect |
|---|---|
| W + R > N | Read and write sets overlap: strong consistency (typical N=3, W=R=2) |
| W + R <= N | Faster, no strong guarantee |
| R = 1, W = N | Fast reads, slow writes |
| W = 1, R = N | Fast writes, slow reads |

The coordinator node proxies the request to the replicas (the N distinct servers clockwise on the
ring, ideally in different DCs).

## Conflict detection: vector clocks

Each value carries a list of `[server, counter]` pairs. A write at server S increments S's counter
(adding the pair if new).
- Version X is an **ancestor** of Y if every counter in X is <= its counterpart in Y: no conflict,
  keep Y.
- Otherwise they are **siblings** (concurrent): return both and let the client or application
  logic merge them, then write back the merge.
Costs: client complexity, and clocks grow with writers, so cap the list (drop oldest pairs), which
can rarely misjudge ancestry.

## Failure detection and repair

- **Do not trust one witness.** Declare a node down only with independent confirmation.
- **Gossip:** every node keeps a membership list with heartbeat counters, increments its own, and
  periodically sends the list to a few random nodes. A member whose counter has not risen for a
  set period is considered offline. No central monitor needed.
- **Heartbeats to a coordinator** work for smaller clusters (placement service, consumer groups).
- **Temporary failure - sloppy quorum + hinted handoff:** write to the first W *healthy* nodes on
  the ring; a stand-in stores a hint and hands the data back when the owner recovers.
- **Permanent failure - anti-entropy with Merkle trees:** split the key space into buckets, hash
  each key, hash each bucket, hash pairs up to a root. Two replicas compare roots; if they differ,
  descend only into differing children. Transfer volume is proportional to the difference, not the
  data size.
- **Data center outage:** replicate across DCs so clients can be served elsewhere.

## Consensus and coordination

- **Raft / Paxos:** replicate an ordered log among 2f+1 nodes; survives f failures (5 nodes survive
  2, 7 survive 3). A leader appends, followers replicate, commit at majority; a new leader is
  elected if the old one dies. Use for small, critical state: cluster maps, placement services,
  money event logs, matching-engine failover.
- **Coordination services (ZooKeeper, etcd):** hierarchical key-value store for config, service
  discovery, membership, leader election, partition maps. Strongly consistent, low volume.
- **Service discovery** picks the right stateful server for a client (chat servers by region and
  load; which Redis node owns a channel).

## Multi-region

- GeoDNS to the nearest region; automated failover.
- Async replication between regions; decide the acceptable lag and possible loss per data type.
- Identical automated deployments everywhere; test region evacuation.
