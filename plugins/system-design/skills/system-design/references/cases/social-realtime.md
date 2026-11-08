# Blueprints: social and real-time

News feed, chat, nearby friends, real-time leaderboard.

---

## News feed

**Scope:** web and mobile; publish a post; see friends' posts in reverse chronological order;
up to 5,000 friends; 10M DAU; text, images and video.

**API**
- `POST /v1/me/feed {content, auth_token}` - publish
- `GET /v1/me/feed {auth_token}` - read own feed

**Two flows**
- **Publish:** load balancer -> web servers (auth, rate limit) -> post service (write post to
  DB and cache) -> fan-out service (push the post ID into friends' feeds) -> notification service.
- **Read:** load balancer -> web servers -> feed service reads the user's list of post IDs from
  the feed cache, then hydrates posts and authors from the content and user caches.

**Crux - fan-out:**

| | Fan-out on write (push) | Fan-out on read (pull) |
|---|---|---|
| When work happens | At publish time, into each friend's cached feed | At read time, merging friends' recent posts |
| Read speed | Fast, precomputed | Slower |
| Cost | Wasted on inactive friends; huge for accounts with millions of followers (hotkey) | Nothing wasted on inactive users |

Use a **hybrid**: push for normal accounts; for celebrities, skip the push and merge their recent
posts in at read time.

**Fan-out worker steps:** fetch friend IDs from the graph store -> drop muted friends and
apply audience settings (from the user cache) -> enqueue `(post_id, friend_ids)` -> workers
append the post ID to each friend's feed list. Store only IDs, and cap each list (a few hundred
entries); almost nobody scrolls further, and a miss falls back to the DB.

**Cache layers:** feed (post IDs per user), content (posts; hot posts separately), social graph
(followers, following), action (liked, replied, shared), counters (likes, replies, followers).

**Scale:** stateless web tier; shard and replicate the DBs; consistent hashing across cache
nodes; queues decouple the fan-out; watch QPS at peak, feed latency and cache hit rates.

---

## Chat system

**Scope:** 1-to-1 and group chat (groups up to 100); text up to 100k characters; online
presence; multiple devices per account; push notifications when offline; history kept forever;
50M DAU.

**Protocol choice (receiver side):**
- Polling: mostly empty responses, wasteful.
- Long polling: holds a connection until a message arrives; the server holding the connection
  may not be the one that receives the message, timeouts still waste work, and it is hard to
  tell when a client disconnected.
- **WebSocket:** persistent and bidirectional; use it for sending and receiving.

**Components**
- **Stateless services** behind a load balancer: login, signup, profile, group management,
  and service discovery.
- **Stateful chat servers:** hold each client's WebSocket.
- **Presence servers:** online/offline status.
- **Push notification** service for offline recipients.
- **Key-value store** for messages: scales horizontally, very low latency, handles the long tail
  of rarely read old messages better than a big relational index. Relational DB for users,
  settings and friend lists.

**Data model**
- 1-to-1: `message(message_id PK, from, to, content, created_at)`.
- Group: `group_message(channel_id, message_id, user_id, content, created_at)`, primary key
  `(channel_id, message_id)`.
- `message_id` must be unique and increase with time **within a conversation**. A global
  Snowflake ID works, but a **per-channel local sequence** is enough and simpler: ordering only
  matters inside one conversation.

**Service discovery:** after login, a coordinator (ZooKeeper-style) picks the best chat server
for the client by region and capacity; the client opens its WebSocket there.

**Message flows**
- 1-to-1: A sends to chat server 1 -> it gets an ID and writes the message to a sync queue and the
  KV store -> if B is online, forward to B's chat server, which pushes it over B's socket; if
  offline, send a push notification.
- Group (small): copy the message into **each member's inbox** (message sync queue). Each
  recipient reads just its own inbox. Works up to roughly a hundred members; very large groups
  need a shared channel and pull instead.

**Multi-device sync:** each device remembers `cur_max_message_id`; on reconnect it fetches
messages where `recipient = me AND message_id > cur_max_message_id` from the KV store.

**Presence**
- Login opens the socket and marks the user online with a timestamp in the KV store.
- Clients send a **heartbeat** every few seconds; no heartbeat within a threshold (for example
  30 s) means offline. This avoids flicker when a phone briefly loses signal.
- Fan-out: a pub/sub channel per friend pair; status changes publish to each friend's channel.
  Fine for small groups; for huge groups, fetch presence on demand (when opening the group).

**Failure and extensions:** if a chat server dies, discovery gives the client a new server
and it reconnects; retry and queue undelivered messages; later add media (compress, object
storage, thumbnails), end-to-end encryption, client-side caching, and edge caching.

