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
- **expertise_level**: string - User's prompt engineering skill level: beginner/trained/advanced/expert (OPTIONAL - will assess if not provided)

## User Interaction Protocol
You MUST follow the established interaction protocol:
- Use **Act** for skill recommendations and guidance
- Use **Propose-Confirm-Act** when executing complex workflows on user's behalf

## Process

### 1. Skill Level Assessment Phase
If expertise_level not provided, you WILL assess based on task complexity and user's question:
- **Beginner**: Creating first prompts, learning basics, following templates
- **Trained**: Converting/importing existing prompts, organizing collections
- **Advanced**: Building workflows, managing competencies, complex validations
- **Expert**: Framework contributions, architecture changes, system optimization

### 2. Skill Mapping Phase
You WILL identify appropriate skills based on user's level and task:

#### Beginner Level Skills
**Core Capabilities:**
- `create-prompt` - Generate structured prompts from templates
- `share-my-prompts` - Share prompts with team members
- `import-prompt-unchanged` - Import existing prompts without modification

**When to Recommend:**
- User needs to create their first prompt
- User wants to share prompts they've created
- User has prompts from other sources to import as-is

**Example Tasks:**
- "I need to create a prompt for code reviews"
- "How do I share my prompt with the team?"
- "I have a prompt from ChatGPT I want to use"

#### Trained Level Skills
**Core Capabilities:**
- `create-skill` - Build complete skills with prompts and workflows
- `convert-prompt` - Modernize legacy prompts to OLAF standards
- `evaluate-prompt-for-adoption` - Assess prompts for framework integration
- `select-competency-collection` - Choose and manage competency collections

**When to Recommend:**
- User understands prompt basics, ready for skill development
- User has legacy prompts needing modernization
- User needs to evaluate external prompts for adoption
- User wants to organize competencies into collections

**Example Tasks:**
- "I want to create a skill with multiple prompts"
- "I have old prompts that need updating"
- "Should we adopt this prompt from the community?"
- "How do I organize my competencies?"

#### Advanced Level Skills
**Core Capabilities:**
- `generate-workflow` - Create multi-step workflows combining skills
- `convert-skill-to-chain` - Transform skills into executable chains
- `manage-competencies` - Full competency lifecycle management
- `validate-prompt-value` - Deep analysis of prompt effectiveness
- `share-skills-with-team` - Share skills and competencies with team repository

**When to Recommend:**
- User needs to orchestrate multiple skills together
- User wants to create reusable skill chains
- User manages competency packages across teams
- User needs metrics on prompt performance
- User wants to share curated skills with team via git

**Example Tasks:**
- "I need a workflow that validates then deploys prompts"
- "How do I chain multiple skills together?"
- "I manage several competency packages"
- "What's the ROI of this prompt?"
- "I want to share these skills with my team"

#### Expert Level Skills
**Core Capabilities:**
- `condense-olaf-framework` - Optimize framework for performance
- `share-prompt-to-olaf` - Contribute prompts to OLAF core
- `verify-competency-compliance` - Deep framework validation
- `migrate-competency-to-skill` - Architectural refactoring
- `create-competency-package` - Build distributable packages
- `validate-olaf-artifacts` - System-wide validation

**When to Recommend:**
- User contributes to OLAF framework development
- User performs architectural changes
- User needs system-level optimizations
- User creates framework extensions

**Example Tasks:**
- "The framework is loading slowly"
- "I want to contribute this prompt to OLAF core"
- "I need to refactor this competency architecture"
- "How do I validate all framework artifacts?"

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

**For Beginners → Trained:**
"Once comfortable with `create-prompt`, try `create-skill` to build complete capabilities"

**For Trained → Advanced:**
"Ready to combine skills? Explore `generate-workflow` to orchestrate multi-step processes"

**For Advanced → Expert:**
"Consider `share-prompt-to-olaf` to contribute your work to the framework core"

## Error Handling
You WILL handle these scenarios:

### Unknown Task
**Trigger**: User request doesn't map to any known skill
**Action**: 
1. Ask clarifying questions about the goal
2. Suggest browsing available skills with `list-skills`
3. Offer to help refine the requirement

### Skill Level Mismatch
**Trigger**: Beginner attempting expert-level task
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

Usage: `olaf create prompt`

Expected Outcome: 
- Complete prompt in skills/[your-prompt-name]/
- Validation against best practices
- Ready-to-use code review capability

Next Step: Run `olaf create prompt` and I'll guide you through the process.
```

**Advanced Example:**
```
User: "I need to validate prompts then deploy them automatically"

Assessment: Advanced level task - workflow orchestration
Recommendation: Multi-step workflow

Workflow:
1. `evaluate-prompt-for-adoption` - Assess prompt quality
2. `convert-prompt` - Ensure OLAF compliance
3. `deploy-imported-prompts` - Deploy to framework
4. `validate-prompt-value` - Verify effectiveness

Alternative: Use `generate-workflow` to create a reusable chain for this process.

Next Step: Would you like me to execute this workflow, or create a permanent workflow chain?
```

## Notes
- This skill serves as the entry point for all prompt engineering activities
- Adapts recommendations based on user expertise progression
- Encourages skill development through learning path suggestions
- Bridges gap between user intent and framework capabilities
