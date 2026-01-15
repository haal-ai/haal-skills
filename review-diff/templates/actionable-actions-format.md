# Actionable Review Actions Template

## Structure

When include_actions=true, generate specific fix commands for each finding:

### High Severity Actions
For each HIGH severity issue, provide:
```markdown
### HIGH: [Issue Title]
**File:** [file-path], line [number]
**Issue:** [Description]
**Action:** 
```bash
# Command to fix the issue
[specific command or series of commands]
```
**Verification:**
```bash
# Command to verify the fix worked
[verification command]
```
```

### Medium Severity Actions
```markdown
### MEDIUM: [Issue Title]
**File:** [file-path], line [number]
**Issue:** [Description]
**Action:**
```bash
# Fix command
[command]
```
**Alternative:** [Alternative approach if applicable]
```

### Low Severity Actions
```markdown
### LOW: [Issue Title]
**File:** [file-path], line [number]
**Suggestion:**
```bash
# Improvement command
[command]
```
**Optional:** This can be addressed when convenient
```

## Action Types by Language

### Python Actions
- **Type hints**: Add type annotations using mypy suggestions
- **Import organization**: Use isort or IDE organize imports
- **Formatting**: Apply black or autopep8 formatting
- **Linting**: Fix pylint/flake8 issues

### C++ Actions  
- **Memory safety**: Replace raw pointers with smart pointers
- **Formatting**: Apply clang-format with project style
- **Modern C++**: Upgrade to modern C++ constructs
- **Include guards**: Add proper header guards

### Java Actions
- **Code formatting**: Apply google-java-format or equivalent
- **Import organization**: Organize imports, remove unused ones
- **Modern features**: Upgrade to modern Java constructs (streams, lambdas)
- **Spring patterns**: Fix dependency injection and configuration issues
- **Exception handling**: Improve exception handling patterns

### Go Actions
- **Code formatting**: Apply gofmt or goimports
- **Error handling**: Add proper error checks and wrapping
- **Concurrency**: Fix goroutine leaks and race conditions
- **Idioms**: Apply Go-specific patterns and best practices
- **Module management**: Update go.mod and dependencies

### Git/Configuration Actions
- **Line endings**: Configure .gitattributes for consistent line endings
- **Missing newlines**: Add newline at end of file
- **File permissions**: Fix executable permissions if needed

### Security Actions
- **Remove secrets**: Replace hardcoded values with environment variables
- **Update dependencies**: Upgrade vulnerable dependencies
- **Access control**: Implement proper authentication/authorization

## Command Categories

### Immediate Fixes
Commands that can be run immediately:
- Formatting tools (black, clang-format)
- Linting auto-fixes (eslint --fix)
- Import organization (isort)

### Manual Fixes
Issues requiring manual intervention:
- Logic changes
- API design improvements
- Architecture refactoring

### Verification Commands
Commands to verify fixes:
- Test runs
- Lint checks
- Build verification
- Security scans