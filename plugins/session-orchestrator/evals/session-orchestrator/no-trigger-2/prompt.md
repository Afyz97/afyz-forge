---
name: session-orchestrator--no-trigger-2
tags: [session-orchestrator, no-trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

What does the findOrder function in src/orders.js return when the id isn't found?
