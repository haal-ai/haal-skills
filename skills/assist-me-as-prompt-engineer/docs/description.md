# assist-me-as-prompt-engineer

## Overview

The `assist-me-as-prompt-engineer` skill serves as an intelligent guide for prompt engineers, providing skill recommendations and workflow guidance based on the user's expertise level and task requirements. It acts as the entry point for all prompt engineering activities within the OLAF framework.

## Purpose

This skill bridges the gap between user intent and framework capabilities by assessing expertise levels, mapping tasks to appropriate skills, and providing clear, actionable guidance. It helps users navigate the prompt engineering skill ecosystem efficiently.

## Key Features

- **Expertise Assessment**: Automatically determines user skill level (beginner, trained, advanced)
- **Skill Mapping**: Matches user tasks to appropriate skills based on expertise and requirements
- **Workflow Orchestration**: Proposes multi-step workflows for complex tasks
- **Learning Path Guidance**: Suggests advancement opportunities to build expertise
- **Interactive Recommendations**: Provides clear next steps and usage instructions

## Usage

Invoke the skill with a task description:

```
@assist-me-as-prompt-engineer I need to create a prompt for code reviews
```

Or invoke without parameters for interactive guidance:

```
@assist-me-as-prompt-engineer
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| task_description | string | Yes | What the user wants to accomplish |
| expertise_level | string | No | User's skill level: beginner/trained/advanced (assessed if not provided) |

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASSISTANCE WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│ 1. Skill Level Assessment                                       │
│    - Assess from task complexity if not provided                │
│    - Categorize: beginner / trained / advanced                  │
│    ↓                                                            │
│ 2. Skill Mapping                                                │
│    - Match task to appropriate skills                           │
│    - Consider expertise level constraints                       │
│    ↓                                                            │
│ 3. Recommendation                                               │
│    - Primary skill with rationale                               │
│    - Supporting skills if applicable                            │
│    ↓                                                            │
│ 4. Workflow Guidance (if complex)                               │
│    - Multi-step workflow proposal                               │
│    - Execution offer                                            │
│    ↓                                                            │
│ 5. Learning Path (optional)                                     │
│    - Advancement suggestions                                    │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The skill provides structured recommendations:

- **Assessment**: Identified expertise level and task understanding
- **Recommendation**: Primary skill(s) with clear rationale
- **Guidance**: Step-by-step instructions or workflow
- **Learning**: Optional advancement suggestions
- **Next Action**: Clear, specific next step

## Skill Recommendations by Level

### Beginner Level
| Skill | Purpose |
|-------|---------|
| `create-prompt` | Draft prompts and stage them |
| `check-prompt-compliance` | Verify prompt compliance |

### Trained Level
| Skill | Purpose |
|-------|---------|
| `create-skill` | Build complete skills with workflows |
| `convert-prompt-to-skill` | Convert prompts to skill structure |
| `evaluate-prompt-for-adoption` | Assess prompts for integration |
| `create-skill-description` | Generate skill documentation |

### Advanced Level
| Skill | Purpose |
|-------|---------|
| `generate-orchestrator` | Create orchestrator skills |
| `convert-skill-to-chain` | Transform skills into chains |
| `validate-prompt-value` | Deep prompt effectiveness analysis |

## Examples

### Example 1: Beginner Task

```
User: I need to create a prompt for code review

Assessment: Beginner level task - first prompt creation
Recommendation: `create-prompt`

This skill will guide you through creating a structured code review 
prompt using proven templates.

Expected Outcome:
- Staged prompt file in `.olaf/staging/generated-prompts/`
- Prompt follows prompt engineering principles

Next Step: What should the prompt review (language, security focus, standards)?
```

### Example 2: Advanced Multi-Step Task

```
User: I need to validate prompts then deploy them automatically

Assessment: Advanced level task - workflow orchestration
Recommendation: Multi-step workflow

Workflow:
1. `evaluate-prompt-for-adoption` - Assess prompt quality
2. `check-prompt-compliance` - Validate directive quality
3. `convert-prompt-to-skill` - Package into skill structure
4. `validate-prompt-value` - Verify effectiveness

Alternative: Use `generate-orchestrator` to create a permanent workflow.

Next Step: Execute this workflow, or create a permanent chain?
```

## Error Handling

| Scenario | Handling |
|----------|----------|
| Unknown task | Ask clarifying questions, offer `help-me-olaf` or `tell-me` |
| Skill level mismatch | Acknowledge goal, recommend prerequisites, provide learning path |
| Multiple skill options | Present top 2-3 options with trade-offs |
| Deprecated skill | Acknowledge old name, provide replacement, explain changes |

## Related Skills

- `help-me-olaf` - General OLAF assistance
- `tell-me` - Information and explanations
- `create-skill` - Build new skills
- `generate-orchestrator` - Create skill orchestrators
