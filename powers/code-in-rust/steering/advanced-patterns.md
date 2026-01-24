# Advanced Rust Patterns

## Agent Directives

When assisting experienced Rust developers, YOU MUST:

1. **Suggest derive macros for common traits** — Debug, Clone, PartialEq, Serialize
2. **Recommend benchmarks for performance-sensitive code** — `criterion` crate
3. **Use builder pattern for complex constructors** — Not structs with 10 fields
4. **Apply lifetimes correctly** — Elision when possible, explicit when needed
5. **Suggest property-based testing for parsing/validation** — `proptest` patterns
6. **Know when to use `Cow<'_, str>`** — Avoid unnecessary allocations

---

## Builder Pattern

Use for constructors with many optional parameters:

```rust
#[derive(Debug, Clone)]
pub struct Server {
    addr: String,
    timeout: Duration,
    max_connections: usize,
    tls_config: Option<TlsConfig>,
}

#[derive(Default)]
pub struct ServerBuilder {
    addr: Option<String>,
    timeout: Duration,
    max_connections: usize,
    tls_config: Option<TlsConfig>,
}

impl ServerBuilder {
    pub fn new() -> Self {
        Self {
            timeout: Duration::from_secs(30),
            max_connections: 100,
            ..Default::default()
        }
    }

    pub fn addr(mut self, addr: impl Into<String>) -> Self {
        self.addr = Some(addr.into());
        self
    }

    pub fn timeout(mut self, timeout: Duration) -> Self {
        self.timeout = timeout;
        self
    }

    pub fn max_connections(mut self, max: usize) -> Self {
        self.max_connections = max;
        self
    }

    pub fn tls(mut self, config: TlsConfig) -> Self {
        self.tls_config = Some(config);
        self
    }

    pub fn build(self) -> Result<Server, BuilderError> {
        Ok(Server {
            addr: self.addr.ok_or(BuilderError::MissingAddr)?,
            timeout: self.timeout,
            max_connections: self.max_connections,
            tls_config: self.tls_config,
        })
    }
}

// Usage
let server = ServerBuilder::new()
    .addr("127.0.0.1:8080")
    .timeout(Duration::from_secs(60))
    .build()?;
```

### Using `typed-builder` Crate

```rust
use typed_builder::TypedBuilder;

#[derive(TypedBuilder)]
pub struct Server {
    addr: String,
    #[builder(default = Duration::from_secs(30))]
    timeout: Duration,
    #[builder(default = 100)]
    max_connections: usize,
    #[builder(default, setter(strip_option))]
    tls_config: Option<TlsConfig>,
}

// Usage
let server = Server::builder()
    .addr("127.0.0.1:8080".to_string())
    .timeout(Duration::from_secs(60))
    .build();
```

---

## Performance Patterns

### Benchmarking with Criterion

```rust
// benches/benchmark.rs
use criterion::{black_box, criterion_group, criterion_main, Criterion, BenchmarkId};

fn benchmark_process(c: &mut Criterion) {
    let data = setup_test_data();
    
    c.bench_function("process", |b| {
        b.iter(|| process(black_box(&data)))
    });
}

// With different input sizes
fn benchmark_process_sizes(c: &mut Criterion) {
    let mut group = c.benchmark_group("process");
    
    for size in [10, 100, 1000, 10000] {
        let data = vec![0u8; size];
        group.bench_with_input(
            BenchmarkId::from_parameter(size),
            &data,
            |b, data| b.iter(|| process(black_box(data))),
        );
    }
    group.finish();
}

criterion_group!(benches, benchmark_process, benchmark_process_sizes);
criterion_main!(benches);
```

### Zero-Copy with `Cow`

```rust
use std::borrow::Cow;

fn process_name(name: &str) -> Cow<'_, str> {
    if name.contains(' ') {
        // Need to allocate
        Cow::Owned(name.replace(' ', "_"))
    } else {
        // No allocation needed
        Cow::Borrowed(name)
    }
}

// Works with both borrowed and owned
fn greet(name: Cow<'_, str>) {
    println!("Hello, {}!", name);
}
```

