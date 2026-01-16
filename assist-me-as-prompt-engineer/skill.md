---
name: assist-me-as-prompt-engineer
description: Guide prompt engineers through available skills based on expertise level
license: Apache-2.0
metadata:
  olaf_tags: [prompt-engineering, assistant, learning, guidance, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **task_description**: string - What the user wants to accomplish (REQUIRED)
- **expertise_level**: string - User's prompt engineering skill level: beginner/trained/advanced (OPTIONAL - will assess if not provided)

## User Interaction Protocol
You MUST follow the established interaction protocol:
- Use **Act** for skill recommendations and guidance
- Use **Propose-Confirm-Act** when executing complex workflows on user's behalf

## Process

### 1. Skill Level Assessment Phase
If expertise_level not provided, you WILL assess based on task complexity and user's question:
- **Beginner**: Creating first prompts, learning basics, following templates
- **Trained**: Creating skills, converting prompts into skills, evaluating prompts
- **Advanced**: Building orchestrators/chains, validating prompts and artifacts

### 2. Skill Mapping Phase
You WILL identify appropriate skills based on user's level and task:

#### Beginner Level Skills
**Core Capabilities:**
- `create-prompt` - Draft a prompt and stage it under `.olaf/staging/generated-prompts/`
- `check-prompt-compliance` - Check prompt compliance and directive quality

**When to Recommend:**
- User needs to create their first prompt
- User wants to verify whether a prompt is compliant

**Example Tasks:**
- "I need to create a prompt for code reviews"
- "Is this prompt compliant with our principles?"

#### Trained Level Skills
**Core Capabilities:**
- `create-skill` - Build complete skills with prompts and workflows
- `convert-prompt-to-skill` - Convert or wrap prompt content into a skill structure
- `evaluate-prompt-for-adoption` - Assess prompts for framework integration
- `create-skill-description` - Generate docs/description.md for an existing skill

**When to Recommend:**
- User understands prompt basics, ready for skill development
- User has existing prompt text and wants a proper skill package
- User needs to evaluate external prompts for adoption
- User needs documentation for an existing prompt

**Example Tasks:**
- "I want to create a skill with multiple prompts"
- "Should we adopt this prompt from the community?"
- "Generate docs for this prompt"

#### Advanced Level Skills
**Core Capabilities:**
- `generate-orchestrator` - Create orchestrator skills combining other skills
- `convert-skill-to-chain` - Transform skills into executable chains
- `validate-prompt-value` - Deep analysis of prompt effectiveness

**When to Recommend:**
- User needs to orchestrate multiple skills together
- User wants to create reusable skill chains
- User needs metrics on prompt performance
- User wants to validate the local skills/artifacts holistically

**Example Tasks:**
- "I need a workflow that validates then deploys prompts"
- "How do I chain multiple skills together?"
- "What's the ROI of this prompt?"
- "How do I validate prompt effectiveness?"


### 3. Recommendation Phase
You WILL provide clear, actionable guidance:

**Recommendation Format:**
```
Based on your [LEVEL] expertise and task "[TASK]", I recommend:

Primary Skill: `[skill-name]`
- Purpose: [Why this skill fits the task]
- Usage: [How to invoke it]
- Expected Outcome: [What user will achieve]

Supporting Skills (optional):
- `[skill-name]`: [Brief purpose]
- `[skill-name]`: [Brief purpose]

Next Step: [Clear action for user to take]
```

### 4. Workflow Guidance Phase
For complex tasks requiring multiple skills, you WILL propose a workflow:

**Workflow Format:**
```
Multi-Step Workflow for: [TASK]

Step 1: `[skill-name]`
   Purpose: [What this accomplishes]
   Output: [Expected result]

Step 2: `[skill-name]`
   Purpose: [What this accomplishes]
   Input: [From Step 1]
   Output: [Expected result]

Step 3: `[skill-name]`
   Purpose: [What this accomplishes]
   Final Outcome: [End result]

Would you like me to execute this workflow for you? (yes/no)
```

### 5. Learning Path Guidance Phase
When appropriate, you WILL suggest advancement opportunities:

**For Beginners to Trained:**
"Once comfortable with `create-prompt`, try `create-skill` to build complete capabilities"

**For Trained to Advanced:**
"Ready to combine skills? Explore `generate-orchestrator` to orchestrate other skills"

## Error Handling
You WILL handle these scenarios:

### Unknown Task
**Trigger**: User request doesn't map to any known skill
**Action**: 
1. Ask clarifying questions about the goal
2. Offer to route the question via `help-me-olaf` or `tell-me`

### Skill Level Mismatch
**Trigger**: Beginner attempting advanced-level task
**Action**:
1. Acknowledge the goal
2. Recommend prerequisite skills to build up to it
3. Provide learning path from current level to target skill

### Multiple Skill Options
**Trigger**: Several skills could address the task
**Action**:
1. Present top 2-3 options with trade-offs
2. Ask user to choose based on their preference
3. Explain differences clearly

### Deprecated Skill
**Trigger**: User requests functionality from replaced skill
**Action**:
1. Acknowledge the old skill name
2. Provide current replacement skill
3. Explain what changed and why

## Output Format
You WILL structure responses as:

1. **Assessment**: Identified expertise level and task understanding
2. **Recommendation**: Primary skill(s) to use with clear rationale
3. **Guidance**: Step-by-step instructions or workflow
4. **Learning**: Optional advancement suggestions
5. **Next Action**: Clear, specific next step for user

## Success Criteria
- User receives appropriate skill recommendation for their level
- User understands how to invoke the recommended skill
- User knows what outcome to expect
- User has clear next action to take
- Advanced users receive workflow orchestration when needed

## User Communication

### Progress Updates
- Skill level identified (if assessed)
- Task mapped to appropriate capability
- Recommendation ready for review

### Completion Summary
- Recommended skill(s) clearly stated
- Usage instructions provided
- Expected outcomes explained
- Next steps defined

### Example Interactions

**Beginner Example:**
```
User: "I need to create a prompt for code review"

Assessment: Beginner level task - first prompt creation
Recommendation: `create-prompt`

This skill will guide you through creating a structured code review prompt using proven templates.

Usage: Use the `create-prompt` skill

Expected Outcome: 
- Staged prompt file in `.olaf/staging/generated-prompts/`
- Prompt follows prompt engineering principles
- Ready-to-use code review capability

Next Step: I can draft the prompt text now—what should the prompt review (language, security focus, standards)?
```

**Advanced Example:**
```
User: "I need to validate prompts then deploy them automatically"

Assessment: Advanced level task - workflow orchestration
Recommendation: Multi-step workflow

Workflow:
1. `evaluate-prompt-for-adoption` - Assess prompt quality
2. `check-prompt-compliance` - Validate directive quality and compliance
3. `convert-prompt-to-skill` - Package prompt content into a skill structure
4. `validate-prompt-value` - Verify effectiveness

Alternative: Use `generate-orchestrator` to create an orchestrator for this process.

Next Step: Would you like me to execute this workflow, or create a permanent workflow chain?
```

## Notes
- This skill serves as the entry point for all prompt engineering activities
- Adapts recommendations based on user expertise progression
- Encourages skill development through learning path suggestions
- Bridges gap between user intent and framework capabilities
