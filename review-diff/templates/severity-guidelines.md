# Severity Guidelines

## HIGH Severity Issues

**Definition**: Issues that may cause failures, security vulnerabilities, or major problems

**Categories:**
- **Security vulnerabilities**: Hardcoded secrets, credentials, potential exploits
- **Memory safety**: Memory leaks, use-after-free, buffer overflows (C++)
- **Runtime errors**: Null pointer dereferences, unhandled exceptions, undefined behavior
- **Thread safety**: Race conditions, deadlocks, data races
- **Critical performance**: Algorithms with poor Big-O complexity, major bottlenecks
- **Breaking changes**: API changes that break backward compatibility

**Action**: Consider addressing before pushing

## MEDIUM Severity Issues

**Definition**: Issues that affect code quality and maintainability

**Categories:**
- **Code quality**: Significant duplication, overly complex functions, poor separation of concerns
- **Best practices**: Missing type hints (Python), improper smart pointer usage (C++)
- **Testing gaps**: Missing unit tests for new functionality, insufficient edge case coverage
- **Documentation**: Missing or outdated API documentation, unclear function/class documentation
- **Formatting violations**: clang-format non-compliance, significant style inconsistencies
- **Naming inconsistencies**: Variables/functions that don't match surrounding code conventions

**Action**: Consider addressing in this commit or a follow-up

## LOW Severity Issues

**Definition**: Minor improvements and suggestions

**Categories:**
- **Minor style**: Small formatting inconsistencies, minor spelling errors in comments
- **Optimization opportunities**: Minor performance improvements, unnecessary temporary objects
- **Code organization**: Suggestions for better file structure, import organization
- **Documentation polish**: Minor documentation improvements, better variable names
- **Consistency**: Minor naming convention variations that don't affect readability

**Action**: Address when convenient

## Classification Guidelines

1. **Impact Assessment**: Consider the potential impact on functionality, security, and maintainability
2. **Urgency**: Evaluate how quickly the issue should be addressed
3. **Context Matters**: Same issue might have different severity in different contexts
4. **Language-Specific**: Apply language-specific severity criteria from knowledge base