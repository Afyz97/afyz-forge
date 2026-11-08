# Mapping designs onto a Laravel stack

Most designs here can start on a plain Laravel + MySQL/PostgreSQL + Redis deployment. Use this
table to turn boxes in a diagram into concrete framework features, and to see where the
framework stops and dedicated infrastructure starts. Check the installed Laravel version before
relying on a newer helper.

## Component map

| Design component | Laravel feature | Notes and limits |
|---|---|---|
| Stateless web tier | `SESSION_DRIVER=redis` or `database`; files on an `s3` disk | `file` sessions or the `local` disk break as soon as there are two servers |
| Read replicas | `read` / `write` hosts in `config/database.php`, `'sticky' => true` | Sticky gives read-your-writes within one request only |
| Cache-aside | `Cache::remember($key, $ttl, fn () => ...)`; `Cache::forget` after writes | `Cache::flexible()` (newer versions) serves stale while refreshing |
| Distributed lock | `Cache::lock('name', $seconds)->block($wait, fn () => ...)` | Needs a shared store (Redis); release in `finally` or use the callback form |
| Rate limiter | `RateLimiter::for(...)` + `throttle:` middleware; `Limit::perMinute(60)->by($key)` | Counter per decay window (fixed-window behaviour); for bursts use a token bucket in Redis with a Lua script |
| Queue + workers | `QUEUE_CONNECTION=redis`, Horizon for supervision and metrics | Never `sync` in production for slow work |
| Retry with backoff | Job `$tries`, `$backoff = [10, 60, 300]`, `retryUntil()` | Exponential schedule via the array |
| Dead-letter queue | `failed_jobs` table, `queue:failed`, `queue:retry` | Alert on growth; inspect before retrying payments |
| Deduplicated jobs | `ShouldBeUnique`, `WithoutOverlapping` middleware | Dedupes dispatch, not side effects: consumers still need idempotency |
| Dispatch after commit | `afterCommit()` / `after_commit => true` | Prevents workers reading rows that were rolled back |
| Pub/sub fan-out | Events with queued (`ShouldQueue`) listeners | One event, many independent side effects |
| Server push | Broadcasting + Laravel Reverb (WebSocket) + Echo; presence channels | Reverb is a stateful tier: scale it horizontally with Redis pub/sub |
| Scheduled and batch jobs | Scheduler, `->onOneServer()`; `Bus::batch()` | Reconciliation and rollups live here |
| Notifications | Notification classes with mail, database, broadcast, SMS channels; queued | Per-user channel preferences live in your own table |
| Full-text search | Scout with Meilisearch, Typesense or Algolia; `queue => true` | Index updates are async, so search is eventually consistent |
| Pessimistic lock | `DB::transaction(fn () => Model::whereKey($id)->lockForUpdate()->first())` | Keep the transaction short; retries via the attempts argument |
| Optimistic lock | `where('version', $v)->update([..., 'version' => $v + 1])`, check affected rows | 0 rows updated = conflict; reload and retry or report |
| Idempotency key | Unique index + `createOrFirst()`, or catch `UniqueConstraintViolationException` | Return the stored result for a repeated key |
| Time-sortable IDs | `HasUlids`, or `HasUuids` (ordered UUIDs) | 128-bit; use a Snowflake-style generator only if you need 64-bit integers |
| Money | `decimal` columns or integer minor units (`amount_cents`) | Never `float` or `double` |
| Leaderboard | `Redis::zincrby`, `zrevrange`, `zrevrank` | Rebuild from the DB if Redis is lost |
| Geo search | Redis `GEOADD` / `GEOSEARCH`, or MySQL `POINT` + spatial index + `ST_Distance_Sphere` | Redis GEO is geohash-based; cache results by cell |
| Large uploads | `Storage::temporaryUploadUrl()` (S3) for direct-to-storage uploads | Keeps big bodies off PHP workers |
| Observability | Pulse, Horizon metrics, log channels to a central sink | Alert on queue wait time, failed jobs, p99 latency |

## Where Laravel stops

Laravel is the application tier. These pieces are separate infrastructure even in a Laravel
project: load balancer, CDN, object storage, Redis cluster, partitioned log (Kafka-style),
time-series DB, search engine, coordination service, and anything needing microsecond latency
or a single-threaded deterministic core (matching engines). Sharding across databases is also
manual: multiple connections plus routing code keyed by the shard key.

## Quick configuration checks for multi-server deployments

```
SESSION_DRIVER   != file      CACHE_STORE      != file / array
QUEUE_CONNECTION != sync      FILESYSTEM_DISK  != local (for user uploads)
Scheduler uses ->onOneServer() for jobs that must run once
Broadcasting has a horizontally scalable backend (Reverb with Redis, or a hosted service)
```
