# Blueprints: web services

URL shortener, web crawler, notification system, search autocomplete.

---

## URL shortener

**Scope:** shorten a long URL; redirect a short URL; codes as short as possible, using
`[0-9a-zA-Z]`; codes never change or expire.
**Numbers:** 100M new URLs/day -> ~1,160 writes/s; 10:1 reads -> ~11,600 reads/s; 10 years ->
365B records; ~100 B each -> ~36.5 TB.

**API**
- `POST /api/v1/data/shorten {longUrl}` -> `shortUrl`
- `GET /api/v1/{shortCode}` -> redirect to the long URL

**Redirect status:** `301` (permanent) lets browsers cache the redirect, so later clicks skip
your servers and load drops. `302` (temporary) sends every click through you, which is what you
want for click analytics.

**Data:** one table `(id PK, short_code UNIQUE, long_url)`, with an index on `long_url` if the
same long URL must map to one code. A relational store is enough; cache hot mappings.

**Crux - generating the code:**

| | Hash + collision check | Base62 of a unique ID |
|---|---|---|
| How | Take the first 7 chars of CRC32/MD5/SHA-1 of the URL; on collision append a salt and retry | Get a unique 64-bit ID (see ids-and-hashing), encode in base 62 |
| Length | Fixed | Grows with the ID |
| Needs an ID generator | No | Yes |
| Collisions | Possible: a DB lookup per attempt, or a Bloom filter in front | Impossible |
| Guessable next code | No | Yes if IDs are sequential (a privacy concern) |

62^7 is ~3.5 trillion, so 7 characters cover 365B URLs with room to spare.

**Shorten flow:** look up `long_url`; if present, return the existing code. Otherwise get a new
ID, encode it, insert `(id, code, long_url)`, return the code.
**Redirect flow:** cache lookup by code -> on miss read the DB and fill the cache -> redirect.

**Scale and extras:** stateless web tier; replicate and later shard the table; rate-limit
`shorten` per IP or key; capture clicks asynchronously for analytics; validate and block
malicious target URLs.

---

## Web crawler

**Scope:** crawl for search indexing; HTML only; 1B pages/month; detect new and changed pages;
skip duplicate content; keep pages 5 years.
**Numbers:** ~400 pages/s (peak 800); 500 KB per page -> 500 TB/month -> ~30 PB over 5 years.
**Qualities:** scalable (parallel), robust (bad HTML, traps, crashes), polite (do not hammer a
host), extensible (new content types as plug-ins).

**Pipeline:** seed URLs -> URL frontier -> HTML downloader (with DNS resolver) -> content
parser -> "content seen?" (hash of page body) -> content storage -> link extractor -> URL
filter (blocklist, file types) -> "URL seen?" (Bloom filter or hash set) -> back into the
frontier.

**Crux - the URL frontier:**
- Traverse breadth-first; depth-first can sink into one enormous site.
- **Front queues (priority):** a prioritiser scores URLs (page rank, traffic, update rate) and
  puts them into queues by priority; a selector picks queues with a bias toward high priority.
- **Back queues (politeness):** a router maps each host to exactly one queue via a host-to-queue
  table; each worker drains one queue sequentially with a delay between requests, so one host
  never sees parallel fetches.
- **Freshness:** recrawl by observed change frequency and importance.
- Keep the frontier mostly on disk with in-memory buffers for enqueue and dequeue.

**Downloader:** obey robots.txt (cache it per host); short timeouts; DNS cache (lookups are
slow and often synchronous); distribute crawlers geographically near target hosts.

**Robustness:** consistent hashing spreads hosts over crawler nodes; persist crawl state for
restarts; catch parser exceptions; validate content.

**Problem content:** duplicates via content hashes (a large share of the web is duplicated);
spider traps (infinite calendars, session URLs) via max URL length, depth limits and per-host
page caps; noise (ads, spam) filtered out.

**Extensions:** server-side rendering for JS-heavy pages, an anti-spam filter, sharded and
replicated storage, analytics.

---

## Notification system

**Scope:** iOS push, Android push, SMS, email; soft real-time; triggered by client actions or
scheduled jobs; users can opt out per channel. ~10M push, 1M SMS, 5M email per day.

**Providers:** APNs (iOS), FCM (Android), an SMS gateway, an email service. Collect device
tokens, phone numbers and emails at install or signup: `users` table plus a `devices` table
(one user, many device tokens).

**Evolution:**
1. One notification server calling providers directly: a single point of failure, cannot scale
   its parts independently, and slow third-party calls block everything.
2. Improved: several stateless notification servers behind a load balancer; DB and cache moved
   out; **one queue per channel** so an SMS outage does not stall push; **workers per channel**
   pull from their queue and call the provider.

**Flow:** trigger service calls the notification API -> server authenticates the caller,
validates, loads user settings and contact info (cache, then DB), renders a template ->
enqueues an event -> channel worker sends via the provider -> result logged.

**Crux - reliability:**
- **No loss:** persist each notification in a notification log before sending; retry failures
  with backoff; after N attempts, alert.
- **No duplicates:** exactly-once delivery is not achievable end to end, so dedupe on an event
  ID: a worker checks whether it has seen the ID and drops repeats.

**Supporting features:** templates with parameters; per-user, per-channel opt-in settings
checked before sending; rate-limit how many notifications one user gets; track delivered,
opened and clicked events; monitor queue depth and scale workers on it; authenticate callers
(app key and secret) so only trusted services can send.

---

## Search autocomplete

**Scope:** as the user types a prefix, return the top 5 historical queries by frequency;
lowercase English letters; under 100 ms.
**Numbers:** 10M DAU x 10 searches x ~20 keystroke requests -> ~24k QPS, peak ~48k; ~0.4 GB of
new query data per day.

**Two services:**
- **Data gathering:** build query frequencies from logs, offline.
- **Query service:** answer "top k for this prefix" from an in-memory structure.

**Crux - the trie:**
- Naive top-k: find the prefix node (O(p)), walk its whole subtree (O(c)), sort (O(c log c)):
  too slow.
- Fixes: cap prefix length (users rarely type more than ~50 characters), so finding the node is
  O(1); **cache the top k queries at every node**, so the answer is O(1) at the cost of memory.

**Data gathering pipeline (not real time):** analytics logs (append-only, unindexed) ->
aggregators (daily or weekly; shorter windows for trend-driven products) -> aggregated
frequency table -> workers rebuild the trie -> trie DB (serialised snapshot in a document store,
or prefix -> node data in a key-value store) -> trie cache in memory, served by the query service.

**Query path:** request -> load balancer -> query service -> trie cache (miss: trie DB, then
fill). Speed-ups: AJAX requests, browser caching of results for an hour or so, sampling only 1
in N queries into the logs.

**Delete:** a filter layer in front of the cache strips banned or harmful suggestions
immediately; remove them from storage asynchronously.

**Scale:** shard by first character, then split heavy ranges further (`s` is far bigger than
`x`). Use a shard map manager driven by historical distribution rather than naive alphabetical
ranges.

**Extensions:** Unicode tries for other languages; per-country tries behind CDNs; trending
queries need streaming aggregation and weighting recent queries more heavily.
