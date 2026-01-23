---
task_id: "update-trajectory"
task_name: "Update Trajectory Documentation"
dependencies: ["cycle_counter", "challenges_list", "insights_list", "citations_list", "trajectory"]
---

# Task: Update Trajectory Documentation

## Input Context
**Required Context Variables**: 
- `cycle_counter`: Current cycle number
- `challenges_list`: List of all challenges presented
- `insights_list`: List of all insights generated
- `citations_list`: List of all sources consulted
- `trajectory`: Current trajectory structure

**Required Files**: None
**Required Tools**: None

## Task Instructions

### 1. Extract Cycle Summary
From latest cycle:
- Key challenges presented
- User responses to challenges
- Main insights generated
- Sources consulted
- Significant shifts in thinking

### 2. Update Trajectory
Append to `trajectory`:
```
Cycle <cycle_counter>:
- Challenges: <key challenges>
- User Response: <summary>
- Insights: <key insights>
- Sources: <sources consulted>
- Evolution: <shifts in thinking>
```

### 3. Identify Milestones
Check if this cycle represents:
- Major breakthrough
- Significant clarification
- Direction change
- Critical discovery

If yes, mark as milestone in `trajectory`

### 4. Check for Stagnation
If last 2 cycles show no meaningful evolution:
- Flag stagnation risk
- Prepare to introduce new perspectives in next cycle

## Output Requirements

**Context Variables Updated**:
- `trajectory`: Updated with cycle summary
- `milestone_markers`: List of significant milestones (if any)
- `stagnation_risk`: Boolean flag

**Files Created**: None
