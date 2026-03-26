---
description: TypeScript � use verb-first test names, not should
globs: ["**/*.spec.ts","**/*.test.ts"]
alwaysApply: false
---

# TypeScript: Use Verb-First Test Names

Start test names with an action verb — not "should". Use `it("returns ...")` not `it("should return ...")`.

## Why

Verb-first names read as specifications: "returns the user", "throws when id is missing". "should" adds a word without adding meaning.

## Bad

```typescript
it("should return the user when found", () => { ... });  // ❌
it("should throw an error when id is missing", () => { ... });  // ❌
```

## Good

```typescript
it("returns the user when found", () => { ... });  // ✅
it("throws when id is missing", () => { ... });  // ✅
```

## Languages

- TypeScript
- JavaScript

