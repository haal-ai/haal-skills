# Tutorial: assist-me-as-prompt-engineer

## Introduction

This tutorial shows you how to use the `assist-me-as-prompt-engineer` skill to get personalized guidance on prompt engineering tasks. The skill assesses your expertise level and recommends the most appropriate skills and workflows for your needs.

## Prerequisites

Before starting, ensure you have:

- [ ] Access to the OLAF framework
- [ ] A clear idea of what you want to accomplish
- [ ] Basic understanding of prompt engineering concepts (helpful but not required)

## Step-by-Step Instructions

### Step 1: Invoke the Skill

Start by invoking the skill with your task:

```
@assist-me-as-prompt-engineer I want to create a prompt for API documentation
```

Or invoke without a task for interactive guidance:

```
@assist-me-as-prompt-engineer
```

### Step 2: Provide Task Description (if not already provided)

If you didn't include a task, the skill will ask:

```
What would you like to accomplish with prompt engineering today?
```

Describe your goal clearly:

```
I need to create a prompt that helps generate API documentation from code comments.
```

### Step 3: Expertise Level Assessment

The skill assesses your level based on task complexity. You can also specify it:

```
@assist-me-as-prompt-engineer expertise_level=trained I want to build a skill
```

**Expertise Levels:**
- **Beginner**: Creating first prompts, learning basics
- **Trained**: Creating skills, converting prompts, evaluating quality
- **Advanced**: Building orchestrators, chains, validating effectiveness

### Step 4: Review the Recommendation

The skill provides a structured recommendation:

```
Assessment: Trained level task - skill development

Primary Skill: `create-skill`
- Purpose: Build a complete skill with prompts and workflows
- Usage: @create-skill
- Expected Outcome: Full skill package with documentation

Supporting Skills:
- `check-prompt-compliance`: Validate your prompts
- `create-skill-description`: Generate documentation

Next Step: Would you like me to start the skill creation process?
```

### Step 5: Follow the Guidance

Based on the recommendation, take action:

**Option A: Execute the recommended skill**
```
Yes, let's start creating the skill
```

**Option B: Ask for more details**
```
Can you explain what create-skill will produce?
```

**Option C: Request alternatives**
```
What other options do I have?
```

### Step 6: Multi-Step Workflow (for complex tasks)

For complex tasks, you'll receive a workflow proposal:

```
Multi-Step Workflow for: Validate and deploy prompts

Step 1: `evaluate-prompt-for-adoption`
   Purpose: Assess prompt quality and fit
   Output: Evaluation report

Step 2: `check-prompt-compliance`
   Purpose: Validate directive quality
   Output: Compliance status

Step 3: `convert-prompt-to-skill`
   Purpose: Package into skill structure
   Output: Complete skill package

Would you like me to execute this workflow for you? (yes/no)
```

### Step 7: Learning Path Suggestions

The skill may suggest advancement opportunities:

```
Learning Path Suggestion:
Once comfortable with `create-prompt`, try `create-skill` to build 
complete capabilities with multiple prompts and workflows.
```

## Verification Checklist

After receiving guidance, verify:

- [ ] You understand the recommended skill's purpose
- [ ] You know how to invoke the recommended skill
- [ ] You understand what output to expect
- [ ] You have a clear next action to take
- [ ] You understand any prerequisites needed

## Troubleshooting

### Recommendation Doesn't Match My Needs

**Symptom**: The suggested skill doesn't fit your task

**Solution**: Provide more details about your goal:
```
Actually, I need something more specific. I want to [detailed description]
```

### Skill Level Seems Wrong

**Symptom**: Recommendations are too basic or too advanced

**Solution**: Explicitly set your expertise level:
```
@assist-me-as-prompt-engineer expertise_level=advanced [your task]
```

### Unknown Task Error

**Symptom**: Skill can't map your request to any capability

**Solution**: The skill will offer alternatives:
```
I'm not sure which skill fits this task. Let me ask some clarifying questions...

Alternatively, try:
- `help-me-olaf` for general assistance
- `tell-me` for information and explanations
```

### Multiple Options Presented

**Symptom**: Several skills could work for your task

**Solution**: Review the trade-offs and choose:
```
Options for your task:
1. `create-skill` - Full skill with workflows (more comprehensive)
2. `convert-prompt-to-skill` - Quick conversion (faster)
3. `create-prompt` - Just the prompt (simplest)

Which approach fits your needs?
```

## Example Scenarios

### Scenario 1: First-Time User

```
User: @assist-me-as-prompt-engineer I'm new and want to create my first prompt

Agent: 
Assessment: Beginner level - first prompt creation

Primary Skill: `create-prompt`
This skill guides you through creating a structured prompt using 
proven templates. Perfect for getting started.

Usage: @create-prompt

Expected Outcome:
- Staged prompt in `.olaf/staging/generated-prompts/`
- Follows prompt engineering best practices

Next Step: What type of prompt do you want to create? 
(code review, documentation, analysis, etc.)
```

### Scenario 2: Experienced User with Complex Task

```
User: @assist-me-as-prompt-engineer expertise_level=advanced 
      I need to create a workflow that validates, tests, and deploys prompts

Agent:
Assessment: Advanced level - workflow orchestration

Recommendation: Use `generate-orchestrator` to create a permanent 
automated workflow.

Workflow Components:
1. `evaluate-prompt-for-adoption` → Quality gate
2. `check-prompt-compliance` → Compliance validation
3. `validate-prompt-value` → Effectiveness metrics
4. `convert-prompt-to-skill` → Packaging

Next Step: Should I help you create this orchestrator, or execute 
the workflow manually first to test it?
```

## Next Steps

After receiving guidance:

1. **Execute the recommended skill** - Follow the provided usage instructions
2. **Explore supporting skills** - Try related skills for comprehensive results
3. **Follow the learning path** - Build expertise progressively
4. **Return for more guidance** - Use this skill whenever you need direction
