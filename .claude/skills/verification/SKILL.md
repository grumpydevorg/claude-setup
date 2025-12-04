---
name: verification
description: >
  Confirms that changes work correctly and haven't broken anything.
  Use when: (1) after implementing changes, (2) before committing,
  (3) user asks "does this work", (4) validating a fix.
---

# Verification Methodology

Systematic process for confirming changes work correctly.

## Verification Levels

| Level | Scope | When |
|-------|-------|------|
| **Unit** | Single function/component | After each change |
| **Integration** | Multiple components together | After feature complete |
| **System** | Full application | Before release |
| **Regression** | Existing functionality | Always |

## Phase 1: Define What to Verify

Before testing, be explicit:

```markdown
## Verification Checklist

### Must Work (Critical)
- [ ] [Primary functionality]
- [ ] [Core use case]

### Should Work (Important)
- [ ] [Secondary functionality]
- [ ] [Edge cases]

### Must Not Break (Regression)
- [ ] [Related feature 1]
- [ ] [Related feature 2]
```

## Phase 2: Verify the Change

### 2.1 Syntax & Compilation
```
- [ ] Code compiles without errors
- [ ] No new type errors
- [ ] Linter passes
```

### 2.2 Unit Verification
```
- [ ] New/modified tests pass
- [ ] Test covers happy path
- [ ] Test covers error cases
- [ ] Test covers edge cases
```

### 2.3 Manual Verification
```
- [ ] Manually tested primary use case
- [ ] Manually tested edge cases
- [ ] Behavior matches expectation
```

## Phase 3: Verify No Regression

### 3.1 Run Existing Tests
```
- [ ] All existing tests pass
- [ ] No new test failures
- [ ] Test coverage not decreased
```

### 3.2 Check Related Features
```
- [ ] Feature A still works (shares code with change)
- [ ] Feature B still works (uses same data)
```

### 3.3 Smoke Test Critical Paths
```
- [ ] User can log in
- [ ] User can perform core action
- [ ] No console errors
```

## Phase 4: Verify Edge Cases

| Edge Case | Test | Result |
|-----------|------|--------|
| Empty input | [How tested] | Pass/Fail |
| Null/undefined | [How tested] | Pass/Fail |
| Very large input | [How tested] | Pass/Fail |
| Concurrent access | [How tested] | Pass/Fail |
| Network failure | [How tested] | Pass/Fail |

## Phase 5: Document Results

```markdown
## Verification Results

### Environment
- Node: v18.0.0
- OS: macOS 14.0
- Branch: feature/xyz

### Test Results
- Unit tests: 45/45 passing
- Integration tests: 12/12 passing
- Manual tests: 5/5 passing

### Coverage
- Lines: 85% (no decrease)
- Branches: 78% (+2%)

### Edge Cases Tested
| Case | Result |
|------|--------|
| Empty input | ✓ Pass |
| Invalid input | ✓ Pass |

### Regression Check
- [x] Related feature A works
- [x] Related feature B works
- [x] Core user flow works
```

## Phase 6: Define Rollback Criteria

When should we rollback?

```markdown
## Rollback Triggers

Immediate rollback if:
- [ ] Error rate increases > 5%
- [ ] Core functionality broken
- [ ] Data corruption detected

Consider rollback if:
- [ ] Performance degradation > 20%
- [ ] High volume of user complaints
- [ ] Unexpected side effects
```

## Rollback Procedure

```markdown
## Rollback Steps

1. Identify: [How to detect problem]
2. Decide: [Who decides to rollback]
3. Execute:
   - `git revert <commit>`
   - OR `git checkout <previous>`
   - Deploy previous version
4. Verify: Confirm rollback successful
5. Communicate: Notify stakeholders
6. Investigate: Root cause analysis
```

## Output: Verification Report

```markdown
# Verification Report: [Change Description]

## Change Summary
[What was changed]

## Verification Status: ✓ PASSED / ✗ FAILED

## Tests Run
| Type | Passed | Failed | Skipped |
|------|--------|--------|---------|
| Unit | 45 | 0 | 0 |
| Integration | 12 | 0 | 2 |
| Manual | 5 | 0 | 0 |

## Coverage
- Before: 83%
- After: 85%

## Edge Cases
| Case | Status |
|------|--------|
| Empty input | ✓ |
| Null values | ✓ |

## Regression
- [x] Feature A works
- [x] Feature B works
- [x] Core flow works

## Rollback Ready
- [x] Rollback procedure documented
- [x] Previous version identified
- [x] Rollback triggers defined

## Sign-off
- Verified by: [name/agent]
- Date: [date]
- Confidence: High/Medium/Low
```

## Quick Verification Checklist

For fast verification:

```
□ Compiles
□ Tests pass
□ Manual check works
□ Related features work
□ Know how to rollback
```
