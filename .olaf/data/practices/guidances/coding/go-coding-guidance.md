# Go Coding Guidance

This guidance extends `[id:practices_dir]standards/universal-coding-standards.md` with Go-specific practices.

## 1. Go Idioms

### Error Handling
- **Always check errors**: Never ignore returned errors with `_`.
- **Wrap errors with context**: Use `fmt.Errorf("operation failed: %w", err)` for error wrapping.
- **Return errors, don't panic**: Reserve `panic` for truly unrecoverable situations.
- **Use sentinel errors sparingly**: Prefer error wrapping over `errors.Is()` chains.

```go
// Good
if err := doSomething(); err != nil {
    return fmt.Errorf("doSomething failed: %w", err)
}

// Bad - ignoring error
_ = doSomething()
```

### Naming Conventions
- **Package names**: Short, lowercase, no underscores (e.g., `httputil`, not `http_util`).
- **Exported names**: PascalCase for public, camelCase for private.
- **Interfaces**: Single-method interfaces use `-er` suffix (e.g., `Reader`, `Writer`, `Closer`).
- **Getters**: No `Get` prefix (use `user.Name()`, not `user.GetName()`).
- **Acronyms**: Keep consistent case (`HTTPServer` or `httpServer`, not `HttpServer`).

### Zero Values
- Design structs so zero values are useful and valid.
- Use pointer types only when nil has semantic meaning.

## 2. Project Structure

```
project/
├── cmd/                    # Main applications
│   └── appname/
│       └── main.go
├── internal/               # Private application code
│   ├── domain/             # Business logic
│   ├── repository/         # Data access
│   └── service/            # Application services
├── pkg/                    # Public library code (if any)
├── go.mod
├── go.sum
└── README.md
```

### Package Organization
- **Keep `main` minimal**: `main.go` should only wire dependencies and start the app.
- **Use `internal/`**: Prevent external imports of internal packages.
- **Avoid circular imports**: Design clean dependency graphs.

## 3. Concurrency

### Goroutines
- **Always ensure goroutines terminate**: Use context cancellation or done channels.
- **Don't start goroutines in library code** without clear ownership semantics.
- **Use `sync.WaitGroup`** to wait for goroutine completion.

### Channels
- **Prefer channels for communication**, mutexes for state protection.
- **Close channels from the sender side only**.
- **Use buffered channels** only when you understand the capacity requirements.

```go
// Good - context-aware goroutine
func worker(ctx context.Context, jobs <-chan Job) {
    for {
        select {
        case <-ctx.Done():
            return
        case job, ok := <-jobs:
            if !ok {
                return
            }
            process(job)
        }
    }
}
```

## 4. Testing

### Table-Driven Tests
- Use table-driven tests for multiple scenarios.
- Name test cases clearly.

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive numbers", 2, 3, 5},
        {"with zero", 0, 5, 5},
        {"negative numbers", -1, -2, -3},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.expected {
                t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.expected)
            }
        })
    }
}
```

### Test Organization
- Place tests in the same package (white-box) or `_test` package (black-box).
- Use `testdata/` directory for test fixtures.
- Use `t.Helper()` in test helper functions.

## 5. Dependencies

### Dependency Injection
- **Inject dependencies via constructor functions**.
- **Accept interfaces, return structs**.
- **Use functional options** for optional configuration.

```go
// Good - accepts interface
type Service struct {
    repo Repository
    log  Logger
}

func NewService(repo Repository, log Logger) *Service {
    return &Service{repo: repo, log: log}
}

// Interface for testing
type Repository interface {
    Get(ctx context.Context, id string) (*Entity, error)
    Save(ctx context.Context, e *Entity) error
}
```

## 6. Code Quality Checks

Before committing, ensure:
- [ ] `go fmt` applied
- [ ] `go vet` passes
- [ ] `golangci-lint run` passes (if configured)
- [ ] Tests pass: `go test ./...`
- [ ] No TODO comments without issue references

## References

- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [Standard Go Project Layout](https://github.com/golang-standards/project-layout)
