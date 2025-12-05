---
name: memory
description: >
  Manages project memory using file-based CLI tool.
  Use when: (1) user says "update memory" or "save this pattern",
  (2) after investigations/planning to persist learnings,
  (3) user asks "what do we know about X",
  (4) consolidating or pruning old knowledge.
---

# Memory Management

Manages persistent project knowledge using JSONL file-based system with CLI tool.

## Installation

The memory CLI must be installed globally. Before first use, check if installed:

```bash
which memory || {
  echo "Installing memory CLI..."
  cp .claude/bin/memory ~/.local/bin/memory
  chmod +x ~/.local/bin/memory
  echo "✓ Installed to ~/.local/bin/memory"
}
```

If `which memory` fails during skill execution, run the installation command above.

## Memory CLI Commands

| Command | Purpose |
|---------|---------|
| `memory create TYPE NAME "observation"` | Create new entity with first observation |
| `memory add TYPE NAME "observation"` | Add observation to existing entity |
| `memory query TERM` | Search all entities for term |
| `memory show TYPE NAME` | Display full entity details |
| `memory list [TYPE]` | List all entities, optionally filtered by type |

## Entity Types

Create entities for different knowledge types:

```
project     - Project-level patterns and architecture
domain      - Domain knowledge (auth, api, db)
pattern     - Reusable patterns discovered
flow        - Known execution flows and data paths
risk        - Known risks and gotchas
```

## Phase 1: Capture Learning

After investigation/planning, identify what to save:

1. **Patterns** - Recurring structures
   ```
   "Routes are in src/routes/, handlers in src/handlers/"
   ```

2. **Learnings** - Discoveries about how things work
   ```
   "Auth uses JWT stored in httpOnly cookies"
   ```

3. **Gotchas** - Non-obvious behaviors
   ```
   "Cache invalidation requires manual clear after deploy"
   ```

4. **Decisions** - Technical choices made
   ```
   "Chose Prisma over TypeORM for type safety"
   ```

## Phase 2: Store in Memory

### Create Entity
```bash
memory create pattern route-structure "Routes defined in src/routes/"
memory add pattern route-structure "Each route file exports Express router"
memory add pattern route-structure "Naming convention: <resource>.routes.ts"
```

With evidence and confidence:
```bash
memory create pattern type-first "Always create types before implementations" \
  --evidence "src/types/" --confidence 0.9
```

### Add to Existing Entity
```bash
memory add project myapp "Uses PostgreSQL with Prisma ORM"
memory add project myapp "Migrations in prisma/migrations/" \
  --evidence "prisma/migrations/"
```

## Phase 3: Query Memory

Before investigation/planning, check existing knowledge:

```bash
memory query "auth"
# Returns all entities related to authentication

memory list pattern
# Shows all pattern entities

memory show pattern route-structure
# Displays full entity with all observations
```

## Phase 4: Review and Organize

Periodically review and maintain:

1. **Review by type**
   ```bash
   memory list pattern    # Review all patterns
   memory list risk       # Review all risks
   memory list flow       # Review all flows
   ```

2. **Check specific areas**
   ```bash
   memory query "database"
   memory query "authentication"
   ```

3. **View details**
   ```bash
   memory show domain auth
   # Shows full history of auth domain knowledge
   ```

## Commands

### "Update memory"
1. Review recent activity
2. Identify learnings worth saving
3. Suggest memory commands to user
4. User executes commands

### "What do we know about X?"
1. Run `memory query "X"`
2. Format and present findings
3. Note gaps in knowledge

### "Show me our patterns"
1. Run `memory list pattern`
2. For each interesting pattern: `memory show pattern <name>`
3. Summarize findings

## Best Practices

- **Be specific** - "auth uses JWT" > "auth stuff"
- **Include evidence** - Use `--evidence` to reference files, commits
- **Use confidence** - `--confidence 0.9` for well-proven patterns
- **Organize by type** - Use correct entity type (pattern, domain, flow, risk)
- **Accumulate observations** - Use `memory add` to build up knowledge over time

## File Structure

Memory is stored in `.claude/memory/` as JSONL files:

```
.claude/memory/
├── project/claude-setup.jsonl
├── pattern/route-structure.jsonl
├── domain/auth.jsonl
├── flow/login-flow.jsonl
└── risk/cache-invalidation.jsonl
```

Each file contains:
- Line 1: Entity metadata (id, type, created, confidence, use_count)
- Lines 2+: Observations (content, added, evidence)
