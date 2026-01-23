# Go Code Review Standards

## Go-Specific Review Areas

### 1. Go Idioms and Best Practices

#### Go Style Guide Compliance
- **gofmt**: Code should be formatted with gofmt or goimports
- **Naming Conventions**: 
  - Packages: lowercase, single word (e.g., `http`, `json`)
  - Variables/Functions: camelCase (e.g., `userID`, `getUserData`)
  - Constants: CamelCase (e.g., `MaxRetries`) or camelCase for private
  - Interfaces: Single method interfaces end in -er (e.g., `Reader`, `Writer`)

#### Code Organization
- **Package Structure**: Logical grouping, avoid deep nesting
- **File Naming**: Clear, descriptive names (snake_case acceptable)
- **Import Grouping**: Standard library, third-party, local packages
- **Function Length**: Keep functions focused and reasonably sized

### 2. Error Handling

#### Error Handling Best Practices
- **Error Checking**: Check every error, don't ignore with `_`
- **Error Wrapping**: Use `fmt.Errorf` with `%w` verb for error wrapping
- **Error Types**: Create custom error types for specific error conditions
- **Error Messages**: Provide clear, actionable error messages

```go
// Good
if err != nil {
    return fmt.Errorf("failed to connect to database: %w", err)
}

// Bad
if err != nil {
    return err // No context
}
```

#### Panic Usage
- **Avoid Panic**: Use panic only for truly exceptional situations
- **Recovery**: If using panic, implement proper recovery
- **Initialization**: Panic acceptable during init() for setup failures

### 3. Memory Management and Performance

#### Memory Efficiency
- **Slice Allocation**: Pre-allocate slices when size is known
- **String Building**: Use strings.Builder for concatenating multiple strings
- **Pointer Usage**: Use pointers for large structs, avoid for small types
- **Goroutine Leaks**: Ensure goroutines terminate properly

#### Performance Patterns
- **Buffered Channels**: Use buffered channels appropriately
- **sync.Pool**: Use for frequently allocated/deallocated objects
- **Interface Efficiency**: Prefer smaller interfaces

### 4. Concurrency

#### Goroutines
- **Goroutine Management**: Ensure goroutines have a way to terminate
- **Context Usage**: Use context.Context for cancellation and timeouts
- **WaitGroups**: Proper use of sync.WaitGroup for coordination
- **Avoid Race Conditions**: Proper synchronization with channels or mutexes

#### Channels
- **Channel Closing**: Close channels from sender side
- **Select Statements**: Use select for non-blocking operations
- **Channel Direction**: Use directional channels in function parameters

```go
// Good
func producer(ch chan<- int) { /* send only */ }
func consumer(ch <-chan int) { /* receive only */ }
```

#### Mutexes and Atomics
- **Mutex Usage**: Prefer channels over mutexes when possible
- **RWMutex**: Use RWMutex for read-heavy workloads
- **Atomic Operations**: Use sync/atomic for simple counters

### 5. Testing

#### Test Structure
- **Test Naming**: TestFunctionName or TestFunctionName_Scenario
- **Table Tests**: Use table-driven tests for multiple scenarios
- **Subtests**: Use t.Run() for grouping related test cases
- **Test Helpers**: Mark helper functions with t.Helper()

#### Test Coverage
- **Critical Paths**: Ensure business logic is well tested
- **Error Paths**: Test error conditions and edge cases
- **Examples**: Include testable examples in documentation

#### Benchmarks and Profiling
- **Benchmark Tests**: Write benchmarks for performance-critical code
- **Profiling**: Use go tool pprof for performance analysis
- **Memory Benchmarks**: Check memory allocations in benchmarks

### 6. Documentation

#### Code Documentation
- **Package Comments**: Every package should have a package comment
- **Function Comments**: Public functions should be documented
- **Example Code**: Provide examples for complex APIs
- **README**: Clear README with usage examples

#### Comment Style
- **Comment Format**: Start with function/type name
- **Avoid Obvious**: Don't comment obvious code
- **WHY not WHAT**: Explain reasoning, not implementation

### 7. Dependencies and Modules

#### Module Management
- **go.mod**: Keep dependencies up to date and minimal
- **Semantic Versioning**: Follow semver for your own modules
- **Vendor Directory**: Use vendor/ directory when necessary
- **Go Version**: Specify minimum Go version in go.mod

#### Security
- **Input Validation**: Validate all external input
- **SQL Injection**: Use parameterized queries
- **Cryptography**: Use proven cryptographic libraries
- **Secrets**: Don't hardcode secrets, use environment variables

### 8. Standard Library Usage

#### Common Patterns
- **HTTP Clients**: Proper timeout and context usage
- **JSON Handling**: Proper struct tags and error handling
- **File Operations**: Always close files, handle errors
- **Database**: Use prepared statements, handle connection pooling

#### Context Usage
- **Context Propagation**: Pass context through call chains
- **Timeout Handling**: Use context.WithTimeout for operations
- **Cancellation**: Respect context cancellation

### 9. Go-Specific Anti-patterns

#### Avoid These Patterns
- **Empty Interface**: Avoid `interface{}` when possible, use generics (Go 1.18+)
- **Nil Pointer Dereference**: Check for nil before dereferencing
- **Range Variable Capture**: Be careful with goroutines in loops
- **Slice Header Modification**: Understand slice header semantics

```go
// Bad - captures loop variable
for _, item := range items {
    go func() {
        process(item) // Wrong: captures last item
    }()
}

// Good
for _, item := range items {
    go func(item Item) {
        process(item)
    }(item)
}
```

### Severity Guidelines for Go

#### HIGH Severity
- Race conditions in concurrent code
- Goroutine leaks
- Resource leaks (unclosed files, connections)
- Security vulnerabilities (SQL injection, hardcoded secrets)
- Nil pointer dereferences
- Improper error handling leading to crashes

#### MEDIUM Severity
- Missing error checks
- Inefficient memory usage (unnecessary allocations)
- Poor concurrency patterns (mutex over channels when inappropriate)
- Missing context propagation
- Non-idiomatic Go code patterns
- Performance issues in hot paths

#### LOW Severity
- Code formatting issues (should be caught by gofmt)
- Missing documentation for exported functions
- Inconsistent naming conventions
- Unnecessary complexity where simpler solutions exist
- Missing examples for public APIs