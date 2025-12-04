---
name: task-decomposition
description: >
  Systematically breaks down complex tasks into manageable subtasks with dependencies.
  Use when: (1) task has multiple parts, (2) unclear where to start, (3) need to parallelize work,
  (4) estimating effort, (5) user says "help me plan" or "break this down".
---

# Task Decomposition Methodology

Systematic process for breaking complex tasks into actionable subtasks.

## When to Decompose

| Complexity Signal | Action |
|-------------------|--------|
| Multiple files affected | Decompose |
| Multiple features/concerns | Decompose |
| Unclear starting point | Decompose |
| Estimated > 1 hour | Decompose |
| Dependencies between parts | Decompose |
| Single, clear action | Skip decomposition |

## Phase 1: Understand the Goal

1. **State the end goal**
   - What does "done" look like?
   - What should work when complete?

2. **Identify constraints**
   - Time constraints?
   - Dependencies on external factors?
   - Technical limitations?

3. **Define scope boundaries**
   - What's IN scope?
   - What's explicitly OUT of scope?

## Phase 2: Identify Components

Break down by one of these strategies:

### Strategy A: Functional Decomposition
Break by what the system does:
```
Feature: User Authentication
├── Login flow
├── Logout flow
├── Password reset
└── Session management
```

### Strategy B: Layer Decomposition
Break by architectural layer:
```
Feature: User Authentication
├── Database schema
├── API endpoints
├── Business logic
├── Frontend UI
└── Tests
```

### Strategy C: Workflow Decomposition
Break by sequence of operations:
```
Feature: User Authentication
├── 1. Design data model
├── 2. Implement storage
├── 3. Create API
├── 4. Build UI
└── 5. Integration testing
```

### Strategy D: Risk Decomposition
Break by uncertainty/risk:
```
Feature: User Authentication
├── Spike: Evaluate auth libraries (HIGH RISK)
├── Core: Basic login (LOW RISK)
├── Extension: OAuth (MEDIUM RISK)
└── Polish: Remember me (LOW RISK)
```

## Phase 3: Define Subtasks

For each component, create a subtask:

```yaml
subtask:
  id: T1
  title: "Implement user login API endpoint"
  description: "Create POST /api/auth/login that validates credentials and returns JWT"

  # Sizing
  size: S  # XS, S, M, L, XL
  confidence: high  # low, medium, high

  # Dependencies
  depends_on: []  # or [T0] if blocked
  blocks: [T2, T3]  # what this unblocks

  # Verification
  done_when:
    - "Endpoint accepts email/password"
    - "Returns JWT on success"
    - "Returns 401 on failure"
    - "Unit tests pass"
```

### Sizing Guide

| Size | Typical Scope | Files | Complexity |
|------|---------------|-------|------------|
| XS | Single function change | 1 | Trivial |
| S | Single feature, one file | 1-2 | Low |
| M | Feature across few files | 2-4 | Medium |
| L | Feature across many files | 4-8 | High |
| XL | **Needs further decomposition** | 8+ | Very high |

**Rule: If size is XL, decompose further.**

## Phase 4: Map Dependencies

Create dependency graph:

```
T0: Setup database schema
 │
 ├──→ T1: User model
 │     │
 │     ├──→ T3: Login API
 │     │     │
 │     │     └──→ T5: Login UI
 │     │
 │     └──→ T4: Register API
 │           │
 │           └──→ T6: Register UI
 │
 └──→ T2: Session storage
       │
       └──→ T3: Login API (also depends on T1)
```

Identify:
- **Critical path** - Longest chain of dependencies
- **Parallelizable tasks** - No dependencies between them
- **Bottlenecks** - Many tasks depend on one

## Phase 5: Order & Prioritize

1. **Topological sort** by dependencies
2. **Prioritize** within each level:
   - Risk reduction first (spikes, unknowns)
   - Critical path items
   - Quick wins for momentum

## Phase 6: Create Execution Plan

Output as TodoWrite-compatible list:

```markdown
## Task: [Main Goal]

### Phase 1: Foundation
- [ ] T0: Setup database schema (XS)
- [ ] T1: User model (S) [depends: T0]
- [ ] T2: Session storage (S) [depends: T0]

### Phase 2: Core API [parallel possible]
- [ ] T3: Login API (M) [depends: T1, T2]
- [ ] T4: Register API (M) [depends: T1]

### Phase 3: Frontend [parallel possible]
- [ ] T5: Login UI (M) [depends: T3]
- [ ] T6: Register UI (M) [depends: T4]

### Phase 4: Integration
- [ ] T7: E2E tests (M) [depends: T5, T6]

### Critical Path: T0 → T1 → T3 → T5 → T7
### Parallelizable: T3/T4, T5/T6
```

## Output Format

```markdown
# Task Decomposition: [Goal]

## Goal
[Clear end state]

## Scope
- IN: [what's included]
- OUT: [what's excluded]

## Subtasks

| ID | Task | Size | Depends On | Blocks | Done When |
|----|------|------|------------|--------|-----------|
| T0 | ... | S | - | T1, T2 | [criteria] |
| T1 | ... | M | T0 | T3 | [criteria] |

## Dependency Graph
[ASCII or description]

## Execution Order
1. [First tasks - can parallelize]
2. [Second wave]
3. [Final tasks]

## Critical Path
[Longest dependency chain]

## Risks
- [Risk 1]: [Mitigation]
```

## Integration with TodoWrite

After decomposition, create todos:

```
TodoWrite([
  {content: "T0: Setup database schema", status: "pending"},
  {content: "T1: User model [blocked by T0]", status: "pending"},
  ...
])
```

Update as work progresses:
- Mark completed
- Add discovered subtasks
- Adjust dependencies

## Guidelines

- **XL = Decompose further** - Never leave XL tasks
- **Include verification** - Every task needs "done when"
- **Track dependencies** - Prevents blocked work
- **Allow parallel work** - Identify what can run simultaneously
- **Stay flexible** - Plan will evolve during execution
