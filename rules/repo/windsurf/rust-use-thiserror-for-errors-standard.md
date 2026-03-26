# Rust: Use thiserror for Custom Error Types

Use the `thiserror` crate to derive `Error` implementations instead of implementing `Display` and `Error` manually.

## Why

Manual `impl Display for MyError` is verbose and error-prone. `thiserror` generates correct, idiomatic implementations and supports error wrapping via `#[from]`.

## Bad

```rust
#[derive(Debug)]
pub enum AppError {
    Io(std::io::Error),
    Parse(String),
}

impl std::fmt::Display for AppError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            AppError::Io(e) => write!(f, "IO error: {}", e), // ❌ manual boilerplate
            AppError::Parse(s) => write!(f, "Parse error: {}", s),
        }
    }
}

impl std::error::Error for AppError {}
```

## Good

```rust
use thiserror::Error;

#[derive(Debug, Error)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error), // ✅ automatic From impl
    #[error("Parse error: {0}")]
    Parse(String),
}
```

## Languages

- Rust
