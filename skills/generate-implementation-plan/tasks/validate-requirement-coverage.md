---
name: validate-requirement-coverage
description: "Task 4 - Validate all EARS requirements are addressed in task breakdown"
task_id: 4
protocol: Propose-Act
---

# Task 4: Validate Requirement Coverage

## Objective

Verify that all EARS requirements from Phase 2 specification are adequately addressed in the implementation task breakdown, and generate a requirement traceability matrix.

## Context Variables

**Required**:
- `requirements_map`: Output from Task 1 (EARS requirements)
- `task_breakdown`: Output from Task 3 (complete task structure)
- `design_layers`: Output from Task 1 (layer information)

**Outputs**:
- `traceability_matrix`: Mapping of requirements to tasks
- `coverage_report`: Summary of requirement coverage
- `gap_analysis`: List of unaddressed or partially addressed requirements

## Execution Steps

### Step 1: Build Requirement-to-Task Mapping

```
For each requirement in requirements_map:
  1. Identify which tasks address this requirement
  2. Match based on:
     - Task description mentions requirement keywords
     - Task targets component that addresses requirement
     - Task in layer that maps to requirement
  
  3. Classify coverage:
     - ✅ Fully Covered: Requirement has dedicated task(s)
     - ⚠️ Partially Covered: Requirement addressed but not thoroughly
     - ❌ Not Covered: No tasks address this requirement
```

**Matching Strategy**:
```python
# Example logic
for requirement in requirements:
    requirement_keywords = extract_keywords(requirement.text)
    covering_tasks = []
    
    for task in task_breakdown:
        # Check if task addresses requirement
        if (task.layer_id in requirement.addressed_by_layers and
            any(keyword in task.description for keyword in requirement_keywords)):
            covering_tasks.append(task.id)
    
    coverage_status = determine_coverage(requirement, covering_tasks)
```

### Step 2: Analyze Coverage by Requirement Type

```
Group requirements by type and calculate coverage:

Functional Requirements:
  - Total: {functional_count}
  - Covered: {functional_covered}
  - Coverage %: {functional_percentage}%

Performance Requirements:
  - Total: {performance_count}
  - Covered: {performance_covered}
  - Coverage %: {performance_percentage}%

Security Requirements:
  - Total: {security_count}
  - Covered: {security_covered}
  - Coverage %: {security_percentage}%

Overall Coverage: {total_covered}/{total_requirements} ({percentage}%)
```

### Step 3: Generate Traceability Matrix

Create comprehensive mapping table:

```markdown
# Requirement Traceability Matrix

## Fully Covered Requirements (✅)

| Req ID | Type | Requirement | Layer | Addressing Tasks | Validation |
|--------|------|-------------|-------|------------------|------------|
| REQ-F-001 | Functional | The system SHALL scan repository directory tree | Layer 1 | 1.1, 1.2, 1.4 | Task 1.4 |
| REQ-F-002 | Functional | The system SHALL validate metadata against schema | Layer 2 | 2.1, 2.3 | Task 2.3 |
| REQ-P-001 | Performance | Process 10k files in < 30s | Layer 1 | 1.1, 1.3 | Task 1.4 |
| REQ-S-001 | Security | Use secure file access permissions | Layer 1 | 1.1 | Task 1.4 |

## Partially Covered Requirements (⚠️)

| Req ID | Type | Requirement | Layer | Addressing Tasks | Gap |
|--------|------|-------------|-------|------------------|-----|
| REQ-U-001 | Usability | Provide progress feedback | Layer 3 | 3.1 | No validation task |
| REQ-R-001 | Reliability | Handle network failures gracefully | Layer 2 | 2.2 | Missing retry logic |

## Not Covered Requirements (❌)

| Req ID | Type | Requirement | Recommended Action |
|--------|------|-------------|-------------------|
| REQ-F-015 | Functional | Support incremental scanning | Add task in Phase 1 |
| REQ-S-003 | Security | Encrypt sensitive metadata | Add task in Phase 2 |

---

## Coverage Statistics

**Overall**: {covered}/{total} requirements ({percentage}%)
**By Type**:
- Functional: {func_covered}/{func_total} ({func_pct}%)
- Performance: {perf_covered}/{perf_total} ({perf_pct}%)
- Security: {sec_covered}/{sec_total} ({sec_pct}%)
- Usability: {use_covered}/{use_total} ({use_pct}%)
- Reliability: {rel_covered}/{rel_total} ({rel_pct}%)

**By Priority**:
- High: {high_covered}/{high_total} ({high_pct}%)
- Medium: {med_covered}/{med_total} ({med_pct}%)
- Low: {low_covered}/{low_total} ({low_pct}%)
```

### Step 4: Identify Gaps and Recommend Actions

```
For each uncovered or partially covered requirement:

1. Analyze why it's not covered:
   - Missing component in design?
   - Overlooked in task breakdown?
   - Cross-cutting concern not addressed?

2. Recommend specific actions:
   - Add new task in Phase X
   - Expand scope of existing Task X.Y
   - Create integration test for validation
   - Add cross-layer coordination task

3. Estimate impact:
   - Additional tasks needed: {count}
   - Estimated time: {minutes} min
   - Phase affected: Phase {N}
```

