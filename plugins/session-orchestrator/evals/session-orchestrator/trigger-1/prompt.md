---
name: session-orchestrator--trigger-1
description: Multi-part feature build. Writer roles must wait for approval, so the run should end at the plan.
tags: [session-orchestrator, trigger, feature, approval-gate]
runs: 1
max_turns: 30
timeout_seconds: 900
allowed_tools: [Skill, Read, Glob, Grep, Agent, Write, Edit]
plugins: ["../../.."]
---

Split this up and use subagents: add a GET /orders.csv endpoint that exports all orders as CSV, write tests for it, and document it in the README. Plan it first.
