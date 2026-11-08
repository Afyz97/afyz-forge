---
name: session-orchestrator--trigger-3
description: Per-call effort unavailable. The user states CLAUDE_CODE_EFFORT_LEVEL is pinned; the skill must switch to model routing only, name the env var in the mode line, and omit effort on every Agent call.
tags: [session-orchestrator, trigger, fallback, effort]
runs: 1
max_turns: 40
timeout_seconds: 1200
allowed_tools: [Skill, Read, Glob, Grep, Agent, Write, Edit]
plugins: ["../../.."]
---

Use subagents to audit this repo read-only: one agent lists every TODO comment, another checks the HTTP handler for security problems. Heads up: our environment pins CLAUDE_CODE_EFFORT_LEVEL=low, so per-call effort settings won't take effect here.
