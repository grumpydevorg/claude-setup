---
name: hypothesis-testing
description: >
  Scientific method for debugging and problem-solving.
  Use when: (1) debugging unclear issues, (2) multiple possible causes,
  (3) need systematic approach to find root cause, (4) user says "I don't know why".
---

# Hypothesis Testing Methodology

Scientific method applied to software debugging and problem-solving.

## The Scientific Method for Code

```
Observe → Hypothesize → Predict → Test → Analyze → Iterate
```

## Phase 1: Observe

Gather all available information:

1. **Symptoms**
   - What is the exact error message?
   - When does it occur?
   - What is the expected vs actual behavior?

2. **Context**
   - What changed recently?
   - Does it happen consistently or intermittently?
   - What environment? (dev/staging/prod)

3. **Reproduction**
   - Can you reproduce it?
   - What are the exact steps?
   - Minimum reproduction case?

**Document observations:**
```markdown
## Observations
- Error: "Cannot read property 'id' of undefined"
- Occurs: When clicking submit on user form
- Frequency: Every time
- Environment: Production only
- Recent changes: Deployed auth update yesterday
```

## Phase 2: Hypothesize

Generate multiple hypotheses (at least 3):

```markdown
## Hypotheses

H1: User object not loaded before form submit
    Likelihood: High (matches error pattern)

H2: API returning different shape in production
    Likelihood: Medium (env-specific)

H3: Race condition in async data loading
    Likelihood: Medium (timing-related)

H4: Null user passed from parent component
    Likelihood: Low (would affect other features)
```

### Hypothesis Quality Checklist
- [ ] Explains the observed symptoms
- [ ] Is testable/falsifiable
- [ ] Based on evidence, not just guessing
- [ ] Considers recent changes

## Phase 3: Predict

For each hypothesis, predict what you should find if true:

```markdown
## Predictions

If H1 (user not loaded):
- P1.1: console.log(user) before submit shows undefined
- P1.2: Adding loading check prevents error
- P1.3: Network tab shows user fetch after submit

If H2 (API shape different):
- P2.1: API response in prod missing 'id' field
- P2.2: Staging API response has 'id' field
- P2.3: API schema changed recently

If H3 (race condition):
- P3.1: Adding delay before submit prevents error
- P3.2: Error timing correlates with network latency
```

## Phase 4: Test

Test predictions systematically:

### Testing Priority
1. **Quick tests first** - Log statements, network inspection
2. **Non-destructive** - Read-only operations
3. **Isolated** - Test one thing at a time
4. **Documented** - Record what you tried

### Test Log

```markdown
## Test Results

### Testing H1 (user not loaded)

Test: Add console.log(user) before submit
Result: user is defined, has id property
Conclusion: H1 REFUTED

### Testing H2 (API shape different)

Test: Compare API responses prod vs staging
Result: Both return same shape with id
Conclusion: H2 REFUTED

### Testing H3 (race condition)

Test: Add 500ms delay before accessing user
Result: Error still occurs
Conclusion: H3 REFUTED

### Back to observation...
New observation: Error only for NEW users, not existing
New hypothesis: H5 - New user creation doesn't return id
```

## Phase 5: Analyze

Evaluate results:

1. **Which hypotheses supported/refuted?**
2. **What new information emerged?**
3. **Do we need new hypotheses?**

```markdown
## Analysis

Refuted: H1, H2, H3, H4
New finding: Error correlates with new user creation
New hypothesis: H5 - Create user API not returning id

Testing H5:
- Check create user API response
- Result: Returns {success: true} without user object
- SUPPORTED: This is the root cause
```

## Phase 6: Conclude & Verify

1. **State the root cause**
2. **Verify with targeted fix**
3. **Confirm fix doesn't break other things**

```markdown
## Conclusion

Root cause: Create user API returns success flag but not user object.
Frontend assumes user.id exists after creation.

Fix: Modify API to return created user, or fetch user after create.

Verification:
- [ ] Fix implemented
- [ ] Original error no longer occurs
- [ ] Existing user flow still works
- [ ] Tests updated
```

## Output Format

```markdown
# Debugging Report: [Issue Summary]

## Observations
- [Symptom 1]
- [Symptom 2]
- [Context]

## Hypotheses Tested

| # | Hypothesis | Prediction | Test | Result |
|---|------------|------------|------|--------|
| H1 | ... | ... | ... | Refuted |
| H2 | ... | ... | ... | Refuted |
| H3 | ... | ... | ... | **Supported** |

## Root Cause
[Clear statement of the actual problem]

## Evidence
[What confirmed this was the cause]

## Solution
[How to fix it]

## Prevention
[How to prevent similar issues]
```

## Anti-Patterns to Avoid

1. **Shotgun debugging** - Random changes hoping something works
2. **Confirmation bias** - Only looking for evidence supporting first guess
3. **Skipping hypotheses** - Jumping to conclusions
4. **Not documenting** - Forgetting what you tried
5. **Single hypothesis** - Always generate multiple
