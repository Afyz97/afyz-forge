---
name: ui-critique--no-trigger-1
tags: [ui-critique, no-trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Run a full WCAG 2.2 AA audit on the checkout page.
