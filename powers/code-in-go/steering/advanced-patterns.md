# Advanced Go Patterns

## Agent Directives

When assisting experienced Go developers, YOU MUST:

1. **Suggest `go:generate` for repetitive code** — Mocks, stringer, enums
2. **Recommend benchmarks for performance-sensitive code** — Not just tests
3. **Use functional options for complex constructors** — Not config structs with 10 fields
4. **Apply context correctly** — Timeouts, cancellation, never store in structs
5. **Suggest fuzzing for parsing/validation code** — `testing.F` patterns
6. **Know when to use `sync.Pool`** — High-allocation hot paths only

---

## Code Generation

### Mock Generation

```go
//go:generate mockgen -source=repository.go -destination=mock_repository.go -package=service
```

Or with `moq`:
```go
//go:generate moq -out repository_mock.go . Repository
```

### Stringer for Enums

```go
//go:generate stringer -type=Status

type Status int

const (
    StatusPending Status = iota
    StatusActive
    StatusClosed
)
```

### Interface Extraction

When user has a concrete type and needs an interface for testing:
```go
// Extract interface from concrete type
type UserService struct { ... }

// Generate minimal interface for what's actually used
type UserGetter interface {
    GetUser(ctx context.Context, id string) (*User, error)
}
```

---

## Functional Options Pattern

Use for constructors with many optional parameters:

```go
type Server struct {
    addr    string
    timeout time.Duration
    logger  Logger
    tls     *tls.Config
}

type Option func(*Server)

func WithTimeout(d time.Duration) Option {
    return func(s *Server) { s.timeout = d }
}

func WithLogger(l Logger) Option {
    return func(s *Server) { s.logger = l }
}

func WithTLS(cfg *tls.Config) Option {
    return func(s *Server) { s.tls = cfg }
}

func NewServer(addr string, opts ...Option) *Server {
    s := &Server{
        addr:    addr,
        timeout: 30 * time.Second, // sensible default
        logger:  noopLogger{},
    }
    for _, opt := range opts {
        opt(s)
    }
    return s
}
```

---

## Performance Patterns

### Benchmarking

```go
func BenchmarkProcess(b *testing.B) {
    data := setupTestData()
    b.ResetTimer() // exclude setup time
    
    for i := 0; i < b.N; i++ {
        Process(data)
    }
}

// With sub-benchmarks
func BenchmarkProcess(b *testing.B) {
    sizes := []int{10, 100, 1000, 10000}
    for _, size := range sizes {
        b.Run(fmt.Sprintf("size=%d", size), func(b *testing.B) {
            data := make([]byte, size)
            b.ResetTimer()
            for i := 0; i < b.N; i++ {
                Process(data)
            }
        })
    }
}
```

### sync.Pool for Hot Paths

```go
var bufPool = sync.Pool{
    New: func() any {
        return new(bytes.Buffer)
    },
}

func Process(data []byte) string {
    buf := bufPool.Get().(*bytes.Buffer)
    defer func() {
        buf.Reset()
        bufPool.Put(buf)
    }()
    
    // use buf...
    return buf.String()
}
```

### Slice Preallocation

```go
// Bad - grows slice repeatedly
var results []Item
for _, id := range ids {
    results = append(results, fetch(id))
}

// Good - preallocate
results := make([]Item, 0, len(ids))
for _, id := range ids {
    results = append(results, fetch(id))
}
```

### Escape Analysis Check

```bash
go build -gcflags='-m' ./...
```

---

## Advanced Testing

### Fuzzing

```go
func FuzzParseConfig(f *testing.F) {
    // Seed corpus
    f.Add([]byte(`{"name": "test"}`))
    f.Add([]byte(`{}`))
    f.Add([]byte(`invalid`))
    
    f.Fuzz(func(t *testing.T, data []byte) {
        cfg, err := ParseConfig(data)
        if err != nil {
            return // invalid input is fine
        }
        // If it parsed, it should be valid
        if cfg.Name == "" {
            t.Error("parsed config has empty name")
        }
    })
}
```

