---
task_id: "analyze-diff-with-router"
task_name: "Analyze Diff with Language Router"
dependencies: ["context.diff_text", "context.files_by_language"]
conditions: []
---

# Analyze Diff with Language Router

## Input Context
**Required Context Variables**: 
- `context.diff_text`: Complete diff content
- `context.files_by_language`: Files categorized by language
- `context.language_categories`: List of detected languages
**Required Files**: 
- `helpers/review-diff-router.md`: Router helper for language-specific analysis
- Language-specific guidelines:
  - `.olaf/data/practices/guidances/code-reviews/review-guidelines-python.md`
  - `.olaf/data/practices/guidances/code-reviews/review-guidelines-cplusplus.md`
  - `.olaf/data/practices/guidances/code-reviews/review-guidelines-java.md`
  - `.olaf/data/practices/guidances/code-reviews/review-guidelines-go.md`
**Required Tools**: None

## Task Instructions

### Execute Router-Based Code Analysis

1. **Load Router Helper**:
   Read and apply instructions from:
   ```
   helpers/review-diff-router.md
   ```

2. **Apply Language-Specific Standards**:
   For each language category in `context.files_by_language`:
   
   **Python files**:
   - Load: `.olaf/data/practices/guidances/code-reviews/review-guidelines-python.md`
   - Apply Python-specific quality checks
   - Check: PEP 8, typing, docstrings, imports
   
   **C++ files**:
   - Load: `.olaf/data/practices/guidances/code-reviews/review-guidelines-cplusplus.md`
   - Apply C++ standards
   - Check: RAII, const correctness, memory management
   
   **Java files**:
   - Load: `.olaf/data/practices/guidances/code-reviews/review-guidelines-java.md`
   - Apply Java conventions
   - Check: Naming, encapsulation, exception handling
   
   **Go files**:
   - Load: `.olaf/data/practices/guidances/code-reviews/review-guidelines-go.md`
   - Apply Go standards
   - Check: gofmt, error handling, interfaces
   
   **Other files**:
   - Apply general code quality principles
   - Focus on security and consistency

3. **Security Vulnerability Scan**:
   For ALL file types:
   - Scan for hardcoded secrets (API keys, passwords, tokens)
   - Check for credential exposure in logs or comments
   - Identify potential injection vulnerabilities
   - Flag use of deprecated/insecure functions

4. **Code Quality Assessment**:
   - **Formatting**: Indentation, spacing, line length
   - **Naming**: Variables, functions, classes
   - **Documentation**: Comments, docstrings
   - **Complexity**: Cyclomatic complexity, nesting depth
   - **Test Coverage**: Missing test files or test directives

5. **Categorize Findings by Severity**:
   ```json
   {
     "HIGH": [
       {"file": "path", "line": 42, "issue": "description", "category": "security"}
     ],
     "MEDIUM": [
       {"file": "path", "line": 15, "issue": "description", "category": "quality"}
     ],
     "LOW": [
       {"file": "path", "line": 8, "issue": "description", "category": "style"}
     ]
   }
   ```

6. **Generate Actionable Fix Commands** (if include_actions enabled):
   For each finding, create specific fix command:
   - Code formatting: `black file.py` or `clang-format -i file.cpp`
   - Import sorting: `isort file.py`
   - Linting: `pylint file.py`
   - Security: Specific remediation steps

## Output Requirements

**State Updates**:
- `context.findings`: Structured findings object (HIGH/MEDIUM/LOW)
- `context.security_issues`: Array of security-specific findings
- `context.quality_issues`: Array of code quality issues
- `context.actionable_commands`: Array of fix commands (if enabled)
- `context.findings_count`: Total number of findings
- `task_status.analyze-diff-with-router`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Findings for report generation
- Security issues for priority highlighting
- Actionable commands for user guidance
