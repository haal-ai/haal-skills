# Tutorial: Generate Implementation Plan

## Overview
This tutorial guides you through generating a detailed implementation task plan from your specification and design documents using the 7-task workflow with user approval gates.

## Prerequisites
- Completed EARS specification (from transform-raw-spec)
- Completed system design (from generate-design)
- Understanding of task-based implementation
- Write access for output directory

## Estimated Time
1-2 hours

## Steps

### Step 1: Prepare Your Input Documents
Ensure both documents are ready:
```
specification_file: ./output/specification.md
design_file: ./output/design.md
```

**Expected Result**: Both documents accessible and complete.

### Step 2: Invoke the Skill
Start the implementation plan generation:
```
generate implementation plan
```

**Expected Result**: Skill begins and prompts for parameters.

### Step 3: Provide Input Parameters
Specify required parameters:
```
specification_file: ./output/specification.md
design_file: ./output/design.md
output_file: ./output/IMPLEMENTATION-TASK-PLAN.md
```

**Expected Result**: Parameters validated and Task 1 begins.

### Step 4: Review Task 1 - Requirements Extraction
The skill extracts and maps requirements:
```
Extracted:
- Skill name: repo-scanner
- Requirements: 47 total
  - Functional: 35
  - Performance: 8
  - Security: 4
- Layers: 4
- Components: 12
```

**Expected Result**: Requirements and design elements extracted.

### Step 5: Approve Layer Mapping
Review the proposed mapping:
```
Layer 1: Data Collection
  Components: FileScanner, MetadataExtractor
  Requirements: REQ-F-001, REQ-F-002, REQ-F-003

Layer 2: Validation
  Components: SchemaValidator, QualityChecker
  Requirements: REQ-F-010, REQ-P-001
```

**Expected Result**: Approve or request adjustments.

### Step 6: Review Task 2 - Task Zero (Optional)
If bootstrap mode enabled:
```
Task 0.0: Extract Task Contexts
  Objective: Generate condensed context files
  Output: tasks/contexts/task-{N}-context.md
```

**Expected Result**: Task 0.0 specification created (if enabled).

### Step 7: Review Task 3 - Task Breakdown
The skill creates phased task structure:
```
Phase 0: Setup (3 tasks)
  - Task 0.0: Extract Task Contexts
  - Task 0.1: Create Directory Structure
  - Task 0.2: Create Coordinator

Phase 1: Data Collection (4 tasks)
  - Task 1.1: Implement FileScanner
  - Task 1.2: Implement MetadataExtractor
  - Task 1.3: Create Integration Tests
  - Task 1.4: Validate Outputs

Phase 2: Validation (3 tasks)
  ...
```

**Expected Result**: Complete task breakdown with dependencies.

### Step 8: Review Task 4 - Requirement Coverage
The skill validates traceability:
```
# Requirement Traceability Matrix

| Req ID | Requirement | Layer | Tasks | Status |
|--------|-------------|-------|-------|--------|
| REQ-F-001 | Scan repository | Layer 1 | 1.1, 1.2 | ✅ Covered |
| REQ-F-002 | Validate metadata | Layer 2 | 2.1 | ✅ Covered |
| REQ-S-001 | Secure access | Layer 1 | 1.1 | ⚠️ Partial |

Coverage: 45/47 requirements (95.7%)
Unaddressed: REQ-F-015, REQ-S-003
```

**Expected Result**: Review coverage and address gaps if needed.

### Step 9: Review Task 5 - Execution Steps
The skill generates execution information:
```
Task 1.1: Implement FileScanner
  Dependencies: Task 0.0, 0.1, 0.2
  Context: skill_path=${skill_path}, component=FileScanner
  Requirements: REQ-F-001
```

**Expected Result**: Execution steps defined for all tasks.

### Step 10: Review Task 6 - Bootstrap Integration (Optional)
If bootstrap mode enabled:
```
# Execute Complete Implementation Plan
Bootstrap command ready for execution
```

**Expected Result**: Bootstrap instructions generated (if enabled).

### Step 11: Review Task 7 - Final Document
The skill generates IMPLEMENTATION-TASK-PLAN.md:
```
Creating final document with:
- Overview and strategy
- Directory structure
- All phases and tasks
- Traceability matrix
- Execution instructions
```

**Expected Result**: Complete implementation plan created.

### Step 12: Verify Output
Review the generated plan:
```markdown
# repo-scanner Implementation Task Plan

## Overview
## Output Directory Structure
## Execution Strategy
## PHASE 0: Setup
## PHASE 1: Data Collection
## PHASE 2: Validation
...
## Requirement Traceability Matrix
## Bootstrap Execution
```

**Expected Result**: Comprehensive, executable implementation plan.

## Expected Outcomes

### Successful Completion
- Complete IMPLEMENTATION-TASK-PLAN.md
- All requirements traced to tasks
- Logical task sequencing
- Ready for execution

### Plan Contents
| Section | Description |
|---------|-------------|
| Overview | High-level implementation approach |
| Directory Structure | Expected output organization |
| Phases | Grouped implementation tasks |
| Traceability | Requirement-to-task mapping |
| Execution | How to run the plan |

### Validation Checklist
- [ ] All EARS requirements extracted
- [ ] Traceability matrix generated
- [ ] Coverage >95% achieved
- [ ] All layers mapped to phases
- [ ] Dependencies properly sequenced
- [ ] Ready for execution

## Troubleshooting

### Common Issues

**Issue**: "Specification file not found"
**Solution**: Verify path to specification.md is correct

**Issue**: "Design file not found"
**Solution**: Verify path to design.md is correct

**Issue**: "Low requirement coverage"
**Solution**: Add tasks to address unaddressed requirements

**Issue**: "Dependency conflict"
**Solution**: Review task sequencing and adjust dependencies

### Best Practices

1. **Verify inputs**: Ensure specification and design are complete
2. **Review coverage**: Address any requirements below 95% coverage
3. **Check dependencies**: Ensure logical task ordering
4. **Consider execution mode**: Choose based on automation needs
5. **Document gaps**: Note any requirements needing manual attention

## Next Steps

After generating your implementation plan:
1. **Review with team**: Share plan for feedback
2. **Execute tasks**: Start implementation following the plan
3. **Track progress**: Monitor task completion
4. **Update as needed**: Adjust plan based on discoveries
5. **Complete ESDI**: Implementation plan marks end of ESDI workflow
