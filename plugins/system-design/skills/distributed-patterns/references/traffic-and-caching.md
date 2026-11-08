# Traffic control and caching

Load balancing, rate limiting, caching, CDN, stateless tiers.

## Load balancing

- Spreads requests over a pool; removes unhealthy servers via health checks; lets you add servers
  for capacity. Run at least two load balancers (active/standby) so the balancer itself is not a
  single point of failure.
- Requires a **stateless** web tier: sessions in a shared store, uploads in object storage.
- Stateful tiers (WebSocket servers) need sticky routing chosen by service discovery, plus
  **draining** before removal: stop new connections, let existing ones close or migrate.
- Geo-routing (GeoDNS) picks the nearest region; health-based failover moves traffic between regions.

## Rate limiting

**Why:** stop abuse and denial of service, control cost (paid third-party calls), keep servers
stable. Examples: posts per second, account creations per day, reward claims per user.

**Where:**
- Client side: never trustworthy on its own (easy to bypass).
- Server side or as middleware / API gateway: the norm. If you already run a gateway (auth, IP
  allowlists, TLS termination), put it there.
- Build only when you need custom algorithms or rules; otherwise use the gateway or a managed one.

**Algorithms**

| Algorithm | How | Strengths | Weaknesses | Use for |
|---|---|---|---|---|
| **Token bucket** | Bucket of capacity B refilled at R tokens/s; each request takes a token or is rejected | Simple, tiny memory, allows short bursts | Two parameters to tune | Default for APIs |
| Leaky bucket | FIFO queue of size B drained at a fixed rate | Smooth, steady outflow | Bursts fill the queue and delay fresh requests | Protecting a fixed-capacity downstream |
| Fixed window counter | Counter per time window (e.g. per minute) | Simplest, tiny memory | Up to 2x the limit can pass around a window edge | Coarse quotas |
| Sliding window log | Store timestamps of accepted requests; drop those older than the window; count | Exact | Memory per request, even rejected ones in some variants | Low-volume, strict limits |
| Sliding window counter | `current_count + previous_count x overlap_fraction` | Smooth, small memory | An approximation (assumes even spread in the previous window) | Large-scale limits needing smoothness |

**Rules:** keyed by user, API key, IP or endpoint; stored in config files and cached by the
limiter. Typical rule shape: `domain, key, unit, requests_per_unit`.

**Implementation:** counters in an in-memory store (Redis `INCR` + `EXPIRE`, or sorted sets for
logs). The read-check-write must be **atomic** (a Lua script or a single atomic command), or
concurrent requests race past the limit.

**Response:** `429 Too Many Requests`, with headers for the limit, remaining requests and seconds
until retry (`X-Ratelimit-Limit`, `X-Ratelimit-Remaining`, `X-Ratelimit-Retry-After`, or the
standard `Retry-After`). Rejected requests are dropped, or queued for later if they matter
(orders).

**Distributed concerns:** one central store avoids races between limiter nodes; in multi-region
setups, sync counters eventually and accept slight overshoot; put limiters at the edge near users.
Limit at several layers (IP at the network edge, user at the application). Monitor whether the
limits are too tight (legitimate users rejected) or too loose (still overloaded).

**Client side:** cache to avoid needless calls, back off on 429, read the retry header.

## Caching

**When:** data is read often, changes rarely, and can tolerate brief staleness.

**Read pattern (cache-aside):** read cache -> on miss read the DB and fill the cache with a TTL.
**Write pattern:** write the DB, then **delete** the cache key (rather than writing the new value,
which races with concurrent readers). Because the two steps are not atomic, choose a TTL that
bounds how long an inconsistency can live.

**Decisions to state explicitly**
- **TTL:** always set one; long enough to absorb load, short enough for freshness.
- **Eviction:** LRU by default; LFU when popularity is stable; FIFO rarely.
- **Failure:** multiple nodes across zones; over-provision memory; plan for a cold cache after a
  restart (warm it, or throttle DB reads).
- **Stampede:** many concurrent misses on one hot key hammer the DB. Use a per-key lock or
  single-flight refill, serve stale while one request refreshes, or add TTL jitter.
- **Key design:** key by the stable identity of the query, not by noisy inputs. Example: for
  location search, key by geohash cell, not raw GPS coordinates.
- **What to store:** IDs and small objects; hydrate separately (feeds store post IDs per user, then
  look posts up in a content cache).
- **Never** the only copy of data you cannot lose or must not get wrong (balances, stock). The DB
  stays the source of truth and its constraints stay the guard.

**Layered caches (feed example):** feed IDs per user; content (hot items separately); social
graph; per-user actions (liked, shared); counters.

**Keeping a cache in sync from the DB:** change data capture (read the DB's change log and apply it
to the cache) keeps writers simple and catches every write path.

## CDN

- Edge servers near users cache static assets (images, CSS, JS, video segments, map tiles). Miss ->
  fetch from origin -> cache for the asset's TTL.
- **Cost:** you pay for transfer; route only popular content through it (the long tail of rarely
  watched video can be cheaper from origin).
- **TTL:** per asset type; for code and styles, version the file name and cache "forever".
- **Invalidation:** vendor API, or (better) versioned URLs.
- **Fallback:** clients detect a CDN outage and fall back to origin.
- Use CDNs as upload ingress points too (upload to the nearest edge).
- For security of private media: signed, expiring URLs.

## Stateless web tier and multi-region checklist

- No local session, file or in-process cache that other servers depend on.
- Autoscaling based on CPU, latency or queue depth.
- Health checks and graceful shutdown.
- Region failover tested; data replication lag measured; deployments identical in every region.
