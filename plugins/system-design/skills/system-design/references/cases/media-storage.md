# Blueprints: media and storage

Video platform, file sync, S3-like object storage, distributed email.

---

## Video upload and streaming (YouTube-like)

**Scope:** upload and watch; mobile, web, TV; several resolutions; uploads up to 1 GB; low
infrastructure cost; high availability.
**Numbers:** 5M DAU, 5 views each; 10% upload one ~300 MB video per day -> 150 TB/day new
storage. CDN egress at $0.02/GB: 5M x 5 x 0.3 GB x 0.02 = ~$150k/day. **Cost is a first-class
requirement.**

**Components:** clients; CDN (serves video); API servers (everything except streaming);
metadata DB + cache; original storage (blob); transcoding servers; transcoded storage; a
completion queue and handlers.

**Upload flow (two parallel tracks)**
1. Video bytes: client uploads to original storage (via pre-signed URL) -> transcoders pull it
   and produce the renditions -> outputs go to transcoded storage and on to the CDN; a completion
   event goes to a queue -> completion handlers update metadata and notify the uploader.
2. Metadata: client sends title, size, format, etc. to the API servers -> metadata DB and cache.

**Streaming:** clients stream from the nearest CDN edge using adaptive protocols (HLS,
MPEG-DASH), switching bitrate with network quality.

**Crux - transcoding pipeline:**
- Why: raw video is huge, devices support different containers and codecs, and adaptive
  streaming needs several bitrates.
- Model the work as a **DAG** defined by configuration: split into video, audio and metadata;
  then encodings per resolution/bitrate, thumbnails, watermarking, in parallel where possible.
- Pieces: **preprocessor** (splits video into GOP-aligned chunks, builds the DAG, caches chunks
  in temporary storage for retries) -> **DAG scheduler** (turns the DAG into stages of tasks) ->
  **resource manager** (task queue, worker queue, running queue; a scheduler pairs the best task
  with the best worker) -> **task workers** -> encoded output.

**Speed:** chunked, resumable, parallel uploads; upload endpoints near users; queues between
every stage so stages run in parallel.
**Safety:** pre-signed upload URLs; DRM, AES encryption or visible watermarks for paid content.
**Cost:** most views go to a few videos, so serve only popular videos from the CDN and the
long tail from your own servers; encode rare videos on demand; keep regional content regional;
partner with ISPs or build edge caches.
**Errors:** recoverable ones (a failed segment, a dead worker) retry; unrecoverable ones (corrupt
format) stop and return an error code.

---

## File sync and storage (Google Drive / Dropbox-like)

**Scope:** upload and download; sync across devices; share with permissions; revision history;
notify on edit, delete, share. 10 GB free per user; files up to 10 GB; data loss is
unacceptable; sync must be fast and bandwidth-thrifty.
**Numbers:** 50M users x 10 GB = 500 PB allocated; 10M DAU x 2 uploads/day at ~500 KB ->
~240 upload QPS, peak ~480.

**API:** simple upload for small files; **resumable upload** (get a session URL, upload,
resume after interruption) for large ones; download; list revisions.

**Starting point and evolution:** one server with `drive/<namespace>/<path>` on disk ->
shard by user -> move file bytes to object storage with cross-region replication -> load
balancer and stateless API servers -> replicated, sharded metadata DB.

**Improved architecture**
- **Block servers:** split files into blocks of up to 4 MB, hash each, compress and encrypt,
  upload blocks to object storage. A file is the ordered list of its block hashes.
- **Metadata DB + cache:** users, workspaces, files, file versions, blocks.
- **Notification service:** tells clients that something changed; uses **long polling** because
  traffic is infrequent and one-directional (server -> client).
- **Offline backup queue:** holds changes for clients that are offline.
- **Cold storage** for files nobody opens.

**Crux - sync efficiency and conflicts:**
- **Delta sync:** only changed blocks are uploaded or downloaded.
- **Dedupe:** identical blocks (same hash) within an account are stored once.
- **Conflicts:** the first version processed wins; the later one becomes a conflict copy the user
  can merge or discard.

**Upload flow:** client sends metadata (status `pending`) and, in parallel, blocks to block
servers -> blocks land in object storage -> a completion callback sets status `uploaded` ->
notification service tells the user's other devices and collaborators.
**Download flow:** a client learns of a change (live notification, or a backlog pulled on
reconnect) -> fetches new metadata -> downloads only the missing blocks -> reassembles.

**Storage savings:** dedupe; cap the number of kept versions and weight recent ones; move idle
data to a cold tier.
**Failures:** standby load balancer; reassign a dead block server's jobs; promote a DB replica;
read from another region if object storage fails; clients reconnect to another notification
server (long-poll connections are lost and must be re-established).

---

## S3-like object storage

**Scope:** create buckets; upload, download, version and list objects; very small to very large
objects; 100 PB/year; 6 nines durability; 4 nines availability; low cost.

**Storage types:** block storage (raw volumes for VMs and databases, fastest, priciest), file
storage (shared POSIX-style folders), object storage (flat namespace, HTTP API, immutable
objects, cheapest, slower, vast scale). Object storage is written once and read many times
(~95% reads).

**Core idea, like a UNIX inode:** keep **metadata** (names, IDs, ACLs) separate from **data**
(the bytes), and scale each independently. Objects are immutable: replace or delete, never edit.

