---
name: plan-implementation
description: >
  Creates detailed implementation plans for features, fixes, and refactors.
  Use when: (1) user needs a plan before coding, (2) complex multi-file changes,
  (3) user asks "how should I implement X", (4) after investigation/flow analysis,
  (5) architectural decisions needed, (6) breaking down large tasks.
  EVOLVING skill - reads CONTEXT.yaml for project-specific patterns.
---

# Implementation Planning Methodology

Systematic process for creating actionable implementation plans.

## Pre-Phase: Load Context

Query memory MCP for project knowledge:
```
mcp__memory__search_nodes("<feature domain>")
```
Use accumulated knowledge:
- Past estimation accuracy → Calibrate new estimates
- Successful patterns → Reuse proven approaches
- Failed patterns → Avoid known pitfalls
- Risk history → Anticipate common risks

## Planning Principles

1. **Concrete over abstract** - Specific files and functions, not vague "update the code"
2. **Ordered by dependency** - Can't use what doesn't exist yet
3. **Testable increments** - Each step should be verifiable
4. **Risk-aware** - Identify what could go wrong
5. **Reversible when possible** - Prefer changes that can be undone

## Phase 1: Synthesize Context

If investigation/flow reports exist, extract:

1. **Key files** that need modification
2. **Dependencies** between files
3. **Existing patterns** to follow
4. **Constraints** discovered

If no prior analysis, quickly identify:
- Entry points for the change
- Files that will be affected
- Existing similar implementations

## Phase 2: Define Success Criteria

Before planning HOW, define WHAT success looks like:

```markdown
## Success Criteria
- [ ] [Specific behavior that should work]
- [ ] [Edge case that should be handled]
- [ ] [Performance requirement if any]
- [ ] [Tests that should pass]
```

## Phase 3: Identify Approach Options

List possible approaches:

| Approach | Pros | Cons | Risk |
|----------|------|------|------|
| Option A | ... | ... | Low/Med/High |
| Option B | ... | ... | Low/Med/High |

Select approach based on:
- Simplicity (prefer simpler)
- Consistency with existing code
- Risk level
- Reversibility

## Phase 4: Decompose & Break Down

### Decomposition Strategies

Choose based on the problem:

**Functional** - Break by what the system does:
```
User Auth → Login flow | Logout flow | Password reset | Session mgmt
```

**Layer** - Break by architectural layer:
```
Feature → Database | API | Business logic | Frontend | Tests
```

**Workflow** - Break by sequence:
```
Feature → 1. Design → 2. Storage → 3. API → 4. UI → 5. Test
```

**Risk** - Break by uncertainty:
```
Feature → Spike (HIGH) | Core (LOW) | Extension (MED) | Polish (LOW)
```

### Sizing Guide

| Size | Scope | Files | Action |
|------|-------|-------|--------|
| XS | Single function | 1 | Do it |
| S | Single feature | 1-2 | Do it |
| M | Cross-file feature | 2-4 | Do it |
| L | Many files | 4-8 | Careful |
| **XL** | **Too big** | **8+** | **Decompose further** |

**Rule: If size is XL, decompose further before proceeding.**

### Ordering Rules
1. **Types/interfaces first** - Define contracts before implementations
2. **Utilities before consumers** - Build blocks before using them
3. **Core logic before integration** - Get it working, then wire it up
4. **Tests alongside or after** - Verify each piece

### Dependency Mapping

Identify:
- **Critical path** - Longest dependency chain
- **Parallelizable** - Tasks with no dependencies between them
- **Bottlenecks** - Many tasks depend on one

### Step Granularity
Each step should:
- Be completable in one focused session
- Be independently testable
- Have clear success criteria
- Modify 1-3 files ideally

### Step Format
```markdown
### Step N: [Clear Action Title]

**Goal:** [What this step accomplishes]

**Files:**
- `path/to/file.ts` - [What changes: add function X, modify Y]
- `path/to/other.ts` - [What changes]

**Details:**
[Specific implementation guidance]
- Add function `processData(input: Input): Output`
- Handle edge case: empty input returns empty array
- Follow existing pattern in `similar.ts:50`

**Verification:**
- [ ] [How to verify this step worked]
```

## Phase 5: Identify Risks and Mitigations

For each significant risk:

```markdown
## Risks

### Risk: [Description]
**Likelihood:** Low/Medium/High
**Impact:** Low/Medium/High
**Mitigation:** [How to prevent or handle]
**Rollback:** [How to undo if needed]
```

Common risks to consider:
- Breaking existing functionality
- Performance regression
- Data migration issues
- API compatibility
- Security implications

## Phase 6: Define Rollback Strategy

How to undo if things go wrong:

- **Code changes**: Git revert strategy
- **Database changes**: Migration rollback
- **Config changes**: Previous values documented
- **External integrations**: Feature flags

## Output: Implementation Plan

Structure the plan as:

```markdown
# Implementation Plan: [Feature/Fix Name]

## Overview
[One paragraph describing what we're building and why]

## Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Approach
[Chosen approach and brief rationale]

## Implementation Steps

### Step 1: [Title]
**Goal:** [What this accomplishes]
**Files:**
- `path/to/file.ts` - [Changes]

**Details:**
[Implementation specifics]

**Verification:**
- [ ] [How to verify]

---

### Step 2: [Title]
**Goal:** [What this accomplishes]
**Files:**
- `path/to/file.ts` - [Changes]

**Details:**
[Implementation specifics]

**Verification:**
- [ ] [How to verify]

---

[Continue for all steps...]

## Testing Strategy
- Unit tests: [What to test]
- Integration tests: [What to test]
- Manual verification: [What to check]

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Med | High | [Mitigation] |

## Rollback Plan
[How to undo if needed]

## Open Questions
- [ ] [Any unresolved decisions]
```

## Planning Guidelines

### Keep It Actionable
- Every step should be doable
- No vague "improve the code" steps
- Specific files, specific changes

### Right Level of Detail
- More detail for complex/risky parts
- Less detail for straightforward parts
- Include code snippets for tricky logic

### Consider the Reader
- Plan should be followable by someone else
- Explain non-obvious decisions
- Link to relevant documentation

### Stay Flexible
- Mark areas of uncertainty
- Note where approach might need adjustment
- Include decision points

### Don't Over-Plan
- Some details emerge during implementation
- Plan enough to start confidently
- Allow for iteration

## Phase 7: Update Memory

After plan execution (success or failure), save to memory MCP:

```
mcp__memory__create_entities([{
  "name": "pattern:<what-was-learned>",
  "entityType": "pattern",
  "observations": [
    "Approach: <what worked or failed>",
    "Evidence: <commit or file reference>",
    "Estimation: <actual vs planned>"
  ]
}])
```

For risks discovered:
```
mcp__memory__add_observations([{
  "entityName": "risk:<area>",
  "contents": ["<risk description and mitigation>"]
}])
```

## Guidelines
