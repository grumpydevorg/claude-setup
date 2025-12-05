---
name: task-routing
description: >
  Automatically assess task complexity and route to appropriate workflow.
  Use when: (1) user invokes /task command, (2) need to decide between direct solve vs multi-agent investigation.
---

# Task Routing & Complexity Assessment

Systematically assess task complexity and route to the appropriate workflow.

## Purpose

Determine whether a task requires:
- **Simple approach:** Direct problem-solving (fast, conversational)
- **Complex approach:** Multi-agent investigation (thorough, systematic)

## Phase 1: Extract Task Characteristics

Analyze the user's request for these indicators:

### 1.1 Location Knowledge
| Indicator | Complexity Signal |
|-----------|-------------------|
| Specific file/function named | ✅ Simple |
| "in src/auth.ts" | ✅ Simple |
| "find where...", "locate...", "where is..." | ⚠️ Complex |
| "not sure where...", "might be in..." | ⚠️ Complex |

### 1.2 Scope Indicators
| Indicator | Complexity Signal |
|-----------|-------------------|
| Single file/component | ✅ Simple |
| 1-3 specific files mentioned | ✅ Simple |
| "all files", "everywhere", "across the codebase" | ⚠️ Complex |
| "entire system", "architecture", "refactor all" | ⚠️ Complex |
| Multiple systems/services | ⚠️ Complex |

### 1.3 Task Type
| Task Type | Typical Complexity |
|-----------|-------------------|
| "add function", "update logic" | ✅ Simple |
| "fix bug" (with location) | ✅ Simple |
| "fix bug" (no location) | ⚠️ Complex |
| "refactor", "redesign", "restructure" | ⚠️ Complex |
| "implement feature" (new, unknown integration points) | ⚠️ Complex |
| "investigate", "understand", "analyze" | ⚠️ Complex |

### 1.4 Certainty Level
| User Language | Signal |
|---------------|--------|
| Confident, specific | ✅ Simple |
| "should be in...", "probably..." | ⚠️ Medium |
| "no idea where", "complex problem", "not sure" | ⚠️ Complex |

## Phase 2: Score Complexity

Assign points based on indicators:

**Simple Signals (subtract points):**
- Specific file/function named: -3
- Single component: -2
- Clear location: -2
- Small scope (1-3 files): -2

**Complex Signals (add points):**
- Unknown location: +3
- "find/where/locate" keywords: +3
- Broad scope: +3
- Multiple systems: +2
- Architectural terms: +2
- User uncertainty: +2

**Complexity Score:**
- Score ≤ 0: Simple
- Score 1-4: Medium
- Score ≥ 5: Complex

## Phase 3: Route Decision

Based on score, choose workflow:

### Simple (Score ≤ 0)
**Direct Problem Solving:**
- Think through the problem step-by-step
- Use standard tools (Read, Edit, Bash)
- Fast, conversational approach
- No subagents needed

### Medium (Score 1-4)
**Light Investigation:**
- Quick exploration (Glob/Grep to find files)
- Read relevant code
- Solve directly
- Consider: Could escalate to complex if needed

### Complex (Score ≥ 5)
**Multi-Agent Investigation:**
1. Launch **investigator** subagent → INVESTIGATION_REPORT.md
2. Launch **code-flow-mapper** subagent → FLOW_REPORT.md
3. Launch **planner** subagent → PLAN.md
4. Enter plan mode → present plan for approval

## Phase 4: Execute & Learn

After task completion, optionally store learning:

```bash
# If routing was successful
memory create pattern task-routing "Request '{summary}' was {simple|complex}, used {approach}"

# If routing was wrong (user feedback)
memory create pattern task-routing-adjustment "Initially routed as {X}, should be {Y}: {reason}"
```

## Examples

### Example 1: Simple
```
User: "Add logging to the login function in src/auth/login.ts"

Analysis:
- Specific file: -3
- Specific function: -3
- Single component: -2
- Clear location: -2
Score: -10 → Simple

Route: Direct solve
```

### Example 2: Complex
```
User: "Find and fix the memory leak in the application"

Analysis:
- Unknown location: +3
- "Find" keyword: +3
- No specific file: 0
- User uncertainty implied: +2
Score: +8 → Complex

Route: Multi-agent (investigator → flow-mapper → planner)
```

### Example 3: Medium
```
User: "Refactor the authentication logic to use the new JWT library"

Analysis:
- "Refactor" keyword: +2
- Known domain (auth): -1
- Scope unclear: +1
Score: +2 → Medium

Route: Light investigation, may escalate if needed
```

## Output Format

Always state your routing decision:

```markdown
**Task Complexity Assessment:**
- Location knowledge: [specific/vague/unknown]
- Scope: [single-file/multi-file/system-wide]
- Complexity score: X
- **Routing decision: [Simple/Medium/Complex]**

[Proceed with chosen approach]
```

## Guidelines

- **Be decisive** - Don't overthink, use the heuristics
- **Trust the score** - The methodology is designed to be reliable
- **Medium is flexible** - Start simple, escalate if needed
- **Learn from feedback** - If user says "that was too simple/complex", store in memory
- **When in doubt** - Ask the user: "Is this a simple fix or does it need investigation?"
