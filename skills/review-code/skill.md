---
name: review-code
description: Comprehensive code review with multiple input modes - manual selection, git-modified files, or batch processing. Focuses on quality, security, and maintainability.
license: Apache-2.0
metadata:
  olaf_tags: [code-review, quality-assurance, security, best-practices, git, batch-processing, modified-files]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:

1. **source_mode**: [manual|git-modified|file-path|copy-paste] - How to identify code for review (REQUIRED)
2. **code_source**: string - What to review (copy-pasted code, file path, folder path, or repository) (REQUIRED for manual mode)
3. **language**: string - Programming language of the code (REQUIRED for manual mode)
4. **context**: string - Additional context about the changes (OPTIONAL)
5. **branch_name**: string - Specific branch to review (OPTIONAL for git-modified mode - defaults to current branch)
6. **file_filter**: string - File types to include (e.g., "*.cs,*.js,*.py") (OPTIONAL for git-modified mode)
7. **batch_size**: number - Number of files to process per batch (OPTIONAL for git-modified mode - default: 10)
8. **focus_areas**: array[enum] - Specific areas to focus on (security, performance, style, etc.) (OPTIONAL)
9. **review_standards**: string/file - Custom coding standards, style guides, or review principles to apply (OPTIONAL)
10. **team_conventions**: string/file - Team-specific conventions, patterns, or architectural guidelines (OPTIONAL)
11. **compliance_requirements**: array[string] - Specific compliance standards (OWASP, NIST, company policies) (OPTIONAL)

**DEFAULT STANDARDS**: You MUST apply these universal coding standards:
- **Universal Standards**: `.olaf/data/practices/standards/universal-coding-standards.md` - Universal coding principles, including the default **Evolution/Refactoring Mode** for existing code and **Creation/New Code Mode** for new modules
- **Team Standards Search**: Automatically search `.olaf/data/practices/standards/` for team-specific standards files
- **Integration Standards**: `.olaf/data/practices/standards/integration-testing-standards.md` - If applicable

When the code under review is part of an **existing system**, treat the **Evolution/Refactoring Mode** as default:
- Assume public APIs and observable behavior are frozen unless the user explicitly requests API changes
- Focus feedback on internal structure: SRP, DI for externals, function size, complexity, naming, error handling, and test coverage

When the user explicitly asks for feedback on a **new module/tool/feature** (greenfield), also apply the **Creation/New Code Mode** from the universal standards (small design first, module boundaries, file size discipline, public API coherence, tests alongside new behavior).

**CRITICAL**: Never assume what code to review. Always explicitly ask the user to specify:
1. What code they want reviewed (copy-paste, file, folder, or repo)
2. What programming language it is
3. Any specific focus areas or concerns
4. Any custom review standards, team conventions, or compliance requirements to apply

## Process

**MANDATORY STEPS - Execute in this exact order:**

### Phase 1: Mode Detection & Requirements Gathering

#### A. Determine Review Mode
1. **Check user request context** for git-related keywords ("modified files", "git changes", "current branch")
2. **Auto-select git-modified mode** if context suggests reviewing repository changes
3. **Ask user for mode selection** if ambiguous:
   - "Manual selection" (user specifies what to review)
   - "Git modified files" (review current branch changes)

#### B. Git-Modified Mode Process
1. **Execute git discovery**:
   - Run `git status --porcelain` to identify changed files
   - Categorize as Modified (M), New (A/?), Deleted (D)
   - Filter out binary/non-reviewable files
   - Present file list to user for confirmation
2. **Batch processing setup**:
   - Process files in manageable batches (default: 10)
   - Prioritize by importance and change complexity
   - Create progress tracking

#### C. Manual Mode Process
1. **Always ask the user first** for:
   - What code to review (copy-paste, file path, folder, or repository)
   - Programming language
   - Specific focus areas or concerns
2. **Never assume** what needs to be reviewed

### Phase 2: Practice Discovery & Standards Loading

#### A. Repository Practices (LOAD FIRST)
1. Search and read applicable repo practices in `.olaf/data/practices/practices/good-bad/*.md`.
2. Filter by detected programming `language` and the file/class under review.
3. Build a short checklist of applicable "good/bad" practices to apply first.

#### B. Standards Loading (After Practices)
1. **Team/Current Standards**: Search `.olaf/data/practices/standards/` for team-specific standards and load those first (if any)
2. **Universal Standards**: Read `.olaf/data/practices/standards/universal-coding-standards.md`
3. **Integration Standards**: Read `.olaf/data/practices/standards/integration-testing-standards.md` if applicable
4. **Confirm loaded set**: Ensure repo practices + team standards + universal standards are all loaded before proceeding

