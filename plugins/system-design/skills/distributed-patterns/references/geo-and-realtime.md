# Geospatial and real-time delivery

## Geospatial indexes

A plain index on latitude and longitude helps only one dimension at a time, so "within radius"
queries scan wide ranges. Map 2D space to 1D keys.

**Even grid:** fixed cells. Trivial, but cities overflow cells while oceans sit empty.

**Geohash:** recursively halve longitude and latitude, interleave the bits, encode in base32.
Longer string = smaller cell; a shared prefix means the points are in the same larger cell.

| Length | Approx. cell size | Typical search radius |
|---|---|---|
| 4 | 39 km x 19.5 km | 5 - 20 km |
| 5 | 4.9 km x 4.9 km | 1 - 2 km |
| 6 | 1.2 km x 0.6 km | 0.5 km |

Boundary problems: two very close points can share no prefix (either side of the equator or a cell
edge), and points in the same cell can be far apart. Always search the **cell plus its 8
neighbours**. If results are too few, drop one character (bigger cells) and search again.
Updating is trivial (recompute one string). Redis GEO commands use geohash internally.

**Quadtree:** split a region into four until each leaf holds at most k items (e.g. 100). Adapts to
density and supports k-nearest search. Built in memory on each server (n log n; minutes for
hundreds of millions of points, a few GB of RAM), so new servers must finish building before taking
traffic; roll out deploys gradually. Updates: nightly rebuild, or in-place with locking.

**Google S2:** maps the sphere onto a Hilbert curve so nearby points have nearby 1D IDs. Covers
arbitrary shapes with cells of mixed levels: ideal for **geofencing**. Most complex.

**Choosing:** geohash for fixed-radius search and easy updates; quadtree when density varies or for
k-nearest; S2 for regions and geofences.

**Caching locations:** key caches by cell ID at the precisions you use, never by raw coordinates
(GPS jitters, users move). Cache `cell -> [ids]` and `id -> details` separately.

**Distance:** filter candidate IDs from cells, then compute exact distance (haversine) and sort.

## Map tiles and routing graphs

- Pre-render the map as 256x256 tiles per zoom level (each level quadruples the count); serve as
  static files from a CDN by `(zoom, x, y)` or geohash. **Vector tiles** cut bandwidth and render
  crisply on device.
- Road networks: intersections are nodes, roads are edges; Dijkstra/A* variants. Split the graph
  into **routing tiles** with neighbour links, at several levels of detail (streets, arterials,
  highways); long routes use coarse tiles in the middle. Tiles are immutable binaries in object
  storage, heavily cached.
- Location streams: batch GPS points on the client; write to a write-optimised store keyed by
  user and time; publish to a stream for traffic and ETA models.

## Real-time delivery to clients

| Method | How | Good for | Costs |
|---|---|---|---|
| Polling | Client asks every N seconds | Rare updates, simplicity | Mostly empty responses; latency up to N |
| Long polling | Server holds the request until data or timeout | Infrequent server -> client updates (file sync notifications) | Reconnect churn; the holding server may not be the one with the data |
| **WebSocket** | Persistent bidirectional connection | Chat, live location, games, navigation, trading UIs | Stateful servers; needs discovery, draining, reconnection |
| Server-sent events | One-way HTTP stream | Server -> client feeds, dashboards | One direction only |
| Mobile push (APNs/FCM) | Platform channel | Waking offline or backgrounded apps | Small payloads; not real time; not for web streaming |

## Running a stateful connection tier

- **Service discovery** assigns each client a server by region and load; the client connects there.
- Keep a registry of `user -> server` (or use pub/sub so you do not need one).
- **Scale in:** mark a server draining, stop new connections, let clients reconnect elsewhere.
- **Failure:** clients reconnect with backoff and resync from the last ID they have.
- **Resync:** each device keeps the latest message ID it has seen and fetches newer ones on reconnect.

## Presence

- Clients send a **heartbeat** every few seconds; no heartbeat within a threshold (for example
  30 s) marks the user offline. This rides out brief network drops without flicker.
- Store `user -> online, last_seen` in a fast key-value store.
- **Fan-out:** publish status changes to friends via pub/sub. Fine for small friend lists; for big
  groups, fetch presence on demand (when the group or list is opened) instead.

## Pub/sub fan-out for live data

- One channel per user (or per topic); servers subscribe on behalf of their connected clients and
  forward messages. Idle channels in Redis cost almost nothing, so pre-create them.
- The bottleneck is CPU for pushes, not memory: estimate pushes per second and divide by
  per-node capacity.
- Shard channels across a cluster with **consistent hashing**; publish the ring through service
  discovery; resize at quiet times, since moved channels force resubscription.
- Filter at the subscriber side when only some receivers qualify (distance within radius).
- Alternatives: actor runtimes (Erlang/Elixir BEAM) handle millions of lightweight processes and can
  host both connections and channels.
