# Tutorial: Generate Design

## Overview
This tutorial guides you through generating a layered system design from an EARS specification using the 5-task master chain coordinator.

## Prerequisites
- Completed EARS specification (from transform-raw-spec or similar)
- Access to design patterns knowledge base
- Understanding of layered architecture concepts
- Write access for output directory

## Estimated Time
1-2 hours

## Steps

### Step 1: Prepare Your Specification
Ensure your EARS specification is ready:
```
Example: ./output/specification.md
```

**Expected Result**: Valid EARS specification document accessible.

### Step 2: Invoke the Skill
Start the design generation:
```
generate design
```

**Expected Result**: Skill begins and prompts for parameters.

### Step 3: Provide Input Parameters
Specify required parameters:
```
specification_file: ./output/specification.md
output_file: ./output/design.md
```

**Expected Result**: Parameters validated and Task 1 begins.

### Step 4: Review Task 1 - Specification Analysis
The skill analyzes your specification:
```
Extracted:
- Functional requirements: 15
- Quality attributes: 5
- Constraints: 3
- Data flow type: pipeline
- Interaction model: batch
```

**Expected Result**: Specification analysis complete, context variables set.

### Step 5: Review Task 2 - Application Type
The skill identifies your application type:
```
📐 Proposed Design

Application Type: CLI Tool
Pattern: Command-Line Architecture
Layers: 4
Confidence: High

Would you like me to:
1. Proceed with this design
2. Adjust layer structure
3. Change technology choices
4. Modify application type classification
```

**Expected Result**: Select option 1 to proceed or adjust as needed.

### Step 6: Review Task 3 - Layer Architecture
The skill designs your layers:
```
Layer 1: Input Processing
  - Purpose: Parse and validate input
  - Technology: Python argparse
  - Input: CLI arguments
  - Output: Validated config object

Layer 2: Core Logic
  - Purpose: Execute main functionality
  - Technology: Python modules
  - Input: Config object
  - Output: Processing results

Layer 3: Output Formatting
  - Purpose: Format and present results
  - Technology: Rich/tabulate
  - Input: Processing results
  - Output: Formatted output

Layer 4: Error Handling
  - Purpose: Manage errors and logging
  - Technology: Python logging
  - Input: Exceptions
  - Output: User-friendly messages
```

**Expected Result**: Layer architecture defined with clear responsibilities.

### Step 7: Review Task 4 - Task Breakdown
The skill creates implementation tasks:
```
Phase 1: Setup (2 tasks)
  - Task 1.1: Create project structure
  - Task 1.2: Set up dependencies

Phase 2: Layer 1 - Input Processing (3 tasks)
  - Task 2.1: Implement argument parser
  - Task 2.2: Add validation logic
  - Task 2.3: Create config object

Phase 3: Layer 2 - Core Logic (4 tasks)
  ...
```

**Expected Result**: Complete task breakdown with dependencies.

### Step 8: Review Task 5 - Design Document
The skill generates the final document:
```
Creating design.md with:
- Architecture overview
- Layer definitions
- Interface contracts
- Task breakdown
- Quality gates
```

**Expected Result**: `design.md` created at specified output path.

### Step 9: Verify Design Document
Review the generated design:
```markdown
# System Design: [Your Project]

## Architecture Overview
[ASCII diagram]

## Layer Definitions
[Detailed layer specs]

## Interface Contracts
[Input/output definitions]

## Task Breakdown
[Implementation tasks]

## Quality Gates
[Validation checkpoints]
```

**Expected Result**: Comprehensive design document ready for implementation planning.

### Step 10: Proceed to Implementation Planning
Use the design for Phase 4:
```
generate implementation plan
specification_file: ./output/specification.md
design_file: ./output/design.md
output_file: ./output/IMPLEMENTATION-TASK-PLAN.md
```

**Expected Result**: Ready to generate executable implementation plan.

## Expected Outcomes

### Successful Completion
- Complete design document
- Appropriate architecture pattern selected
- All layers defined with interfaces
- Task breakdown ready for implementation

### Design Document Contents
| Section | Description |
|---------|-------------|
| Architecture Overview | High-level system diagram |
| Layer Definitions | Detailed layer specifications |
| Interface Contracts | Input/output definitions |
| Task Breakdown | Implementation approach |
| Quality Gates | Validation checkpoints |

### Validation Checklist
- [ ] Application type correctly identified
- [ ] Each layer has single responsibility
- [ ] Interfaces explicitly defined
- [ ] Technology choices justified
- [ ] Tasks have dependencies mapped
- [ ] Quality checkpoints identified

## Troubleshooting

### Common Issues

**Issue**: "Specification file not found"
**Solution**: Verify path to specification.md is correct

**Issue**: "Application type incorrect"
**Solution**: Use option 4 at user approval gate to modify classification

**Issue**: "Missing design patterns KB"
**Solution**: Ensure `kb/design-patterns-guidance.md` is accessible

**Issue**: "Layer count seems wrong"
**Solution**: Use option 2 at user approval gate to adjust structure

### Best Practices

1. **Review specification first**: Ensure EARS spec is complete before designing
2. **Validate application type**: Confirm the detected type matches your needs
3. **Check layer responsibilities**: Each layer should have one clear purpose
4. **Verify interfaces**: Ensure data flows clearly between layers
5. **Consider extensibility**: Design for future requirements

## Next Steps

After generating your design:
1. **Review with team**: Share design for feedback
2. **Generate implementation plan**: Use generate-implementation-plan skill
3. **Refine if needed**: Return to adjust architecture
4. **Document decisions**: Capture design rationale
5. **Continue ESDI**: Move to Phase 4 (Implementation Planning)
