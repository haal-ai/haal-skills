# Rust Coding Guidance

## Agent Directives

YOU MUST apply these rules to ALL Rust code you generate:

1. **NEVER use `.unwrap()` in production** — Use `?`, `match`, or `.expect("reason")`
2. **ALWAYS add error context** — Use `anyhow::Context` or `map_err`
3. **Prefer borrows over owned types** — `&str` not `String`, `&[T]` not `Vec<T>` in params
4. **Use derive macros** — `#[derive(Debug, Clone, PartialEq)]` where appropriate
5. **Follow naming conventions** — `snake_case` functions, `PascalCase` types, `SCREAMING_SNAKE` constants
6. **Async code must be cancellation-safe** — Use `tokio::select!` carefully

---

## Reference: Rust Idioms

### Error Handling

- **Never use `.unwrap()` in production**: Reserve for tests or when panic is truly intended.
- **Use `?` operator**: Propagate errors cleanly up the call stack.
- **Add context to errors**: Use `anyhow::Context` or custom error types.
- **Library vs Application errors**:
  - Libraries: Use `thiserror` for typed errors
  - Applications: Use `anyhow` for flexible error handling

```rust
// Good - with context
fn read_config(path: &Path) -> anyhow::Result<Config> {
    let content = fs::read_to_string(path)
        .with_context(|| format!("failed to read config from {}", path.display()))?;
    toml::from_str(&content)
        .context("failed to parse config")
}

// Bad - unwrap in production
fn read_config(path: &Path) -> Config {
    let content = fs::read_to_string(path).unwrap(); // NEVER
    toml::from_str(&content).unwrap()
}
```

### Ownership & Borrowing

- **Prefer borrows in function parameters**: Accept `&str` not `String`, `&[T]` not `Vec<T>`.
- **Return owned types**: Functions typically return owned data.
- **Use `Cow` for flexibility**: When you might or might not need to clone.
- **Clone consciously**: Only when necessary, not as a default.

```rust
// Good - accepts borrow
fn process(data: &str) -> String {
    data.to_uppercase()
}

// Bad - forces caller to own
fn process(data: String) -> String {
    data.to_uppercase()
}
```

### Naming Conventions

- **Functions/methods**: `snake_case` (e.g., `process_data`, `get_user`)
- **Types/traits**: `PascalCase` (e.g., `UserService`, `Repository`)
- **Constants**: `SCREAMING_SNAKE_CASE` (e.g., `MAX_CONNECTIONS`)
- **Lifetimes**: Short lowercase (e.g., `'a`, `'de`)
- **Type parameters**: Single uppercase or descriptive (e.g., `T`, `Item`)

### Option & Result Patterns

- **Use combinators**: `map`, `and_then`, `unwrap_or_default`
- **Avoid nested matching**: Chain combinators instead
- **Use `ok_or` / `ok_or_else`**: Convert `Option` to `Result`

```rust
// Good - combinator chain
fn get_username(id: u64) -> Option<String> {
    users.get(&id)
        .filter(|u| u.is_active)
        .map(|u| u.name.clone())
}

// Verbose - nested matching
fn get_username(id: u64) -> Option<String> {
    match users.get(&id) {
        Some(user) => {
            if user.is_active {
                Some(user.name.clone())
            } else {
                None
            }
        }
        None => None,
    }
}
```

## 2. Project Structure

```
project/
├── src/
│   ├── main.rs           # Binary entry point
│   ├── lib.rs            # Library root (if both bin and lib)
│   ├── domain/           # Business logic
│   │   ├── mod.rs
│   │   └── user.rs
│   ├── repository/       # Data access
│   │   ├── mod.rs
│   │   └── user_repo.rs
│   └── service/          # Application services
│       ├── mod.rs
│       └── user_service.rs
├── tests/                # Integration tests
│   └── integration_test.rs
├── benches/              # Benchmarks
│   └── benchmark.rs
├── Cargo.toml
├── Cargo.lock
└── README.md
```

### Module Organization

- **Keep `main.rs` minimal**: Wire dependencies and start the app.
- **Use `mod.rs` or inline modules**: Organize by responsibility.
- **Avoid circular dependencies**: Design clean module graphs.
- **Re-export public API**: Use `pub use` in `lib.rs` for clean API surface.

## 3. Concurrency

### Threads & Channels

- **Use `std::sync::mpsc`** for message passing between threads.
- **Prefer `Arc<Mutex<T>>`** over raw pointers for shared state.
- **Use `parking_lot`** for faster mutexes when needed.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let handles: Vec<_> = (0..10).map(|_| {
    let counter = Arc::clone(&counter);
    thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    })
}).collect();

for handle in handles {
    handle.join().unwrap();
}
```

### Async/Await

- **Use `tokio` or `async-std`** as async runtime.
- **Avoid blocking in async code**: Use `spawn_blocking` for CPU-bound work.
- **Be careful with `select!`**: Ensure cancellation safety.
- **Use `tokio::sync`** primitives in async code, not `std::sync`.

```rust
use tokio::time::{timeout, Duration};

async fn fetch_with_timeout(url: &str) -> anyhow::Result<String> {
    timeout(Duration::from_secs(10), fetch(url))
        .await
        .context("request timed out")?
}
```

## 4. Testing

### Unit Tests

Place tests in the same file with `#[cfg(test)]` module:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_positive() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, -2), -3);
    }

    #[test]
    fn test_add_zero() {
        assert_eq!(add(0, 5), 5);
    }
}
```

### Test Organization

- **Unit tests**: In `#[cfg(test)]` module within source files.
- **Integration tests**: In `tests/` directory.
- **Use `rstest`** for parameterized tests.
- **Use `mockall`** for mocking traits.

### Parameterized Tests with rstest

```rust
use rstest::rstest;

#[rstest]
#[case(2, 3, 5)]
#[case(0, 5, 5)]
#[case(-1, -2, -3)]
fn test_add(#[case] a: i32, #[case] b: i32, #[case] expected: i32) {
    assert_eq!(add(a, b), expected);
}
```

## 5. Dependencies & Traits

### Dependency Injection

- **Define traits for external dependencies**.
- **Accept trait bounds, return concrete types**.
- **Use `impl Trait` for simple cases**.

```rust
// Define trait for dependency
pub trait UserRepository {
    fn get(&self, id: u64) -> Option<User>;
    fn save(&self, user: &User) -> anyhow::Result<()>;
}

// Service accepts trait
pub struct UserService<R: UserRepository> {
    repo: R,
}

impl<R: UserRepository> UserService<R> {
    pub fn new(repo: R) -> Self {
        Self { repo }
    }

    pub fn get_user(&self, id: u64) -> Option<User> {
        self.repo.get(id)
    }
}
```

### Common Derive Macros

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash)]  // For most types
#[derive(Default)]                             // When zero-value makes sense
#[derive(serde::Serialize, serde::Deserialize)] // For serialization
```

## 6. Code Quality Checks

Before committing, ensure:

- [ ] `cargo fmt` applied
- [ ] `cargo clippy` passes (no warnings)
- [ ] `cargo test` passes
- [ ] `cargo doc` builds without warnings
- [ ] No `TODO` comments without issue references
- [ ] No `.unwrap()` in non-test code

### Clippy Configuration

In `Cargo.toml` or `.cargo/config.toml`:
```toml
[lints.clippy]
unwrap_used = "warn"
expect_used = "warn"
pedantic = "warn"
```

## References

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
- [Effective Rust](https://www.lurklurk.org/effective-rust/)
