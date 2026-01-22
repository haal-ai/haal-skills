# Analyze Spec Vs Code

## Overview
The `analyze-spec-vs-code` skill compares an EARS (Easy Approach to Requirements Syntax) specification against the codebase to produce gap analysis, impact analysis, and remediation plans through a structured three-phase process.

## Purpose
This skill exists to identify discrepancies between requirements specifications and actual code implementation, providing systematic analysis of what's implemented, missing, or diverged from the spec. It helps teams ensure code alignment with business requirements and plan remediation efforts.

## Key Features
- **Multi-phase analysis**: Gap analysis, impact analysis, and remediation planning
- **EARS specification parsing**: Structured analysis of Trigger/Condition/Response/Measure requirements
- **Traceability matrix**: Mapping of requirements to implementation status with evidence
- **Process workflow analysis**: End-to-end execution flow mapping
- **Data model alignment**: Schema and configuration validation
- **Impact assessment**: Business and technical impact evaluation
- **Sequenced remediation planning**: Structured work breakdown for closing gaps

## Usage
Invoke the skill by name: `analyze-spec-vs-code`

## Parameters

### Required Parameters
- **ears_spec_path**: string - Path to the decision-aligned EARS spec (Step 2)
- **code_roots**: string[] - One or more root folders to scan (e.g., ["scripts/olaf", "vscode-extension/src"])
- **output_folder**: string - Folder to write staging (e.g., `spec-<channel>-<model>` or `staging`)

### Optional Parameters
- **languages**: string[] - Languages of interest (e.g., ["go", "ts", "md"])
- **strict_template_compliance**: boolean - Enforce template structure (default: true)

## Process Flow
1. **Validation Phase**: Verify parameters, spec accessibility, and code permissions
2. **Phase 1 - Gap Analysis**: Parse EARS spec, perform static code scan, create traceability matrix
3. **Phase 1B - Process Workflow**: Map execution flow and identify UX issues
4. **Phase 1C - Data Model**: Enumerate structures and recommend schema changes
5. **Phase 2 - Impact Analysis**: Assess impacts of missing/diverged items
6. **Phase 3 - Remediation Plan**: Create sequenced work breakdown and acceptance criteria

## Output
Generates comprehensive analysis reports in `.olaf/work/staging/spec-analysis/`:
- `phase1-gap-analysis-<timestamp>.md` - Requirements traceability matrix
- `phase1b-process-workflow-<timestamp>.md` - Process flow analysis
- `phase1c-data-model-<timestamp>.md` - Data model alignment
- `phase2-impact-analysis-<timestamp>.md` - Impact assessment
- `phase3-remediation-plan-<timestamp>.md` - Remediation strategy

## Examples
- Analyzing a new feature specification against existing codebase
- Validating compliance with regulatory requirements
- Planning migration from legacy to new system specifications
- Ensuring implementation completeness for critical business functions

## Error Handling
- **Missing EARS Spec**: Requests correct path and validates accessibility
- **Code Root Access Issues**: Provides alternative scan approaches
- **Template Compliance Failures**: Offers to proceed with available data
- **Static Scan Failures**: Documents limitations and enables manual analysis

## Related Skills
- `bootstrap-functional-spec-from-code` - For creating specs from existing code
- `review-human-written-spec` - For challenging and improving specifications
- `generate-tech-spec-from-code` - For comprehensive technical documentation
