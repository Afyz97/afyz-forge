---
name: session-orchestrator--trigger-2
description: Read-only audit. Read-only roles may run immediately because the user asked for orchestration.
tags: [session-orchestrator, trigger, read-only]
runs: 1
max_turns: 40
timeout_seconds: 1200
allowed_tools: [Skill, Read, Glob, Grep, Agent, Write, Edit]
plugins: ["../../.."]
---

Orchestrate a read-only audit of this repo with subagents: one pass for TODO comments, one for dead or unused code, one for security issues in the HTTP handler. Don't change any project files; just report back.
