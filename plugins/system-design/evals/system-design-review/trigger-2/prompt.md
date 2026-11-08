---
name: system-design-review--trigger-2
tags: [system-design-review, trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Do a production readiness review of this booking service design. Two users can book the last room at the same time and we store prices as floats.
