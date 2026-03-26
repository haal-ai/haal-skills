# C/C++ Patterns

Detect C/C++ patterns: classes, headers, inheritance, RAII, and memory management.

## Search Patterns

### File Roles

```
# Headers
*.h
*.hpp
*.hxx
*.hh

# Implementation
*.cpp
*.cxx
*.cc
*.c

# Common naming
*_handler.h
*_handler.cpp
*_service.h
*_service.cpp
*_manager.h
*_manager.cpp
*_utils.h
*_utils.cpp
*_types.h
*_types.cpp
*_error.h
*_error.cpp

# Module patterns
src/
include/
lib/
```

### Structure Markers

```
# Class declarations
class [A-Z]*
class [A-Z]* : public
class [A-Z]* : private
class [A-Z]* : protected

# Struct declarations
struct [A-Z]*
struct [A-Z_a-z]*  # C-style

# Inheritance
: public [A-Z]*
: private [A-Z]*
: protected [A-Z]*
: virtual public

# Virtual methods
virtual
virtual void
virtual [A-Z]* = 0  // pure virtual
override
final

# Access specifiers
public:
private:
protected:
```

### Memory Management Patterns

```
# RAII patterns
std::unique_ptr<*>
std::shared_ptr<*>
std::weak_ptr<*>
std::make_unique<*>
std::make_shared<*>

# Raw pointers (legacy)
*
&
new [A-Z]*
delete
delete[]

# Smart pointer methods
.get()
.release()
.reset()
.use_count()

# Move semantics
std::move
&&  // rvalue reference
noexcept
```

### Modern C++ Patterns

```
# Templates
template<typename T>
template<class T>
template<typename... Args>

# Concepts (C++20)
concept
requires
requires expression

# constexpr
constexpr
consteval
constinit

# Auto
auto
auto&
auto&&
decltype(auto)

# Lambda
[=]
[&]
[this]
[...](auto&&... args)
```

### Error Handling Patterns

```
# Exceptions
try
catch
throw
std::exception
std::runtime_error
std::logic_error

# Error codes
errno
return -1
return NULL
return nullptr

# Result types
std::expected<T, E>
std::optional<T>
std::variant<T, E>
```

### Header Patterns

```
# Include guards
#ifndef [A-Z_]*
#define [A-Z_]*
#endif

# Pragma once
#pragma once

# Includes
#include <...>  // system
#include "..."  // local

# Forward declarations
class [A-Z]*;
struct [A-Z]*;
```

## Analysis Method

1. **Enumerate classes/structs**: Group by naming patterns
2. **Sample headers**: Read 3-5 header files per category
3. **Detect inheritance**: Check base class patterns
4. **Analyze memory management**: Check RAII vs raw pointers
5. **Check modern C++ features**: Check C++11/14/17/20 usage

## Reporting Threshold

Report only if:
- ≥3 files with same class pattern
- Mixed RAII and raw pointer usage
- Inconsistent include guard style

## Insight Template

```
INSIGHT:
  id: CPP-[n]
  title: "C++ PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - base_class: [name or none]
    - virtual_methods: [list]
    - smart_pointers: [unique_ptr|shared_ptr|none]
    - include_guards: [pragma once|#ifndef]
```

## Command Template

When a C++ pattern is detected, propose a command:

```yaml
name: "create-cpp-[pattern]"
summary: "Scaffold a new [Pattern] in C++"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new class?"
  - "Which namespace should it belong to?"
steps:
  - name: "Create header"
    description: "Create header file with include guard"
    codeSnippet: |
      #pragma once
      
      #include <memory>
      
      namespace [Namespace] {
      
      class [Name]
      {
      public:
          [Name]() = default;
          ~[Name]() = default;
          
      private:
          // members
      };
      
      } // namespace [Namespace]
  - name: "Create implementation"
    description: "Create cpp file with methods"
    codeSnippet: |
      #include "[name].h"
      
      namespace [Namespace] {
      
      // implementation
      
      } // namespace [Namespace]
```

## Common C++ Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **RAII wrapper** | `unique_ptr`, destructor, `noexcept` | Standard: "RAII pattern" |
| **PIMPL** | `Impl* pImpl`, forward declaration | Standard: "PIMPL pattern" |
| **Factory** | `static create()`, `make_unique` | Command: "create-factory" |
| **Observer** | `virtual void on*`, callback | Command: "create-observer" |
| **CRTP** | `class Derived : public Base<Derived>` | Standard: "CRTP pattern" |
