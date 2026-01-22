---
type: reference
---

# API Design Question Catalog (Specification Challenge)

## Purpose
This catalog helps ensure reviews consistently identify the missing decisions that block API contract design.

## 1) Identity and uniqueness
- How is each main entity uniquely identified in the business?
- Are there natural keys (email, registration number) that must be supported?
- Can identifiers change? If yes, how do we preserve referential integrity?
- What is the duplicate handling policy (reject, merge, allow with warning)?

## 2) Relationships and ownership
- Which relationships are mandatory vs optional?
- Can an entity belong to multiple parents (e.g., shared ownership)?
- What happens when a parent is deleted or deactivated?

## 3) Lifecycle and state machine
- What are the states of each entity?
- What transitions are allowed, and who can trigger them?
- Are transitions time-based (expiry, deadlines)?
- Is soft delete required (archival) vs hard delete?

## 4) Operations and workflows
- What are the key business workflows that the API must support end-to-end?
- Which operations must be atomic?
- Are there bulk operations (bulk create, bulk update, import)?

## 5) Search, filtering, and pagination
- What are the main lookup scenarios?
- Which filters are required (date ranges, status, owner, text search)?
- What default sort order is expected?
- Pagination style preference (page/size vs cursor)?

## 6) Validation and error behavior
- What validations are mandatory (required fields, formats, ranges)?
- When invalid state is requested, should the API return a specific business error?
- Should the API be strict (reject unknown fields) or tolerant?

## 7) Concurrency and idempotency
- Are repeated submissions expected (retries)?
- Do we need idempotency keys for create operations?
- How do we handle concurrent updates (last-write-wins vs optimistic locking)?

## 8) Security, privacy, and roles
- Who are the API users (roles/personas)?
- Which roles can see which data?
- Are there privacy constraints (PII/medical data)?
- Do we need audit trails (who changed what/when)?

## 9) Reporting and read models
- Are there reporting requirements (aggregations, metrics)?
- Are there read-optimized endpoints needed (views, dashboards)?

## 10) Integration boundaries
- Will other systems integrate later?
- What events or webhooks are expected?
- Are there regulatory constraints (retention, consent)?

## How to use this catalog
When reviewing a spec, you MUST:
- Confirm which of these areas are explicitly defined
- Turn missing definitions into SME questions
- For each question, include why it matters and propose options
