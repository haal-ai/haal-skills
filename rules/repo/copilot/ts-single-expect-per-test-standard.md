---
applyTo: "**/*.spec.ts,**/*.test.ts,**/*.spec.tsx"
---

# TypeScript: One Expect Per Test Case

Each `it()` block should contain a single `expect()` assertion.

## Why

Multiple assertions in one test hide the root cause of failure — if the first assertion fails, the rest are never checked. Single assertions produce pinpoint failure messages.

## Bad

```typescript
it("creates a user correctly", () => {
    const user = createUser("alice", "alice@x.com");
    expect(user.name).toBe("alice");          // ❌ multiple expects
    expect(user.email).toBe("alice@x.com");
    expect(user.id).toBeDefined();
});
```

## Good

```typescript
describe("when creating a user", () => {
    let user: User;
    beforeEach(() => { user = createUser("alice", "alice@x.com"); });

    it("sets the name", () => {
        expect(user.name).toBe("alice");      // ✅ one expect
    });
    it("sets the email", () => {
        expect(user.email).toBe("alice@x.com");
    });
    it("assigns an id", () => {
        expect(user.id).toBeDefined();
    });
});
```

## Languages

- TypeScript
- JavaScript

