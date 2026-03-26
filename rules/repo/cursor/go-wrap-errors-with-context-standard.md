---
description: Go — wrap errors with context using fmt.Errorf and %w
globs: ["**/*.go"]
alwaysApply: false
---

# Go: Wrap Errors with Context

Always wrap errors with `fmt.Errorf("context: %w", err)` instead of returning them bare.

## Why

Bare `return err` loses call-stack context, making debugging hard. The `%w` verb wraps the original error so `errors.Is` and `errors.As` still work.

## Bad

```go
func GetUser(id string) (*User, error) {
    u, err := db.Query(id)
    if err != nil {
        return nil, err // ❌
    }
    return u, nil
}
```

## Good

```go
func GetUser(id string) (*User, error) {
    u, err := db.Query(id)
    if err != nil {
        return nil, fmt.Errorf("GetUser %s: %w", id, err) // ✅
    }
    return u, nil
}
```

## Languages

- Go
