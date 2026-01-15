---
name: analyze-spec-vs-code
description: Propose–Act protocol to compare an EARS specification against the codebase, produce Phase 1 gaps, Phase 2 impact analysis, and Phase 3 remediation plan.
license: Apache-2.0
metadata:
  olaf_tags: [business-analyst, requirements, EARS, gap-analysis, impact-analysis, remediation-plan, propose-act]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **ears_spec_path**: string - Path to the decision-aligned EARS spec (Step 2) (REQUIRED)
- **code_roots**: string[] - One or more root folders to scan (e.g., ["scripts/olaf", "vscode-extension/src"]) (REQUIRED)
- **languages**: string[] - Languages of interest (e.g., ["go", "ts", "md"]) (OPTIONAL)
- **output_folder**: string - Folder to write staging (e.g., `spec-<channel>-<model>` or `staging`) (REQUIRED)
- **strict_template_compliance**: boolean - Enforce template structure (default: true) (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- **Propose-Act**: For each phase, follow Propose → Act → Confirm
- Select appropriate protocol based on operation risk and impact
- Propose: Outline the structure using the template + which tools/scans you will run
- Act: Generate the output file with fresh timestamp in output_folder
- Confirm: Summarize outcomes and list any open questions

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate EARS spec accessibility and format
- Check access to code roots and scan permissions
- Verify output folder write permissions

### 2. Execution Phase
You WILL execute these operations following Propose-Act protocol:

## Phase 1 — Spec vs Code: Gap Analysis
Template: `templates/spec-gap-analysis-template.md`
- Parse the EARS spec (Trigger/Condition/Response/Measure) and enumerate REQ-IDs.
- Perform static scan on `[code_roots]` to locate places implementing flags/behaviors/logging/exit codes.
- Populate a Traceability Matrix (req → status: Implemented / Missing / Diverged) with evidence (file:line) and short notes.
- Capture “Open Questions” where ambiguity prevents classification.
- **Save as**: `.olaf/work/staging/spec-analysis/phase1-gap-analysis-<timestamp>.md`

## Phase 1B — Process & Workflow Alignment
Template: `templates/spec-process-workflow-template.md`
- Map the end-to-end execution flow with file:line evidence (flags → anchoring → registry → selection → plan → TMP → swap → refresh/update).
- Identify process UX issues (help/version, confirmation gates, precedence visibility, dry-run ordering, retries/backoff, lock handling).
- **Save as**: `.olaf/work/staging/spec-analysis/phase1b-process-workflow-<timestamp>.md`

## Phase 1C — Data Model Alignment
Template: `templates/spec-data-model-template.md`
- Enumerate struct/JSON shapes and their locations; map to spec expectations (config schema, registry presence, provenance, schema versioning).
- Recommend schema/artifact changes (e.g., traceability JSON, source fields).
- **Save as**: `.olaf/work/staging/spec-analysis/phase1c-data-model-<timestamp>.md`

## Phase 2 — Impact Analysis
Template: `templates/spec-impact-analysis-template.md`
- For Missing and Diverged items, assess impacts:
  - Change type (New/Modify/Deprecate/Remove)
  - Business/Technical impacts and risk
  - Affected modules/APIs/CLI flags, data/config/schema
  - Effort estimation and sequencing/rollback
  - Test impacts (affected/new ATs/VCs)
- **Save as**: `.olaf/work/staging/spec-analysis/phase2-impact-analysis-<timestamp>.md`

## Phase 3 — Remediation Plan
Template: `templates/spec-remediation-plan-template.md`
- Propose a sequenced Work Breakdown by capability/domain to close gaps and resolve divergences.
- Define acceptance criteria per workstream and risk management.
- Identify communication cadence and Definition of Done (spec refresh if needed).
- **Save as**: `.olaf/work/staging/spec-analysis/phase3-remediation-plan-<timestamp>.md`

### 3. Validation Phase
You WILL validate results:
- Confirm all phase reports are generated correctly
- Verify template compliance and completeness
- Validate traceability matrix accuracy

## Output Format
You WILL generate outputs following this structure:
- **Primary deliverable**: Multi-phase analysis reports following respective templates
- **Output location**: Save all reports in `.olaf/work/staging/spec-analysis/` subfolder
- **Supporting files**: Static scan results and code evidence files
- **Documentation**: Comprehensive gap analysis and remediation plan

**File Naming Convention**:
- Phase 1: `.olaf/work/staging/spec-analysis/phase1-gap-analysis-<timestamp>.md`
- Phase 1B: `.olaf/work/staging/spec-analysis/phase1b-process-workflow-<timestamp>.md`
- Phase 1C: `.olaf/work/staging/spec-analysis/phase1c-data-model-<timestamp>.md`
- Phase 2: `.olaf/work/staging/spec-analysis/phase2-impact-analysis-<timestamp>.md`
- Phase 3: `.olaf/work/staging/spec-analysis/phase3-remediation-plan-<timestamp>.md`

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when each phase completes
- Location/reference of generated reports
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Summary of all phases executed
- Files created with locations in `.olaf/work/staging/spec-analysis/` subfolder
- Concise status summary: counts of Implemented / Missing / Diverged
- Top risks identified and ETA for remediation plan

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Prefer deterministic mapping between REQ-IDs and code evidence with exact file:line references
- Rule 2: Follow Propose-Act protocol strictly for each phase before proceeding to next
- Rule 3: Verify Measures when possible (timings, exit codes, log lines) for evidence validation
- Rule 4: Maintain cross-links between Phase 1 matrix rows and Phase 1B/1C detailed sections

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated and EARS spec parsed
- [ ] All three phases (1, 2, 3) executed with sub-phases (1B, 1C)
- [ ] Traceability matrix populated with evidence
- [ ] All outputs generated in specified template format
- [ ] User communication completed with status summary
- [ ] Save locations confirmed in `.olaf/work/staging/spec-analysis/` subfolder

## Required Actions
1. Validate all required input parameters and EARS spec accessibility
2. Execute Phase 1 (Gap Analysis) with sub-phases 1B and 1C following Propose-Act protocol
3. Execute Phase 2 (Impact Analysis) for Missing and Diverged items
4. Execute Phase 3 (Remediation Plan) with sequenced work breakdown
5. Provide comprehensive user communication with status summary
6. Confirm all files saved in `.olaf/work/staging/spec-analysis/` subfolder

## Error Handling
You WILL handle these scenarios:
- **Missing EARS Spec**: Request correct path and validate accessibility
- **Code Root Access Issues**: Provide alternative scan approaches or request permissions
- **Template Compliance Failures**: Offer to proceed with available data or request clarification
- **Static Scan Failures**: Document limitations and proceed with manual analysis where possible

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for each phase (Propose → Act → Confirm)
- NEVER proceed to next phase without confirming current phase completion
- ALWAYS provide exact file:line evidence for traceability matrix
- ALWAYS cross-reference Phase 1 findings with detailed 1B/1C analysis
- ALWAYS validate template compliance before saving files
- IF Steps 3-5 decisions evolved after EARS spec, add TODO to refresh Step 2 and re-run Phase 1

