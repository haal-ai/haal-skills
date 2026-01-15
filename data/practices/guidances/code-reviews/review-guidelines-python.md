
# Python Code Review Instructions

Generate a comprehensive code review report for Python code changes with specific, actionable feedback in the following areas:

## 1. **Python-Specific Issues**

### Type Hints and Static Analysis

- **Check for missing type hints**: Identify functions, methods, and variables lacking proper type annotations
- **Validate type hint accuracy**: Ensure type hints match actual usage and are not overly broad (e.g., `Any`)
- **Suggest mypy compliance**: Flag code that would fail mypy static type checking

### Python Best Practices

- **PEP 8 compliance**: Check for style violations (line length, naming conventions, imports organization)
- **Pythonic code patterns**: Identify non-Pythonic constructs that could use list comprehensions, context managers, or built-in functions
- **Import organization**: Ensure imports are grouped (standard library, third-party, local) and sorted
- **Docstring quality**: Verify functions/classes have proper docstrings following PEP 257

## 2. **Memory and Performance**

### Memory Management

- **Large data structure handling**: Flag inefficient use of lists/dicts that could benefit from generators or itertools
- **Memory leaks**: Identify circular references, unclosed files, or database connections
- **Global variable usage**: Warn about excessive global state that could cause memory retention

### Performance Optimization

- **Algorithm efficiency**: Suggest more efficient algorithms or data structures (e.g., set vs list for membership testing)
- **Loop optimization**: Identify opportunities for vectorization with numpy/pandas or built-in optimizations
- **String concatenation**: Flag inefficient string building (use join() or f-strings instead of +=)

## 3. **Error Handling and Robustness**

### Exception Management

- **Specific exception catching**: Replace bare `except:` with specific exception types
- **Resource cleanup**: Ensure proper use of context managers or try/finally blocks
- **Error propagation**: Check if exceptions are properly logged or re-raised with context

### Input Validation

- **Parameter validation**: Suggest validation for function parameters, especially public APIs
- **Edge case handling**: Identify missing handling for None, empty collections, or boundary conditions

## 4. **Security Concerns**

### Common Python Security Issues

- **SQL injection**: Check for string concatenation in database queries (suggest parameterized queries)
- **Path traversal**: Validate file path operations for potential directory traversal attacks
- **Pickle usage**: Warn about unpickling untrusted data
- **Eval/exec usage**: Flag dynamic code execution that could be security risks

## 5. **Testing and Quality Assurance**

### Test Coverage

- **Missing test scenarios**: Identify untested code paths, edge cases, or error conditions
- **Test quality**: Suggest improvements to test clarity, isolation, and maintainability
- **Mock usage**: Recommend proper mocking for external dependencies

### Code Organization

- **Function/class size**: Flag overly large functions or classes that should be decomposed
- **Separation of concerns**: Identify mixed responsibilities that violate single responsibility principle
- **Dependency injection**: Suggest ways to reduce tight coupling

## 6. **Documentation and Maintainability**

### Code Documentation

- **README updates**: Check if new features require README or documentation updates
- **API documentation**: Ensure public interfaces are properly documented
- **Configuration documentation**: Verify new config options are documented

### Code Clarity

- **Variable naming**: Suggest more descriptive names for unclear variables
- **Magic numbers**: Identify hard-coded values that should be constants
- **Complex expressions**: Recommend breaking down complex one-liners for readability

## Review Output Format

For each issue found, provide:

1. **File and line number**: Exact location of the issue
2. **Issue category**: Which section above it falls under
3. **Current code**: Show the problematic code snippet
4. **Suggested fix**: Provide specific, actionable code improvement
5. **Rationale**: Brief explanation of why the change improves the code

Example:

```
**File: `src/utils.py`, Line 45**
**Category: Python Best Practices - Type Hints**
**Current:** `def process_data(data):`
**Suggested:** `def process_data(data: List[Dict[str, Any]]) -> Dict[str, int]:`
**Rationale:** Adding type hints improves code clarity and enables static type checking
```

## Priority Levels

- **Critical**: Security issues, potential runtime errors, or major performance problems
- **High**: Code quality issues that significantly impact maintainability
- **Medium**: Style violations or minor optimization opportunities
- **Low**: Cosmetic improvements or optional enhancements
