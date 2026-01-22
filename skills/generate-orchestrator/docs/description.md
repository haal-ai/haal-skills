# generate-orchestrator

## Overview

The `generate-orchestrator` skill generates orchestrator skills that coordinate and sequence other skills into automated workflows. It creates complete skill packages under the skills directory with proper structure and documentation.

## Purpose

This skill helps developers create meta-skills that chain multiple existing skills together into cohesive workflows. Orchestrators enable complex multi-step processes to be executed with proper sequencing, review gates, and error handling.

## Key Features

- **Skill Chaining**: Orchestrates multiple skills in a defined sequence
- **Review Gates**: Supports named checkpoints requiring user confirmation
- **Failure Handling**: Configurable stop-on-failure behavior with recovery guidance
- **Context Passing**: Defines how output from one step feeds into the next
- **Complete Package Generation**: Creates skill.md, description.md, and tutorial.md

## Usage

Invoke the skill with the following parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `orchestrator_name` | string | Yes | - | Name for the orchestrator (kebab-case, max 4 words) |
| `description` | string | Yes | - | Brief description of orchestrator purpose |
| `skills_to_orchestrate` | array | Yes | - | Ordered list of skill names to orchestrate |
| `review_gates` | array | No | - | Named checkpoints requiring user confirmation |
| `stop_on_failure` | boolean | No | true | Whether to stop when a step fails |
| `mode` | string | No | interactive | Generation mode: interactive or specification |

## Process Flow

1. **Validate Inputs**: Collects and validates required parameters (interactive) or validates specification (specification mode)
2. **Load Templates**: Reads orchestrator skill template and prompting principles
3. **Gather Details**: Asks orchestrator-specific questions until all parameters are complete
4. **Generate Package**: Creates the orchestrator skill package under skills/
5. **Validate and Save**: Verifies all required sections exist and saves files

## Output

The skill generates a complete orchestrator package:

```
skills/[orchestrator_name]/
├── skill.md           # Main orchestrator definition
├── docs/
│   ├── description.md # Skill overview and usage
│   └── tutorial.md    # Step-by-step guide
```

The generated orchestrator includes:
- Explicit list of skills to orchestrate
- Execution order and review gates
- Stop-on-failure behavior and recovery guidance
- Context/output passing between steps

## Examples

**Basic orchestrator**:
```
Generate an orchestrator called "code-review-workflow" 
that orchestrates: review-code, review-diff, git-add-commit
```

**With review gates**:
```
Generate an orchestrator "release-pipeline" 
orchestrating: review-code, augment-code-unit-test, generate-changelog-entry
with review gates after review-code and before changelog generation
```

**From specification**:
```
Generate an orchestrator from specification mode
using the workflow spec in ./specs/my-workflow.md
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Invalid input | Provides specific error message |
| Template not found | Lists available templates |
| Invalid specification | Provides validation errors |
| File already exists | Prompts for confirmation before overwriting |
| Empty skills list | Requires at least one skill to orchestrate |

## Related Skills

- `create-skill` - For creating individual skills
- `convert-skill-to-chain` - For converting skills to chain format
- `esdi-chain` - For ESDI-based workflow chains
