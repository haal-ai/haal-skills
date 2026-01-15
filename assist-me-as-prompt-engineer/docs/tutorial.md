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

Usage: olaf create prompt

Expected Outcome: 
- Complete prompt in skills/[your-prompt-name]/
- Validation against best practices
- Ready-to-use code review capability

Next Step: Run `olaf create prompt` and I'll guide you through the process.
```

**Step 2**: Follow the recommendation
```bash
olaf create prompt
```

**Step 3**: Complete the guided creation process

#### Scenario 2: Sharing Your Prompts
**Goal**: Share prompts with team

**Command**:
```bash
olaf prompt help "How do I share my prompts?"
```

**Expected Guidance**:
- Recommendation: `share-my-prompts`
- Export process explained
- Team distribution steps

#### Scenario 3: Importing Existing Prompts
**Goal**: Import a ChatGPT prompt unchanged

**Command**:
```bash
olaf guide me "I have a prompt from ChatGPT to import"
```

**Expected Guidance**:
- Recommendation: `import-prompt-unchanged`
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
- Manifest created

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
- Recommendation: `convert-prompt`
- Conversion process explained
- Validation steps included

#### Scenario 6: Organizing Competencies
**Goal**: Choose competency collection for project

**Command**:
```bash
olaf guide me "How do I organize my competencies?"
```

**Expected Guidance**:
- Recommendation: `select-competency-collection`
- Collection management explained
- Best practices provided

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
2. convert-prompt - Ensure OLAF compliance
3. deploy-imported-prompts - Deploy to framework
4. validate-prompt-value - Verify effectiveness

Alternative: Use generate-workflow to create a reusable chain.

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

#### Scenario 9: Competency Management
**Goal**: Manage competency package lifecycle

**Command**:
```bash
olaf guide me "I manage several competency packages"
```

**Expected Guidance**:
- Recommendation: `manage-competencies`
- Lifecycle management explained
- Best practices for teams

### Level 4: Expert Tasks

#### Scenario 10: Framework Optimization
**Goal**: Improve framework loading performance

**Command**:
```bash
olaf prompt assistant "The framework is loading slowly"
```

**Expected Response**:
```
Assessment: Expert level task - framework optimization
Recommendation: condense-olaf-framework

This optimizes framework loading by condensing competencies
into an efficient format.

Usage: olaf condense olaf framework

Expected Outcome:
- Reduced loading time
- Optimized framework structure
- Maintained functionality

Next Step: Run condensation and benchmark improvements.
```

#### Scenario 11: Contributing to OLAF Core
**Goal**: Share prompt with framework

**Command**:
```bash
olaf prompt help "I want to contribute this prompt to OLAF core"
```

**Expected Guidance**:
- Recommendation: `share-prompt-to-olaf`
- Contribution process explained
- Quality requirements outlined
- Review process described

#### Scenario 12: Architectural Refactoring
**Goal**: Restructure competency as skill

**Command**:
```bash
olaf guide me "I need to refactor this competency architecture"
```

**Expected Guidance**:
- Recommendation: `migrate-competency-to-skill`
- Migration strategy explained
- Backward compatibility addressed
- Validation steps included

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

### Beginner → Trained
**When Ready**:
- Comfortable with `create-prompt`
- Created several prompts successfully
- Understand prompt structure

**Next Steps**:
- Try `create-skill`
- Explore `convert-prompt`
- Learn `select-competency-collection`

### Trained → Advanced
**When Ready**:
- Built multiple skills
- Managed prompt collections
- Understand skill architecture

**Next Steps**:
- Try `generate-workflow`
- Explore `convert-skill-to-chain`
- Learn `manage-competencies`

### Advanced → Expert
**When Ready**:
- Created complex workflows
- Managed competency packages
- Contributed to team capabilities

**Next Steps**:
- Try `share-prompt-to-olaf`
- Explore `condense-olaf-framework`
- Learn `verify-competency-compliance`

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

- `list-skills` - Browse all available skills
- `use-skill` - Execute specific skills directly
- `help-me-olaf` - General OLAF assistance
- `tell-me` - Learn about OLAF features

## Summary

The Prompt Engineering Assistant is your guide through OLAF's capabilities:
- ✓ Assesses your expertise automatically
- ✓ Recommends appropriate skills
- ✓ Guides complex workflows
- ✓ Suggests learning paths
- ✓ Adapts to your growth

Start with simple tasks, progress naturally, and let the assistant guide your journey from beginner to expert prompt engineer.
