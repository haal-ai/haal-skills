# Remediation Plan Checklist (DB ↔ API)

Use this checklist to ensure the plan covers real delivery work (not just schema diffs).

## 1) Compatibility strategy
- Backwards compatibility guarantees (API + DB)
- Versioning strategy (if breaking changes are unavoidable)
- Dual-read / dual-write (if migration requires coexistence)

## 2) Schema change plan
- Additive changes first (new nullable columns/tables)
- Constraints rollout strategy (validate later, enforce later)
- Indexing plan aligned to query patterns

## 3) Data migration / backfill
- Source of truth for new columns (derive vs manual input vs external system)
- Backfill approach (online batches vs offline job)
- Data validation strategy (checksums, row counts, sampling)
- Handling of historical records (default values, unknowns)

## 4) Operational plan
- Downtime expectations (none / limited / planned)
- Rollback plan (including reversing partial migrations)
- Monitoring and alerting signals

## 5) Security and audit
- Audit fields (who/when changed) and storage location
- Access control implications (who can update what)

## 6) Risk register
- Top risks with mitigations
- Explicit “what could go wrong” scenarios
