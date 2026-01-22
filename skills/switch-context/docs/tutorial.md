# Tutorial: switch-context

## Introduction

This tutorial guides you through using the `switch-context` skill to manage and switch between different operational contexts. Contexts customize AI agent behavior for specific projects, frameworks, or workflows.

## Prerequisites

Before starting, ensure you have:

- [ ] Access to the OLAF framework
- [ ] The `.olaf/data/context/` directory exists
- [ ] At least one context template file (context-*.md)

## Step-by-Step Instructions

### Step 1: View Available Contexts

Start by listing available contexts:

```
@switch-context
```

Or use the explicit command:

```
context list
```

You'll see a numbered list:

```
Available contexts:
1. default - General purpose development context
2. springboot-hexagonal - Spring Boot with hexagonal architecture
3. python-fastapi - Python FastAPI backend development
4. react-typescript - React with TypeScript frontend

Current active: default

Select a context by number or name:
```

### Step 2: Check Current Context Status

To see only the current status:

```
context status
```

Output:

```
Current Context: default
Available Contexts: 4
Location: .olaf/data/context/context-current.md
```

### Step 3: Switch to a Different Context

Select a context by number:

```
2
```

Or by name:

```
@switch-context context_name=springboot-hexagonal
```

The skill confirms the switch:

```
✓ Context switched to: springboot-hexagonal

⚠️ IMPORTANT: Please start a new conversation for the 
'springboot-hexagonal' context to be active. The context 
change will only take effect in a fresh session.
```

### Step 4: Start a New Session

**Critical Step**: The context change only takes effect in a new session.

1. End your current conversation
2. Start a new conversation
3. The new context is now active

### Step 5: Verify Context is Active

In your new session, the AI agent will follow the context instructions. You can verify by asking:

```
What context are you operating in?
```

Or check the status:

```
context status
```

### Step 6: Clear Context (Optional)

To remove the active context and return to default behavior:

```
context clear
```

Output:

```
✓ Context cleared successfully

⚠️ IMPORTANT: Please start a new conversation for the 
context clearing to be active.
```

## Creating Custom Contexts

### Step 1: Create a Context File

Create a new file in `.olaf/data/context/`:

```
.olaf/data/context/context-myproject.md
```

### Step 2: Add Context Content

Structure your context file:

```markdown
# MyProject Context

## Project Overview
This is a Node.js microservices project using Express and MongoDB.

## Coding Standards
- Use TypeScript for all new code
- Follow ESLint configuration
- Write unit tests for all functions

## Architecture
- Microservices pattern
- Event-driven communication
- MongoDB for persistence

## Conventions
- Use kebab-case for file names
- Use camelCase for variables
- Use PascalCase for classes
```

### Step 3: Switch to Your Context

```
@switch-context context_name=myproject
```

## Verification Checklist

After switching contexts, verify:

- [ ] Context switch confirmation received
- [ ] New session started
- [ ] AI agent follows context instructions
- [ ] Context status shows correct active context

## Troubleshooting

### Context Not Found

**Symptom**: Error message "Context 'xyz' not found"

**Cause**: The context file doesn't exist

**Solution**: 
1. Check available contexts with `context list`
2. Verify file exists: `.olaf/data/context/context-xyz.md`
3. Create the context file if needed

### Context Not Taking Effect

**Symptom**: AI agent doesn't follow context instructions

**Cause**: Session not restarted after switch

**Solution**:
1. Confirm you received the switch confirmation
2. Close current conversation completely
3. Start a fresh new conversation
4. Verify with `context status`

### Invalid Selection

**Symptom**: Error when selecting by number

**Cause**: Number out of range

**Solution**: Use a number from the displayed list, or use the context name directly

### No Contexts Available

**Symptom**: Empty context list

**Cause**: No context-*.md files in the context directory

**Solution**:
1. Navigate to `.olaf/data/context/`
2. Create at least one context file: `context-default.md`
3. Add context content
4. Run `context list` again

### File Permission Error

**Symptom**: Cannot switch or clear context

**Cause**: File system permission issue

**Solution**:
1. Check write permissions on `.olaf/data/context/`
2. Ensure `context-current.md` is not locked
3. Try clearing and re-switching

## Example Scenarios

### Scenario 1: Project-Based Context Switching

```
# Morning: Working on backend
@switch-context context_name=springboot-backend
[Start new session]
[Work on Spring Boot code with backend-specific guidance]

# Afternoon: Switch to frontend
@switch-context context_name=react-frontend
[Start new session]
[Work on React code with frontend-specific guidance]
```

### Scenario 2: Environment-Based Contexts

```
# Development work
@switch-context context_name=dev-environment
[Relaxed validation, verbose logging guidance]

# Production deployment
@switch-context context_name=prod-environment
[Strict validation, security-focused guidance]
```

## Next Steps

After mastering context switching:

1. **Create project-specific contexts** - Customize for each project
2. **Share contexts with team** - Standardize team workflows
3. **Combine with carry-over** - Use `carry-over-session` to preserve work across context switches
4. **Document your contexts** - Keep context files well-documented for team use
