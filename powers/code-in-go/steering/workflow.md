# Go Coding Session Workflow

## Agent Directives

At session start:
1. Load all steering files silently
2. Respond with: `🔧 Go session ready. What are we building?`

During coding:
1. **Apply all practices automatically** — Don't list them, just use them
2. **Show code, not process** — Skip verbose sections like "Practices Applied"
3. **Inline commit suggestions** — After ~20 min of work, add a brief reminder
4. **Only interrupt for violations** — Brief warning + compliant alternative

## When to Warn

Only show warnings for:
- User on protected branch (`main`/`master`/`develop`) → prompt to create feature branch
- Code that ignores errors → show fix
- Missing tests for new behavior → generate them

Keep warnings brief:
```
⚠️ You're on main. Create a branch first:
git checkout -b feature/<name>
```

## Output Style

DO:
- Show clean, working code
- Include tests inline with implementation
- Suggest commit message after significant changes

DON'T:
- List "Practices Applied"
- Show "Impact Analysis" for small changes
- Ask "Proceed?" for straightforward requests
- Use verbose multi-section formats

## Rules Summary

| Rule | Action |
|------|--------|
| Error ignored with `_` | Fix silently or warn |
| Missing error wrap | Add `fmt.Errorf("context: %w", err)` |
| External dep not injected | Refactor to accept interface |
| No tests for new code | Generate table-driven tests |
| ~20 min without commit | Brief inline reminder |
| On protected branch | Prompt for feature branch |
