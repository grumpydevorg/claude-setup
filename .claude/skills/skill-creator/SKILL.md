---
name: skill-creator
description: >
  Creates new Claude Code skills following Anthropic best practices.
  Use when: (1) user wants to create a new skill, (2) user says "make a skill for X",
  (3) user wants to extend Claude's capabilities, (4) converting a workflow to a skill.
---

# Skill Creator

Creates well-structured skills following Anthropic's best practices.

## Architecture Principles (DRY)

This project uses a layered architecture:

```
agents/   → Core logic (single source of truth)
skills/   → Auto-triggered wrappers (thin, delegate to agents)
commands/ → Explicit orchestration (chain multiple agents)
```

**Before creating a skill, decide:**
- Does this need a new **agent** (reusable expertise)?
- Does this need a new **skill** (auto-trigger for existing agent)?
- Does this need a new **command** (explicit multi-step workflow)?

## Skill Creation Process

### Step 1: Gather Requirements
Ask the user:
- What capability should this provide?
- When should it auto-trigger?
- Does an existing agent handle this? (check `.claude/agents/`)

### Step 2: Create Skill Structure

```
.claude/skills/<skill-name>/
├── SKILL.md          # Required: frontmatter + instructions
├── references/       # Optional: documentation to load as-needed
└── scripts/          # Optional: helper scripts
```

### Step 3: Write SKILL.md

```yaml
---
name: lowercase-with-hyphens
description: >
  Brief description of what it does.
  Use when: (1) trigger condition, (2) trigger condition, (3) trigger condition.
  Delegates to X agent if applicable.
---

# Skill Title

Brief explanation of purpose.

## Delegation (if wrapping an agent)

This skill delegates to the **agent-name** agent in `.claude/agents/agent-name.md`.

## Instructions (if standalone)

1. Step one
2. Step two
3. Step three
```

## Best Practices

### Description Field (Critical)
- Include BOTH what it does AND when to use it
- All trigger conditions go here (body only loads after triggering)
- Max 1024 characters, be specific

### Body Guidelines
- Keep under 500 lines
- Use imperative form ("Run X", not "Running X")
- Reference agents instead of duplicating logic
- Include "when to use this vs command" guidance

### Progressive Disclosure
- Core workflow in SKILL.md
- Variant details in references/
- Keep references one level deep

### What NOT to Include
- README.md, CHANGELOG.md (not functional)
- Duplicated agent logic
- Verbose explanations (assume Claude is capable)

## Template

Create skill at `.claude/skills/<name>/SKILL.md`:

```yaml
---
name: <skill-name>
description: >
  <What it does>.
  Use when: (1) <condition>, (2) <condition>.
---

# <Skill Title>

<Brief purpose>

## Instructions

1. <Step>
2. <Step>
```
