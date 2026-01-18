# Tutorial: ESDI Chain

## Overview
This tutorial guides you through the complete ESDI workflow, from initial idea exploration to a fully executable implementation plan. You'll learn how to coordinate the four phases and produce comprehensive development documentation.

## Prerequisites
- OLAF framework installed and configured
- Access to all ESDI phase skills:
  - challenge-me (Phase 1)
  - transform-raw-spec (Phase 2)
  - generate-design (Phase 3)
  - generate-implementation-plan (Phase 4)
- Clear initial idea or problem statement
- Terminal access for session management

## Estimated Time
4-8 hours (varies by project complexity)

## Steps

### Step 1: Initialize ESDI Session
Start a new ESDI workflow:
```
esdi chain
```

**Expected Result**: Session initialization begins with options to create new or resume existing session.

### Step 2: Choose Session Type
Select your session option:
```
Options:
a) Resume existing ESDI session
b) Create new ESDI session
c) View session details
```

**Expected Result**: For new projects, select option (b).

### Step 3: Provide Topic Name
Enter a short, descriptive topic name:
```
Example: repository-scanner
Format: kebab-case
```

**Expected Result**: Output directory created at `.olaf/work/staging/esdi/YYYYMMDD-repository-scanner/`

### Step 4: Describe Your Idea
Provide your initial problem statement:
```
Example: "Create an intelligent onboarding system that scans repositories, 
analyzes code structure, and generates comprehensive documentation"
```

**Expected Result**: Idea captured and Phase 1 begins.

### Step 5: Complete Phase 1 - Exploration
Work through the challenge-me skill interactively:
- Engage in ideation cycles
- Respond to challenges and refinements
- Review research and citations
- Say "save" when satisfied

**Expected Result**: 
- `exploration-findings.md` created
- Ideas refined and documented
- Research sources captured

### Step 6: Complete Phase 2 - Specification
Transform findings into EARS requirements:
- Step 1: Clarify & Group (automated)
- Step 2: Transform to EARS (automated)
- Step 3: Quality Check (make decisions)
- Step 4: Completeness (make decisions)
- Step 5: Challenge & Amplify (make decisions)
- Step 6: Visual Documentation (automated)
- Step 7: Testability Assessment (automated)

**Expected Result**:
- `specification.md` created
- Formal EARS requirements documented
- Step files for traceability

### Step 7: Complete Phase 3 - Design
Generate layered system design:
- Review specification analysis
- Approve application type classification
- Review proposed architecture
- Confirm layer structure

**Expected Result**:
- `design.md` created
- Architecture diagrams included
- Component interfaces defined

### Step 8: Complete Phase 4 - Implementation Planning
Generate executable task breakdown:
- Requirements extracted and mapped
- Task 0.0 (context extraction) generated
- Task breakdown created
- Requirement coverage validated

**Expected Result**:
- `IMPLEMENTATION-TASK-PLAN.md` created
- Requirement traceability matrix included
- Ready for bootstrap execution

### Step 9: Review Final Outputs
Verify all ESDI artifacts:
```
.olaf/work/staging/esdi/YYYYMMDD-repository-scanner/
├── exploration-findings.md    ✅
├── specification.md           ✅
├── design.md                  ✅
└── IMPLEMENTATION-TASK-PLAN.md ✅
```

**Expected Result**: All four artifacts present and complete.

### Step 10: Execute Implementation Plan
Start implementation using bootstrap orchestrator:
```bash
python .\.olaf\core\agentic\straf\olaf_strands_agent.py \
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" \
  --context "bootstrap_doc=${output_dir}/IMPLEMENTATION-TASK-PLAN.md" \
  --tool-mode auto \
  --aws-profile bedrock
```

**Expected Result**: Implementation begins following the generated task plan.

## Expected Outcomes

### Successful Completion
- Complete ESDI artifact set
- Formal requirements with traceability
- Layered architecture design
- Executable implementation plan

### Phase Outputs Summary
| Phase | Output | User Engagement |
|-------|--------|-----------------|
| 1 - Exploration | exploration-findings.md | HIGH |
| 2 - Specification | specification.md | HIGH |
| 3 - Design | design.md | MEDIUM |
| 4 - Implementation | IMPLEMENTATION-TASK-PLAN.md | LOW |

### Validation Checklist
- [ ] All four phases completed
- [ ] Each output file exists and is valid
- [ ] Implementation plan includes Task 0.0
- [ ] All review gates passed
- [ ] Ready for bootstrap execution

## Troubleshooting

### Common Issues

**Issue**: "Phase skill not found"
**Solution**: Verify all dependent skills are installed (challenge-me, transform-raw-spec, generate-design, generate-implementation-plan)

**Issue**: "Session state lost"
**Solution**: Use `start_phase` parameter to resume from last completed phase

**Issue**: "Output directory not created"
**Solution**: Check write permissions for `.olaf/work/staging/esdi/` directory

**Issue**: "Phase 2 decisions unclear"
**Solution**: Review exploration findings before making specification decisions

### Best Practices

1. **Don't rush exploration**: Phase 1 sets the foundation for everything else
2. **Document decisions**: Capture reasoning during interactive phases
3. **Review between phases**: Ensure each phase output is satisfactory before proceeding
4. **Use resume capability**: Save progress and resume if needed
5. **Validate coverage**: Check requirement traceability before implementation

## Next Steps

After completing ESDI:
1. **Execute implementation plan**: Use bootstrap orchestrator
2. **Track progress**: Monitor task completion
3. **Iterate if needed**: Return to earlier phases if gaps discovered
4. **Document learnings**: Capture insights for future projects
5. **Share artifacts**: Make ESDI outputs available to team
