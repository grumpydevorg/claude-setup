---
name: decision-making
description: >
  Framework for making and documenting technical decisions.
  Use when: (1) multiple valid approaches exist, (2) user asks "should I use X or Y",
  (3) architectural choices needed, (4) trade-offs to evaluate.
---

# Technical Decision-Making Methodology

Systematic framework for evaluating options and making documented decisions.

## When to Use This Framework

| Situation | Use Framework? |
|-----------|---------------|
| Multiple valid approaches | Yes |
| Significant trade-offs | Yes |
| Reversibility unclear | Yes |
| Team needs alignment | Yes |
| Trivial choice | No |
| Clear best practice exists | No |

## Phase 1: Frame the Decision

1. **State the decision clearly**
   ```
   Decision: Which database to use for user sessions
   ```

2. **Define the context**
   - Why is this decision needed now?
   - What constraints exist?
   - Who are the stakeholders?

3. **Identify decision type**
   | Type | Reversibility | Time Investment |
   |------|--------------|-----------------|
   | One-way door | Hard to reverse | More analysis |
   | Two-way door | Easy to reverse | Decide faster |

## Phase 2: Generate Options

List all viable options (at least 2-3):

```markdown
## Options

### Option A: Redis
[Brief description]

### Option B: PostgreSQL sessions
[Brief description]

### Option C: JWT (stateless)
[Brief description]

### Option D: Do nothing (baseline)
[Current state for comparison]
```

**Include "do nothing"** as baseline for comparison.

## Phase 3: Define Criteria

What factors matter for this decision?

```markdown
## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Performance | High | Session lookup speed |
| Scalability | High | Multi-instance support |
| Complexity | Medium | Implementation effort |
| Cost | Medium | Infrastructure cost |
| Team familiarity | Low | Learning curve |
```

### Common Criteria Categories
- **Technical**: Performance, scalability, security, maintainability
- **Organizational**: Cost, timeline, team skills, vendor lock-in
- **Strategic**: Future flexibility, alignment with direction

## Phase 4: Evaluate Options

Score each option against criteria:

```markdown
## Evaluation Matrix

| Criterion | Weight | Redis | PostgreSQL | JWT |
|-----------|--------|-------|------------|-----|
| Performance | High | ★★★ | ★★☆ | ★★★ |
| Scalability | High | ★★★ | ★★☆ | ★★★ |
| Complexity | Medium | ★★☆ | ★★★ | ★☆☆ |
| Cost | Medium | ★★☆ | ★★★ | ★★★ |
| Team familiarity | Low | ★★☆ | ★★★ | ★★☆ |

Weighted Score:
- Redis: 2.6
- PostgreSQL: 2.5
- JWT: 2.3
```

## Phase 5: Consider Trade-offs

For top options, deep-dive trade-offs:

```markdown
## Trade-off Analysis

### Redis
Pros:
- Fast lookup (sub-ms)
- Built for this use case
- Easy scaling

Cons:
- Additional infrastructure
- Data loss on restart (without persistence)
- Another system to maintain

### PostgreSQL
Pros:
- No new infrastructure
- ACID guarantees
- Existing backups cover it

Cons:
- Slower than Redis
- More DB load
- May need session table maintenance
```

## Phase 6: Decide

Make the decision explicitly:

```markdown
## Decision

**Chosen option: Redis**

### Rationale
1. Performance is critical for session lookups on every request
2. We're already planning to add Redis for caching
3. Two-way door: Can migrate to PostgreSQL if needed

### Rejected alternatives
- PostgreSQL: Performance concern under high load
- JWT: Complexity of token invalidation
```

## Phase 7: Document

Create decision record (ADR format):

```markdown
# ADR-001: Session Storage

## Status
Accepted

## Context
[Why this decision was needed]

## Decision
[What we decided]

## Consequences

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Cost 1]
- [Risk 1]

### Neutral
- [Side effect]

## Alternatives Considered
- [Option B]: [Why rejected]
- [Option C]: [Why rejected]
```

## Output: Decision Record

```markdown
# Decision: [Title]

## Context
[Why this decision is needed]

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| A | ... | ... |
| B | ... | ... |

## Evaluation

| Criterion | Wt | A | B |
|-----------|----|----|---|
| ... | H | ★★★ | ★★☆ |

## Decision
**Chosen: [Option]**

## Rationale
[Why this option]

## Consequences
- [Impact 1]
- [Impact 2]

## Review Date
[When to revisit this decision]
```

## Decision Quality Checklist

Before finalizing:
- [ ] Multiple options considered
- [ ] Criteria defined and weighted
- [ ] Trade-offs explicitly stated
- [ ] Rationale documented
- [ ] Consequences acknowledged
- [ ] Reversibility assessed
- [ ] Stakeholders consulted (if applicable)
