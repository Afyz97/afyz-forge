# Back-of-the-envelope estimation

Rough numbers decide whether a design is even plausible. Precision does not matter, but the
working must be visible: write every assumption down, label every unit, and round hard.

## Rules

1. List assumptions first, numbered, so anyone can challenge one input without redoing all of it.
2. Round aggressively: 99,987 / 9.1 becomes 100,000 / 10. Keep one significant figure.
3. Always attach units (`5 MB`, never `5`). Most estimation mistakes are unit slips.
4. Estimate the **peak**, not just the average. Use 2x the average by default, 5x for bursty
   domains (market open, sales, sports events, ad traffic).
5. Multiply storage by the **replication factor** (usually 3) and by the retention period.
6. Sanity-check the result against the calibration table at the bottom.

## Unit shortcuts

| Power | Approx. value | Name | Bytes |
|---|---|---|---|
| 2^10 | 1 thousand | Kilo | 1 KB |
| 2^20 | 1 million | Mega | 1 MB |
| 2^30 | 1 billion | Giga | 1 GB |
| 2^40 | 1 trillion | Tera | 1 TB |
| 2^50 | 1 quadrillion | Peta | 1 PB |

- 1 day = 86,400 s. Rounding to 10^5 s is fine for speed but gives a result about 14% low.
- 1M requests per day is about 12 per second. 1B per day is about 12,000 per second.
- 1 month ~ 2.5 million seconds. 1 year ~ 30 million seconds.

## Latency orders of magnitude

Approximate values (circa 2020 hardware). Learn the ratios, not the digits.

| Operation | Approx. latency |
|---|---|
| L1 cache reference | 0.5 ns |
| L2 cache reference | 7 ns |
| Main memory reference | 100 ns |
| Compress 1 KB with a fast compressor | 10 us |
| Send 2 KB over a 1 Gbps network | 20 us |
| SSD random read | 150 us |
| Read 1 MB sequentially from memory | 250 us |
| Round trip inside one data center | 500 us |
| Disk seek (spinning disk) | 10 ms |
| Read 1 MB sequentially from the network | 10 ms |
| Read 1 MB sequentially from a spinning disk | 30 ms |
| Packet round trip between continents | 150 ms |

Conclusions that drive designs:
- Memory is fast and disk seeks are slow, so keep hot data in memory and make disk access
  sequential (append-only logs, batching).
- Simple compression is cheap relative to sending bytes, so compress before crossing a network.
- Cross-region round trips cost about 300 times an in-DC hop, so keep chatty calls inside one
  region and replicate data closer to users.

## Availability in nines

| Availability | Downtime per year | Downtime per day |
|---|---|---|
| 99% | 3.65 days | 14.4 min |
| 99.9% | 8.77 hours | 1.44 min |
| 99.99% | 52.6 min | 8.6 s |
| 99.999% | 5.26 min | 0.86 s |
| 99.9999% | 31.5 s | 86 ms |

Components in series multiply: two 99.9% services in a chain give about 99.8%. Redundant
copies in parallel raise availability, which is why every tier gets a spare.

## Formulas

```
QPS (avg)        = DAU x actions_per_user_per_day / 86,400
Peak QPS         = QPS x peak_factor                      (2x default, 5x bursty)
Write storage/day= writes_per_day x bytes_per_item
Total storage    = storage/day x 365 x years x replication_factor
Bandwidth        = QPS x bytes_per_response               (ingress and egress separately)
Cache memory     = ~20% of the daily hot read set         (80/20 heuristic; measure later)
Servers          = peak QPS / sustainable QPS per server  (benchmark; never assume it)
DB nodes         = peak TPS / sustainable TPS per node     (x2 if each operation writes twice)
```

## Worked example - a microblogging service

Assumptions: 300M MAU, 50% use it daily, 2 posts per user per day, 10% of posts carry 1 MB of
media, keep media for 5 years.

- DAU = 300M x 0.5 = 150M
- Post QPS = 150M x 2 / 86,400 = ~3,500; peak (2x) = ~7,000
- Media per day = 150M x 2 x 10% x 1 MB = 30 TB
- Media over 5 years = 30 TB x 365 x 5 = ~55 PB (before replication)

## Calibration numbers from the blueprints

Use these to check that your own result is in a believable range. Values are the assumptions
and results used in the case files, recomputed where the original arithmetic was off.

| System | Key assumptions | Result |
|---|---|---|
| URL shortener | 100M new URLs/day, 10:1 reads, 10 years, ~100 B per URL | ~1,160 writes/s, ~11,600 reads/s, 365B records, ~36.5 TB |
| Web crawler | 1B pages/month, 500 KB avg page, 5 years | ~400 pages/s (peak 800), 500 TB/month, ~30 PB |
| Notifications | 10M push, 1M SMS, 5M email per day | ~185 sends/s average across channels |
| Chat | 50M DAU, 1-to-1 and groups up to 100 | connection count, not QPS, is the limit |
| Autocomplete | 10M DAU, 10 searches/day, ~20 keystroke requests per search | ~24,000 QPS, peak ~48,000; ~0.4 GB/day new query data |
| Video platform | 5M DAU, 10% upload one 300 MB video/day; 5 views/day | 150 TB/day new storage; CDN ~$150k/day at $0.02/GB |
| File sync | 50M users x 10 GB quota; 10M DAU x 2 uploads/day at 500 KB | 500 PB allocated; ~240 upload QPS, peak ~480 |
| Proximity search | 100M DAU x 5 searches, 200M businesses | ~5,000 search QPS |
| Nearby friends | 10M concurrent users, update every 30 s, ~40 online friends each | ~334k updates/s, ~14M fan-out pushes/s |
| Maps | 1B DAU, 35 min navigation per week, batched GPS updates | ~200k QPS, peak ~1M |
| Metrics | 1,000 pools x 100 hosts x 100 metrics | ~10M time series |
| Ad-click aggregation | 1B clicks/day, 0.1 KB each | ~10k QPS (peak 50k), 100 GB/day, 3 TB/month |
| Hotel booking | 5,000 hotels, 1M rooms, 70% occupancy, 3-night stays | ~240k reservations/day, ~3 TPS |
| Email | 1B users, 10 sent and 40 received/day, 50 KB metadata, 20% with 500 KB attachments | ~100k send QPS, ~730 PB/year metadata, ~1,460 PB/year attachments |
| Object storage | 100 PB, 40% utilised, size mix 20% 0.5 MB / 60% 32 MB / 20% 200 MB | ~0.68B objects, ~0.68 TB metadata at 1 KB each |
| Leaderboard | 5M DAU, 10 games/day, 25M MAU | ~500 score QPS (peak 2,500); ~650 MB sorted set |
| Payments | 1M transactions/day | ~10 TPS: correctness, not throughput, is the problem |
| Digital wallet | 1M transfers/s, 2 writes each, ~1,000 TPS per RDBMS node | ~2,000 nodes, so raise per-node TPS instead |
| Stock exchange | 1B orders over a 6.5 h session, 100 symbols | ~43k QPS, peak ~215k at the open |

Reading the table: when throughput is tiny (payments, hotel), the design is about correctness;
when it is huge (nearby friends, wallet, exchange), it is about removing hops, batching and
partitioning.
