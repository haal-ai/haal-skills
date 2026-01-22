---
type: reference
---

# DB Artifacts Request Checklist

## 1) Schema definition artifacts (preferred)
Provide at least one:
- Migrations (Flyway/Liquibase/EF Core/Alembic)
- DDL export (schema-only)

## 2) Relationship and constraint details
Provide if available:
- Primary keys and foreign keys
- Unique constraints
- Check constraints
- Nullability rules
- Indexes (including composite indexes)

## 3) Reference data and enum encoding
Provide:
- Code tables / lookup tables
- Enum encoding strategy (string codes vs numeric ids)
- Meaning of codes (data dictionary)

## 4) Data semantics (data dictionary)
Provide:
- Table purpose and ownership
- Column meaning, units, and formats
- Historical/audit strategy (effective dates, soft deletes)

## 5) Data access and operational constraints
Provide:
- Expected query patterns (hot paths)
- Volume estimates (row counts, growth)
- SLO/performance constraints
- Any read replicas / CDC / ETL constraints

## 6) Integration and ownership (microservices)
Provide:
- Which system is the system-of-record for each concept
- Who is allowed to write which tables
- Any planned data replication (events/CDC)
- Any constraints on changing the DB schema

## 7) Optional but helpful
- ERD diagram
- Anonymized sample rows for critical tables
- Existing SQL queries/reports used by current consumers
