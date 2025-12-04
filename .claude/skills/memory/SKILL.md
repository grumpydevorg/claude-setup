---
name: memory
description: >
  Manages project memory using memory MCP tools.
  Use when: (1) user says "update memory" or "save this pattern",
  (2) after investigations/planning to persist learnings,
  (3) user asks "what do we know about X",
  (4) consolidating or pruning old knowledge.
---

# Memory Management

Manages persistent project knowledge using memory MCP tools.

## Memory MCP Tools

| Tool | Purpose |
|------|---------|
| `mcp__memory__create_entities` | Create new knowledge nodes |
| `mcp__memory__add_observations` | Add facts to existing nodes |
| `mcp__memory__search_nodes` | Find relevant knowledge |
| `mcp__memory__read_graph` | View all knowledge |
| `mcp__memory__create_relations` | Link related nodes |
| `mcp__memory__delete_entities` | Remove outdated nodes |
| `mcp__memory__delete_observations` | Remove specific facts |

## Entity Types

Create entities for different knowledge types:

```
project:<name>         - Project-level patterns
skill:<skill-name>     - Skill-specific learnings
domain:<area>          - Domain knowledge (auth, api, db)
pattern:<name>         - Reusable patterns discovered
risk:<name>            - Known risks and gotchas
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
```
mcp__memory__create_entities([
  {
    "name": "pattern:route-structure",
    "entityType": "pattern",
    "observations": [
      "Routes defined in src/routes/",
      "Each route file exports Express router",
      "Naming convention: <resource>.routes.ts"
    ]
  }
])
```

### Add to Existing Entity
```
mcp__memory__add_observations([
  {
    "entityName": "project:myapp",
    "contents": [
      "Uses PostgreSQL with Prisma ORM",
      "Migrations in prisma/migrations/"
    ]
  }
])
```

### Create Relations
```
mcp__memory__create_relations([
  {
    "from": "pattern:route-structure",
    "to": "domain:api",
    "relationType": "belongs_to"
  }
])
```

## Phase 3: Query Memory

Before investigation/planning, check existing knowledge:

```
mcp__memory__search_nodes("auth")
→ Returns all nodes related to authentication

mcp__memory__read_graph()
→ Returns full knowledge graph
```

## Phase 4: Consolidate

Periodically review and clean up:

1. **Merge similar nodes**
   - Find duplicates with `search_nodes`
   - Combine observations
   - Delete redundant nodes

2. **Prune stale knowledge**
   - Review nodes not accessed recently
   - Delete outdated information
   - Update changed patterns

3. **Strengthen connections**
   - Add missing relations
   - Remove broken links

## Commands

### "Update memory"
1. Review recent activity
2. Identify learnings worth saving
3. Create/update entities
4. Confirm with user

### "What do we know about X?"
1. `search_nodes(X)`
2. Format and present findings
3. Note gaps in knowledge

### "Consolidate memory"
1. `read_graph()` full state
2. Identify duplicates/stale nodes
3. Propose cleanup
4. Execute with user approval

### "Forget X"
1. `search_nodes(X)`
2. Confirm deletion
3. `delete_entities` or `delete_observations`

## Best Practices

- **Be specific** - "auth uses JWT" > "auth stuff"
- **Include evidence** - Reference files, commits
- **Link related** - Create relations between nodes
- **Prune regularly** - Remove outdated knowledge
- **Namespace entities** - Use type prefixes (pattern:, domain:, etc.)
