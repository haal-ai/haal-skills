---
inclusion: manual
---

# TypeScript: Use Intersection Types for DTO Enrichment

When defining a presentation DTO that enriches a domain type, use an intersection type (`DomainType & { extraField: T }`) instead of manually re-declaring the domain type's fields.

## Why

Intersection types ensure structural drift is caught at compile time. Re-declaring fields creates duplicated definitions that silently diverge from the domain.

## Bad

```typescript
// Manually re-declaring domain fields ❌
interface UserDTO {
  id: string;
  name: string;
  email: string;
  role: string; // extra field
}
```

## Good

```typescript
// Intersection type — drift caught at compile time ✅
type UserDTO = User & { role: string };
```

## Languages

- TypeScript
