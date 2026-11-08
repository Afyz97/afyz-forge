---
name: session-orchestrator--no-trigger-1
tags: [session-orchestrator, no-trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Rename the function getUser to fetchUser in src/users.js.
