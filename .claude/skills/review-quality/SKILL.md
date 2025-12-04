---
name: review-quality
description: >
  Comprehensive code review for quality, security, and maintainability.
  Use when: (1) reviewing changes before commit, (2) user asks "is this code good",
  (3) security concerns mentioned, (4) user wants feedback on implementation,
  (5) PR review requested, (6) checking for best practices.
---

# Code Review Methodology

Systematic process for reviewing code quality, security, and maintainability.

## Review Scope

First, determine what to review:

| Trigger | Scope |
|---------|-------|
| Before commit | `git diff` - staged/unstaged changes |
| PR review | All files in the PR |
| Specific file | Just that file |
| "Review my code" | Recent changes or specified area |

## Phase 1: Understand Context

Before critiquing, understand:

1. **What is this code trying to do?**
2. **What problem does it solve?**
3. **What constraints exist?** (performance, compatibility, etc.)

Read related code if needed to understand the context.

## Phase 2: Correctness Review

Does the code work correctly?

### Logic Errors
- [ ] Correct algorithm for the problem?
- [ ] Edge cases handled? (null, empty, boundary values)
- [ ] Off-by-one errors?
- [ ] Correct comparison operators? (`<` vs `<=`, `==` vs `===`)
- [ ] Proper boolean logic? (De Morgan's law violations)

### State Management
- [ ] Variables initialized before use?
- [ ] State mutations intentional and tracked?
- [ ] Race conditions possible?
- [ ] Memory leaks? (listeners not removed, refs held)

### Error Handling
- [ ] Errors caught appropriately?
- [ ] Error messages helpful?
- [ ] Cleanup happens on error? (finally, defer)
- [ ] Errors not silently swallowed?

### Async Code
- [ ] Promises awaited/handled?
- [ ] No floating promises?
- [ ] Concurrent operations safe?
- [ ] Timeouts where needed?

## Phase 3: Security Review

Is the code secure?

### Input Validation
- [ ] All external input validated?
- [ ] Type coercion issues?
- [ ] Length/size limits enforced?

### Injection Attacks
- [ ] SQL injection: parameterized queries used?
- [ ] XSS: output escaped/sanitized?
- [ ] Command injection: shell args escaped?
- [ ] Path traversal: paths validated?

### Authentication/Authorization
- [ ] Auth checks present where needed?
- [ ] Authorization not just authentication?
- [ ] Sensitive operations protected?

### Data Exposure
- [ ] No secrets in code? (API keys, passwords)
- [ ] Sensitive data not logged?
- [ ] PII handled properly?
- [ ] Error messages don't leak internals?

### Dependencies
- [ ] Dependencies from trusted sources?
- [ ] Known vulnerabilities?
- [ ] Minimal dependency surface?

## Phase 4: Maintainability Review

Is the code maintainable?

### Readability
- [ ] Clear naming? (variables, functions, classes)
- [ ] Single responsibility per function?
- [ ] Reasonable function length? (<30 lines ideal)
- [ ] Comments explain WHY, not WHAT?
- [ ] No magic numbers/strings?

### Structure
- [ ] Logical file organization?
- [ ] Appropriate abstraction level?
- [ ] No deep nesting? (>3 levels is a smell)
- [ ] DRY - no copy-paste code?

### Consistency
- [ ] Follows project conventions?
- [ ] Consistent with surrounding code?
- [ ] Consistent error handling pattern?

### Future-Proofing
- [ ] Easy to modify later?
- [ ] Not over-engineered?
- [ ] Clear extension points if needed?

## Phase 5: Performance Review

Is the code performant?

### Complexity
- [ ] Reasonable time complexity?
- [ ] No N+1 queries?
- [ ] No unnecessary loops/iterations?

### Resources
- [ ] Memory usage reasonable?
- [ ] Database connections managed?
- [ ] Files/streams closed?

### Caching
- [ ] Appropriate caching used?
- [ ] Cache invalidation handled?

### Optimization
- [ ] Not prematurely optimized?
- [ ] Hot paths identified and optimized?

## Phase 6: Testing Review

Is the code tested?

- [ ] Tests exist for new functionality?
- [ ] Tests cover edge cases?
- [ ] Tests are meaningful (not just coverage)?
- [ ] Tests are maintainable?
- [ ] No flaky tests introduced?

## Output Format

Structure feedback by priority:

```markdown
# Code Review: [Area/PR/Commit]

## Summary
[One paragraph overall assessment]

## Critical Issues (Must Fix)

### 1. [Issue Title]
**Location:** `file.ts:42`
**Problem:** [Clear description]
**Risk:** [What could go wrong]
**Fix:**
```typescript
// Before
problematicCode()

// After
fixedCode()
```

## Warnings (Should Fix)

### 1. [Issue Title]
**Location:** `file.ts:100`
**Problem:** [Description]
**Suggestion:** [How to improve]

## Suggestions (Consider)

### 1. [Issue Title]
**Location:** `file.ts:150`
**Idea:** [Optional improvement]

## Positive Notes
- [Something done well]
- [Good pattern used]

## Checklist Summary
| Category | Status |
|----------|--------|
| Correctness | Pass/Issues |
| Security | Pass/Issues |
| Maintainability | Pass/Issues |
| Performance | Pass/Issues |
| Testing | Pass/Issues |
```

## Review Guidelines

### Be Constructive
- Critique code, not the author
- Explain WHY something is an issue
- Provide concrete fixes, not vague complaints
- Acknowledge good work

### Prioritize
- Focus on correctness and security first
- Don't nitpick style if there are real bugs
- Distinguish "must fix" from "nice to have"

### Be Specific
- Point to exact lines
- Show code examples
- Reference documentation/standards

### Know When to Stop
- Don't demand perfection
- Consider time/effort tradeoffs
- Some issues can be separate PRs
