# Rust Patterns

Detect Rust-specific patterns: traits, implementations, structs, enums, modules, and error handling.

## Search Patterns

### File Roles

```
# Modules
src/lib.rs
src/main.rs
src/**/*.rs

# Common naming conventions
*_handler.rs
*_service.rs
*_repository.rs
*_adapter.rs
*_client.rs
*_error.rs
*_types.rs
*_utils.rs
*_test.rs (unit tests alongside source)
tests/ (integration tests)
```

### Structure Markers

```
# Structs
struct [A-Z]*
pub struct [A-Z]*
struct [A-Z]*<'a>  # generic with lifetime

# Enums
enum [A-Z]*
pub enum [A-Z]*

# Traits
trait [A-Z]*
pub trait [A-Z]*
trait [A-Z]*<T>  # generic trait

# Implementations
impl [A-Z]*
impl [A-Z]*<T> for [A-Z]*  # trait implementation
impl<'a> [A-Z]*  # lifetime implementation

# Derive macros
#[derive(
#[derive(Debug)]
#[derive(Clone)]
#[derive(Serialize, Deserialize)]

# Common attributes
#[async_trait]
#[tokio::main]
#[cfg(test)]
#[allow(dead_code)]
#[must_use]
```

### Error Handling Patterns

```
# Result types
Result<T, E>
anyhow::Result<T>
thiserror::

# Error enums
enum [A-Z]*Error
impl std::error::Error for
impl Display for

# Error propagation
?
.map_err(
.context(
```

### Async Patterns

```
# Async functions
async fn
pub async fn

# Async traits
#[async_trait]
async fn execute(&self)

# Tokio patterns
tokio::spawn
tokio::main
tokio::test
```

### Module Organization

```
# Module declarations
mod [a-z_]*;
pub mod [a-z_]*;
mod [a-z_]* { }

# Re-exports
pub use
pub use crate::

# Use statements
use crate::
use std::
use anyhow::
use serde::
```

## Analysis Method

1. **Enumerate structs/traits/enums**: Group by naming patterns
2. **Sample implementations**: Read 3-5 impl blocks per trait
3. **Detect trait implementations**: Find `impl Trait for Struct` patterns
4. **Analyze error handling**: Check for custom error types vs anyhow/thiserror
5. **Check module structure**: Analyze mod declarations and re-exports

## Reporting Threshold

Report only if:
- ≥3 files with same pattern (e.g., multiple structs implementing same trait)
- ≥2 trait implementations with similar structure
- Inconsistent error handling across modules

## Insight Template

```
INSIGHT:
  id: RUST-[n]
  title: "RUST PATTERN: [TraitName] trait has [N] implementations"
  summary: "[N] structs implement [TraitName] with consistent structure."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows impl [Trait] for [Struct]
  template_markers:
    - trait_name: [name]
    - required_methods: [list]
    - common_derives: [list]
    - async: [true|false]
```

## Command Template

When a Rust pattern is detected, propose a command:

```yaml
name: "create-rust-[pattern]"
summary: "Scaffold a new [Pattern] implementation in Rust"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new struct?"
  - "Which module should it belong to?"
steps:
  - name: "Create struct"
    description: "Create struct with standard derives"
    codeSnippet: |
      #[derive(Debug, Clone)]
      pub struct [Name] {
          // fields
      }
  - name: "Implement trait"
    description: "Implement required trait methods"
    codeSnippet: |
      impl [Trait] for [Name] {
          // methods
      }
  - name: "Add to module"
    description: "Export from module if needed"
```

## Common Rust Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Adapter trait** | `impl Adapter for`, `trait Adapter` | Standard: "Adapter trait pattern" |
| **Error enum** | `enum *Error`, `impl Display for` | Command: "create-error-type" |
| **Builder pattern** | `fn with_`, `fn build()`, `#[must_use]` | Command: "create-builder" |
| **State machine** | Multiple enums with `impl From` | Standard: "State machine pattern" |
| **Repository trait** | `trait Repository`, `async fn get/save` | Command: "create-repository" |
