# system-design

A system design toolkit for Claude Code, built from a study of the
[liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes) chapter notes
(28 chapters). The guidance is rewritten and reorganised for agent use. See [NOTICE.md](NOTICE.md).

## Skills

| Skill | Invocation | What it does |
|---|---|---|
| `system-design` | Automatic | Designs a system end to end: 4-step method (scope and estimate, high-level, deep dive, wrap-up), storage-by-access-pattern table, signal -> pattern map, design-doc template. References: estimation (formulas, latency numbers, nines, calibration numbers from 19 systems), the scale ladder, a Laravel stack mapping and **22 blueprints** in 6 case files. |
| `distributed-patterns` | Automatic | Answers single-mechanism questions with defaults and trade-offs: rate limiting, caching/CDN, sharding, consistent hashing, replication, CAP, quorum, vector clocks, gossip, Merkle trees, Raft, IDs, Bloom filters, queues and delivery semantics, stream windows and watermarks, idempotency, locking, 2PC/TC-C/saga, event sourcing, ledgers, reconciliation, LSM, erasure coding, geohash/quadtree/S2, WebSocket/SSE/long polling, presence. |
| `system-design-review` | Automatic | Reviews an existing design doc or backend codebase: checklist across redundancy, state, data tier, async work, money correctness, abuse, real-time and observability; severity-ranked findings with evidence, the first bottleneck and top 3 fixes. Includes Laravel config smells. |
| `system-design-interview` | `/system-design:system-design-interview [problem]` | Mock interview: Claude plays the interviewer on a 45-minute budget, then scores you on 6 dimensions and compares with the reference blueprint. |

## Blueprints

| File | Systems |
|---|---|
| `cases/web-services.md` | URL shortener, web crawler, notification system, search autocomplete |
| `cases/social-realtime.md` | News feed, chat, nearby friends, real-time leaderboard |
| `cases/media-storage.md` | Video streaming, file sync (Drive), S3-like object storage, email service |
| `cases/geo.md` | Proximity search, maps and navigation |
| `cases/data-infra.md` | Distributed message queue, metrics and alerting, ad-click aggregation, plus key-value store, rate limiter, ID generator, consistent hashing |
| `cases/money-and-booking.md` | Hotel reservation, payment system, digital wallet, stock exchange |

## Layout

```
plugins/system-design/
  .claude-plugin/plugin.json
  skills/
    system-design/            SKILL.md + references/{estimation,scaling-ladder,stack-mapping}.md + references/cases/*.md
    distributed-patterns/     SKILL.md + references/ (7 topic files)
    system-design-review/     SKILL.md
    system-design-interview/  SKILL.md (manual command)
  evals/                      trigger / no-trigger routing evals for the 3 automatic skills
```

The skills link to each other with relative paths (`../distributed-patterns/references/...`), so
install the plugin as a whole.

## Install

```
/plugin marketplace add Afyz97/ai-skills
/plugin install system-design@ai-skills
```

## Validate and test

```
claude plugin validate --strict ./plugins/system-design
claude plugin eval ./plugins/system-design --ablation none
```

## Notes on accuracy

Numbers in the blueprints come from the source notes and were re-derived. Two arithmetic slips
in the source were corrected: URL-shortener storage is ~36.5 TB for 365B records at ~100 B each
(not 365 TB), and the leaderboard example uses 5M DAU consistently.
