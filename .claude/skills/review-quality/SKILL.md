---
name: review-quality
description: >
  Reviews code for quality, security, and maintainability issues.
  Use when: (1) user asks about code quality, (2) reviewing changes before commit,
  (3) user asks "is this code good", (4) security concerns mentioned,
  (5) user wants feedback on their implementation.
  Delegates to code-reviewer agent for thorough review.
---

# Code Quality Review

Automatically triggers when users need code quality feedback or are preparing to commit.

## Delegation

This skill delegates to the **code-reviewer** agent defined in `.claude/agents/code-reviewer.md`.

Use the code-reviewer subagent focusing on:
- Recent changes (git diff) if reviewing before commit
- Specific files if user mentions them
- Full review checklist from the agent

## When to Auto-Invoke (vs /code-review)

- **Use this skill**: Automatic quality hints during development
- **Use /code-review**: Explicit, thorough review before committing
