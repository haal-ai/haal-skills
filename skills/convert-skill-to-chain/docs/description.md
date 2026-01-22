# convert-skill-to-chain

## Overview

The `convert-skill-to-chain` skill is a master coordinator that transforms existing OLAF skills into the master-chain pattern. It orchestrates a multi-step conversion process that analyzes skill structure, detects workflow patterns, and extracts individual tasks into a modular chain architecture.

## Purpose

This skill enables prompt engineers to refactor complex single-prompt skills into maintainable, modular task chains. The master-chain pattern improves skill maintainability, enables task reuse across skills, and provides clearer execution flow with explicit dependencies.

## Key Features

- **Pattern Detection**: Automatically identifies workflow patterns (sequential, cyclic, session-chained, conditional, hybrid)
- **Conversion Evaluation**: Assesses whether conversion is necessary based on complexity scoring
- **Task Extraction**: Breaks down monolithic skills into discrete, reusable task files
- **Common Task Reuse**: Searches for existing common tasks to avoid duplication
- **Master Coordinator Generation**: Creates a new master coordinator prompt for the converted skill
- **Registry Integration**: Updates task registry with newly created tasks

## Usage

Invoke the skill to convert an existing skill to the master-chain pattern:

```
@convert-skill-to-chain
```

The skill will guide you through selecting a skill and execute the conversion workflow automatically.

## Parameters

This skill operates interactively and collects parameters during execution:

| Parameter | Type | Description |
|-----------|------|-------------|
| skill_name | string | Name of skill to convert (collected during Task 1) |
| skill_path | string | Path to skill directory (derived from skill_name) |

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONVERSION WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│ Task 1: Select skill to convert                                 │
│    ↓                                                            │
│ Task 2: Backup original skill prompt                            │
│    ↓                                                            │
│ Task 3: Analyze existing skill structure                        │
│    ↓                                                            │
│ Task 4: Detect workflow pattern                                 │
│    ↓                                                            │
│ Task 5: Evaluate if conversion is necessary ──→ [STOP if NO]    │
│    ↓ (if YES)                                                   │
│ Task 6: Search for reusable common tasks                        │
│    ↓                                                            │
│ Task 7: Identify task boundaries                                │
│    ↓                                                            │
│ Task 8: Extract individual tasks                                │
│    ↓                                                            │
│ Task 9: Create master coordinator prompt                        │
│    ↓                                                            │
│ Task 10: Update task registry with new tasks                    │
│    ↓                                                            │
│ Task 11: Generate conversion summary                            │
└─────────────────────────────────────────────────────────────────┘
```

## Output

Upon successful conversion, the skill produces:

- **Backup File**: Original skill.md preserved before modification
- **Task Files**: Individual task prompts in the skill's `tasks/` directory
- **Master Coordinator**: New skill.md with master-chain structure
- **Registry Updates**: Task registry updated with new task entries
- **Conversion Summary**: Report of changes made and new structure

## Examples

### Example 1: Converting a Sequential Workflow Skill

```
User: @convert-skill-to-chain

Agent: [Executes Task 1 - Select skill]
Available skills for conversion:
1. analyze-code-quality
2. generate-documentation
3. review-pull-request

Please select a skill to convert:

User: analyze-code-quality

Agent: [Executes Tasks 2-11]
...
Conversion Complete!
- Pattern detected: sequential
- Tasks extracted: 5
- Common tasks reused: 2
- Master coordinator created: analyze-code-quality/skill.md
```

### Example 2: Skill Not Requiring Conversion

```
User: @convert-skill-to-chain

Agent: [Executes Tasks 1-5]
Analysis Complete - No Conversion Needed
============================================
Skill: simple-formatter
Complexity: 2/10

This skill remains as a single-prompt implementation.
No further action required.
```

## Error Handling

| Error Condition | Handling |
|----------------|----------|
| Skill directory not found | Reports error and requests valid skill name |
| Missing skill.md | Reports missing file and stops execution |
| Backup failure | Stops chain to prevent data loss |
| Task extraction failure | Reports specific error and stops chain |

## Related Skills

- `create-skill` - Create new skills from scratch
- `generate-orchestrator` - Create orchestrator skills combining multiple skills
- `analyze-skill-structure` - Analyze skill structure without conversion
