# Review-Diff Language Detection Router

This router analyzes git diff output to detect file languages and route each file to appropriate language-specific review standards. Before pushing your commit, it generates comprehensive code review reports with targeted, actionable feedback based on the programming languages detected.

## MANDATORY: File and Line Number Reporting

**Every finding in your code review report MUST include the exact file name and line number(s) where the issue occurs, and files MUST be output using Markdown links with relative paths so hyperlinks work in VS Code AI chat.**

- For each HIGH, MEDIUM, or LOW severity item, explicitly list:
  - The affected file path as a Markdown link with a relative path (e.g., `[src/foo/bar.py](src/foo/bar.py)`).
  - The line number(s) where the change or issue is present (add after the link, e.g., `, line 42`).
- If a finding applies to multiple lines, specify the range (e.g., lines 10-15)
- If a finding applies to an entire file, state "entire file" and explain why
- Reports that do not include file and line numbers, or do not use Markdown links for files, will be considered incomplete.

**Example:**
MEDIUM: Unused import  
File: [src/foo/bar.py](src/foo/bar.py), line 42  
Details: The import 'os' is not used in this file.

**This requirement applies to all review areas and all languages.**

## Language Detection and Routing

**CRITICAL: Read all review-commit-* files to understand which file types have specific review items, and apply them individiaully to all changes in files.**

### Step 1: Identify All Changed Files by Language

Analyze the git diff output and categorize each changed file by its extension:
- **Python files**: `.py` → Apply Python review instructions
- **C++ files**: `.cpp`, `.hpp`, `.h`, `.cc`, `.c`, `.ipp` → Apply C++ review instructions
- **Java files**: `.java` → Apply Java review instructions
- **Go files**: `.go` → Apply Go review instructions
- **JavaScript/TypeScript**: `.js`, `.ts`, `.jsx`, `.tsx` → Apply JavaScript/TypeScript review (if available)
- **Documentation**: `.md`, `.rst`, `.txt` → Apply documentation review (general principles)
- **Other files**: Apply general code review principles

### Step 2: Apply Appropriate Language-Specific Instructions PER FILE

**For Python Files (.py)**
- **MUST USE:** `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-python.md`
- **Apply to:** Every `.py` file in the changes, regardless of how many other file types are present
- **Focus:** Type hints, PEP compliance, memory management, security, testing
- **Example:** If changes include `install.py`, `test_install.py`, and 5 markdown files, still apply Python review to both .py files

**For C++ Files (.cpp, .hpp, .h, .cc, .c, .ipp)**
- **MUST USE:** `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-cplusplus.md`
- **Apply to:** Every C++ file in the changes, regardless of how many other file types are present
- **Focus:** Memory safety, modern C++ standards, performance, thread safety
- **Example:** If changes include `parser.cpp`, `utils.h`, and 10 Python files, still apply C++ review to both C++ files

**For Java Files (.java)**
- **MUST USE:** `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-java.md`
- **Apply to:** Every `.java` file in the changes, regardless of how many other file types are present
- **Focus:** Modern Java features, Spring framework patterns, exception handling, JVM performance
- **Example:** If changes include `UserService.java`, `PaymentController.java`, and other files, apply Java review to both .java files

**For Go Files (.go)**
- **MUST USE:** `.olaf/data/practices/guidances/review/code-reviews/review-guidelines-go.md`
- **Apply to:** Every `.go` file in the changes, regardless of how many other file types are present
- **Focus:** Go idioms, error handling, concurrency patterns, goroutine management
- **Example:** If changes include `main.go`, `handler.go`, and other files, apply Go review to both .go files

**For Mixed Language Commits**
- **Review each file with its appropriate language-specific instructions**
- **Organize report by language**: Group Python findings together, C++ findings together, etc.
- **Cross-language considerations**: Note any interface compatibility concerns between languages

**For Other Languages**
- **Fallback:** Use general code review principles below
- **Adapt:** Apply relevant concepts from available language-specific files where applicable
- **Document:** Note which files were reviewed with general principles vs language-specific instructions

## General Code Review Areas (All Languages)

When language-specific instructions don't apply, or as supplementary guidelines:

1. **Code Duplication**
   - Identify any code duplication that could be refactored into shared functions or modules

2. **Code Formatting and Style Compliance**
   - Look for spelling errors in code, comments, and documentation
   - **clang-format compliance**: Check if `.clang-format` files exist in the project and verify code formatting matches the specified style
   - **Formatting consistency**: Ensure indentation, spacing, and bracket placement follows project standards
   - **Language-specific formatting**: Apply appropriate formatting rules for each language (PEP 8 for Python, Google/LLVM style for C++, etc.)

3. **Test Coverage**
   - Are there missing regression or unit test scenarios for the changes?
   - Suggest new or updated tests if coverage is insufficient
   - Verify test quality and maintainability

4. **Naming Convention Consistency**
   - **Variable naming**: Ensure new variables follow the same naming pattern as surrounding code (camelCase, snake_case, PascalCase)
   - **Function naming**: Check that function names are consistent with existing codebase conventions
   - **Class/struct naming**: Verify class names follow project standards
   - **Constant naming**: Ensure constants use appropriate naming (UPPER_CASE, kConstantName, etc.)
   - **File naming**: Check that new files follow existing naming patterns in the project
   - **Cross-reference existing code**: Compare naming patterns in the same file, module, or similar components to ensure consistency

