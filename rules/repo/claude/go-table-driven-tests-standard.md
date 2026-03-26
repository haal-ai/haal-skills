# Go: Use Table-Driven Tests

Structure tests as table-driven using a slice of structs with a `name` field and `t.Run`.

## Why

Table-driven tests reduce duplication, make it easy to add cases, and produce clear failure messages via subtest names.

## Bad

```go
func TestAdd(t *testing.T) {
    if Add(1, 2) != 3 {
        t.Error("expected 3")
    }
    if Add(0, 0) != 0 {
        t.Error("expected 0")
    }
}
```

## Good

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {name: "positive numbers", a: 1, b: 2, expected: 3},
        {name: "zeros", a: 0, b: 0, expected: 0},
        {name: "negative", a: -1, b: 1, expected: 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.expected {
                t.Errorf("got %d, want %d", got, tt.expected)
            }
        })
    }
}
```

## Languages

- Go
