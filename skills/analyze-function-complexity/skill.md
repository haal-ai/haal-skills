---
name: analyze-function-complexity
description: Analyze a specific function's complexity, structure, and provide detailed metrics similar to complexity analyzer output
license: Apache-2.0
metadata:
  olaf_tags: [function-analysis, complexity, code-quality, metrics]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed



## Input Parameters
You MUST request these parameters if not provided by the user:
- **function_name**: string - Name of the function to analyze (REQUIRED)
- **file_path**: string - Path to the file containing the function (OPTIONAL)
- **language**: string - Programming language (auto-detected if file_path provided) (OPTIONAL)
- **context**: string - Additional context about the function's purpose (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select appropriate protocol based on operation risk and impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate function location and accessibility
- Check access to required tools and files

### 2. Execution Phase
You WILL execute these operations as needed:

**Function Location**:
- If file_path provided, locate the function in the file
- If only function_name provided, search the current workspace
- Extract the complete function code including signature and body

**Complexity Analysis**:
   - Calculate cyclomatic complexity using standard patterns:
     - Decision points: if, else if, else, switch, case, default
     - Loops: for, foreach, while, do-while
     - Logical operators: &&, ||, and, or
     - Exception handling: try, catch, except, finally
     - Ternary operators: ? :
   - Count lines of code (excluding comments and blank lines)
   - Calculate complexity density (complexity / line_count)
   - Determine maximum nesting depth
   - Count function parameters

**Structure Analysis**:
- Function signature analysis (parameters, return type)
- Nesting depth analysis with specific depth calculation
- Variable scope analysis
- Dependency analysis (functions/methods called)
- External dependency identification
- Coupling level assessment (Low/Medium/High)

**Quality Assessment**:
- Code readability score (1-10 scale)
- Maintainability indicators (1-10 scale)
- Testability score (1-10 scale)
- Potential refactoring opportunities with specific patterns
- Best practices adherence assessment

**Risk and Recommendations**:
- Apply standard risk thresholds:
  - 1-5: Low risk
  - 6-10: Moderate risk
  - 11-20: High risk
  - 21-50: Very High risk
  - 50+: Critical risk
- Generate specific, actionable recommendations with line references
- Identify concrete refactoring opportunities
- Calculate required test coverage based on complexity

### 3. Validation Phase
You WILL validate results:
- Confirm all complexity metrics are calculated correctly
- Verify template formatting meets requirements
- Validate recommendations are actionable and specific

## Output Format
You WILL generate outputs following this structure:
- **Primary deliverable**: Follow template `templates/function-complexity-analysis-template.md`
- **Output location**: Save analysis in `.olaf/work/staging/function-analyses/` subfolder
- **Supporting files**: Include calculation methodology and reasoning in the report
- **Documentation**: Complete report with all required sections populated

**File Naming Convention**:
- Format: `function-analysis-{function_name}-{timestamp}.md`
- Example: `function-analysis-processUserData-20251119-1430.md`
- Location: `.olaf/work/staging/function-analyses/function-analysis-{function_name}-{timestamp}.md`

The report MUST follow the exact template structure and include all sections:

### Required Template Sections:
1. **Function Metadata**: Name, file path, language, analysis timestamp
2. **Function Signature**: Complete code signature with parameters and return type
3. **Complexity Metrics**: 
   - Cyclomatic complexity score
   - Lines of code (excluding comments/blank lines)
   - Complexity density (complexity/line_count)
   - Maximum nesting depth
   - Parameter count
4. **Complexity Breakdown Table**: Count and complexity points by construct type:
   - If/Else statements
   - Loops (for, while, do-while, foreach)
   - Switch/Case statements
   - Logical operators (&&, ||, and, or)
   - Exception handling (try/catch/finally)
5. **Risk Assessment**: Level classification with standard thresholds
6. **Code Quality Indicators**: Readability, maintainability, testability scores (1-10)
7. **Dependencies**: Functions called, external dependencies, coupling level
8. **Recommendations**: Specific, actionable improvement suggestions with line numbers
9. **Refactoring Opportunities**: Concrete patterns and techniques to apply
10. **Test Coverage Recommendations**: Minimum test cases based on complexity score

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Brief overview of complexity and risk level with specific metrics
- Key metrics: cyclomatic complexity, lines of code, complexity density
- Immediate actions: Priority recommendations with specific line numbers when applicable

### Completion Summary
- Detailed report using the exact template format with all required sections populated
- Template placeholders populated with actual analysis results
- **File saved as**: `.olaf/work/staging/function-analyses/function-analysis-{function_name}-{timestamp}.md`
- **Analysis timestamp**: {YYYYMMDD-HHmm format}
- **Report location**: Full path to generated analysis file in staging directory

**Template Placeholders to Populate**:
- {function_name}, {file_path}, {language}, {timestamp}
- {function_signature} - complete code signature
- {complexity_score}, {line_count}, {complexity_density}, {max_nesting_depth}, {parameter_count}
- {if_count}, {loop_count}, {switch_count}, {logical_count}, {exception_count}
- {if_complexity}, {loop_complexity}, {switch_complexity}, {logical_complexity}, {exception_complexity}
- {risk_level} - using standard thresholds
- {readability_score}, {maintainability_score}, {testability_score} - scored 1-10
- {called_functions}, {external_deps}, {coupling_level}
- {recommendations_list} - specific, actionable items with line references
- {refactoring_suggestions} - concrete patterns and techniques
- {min_test_cases}, {branch_tests}, {edge_case_tests}

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Always provide specific, actionable recommendations with line references when possible
- Rule 2: Include complexity calculation methodology and show work
- Rule 3: Consider language-specific patterns and idioms in analysis
- Rule 4: Provide context-appropriate thresholds based on function purpose
- Rule 5: Include both quantitative metrics and qualitative assessment

## Success Criteria
You WILL consider the task complete when:
- [ ] Function located and extracted successfully
- [ ] All complexity metrics calculated using proper methodology
- [ ] Template populated with all required placeholders
- [ ] Risk assessment applied using standard thresholds
- [ ] Specific recommendations provided with actionable guidance
- [ ] Quality scores assigned on 1-10 scales
- [ ] Test coverage requirements calculated
- [ ] Analysis report saved in `.olaf/work/staging/function-analyses/` subfolder
- [ ] File location provided to user with full staging directory path

## Required Actions
1. Validate all required input parameters and function accessibility
2. Extract function code and analyze structure following appropriate interaction protocol
3. Calculate all complexity metrics using language-specific patterns
4. Generate outputs in specified template format
5. Provide user communication with progress updates and completion summary
6. Ensure all template placeholders are populated with accurate data

## Error Handling
You WILL handle these scenarios:
- **Missing Function**: Provide clear guidance on function location methods
- **File Access Issues**: Offer alternative search approaches in workspace
- **Language Detection Failures**: Request user clarification on programming language
- **Complexity Calculation Issues**: Explain methodology and request code clarification
- **Template Formatting Problems**: Validate all required sections are included

⚠️ **Critical Requirements**
- MANDATORY: Follow established interaction protocol (Act/Propose-Act/Propose-Confirm-Act)
- MUST use exact template format from `templates/function-complexity-analysis-template.md`
- ALL template placeholders must be populated with actual values
- ALWAYS provide actionable, specific guidance with line references when possible
- ALWAYS include positive aspects and strengths when present
- ALWAYS balance thoroughness with clarity in reporting

