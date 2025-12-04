---
name: trace-flow
description: >
  Traces code execution paths, data flow, and file interconnections.
  Use when: (1) user asks "how does X work", (2) understanding call chains,
  (3) tracing request/response flow, (4) debugging execution order,
  (5) mapping component relationships, (6) understanding data transformations.
---

# Code Flow Tracing Methodology

Systematic process for understanding how code executes and data flows.

## Flow Types

Identify which flow type you're tracing:

| Type | Question | Focus |
|------|----------|-------|
| **Execution** | "What happens when X?" | Function calls, order |
| **Data** | "How does data get from A to B?" | Transformations, state |
| **Control** | "What decides X?" | Conditionals, routing |
| **Event** | "What triggers X?" | Listeners, callbacks |
| **Error** | "What happens when X fails?" | Catch blocks, fallbacks |

## Phase 1: Identify Entry Points

Find where the flow starts:

1. **HTTP/API flows**
   - Route definitions (`router.get`, `app.post`, `@Get()`)
   - Controller methods
   - Middleware chain

2. **Event flows**
   - Event listeners (`on`, `addEventListener`, `subscribe`)
   - Message handlers
   - Webhook receivers

3. **User interaction flows**
   - Click handlers, form submissions
   - Component lifecycle hooks
   - State change triggers

4. **Scheduled/background flows**
   - Cron jobs, schedulers
   - Queue consumers
   - Background workers

## Phase 2: Trace Forward (Downstream)

From entry point, follow execution:

1. **Direct calls**
   ```
   functionA() → functionB() → functionC()
   ```

2. **Async boundaries**
   - Promises, async/await
   - Callbacks
   - Event emissions

3. **External calls**
   - Database queries
   - API requests
   - File system operations

4. **State mutations**
   - Variable assignments
   - Store updates (Redux, Vuex, etc.)
   - Cache writes

Document as you go:
```
1. [entry.ts:10] handleRequest(req)
   └─ 2. [validator.ts:25] validate(req.body)
      └─ 3. [service.ts:50] processData(validated)
         ├─ 4. [db.ts:100] query(sql)
         └─ 5. [cache.ts:30] set(key, result)
```

## Phase 3: Trace Backward (Upstream)

From a point of interest, trace what leads there:

1. **Find all callers**
   ```
   Search: functionName(
   ```

2. **Find all triggers**
   - What events cause this?
   - What conditions must be true?

3. **Find data sources**
   - Where do the parameters come from?
   - What state is read?

## Phase 4: Map Data Transformations

Track how data changes shape:

```
Input: { user_id: 123, action: "purchase" }
   │
   ├─ [validator.ts] → { userId: 123, action: "purchase" }  // camelCase
   │
   ├─ [enricher.ts] → { userId: 123, action: "purchase", user: {...} }  // added user
   │
   ├─ [processor.ts] → { orderId: "abc", userId: 123, ... }  // transformed
   │
   └─ Output: { success: true, orderId: "abc" }
```

Note:
- Type conversions
- Field renames
- Additions/removals
- Aggregations

## Phase 5: Identify Branching Points

Find where flow can diverge:

1. **Conditionals**
   ```typescript
   if (user.isAdmin) {
     // Branch A
   } else {
     // Branch B
   }
   ```

2. **Error boundaries**
   ```typescript
   try {
     // Happy path
   } catch {
     // Error path
   }
   ```

3. **Feature flags**
   ```typescript
   if (featureEnabled('newFlow')) {
     // New flow
   }
   ```

4. **Routing decisions**
   - Strategy patterns
   - Factory methods
   - Dynamic dispatch

## Phase 6: Document Side Effects

Identify all side effects:

- **Writes**: Database, file system, cache
- **Sends**: API calls, emails, notifications
- **Logs**: Audit trails, analytics
- **State**: Global state, session, cookies

## Output: Flow Report

Structure findings as:

```markdown
# Flow Report: [Flow Name]

## Overview
[One paragraph describing this flow]

## Entry Points
| Entry | File | Trigger |
|-------|------|---------|
| handlePurchase | api/purchase.ts:20 | POST /api/purchase |

## Execution Flow

### Happy Path
```
1. [api/purchase.ts:20] handlePurchase(req)
   │  Validates request body
   │
   ├─ 2. [services/cart.ts:50] getCart(userId)
   │     │  Fetches user's cart from DB
   │     │
   │     └─ 3. [db/queries.ts:100] findCart(userId)
   │           DB query: SELECT * FROM carts WHERE user_id = ?
   │
   ├─ 4. [services/payment.ts:30] processPayment(cart, paymentInfo)
   │     │  Charges payment provider
   │     │
   │     └─ 5. [external/stripe.ts:20] charge(amount, token)
   │           External API: POST stripe.com/v1/charges
   │
   └─ 6. [services/order.ts:40] createOrder(cart, payment)
         │  Creates order record
         │
         ├─ 7. [db/queries.ts:150] insertOrder(order)
         │     DB write: INSERT INTO orders
         │
         └─ 8. [services/email.ts:25] sendConfirmation(order)
               Side effect: Sends email
```

### Error Paths
- **Payment fails** at step 4 → Returns 402, no order created
- **Cart not found** at step 2 → Returns 404

## Data Transformations
[How data shape changes through the flow]

## Side Effects
| Effect | Location | Description |
|--------|----------|-------------|
| DB Write | step 7 | Creates order record |
| Email | step 8 | Sends confirmation |
| External API | step 5 | Charges Stripe |

## Dependencies
[External services, databases, etc.]

## Potential Issues
[Race conditions, error handling gaps, etc.]
```

## Techniques

### Following Async Code
- Track Promise chains
- Note callback registrations
- Watch for event emissions
- Follow queue messages

### Handling Indirection
- Dependency injection → check container/config
- Strategy pattern → list all implementations
- Event bus → find all subscribers
- Dynamic imports → search for import patterns

### Reading Framework Code
- Know common patterns (MVC, middleware, hooks)
- Check framework documentation for lifecycle
- Look for decorators/annotations that add behavior
