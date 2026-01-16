# Prompt Engineering Assistant - Tutorial

## Introduction
This tutorial walks you through using the Prompt Engineering Assistant to navigate OLAF's prompt engineering capabilities based on your expertise level.

## Prerequisites
- OLAF framework installed
- Basic understanding of prompt engineering concepts
- Access to terminal/command line

## Learning Path

### Level 1: Beginner Tasks

#### Scenario 1: Creating Your First Prompt
**Goal**: Create a code review prompt

**Step 1**: Ask for assistance
```bash
olaf prompt assistant "I need to create a code review prompt"
```

**Expected Response**:
```
Assessment: Beginner level task - first prompt creation
Recommendation: create-prompt

This skill guides you through creating a structured code review 
prompt using proven templates.

Usage: use the `create-prompt` skill

Expected Outcome: 
- Staged prompt file in `.olaf/staging/generated-prompts/`
- Prompt follows prompt engineering principles
- Ready-to-use code review capability

Next Step: Tell me what you want the prompt to do and I’ll draft it.
```

#### Scenario 2: Checking Prompt Compliance
**Goal**: Validate a prompt before using it

**Command**:
```bash
olaf prompt help "Is this prompt compliant?"
```

**Expected Guidance**:
- Recommendation: `check-prompt-compliance`
- What is non-compliant and why
- Concrete edits to make it compliant

#### Scenario 3: Importing Existing Prompts
**Goal**: Bring a ChatGPT prompt into OLAF

**Command**:
```bash
olaf guide me "I have a prompt from ChatGPT to import"
```

**Expected Guidance**:
- Recommendation: `convert-prompt-to-skill`
- Import process steps
- Where prompt will be stored

### Level 2: Trained Tasks

#### Scenario 4: Building Your First Skill
**Goal**: Create a skill with multiple prompts

**Step 1**: Request assistance
```bash
olaf prompt assistant "I want to create a skill with multiple prompts"
```

**Expected Response**:
```
Assessment: Trained level task - skill development
Recommendation: create-skill

Ready to build complete capabilities? This skill helps you create
a full skill package with prompts, docs, and workflows.

Usage: olaf create skill

Expected Outcome:
- Complete skill structure
- Multiple prompts organized
- Documentation generated

Next Step: Run `olaf create skill` to begin.
```

**Step 2**: Execute the skill creation

#### Scenario 5: Modernizing Legacy Prompts
**Goal**: Update old prompts to OLAF standards

**Command**:
```bash
olaf prompt help "I have old prompts that need updating"
```

**Expected Guidance**:
- Recommendation: `convert-prompt-to-skill`
- Conversion/packaging steps explained
- Validation steps included

#### Scenario 6: Creating Prompt Documentation
**Goal**: Generate documentation for a prompt/skill

**Command**:
```bash
olaf guide me "Generate docs for this prompt"
```

**Expected Guidance**:
- Recommendation: `create-skill-description`
- What it will extract and how it structures the docs

### Level 3: Advanced Tasks

#### Scenario 7: Creating a Workflow
**Goal**: Build workflow that validates then deploys prompts

**Step 1**: Request workflow guidance
```bash
olaf prompt assistant "I need a workflow that validates then deploys prompts"
```

**Expected Response**:
```
Assessment: Advanced level task - workflow orchestration
Recommendation: Multi-step workflow

Workflow:
1. evaluate-prompt-for-adoption - Assess prompt quality
2. check-prompt-compliance - Ensure directive quality and compliance
3. convert-prompt-to-skill - Package prompt content into a skill structure
4. validate-prompt-value - Verify effectiveness
5. validate-olaf-artifacts - Validate local artifacts holistically (optional)

Alternative: Use generate-orchestrator to create an orchestrator.

Next Step: Would you like me to execute this workflow, or create 
a permanent workflow chain? (workflow/chain)
```

**Step 2**: Choose execution or chain creation
```bash
# For one-time execution
> workflow

# For reusable chain
> chain
```

#### Scenario 8: Skill Chain Creation
**Goal**: Convert skill to executable chain

**Command**:
```bash
olaf prompt help "How do I chain multiple skills together?"
```

**Expected Guidance**:
- Recommendation: `convert-skill-to-chain`
- Chain architecture explained
- Execution model described

## Common Patterns

### Pattern 1: "I Don't Know What Skill to Use"
**Solution**: Describe your goal, let the assistant recommend

```bash
olaf prompt assistant "I want to [your goal]"
```

### Pattern 2: "I'm Not Sure About My Level"
**Solution**: The assistant auto-assesses based on your task

No need to specify level - it's determined automatically

### Pattern 3: "I Need Multiple Skills"
**Solution**: Request workflow orchestration

```bash
olaf prompt help "I need to [complex multi-step goal]"
```

The assistant will propose a complete workflow

### Pattern 4: "I Want to Learn More"
**Solution**: Ask about advancement

```bash
olaf guide me "What should I learn next?"
```

## Progression Path

### Beginner to Trained
**When Ready**:
- Comfortable with `create-prompt`
- Created several prompts successfully
- Understand prompt structure

**Next Steps**:
- Try `create-skill`
- Explore `convert-prompt-to-skill`
- Try `create-skill-description`

### Trained to Advanced
**When Ready**:
- Built multiple skills
- Managed prompt collections
- Understand skill architecture

**Next Steps**:
- Try `generate-orchestrator`
- Explore `convert-skill-to-chain`
- Try `validate-olaf-artifacts`

## Tips and Best Practices

### Tip 1: Be Specific About Your Goal
**Less Effective**: "Help with prompts"
**More Effective**: "I need to create a prompt that reviews Python code for security issues"

### Tip 2: Don't Worry About Your Level
The assistant automatically assesses and recommends appropriately

### Tip 3: Ask for Workflows
For multi-step tasks, explicitly mention "workflow" to get orchestration guidance

### Tip 4: Use Aliases
Multiple ways to invoke:
- `olaf prompt assistant`
- `olaf prompt help`
- `olaf guide me`
- `olaf pe assistant`

### Tip 5: Follow Learning Paths
Progress naturally through levels - the assistant will suggest when you're ready for more

## Troubleshooting

### Issue: "I Got a Skill I Don't Understand"
**Solution**: Ask for tutorial
```bash
olaf tell me about [skill-name]
```

### Issue: "The Recommended Skill Seems Too Advanced"
**Solution**: Ask for prerequisites
```bash
olaf prompt help "What do I need to learn before [skill-name]?"
```

### Issue: "I Need Multiple Skills But Don't Know the Order"
**Solution**: Request workflow
```bash
olaf prompt assistant "workflow for [your complex goal]"
```

### Issue: "I'm Not Finding the Right Skill"
**Solution**: Browse all skills
```bash
olaf list skills
```

Then describe to assistant which one matches your need

## Next Steps

1. **Start Simple**: Begin with beginner skills
2. **Practice Regularly**: Create prompts frequently
3. **Progress Gradually**: Move to next level when comfortable
4. **Ask Questions**: Use the assistant whenever unsure
5. **Contribute Back**: Share your prompts with the community

## Related Skills

- `help-me-olaf` - General OLAF assistance
- `tell-me` - Learn about OLAF features

## Summary

The Prompt Engineering Assistant is your guide through OLAF's capabilities:
- Assesses your expertise automatically
- Recommends appropriate skills
- Guides complex workflows
- Suggests learning paths
- Adapts to your growth

Start with simple tasks, progress naturally, and let the assistant guide your journey from beginner to advanced prompt engineer.
