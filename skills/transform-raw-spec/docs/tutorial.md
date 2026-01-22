# Tutorial: Transform Raw Spec

## Overview
This tutorial guides you through transforming a raw specification document into a complete, testable EARS specification using the 7-step process.

## Prerequisites
- Raw specification or rules document to transform
- Access to transform-raw-spec templates
- Understanding of EARS (Easy Approach to Requirements Syntax)
- Terminal access for timestamp generation
- Write access to output directory

## Estimated Time
2-4 hours (varies by specification complexity)

## Steps

### Step 1: Prepare Your Source Document
Ensure your raw specification is accessible:
```
Example: docs/my-project-rules.md
```

**Expected Result**: Source document ready for transformation.

### Step 2: Invoke the Skill
Start the transformation process:
```
transform raw spec
```

**Expected Result**: Skill begins and prompts for parameters.

### Step 3: Provide Input Parameters
Specify required parameters:
```
raw_rules_path: docs/my-project-rules.md
output_folder: spec-my-project
spec_name: My Project
```

**Expected Result**: Parameters validated and transformation begins.

### Step 4: Review Step 1 - Clarify & Group
The skill automatically:
- Extracts domains from your specification
- Identifies gaps and questions
- Groups related requirements

**Expected Result**: `step1-<timestamp>.md` created with domain grouping.

### Step 5: Review Step 2 - Transform to EARS
The skill automatically:
- Converts requirements to EARS format
- Normalizes flags and terminology
- Structures with Trigger/Condition/Response/Measure

**Expected Result**: `step2-<timestamp>.md` created with EARS requirements.

### Step 6: Complete Step 3 - Quality Check
User engagement required:
```
Review presented items:
1. Contradictions found
2. Duplicate requirements
3. Scope clarifications needed

Make decisions for each numbered item.
```

**Expected Result**: `step3-<timestamp>.md` created with your decisions recorded.

### Step 7: Complete Step 4 - Completeness & Consistency
User engagement required:
```
Review and decide on:
1. Missing scenarios
2. Edge cases
3. Terminology consistency
4. Conflict resolution
```

**Expected Result**: `step4-<timestamp>.md` created with completeness decisions.

### Step 8: Complete Step 5 - Challenge, Simplify, Amplify
User engagement required:
```
Review challenge catalog:
- CLI UX patterns
- Error taxonomy
- Security hardening
- Retry/idempotency patterns

Assign MoSCoW priorities.
```

**Expected Result**: `step5-<timestamp>.md` created with challenge decisions.

### Step 9: Review Step 6 - Visual Documentation
The skill automatically generates:
- High-level architecture diagram
- Process flow diagrams
- State diagrams
- Error handling trees

**Expected Result**: `step6-<timestamp>.md` created with Mermaid diagrams.

### Step 10: Review Step 7 - Testability Assessment
The skill automatically generates:
- Verification criteria framework
- Test categories and scenarios
- Quality metrics
- Success thresholds

**Expected Result**: `step7-<timestamp>.md` created with testability assessment.

### Step 11: Review Final Specification
The skill consolidates all outputs:
```
specification.md contains:
- Complete EARS requirements
- All decisions integrated
- Ready for design phase
```

**Expected Result**: `specification.md` created as the definitive output.

### Step 12: Verify Output Structure
Check your output folder:
```
spec-my-project/
├── step1-20251122-1430.md
├── step2-20251122-1445.md
├── step3-20251122-1500.md
├── step4-20251122-1520.md
├── step5-20251122-1545.md
├── step6-20251122-1600.md
├── step7-20251122-1615.md
└── specification.md
```

**Expected Result**: All step files and final specification present.

## Expected Outcomes

### Successful Completion
- 7 timestamped step files
- Consolidated specification.md
- All decisions documented
- Ready for design phase

### Output Quality Indicators
- EARS format consistently applied
- No unresolved contradictions
- Complete testability criteria
- Visual documentation included

### Validation Checklist
- [ ] All 7 steps completed
- [ ] User decisions recorded in Steps 3-5
- [ ] specification.md is complete
- [ ] Diagrams render correctly
- [ ] Testability criteria defined

## Troubleshooting

### Common Issues

**Issue**: "Template not found"
**Solution**: Verify templates exist in `templates/` directory

**Issue**: "Timestamp format incorrect"
**Solution**: Use time tools or `scripts/now/bin/now-<os>-<arch>` binary

**Issue**: "Mermaid diagrams not rendering"
**Solution**: Use a stronger model for Step 6 or mark for later upgrade

**Issue**: "Step 2 needs refresh after decisions"
**Solution**: The skill will prompt for Step 2 refresh if flags/terms change

### Best Practices

1. **Read source thoroughly**: Understand your raw spec before starting
2. **Take time on decisions**: Steps 3-5 decisions affect final quality
3. **Document rationale**: Explain why you made each decision
4. **Review diagrams**: Ensure visual documentation is accurate
5. **Validate testability**: Confirm all requirements are testable

## Next Steps

After transforming your specification:
1. **Proceed to design**: Use specification.md with generate-design skill
2. **Share with team**: Review specification with stakeholders
3. **Update if needed**: Return to earlier steps if gaps found
4. **Archive step files**: Keep for traceability
5. **Continue ESDI**: Move to Phase 3 (Design) if in ESDI workflow
