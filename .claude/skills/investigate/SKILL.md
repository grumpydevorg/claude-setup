---
name: investigate
description: >
  Investigates codebases to find related files, dependencies, and patterns.
  Use when: (1) user describes a bug or issue to fix, (2) user asks "where is X handled",
  (3) user wants to understand code relationships, (4) implementing features that touch multiple files.
  Delegates to investigator agent for deep analysis.
---

# Code Investigation

Automatically triggers when users need to understand code relationships or locate relevant files for a problem.

## Delegation

This skill delegates to the **investigator** agent defined in `.claude/agents/investigator.md`.

Use the investigator subagent with the following prompt:
- Pass the user's problem/question
- If a claude-instance directory exists, pass its path for report output
- Otherwise, provide findings directly

## When to Auto-Invoke (vs /task_medium)

- **Use this skill**: Quick investigation, single questions, understanding code
- **Use /task_medium**: Full structured workflow with reports, planning, and approval
