---
name: trace-flow
description: >
  Traces code execution paths, dependencies, and file interconnections.
  Use when: (1) user asks "how does X work", (2) user needs to understand call chains,
  (3) tracing data flow through the application, (4) mapping component relationships.
  Delegates to code-flow-mapper agent for deep analysis.
---

# Code Flow Tracing

Automatically triggers when users need to understand how code executes or how files connect.

## Delegation

This skill delegates to the **code-flow-mapper** agent defined in `.claude/agents/code-flow-mapper.md`.

Use the code-flow-mapper subagent with the following prompt:
- Pass the specific flow/feature to trace
- If an INVESTIGATION_REPORT.md exists, reference it
- If a claude-instance directory exists, pass its path for report output
- Otherwise, provide flow analysis directly

## When to Auto-Invoke (vs /task_medium)

- **Use this skill**: Quick flow questions, understanding execution paths
- **Use /task_medium**: Full structured workflow with investigation + flow + planning
