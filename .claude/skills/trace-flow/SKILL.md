---
name: trace-flow
description: >
  Traces code execution paths, data flow, and file interconnections with verification.
  Use when: (1) user asks "how does X work", (2) understanding call chains,
  (3) tracing request/response flow, (4) debugging execution order.
  EVOLVING skill - uses memory MCP for known flows and patterns.
---

# Code Flow Tracing Methodology

Systematic process for understanding code execution and data flow.

## Pre-Phase: Load Context

Query memory MCP for known flows and architecture:
```
mcp__memory__search_nodes("<component or flow name>")
```
Use existing knowledge to accelerate tracing.

## Phase 1: Identify Flow Type & Entry Points

| Type | Question | Focus |
|------|----------|-------|
| Execution | "What happens when X?" | Function calls |
| Data | "How does data get from A to B?" | Transformations |
| Control | "What decides X?" | Conditionals |
| Event | "What triggers X?" | Listeners |
| Error | "What happens when X fails?" | Catch blocks |

Find entry points:
- HTTP/API: routes, controllers, middleware
- Events: listeners, handlers
- User: click handlers, lifecycle hooks
- Background: cron, queues, workers

## Phase 2: Trace Forward (Downstream)

From entry point, follow:
1. Direct calls: `A() → B() → C()`
2. Async boundaries: promises, callbacks
3. External calls: DB, API, filesystem
4. State mutations: store updates, cache writes

Document as tree:
```
1. [entry.ts:10] handleRequest(req)
   └─ 2. [validator.ts:25] validate(req.body)
      └─ 3. [service.ts:50] processData(validated)
```

## Phase 3: Trace Backward (Upstream)

From point of interest:
1. Find all callers: `grep "functionName("`
2. Find all triggers: events, conditions
3. Find data sources: parameters, state

## Phase 4: Map Data Transformations

Track shape changes:
```
Input: { user_id: 123 }
  → [validator] { userId: 123 }      // camelCase
  → [enricher]  { userId: 123, user: {...} }  // added
  → Output: { success: true }
```

## Phase 5: Identify Branching & Side Effects

**Branching:** conditionals, error boundaries, feature flags
**Side effects:** DB writes, API calls, emails, logs

## Phase 6: Verify Flow

**Critical step - confirm understanding:**

1. **Trace a concrete example**
   - Pick specific input
   - Follow through manually
   - Confirm output matches expectation

2. **Check edge cases**
   - What if input is null/empty?
   - What if external call fails?

3. **Validate with tests**
   - Do existing tests confirm this flow?
   - Any gaps in test coverage?

## Phase 7: Update Memory

If new flows/patterns discovered, save to memory MCP:
```
mcp__memory__create_entities([{
  "name": "flow:<flow-name>",
  "entityType": "flow",
  "observations": [
    "Entry: <entry point>",
    "Path: A → B → C",
    "<key insight>"
  ]
}])
```

## Output: Flow Report

```markdown
# Flow Report: [Flow Name]

## Overview
[One paragraph description]

## Entry Points
| Entry | File | Trigger |
|-------|------|---------|
| handleX | api/x.ts:20 | POST /api/x |

## Execution Flow

### Happy Path
```
1. [file.ts:20] function(req)
   ├─ 2. [service.ts:50] process(data)
   └─ 3. [db.ts:100] save(result)
```

### Error Paths
- Payment fails → Returns 402

## Verification
- [x] Traced with example input: {...}
- [x] Confirmed output: {...}
- [ ] Edge case: empty input (needs test)

## Side Effects
| Effect | Location | Description |
|--------|----------|-------------|
| DB Write | step 3 | Saves record |

## Learnings for Memory
- [Pattern discovered]
```
