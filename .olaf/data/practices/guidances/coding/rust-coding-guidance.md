# Rust Coding Guidance

This guidance extends `[id:practices_dir]standards/universal-coding-standards.md` with Rust-specific practices.

## 1. Rust Idioms

### Error Handling
- Prefer returning `Result<T, E>`; avoid panics for recoverable errors.
- Avoid `unwrap()` / `expect()` in production code. Use them in tests or when a precondition is truly guaranteed and documented.
- Add context at boundaries:
  - If using `anyhow`, prefer `Context` (`.context("...")?`).
  - If defining a library API, prefer a typed error enum via `thiserror`.
- Use `?` for propagation, but keep the call site readable with small helper functions.

### Ownership & Borrowing
- Prefer borrowing (`&T`, `&str`) in function parameters unless ownership transfer is required.
- Avoid unnecessary clones; clone only at API boundaries or when semantics require it.
- Prefer iterators and slices (`&[T]`) for collections.

### Naming & Style
- Follow `rustfmt` defaults.
- Use `snake_case` for functions/variables/modules, `CamelCase` for types/traits, `SCREAMING_SNAKE_CASE` for constants.
- Keep modules cohesive; avoid large "god modules".

## 2. Project Structure

Typical Rust layout:

```
project/
├── Cargo.toml
├── src/
│   ├── lib.rs            # Library crate entry (if applicable)
│   ├── main.rs           # Binary crate entry (if applicable)
│   ├── domain/           # Domain types and business rules
│   ├── service/          # Application services
│   ├── repo/             # Repository traits + implementations
│   └── adapters/         # External integrations (db/http/fs)
├── tests/                # Integration tests
└── README.md
```

Guidance:
- Keep `main.rs` thin: wire dependencies and call into services.
- Use traits for dependency injection: accept trait objects or generics depending on needs.
- Keep external IO (db/fs/http) behind injected adapters.

## 3. Dependency Injection (DI)

- Define traits for collaborators (e.g., `UserRepository`).
- Prefer constructor functions to build services.
- Keep trait contracts narrow and test-friendly.

Example:

```rust
pub trait UserRepository {
    fn get(&self, id: &str) -> anyhow::Result<User>;
}

pub struct UserService<R> {
    repo: R,
}

impl<R: UserRepository> UserService<R> {
    pub fn new(repo: R) -> Self {
        Self { repo }
    }
}
```

## 4. Concurrency

- Prefer ownership-transfer patterns to avoid shared mutable state.
- If you must share state, use `Arc<Mutex<T>>` / `Arc<RwLock<T>>` carefully and keep lock scope small.
- For async code, avoid blocking calls in async tasks; use appropriate async primitives.

## 5. Testing

- Prefer unit tests close to the code (`mod tests { ... }`).
- Use integration tests in `tests/` for boundary-level verification.
- Use table-driven style with helper structs and subtests patterns.

Example:

```rust
#[test]
fn validate_email_cases() {
    struct Case {
        name: &'static str,
        email: &'static str,
        ok: bool,
    }

    let cases = [
        Case { name: "empty", email: "", ok: false },
        Case { name: "missing at", email: "abc", ok: false },
        Case { name: "basic", email: "a@b", ok: true },
    ];

    for case in cases {
        let result = validate_email(case.email);
        assert_eq!(result.is_ok(), case.ok, "{}", case.name);
    }
}
```

## 6. Quality Checks

Before committing, ensure:
- [ ] `cargo fmt` is clean
- [ ] `cargo clippy` is clean (or lints are justified)
- [ ] `cargo test` passes
- [ ] No TODO comments without an issue reference

## References

- The Rust Book: https://doc.rust-lang.org/book/
- Rust API Guidelines: https://rust-lang.github.io/api-guidelines/
- Rust Clippy: https://github.com/rust-lang/rust-clippy
