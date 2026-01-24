# Quarkus Coding Session Workflow

## Agent Directives

At session start:
1. Load all steering files silently
2. Respond with: `⚡ Quarkus session ready. What are we building?`

During coding:
1. **Apply all practices automatically** — Don't list them, just use them
2. **Show code, not process** — Skip verbose sections like "Practices Applied"
3. **Inline commit suggestions** — After ~20 min of work, add a brief reminder
4. **Only interrupt for violations** — Brief warning + compliant alternative

## When to Warn

Only show warnings for:
- User on protected branch (`main`/`master`/`develop`) → prompt to create feature branch
- Field injection instead of constructor injection → show fix
- Missing tests for new endpoints → generate them

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
| Field injection `@Inject` on field | Refactor to constructor injection |
| Missing error handling | Add `ExceptionMapper` or proper Response |
| No validation on input | Add Bean Validation annotations |
| No tests for new endpoint | Generate `@QuarkusTest` with RestAssured |
| ~20 min without commit | Brief inline reminder |
| On protected branch | Prompt for feature branch |

## Dev Mode Commands

```bash
# Start dev mode with live reload
./mvnw quarkus:dev

# Run tests continuously
./mvnw quarkus:test

# Build native image
./mvnw package -Dnative

# Generate project
mvn io.quarkus.platform:quarkus-maven-plugin:create
```
