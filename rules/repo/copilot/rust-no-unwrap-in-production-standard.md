---
applyTo: "**/*.rs"
---

# Rust: No unwrap() in Production Code

Do not use `.unwrap()` or `.expect()` outside of tests and examples. Use `?`, `if let`, or `match` instead.

## Why

`.unwrap()` panics on `None`/`Err` at runtime, crashing the process. Production code must handle errors explicitly.

## Bad

```rust
fn get_user(id: &str) -> User {
    let user = db.find(id).unwrap(); // ❌ panics if not found
    user
}
```

## Good

```rust
fn get_user(id: &str) -> Result<User, AppError> {
    let user = db.find(id)?; // ✅ propagates error to caller
    Ok(user)
}
```

## Exception

`.unwrap()` and `.expect()` are acceptable in:
- `#[cfg(test)]` blocks
- `fn main()` after explicit validation
- `const` context where the value is statically known

## Languages

- Rust

