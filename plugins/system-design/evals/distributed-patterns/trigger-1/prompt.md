---
name: distributed-patterns--trigger-1
tags: [distributed-patterns, trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Should I use a token bucket or a sliding window counter for our API rate limiter, and how do I keep it atomic in Redis?