## File Exclusions and Special Considerations

### Files and Directories to Exclude from Review

**DO NOT perform code review for the following file types or locations:**

- **Regression test files**: Any file with a `.play` or `.gsv` extension
- **Regression directories**: Any file or subdirectory under `/regression/`, `/play/`, or similar regression/test areas
- **Rationale**: These files are test scripts, test data, or generated content and are explicitly excluded from code review. AI review is not permitted for these files or directories.

**IMPORTANT:** If a code review request includes any file or folder matching these patterns, you MUST skip review for those files and do not include them in your report. Only source code files (e.g., `.py`, `.cpp`, etc.) outside these excluded areas should be reviewed.

### Critical Security Checks (All Files)

**Always scan for potential security vulnerabilities:**

#### Hardcoded Secrets Detection

- **Passwords**: Look for variables like `password`, `pwd`, `pass` with hardcoded values
- **API Keys**: Search for patterns like `api_key`, `apikey`, `secret_key`, `access_token`
- **Database credentials**: Check for `db_password`, `database_url`, `connection_string` with actual values
- **Authentication tokens**: Identify `auth_token`, `bearer_token`, `jwt_secret` with hardcoded values
- **Configuration files**: Pay special attention to `.env`, `.config`, `.ini`, `.yaml`, `.json` files

#### Security Red Flags

- **Plain text credentials**: Any configuration or code containing actual passwords/tokens
- **Commented secrets**: Credentials in comments that should be removed
- **Test credentials**: Even test/dummy credentials should use placeholder values
- **Environment variable exposure**: Hardcoded values that should use environment variables

**Action Required**: Flag any potential secrets and suggest using environment variables, secret management systems, or configuration placeholders instead.

## Review Process

1. **Pre-screening**: Check for file exclusions and critical security issues first
2. **Identify primary language(s)** in the commit
3. **Load appropriate language-specific instructions** from the corresponding .md file
4. **Apply language-specific review criteria** with priority on critical and high-severity issues
5. **Include general review areas** as supplementary checks
6. **Generate structured report** with specific, actionable feedback

## Severity-Based Review Output

**Organize all review findings by severity level in the following order. For EVERY finding, you MUST include:**

- The filename and line number(s) where the issue occurs (or a clear reference to the affected region). This is mandatory for every finding, regardless of severity.
- A concise description of the issue
- Actionable recommendations

**All findings MUST be grouped and organized into the following explicit severity sections. If you do not include file and line numbers for each finding, the review is incomplete and must be corrected.**

## Example Output Format

#### HIGH

- `roa/service/refund/api/refund_api_driver.py:120-130` — Unhandled exception in refund logic. Add specific exception handling for API failures.

#### MEDIUM

- `roa/helpers/shared_api/rco/railconnect_commitrefund_rq/encoders/RailConnect_CommitRefundRQEncoderV2_8.py:1-12` — Missing type hints and docstrings. Add type annotations and docstrings to constructor and encode method.

#### LOW

- `roa/service/refund/api/refund_api_driver.py:10-50` — Import blocks could be better organized for readability.

---

**All findings must be grouped in these sections, and every finding must include file/line references. This is required for every review.**

### HIGH Severity Issues

- **Security vulnerabilities**: Hardcoded secrets, credentials, potential exploits
- **Memory safety**: Memory leaks, use-after-free, buffer overflows (C++)
- **Runtime errors**: Null pointer dereferences, unhandled exceptions, undefined behavior
- **Thread safety**: Race conditions, deadlocks, data races
- **Critical performance**: Algorithms with poor Big-O complexity, major bottlenecks
- **Breaking changes**: API changes that break backward compatibility

### MEDIUM Severity Issues

- **Code quality**: Significant duplication, overly complex functions, poor separation of concerns
- **Best practices**: Missing type hints (Python), improper smart pointer usage (C++)
- **Testing gaps**: Missing unit tests for new functionality, insufficient edge case coverage
- **Documentation**: Missing or outdated API documentation, unclear function/class documentation
- **Formatting violations**: clang-format non-compliance, significant style inconsistencies
- **Naming inconsistencies**: Variables/functions that don't match surrounding code conventions

### LOW Severity Issues

- **Minor style**: Small formatting inconsistencies, minor spelling errors in comments
- **Optimization opportunities**: Minor performance improvements, unnecessary temporary objects
- **Code organization**: Suggestions for better file structure, import organization
- **Documentation polish**: Minor documentation improvements, better variable names
- **Consistency**: Minor naming convention variations that don't affect readability

**How to Use This Report:**

- **HIGH severity**: These issues may cause failures, security vulnerabilities, or major problems - consider addressing before pushing
- **MEDIUM severity**: These issues affect code quality and maintainability - consider addressing in this commit or a follow-up
- **LOW severity**: These are improvement suggestions that can be addressed when convenient
- Use the generated report as guidance to update your commit message and make any code or documentation changes you deem appropriate
- This process helps maintain code quality, consistency, and up-to-date documentation across different programming languages

Finish by asking the user if there are any other aspects of the code review they would like to discuss.
