---
description: "Code review for C++"
applyTo: "*.cpp,*.hpp,*.h,*.c,*.ipp"
---
# C++ Code Review Instructions

Generate a comprehensive code review report for C++ code changes with specific, actionable feedback in the following areas:

## 1. **Memory Management and Resource Safety**

### Memory Leaks and Ownership
- **Raw pointer usage**: Identify raw pointers that should use smart pointers (`std::unique_ptr`, `std::shared_ptr`)
- **Memory leak detection**: Check for `new` without corresponding `delete`, or missing destructors
- **Double deletion**: Flag potential double-delete scenarios or use-after-free bugs
- **RAII compliance**: Ensure resources are properly managed through constructors/destructors

### Smart Pointer Best Practices
- **Appropriate smart pointer choice**: Suggest `unique_ptr` vs `shared_ptr` vs `weak_ptr` based on ownership semantics
- **Circular reference detection**: Identify potential `shared_ptr` cycles that need `weak_ptr`
- **Custom deleters**: Check if custom deleters are needed for non-standard cleanup

## 2. **Modern C++ Standards and Best Practices**

### C++11/14/17/20 Features
- **Range-based loops**: Replace traditional for loops where appropriate
- **Auto keyword usage**: Suggest `auto` for complex type declarations while maintaining readability
- **Lambda expressions**: Identify opportunities for lambda usage in algorithms
- **Move semantics**: Check for missing move constructors/assignment operators
- **Constexpr usage**: Suggest `constexpr` for compile-time constants and functions

### STL and Standard Library
- **Algorithm usage**: Replace manual loops with STL algorithms (`std::find`, `std::transform`, etc.)
- **Container choice**: Suggest appropriate containers (`vector` vs `list` vs `deque` vs `unordered_map`)
- **Iterator safety**: Check for iterator invalidation issues

## 3. **Performance and Optimization**

### Efficiency Concerns
- **Pass by reference**: Flag expensive copy operations that should use const references
- **Return value optimization**: Ensure functions return by value when RVO/NRVO applies
- **Unnecessary copies**: Identify temporary objects or redundant copying
- **Cache efficiency**: Suggest data structure layouts that improve cache locality

### Algorithmic Efficiency
- **Big-O complexity**: Identify algorithms with poor time/space complexity
- **Premature optimization**: Flag micro-optimizations that hurt readability without significant benefit
- **Compiler optimization hints**: Suggest `inline`, `constexpr`, or `[[likely]]` attributes where beneficial

## 4. **Thread Safety and Concurrency**

### Synchronization Issues
- **Race conditions**: Identify shared data access without proper synchronization
- **Deadlock potential**: Check for multiple lock acquisition that could deadlock
- **Atomic operations**: Suggest `std::atomic` for simple shared variables
- **Thread-safe alternatives**: Recommend thread-safe containers or patterns

### Modern Concurrency
- **std::thread usage**: Check for proper thread lifecycle management
- **Future/promise patterns**: Suggest async patterns where appropriate
- **Lock-free programming**: Identify opportunities for lock-free data structures

## 5. **Error Handling and Robustness**

### Exception Safety
- **Exception safety guarantees**: Ensure functions provide basic, strong, or no-throw guarantees
- **RAII for exception safety**: Check that resources are properly cleaned up during stack unwinding
- **Custom exception types**: Suggest specific exception types instead of generic `std::runtime_error`

### Input Validation and Edge Cases
- **Null pointer checks**: Verify pointer validity before dereferencing
- **Boundary conditions**: Check array bounds, container size validation
- **Integer overflow**: Identify potential arithmetic overflow scenarios
- **Undefined behavior**: Flag operations that could result in undefined behavior

## 6. **Code Organization and Design**

### Class Design
- **Rule of Three/Five/Zero**: Ensure proper implementation of special member functions
- **Virtual destructor**: Check for missing virtual destructors in base classes
- **Interface segregation**: Identify overly large interfaces that should be split
- **Const correctness**: Ensure proper use of `const` methods and parameters

### Header File Management
- **Include guards**: Verify proper header guards or `#pragma once`
- **Forward declarations**: Suggest forward declarations to reduce compilation dependencies
- **Header inclusion**: Check for unnecessary includes or missing includes
- **Namespace usage**: Ensure proper namespace usage and avoid `using namespace std` in headers

## 7. **Security Considerations**

### Buffer Safety
- **Buffer overflows**: Check array/string operations for potential overflows
- **Format string vulnerabilities**: Validate printf-style format strings
- **Integer overflow security**: Identify arithmetic operations that could be exploited

### Safe Coding Practices
- **Input sanitization**: Ensure external input is properly validated
- **Secure random numbers**: Check for cryptographically secure random number usage where needed
- **Compiler security features**: Suggest enabling stack protection and other security features

## 8. **Testing and Quality Assurance**

### Test Coverage
- **Unit test completeness**: Identify missing test cases for new functionality
- **Edge case testing**: Suggest tests for boundary conditions and error paths
- **Mock usage**: Recommend proper mocking for external dependencies
- **Performance testing**: Suggest benchmarks for performance-critical code

### Code Quality Metrics
- **Cyclomatic complexity**: Flag overly complex functions that should be decomposed
- **Code duplication**: Identify repeated code that should be refactored
- **Function length**: Suggest breaking down large functions

## 9. **Any other issues    **

### Any other issues
- **According to best practices**: Check for up-to-date best practices and any other issues

## Review Output Format

For each issue found, provide:
1. **File and line number**: Exact location of the issue
2. **Issue category**: Which section above it falls under
3. **Severity level**: Critical/High/Medium/Low
4. **Current code**: Show the problematic code snippet
5. **Suggested fix**: Provide specific, actionable code improvement
6. **Rationale**: Brief explanation of why the change improves the code

Example:
```
**File: `src/manager.cpp`, Line 127**
**Category: Memory Management - Smart Pointers**
**Severity: High**
**Current:** `Widget* widget = new Widget(); /* ... */ delete widget;`
**Suggested:** `auto widget = std::make_unique<Widget>();`
**Rationale:** Using smart pointers prevents memory leaks and provides exception safety
```

## Priority Levels
- **Critical**: Memory safety issues, undefined behavior, security vulnerabilities
- **High**: Resource leaks, thread safety issues, significant performance problems
- **Medium**: Modern C++ best practices, code organization improvements
- **Low**: Style preferences, minor optimizations, documentation updates

## Static Analysis Integration
- **Compiler warnings**: Address all compiler warnings at high warning levels
- **Static analysis tools**: Integrate with tools like Clang Static Analyzer, PVS-Studio, or Coverity
- **Sanitizer recommendations**: Suggest running AddressSanitizer, ThreadSanitizer, or UBSan for testing
