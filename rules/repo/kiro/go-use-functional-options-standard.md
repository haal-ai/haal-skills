---
inclusion: manual
---

# Go: Use Functional Options for Optional Configuration

Use the functional options pattern (`type Option func(*Config)`) for structs with optional configuration fields.

## Why

Functional options avoid large constructor signatures, remain backward compatible when new options are added, and are self-documenting at call sites.

## Bad

```go
func NewServer(host string, port int, timeout time.Duration, maxConns int, tls bool) *Server {
    // ❌ brittle — adding a field breaks all callers
}
```

## Good

```go
type Option func(*Server)

func WithTimeout(d time.Duration) Option {
    return func(s *Server) { s.timeout = d }
}

func WithTLS(enabled bool) Option {
    return func(s *Server) { s.tls = enabled }
}

func NewServer(host string, port int, opts ...Option) *Server {
    s := &Server{host: host, port: port}
    for _, opt := range opts {
        opt(s)
    }
    return s
}

// Call site is readable and extensible ✅
srv := NewServer("localhost", 8080, WithTimeout(30*time.Second), WithTLS(true))
```

## Languages

- Go
