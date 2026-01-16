# Tutorial: should-i-use-ai

## Introduction

This tutorial guides you through using the `should-i-use-ai` skill to determine the best approach for your development tasks. By the end, you'll know how to quickly decide between AI assistance and traditional IDE tools for maximum efficiency.

## Prerequisites

Before starting, ensure you have:

- [ ] A clear understanding of the task you want to accomplish
- [ ] Access to both AI/LLM tools and your IDE
- [ ] Familiarity with basic IDE features

## Step-by-Step Instructions

### Step 1: Formulate Your Task

Describe your task in a single, clear sentence. Be specific about what you want to accomplish.

Good examples:
- "Refactor this function to use async/await"
- "Generate unit tests for my authentication module"
- "Rename all occurrences of 'userId' to 'customerId'"

Avoid vague descriptions:
- "Help me with my code" (too broad)
- "Make it better" (unclear goal)

### Step 2: Invoke the Skill

Present your task to the skill:

```
Should I use AI for: [your task description]
```

Or simply:

```
[your task description]
```

### Step 3: Review the Recommendation

The skill will provide one of two recommendations:

**🔧 IDE Tools Recommendation**:
```
Recommendation: Use IDE Tools

Task Category: [Category]
Specific Actions:
- IDE Feature: [Feature name]
- Keyboard Shortcut: [Shortcut]
- CLI Alternative: [Command]

Why IDE: [Explanation]
```

**🧠 AI/LLM Recommendation**:
```
Recommendation: Use AI/LLM

Task Category: [Category]
Suggested Prompt: [Generated prompt]

Why AI: [Explanation]
```

### Step 4: Follow the Guidance

**If IDE Tools are recommended:**

1. Open your IDE
2. Navigate to the suggested feature
3. Use the keyboard shortcut if provided
4. Apply the operation to your code

**If AI/LLM is recommended:**

1. Check for existing prompts in your competency index
2. Use the suggested prompt or customize it
3. Review and apply the AI-generated solution

### Step 5: Evaluate the Result

After completing the task:

1. Verify the outcome meets your expectations
2. Note whether the recommendation was appropriate
3. Consider the time saved by using the right tool

## Verification Checklist

After using the skill, verify:

- [ ] Recommendation was clear and actionable
- [ ] Specific tools or prompts were provided
- [ ] Reasoning made sense for your task
- [ ] You were able to complete the task efficiently

## Understanding the Categories

### Tasks Best for IDE Tools

| Category | Examples |
|----------|----------|
| Basic Code Manipulation | Rename, extract method, inline variable |
| File Operations | Create, move, delete files |
| Navigation | Go to definition, find usages |
| Template Generation | Getters/setters, constructors |
| Formatting | Auto-format, organize imports |
| Version Control | Commit, diff, merge |

### Tasks Best for AI/LLM

| Category | Examples |
|----------|----------|
| Logic & Reasoning | Debug complex issues, optimize algorithms |
| Context-Aware Generation | Write tests based on implementation |
| Intelligent Refactoring | Redesign architecture, apply patterns |
| Migration | Update API versions, change frameworks |
| Analysis | Security review, code quality assessment |

## Troubleshooting

### "Recommendation doesn't seem right"

**Cause**: Task description may be ambiguous or span multiple categories.

**Solution**: Provide more specific details about what you're trying to accomplish.

### "I don't have the suggested IDE feature"

**Cause**: IDE features vary between editors.

**Solution**: Search for equivalent functionality in your IDE or use the CLI alternative if provided.

### "The suggested prompt doesn't work well"

**Cause**: AI prompts may need customization for your specific context.

**Solution**: Modify the prompt to include more context about your codebase or requirements.

## Next Steps

After mastering this skill:

1. **Build Intuition**: Over time, you'll naturally know which tool to use
2. **Learn IDE Shortcuts**: Invest time in learning your IDE's capabilities
3. **Refine AI Prompts**: Develop a library of effective prompts for common tasks
4. **Share Knowledge**: Help teammates understand when to use each approach
5. **Track Efficiency**: Note which recommendations save you the most time
