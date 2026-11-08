# Blueprints: money and booking

Hotel reservation, payment system, digital wallet, stock exchange. In all four, throughput is
secondary until proven otherwise; **correctness** (no double booking, no double charge, every cent
accounted for) is the design. Mechanisms: `../../../distributed-patterns/references/transactions-and-money.md`.

---

## Hotel reservation (also flights, cinemas, Airbnb)

**Scope:** 5,000 hotels, 1M rooms; hotel and room pages; reserve and cancel; pay in full at booking;
admin panel; 10% overbooking allowed; prices change daily. High concurrency at peak; a few seconds
of reservation latency is fine.
**Numbers:** 1M rooms x 70% occupancy / 3-night stays -> ~240k reservations/day -> ~3 TPS. With a
~10% conversion per funnel step, ~30 QPS on the order page and ~300 QPS on room details. Small.

**API:** hotels and room types (CRUD for ops only); `GET /v1/reservations`,
`GET /v1/reservations/{id}`, `POST /v1/reservations`, `DELETE /v1/reservations/{id}`.
Reservation request: `{startDate, endDate, hotelID, roomTypeID, roomCount, reservationID}` where
`reservationID` is the **idempotency key**.

**Storage:** relational. Reads dominate, writes are few, the schema is clear, and ACID prevents
oversell and double charges.

**Crux 1 - model inventory per room type per day.** Guests book a room type, not a room number
(assigned at check-in). Table `room_type_inventory(hotel_id, room_type_id, date, total_inventory,
total_reserved)`, one row per day, pre-filled ~2 years ahead by a daily job (5,000 x 20 types x 730
days ~ 73M rows: one DB plus replicas). Availability for each night in the range:
`total_reserved + requested <= 1.1 x total_inventory` (overbooking).

**Crux 2 - concurrency:**
- *Same user clicks twice:* disabling the button is not enough. Generate the reservation ID when the
  order form is created; submit it with the request; a **unique constraint** on it rejects the second
  insert and you return the first result.
- *Two users race for the last room:* check-then-update in two statements oversells unless guarded:
  - **Pessimistic lock** (`SELECT ... FOR UPDATE`): simple, serialises; deadlock risk and poor scale
    under long transactions. Avoid as the default.
  - **Optimistic lock** (version column; update only if the version is unchanged, else retry):
    fast when conflicts are rare - a good fit here.
  - **DB constraint** (`CHECK (total_inventory * 1.1 - total_reserved >= 0)`): simplest; also fine at
    low contention, though constraints are harder to version and not supported everywhere.
  Under very high contention (flash sales), queue requests per room type instead.

**Scale (booking.com-sized, ~1000x):** services are stateless; shard the DB by `hotel_id` (every
query has it; e.g. 30k QPS over 16 shards ~ 1.9k each); cache availability in Redis
(`hotelId_roomTypeId_date -> available`, TTL past dates) fed by **change data capture** from the DB.
The cache may lag, but the DB constraint still blocks invalid bookings; the UI just shows "sold out"
a moment late. Move past reservations to cold storage.

**Microservice consistency:** keeping reservation and inventory in **one service and one DB** lets
one ACID transaction cover both - pragmatic and usually right. Split them and you need 2PC (blocking)
or a saga (compensations, eventual consistency); count that complexity before splitting.

**Architecture:** CDN; public API gateway (auth, rate limiting); hotel service (cache aggressively);
rate service (prices per future date, which depend on occupancy); reservation service (owns
inventory); payment service; internal hotel-management service behind a VPN; gRPC between services.

---

## Payment system (e-commerce checkout)

**Scope:** pay-in (customers pay the platform on behalf of sellers) and pay-out (platform pays sellers);
cards via a payment service provider (PSP) such as Stripe or Adyen; card data never stored by us;
one currency; 1M transactions/day (~10 TPS). Reliability, fault tolerance, and reconciliation with
internal and external systems are the requirements.

**Pay-in components:** payment service (accepts a payment event, runs risk/AML checks, coordinates);
payment executor (executes each payment order through the PSP); PSP; card schemes; **ledger**
(double-entry record of every money movement); **wallet** (seller balances).
Flow: place order -> payment service stores the event -> for each order, the executor stores it and
calls the PSP -> on success the wallet balance and the ledger are updated.

**API:** `POST /v1/payments {buyer_info, checkout_id, credit_card_info, payment_orders[]}` where each
order has `seller_account, amount, currency, payment_order_id`. `payment_order_id` is the idempotency
key forwarded to the PSP. **Amount is a string** (or integer minor units), never a float.
`GET /v1/payments/{id}` for status.

