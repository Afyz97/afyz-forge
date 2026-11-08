---
name: ui-accessibility--trigger-1
tags: [ui-accessibility, trigger]
runs: 1
max_turns: 4
timeout_seconds: 240
allowed_tools: [Skill, Read, Glob, Grep]
plugins: ["../../.."]
---

Is this modal accessible? Focus seems to escape it and screen readers don't announce the title.
