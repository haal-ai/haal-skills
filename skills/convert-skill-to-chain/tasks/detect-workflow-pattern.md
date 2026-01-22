---
task_id: "detect-workflow-pattern"
task_name: "Detect Workflow Pattern"
dependencies: ["skill_structure", "skill_prompt_file"]
---

# Task: Detect Workflow Pattern

## Input Context

**Required Context Variables**:
- `skill_structure`: Analysis of current skill structure
- `skill_prompt_file`: Path to skill prompt file to analyze
- `skill_name`: Name of skill being converted

**Required Files**:
- Source skill prompt file at `skill_prompt_file`
- Pattern reference: `skills/convert-skill-to-chain/kb/workflow-patterns.md`

**Required Tools**: None

## Task Instructions

### 1. Load Pattern Reference
Read the workflow patterns KB:
```
skills/convert-skill-to-chain/kb/workflow-patterns.md
```

### 2. Analyze Skill Content
Read the skill prompt file and identify pattern indicators:

**Loop/Cycle Indicators**:
- Keywords: "repeat", "until", "while", "iterate", "cycle", "again", "multiple times"
- Numbered rounds/iterations (e.g., "round 1, round 2")
- Exit conditions (e.g., "when user says stop", "until goal achieved")
- Progress tracking across iterations

**Session-Chain Indicators**:
- Keywords: "next session", "handoff", "continue in", "stage", "phase"
- Multiple sub-skill references
- Artifact generation for continuation
- User instruction to start new session

**Conditional Branch Indicators**:
- Keywords: "if", "based on", "depending on", "when", "choose"
- Multiple execution paths
- Platform/environment-specific logic
- Optional steps based on conditions

**Sequential Indicators** (default):
- Single linear execution path
- No loops or branches
- One-time execution of each step

### 3. Classify Primary Pattern
Based on the strongest indicators, classify as:
- `sequential`: No loops, branches, or sessions
- `cyclic`: Contains repeating task sets
- `session-chained`: Multi-session workflow with handoffs
- `conditional`: Branching logic without loops
- `hybrid`: Combination of multiple patterns

**Hybrid Pattern Detection**:
If multiple pattern types detected, classify as hybrid and identify component patterns:
- Example: `cyclic + conditional` = Loop with conditional branches inside
- Example: `sequential + conditional` = Linear flow with optional branches
- Example: `session-chained + cyclic` = Multi-session with iterative stages

### 4. Extract Pattern Metadata

For **Cyclic** patterns:
- Identify loop boundary (which tasks/steps repeat)
- Detect exit conditions (user input, condition check, iteration count)
- Estimate max_iterations for safety

For **Session-Chained** patterns:
- Count number of sessions/stages
- Identify handoff points
- List required artifacts for continuation

For **Conditional** patterns:
- Identify decision points
- List conditional branches
- Map convergence points

For **Hybrid** patterns:
- Document each component pattern
- Identify pattern interaction points
- Prioritize dominant pattern

### 5. Store Detection Results

**Context Variables to Create**:
```
detected_pattern: [sequential|cyclic|session-chained|conditional|hybrid]
pattern_confidence: [high|medium|low]
pattern_indicators: [list of detected keywords/structures]

# For cyclic patterns:
loop_boundary: [description of what repeats]
exit_conditions: [list of exit conditions]
estimated_max_iterations: [number]

# For session-chained patterns:
session_count: [number]
handoff_points: [list of session boundaries]
required_artifacts: [list of artifacts]

# For conditional patterns:
decision_points: [list of decision tasks]
branch_paths: [list of branches]
convergence_points: [list of merge points]

# For hybrid patterns:
component_patterns: [list of pattern types]
dominant_pattern: [primary pattern type]
pattern_interactions: [description of how patterns combine]
```

## Output Requirements

**Context Variables Created**:
- `detected_pattern`: Primary pattern classification
- `pattern_confidence`: Confidence level in detection
- `pattern_indicators`: Supporting evidence
- Pattern-specific metadata (see above)

**Files Created**: None

**Display to User**:
```
Pattern Detection Results
===========================
Skill: {{skill_name}}
Detected Pattern: {{detected_pattern}}
Confidence: {{pattern_confidence}}

Key Indicators:
{{pattern_indicators}}

Pattern Details:
{{pattern_metadata}}
```

## Examples

### Example 1: Sequential Pattern
```
Skill: search-and-learn
Detected: sequential
Indicators:
- Single linear execution
- No loops or branches
- Tasks execute once each
```

### Example 2: Cyclic Pattern
```
Skill: challenge-me
Detected: cyclic
Indicators:
- "repeat until mastery achieved"
- "each round presents new challenge"
- Exit: user decision OR mastery threshold
Loop Boundary: Tasks 2-5 (present → evaluate → feedback → check)
Max Iterations: 20
```

### Example 3: Hybrid Pattern
```
Skill: adaptive-learning
Detected: hybrid (cyclic + conditional)
Component Patterns:
- Cyclic: Learning rounds repeat
- Conditional: Different content based on performance
Dominant: cyclic
Interactions: Conditional branches inside loop iterations
```