**Example Gap Analysis**:
```
Gap: REQ-F-015 "Support incremental scanning"

Analysis:
  - Design has FileScanner component (Layer 1)
  - Task 1.1 implements full scanning only
  - No task for incremental scanning capability

Recommendation:
  - Add Task 1.5: "Implement Incremental Scanning"
  - Depends on: Task 1.1
  - Estimated time: 30 minutes
  - Outputs: incremental_scanner.py

Impact: +1 task in Phase 1, extends timeline by 30 min
```

### Step 5: Calculate Coverage Threshold

```
Determine if coverage meets acceptable threshold:

Coverage Level Classification:
  - Excellent: ≥ 95% coverage
  - Good: 90-94% coverage
  - Acceptable: 85-89% coverage
  - Poor: 80-84% coverage
  - Inadequate: < 80% coverage

Critical Requirements (High Priority):
  - Must have 100% coverage
  - Any gaps are blocking issues

Recommendation:
  - Excellent/Good: Proceed to implementation
  - Acceptable: Consider adding gap tasks
  - Poor/Inadequate: Revise task breakdown
```

### Step 6: Propose to User

**CRITICAL**: Ask for user approval before proceeding

```
Present to user:

📊 Requirement Coverage Analysis

Overall Coverage: {total_covered}/{total_requirements} ({percentage}%)
Coverage Level: {level} (Excellent/Good/Acceptable/Poor/Inadequate)

✅ Fully Covered: {fully_covered_count} requirements
⚠️ Partially Covered: {partially_covered_count} requirements  
❌ Not Covered: {not_covered_count} requirements

Critical Issues:
  {List any high-priority requirements not covered}

Recommendations:
  {If coverage < 95%:}
  - Add {recommended_task_count} tasks to address gaps
  - Focus on: {gap_areas}
  - Estimated additional time: {extra_minutes} min

  {If coverage >= 95%:}
  - Coverage is excellent, proceed to implementation

[Show detailed traceability matrix]

Does this coverage meet your requirements?
Options:
  1. Approve and proceed (coverage acceptable)
  2. Add recommended tasks to address gaps
  3. Adjust requirements (de-prioritize some items)
```

### Step 7: User Decision Gate

Handle user response:

**Option 1 - Approve**:
```
User approves coverage → Save traceability_matrix, proceed to Task 4
```

**Option 2 - Add Gap Tasks**:
```
1. Generate additional tasks for uncovered requirements
2. Insert into appropriate phases
3. Update task_breakdown
4. Recalculate coverage
5. Re-propose to user
```

**Option 3 - Adjust Requirements**:
```
1. User marks some requirements as "deferred" or "out-of-scope"
2. Update requirements_map with new status
3. Recalculate coverage excluding deferred items
4. Re-propose to user
```

## Success Criteria

✅ Traceability matrix generated for all requirements
✅ Coverage calculated per requirement type and priority
✅ Gaps identified with specific recommendations
✅ Coverage threshold evaluated (≥85% recommended)
✅ High-priority requirements 100% covered
✅ User approves coverage level

## Error Handling

**If requirements_map missing**:
```
Error: Requirements map not available

Task 0 must complete successfully before validation.
Requirements are extracted from specification.md in Task 0.
```

**If task_breakdown incomplete**:
```
Error: Task breakdown not available or invalid

Task 2 must complete successfully before validation.
Ensure all phases and tasks are defined.
```

**If coverage critically low (<80%)**:
```
Warning: Requirement coverage is critically low ({percentage}%)

This indicates significant gaps between specification and implementation plan.

Recommended actions:
1. Review design.md - does it address all requirements?
2. Review task breakdown - are tasks comprehensive?
3. Consider additional phases or components

Cannot proceed until coverage improves to ≥80%.
```

## Output

Returns to coordinator:

```json
{
  "status": "success",
  "coverage": {
    "total_requirements": 47,
    "fully_covered": 43,
    "partially_covered": 2,
    "not_covered": 2,
    "coverage_percentage": 91.5,
    "level": "good"
  },
  "by_type": {
    "functional": {"total": 28, "covered": 27, "percentage": 96.4},
    "performance": {"total": 8, "covered": 7, "percentage": 87.5},
    "security": {"total": 6, "covered": 5, "percentage": 83.3},
    "usability": {"total": 3, "covered": 2, "percentage": 66.7},
    "reliability": {"total": 2, "covered": 2, "percentage": 100.0}
  },
  "gaps": [
    {
      "req_id": "REQ-F-015",
      "priority": "medium",
      "recommended_action": "Add Task 1.5: Implement Incremental Scanning"
    },
    {
      "req_id": "REQ-S-003",
      "priority": "high",
      "recommended_action": "Add Task 2.4: Implement Metadata Encryption"
    }
  ],
  "user_decision": "approved"
}
```

## Next Task

Proceed to Task 4: Generate Execution Steps (with requirement references in task descriptions)
