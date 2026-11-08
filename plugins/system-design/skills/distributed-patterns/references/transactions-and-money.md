# Transactions, concurrency and money

## Idempotency

An operation is idempotent if repeating it has the same effect as doing it once. Required on every
write that books, charges, transfers or sends.

**Mechanism:**
1. The client generates a unique key (UUID) **before** the first attempt - for example when the
   checkout or booking form is created - and sends it with every retry (`Idempotency-Key` header,
   or a `reservation_id` / `payment_order_id` / `transaction_id` field).
2. The server inserts the key under a **unique constraint** in the same transaction as the
   business write.
3. A duplicate insert fails; the server returns the stored result of the first attempt instead
   of redoing the work.
4. Forward the key to downstream providers (PSPs accept one) so they dedupe too.

Disabling the button in the UI is a nicety, not a guarantee (scripts, retries, double taps).

## Concurrency on shared rows (overselling, double booking, negative balances)

Check-then-act in two statements races: two transactions both see "1 left" and both book.

| Technique | How | Good when | Watch out |
|---|---|---|---|
| Pessimistic lock | `SELECT ... FOR UPDATE` inside the transaction | Short critical sections with heavy contention | Deadlocks; long transactions block everyone; poor scale |
| **Optimistic lock** | `version` column; `UPDATE ... SET ..., version = v+1 WHERE id = ? AND version = v`; 0 rows = conflict, retry | Conflicts are rare (most booking systems) | Many retries under heavy contention |
| **DB constraint** | `CHECK (available >= 0)`, or atomic `UPDATE ... SET reserved = reserved + n WHERE reserved + n <= limit` | Simple invariants, low contention | Harder to version-control; not every DB supports CHECK |
| Queue per hot item | Serialise requests for one item through a single consumer | Flash sales, extreme contention | Added latency and moving parts |

Prefer version numbers over timestamps for optimistic locking (clocks drift).

## Transactions across services or shards

First choice: **do not distribute it.** Keep the invariant inside one service and one database so a
local ACID transaction covers it (reservation and inventory together). Split only when a number
forces you.

| | 2PC | TC/C (try-confirm/cancel) | Saga |
|---|---|---|---|
| Shape | Coordinator: prepare all, then commit or abort all | Phase 1 local transactions reserve/deduct; phase 2 confirm or compensate | Ordered local transactions; on failure run compensations in reverse |
| Locks held across phases | Yes | No (each phase commits locally) | No |
| Parallel steps | Yes | Yes | No (linear) |
| Visible partial state | No | Yes | Yes |
| Logic lives in | Database protocol | Application | Application |
| Weak spots | Blocking; coordinator is a single point of failure; slow | Complex business code; out-of-order messages | Long chains; compensations must be correct |

**Saga coordination:** choreography (services react to each other's events; logic scattered) vs
**orchestration** (one coordinator drives the steps; easier to reason about - preferred for money).

**Rules for money in TC/C or sagas:**
- **Deduct before you add.** The intermediate state may only ever have *less* money in circulation,
  never more.
- Persist a **phase status table** (transaction ID and payload, phase 1 status per participant,
  phase 2 type, phase 2 status, out-of-order flag) so a crashed coordinator can resume.
- Handle **out-of-order** delivery: if a cancel arrives before its try, record that, and reject the
  late try.

## Event sourcing and CQRS

- **Command:** a request to change something ("transfer 1 from A to C"). May be rejected.
- **Event:** an immutable fact that happened ("A debited 1", "C credited 1").
- **State:** the result of applying events (current balances).
- **State machine:** validates commands against state and emits events; applies events to state.
  Must be **deterministic** (no wall clock, randomness or external I/O inside), so replay always
  gives the same result.

Benefits: the balance at any point in time (replay up to it); proof that current state is correct
(recompute from the start); safe code changes (run old and new code over the same events and
compare); natural audit trail.
- Commands and events are both ordered (FIFO queues or logs).
- Only the **event log** must be durable and replicated (Raft); state and snapshots are rebuildable,
  and commands cannot rebuild events because validation depends on state at the time.
- **Snapshots** bound replay time.
- **CQRS:** writes go through the state machine; reads come from read-only projections built from
  the events, which can push results back to callers instead of being polled.
- High-throughput versions keep the log in local append-only files (mmap) and state in a local LSM
  store (RocksDB).

## Double-entry ledger

Every movement writes two entries of equal amount: a debit to one account and a credit to another.
The sum over all entries is always zero, which makes errors detectable and every cent traceable.
Store entries append-only; derive balances from them (or maintain balances transactionally next to
them).

## Reconciliation

Distributed money flows will drift: a webhook lost, a retry after a timeout, a bug. Reconciliation
is the safety net.
- Nightly, compare an external source of truth (the PSP's settlement file, the bank statement) with
  internal records; also compare internal systems with each other (ledger vs wallet).
- Classify mismatches: known and auto-fixable; known but manual; unknown and investigated.
- Also reconcile streaming aggregates against raw events (ad billing).
- Alert on the mismatch count; it is a top-level health metric for money systems.

## Retries

Strategies: immediate, fixed interval, incremental, **exponential backoff** (default; add jitter),
cancel when the error is terminal or attempts run out. Respect a server's `Retry-After`. Retries
are only safe when the operation is idempotent.

## Payment-specific rules

- Amounts as integer minor units or decimal strings; never binary floating point.
- Card data never touches your servers: use the PSP's hosted page or SDK and store their token.
- Treat the PSP **webhook** as authoritative; the browser redirect can be lost or forged.
- Track explicit states (`NOT_STARTED -> EXECUTING -> SUCCESS | FAILED`), and a job that alerts on
  payments stuck in a state too long. Show "pending" honestly while waiting on 3-D Secure or review.
- Read balances from the primary (or a consensus-replicated store), not a lagging replica.
- Security: TLS everywhere, certificate pinning in apps, encryption at rest, rate limits, fraud
  signals (address verification, CVV, behaviour), PCI DSS scope kept minimal.