#### C. Strategic Planning (After Practices and Standards)
1. **Analyze the scope** of the code to be reviewed
2. **Determine the review approach**:
   - Single file vs. multiple files
   - Specific functions vs. entire codebase
   - Focus areas (security, performance, maintainability)
   - Precedence to apply: Repo Practices → Team/Current Standards → Universal Standards (plus any custom provided)
3. **Plan the review strategy** based on loaded standards, not general knowledge

### Phase 3: In-Depth Analysis (Apply Loaded Standards)
1. **Initial Analysis**:
   - Review code structure and organization
   - **Apply loaded repo practices FIRST**: Use applicable items from `.olaf/data/practices/practices/good-bad/*.md`
   - **Apply loaded team-specific standards**: Use any team standards found in `.olaf/data/practices/standards/`
   - **Apply loaded universal coding standards**: Use the specific standards from `.olaf/data/practices/standards/universal-coding-standards.md`
   - **Check against loaded quality principles**: Readability, maintainability, function length, complexity
   - **Apply custom review standards** (if provided by user)
   - **Verify adherence to team conventions** (if specified)
   - Assess error handling and logging using loaded standards2. **Security Assessment** (Using Loaded Standards):
   - **Apply loaded security standards**: Use security requirements from `.olaf/data/practices/standards/universal-coding-standards.md`
   - Identify potential vulnerabilities based on loaded standards
   - Check input validation per loaded requirements
   - Review authentication/authorization against loaded standards
   - **Apply compliance requirements** (OWASP, NIST, etc. if specified)
3. **Quality Evaluation** (Using Loaded Standards):
   - **Apply loaded quality standards**: Use readability & maintainability from loaded standards
   - **Check function length**: Apply loaded limits (typically 20-30 lines)
   - **Check complexity**: Apply loaded complexity limits (typically <10)
   - **Verify naming conventions**: Apply loaded naming standards
   - **Check test coverage**: Apply loaded testing requirements (typically >80%)
   - **Cross-reference with loaded standards**: Never use general knowledge, only loaded standards
4. **Performance Check**:
   - Identify potential bottlenecks
   - Review resource usage
   - Check for memory leaks
   - Assess algorithm efficiency

### Phase 4: Deep Investigation
- **Take time to understand** the code's purpose and context
- **Look for subtle issues** that might not be immediately obvious
- **Consider the broader implications** of the code changes
- **Think about edge cases** and potential failure scenarios

### Phase 5: Structuring Refactor Suggestions (If Applicable)

When you propose refactors (beyond pointing out issues), structure your
refactor suggestions using this format, aligned with the universal standards
Evolution/Refactoring Mode:

```text
## Current Code Analysis
[Brief issues identified: complexity, duplication, missing DI, etc.]

## Refactored Internals (Public API Unchanged)
[How to improve internal structure while keeping public APIs and behavior
stable]

## Modernization Proposal
- Benefits: [e.g., improved testability via DI, reduced complexity]
- Tests: [Characterization/unit/integration tests to add or update]
- Next Steps: [Safe evolution paths, potential API improvements]
```

Keep **public APIs and behavior frozen** in these refactor suggestions unless
the user explicitly requests API-level changes.

## Output Format
You WILL generate outputs following this structure:

**Primary Deliverable**: Use `templates/developer/code-review-template.md` to structure the review:
- Follow the template's sections for consistency
- Include all required fields from the template
- Replace placeholder content with actual analysis
- Maintain the structured format for documentation

**Save Locations**:
- Single file/manual mode: `.olaf/work/staging/code-review/<entity-name>-YYYYMMDD/review.md`
- Action plan: `.olaf/work/staging/code-review/<entity-name>-YYYYMMDD/action-plan.md`
- Git-modified mode summary: `.olaf/work/staging/code-reviews/code-review-summary-YYYYMMDD-NNN.md`

## User Communication

### Progress Updates
- Confirmation when review mode is determined
- Status when loading standards and practices
- Notification when analyzing each file or batch
- Progress tracking for git-modified mode (X of Y files reviewed)

### Completion Summary
- **For Single File/Manual Mode**:
  - Critical issues found (security vulnerabilities, major bugs, performance concerns)
  - Recommendations for improvements (code quality, best practices, refactoring)
  - Positive feedback (well-implemented features, clean code examples)
  - Files saved with locations
- **For Git-Modified Mode**:
  - Number of files reviewed by type (modified, new, deleted)
  - List of all generated code review files
  - Aggregated findings by severity level
  - Common patterns or issues found across multiple files

### Next Steps
- **For Single File/Manual Mode**:
  - Review the saved analysis at `.olaf/work/staging/code-review/<entity-name>-YYYYMMDD/review.md`
  - Follow the action plan at `.olaf/work/staging/code-review/<entity-name>-YYYYMMDD/action-plan.md`
  - Prioritize critical issues first
  - Consider applying similar improvements to related code
