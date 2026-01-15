# Universal Coding Standards

These standards define how code should be written and evolved in all OLAF projects.
They are designed to be **operational for LLM-driven work** and apply by default
unless overridden by language- or team-specific standards.

## 1. Core Principles (Always Apply)

- **Single Responsibility (SRP)**: Each class/function/module should have one clear
  responsibility and one primary reason to change.
- **Dependency Injection (DI)**: Treat all external dependencies (files, DBs,
  queues, loggers, clocks, network clients, etc.) as injected collaborators to
  enable testability with mocks/fakes.
- **Function size & complexity**:
  - Prefer functions under ~20–30 lines.
  - Aim for cyclomatic complexity < 10 per function.
  - Extract helpers instead of adding nested conditionals.
- **Parameters & configuration**:
  - Prefer **≤ 4 parameters** per function/method.
  - When parameters are related, group them into a config/options struct/object.
  - Keep a consistent order across similar functions
    (e.g., context/env → inputs → options/dependencies).
- **Naming & readability**:
  - Use clear, descriptive names for variables, functions, and classes.
  - Avoid cryptic abbreviations and over-generic names (`data`, `info`, `tmp`).
- **Comments**:
  - Explain **WHY**, domain intent, invariants, and edge cases.
  - Do not restate obvious logic or types.
- **Error handling & logging**:
  - Use explicit error handling at appropriate boundaries.
  - Implement structured logging with appropriate levels.
  - Do not leak sensitive data in logs or error messages.
- **Configuration**:
  - Externalize configuration from code (files, env vars, config objects).

## 2. Evolution / Refactoring Mode (Default)

**This is the default mode.** When working in an existing codebase, apply these
rules unless a task explicitly requests greenfield creation.

- **Public APIs are frozen by default**:
  - Do not change the name, signature, or behavior of public/exported APIs
    unless there is an explicit migration/deprecation plan.
- **Start with characterization tests**:
  - Before refactoring, add tests around the current behavior of the public API
    or code path you are touching.
  - Keep these tests as a safety net while refactoring internals.
- **Refactor internals first**:
  - Focus on private helpers, data flows, and internal modules.
  - Introduce DI for external dependencies.
  - Split large, multi-purpose functions into smaller SRP-aligned units.
- **Small, incremental steps**:
  - Prefer multiple small, testable changes over big rewrites.
  - After each step, ensure all tests pass before proceeding.
- **Modernization stays internal**:
  - Treat public signatures and external contracts as frozen in this mode.
  - Any modernization of public APIs must be proposed separately.

### 2.1 Refactoring Output Format (for LLM-Driven Refactors)

For refactoring-focused tasks, use this structured output:

```text
## Current Code Analysis
[Brief issues identified: complexity, duplication, missing DI, etc.]

## Refactored Internals (Public API Unchanged)
[Cleaned internal code structure adhering to SRP, DI, and testability]

## Modernization Proposal
- Benefits: [e.g., improved testability via DI, reduced complexity]
- Tests: [Characterization/unit/integration tests added or updated]
- Next Steps: [Safe evolution paths, potential API improvements]
```

Treat public APIs and observable behavior as frozen during these refactors.
Any proposed behavior changes stay in the **Modernization Proposal** section.

## 3. Creation / New Code Mode (Greenfield)

Use this mode only when adding **new modules/tools/features** (for example,
a new helper CLI like `git-differ`) rather than evolving existing ones.

- **Small design first**:
  - Identify responsibilities and boundaries before writing code.
  - Define seams where DI will inject external dependencies.
- **Module and file structure**:
  - Group code by responsibility, not by technology alone.
  - Prefer files ≤ 300–400 lines; if a file grows beyond that, consider
    splitting along clear responsibility lines.
- **Public APIs**:
  - Design coherent, minimal public APIs consistent with existing naming and
    parameter ordering conventions.
  - Make error handling and return types explicit.
- **Tests alongside code**:
  - Add tests as you introduce new public behavior, not as an afterthought.
  - Favor unit tests plus targeted integration tests at the new boundaries.

## 4. Cross-Cutting Domains

These standards apply in both Evolution and Creation modes.

### 4.1 Security

- Validate all external inputs.
- Implement proper authentication and authorization, following the
  **principle of least privilege**.
- Encrypt sensitive data in transit and at rest where applicable.
- Do not expose sensitive details in error messages.
- Use parameterized queries to prevent SQL injection.
- Sanitize and encode untrusted data in web contexts to prevent XSS.

### 4.2 Performance & Resource Management

- Choose appropriate algorithms and data structures for the problem.
- Properly dispose of resources (connections, files, memory, goroutines,
  threads, etc.).
- Optimize database queries and avoid N+1 patterns.
- Use caching when appropriate and safe.
- Minimize and batch network/API calls when possible.

### 4.3 Testing

- Prefer **high coverage** around critical business logic and public APIs.
- Follow clear test structure (e.g., Arrange–Act–Assert).
- Keep tests independent from each other; avoid global mutable state.
- Mock or fake external dependencies (DBs, queues, external services) when
  unit testing.
- Add integration tests for critical flows and cross-service interactions.

### 4.4 Version Control & Documentation

- Write clear, descriptive commit messages.
- Use consistent branch naming conventions aligned with team practices.
- Require code review for all non-trivial changes.
- Keep README and API documentation up to date with behavior changes.
- Maintain a changelog for user-visible releases where applicable.
- Ensure appropriate license information is present.

## 5. Language- and Team-Specific Extensions

- Language- and framework-specific standards (for example, Python, TypeScript,
  Go, React) **extend or refine** these universal rules.
- Teams should define these in their own standards files using the
  provided coding standards template.
- When both universal and language/team-specific standards exist, apply this
  precedence:

  1. Repository practices (good/bad examples, project conventions)
  2. Team and language-specific standards
  3. Universal coding standards (this document)

This ensures that local conventions and language realities are respected
while keeping a consistent baseline across projects.