### Avoiding Allocations

```rust
// Bad - allocates on every call
fn get_default() -> String {
    "default".to_string()
}

// Good - returns static reference
fn get_default() -> &'static str {
    "default"
}

// Bad - grows vec repeatedly
let mut results = Vec::new();
for item in items {
    results.push(process(item));
}

// Good - preallocate
let mut results = Vec::with_capacity(items.len());
for item in items {
    results.push(process(item));
}

// Better - use iterator
let results: Vec<_> = items.iter().map(process).collect();
```

### String Building

```rust
// Bad - multiple allocations
let result = "Hello, ".to_string() + &name + "!";

// Good - format macro
let result = format!("Hello, {}!", name);

// Best for loops - preallocate
let mut result = String::with_capacity(estimated_size);
for item in items {
    result.push_str(&item.to_string());
    result.push('\n');
}
```

---

## Advanced Testing

### Property-Based Testing with Proptest

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn test_parse_roundtrip(s in "\\PC*") {
        if let Ok(parsed) = parse(&s) {
            let serialized = serialize(&parsed);
            let reparsed = parse(&serialized).unwrap();
            prop_assert_eq!(parsed, reparsed);
        }
    }

    #[test]
    fn test_add_commutative(a in any::<i32>(), b in any::<i32>()) {
        prop_assert_eq!(add(a, b), add(b, a));
    }
}
```

### Custom Strategies

```rust
use proptest::prelude::*;

fn valid_email() -> impl Strategy<Value = String> {
    (
        "[a-z]{1,10}",      // local part
        "[a-z]{1,10}",      // domain
        "(com|org|net)",    // tld
    )
        .prop_map(|(local, domain, tld)| format!("{}@{}.{}", local, domain, tld))
}

proptest! {
    #[test]
    fn test_email_validation(email in valid_email()) {
        prop_assert!(validate_email(&email).is_ok());
    }
}
```

### Snapshot Testing with Insta

```rust
use insta::assert_snapshot;

#[test]
fn test_render_output() {
    let output = render(&input);
    assert_snapshot!(output);
}

#[test]
fn test_json_output() {
    let data = process(&input);
    insta::assert_json_snapshot!(data);
}
```

### Test Fixtures with rstest

```rust
use rstest::{rstest, fixture};

#[fixture]
fn database() -> TestDb {
    TestDb::new()
}

#[rstest]
fn test_user_creation(database: TestDb) {
    let user = database.create_user("test@example.com");
    assert!(user.is_ok());
}

#[rstest]
#[case("valid@email.com", true)]
#[case("invalid", false)]
#[case("@nodomain.com", false)]
fn test_email_validation(#[case] email: &str, #[case] expected: bool) {
    assert_eq!(is_valid_email(email), expected);
}
```

---

## Async Patterns

### Graceful Shutdown

```rust
use tokio::signal;
use tokio::sync::broadcast;

async fn run_server() -> anyhow::Result<()> {
    let (shutdown_tx, _) = broadcast::channel(1);
    
    let server = Server::new(shutdown_tx.subscribe());
    let server_handle = tokio::spawn(server.run());
    
    // Wait for shutdown signal
    signal::ctrl_c().await?;
    println!("Shutdown signal received");
    
    // Notify all tasks
    let _ = shutdown_tx.send(());
    
    // Wait for server to finish
    server_handle.await??;
    
    Ok(())
}

struct Server {
    shutdown: broadcast::Receiver<()>,
}

impl Server {
    async fn run(mut self) -> anyhow::Result<()> {
        loop {
            tokio::select! {
                _ = self.shutdown.recv() => {
                    println!("Server shutting down");
                    break;
                }
                result = self.accept_connection() => {
                    // Handle connection
                }
            }
        }
        Ok(())
    }
}
```

### Timeout and Retry

```rust
use tokio::time::{timeout, Duration};

