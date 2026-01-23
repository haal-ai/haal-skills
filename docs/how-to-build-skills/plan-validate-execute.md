# Plan-Validate-Execute Pattern

When the agent performs complex, open-ended tasks, it can make mistakes. The "plan-validate-execute" pattern catches errors early by having the agent first create a plan in a structured format, then validate that plan with a script before executing it.

## The Problem

Imagine asking the agent to refactor 20 functions across multiple files to apply consistent error handling. Without validation, the agent might:
- Miss some functions
- Break existing tests
- Introduce inconsistent patterns
- Forget to update callers

## The Solution

Add an intermediate plan file that gets validated before applying changes:

1. **Analyze** → understand the scope
2. **Create plan file** → structured JSON/YAML output
3. **Validate plan** → script checks for errors
4. **Execute** → apply changes
5. **Verify** → tests pass

## Why This Pattern Works

- **Catches errors early**: Validation finds problems before changes are applied
- **Machine-verifiable**: Scripts provide objective verification
- **Reversible planning**: The agent can iterate on the plan without touching originals
- **Clear debugging**: Error messages point to specific problems

## When to Use

- Batch operations
- Destructive changes
- Complex validation rules
- High-stakes operations

## Progress Tracking

For long-running tasks, ask the agent to iterate through the plan and mark each task as done (e.g., with a checkbox `[x]`). This allows you to:
- Resume in a new session if the context window is exhausted
- Continue later without losing track of progress
- Easily see what's completed vs remaining

Example plan format:
```markdown
- [x] Refactor `process_payment` in billing.py
- [x] Update callers in checkout.py
- [ ] Add error handling to `validate_card`
- [ ] Update tests
```

## Implementation Tip

Make validation scripts verbose with specific error messages:

```
"Function 'process_payment' not found in src/billing.py. 
Available functions: calculate_total, apply_discount, generate_invoice"
```

This helps the agent fix issues quickly.
