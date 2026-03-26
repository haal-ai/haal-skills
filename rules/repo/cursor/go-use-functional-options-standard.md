---
description: Go — use functional options pattern for optional configuration
globs: ["**/*.go"]
alwaysApply: false
---

# Go: Use Functional Options for Optional Configuration

Use the functional options pattern (`type Option func(*Config)`) for structs with optional configuration fields.

## Why

Functional options avoid large constructor signatures and remain backward compatible when new options are added.

## Bad

```go
func NewServer(host string, port int, timeout time.Duration, tls bool) *Server {
    // ❌ brittle — adding a field breaks all callers
}
```

## Good

```go
type Option func(*Server)

func WithTimeout(d time.Duration) Option {
    return func(s *Server) { s.timeout = d }
}

func NewServer(host string, port int, opts ...Option) *Server { // ✅
    s := &Server{host: host, port: port}
    for _, opt := range opts { opt(s) }
    return s
}
```

## Languages

- Go