---

## Nearby friends

**Scope:** show friends within a configurable radius (for example 5 miles), each with a
distance and last-update time, refreshed every few seconds; straight-line distance; keep
location history for analytics; inactive users disappear after ~10 minutes.
**Numbers:** 100M daily users, 10M concurrent, update every 30 s -> ~334k location updates/s;
400 friends each, ~10% online -> ~40 forwards per update -> ~14M pushes/s.
**Qualities:** low latency, occasional lost updates acceptable, eventual consistency is fine.

**Why not proximity-search style?** Locations change constantly, so a static index does not
fit. Instead use the backend as a fan-out hub: receive each update, forward it only to online
friends who are within range.

**Components:** load balancer; stateless REST API servers (friends, profiles); **stateful
WebSocket servers**; Redis **location cache** (`user_id -> lat, lng, ts` with a TTL, so inactive
users expire); a write-optimised **location history** store (Cassandra-style); user DB;
**Redis pub/sub** with one channel per user.

**Update flow:** client sends its location over the socket -> WebSocket server writes history
and updates the location cache (and keeps the latest value in memory) -> publishes to the
user's own channel -> every WebSocket server holding a subscribed friend receives it,
computes the distance, and pushes it to that friend only if within the radius.

**Client initialisation:** on connect, the server loads the friend list, subscribes to every
friend's channel (online or not), reads their cached locations and sends the nearby ones.
Pre-create channels for all users; idle channels in Redis cost almost no memory.

**Scaling Redis pub/sub:** memory is small (~200 GB for all channels) but CPU is the limit:
~14M pushes/s at ~100k pushes per server needs 140+ servers. Distribute channels across a
cluster with consistent hashing; keep the hash ring in service discovery (etcd, ZooKeeper);
WebSocket servers cache the ring. Resizing moves channels and triggers mass resubscription,
so resize at the daily low and over-provision.

**Other points:** WebSocket servers must drain connections before removal; cap friend counts
(whales just make one server busier); add/remove friend triggers subscribe/unsubscribe; for
"random people nearby", add pub/sub channels per geohash cell and subscribe to the user's cell
plus neighbours. Erlang/BEAM is a viable alternative to Redis pub/sub but hiring is harder.

---

## Real-time gaming leaderboard

**Scope:** a point per match won; a new leaderboard each month; show top 10 and a user's own
rank (bonus: the 4 players above and below); real-time updates; ties share a rank.
**Numbers:** 5M DAU, 25M MAU, 10 matches per day -> ~500 score updates/s (peak ~2,500);
top-10 reads ~50/s.

**API:** `POST /v1/scores {user_id, points}` (only game servers may call it, never clients, or
players will forge wins); `GET /v1/scores` (top 10); `GET /v1/scores/{user_id}` (rank and score).

**Crux - computing rank:**
- Relational table with an index on score: top 10 is fine (`ORDER BY score DESC LIMIT 10`), but
  an arbitrary user's rank needs counting everyone above them, which does not scale.
- **Redis sorted set** (hash map + skip list): `ZINCRBY lb_2026_10 1 user` to score,
  `ZREVRANGE lb 0 9 WITHSCORES` for the top 10, `ZREVRANK lb user` for a rank, then
  `ZREVRANGE lb rank-4 rank+4` for neighbours. All are O(log n) (+m for ranges).
- Size: 25M users x ~26 bytes ~650 MB; even doubled for skip-list overhead, one node is enough,
  and 2,500 writes/s is easy.

**Durability:** Redis replica plus persistence; keep user profiles and a match/score history
table in MySQL, from which the board can be rebuilt after a total loss. Cache the top-10 user
profiles.

**Scaling to 500M DAU (~65 GB, ~250k QPS):**
- **Fixed partitions by score range** (`0-100`, `101-200`, ...): top 10 comes from the highest
  shard; a rank is the rank inside the user's shard plus the counts of all higher shards. Keep
  `user -> shard` in a lookup and move users when they cross a range boundary.
- **Hash partitions (Redis Cluster):** top 10 means scatter-gather to every shard; exact rank is
  hard. Prefer score ranges here.
- **NoSQL alternative** (DynamoDB/Cassandra): partition by month plus a write-shard suffix
  (`user_id % N`) to avoid a hot partition, score as sort key, scatter-gather for top k. Exact
  rank is impractical; show a percentile computed by a periodic job instead.

**Extras:** break ties by who reached the score first (store a timestamp alongside the score);
consider serverless functions behind an API gateway if building from scratch; give write-heavy
Redis nodes ~2x the memory they need for snapshots.