**Data:** relational with ACID, proven in finance, good tooling and DBAs. `payment_events(checkout_id
PK, buyer_info, seller_info, credit_card_info, is_payment_done)`; `payment_orders(payment_order_id PK,
buyer_account, amount, currency, checkout_id FK, status NOT_STARTED|EXECUTING|SUCCESS|FAILED,
ledger_updated, wallet_updated)`. A background job watches in-flight orders and alerts on stuck ones.

**Double-entry ledger:** every movement is a debit on one account and an equal credit on another;
all entries sum to zero; this gives end-to-end traceability.

**PSP integration (hosted payment page):** checkout -> payment service registers the payment with the
PSP (amount, currency, our order UUID as nonce) -> PSP returns a token, stored by us -> the PSP's
hosted page (iframe, SDK or redirect) collects card details -> PSP processes and redirects back with
the token and result -> **the PSP also calls our webhook**, which is the authoritative status.
This keeps card data, and most PCI scope, out of our systems.

**Crux 1 - reconciliation:** the happy path is not enough. Nightly, compare the PSP's **settlement
file** with our ledger and wallet (and the ledger with the wallet). Mismatches are: classifiable and
auto-fixable; classifiable but manual; unclassifiable and investigated by finance.

**Crux 2 - exactly-once:** exactly-once = at-least-once (retries) + at-most-once (idempotency).
- Retries: exponential backoff by default; honour `Retry-After`; cap attempts; failed payments go to
  a **retry queue**, terminal ones to a **dead-letter queue** for inspection. Decide retry vs refund
  from the payment's recorded state.
- Idempotency: clients send an `Idempotency-Key` (a UUID); the server inserts it under a unique
  constraint; a duplicate insert returns the original result. The PSP dedupes on our nonce too, so a
  retry after a PSP success cannot charge twice.

**Slow payments:** risk review or 3-D Secure can take hours. Show a pending state, wait for the
webhook (or poll the PSP), notify the user when done.

**Internal communication:** synchronous HTTP chains are slow, fragile and tightly coupled. Publish
payment results to a queue that **several services consume** (ledger, wallet, analytics,
notifications). Accept eventual consistency and keep it honest with reconciliation.

**Consistency with replicas:** serve reads and writes from the primary and use replicas only for
failover, or use a consensus-replicated database (Raft-based) so replicas never lag.

**Security:** HTTPS everywhere; encryption and integrity checks; certificate pinning on mobile;
multi-region replication and snapshots; rate limiting and firewalls; tokenised cards; PCI DSS;
fraud checks (address verification, CVV, behaviour analysis).
**Pay-out:** same shape, money moves from the platform to sellers' banks, usually via a payouts
provider, with heavy bookkeeping and regulatory work.

---

## Digital wallet (balance transfers)

**Scope:** transfers between wallets only; 1M TPS; 99.99% availability; transactional; and
**reproducible** - be able to replay history to rebuild any past balance (reconciliation only finds
discrepancies, not their cause).
**Numbers:** each transfer touches two accounts, so ~2M writes/s; at ~1,000 TPS per relational node
that is ~2,000 nodes. The design goal becomes **raising per-node throughput**.

**API:** `POST /v1/wallet/balance_transfer {from_account, to_account, amount (string), currency,
transaction_id (idempotency key)}`.

**Evolution of the design**
1. **Sharded Redis** `account -> balance` (partition map in ZooKeeper): fast, but not durable and no
   atomic transfer across two shards.
2. **Sharded relational DBs + distributed transactions:**
   - **2PC:** coordinator asks all shards to prepare, then commit or abort. Holds locks, blocks if the
     coordinator dies.
   - **TC/C (try-confirm/cancel):** two independent local transactions with compensation. Try debits
     A (C does nothing); confirm credits C; cancel refunds A. **Always deduct before adding**, so the
     in-between state never lets money be spent twice. Persist a **phase status table** (transaction,
     try status, second phase, its status, out-of-order flag) to recover a crashed coordinator; the
     flag handles a cancel that arrives before its try.
   - **Saga:** a linear sequence of local transactions, compensated in reverse on failure;
     orchestration (one coordinator) beats choreography for wallets. TC/C can run steps in parallel,
     saga cannot - pick TC/C for lower latency.
3. **Event sourcing** for auditability: commands (requested transfers, may fail) go into a FIFO
   queue; a **deterministic state machine** validates each against current state and emits events
   (immutable facts: "A -1", "C +1"); applying events produces state (balances). Replaying events
   reproduces any past balance, verifies current balances, and lets new code be checked against old
   results. Reads go to read-only projections (**CQRS**).
