# Go Patterns

Detect Go-specific patterns: structs, interfaces, goroutines, channels, and error handling.

## Search Patterns

### File Roles

```
# Standard layout
cmd/
internal/
pkg/
api/
configs/
go.mod
go.sum

# Common files
main.go
*.go

# Naming conventions
*_handler.go
*_service.go
*_repository.go
*_store.go
*_client.go
*_error.go
*_types.go
*_test.go
```

### Structure Markers

```
# Struct declarations
type [A-Z]* struct {
type [a-z]* struct {

# Interface declarations
type [A-Z]* interface {

# Embedded structs
struct {
    [A-Z]*
}

# Struct tags
`json:"..."`
`db:"..."`
`validate:"..."`
`yaml:"..."`
`mapstructure:"..."`
```

### Interface Patterns

```
# Interface definition
type [A-Z]* interface {
    [Method]([args]) ([returns])
}

# Interface implementation (implicit)
func ([receiver] *[Type]) [Method]([args]) ([returns])

# Common interfaces
io.Reader
io.Writer
io.Closer
http.Handler
error

# Empty interface
interface{}
any
```

### Method Patterns

```
# Value receiver
func ([receiver] [Type]) [Method]([args]) ([returns])

# Pointer receiver
func ([receiver] *[Type]) [Method]([args]) ([returns])

# Constructor pattern
func New[Type]([args]) *[Type] {
    return &[Type]{}
}

# Functional options
type Option func(*[Type])
func With[Option]([arg]) Option
```

### Error Handling Patterns

```
# Error creation
errors.New("...")
fmt.Errorf("...")
errors.Is(
errors.As(
errors.Join(

# Custom errors
type [A-Z]*Error struct {
    // fields
}
func (e *[A-Z]*Error) Error() string

# Error wrapping
if err != nil {
    return fmt.Errorf("context: %w", err)
}

# Sentinel errors
var Err[A-Z]* = errors.New("...")
```

### Concurrency Patterns

```
# Goroutines
go func() {
go [function](

# Channels
chan [Type]
chan<- [Type]  // send-only
<-chan [Type]  // receive-only
make(chan [Type])

# Select
select {
case <-[channel]:
case [channel] <- [value]:
default:
}

# Context
context.Context
context.Background()
context.TODO()
context.WithCancel(
context.WithTimeout(
context.WithDeadline(
```

### Testing Patterns

```
# Test functions
func Test[A-Z]*(t *testing.T)

# Table-driven tests
tests := []struct {
    name string
    // fields
}{
    {name: "...", /* ... */},
}
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        // test
    })
}

# Benchmarks
func Benchmark[A-Z]*(b *testing.B)

# Examples
func Example[A-Z]*()
```

## Analysis Method

1. **Enumerate structs/interfaces**: Group by naming patterns
2. **Sample implementations**: Read 3-5 files per package
3. **Detect interface patterns**: Check method signatures
4. **Analyze error handling**: Check error types and wrapping
5. **Check concurrency**: Check goroutine and channel usage

## Reporting Threshold

Report only if:
- ≥3 structs implementing same interface
- Inconsistent error handling patterns
- Mixed value/pointer receiver patterns

## Insight Template

```
INSIGHT:
  id: GO-[n]
  title: "GO PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - interface_name: [name]
    - methods: [list]
    - receiver_type: [pointer|value]
    - error_handling: [wrap|sentinel|custom]
```

## Command Template

When a Go pattern is detected, propose a command:

```yaml
name: "create-go-[pattern]"
summary: "Scaffold a new [Pattern] in Go"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new struct?"
  - "Which package should it belong to?"
steps:
  - name: "Create interface"
    description: "Define interface with methods"
    codeSnippet: |
      type [Name] interface {
          [Method]([args]) ([returns])
      }
  - name: "Create struct"
    description: "Create struct with fields"
    codeSnippet: |
      type [name] struct {
          // fields
      }
  - name: "Implement interface"
    description: "Implement methods"
    codeSnippet: |
      func (s *[name]) [Method]([args]) ([returns]) {
          // implementation
      }
  - name: "Create constructor"
    description: "Create constructor function"
    codeSnippet: |
      func New[Name]([args]) *[Name] {
          return &[Name]{
              // initialization
          }
      }
```

## Common Go Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Repository pattern** | `interface Repository`, `Get/Save` methods | Command: "create-repository" |
| **Functional options** | `type Option func`, `With*` functions | Standard: "Functional options pattern" |
| **Error wrapping** | `fmt.Errorf`, `%w`, `errors.Is/As` | Standard: "Error wrapping pattern" |
| **Worker pool** | `chan`, `goroutine`, `select` | Command: "create-worker-pool" |
| **Middleware chain** | `http.Handler`, `func(http.Handler)` | Command: "create-middleware" |
