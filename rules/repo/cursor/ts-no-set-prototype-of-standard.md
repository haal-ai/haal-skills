---
description: TypeScript — do not use Object.setPrototypeOf in custom errors
globs: ["**/*.ts", "**/*.tsx"]
alwaysApply: false
---

# TypeScript: No Object.setPrototypeOf in Errors

Do not use `Object.setPrototypeOf` when defining custom errors.

## Why

`Object.setPrototypeOf` in custom error constructors causes subtle prototype chain issues with TypeScript's error handling. Extend `Error` directly instead.

## Bad

```typescript
class CustomError extends Error {
  constructor(message: string) {
    super(message);
    Object.setPrototypeOf(this, CustomError.prototype); // ❌
  }
}
```

## Good

```typescript
class CustomError extends Error {
  constructor(message: string) {
    super(message);
  }
}
```

## Languages

- TypeScript
- JavaScript