4. **High performance:** keep commands and events in local append-only files (mmap), cache recent
   ones in memory, store state in a local embedded DB (RocksDB, LSM-based, write-optimised), and save
   periodic **snapshots** so replays start from a recent point.
5. **Reliability:** only the **event list** must be durable (state and snapshots can be rebuilt;
   commands are non-deterministic, so they cannot rebuild events). Replicate the event log with
   **Raft**: the leader appends, followers replicate; the group survives while a majority lives.
6. **Scale out:** shard accounts across many Raft groups; a saga or TC/C coordinator spans shards.
   To avoid client polling, put a reverse proxy in front that submits commands and receives pushed
   results from the read side.

**Lifecycle of a cross-shard transfer:** client -> coordinator writes a phase status row -> sends
`A-1` to partition 1's Raft leader -> validated, turned into an event, replicated -> read side
pushes the result back -> coordinator records success and sends `C+1` to partition 2 -> same ->
coordinator records completion and replies to the client.

---

## Stock exchange

**Scope:** stocks only; place and cancel **limit orders**; normal trading hours; real-time fills
and order book; tens of thousands of concurrent users, ~100 symbols, billions of orders/day; risk
checks (e.g. max daily volume per user); funds withheld for open orders. 99.99% availability,
millisecond-level round trips judged at p99, KYC, DDoS protection.
**Numbers:** 1B orders over 6.5 h -> ~43k QPS; peak ~5x (~215k) at the open.

**Concepts:** brokers connect retail users; institutional clients split large orders. Limit order
(fixed price, may rest or fill partially) vs market order (executes now). Bid = best buy price,
ask = best sell price. Market data levels: L1 (best bid/ask), L2 (several price levels), L3
(queue depth per order at each level). Candlesticks (open, high, low, close, volume) per interval.
FIX is the industry wire protocol.

**Three flows**
- **Trading (critical path, latency-sensitive):** client gateway (auth, validation, rate limit;
  keep it thin) -> order manager (risk checks, wallet funds check and hold, order state) ->
  **sequencer** -> **matching engine** -> fills back via the sequencer -> order manager -> gateway.
- **Market data:** execution stream -> market data publisher builds order books and candlesticks
  -> data service -> subscribers.
- **Reporting (off critical path, accuracy over speed):** orders and executions written to a DB for
  history, tax, compliance and settlement.

**Matching engine:** one order book per symbol; a match emits two fills (buy and sell); output
order must be **deterministic**. Order book: per side, a map of price -> price level, each level a
doubly linked FIFO list of orders, plus a map of order ID -> node, so add, match and cancel are
O(1) and best bid/ask is tracked. Matching is price-time priority (FIFO within a price).

**Sequencer:** stamps every inbound order and outbound fill with a sequence number. This gives
fairness, deterministic replay for fast recovery, and exactly-once handling (gaps and duplicates are
visible). A log like Kafka could do it, but a custom one is far lower latency.

**Crux - latency:** a classic multi-service layout gives tens of milliseconds; the goal is tens of
microseconds. So: strip everything (even logging) from the critical path; put gateway, order
manager, sequencer and matching on **one server**, communicating through an **mmap-ed event store**
(in `/dev/shm`, so no disk I/O); run each component as a single-threaded **application loop
pinned to a CPU core** (no context switches, no locks); package the order manager as a library
inside each component. Watch p99 and p99.99, and avoid GC pauses (or use a GC-free runtime style).

**Event sourcing:** the sequencer is the single writer to the event store; every component
subscribes and rebuilds state from events, which also makes hot standbys trivial.

**Availability and fault tolerance (99.99% ~ 8.6 s down per day):** a hot standby matching engine
consumes the same events but does not publish; heartbeats detect primary failure; replicate the
event store across servers (reliable UDP) and elect a leader with Raft. Fail over manually at first
until failure modes are understood; use chaos testing; define recovery time and point objectives.
Data loss is unacceptable, so replicate and back up continuously.

**Market data:** **ring buffers** (preallocated, lock-free; pad sequence counters onto their own
cache lines) for candlesticks; keep limited history in memory; columnar time-series DB (kdb+-style)
for real-time analytics, a historical DB after the close. Fairness: publish to all subscribers
simultaneously with **multicast** over reliable UDP. **Colocation** lets brokers place servers in
the exchange's data center (a paid latency tier).

**Security:** separate public services from trading paths; cache public read-only data; use
cacheable URLs (`/data/recent`, not arbitrary query ranges); allowlists and blocklists; rate limits.
