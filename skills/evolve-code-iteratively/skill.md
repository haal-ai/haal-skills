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

**IMPORTANT**: When you don't have these required parameters, ask the USER to provide them.
- **code**: string - The code to be analyzed and evolved (REQUIRED)
- **goals**: array[enum] - Primary goals from: performance, maintainability, testability (REQUIRED - select one or more)
- **iterations**: number - (Optional) Maximum number of iterations (default: 3, max: 5)
- **test_cases**: string - (Optional) Test cases to validate changes

You MUST apply the **Evolution/Refactoring Mode** from the universal coding
standards as the default:
- Read `.olaf/data/practices/standards/universal-coding-standards.md` and treat
  public APIs and observable behavior as **frozen** unless the user explicitly
  requests API changes.
- Focus changes on internal structure (private helpers, data flows, wiring),
  enforcing SRP, DI for external dependencies, and reasonable function
  size/complexity.
- Prefer small, incremental refactors validated by tests over large rewrites.

## Process
1. **Initial Assessment**:
   - Analyze code structure and patterns
   - Establish baseline metrics (count lines, functions, complexity indicators where measurable)
   - Identify optimization opportunities with estimated impact
   - Identify public APIs and externally observable behavior that must remain
     stable in this evolution.
   - Document current state and technical debt
   - If tests around the affected behavior are missing, propose or add
     **characterization tests** to lock in current behavior before deep
     refactors.
2. **Iterative Improvement**:
   - For each iteration (up to max iterations):
     1. Critique current code against goals
     2. Propose two distinct solutions with specific implementation details
     3. Compare options with pros/cons table
     4. Make a recommendation to the USER and ask for feedback: "Option 1", "Option 2", or "Stop here"
     5. Based on USER feedback, implement selected changes
     6. Validate with unit tests if they exist or propose to create basic validation
     7. Document changes and measure impact where possible
   - Continue until max iterations reached or user chooses to stop
3. **Finalization**:
   - Generate comprehensive improvement report with available metrics
   - Document all changes made with rationale for each decision
   - Provide before/after code comparison with annotations
   - Include recommendations for future improvements
   - Create rollback instructions if needed

## Output/Result Format

Use template: `templates/developer/code-evolution-report-template.md.md`

The report should include:
- Initial assessment with baseline metrics
- Iteration reports documenting each improvement cycle
- Before/after code comparisons with annotations
- Metrics comparison showing improvements
- Decision log with rationale for each change
- Rollback instructions for each iteration
- Final recommendations for future work

Save iteration reports to: `.olaf/work/staging//code-evolution/YYYYMMDD-HHmm/`

## Output to USER
1. **Initial Analysis**:
   - Code quality assessment
   - Identified improvement areas
   - Proposed iteration plan
2. **Iteration Updates**:
   - Changes made in each iteration
   - Impact on goals
   - Validation results
3. **Final Report**:
   - Summary of improvements with measurable impact where possible
   - Qualitative assessment of code quality improvements
   - Performance analysis (theoretical gains, algorithm improvements)
   - Recommendations for future work
   - Rollback instructions for each change made

## Domain-Specific Rules
- Rule 1: Preserve functionality
- Rule 2: One change per iteration
- Rule 3: Validate with tests
- Rule 4: Document decisions
- Rule 5: Maintain readability

## Required Actions
1. Validate all required input parameters are provided
2. Analyze input code and establish baseline measurements
3. Define success criteria for each selected goal
4. Execute iterative improvement process with user feedback
5. Validate changes preserve functionality
6. Document process and generate comprehensive deliverables

⚠️ **Critical Notes**
- Never break existing functionality without explicit user approval
- Keep iterations small and focused on one primary improvement area
- Provide rollback capability and instructions for each change
- Document all assumptions and limitations clearly
- Consider team's skill level when proposing solutions
- Stop iterations if no meaningful improvements can be identified
- Measure impact where possible, document qualitative improvements where quantitative metrics aren't available

