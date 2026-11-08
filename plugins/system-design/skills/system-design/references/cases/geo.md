# Blueprints: location

Proximity search (Yelp-like) and maps with navigation (Google Maps-like). Index details live in
`../../../distributed-patterns/references/geo-and-realtime.md`.

---

## Proximity service (nearby businesses)

**Scope:** given a location and radius, list nearby businesses; owners add, edit or delete
businesses (visible by next day, not real time); view business details. Low latency, privacy
compliance (GDPR/CCPA), peak handling in dense areas.
**Numbers:** 100M DAU x 5 searches -> ~5,000 QPS; 200M businesses.

**API**
- `GET /v1/search/nearby?latitude=&longitude=&radius=5000` (paginate results)
- `GET|POST|PUT|DELETE /v1/businesses/{id}`

**Services**
- **Location-based service (LBS):** read-only, stateless, high QPS, spiky by area and hour.
- **Business service:** owner writes (low QPS) and detail reads (high QPS, cacheable).
- **DB cluster:** primary for writes, replicas for reads. Replica lag is harmless because
  business changes are not real time.

**Crux - the spatial index.** A naive bounding-box query on latitude and longitude can only use
one index dimension at a time, so it scans huge ranges. Map 2D into 1D:

| Option | Strength | Weakness |
|---|---|---|
| Even grid | Trivial | Density varies wildly (city vs desert) |
| **Geohash** | A string; prefix = area; easy to compute, index and update; fixed-radius search | Fixed cell sizes; edge effects |
| **Quadtree** | Adapts to density; k-nearest queries | In-memory tree to build and keep in sync; harder updates |
| S2 (Hilbert curve) | Arbitrary-area coverage, geofencing, flexible levels | Most complex |

With geohash, pick the shortest length whose cell covers the radius (about 6 for 0.5 km, 5 for
1-2 km, 4 for 5-20 km), then query the user's cell **plus its 8 neighbours**, because nearby
points can sit in adjacent cells with no shared prefix. If too few results, shorten the
geohash by one and search again.

Quadtree notes: split until each leaf holds at most ~100 businesses; the whole index for 200M
businesses fits in a few GB on every LBS server; building takes minutes at startup (n log n), so
roll deploys out gradually and keep new servers out of rotation until the tree is ready; apply
owner edits in a nightly rebuild, or update in place with locking.

**Data:** `business` table sharded by business ID. **Geospatial index** table
`(geohash, business_id)`, one row per business, compound key: small enough for one DB, so add
read replicas rather than sharding.

**Caching:** do not key on raw coordinates (GPS jitters and users move). Cache
`geohash -> [business_id]` for each precision level you use, and `business_id -> details`.
Both fit in a modest Redis cluster; replicate it per region.

**Request walk:** client sends (lat, lng, radius) -> LBS picks the geohash length -> computes the
cell plus 8 neighbours -> fetches business IDs for all 9 cells from Redis in parallel -> fetches
details -> computes exact distances, filters, ranks -> returns. Deploy LBS in several regions,
near users and within data-residency rules.

---

## Maps, navigation and ETA

**Scope:** 1B DAU; location updates, navigation with ETA, map rendering; driving, walking,
cycling; traffic-aware; no multi-stop or business info. Accuracy, smooth rendering, and low data
and battery use on mobile.

**Map basics**
- Positions are latitude/longitude; projecting the globe to a flat map always distorts; web maps
  use **Web Mercator**.
- **Geocoding** turns an address into coordinates (reverse geocoding goes back), typically by
  interpolating along mapped street networks.
- **Tiling:** the world is pre-cut into 256x256 tiles per zoom level; zoom 0 is one tile; each
  level quadruples the count. Clients fetch only visible tiles for their zoom.
- **Routing graph:** intersections are nodes, roads are edges; routing uses Dijkstra/A*
  variants. The world graph is too big, so cut it into **routing tiles** that reference
  neighbours, at several levels of detail (local streets, arterials, highways). Long routes use
  coarse tiles; ends of the route use detailed ones.

**Numbers:** ~70 PB of tiles across zoom levels (after compressing near-identical tiles);
navigation location updates ~200k QPS average, ~1M peak, with client-side batching.

**Location service:** clients batch GPS points and send them every few seconds
(`POST /v1/locations` with an array of `(lat, lng, ts)`). Write-heavy and freshness beats
consistency, so use a wide-column store keyed by `user_id` (partition) and `timestamp`
(clustering). Also publish updates to a stream (Kafka-style) for traffic detection, road
learning, ETA models and analytics.

**Map rendering:** tiles are static files keyed by zoom and position, served from a **CDN**.
Clients can compute tile URLs themselves (cheap, but the scheme is then frozen in every
installed app) or ask a small API for them (one extra call, free to change later). **Vector
tiles** (paths and polygons rendered on the device) save a lot of bandwidth over raster images
and zoom smoothly.

**Navigation service**
- **Geocoding service** resolves origin and destination (key-value lookup, read-heavy; cache it).
- **Route planner** orchestrates:
  - **Shortest-path service:** A* over routing tiles loaded from object storage (tiles are
    immutable binaries; cache them hard); returns top-k candidate routes ignoring traffic.
  - **ETA service:** ML predictions from live and historical traffic for each candidate.
  - **Ranker:** applies user filters (avoid tolls, avoid highways) and orders routes.
- **Updater services** consume the location stream to refresh traffic data and routing tiles.

**Adaptive rerouting:** track active navigations. Storing every tile of every route is too much;
store the origin tile plus its ancestors at coarser levels until one contains the destination.
When an incident hits a tile, find affected users by checking their stored coarse tiles, then
recompute and push a better route.

**Delivery to clients:** mobile push payloads are too small and absent on web; long polling is
heavier than WebSocket; SSE is one-way. Use **WebSocket** (bidirectional is handy for features
like last-mile delivery).

**Extensions:** multi-stop routing (sell to delivery and ride-hailing companies), offline maps,
transit modes.
