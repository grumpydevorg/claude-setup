---
name: investigate
description: >
  Deep codebase investigation using scientific method to find all files related to a problem.
  Use when: (1) user describes a bug or issue, (2) user asks "where is X handled",
  (3) implementing features touching unknown files, (4) understanding code relationships.
  EVOLVING skill - uses file-based memory for project-specific knowledge.
---

# Code Investigation Methodology

Systematic, scientific process for discovering code related to a problem.

## Pre-Phase: Load Context

Query memory for existing project knowledge:
```bash
memory query "<problem domain>"
```
Use accumulated patterns to guide investigation.

## Phase 1: Observe & Decompose

1. **State the problem clearly**
   - Observed behavior vs expected behavior
   - Error messages/symptoms

2. **Extract keywords**
   - Component/feature names
   - Error strings, function/class names
   - Domain terms (auth, payment, cache)

3. **Categorize problem type**
   | Type | Focus |
   |------|-------|
   | Bug fix | Error source + trigger paths |
   | New feature | Integration points + similar implementations |
   | Refactor | All usages + dependencies |

## Phase 2: Hypothesize

1. **Generate 2-3 hypotheses** about where the problem lives
   ```
   H1: Bug is in authentication middleware
   H2: Bug is in session storage logic
   H3: Bug is in request validation
   ```

2. **Rank by likelihood** (use memory patterns if available)

3. **Define predictions** for each
   ```
   If H1 correct: should find auth code in stack trace
   ```

## Phase 3: Search & Gather Evidence

1. **Test hypotheses** through targeted search
   - Grep for error messages, function names
   - Glob for file patterns

2. **Record evidence**
   | File | Supports | Contradicts | Notes |
   |------|----------|-------------|-------|

3. **Follow dependencies** from found files

## Phase 4: Analyze & Conclude

1. **Score hypotheses** (+2 strong for, -2 strong against)
2. **Identify most supported hypothesis**
3. **Note remaining uncertainty**

## Phase 5: Expand & Document

1. **Find related files** (tests, mocks, docs)
2. **Assess change impact** (dependents, coverage)

## Phase 6: Update Memory

If learnings discovered, suggest memory commands:

```markdown
## Memory Update Suggestions
- `memory create pattern <name> "<what was learned>"`
- `memory create domain <area> "<domain knowledge>"`
```

Example:
```bash
memory create pattern auth-middleware "Auth middleware in src/middleware/auth.ts"
memory create domain auth "Uses JWT in httpOnly cookies"
```

## Output: Investigation Report

```markdown
# Investigation Report: [Problem Summary]

## Problem Statement
[Observed vs expected]

## Hypotheses Tested
| Hypothesis | Prediction | Evidence | Result |
|------------|------------|----------|--------|
| H1: ... | Should find X | Found X | Supported |

## Conclusion
[Most supported hypothesis + confidence]

## Key Files (Ranked)
### Critical
- `path/to/file.ts:45` - [Why]
### Important
- `path/to/related.ts` - [Why]

## Impact Assessment
- Direct dependents: [list]
- Test coverage: [status]

## Learnings for Memory
- [Pattern to remember]
```

## Guidelines

- **Be scientific** - Test hypotheses, don't just search randomly
- **Record evidence** - Track what supports/contradicts each hypothesis
- **Use context** - Query memory for project patterns
- **Update memory** - Store learnings for future investigations
