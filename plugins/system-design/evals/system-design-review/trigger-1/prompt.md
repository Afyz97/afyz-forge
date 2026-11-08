---
name: system-design-review--trigger-1
tags: [system-design-review, trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Review our architecture doc: one Laravel server with file sessions, MySQL with no replicas, and payments processed synchronously in the checkout controller. What breaks first at 10x traffic?