async fn fetch_with_retry(url: &str, max_retries: u32) -> anyhow::Result<Response> {
    let mut last_error = None;
    
    for attempt in 0..max_retries {
        match timeout(Duration::from_secs(10), fetch(url)).await {
            Ok(Ok(response)) => return Ok(response),
            Ok(Err(e)) => {
                last_error = Some(e);
                tokio::time::sleep(Duration::from_millis(100 * 2_u64.pow(attempt))).await;
            }
            Err(_) => {
                last_error = Some(anyhow::anyhow!("request timed out"));
            }
        }
    }
    
    Err(last_error.unwrap_or_else(|| anyhow::anyhow!("unknown error")))
}
```

### Concurrent Processing

```rust
use futures::stream::{self, StreamExt};

async fn process_all(items: Vec<Item>) -> Vec<Result<Output, Error>> {
    stream::iter(items)
        .map(|item| async move { process(item).await })
        .buffer_unordered(10)  // Max 10 concurrent
        .collect()
        .await
}
```

---

## Error Handling Patterns

### Custom Error Types with thiserror

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ServiceError {
    #[error("user not found: {0}")]
    UserNotFound(u64),
    
    #[error("validation failed: {field} - {message}")]
    Validation { field: String, message: String },
    
    #[error("database error")]
    Database(#[from] sqlx::Error),
    
    #[error("external service error")]
    External(#[source] reqwest::Error),
}

// Usage
fn get_user(id: u64) -> Result<User, ServiceError> {
    users.get(&id)
        .cloned()
        .ok_or(ServiceError::UserNotFound(id))
}
```

### Error Context with anyhow

```rust
use anyhow::{Context, Result};

fn load_config(path: &Path) -> Result<Config> {
    let content = fs::read_to_string(path)
        .with_context(|| format!("failed to read config from {}", path.display()))?;
    
    let config: Config = toml::from_str(&content)
        .context("failed to parse config file")?;
    
    config.validate()
        .context("config validation failed")?;
    
    Ok(config)
}
```

---

## Macro Patterns

### Declarative Macros

```rust
macro_rules! map {
    ($($key:expr => $value:expr),* $(,)?) => {{
        let mut m = std::collections::HashMap::new();
        $(m.insert($key, $value);)*
        m
    }};
}

// Usage
let scores = map! {
    "Alice" => 100,
    "Bob" => 85,
};
```

### Derive Macros (proc-macro)

When to suggest external derive macros:
- `serde` - Serialization/deserialization
- `thiserror` - Error types
- `typed-builder` - Builder pattern
- `derive_more` - Common trait implementations
- `strum` - Enum utilities

---

## Module Management

### Common Commands

```bash
# Format code
cargo fmt

# Lint with clippy
cargo clippy -- -W clippy::pedantic

# Check without building
cargo check

# Build release
cargo build --release

# Run tests
cargo test

# Run specific test
cargo test test_name

# Generate docs
cargo doc --open

# Update dependencies
cargo update

# Check for outdated deps
cargo outdated  # requires cargo-outdated

# Security audit
cargo audit  # requires cargo-audit
```

### Workspace Setup

```toml
# Cargo.toml (workspace root)
[workspace]
members = [
    "crates/core",
    "crates/api",
    "crates/cli",
]

[workspace.dependencies]
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
anyhow = "1"
thiserror = "1"
```

```toml
# crates/core/Cargo.toml
[dependencies]
tokio = { workspace = true }
serde = { workspace = true }
```

---

## Build & Debug

### Version Injection

```toml
# Cargo.toml
[package]
version = "0.1.0"
```

```rust
const VERSION: &str = env!("CARGO_PKG_VERSION");

fn main() {
    println!("Version: {}", VERSION);
}
```

### Feature Flags

```toml
# Cargo.toml
[features]
default = ["json"]
json = ["serde_json"]
full = ["json", "yaml", "toml"]
```

```rust
#[cfg(feature = "json")]
pub mod json {
    // JSON support
}
```

### Profiling

```bash
# CPU profiling with flamegraph
cargo install flamegraph
cargo flamegraph --bin myapp

# Memory profiling with heaptrack (Linux)
heaptrack ./target/release/myapp
heaptrack_gui heaptrack.myapp.*.gz
```
