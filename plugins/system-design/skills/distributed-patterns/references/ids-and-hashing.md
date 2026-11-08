# IDs, short codes and hashing

## Unique IDs in a distributed system

A single auto-increment column stops working once writes span many databases. Options:

| Approach | How | Pros | Cons |
|---|---|---|---|
| Multi-master auto-increment | Each of k DBs increments by k from a different start | Numeric, uses the DB | Hard across DCs; not time-ordered across servers; breaks when servers are added or removed |
| UUID (v4) | 128-bit random, generated anywhere | No coordination; scales with app servers | 128 bits; not time-sortable; non-numeric; poor index locality |
| Ticket server | One DB hands out sequential IDs | Simple, numeric | Single point of failure; coordination for redundancy |
| **Snowflake-style** | 64-bit composed from time + location + sequence | Numeric, 64-bit, roughly time-ordered, no coordination | Depends on clocks |
| ULID / UUIDv7 | 128-bit with a millisecond timestamp prefix | Time-sortable, no coordination, standard tooling | 128 bits |

**Snowflake layout (64 bits):**

```
| 1 bit sign (0) | 41 bits ms since custom epoch | 5 bits datacenter | 5 bits machine | 12 bits sequence |
```

- 41 bits of milliseconds last ~69 years from the chosen epoch.
- 32 datacenters x 32 machines; IDs fixed at startup.
- Sequence resets each millisecond: 4,096 IDs per ms per machine.
- Tune the split per use case: fewer sequence bits and more timestamp bits for low-volume,
  long-lived systems.

**Clock caveats:** synchronise with NTP; if the clock moves backwards, wait or refuse rather than
emit duplicates; IDs are only roughly ordered across machines. The generator is critical
infrastructure: run several, with failover.

**Scoped sequences:** if order only matters within a conversation, account or partition, a
per-scope sequence (chat channel message IDs) is simpler than a global generator.

## Short codes (URL shortener and friends)

**Base62** (`0-9a-zA-Z`): encode a unique numeric ID. 62^7 is ~3.5 trillion codes in 7 characters.
No collisions; length grows with the ID; sequential IDs make codes guessable (shuffle or use
Snowflake IDs if that matters).

**Hash + truncate:** first 7 characters of CRC32, MD5 or SHA-1 of the input. Fixed length, no ID
generator, but collisions happen: on a hit, append a salt and rehash. Each check is a DB lookup,
so put a Bloom filter in front.

## Content hashing and dedupe

- Hash content to detect duplicates: crawled pages ("content seen?"), file blocks (store identical
  blocks once), attachments sent to many recipients.
- Hash blocks (e.g. up to 4 MB) rather than whole files to enable delta sync.
- Checksums (CRC, MD5 ETags) verify integrity on write, on read and in background scrubbing.
- Event and message dedupe: keep the IDs seen within a window and drop repeats.

## Bloom filter

A bit array plus k hash functions. Add: set k bits. Query: if any bit is 0 the item is definitely
absent; if all are 1 it is *probably* present. No false negatives, tunable false positives, tiny
memory, no deletes (use a counting variant).
Uses: skip disk lookups for keys not in an SSTable; "URL seen?" in crawlers; checking short-code
collisions before hitting the DB; cache-admission filters.

## Merkle trees

Hash tree over buckets of data: leaves hash data blocks, parents hash their children. Comparing
roots tells whether two copies match; descending into differing branches finds exactly which
buckets to sync. Used for replica repair and verifying large datasets.
