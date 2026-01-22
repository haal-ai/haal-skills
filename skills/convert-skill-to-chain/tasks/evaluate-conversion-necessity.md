---
task_id: "evaluate-conversion-necessity"
task_name: "Evaluate if Conversion to Chain is Necessary"
dependencies: ["skill_structure", "detected_pattern"]
---

# Task: Evaluate Conversion Necessity

## Input Context

**Required Context Variables**:
- `skill_structure`: Analysis of current skill structure
- `detected_pattern`: Detected workflow pattern
- `pattern_confidence`: Confidence level in pattern detection
- `skill_content`: Full skill prompt content
- `skill_name`: Name of skill being analyzed

**Required Files**: None
**Required Tools**: None

## Task Instructions

### Purpose
Determine if the skill is complex enough to benefit from conversion to master-chain pattern, or if it's simple enough to remain as a single prompt.

### 1. Evaluate Complexity Indicators

**Simple Skills (NO CONVERSION NEEDED)**:
- **Task Count**: 1-3 distinct logical steps
- **No Loops**: Single linear execution, no iterations
- **No Sub-Prompts**: Doesn't call other skills or external prompts
- **No Multi-Phase**: Single execution session
- **No Complex Branching**: At most 1-2 simple conditional checks
- **Low State Management**: Minimal context variables (< 5)
- **Single Purpose**: Does one clear thing without orchestration

**Complex Skills (CONVERSION BENEFICIAL)**:
- **High Task Count**: 4+ distinct logical steps
- **Loops/Iterations**: Cyclic patterns requiring repeated execution
- **Sub-Prompt Calls**: Invokes other skills or external prompts
- **Multi-Phase**: Requires multiple sessions or handoffs
- **Complex Branching**: Multiple decision trees or conditional paths
- **Heavy State Management**: Many context variables (5+)
- **Orchestration**: Coordinates multiple operations or tools

### 2. Apply Decision Criteria

**SKIP CONVERSION if ALL of the following are true**:
1. Detected pattern is `sequential` with HIGH confidence
2. Skill structure shows `complexity: low` or `complexity: medium` with section_count <= 3
3. No external tool invocations beyond simple file reads
4. No loops or iteration keywords found
5. No sub-skill calls or prompt chaining
6. Workflow completes in single session

**PROCEED WITH CONVERSION if ANY of the following are true**:
1. Detected pattern is `cyclic`, `session-chained`, or `hybrid`
2. Skill structure shows `complexity: high` OR section_count >= 4
3. Multiple external tools or scripts called
4. Contains loops, iterations, or recursive elements
5. Calls other skills or sub-prompts
6. Multi-session or multi-phase workflow
7. Complex state management with many variables

### 3. Analyze Current Skill Content

Read through skill content and count:
- **Distinct instruction blocks**: Look for numbered steps, major sections
- **Decision points**: Count "if", "based on", "when", "choose" branches
- **External calls**: Scripts, tools, other skills referenced
- **Variables tracked**: Count unique context variables or state elements
- **Loop keywords**: "repeat", "iterate", "until", "again", "cycle"

### 4. Make Decision

Based on analysis, set:
```
conversion_necessary: [true|false]
conversion_reason: [detailed explanation]
complexity_score: [1-10 scale]
```

**Complexity Scoring Guide**:
- **1-3**: Simple - single purpose, linear execution, < 3 steps
- **4-6**: Medium - multiple steps but linear, basic state
- **7-10**: Complex - loops, branches, multi-phase, orchestration

### 5. Display Results

Show clear decision to user:

**If conversion_necessary = FALSE**:
```
CONVERSION NOT NECESSARY
================================
Skill: {{skill_name}}
Complexity Score: {{complexity_score}}/10

REASON:
{{conversion_reason}}

RECOMMENDATION:
This skill is simple enough to remain as a single prompt file.
No conversion to master-chain pattern needed.

Keeping it simple will:
✓ Reduce cognitive overhead
✓ Faster execution (no chain orchestration)
✓ Easier to understand and maintain
✓ Lower token consumption

STOPPING CONVERSION PROCESS.
```

**If conversion_necessary = TRUE**:
```
✓ CONVERSION BENEFICIAL
=======================
Skill: {{skill_name}}
Complexity Score: {{complexity_score}}/10

REASON:
{{conversion_reason}}

BENEFITS OF CONVERSION:
✓ Better task isolation and reusability
✓ Clearer separation of concerns
✓ Easier to test individual components
✓ Improved maintainability

PROCEEDING WITH CONVERSION.
```

## Output Requirements

**Context Variables Created**:
- `conversion_necessary`: Boolean (true/false)
- `conversion_reason`: Detailed explanation of decision
- `complexity_score`: Numeric score 1-10
- `conversion_decision`: Display message shown to user

**Conditional Flow**:
- If `conversion_necessary = false`: STOP chain execution, skip all remaining tasks
- If `conversion_necessary = true`: Continue to next task

**Files Created**: None

## Examples

### Example 1: Simple Skill - No Conversion
```
Skill: hello-world
Pattern: sequential (high confidence)
Analysis:
- Steps: 2 (greet user, show message)
- Loops: None
- External Tools: None
- Branches: None
- State: 1 variable (user_name)

Decision: conversion_necessary = FALSE
Complexity Score: 2/10
Reason: Simple linear execution with minimal state. 
        Converting to chain would add unnecessary overhead.
```

### Example 2: Complex Skill - Conversion Needed
```
Skill: adaptive-learning
Pattern: hybrid (cyclic + conditional)
Analysis:
- Steps: 8 distinct phases
- Loops: Yes (learning rounds repeat)
- External Tools: 3 (quiz-generator, evaluator, progress-tracker)
- Branches: 4 decision points
- State: 12 context variables

Decision: conversion_necessary = TRUE
Complexity Score: 9/10
Reason: Complex hybrid pattern with loops, multiple tools, 
        heavy state management. Chain pattern will improve 
        modularity and maintainability.
```

### Example 3: Borderline - Conversion Beneficial
```
Skill: code-reviewer
Pattern: sequential (medium confidence)
Analysis:
- Steps: 5 phases (read, analyze, check, report, cleanup)
- Loops: None, but potential for future iteration
- External Tools: 2 (linter, formatter)
- Branches: 2 simple checks
- State: 6 context variables

Decision: conversion_necessary = TRUE
Complexity Score: 6/10
Reason: While currently sequential, the 5 distinct phases 
        with multiple tools benefit from task isolation.
        Future enhancement may add iteration capability.
```
