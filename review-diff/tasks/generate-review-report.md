---
task_id: "generate-review-report"
task_name: "Generate Review Report"
dependencies: ["context.findings", "context.save_report", "context.include_actions"]
conditions: []
---

# Generate Review Report

## Input Context
**Required Context Variables**: 
- `context.findings`: Structured findings (HIGH/MEDIUM/LOW)
- `context.security_issues`: Security-specific findings
- `context.quality_issues`: Code quality issues
- `context.actionable_commands`: Fix commands (if enabled)
- `context.save_report`: Boolean - save to file or display
- `context.include_actions`: Boolean - include fix commands
- `context.timestamp`: Session timestamp (YYYYMMDD-HHMMSS) from master skill initialization
- `context.language_categories`: Detected languages
- `context.files_by_language`: Files categorized by language
**Required Files**: None
**Required Tools**: File I/O for saving report (if enabled)

## Task Instructions

### Create Comprehensive Review Report

1. **Build Report Structure**:
   
   **Section 1: Language Detection Results**
   ```markdown
   ## Language Detection Results
   
   **Files Analyzed by Language**:
   - Python: [count] files
   - C++: [count] files
   - Java: [count] files
   - Go: [count] files
   - Other: [count] files
   
   **Review Standards Applied**:
   - Python: review-standard-python.md
   - C++: review-standard-cplusplus.md
   - [etc.]
   ```

   **Section 2: Security Assessment**
   ```markdown
   ## Security Assessment
   
   **HIGH Priority Security Issues** ([count]):
   - [`file.py:42`](file.py#L42) - Hardcoded API key detected
   - [`module.cpp:105`](module.cpp#L105) - Potential buffer overflow
   
   **MEDIUM Priority**:
   [list issues]
   ```

   **Section 3: Code Quality Findings**
   ```markdown
   ## Code Quality Findings
   
   ### HIGH Severity ([count])
   - [`file.py:15`](file.py#L15) - Function exceeds complexity threshold
   
   ### MEDIUM Severity ([count])
   - [`file.py:23`](file.py#L23) - Missing type hints
   
   ### LOW Severity ([count])
   - [`file.py:8`](file.py#L8) - Line exceeds 120 characters
   ```

   **Section 4: Test Coverage Assessment**
   ```markdown
   ## Test Coverage Assessment
   
   **Missing Tests**:
   - `new_module.py` - No corresponding test file found
   
   **Test Directives Needed**:
   - Add unit tests for new functions
   ```

   **Section 5: Actionable Commands** (if include_actions=true)
   ```markdown
   ## Actionable Fix Commands
   
   ### Formatting
   ```bash
   black file.py
   clang-format -i module.cpp
   ```
   
   ### Linting
   ```bash
   pylint file.py
   ```
   
   ### Security
   - Remove hardcoded API key from file.py:42
   - Use environment variables or secure vault
   ```

2. **Format Report Output**:
   - Use proper Markdown formatting
   - Make file paths clickable links with line anchors
   - Group findings by severity
   - Include file/line references for every finding
   - Add summary statistics at top

3. **Handle Output Method**:
   
   **Option A: Save to Staging Directory** (if save_report=true):
   - Create directory: `.olaf/work/staging/diff-reviews/`
   - Save report: `review-report-[timestamp].md`
   - If include_actions=true, save: `actions-[timestamp].md`
   - Display confirmation with file paths
   
   **Option B: Display on Screen** (default):
   - Output complete report to console
   - Format for readability
   - Include summary at end

4. **Generate Summary Statistics**:
   ```markdown
   ## Review Summary
   
   **Total Findings**: [count]
   - HIGH: [count]
   - MEDIUM: [count]
   - LOW: [count]
   
   **Security Issues**: [count]
   **Files Reviewed**: [count]
   **Languages**: [list]
   ```

## Output Requirements

**State Updates**:
- `context.report_file`: Path to saved report file (if saved)
- `context.actions_file`: Path to actions file (if saved and enabled)
- `context.report_displayed`: Boolean indicating report was shown
- `context.report_summary`: Summary statistics object
- `task_status.generate-review-report`: "completed"

**Files Created**: 
- `.olaf/work/staging/diff-reviews/review-report-[timestamp].md` (if save_report=true)
- `.olaf/work/staging/diff-reviews/actions-[timestamp].md` (if save_report=true AND include_actions=true)

**Context Passed to Next Tasks**:
- Report file path for cleanup tracking (if saved)
