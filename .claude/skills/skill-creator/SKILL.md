---
name: skill-creator
description: >
  Creates new Claude Code skills following Anthropic best practices.
  Use when: (1) user wants to create a new skill, (2) user says "make a skill for X",
  (3) user wants to extend Claude's capabilities, (4) converting a workflow to a skill.
---

# Skill Creator

Creates well-structured skills following Anthropic's best practices.

## Architecture: Skills as Single Source of Truth

```
skills/   → FULL methodology and expertise (single source of truth)
agents/   → THIN runtime config (tools, color) + pointer to skill
commands/ → Explicit orchestration (chains multiple agents)
```

### How It Works

1. **Skills** contain ALL the expertise - the actual methodology for HOW to do something
2. **Agents** are thin wrappers that specify tools/permissions and reference a skill
3. **Commands** orchestrate multiple agents in sequence

### Example

**Skill** (`.claude/skills/investigate/SKILL.md`) - 150 lines of methodology:
```yaml
---
name: investigate
description: Deep codebase investigation...
---
# Phase 1: Problem Decomposition
[Full methodology here...]
```

**Agent** (`.claude/agents/investigator.md`) - 10 lines:
```yaml
---
name: investigator
tools: Glob, Grep, Read, Bash
color: cyan
---
Follow the methodology in `.claude/skills/investigate/SKILL.md`.
```

## Decision Tree

When adding a new capability:

```
Need new capability?
│
├─ Is it a methodology/expertise?
│  └─ YES → Create a SKILL (with full methodology)
│           └─ Need it as subagent? → Also create thin AGENT
│
├─ Need restricted tool access or isolated execution?
│  └─ YES → Create AGENT referencing existing skill
│
└─ Need explicit multi-step workflow?
   └─ YES → Create COMMAND that orchestrates agents
```

## Skill Creation Process

### Step 1: Define the Methodology

Ask:
- What problem does this solve?
- What are the STEPS to solve it?
- What are the edge cases?
- What output format is expected?

### Step 2: Create Skill Structure

```
.claude/skills/<skill-name>/
├── SKILL.md              # Required: full methodology
└── references/           # Optional: extended docs, patterns
    └── patterns.md
```

### Step 3: Write SKILL.md

```yaml
---
name: lowercase-with-hyphens
description: >
  [What it does - one line].
  Use when: (1) trigger, (2) trigger, (3) trigger.
---

# [Skill Title] Methodology

[One line purpose]

## Phase 1: [First Phase Name]

[Detailed instructions for this phase]

1. **Step one**
   - Sub-detail
   - Sub-detail

2. **Step two**
   [...]

## Phase 2: [Second Phase Name]

[Continue with full methodology...]

## Output Format

[Template for expected output]

## Guidelines

- [Key principle 1]
- [Key principle 2]
```

### Step 4: Create Thin Agent (if needed)

Only if the skill needs to run as a subagent:

```yaml
---
name: skill-name-doer
description: [Brief description]
tools: [Minimal required tools]
color: [cyan/yellow/green/magenta]
---

Follow the methodology in `.claude/skills/<skill-name>/SKILL.md`.

[Any agent-specific output format requirements]
```

## Evolving vs Static Skills

Not all skills need memory. Choose based on the skill's nature:

### Static Skills (No Memory)
Universal methodologies that don't change per project:
- **skill-creator**: How to create skills is universal
- **review-quality**: Code review checklist is universal
- **decision-making**: Decision framework is universal
- **hypothesis-testing**: Scientific method is universal
- **verification**: Testing methodology is universal
- **task-decomposition**: Breaking down work is universal

Structure:
```
.claude/skills/static-skill/
└── SKILL.md              # Methodology only
```

### Evolving Skills (With Memory)
Project-specific skills that learn and adapt:
- **investigate**: Learns project structure, common patterns
- **trace-flow**: Learns architectural patterns, data flows
- **plan-implementation**: Learns estimation accuracy, risk patterns
- **memory-management**: Meta-skill for managing memory

Structure:
```
.claude/skills/evolving-skill/
├── SKILL.md              # Methodology + Pre-Phase: Load Context
└── CONTEXT.yaml          # Tiered memory storage
```

### CONTEXT.yaml Structure

```yaml
version: 1
meta:
  skill: investigate
  total_entries: 15
  prune_threshold: 50

core:           # Always loaded - highest value patterns
  - id: core-001
    type: pattern
    content: "Entry points are in src/routes/"
    confidence: 0.95
    evidence: ["investigation-auth", "investigation-api"]

domain:         # Loaded when context matches
  auth:
    - id: auth-001
      type: learning
      content: "Auth middleware in src/middleware/auth.ts"
      confidence: 0.9

archive:        # Searchable but not auto-loaded
  - id: arch-001
    type: gotcha
    content: "Legacy code in /old - do not use"
    archived_from: core
    reason: "Rarely relevant"

relations:      # Links between entries
  - from: core-001
    to: auth-001
    type: "contains"
```

### Memory Lifecycle

1. **Add**: New patterns discovered during skill execution
2. **Update**: Increase/decrease confidence based on validation
3. **Promote**: Low-tier entries that prove valuable → higher tier
4. **Demote**: Entries that prove less valuable → lower tier
5. **Prune**: Remove low-confidence, unused entries
6. **Consolidate**: Merge related entries, extract abstractions

## Best Practices

### Description Field (Critical for Discovery)
- Include BOTH what and when
- All trigger conditions here (body loads AFTER triggering)
- Max 1024 characters
- Be specific: "Use when user asks about code quality" not "Use for code"
- For evolving skills, include "EVOLVING skill" in description

### Methodology Content
- **Be comprehensive** - Include the full HOW
- **Use phases** - Break into logical steps
- **Include examples** - Show expected inputs/outputs
- **Define output format** - Template for results
- Under 500 lines (use references/ for extended content)

### What NOT to Include
- README.md, CHANGELOG.md (not functional)
- Vague instructions like "think carefully"
- Duplicate content (reference other skills if needed)

## Templates

### Standalone Skill (no agent needed)

```yaml
---
name: my-skill
description: >
  [Does X]. Use when: (1) condition, (2) condition.
---

# [Skill Name] Methodology

## Purpose
[What this accomplishes]

## Process

### Phase 1: [Name]
[Instructions...]

### Phase 2: [Name]
[Instructions...]

## Output Format
[Template...]

## Guidelines
- [Guideline 1]
- [Guideline 2]
```

### Skill + Agent Pair

**Skill:**
```yaml
---
name: my-skill
description: >
  [Does X]. Use when: (1) condition, (2) condition.
---

# [Full methodology - see above]
```

**Agent:**
```yaml
---
name: my-skill-agent
description: [Brief - runs my-skill as subagent]
tools: [Minimal tools]
color: cyan
---

Follow `.claude/skills/my-skill/SKILL.md`.
[Output format if different from skill default]
```
