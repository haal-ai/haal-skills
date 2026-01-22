# Pet Clinic API — Functional Specification (Detailed)

## 1) Metadata & traceability
- Demand folder:
- Demand input:
- Approved decisions:
- Spec timestamp (YYYYMMDD-HHmm):
- Target audience:

## 2) Goals, scope, and non-goals

## 3) Roles & permissions (RBAC)
Provide a role-to-capability mapping and an endpoint-level RBAC matrix.

## 4) Domain model

### 4.1 Entities & relationships (Mermaid)
```mermaid
classDiagram
  class Owner {
    id
    firstName
    lastName
    email
    phone
  }
  class Pet {
    id
    ownerId
    name
    type
    birthDate
  }
  class Vet {
    id
    name
    active
  }
  class Appointment {
    id
    petId
    vetId
    startTime
    durationMinutes
    status
  }
  class Visit {
    id
    petId
    vetId
    appointmentId
    visitTime
    notes
    lastEditedAt
    lastEditedBy
  }

  Owner "1" --> "0..*" Pet
  Pet "1" --> "0..*" Appointment
  Pet "1" --> "0..*" Visit
  Vet "1" --> "0..*" Appointment
  Appointment "0..1" --> "0..1" Visit
```

### 4.2 Appointment lifecycle (Mermaid)
```mermaid
stateDiagram-v2
  [*] --> BOOKED
  BOOKED --> CANCELLED
  BOOKED --> COMPLETED
  BOOKED --> NO_SHOW
  CANCELLED --> [*]
  COMPLETED --> [*]
  NO_SHOW --> [*]
```

## 5) Key business rules (testable)
Include validation rules, constraints, and expected error behaviors.

## 6) Core workflows (Mermaid)

### 6.1 Happy path: create owner → add pet → book appointment → record visit
```mermaid
sequenceDiagram
  participant R as Reception
  participant API as API
  participant V as Vet

  R->>API: POST /owners
  API-->>R: 201 Owner
  R->>API: POST /owners/{ownerId}/pets
  API-->>R: 201 Pet
  R->>API: POST /appointments
  API-->>R: 201 Appointment
  V->>API: POST /pets/{petId}/visits
  API-->>V: 201 Visit
```

### 6.2 Scheduling conflict: double-book hard block; manager override
```mermaid
sequenceDiagram
  participant R as Reception
  participant API as API
  participant M as Manager

  R->>API: POST /appointments (overlapping)
  API-->>R: 409 Conflict
  M->>API: POST /appointments (overrideDoubleBooking=true, overrideReason=...)
  API-->>M: 201 Appointment
```

## 7) Endpoint behavior details
For each resource, specify:
- Request fields, required/optional
- Validation rules
- Response shape
- Error cases (400/401/403/404/409)

## 8) Data conventions
- Timezone handling
- Pagination
- Audit fields

## 9) Examples
Provide example requests/responses for the trickiest flows (duplicate owner warn; double-book override; visit edit).
