# Scale ladder: from one server to millions of users

Climb one rung at a time. Each rung lists the signal that justifies it; without the signal,
stay where you are.

## Rung 0 - One server

Web app, database and cache on one machine. DNS resolves the domain to that machine's IP;
browsers and mobile apps send HTTP and get back HTML or JSON.
**Leave when:** the web and data tiers compete for CPU or memory, or one box is a scary single
point of failure.

## Rung 1 - Separate the database

Web tier and data tier on different servers so each scales on its own.
Choosing the store:
- Relational by default: joins, transactions, decades of tooling.
- Non-relational when you need very low latency, the data has no real relations, you only
  serialise and deserialise blobs (JSON, documents), or the volume is massive.
  Families: key-value, document, wide-column, graph.

## Rung 2 - Load balancer and more web servers

Vertical scaling (bigger box) is quick but has a hard ceiling and no redundancy. Horizontal
scaling (more boxes) needs a load balancer, which gives:
- failover: a dead server drops out and traffic shifts to the rest
- capacity: add servers when traffic grows
Clients reach the load balancer's public IP; web servers sit on private IPs.

## Rung 3 - Database replication

One primary takes writes; replicas copy it and serve reads. Most apps read far more than they
write, so replicas outnumber primaries.
- A replica dies: send its reads to other replicas, or briefly to the primary, and replace it.
- The primary dies: promote a replica. It may lag behind, so missing writes need recovery
  (multi-primary or circular replication are alternatives with their own problems).
- Replication lag means a user may not read their own fresh write from a replica. For
  read-after-write paths (profile just edited, payment just made), read from the primary.

## Rung 4 - Cache tier

An in-memory store in front of the database for data that is read often and changed rarely.
Decide, explicitly:
- **Expiry:** always set a TTL. Too short hammers the DB, too long serves stale data.
- **Consistency:** the DB write and cache update are not one transaction. Prefer "write DB,
  then delete the cache key" and let the next read refill it.
- **Failure:** one cache node is a single point of failure; run several, across zones, and
  over-provision memory.
- **Eviction:** LRU is the usual default; LFU or FIFO when the access pattern says so.
- **Never** make the cache the only home of data you cannot lose (balances, stock counts).

## Rung 5 - CDN for static content

Images, CSS, JS and video are served from edge servers near users. On a miss the edge fetches
from origin and keeps it for its TTL.
- Cost: you pay for transfer, so do not push rarely used assets through it.
- Expiry: set per asset type; version file names (`app.3f9c.js`) instead of invalidating.
- Fallback: if the CDN fails, clients should be able to fetch from origin.

## Rung 6 - Stateless web tier

Move session and per-user state out of web servers into a shared store (Redis, the DB).
Any server can then answer any request, so autoscaling and rolling deploys become trivial.
Also move uploaded files to object storage; local disk on a web server is invisible to its
siblings.

## Rung 7 - Multiple data centers or regions

GeoDNS sends users to the nearest healthy region; if a region fails, all traffic shifts to the
others. Needs:
- traffic steering and health checks
- data replication between regions (async, so decide how much lag and loss is acceptable)
- identical, automated deployment to every region

## Rung 8 - Message queue

Producers publish work to a durable queue; consumers process it asynchronously. This
decouples the two sides so they scale and fail independently: a burst piles up in the queue
instead of in request latency. Typical first uses: email/SMS, image or video processing,
calls to slow third-party APIs.

## Rung 9 - Logging, metrics, automation

Before going further, make the system observable: centralised error logs; host metrics (CPU,
memory, disk); aggregate metrics (DB tier, cache tier); business metrics (DAU, revenue,
retention). Automate build, test and deploy so many people can ship safely.

## Rung 10 - Shard the database

When one primary cannot hold the data or take the writes, split rows across shards by a key
(often `user_id`). Every shard has the same schema and a disjoint slice of data.
- **Shard key** must spread data and load evenly and match the main query, so most requests
  hit one shard.
- **Resharding** happens when a shard fills or the distribution skews. Consistent hashing
  limits how much data moves.
- **Hot keys** (the celebrity problem): one key draws too much traffic. Give it a dedicated
  shard or split it further.
- **Joins** across shards are expensive. Denormalise so the common query reads one table on
  one shard.
- Move non-relational, high-volume data (logs, events, chat history) to stores built for it.

## Summary

Keep the web tier stateless. Put redundancy at every tier. Cache as much as is safe. Serve
static assets from a CDN. Replicate across regions. Shard the data tier. Split tiers into
services that scale on their own. Monitor everything and automate deployment.
