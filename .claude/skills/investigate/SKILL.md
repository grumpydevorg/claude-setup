---
name: investigate
description: >
  Deep codebase investigation to find all files related to a problem, bug, or feature.
  Use when: (1) user describes a bug or issue, (2) user asks "where is X handled",
  (3) user wants to implement a feature touching unknown files, (4) understanding code relationships,
  (5) before making changes that might have wide impact.
---

# Code Investigation Methodology

Systematic process for discovering all code related to a problem.

## Phase 1: Problem Decomposition

Before searching, extract key elements:

1. **Identify keywords**
   - Component/feature names mentioned
   - Error messages or log strings
   - Function/class names if provided
   - Domain terms (auth, payment, cache, etc.)

2. **Determine problem type**
   - Bug fix → find error source + all code paths that trigger it
   - New feature → find integration points + similar implementations
   - Refactor → find all usages + dependencies
   - Performance → find hot paths + bottlenecks

3. **List questions to answer**
   - Where does this behavior originate?
   - What triggers this code path?
   - What depends on this?
   - Are there tests covering this?

## Phase 2: Entry Point Discovery

Search in order of specificity:

1. **Exact matches** (highest confidence)
   ```
   Grep for: error messages, function names, class names
   ```

2. **Partial matches** (medium confidence)
   ```
   Grep for: partial terms, camelCase variants, snake_case variants
   ```

3. **Semantic matches** (requires reading)
   ```
   Grep for: domain terms, related concepts
   ```

4. **Structural search**
   ```
   Glob for: **/[Aa]uth*, **/[Cc]ache*, test files, config files
   ```

## Phase 3: Dependency Mapping

From each entry point, trace:

1. **Imports/requires** - What does this file depend on?
2. **Exports/exposes** - What depends on this file?
3. **Configuration** - What config files affect this?
4. **Types/interfaces** - What contracts does this implement?

Build a dependency graph mentally:
```
entry_point.ts
├── imports: utils.ts, types.ts, api.ts
├── imported_by: handler.ts, controller.ts
└── config: settings.json, .env
```

## Phase 4: Contextual Expansion

Expand search to related areas:

1. **Test files** - Find `*.test.*`, `*.spec.*`, `__tests__/`
2. **Mocks/fixtures** - Find test data that reveals expected behavior
3. **Documentation** - Find inline docs, README sections
4. **Similar patterns** - Search for analogous implementations
5. **Error handling** - Find catch blocks, error boundaries
6. **Logging** - Find log statements that reveal flow

## Phase 5: Impact Analysis

Assess change impact:

1. **Direct dependents** - Files that import the target
2. **Indirect dependents** - Files that import the direct dependents
3. **Test coverage** - Which tests exercise this code?
4. **Build/deploy** - Does this affect build config, CI/CD?

## Output: Investigation Report

Structure findings as:

```markdown
# Investigation Report: [Problem Summary]

## Problem Statement
[Restate the problem in your own words]

## Key Files (Ranked by Relevance)

### Critical (Must Understand)
- `path/to/file.ts` - [Why critical: main logic for X]
- `path/to/other.ts` - [Why critical: handles Y]

### Important (Likely Affected)
- `path/to/related.ts` - [Why: shares dependency Z]

### Context (Helpful Background)
- `path/to/types.ts` - [Why: defines interfaces]
- `path/to/test.ts` - [Why: shows expected behavior]

## Code Flow
[How the code executes for this problem]
1. Entry: `handler.ts:45` receives request
2. Calls: `service.ts:120` processes data
3. Uses: `util.ts:30` for transformation
4. Returns: response via `handler.ts:60`

## Dependencies
[Key dependencies affecting this code]

## Potential Impact
[What else might be affected by changes]

## Recommendations
[Suggested approach based on findings]
```

## Guidelines

- **Be thorough** - Miss nothing that could cause bugs
- **Rank by relevance** - Not all files are equally important
- **Explain WHY** - Don't just list files, explain their role
- **Note uncertainty** - Flag areas that need more investigation
- **Consider tests** - Always find related test files
