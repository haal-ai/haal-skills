---
applyTo: "**/*.rs"
---

# Rust: Derive Common Traits on Data Types

Always derive `Debug` on all types, and derive `Clone`, `PartialEq` on value types and DTOs.

## Why

`Debug` is essential for logging and test failures. `Clone` and `PartialEq` are needed for testing and common data manipulation. Forgetting them causes compilation errors later that require refactoring.

## Bad

```rust
pub struct User {  // ❌ missing Debug — breaks dbg!(), {:?} formatting
    pub id: String,
    pub name: String,
}

pub struct Config {  // ❌ missing Clone — can't pass to multiple consumers
    pub timeout: u64,
}
```

## Good

```rust
#[derive(Debug, Clone, PartialEq)]  // ✅ value type with full derives
pub struct User {
    pub id: String,
    pub name: String,
}

#[derive(Debug, Clone)]  // ✅ config type
pub struct Config {
    pub timeout: u64,
}
```

## Languages

- Rust