### Build Tags for Integration Tests

```go
//go:build integration

package mypackage_test

func TestDatabaseIntegration(t *testing.T) {
    // Only runs with: go test -tags=integration ./...
}
```

### Golden Files

```go
func TestRender(t *testing.T) {
    got := Render(input)
    
    golden := filepath.Join("testdata", t.Name()+".golden")
    if *update {
        os.WriteFile(golden, got, 0644)
    }
    
    want, _ := os.ReadFile(golden)
    if !bytes.Equal(got, want) {
        t.Errorf("mismatch: got %s, want %s", got, want)
    }
}
```

### t.Cleanup

```go
func TestWithTempFile(t *testing.T) {
    f, err := os.CreateTemp("", "test")
    require.NoError(t, err)
    t.Cleanup(func() { os.Remove(f.Name()) })
    
    // test using f...
}
```

---

## Context Patterns

### Timeout Propagation

```go
func Handler(w http.ResponseWriter, r *http.Request) {
    // Inherit request context with additional timeout
    ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
    defer cancel()
    
    result, err := service.Process(ctx, r.Body)
    // ...
}
```

### Graceful Shutdown

```go
func main() {
    srv := &http.Server{Addr: ":8080", Handler: handler}
    
    go func() {
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            log.Fatal(err)
        }
    }()
    
    // Wait for interrupt
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    
    // Graceful shutdown with timeout
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    
    if err := srv.Shutdown(ctx); err != nil {
        log.Printf("shutdown error: %v", err)
    }
}
```

### Context Anti-Patterns

```go
// BAD - storing context in struct
type Service struct {
    ctx context.Context // NEVER do this
}

// GOOD - pass context to methods
type Service struct{}

func (s *Service) Process(ctx context.Context, data []byte) error {
    // use ctx here
}
```

---

## Advanced Error Handling

### Custom Error Types

```go
type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation failed on %s: %s", e.Field, e.Message)
}

// Usage with errors.As
var valErr *ValidationError
if errors.As(err, &valErr) {
    // handle validation error specifically
    log.Printf("field %s invalid: %s", valErr.Field, valErr.Message)
}
```

### Structured API Errors

```go
type APIError struct {
    Code    string `json:"code"`
    Message string `json:"message"`
    Details any    `json:"details,omitempty"`
}

func (e *APIError) Error() string {
    return fmt.Sprintf("%s: %s", e.Code, e.Message)
}

// Predefined errors
var (
    ErrNotFound     = &APIError{Code: "NOT_FOUND", Message: "resource not found"}
    ErrUnauthorized = &APIError{Code: "UNAUTHORIZED", Message: "authentication required"}
)
```

---

## Module Management

### Common Commands

```bash
# Clean up unused deps
go mod tidy

# Why is this dependency here?
go mod why github.com/some/package

# Dependency graph
go mod graph | grep github.com/some/package

# Update all dependencies
go get -u ./...

# Update specific dependency
go get github.com/some/package@latest
```

### Private Modules

```bash
# In .bashrc/.zshrc or CI env
export GOPRIVATE=github.com/mycompany/*
export GOPROXY=https://proxy.golang.org,direct
```

### Replace Directives (Local Development)

```go
// go.mod - for local development only, remove before commit
replace github.com/mycompany/shared => ../shared
```

---

## Build & Debug

### Version Injection

```bash
go build -ldflags="-X main.version=1.2.3 -X main.commit=$(git rev-parse HEAD)"
```

```go
var (
    version = "dev"
    commit  = "unknown"
)

func main() {
    fmt.Printf("version: %s, commit: %s\n", version, commit)
}
```

### Profiling

```go
import _ "net/http/pprof"

func main() {
    go func() {
        log.Println(http.ListenAndServe("localhost:6060", nil))
    }()
    // ...
}
```

```bash
# CPU profile
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

# Memory profile
go tool pprof http://localhost:6060/debug/pprof/heap

# Goroutine dump
curl http://localhost:6060/debug/pprof/goroutine?debug=2
```
