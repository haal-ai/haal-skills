# generate-spec-from-dfd

> Step-by-step tutorial for generating functional specifications from DFD analysis

## Prerequisites
- Existing DFD analysis files (e.g., `{project}_analysis.md`)
- Source code access for technical detail confirmation
- Optionally: `DFD_level1_tasks.md`, `DFD_level2_tasks.md`

## Estimated Time
15–30 minutes

## Step-by-Step Instructions

### Step 1: Provide DFD Analysis Path
> "Generate a functional spec from the DFD analysis in docs/dfd/"

Specify:
- **dfd_analysis_path**: Path to DFD analysis files
- **source_path**: Path to source code for confirmation
- **project_name**: Project identifier

### Step 2: DFD Parsing
The skill reads DFD documentation as the primary source:
- Level 1 data flows (system overview)
- Level 2 data flows (detailed process breakdown)
- External entities and data stores

### Step 3: Codebase Confirmation
Source code is examined only to:
- Replace vague terms with exact values
- Confirm technical implementation details
- Identify precise function/API names

### Step 4: Review Draft Specification
A developer-implementable functional specification is generated with:
- Precise requirements (no ambiguity)
- Traceability to DFD elements
- QA checklists per functional area
- Implementation notes

### Step 5: Approve and Save
Review the specification, request changes if needed, and approve to save.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| DFD files not found | Verify the dfd_analysis_path is correct |
| Vague requirements | Point to source code for precise details |
| Missing traceability | Ensure DFD has numbered data flows |
| Spec too long | Focus on critical paths first |

## Verification Checklist
- [ ] All DFD data flows mapped to requirements
- [ ] Requirements are precise and implementable
- [ ] Traceability links back to DFD elements
- [ ] Source code confirms technical details
- [ ] QA checklists included
