---
name: memory-management
description: >
  Manages CONTEXT.yaml lifecycle for evolving skills.
  Use when: (1) updating skill memory, (2) consolidating learnings,
  (3) pruning stale entries, (4) reviewing skill knowledge.
---

# Memory Management Methodology

Meta-skill for managing CONTEXT.yaml files in evolving skills.

## CONTEXT.yaml Structure

```yaml
version: 1
meta:
  created: YYYY-MM-DD
  last_updated: YYYY-MM-DD
  skill: skill-name
  total_entries: N
  prune_threshold: 50

core: []        # Always loaded, high confidence
domain: {}      # Loaded when domain matches
archive: []     # Searchable, not auto-loaded
relations: []   # Connections between entries
lifecycle: {}   # Consolidation tracking
```

## When to Update Memory

| Event | Action |
|-------|--------|
| Pattern discovered | Add to domain or core |
| Learning confirmed | Increase confidence |
| Learning contradicted | Decrease confidence or remove |
| Same learning 3+ times | Promote to core |
| Not used in 30 days | Move to archive |
| Confidence < 0.3 | Prune |

## Phase 1: Adding Entries

### Entry Types
- **pattern**: Recurring code structure
- **learning**: Insight from specific investigation
- **gotcha**: Known issue or workaround
- **decision**: Technical choice made
- **flow**: Documented execution path

### Entry Template
```yaml
- id: unique_id
  type: pattern|learning|gotcha|decision|flow
  domain: [relevant, domains]
  content: "Description of the learning"
  confidence: 0.7  # 0.0 to 1.0
  evidence:
    - "file:line supporting this"
  created: YYYY-MM-DD
  last_used: YYYY-MM-DD
  use_count: 0
```

### Initial Confidence Guide
| Basis | Confidence |
|-------|------------|
| Single observation | 0.5 |
| Confirmed once | 0.7 |
| Confirmed multiple times | 0.85 |
| Documented/tested | 0.95 |

## Phase 2: Updating Entries

### On Successful Use
```yaml
# Increase confidence (cap at 0.99)
confidence: min(current + 0.05, 0.99)
last_used: today
use_count: current + 1
```

### On Contradiction
```yaml
# Decrease confidence
confidence: max(current - 0.15, 0.0)
# Add contradiction note
notes: "Contradicted on YYYY-MM-DD: [reason]"
```

### Promotion to Core
When entry qualifies:
- confidence >= 0.9
- use_count >= 5
- no recent contradictions

Move from domain to core section.

## Phase 3: Pruning

### Prune Criteria
- confidence < 0.3
- Not used in 60+ days AND use_count < 3
- Explicitly marked obsolete
- Referenced file no longer exists

### Prune Process
1. Identify candidates
2. Review for false positives
3. Remove or archive
4. Update total_entries

## Phase 4: Consolidation

Triggered when:
- total_entries > prune_threshold
- archive_size > 30
- days_since_last > 14
- User requests

### Consolidation Process

1. **Merge similar entries**
   ```yaml
   # Before: Two similar learnings
   - id: l1
     content: "Auth uses JWT"
   - id: l2
     content: "JWT tokens in httpOnly cookies"

   # After: Merged pattern
   - id: p1
     content: "Auth uses JWT in httpOnly cookies"
     merged_from: [l1, l2]
   ```

2. **Resolve contradictions**
   - Keep entry with more evidence
   - Or mark as context-dependent

3. **Update relationships**
   - Add discovered connections
   - Remove broken relations

4. **Prune stale entries**

5. **Rebalance tiers**
   - Promote high-confidence to core
   - Demote low-confidence to archive

## Phase 5: Retrieval

### Loading Strategy

```
1. ALWAYS load: core entries (high confidence, universal)
2. DOMAIN load: entries matching current task domain
3. ON-DEMAND: search archive when needed
```

### Domain Matching

Extract domains from current task:
- "auth bug" → load domain.auth
- "database slow" → load domain.database
- "API error" → load domain.api

## Output: Memory Report

```markdown
# Memory Status: [Skill Name]

## Overview
- Total entries: N
- Core: X
- Domain: Y
- Archive: Z

## Health
- Entries needing review: N
- Low confidence (<0.5): N
- Stale (>30 days): N

## Recent Activity
| Date | Action | Entry |
|------|--------|-------|
| YYYY-MM-DD | Added | [entry] |
| YYYY-MM-DD | Updated | [entry] |

## Recommendations
- [ ] Consolidate: N similar entries found
- [ ] Prune: N stale entries
- [ ] Review: N low-confidence entries
```

## Maintenance Commands

### Review Memory
```
"Review the memory for [skill]"
→ Load CONTEXT.yaml
→ Generate health report
→ Suggest actions
```

### Consolidate Memory
```
"Consolidate [skill] memory"
→ Run full consolidation
→ Report changes
```

### Prune Memory
```
"Prune stale entries from [skill]"
→ Identify prune candidates
→ Confirm with user
→ Remove entries
```

### Search Memory
```
"What do we know about [topic]?"
→ Search all CONTEXT.yaml files
→ Return relevant entries
```
