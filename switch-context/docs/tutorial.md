# Context Switch: Step-by-Step Tutorial

**How to Execute the "Context Switch" Workflow**

This tutorial shows exactly how to switch between different project contexts in OLAF.

## Prerequisites

- OLAF framework installed and active
- At least one context template file in `.olaf/data/context/`
- Access to GitHub Copilot Chat or compatible IDE

## Step-by-Step Instructions

### Step 1: List Available Contexts
Brief: Check what contexts are available to switch to

**User Action:**
1. Open GitHub Copilot Chat
2. Type: `context switch`
3. Press Enter

**Copilot Response:**
```
Available contexts:
1. default
2. springboot-hexagonal

Select context by number:
```

### Step 2: Select Context by Number
**User Action:** Type the number of the context you want

```
2
```

**Provide Selection:**
- Enter the number corresponding to your desired context
- Example: We selected "2" for springboot-hexagonal

### Step 3: Context Switch Execution
**What Copilot Does:**
- Validates the selected context file exists
- Copies `.olaf/data/context/context-springboot-hexagonal.md` to `.olaf/data/context/context-current.md`
- Confirms the switch

**You Should See:** 
```
✓ Switched to context: springboot-hexagonal
⚠️ Start new conversation for context to activate
```

### Step 4: Start New Session
**User Action:**
1. Close the current Copilot Chat conversation
2. Open a new Copilot Chat conversation
3. The new context is now automatically loaded via bootstrap

**What Happens:**
- OLAF bootstrap loads the active context file
- Project-specific context is applied to the session
- You're now working with the new context active

## Verification Checklist

✅ **Context file copied** - Check `.olaf/data/context/context-current.md` exists
✅ **New session started** - Opened fresh Copilot conversation
✅ **Context loaded** - Bootstrap loaded the new context automatically
✅ **Ready to work** - Can now work with project-specific context

## Troubleshooting

**If context doesn't seem active:**
```
Make sure you started a NEW conversation. 
Context changes only take effect in fresh sessions.
```

**If no contexts are listed:**
- Check `.olaf/data/context/` directory exists
- Ensure you have at least one `context-*.md` file
- File naming must follow pattern: `context-{name}.md`

**If "context not found" error:**
- Verify the context file exists in `.olaf/data/context/`
- Check file name matches pattern exactly

## Key Learning Points

1. **Context switch requires new session:** Changes only take effect when you start a fresh conversation because the bootstrap process runs at session start.

2. **context-current.md is the active file:** This file gets overwritten each time you switch. The template files (context-*.md) remain unchanged.

3. **Bootstrap automatic loading:** You don't need to manually load the context. In this repo, bootstrap behavior is defined in `.windsurf/rules/olaf-bootstrap-skills.md` and loads (in order):
	- `.olaf/context/current-context.md` (preferred)
	- `.olaf/data/context/context-current.md` (legacy)
	- `.olaf/data/context/context-default.md` (fallback)

## Next Steps to Try

- Create your own custom context template in `.olaf/data/context/context-myproject.md`
- Use `context status` to check which context is currently active
- Use `context clear` to remove the active context and return to default OLAF framework
- Switch between multiple project contexts as you work on different codebases

## Expected Timeline

- **Total context switch time:** 10-30 seconds
- **User input required:** Select context number, start new session
- **Copilot execution time:** Instant (file copy operation)
