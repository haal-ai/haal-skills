---
name: validate-prompt-value
description: Comprehensive evaluation of prompt effectiveness, business value, and implementation quality
license: Apache-2.0
metadata:
  olaf_tags: [validation, effectiveness, value-assessment, quality-assurance]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **prompt_source**: string - The prompt to validate (file path, copy-paste, or prompt name) (REQUIRED)
- **validation_scope**: string - Scope of validation (effectiveness|business-value|technical-quality|complete) (REQUIRED)
- **use_case_context**: string - Intended use case or business scenario for the prompt (OPTIONAL)
- **success_metrics**: string - Expected outcomes or performance criteria (OPTIONAL)
- **target_audience**: string - Who will use this prompt (developers, business analysts, etc.) (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for comprehensive validation due to analysis impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm prompt source is accessible and readable
- Validate validation scope is one of supported options
- Check access to evaluation frameworks and criteria
- Verify prompt follows standard structure if applicable

### 2. Execution Phase
You WILL execute these operations based on validation scope:

**Effectiveness Analysis** (when scope includes effectiveness or complete):
- Analyze prompt clarity and specificity
- Evaluate instruction structure and imperative language usage
- Assess parameter completeness and validation requirements
- Review error handling comprehensiveness
- Check success criteria definition and measurability

**Business Value Assessment** (when scope includes business-value or complete):
- Evaluate problem-solution alignment
- Assess automation potential and efficiency gains
- Analyze scalability and reusability factors
- Review integration potential with existing workflows
- Calculate estimated time savings and resource optimization

**Technical Quality Review** (when scope includes technical-quality or complete):
- Validate prompt engineering best practices adherence
- Check OLAF framework compliance if applicable
- Assess maintainability and documentation quality
- Review extensibility and configuration options
- Evaluate security considerations and data handling

**Core Logic**: Execute comprehensive validation protocol
- Apply systematic evaluation criteria for selected scope
- Generate quantified assessment scores where applicable
- Provide actionable improvement recommendations
- Document validation methodology and assumptions

### 3. Validation Phase
You WILL validate assessment results:
- Confirm all evaluation criteria were applied
- Verify recommendations are actionable and specific
- Validate scoring methodology is consistent and transparent

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Comprehensive validation report with structured sections
- Validation summary: Executive summary with key findings and recommendations
- Scoring matrix: Quantified assessment across multiple dimensions
- Improvement roadmap: Prioritized action items for enhancement

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when prompt analysis begins
- Status updates for each validation dimension
- Completion notification for scoring and recommendations

### Completion Summary
- Overall validation score and category rating
- Key strengths identified in the prompt
- Critical improvement areas highlighted
- Estimated implementation effort for recommendations

### Next Steps
You WILL clearly define:
- Priority actions for prompt improvement
- Recommended validation frequency for iterative improvement
- Suggested testing methodology for effectiveness verification
- Framework compliance actions if applicable

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: You MUST provide quantified scores (1-10 scale) for each evaluation dimension
- Rule 2: You WILL prioritize recommendations by impact and implementation effort
- Rule 3: You NEVER validate prompts without explicit user consent for the assessment scope
- Rule 4: You MUST document all assumptions and limitations in your evaluation methodology
- Rule 5: You WILL provide specific examples for improvement recommendations

## Success Criteria
You WILL consider the task complete when:
- [ ] Prompt source successfully analyzed and documented
- [ ] All validation dimensions for selected scope completed
- [ ] Quantified scores provided with clear methodology
- [ ] Actionable improvement recommendations generated
- [ ] Validation report structured and formatted properly
- [ ] Next steps clearly defined for prompt enhancement

## Required Actions
1. Validate prompt source accessibility and validation scope
2. Execute systematic evaluation following established criteria
3. Generate quantified assessment with supporting evidence
4. Provide structured recommendations with implementation guidance
5. Document validation methodology and next steps

## Error Handling
You WILL handle these scenarios:
- **Prompt Source Inaccessible**: Request alternative source method or file path correction
- **Invalid Validation Scope**: Provide list of supported scopes and request valid selection
- **Incomplete Prompt Structure**: Note structural issues and provide framework guidance
- **Missing Context Information**: Request additional context for accurate business value assessment
- **Evaluation Criteria Conflicts**: Document conflicts and provide multiple assessment perspectives

⚠️ **Critical Requirements**
- MANDATORY: Provide quantified scores for objective evaluation comparison
- MANDATORY: Include specific examples in all improvement recommendations
- NEVER validate prompts without understanding their intended use case
- ALWAYS document evaluation methodology and assumptions for transparency
- ALWAYS provide both strengths and improvement areas for balanced assessment
- ALWAYS prioritize recommendations by business impact and implementation feasibility