**Components:** load balancer; stateless API service; IAM (authn, authz); data store; metadata
store.
- Upload: authorise -> stream bytes to the data store, which returns an object UUID -> write
  `(bucket, name, object_id, metadata)` to the metadata store.
- Download: authorise -> look up the UUID by name -> read bytes by UUID.

**Data store internals**
- **Data routing service** (stateless): asks the placement service where to write, reads and
  writes data nodes.
- **Placement service:** keeps the cluster map (racks, hosts, disks), receives heartbeats, picks
  the replica group for a UUID deterministically via consistent hashing. It is critical, so run
  5 or 7 replicas with Raft or Paxos (7 survives 3 failures).
- **Data nodes:** the primary writes locally and replicates to two secondaries before
  acknowledging (strong consistency, higher latency).

**Crux 1 - small objects:** one file per object wastes disk blocks and exhausts inodes. Append
many objects into large files (a few GB, write-ahead-log style) and keep an object mapping table
`(object_id, file_name, offset, size)` in a local embedded DB (SQLite) on each node. Writes to an
open file are serialised, so give each CPU core its own open file.

**Crux 2 - durability:**
- Replicate across **failure domains** (rack, data center, power, network), not just disks.
  Three copies at ~0.81% annual disk failure rate give about 6 nines.
- **Erasure coding** (for example 8 data + 4 parity chunks across domains) survives 4 lost
  chunks, costs ~50% extra storage versus 200% for 3 replicas, and reaches far higher durability,
  but reads gather chunks from many nodes and writes cost CPU. Replication for latency-sensitive
  data; erasure coding for cheap durability.
- **Checksums** on every object and file detect silent corruption; with erasure coding verify
  each chunk.

**Metadata:** buckets table is small (per-user bucket limits) -> one DB with replicas for reads.
Objects table is huge -> shard by `hash(bucket_name, object_name)`, which matches lookups by
name. Listing by prefix (`LIKE 'photos/%'`) then hits every shard, making pagination messy, so
keep a **denormalised listing table sharded by bucket** for list operations.

**Versioning:** each upload of the same name gets a new `object_version` (time-ordered UUID) and
a new object ID; a delete inserts a **delete marker** version, and reads of a deleted name return
404.

**Multipart upload:** initiate -> upload ID; upload parts in parallel, each acknowledged with an
ETag (checksum); complete with the list of parts and ETags -> the store assembles the object.
**Garbage collection:** lazily deleted objects, orphaned parts, corrupt data. **Compaction**
copies live objects into a new file, updates the mapping table in one transaction, then frees the
old file; batch small files to avoid churn.

---

## Distributed email service (Gmail-like)

**Scope:** 1B users; send, receive, fetch, filter and search mail; attachments; anti-spam; web
clients over HTTP (SMTP still used between mail servers). Reliable (no loss), available,
scalable, extensible.
**Numbers:** ~100k send QPS; ~730 PB/year of metadata and ~1,460 PB/year of attachments.

**Protocols:** SMTP sends between servers; POP downloads and deletes from the server; IMAP keeps
mail on the server; HTTPS for web clients. DNS **MX records** say which servers accept mail for a
domain. Attachments travel base64-encoded, commonly capped around 25 MB.

**Architecture:** webmail clients -> web servers (REST: send, folders, messages) and
**real-time servers** (WebSocket, long-polling fallback, to push new mail); metadata DB;
attachment object store; distributed cache of recent mail; search store.

**Send flow:** load balancer (rate limits) -> web servers validate size and policy (same-domain
mail short-circuits to local delivery after a spam check) -> outgoing queue (attachments
referenced from the object store) -> SMTP outgoing workers run spam and virus checks and deliver
-> copy stored in Sent. Failed validations go to an error queue. Watch queue size: growth means a
remote server is down (retry with exponential backoff) or workers are too few.
**Receive flow:** SMTP load balancer -> SMTP servers apply acceptance policy -> large attachments
to object storage -> incoming queue -> processing workers (spam, virus) -> storage, cache, object
store -> real-time servers push to online users; offline users pull later.

**Crux - metadata store:** headers are small and hot, bodies are read once, almost every
operation is scoped to one user, recent mail dominates, and loss is unacceptable. At this scale
mail providers build custom stores; in a design, describe a wide-column store partitioned by
`user_id` with clustering keys for order (`email_id` as a time UUID), strong consistency, and easy
incremental backups. Wide-column stores cannot filter on non-key columns, so **denormalise per
query** (separate read and unread tables; move rows on mark-as-read). Threads come from the
`Message-Id`, `In-Reply-To` and `References` headers. Choose consistency over availability: during
a failover a user's mailbox is briefly read-only rather than wrong.

**Deliverability** (the hard business part): dedicated sending IPs warmed up over weeks; separate
marketing and transactional mail; ban spammers fast; process ISP feedback loops; authenticate
with SPF, DKIM and DMARC.

**Search:** per-user, write-heavy (every new mail is indexed, searches are rare), must be
accurate and fresh. Use a search cluster partitioned by `user_id`, indexing asynchronously from a
queue while queries stay synchronous; or a custom LSM-based index co-located with the mail store
for larger scale.

**Wrap-up topics:** multi-DC with leader/follower failover; GDPR and PII handling; encryption,
phishing protection, safe browsing; dedupe repeated attachments.