- **For Git-Modified Mode**:
  - Review the summary report at `.olaf/work/staging/code-reviews/code-review-summary-YYYYMMDD-NNN.md`
  - Address high-priority issues across all files
  - Consider team-wide improvements for common patterns
  - Review individual file analyses for detailed feedback

## Domain-Specific Rules
- Rule 1: Be constructive and specific
- Rule 2: Reference relevant standards
- Rule 3: Prioritize staging by severity
- Rule 4: Provide clear examples
- Rule 5: Consider context and constraints

## Success Criteria
You WILL consider the task complete when:
- [ ] Review mode determined and parameters gathered
- [ ] Standards and practices loaded from repository
- [ ] Code analyzed against loaded standards
- [ ] Security assessment completed
- [ ] Quality evaluation completed
- [ ] Performance check completed
- [ ] Review report generated and saved
- [ ] Action plan generated (for single file/manual mode)
- [ ] Summary report generated (for git-modified mode)
- [ ] User notified of completion with file locations

## Required Actions

### For All Review Modes
1. Analyze code changes
2. Identify issues and improvements
3. Document staging
4. Provide actionable feedback
5. Highlight positive aspects

### Single File/Manual Mode Actions
6. **ALWAYS propose saving results** - Ask user if they want to save the review as a file
7. **If user agrees**, derive `entity_name`:
   - For a single file: use the file basename without extension
   - For a folder or repository: use the last path segment as name
   - For copy-paste input: ask the user for a short, kebab-case entity name
8. **Save the review** to: `.olaf/work/staging/code-review/<entity_name>-YYYYMMDD/review.md`
9. **AFTER SAVING**: Automatically propose a curative action plan with specific, actionable steps
10. **Save the action plan** to: `.olaf/work/staging/code-review/<entity_name>-YYYYMMDD/action-plan.md`

### Git-Modified Mode Actions (Additional)
6. **Filter non-reviewable files** before user confirmation (binary files, large data files)
7. **Process in manageable batches** to avoid overwhelming output
8. **Prioritize high-impact files** (core logic, frequently changed) first
9. **Generate individual review files** before creating summary to ensure completeness
10. **Create comprehensive summary** with serial number: `.olaf/work/staging/code-reviews/code-review-summary-YYYYMMDD-NNN.md`
11. **Aggregate staging** across all reviewed files by severity level
12. **Identify common patterns** or issues found across multiple files

## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items (code source, language, mode) from user
- **Invalid Review Mode**: Ask user to select from valid options (manual, git-modified, file-path, copy-paste)
- **Git Command Failures**: Provide error details and suggest manual mode as alternative
- **Standards File Not Found**: Proceed with built-in knowledge, note limitation in review
- **File Access Issues**: Report specific files that couldn't be accessed, continue with accessible files
- **Large Batch Size**: Warn user and suggest smaller batch size for better performance
- **No Modified Files Found**: Inform user and ask if they want to review specific files instead

## Curative Action Plan Requirements

**MANDATORY**: After saving the code review, you MUST automatically generate and propose a curative action plan.

Use template: `templates/code-review-action-plan-template.md`

The action plan should include:
- **Priority Matrix**: Issues categorized by severity and difficulty
- **Actionable Steps**: Specific fix instructions for both human developers and LLM agents
- **Implementation Order**: Logical sequence considering dependencies
- **Effort Estimates**: Time/complexity estimates for each fix
- **Code Examples**: Before/after examples for major changes
- **Validation Criteria**: How to verify each fix is successful

Additionally, the action plan MUST always contain tasks to:
- Ensure the work is performed in a **dedicated git worktree**, not directly on the
  main/default working tree.
- Regularly verify that the solution **builds successfully** (run the appropriate
  build command during the work).
- Capture a **baseline of unit tests** at the start of the work (record current
  test status/coverage for the affected area).
- Re-run the **same unit tests at the end** and confirm the baseline is not
  degraded.
- If new test failures appear, add tasks to fix **only the new bugs introduced
  by this change** (do not attempt to solve pre-existing failing tests).

âš ï¸ **Critical Notes**
- **ALWAYS ASK FIRST**: Never assume what code to review - always explicitly ask the user
- **DEPTH REQUIRED**: Take time to understand code before jumping to conclusions
- **STRATEGIC APPROACH**: Plan your review methodology based on the code scope
- Never expose sensitive information
- Consider the change's context
- Balance perfection with practicality
- Respect team conventions
- Keep feedback objective
- **NO SHORTCUTS**: Thorough analysis is mandatory - never rush to conclusions

