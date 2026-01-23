---
name: evolve-code-iteratively
description: Incrementally improve code based on specific goals (performance, maintainability, testability) using a structured, iterative approach.
license: Apache-2.0
metadata:
  olaf_tags: [refactoring, code-quality, optimization, iterative]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:
1. **code**: string - The code to be analyzed and evolved (REQUIRED)
2. **goals**: array[enum] - Primary goals from: performance, maintainability, testability (REQUIRED - select one or more)
3. **iterations**: number - Maximum number of iterations (OPTIONAL - default: 3, max: 5)
4. **test_cases**: string - Test cases to validate changes (OPTIONAL)

**IMPORTANT**: You MUST apply the **Evolution/Refactoring Mode** from the universal coding standards as the default:
- Read `.olaf/data/practices/standards/universal-coding-standards.md` and treat public APIs and observable behavior as **frozen** unless the user explicitly requests API changes
- Focus changes on internal structure (private helpers, data flows, wiring), enforcing SRP, DI for external dependencies, and reasonable function size/complexity
- Prefer small, incremental refactors validated by tests over large rewrites

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before modifying code
- Present improvement options as numbered lists for easy selection
- Provide clear progress updates at each iteration
- Confirm user choice between proposed options before implementing changes

## Process

### 1. Validation Phase
You MUST verify all requirements:
- Confirm all required parameters (code, goals) are provided
- Validate goals are from allowed set (performance, maintainability, testability)
- Check if test cases are available for validation
- Read universal coding standards if available

### 2. Initial Assessment Phase
You WILL analyze the code:
- Analyze code structure and patterns
- Establish baseline metrics (count lines, functions, complexity indicators where measurable)
- Identify optimization opportunities with estimated impact
- Identify public APIs and externally observable behavior that must remain stable in this evolution
- Document current state and technical debt
- If tests around the affected behavior are missing, propose or add **characterization tests** to lock in current behavior before deep refactors

### 3. Iterative Improvement Phase
You WILL execute improvement cycles:
- For each iteration (up to max iterations):
  1. Critique current code against goals
  2. Propose two distinct solutions with specific implementation details
  3. Compare options with pros/cons table
  4. Make a recommendation to the USER and ask for feedback: "Option 1", "Option 2", or "Stop here"
  5. Based on USER feedback, implement selected changes
  6. Validate with unit tests if they exist or propose to create basic validation
  7. Document changes and measure impact where possible
- Continue until max iterations reached or user chooses to stop

### 4. Finalization Phase
You WILL generate comprehensive deliverables:
- Generate comprehensive improvement report with available metrics
- Document all changes made with rationale for each decision
- Provide before/after code comparison with annotations
- Include recommendations for future improvements
- Create rollback instructions if needed

## Output Format
You WILL generate outputs following this structure:

**Primary Deliverable**: Use template: `templates/developer/code-evolution-report-template.md`

The report should include:
- Initial assessment with baseline metrics
- Iteration reports documenting each improvement cycle
- Before/after code comparisons with annotations
- Metrics comparison showing improvements
- Decision log with rationale for each change
- Rollback instructions for each iteration
- Final recommendations for future work

**Save Location**: `.olaf/work/staging/code-evolution/YYYYMMDD-HHmm/`

## User Communication

### Progress Updates
- Initial code quality assessment and identified improvement areas
- Proposed iteration plan with goals
- Changes made in each iteration with impact on goals
- Validation results after each change
- Confirmation when each iteration completes

### Completion Summary
- Summary of improvements with measurable impact where possible
- Qualitative assessment of code quality improvements
- Performance analysis (theoretical gains, algorithm improvements)
- Number of iterations completed
- Files created with locations

### Next Steps
- Recommendations for future work
- Rollback instructions for each change made
- Suggestions for additional testing or validation
- Consider applying similar improvements to related code

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Preserve functionality - Never break existing functionality without explicit user approval
- Rule 2: One change per iteration - Keep iterations small and focused on one primary improvement area
- Rule 3: Validate with tests - Always validate changes preserve functionality
- Rule 4: Document decisions - Document all assumptions and limitations clearly
- Rule 5: Maintain readability - Consider team's skill level when proposing solutions
- Rule 6: Provide rollback capability and instructions for each change
- Rule 7: Stop iterations if no meaningful improvements can be identified
- Rule 8: Measure impact where possible, document qualitative improvements where quantitative metrics aren't available

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated
- [ ] Initial code assessment completed with baseline metrics
- [ ] Iterative improvements executed (up to max iterations or user stops)
- [ ] Each iteration validated with tests or validation proposed
- [ ] Comprehensive improvement report generated
- [ ] Before/after code comparison provided
- [ ] Rollback instructions documented
- [ ] User notified of completion with summary

## Required Actions
1. Validate all required input parameters are provided
2. Analyze input code and establish baseline measurements
3. Define success criteria for each selected goal
4. Execute iterative improvement process with user feedback
5. Validate changes preserve functionality
6. Document process and generate comprehensive deliverables

## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items (code or goals) from user
- **Invalid Goals**: Ask user to select from valid options (performance, maintainability, testability)
- **Test Validation Failures**: Stop iteration, report issue, ask user for guidance
- **No Improvements Identified**: Stop iterations early, report current state as optimal
- **User Stops Early**: Generate report with completed iterations only
- **Template File Missing**: Generate report without template structure

⚠️ **Critical Requirements**
- MANDATORY: Get user approval before modifying code
- MANDATORY: Preserve functionality unless explicitly approved to change
- NEVER break existing functionality without explicit user approval
- ALWAYS provide rollback instructions for each change
- ALWAYS validate changes with tests when available
- ALWAYS document assumptions and limitations clearly
- ALWAYS present two options for user choice at each iteration

