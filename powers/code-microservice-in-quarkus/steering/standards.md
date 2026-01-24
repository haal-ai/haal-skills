# Universal Coding Standards

## Agent Directives

YOU MUST apply these rules to ALL generated code:

1. **Single Responsibility** — Each class/method has one job
2. **Dependency Injection** — Inject external deps via CDI constructor injection
3. **Function size** — Keep under 30 lines, complexity < 10
4. **Parameters** — Max 4 params; group related ones into a DTO/record
5. **Error handling** — Explicit handling, no sensitive data in logs
6. **Tests** — Generate `@QuarkusTest` tests for new/changed code

When refactoring existing code:
- Freeze public APIs by default
- Add characterization tests before changing internals
- Small incremental steps

---

## Reference: Core Principles

- **Single Responsibility (SRP)**: Each class/method/module should have one clear responsibility and one primary reason to change.
- **Dependency Injection (DI)**: Treat all external dependencies (repositories, clients, services) as injected collaborators via CDI to enable testability with mocks.
- **Function size & complexity**:
  - Prefer methods under ~20–30 lines.
  - Aim for cyclomatic complexity < 10 per method.
  - Extract helpers instead of adding nested conditionals.
- **Parameters & configuration**:
  - Prefer **≤ 4 parameters** per method.
  - When parameters are related, group them into a DTO or record.
  - Keep a consistent order across similar methods.
- **Naming & readability**:
  - Use clear, descriptive names for variables, methods, and classes.
  - Avoid cryptic abbreviations and over-generic names (`data`, `info`, `tmp`).
- **Comments**:
  - Explain **WHY**, domain intent, invariants, and edge cases.
  - Do not restate obvious logic or types.
  - Use Javadoc for public API.
- **Error handling & logging**:
  - Use explicit error handling with exceptions and `ExceptionMapper`.
  - Implement structured logging with appropriate levels.
  - Do not leak sensitive data in logs or error messages.
- **Configuration**:
  - Externalize configuration from code using `application.properties` and `@ConfigMapping`.

## 2. Evolution / Refactoring Mode (Default)

**This is the default mode.** When working in an existing codebase, apply these rules unless a task explicitly requests greenfield creation.

- **Public APIs are frozen by default**:
  - Do not change the name, signature, or behavior of public REST endpoints unless there is an explicit migration/deprecation plan.
- **Start with characterization tests**:
  - Before refactoring, add tests around the current behavior of the endpoint or service you are touching.
  - Keep these tests as a safety net while refactoring internals.
- **Refactor internals first**:
  - Focus on private helpers, data flows, and internal services.
  - Introduce DI via CDI for external dependencies.
  - Split large, multi-purpose methods into smaller SRP-aligned units.
- **Small, incremental steps**:
  - Prefer multiple small, testable changes over big rewrites.
  - After each step, ensure all tests pass before proceeding.
- **Modernization stays internal**:
  - Treat public signatures and external contracts as frozen in this mode.
  - Any modernization of public APIs must be proposed separately.

### 2.1 Refactoring Output Format

For refactoring-focused tasks, use this structured output:

```text
## Current Code Analysis
[Brief issues identified: complexity, duplication, missing DI, etc.]

## Refactored Internals (Public API Unchanged)
[Cleaned internal code structure adhering to SRP, DI, and testability]

## Modernization Proposal
- Benefits: [e.g., improved testability via CDI, reduced complexity]
- Tests: [Characterization/unit/integration tests added or updated]
- Next Steps: [Safe evolution paths, potential API improvements]
```

## 3. Creation / New Code Mode (Greenfield)

Use this mode only when adding **new services/endpoints/features** rather than evolving existing ones.

- **Small design first**:
  - Identify responsibilities and boundaries before writing code.
  - Define interfaces where DI will inject external dependencies.
- **Package and class structure**:
  - Group code by responsibility (domain, repository, service, resource).
  - Prefer classes ≤ 300–400 lines; if a class grows beyond that, consider splitting along clear responsibility lines.
- **Public APIs**:
  - Design coherent, minimal REST APIs consistent with existing naming conventions.
  - Make error handling and return types explicit.
  - Use DTOs for request/response, not entities.
- **Tests alongside code**:
  - Add tests as you introduce new public behavior, not as an afterthought.
  - Favor unit tests plus targeted integration tests at the new boundaries.

## 4. Cross-Cutting Domains

### 4.1 Security

- Validate all external inputs with Bean Validation.
- Implement proper authentication and authorization with Quarkus Security.
- Use `@RolesAllowed`, `@Authenticated` annotations.
- Do not expose sensitive details in error messages.
- Use parameterized queries (Panache handles this).
- Sanitize untrusted data in web contexts.

### 4.2 Performance & Resource Management

- Choose appropriate algorithms and data structures for the problem.
- Use connection pooling (Agroal is default in Quarkus).
- Optimize database queries and avoid N+1 patterns.
- Use pagination for list endpoints.
- Consider caching with `@CacheResult` when appropriate.
- Minimize and batch network/API calls when possible.

### 4.3 Testing

- Prefer **high coverage** around critical business logic and REST endpoints.
- Follow clear test structure (Arrange–Act–Assert / Given-When-Then).
- Keep tests independent from each other; avoid global mutable state.
- Mock external dependencies via `@InjectMock`.
- Add integration tests with Testcontainers for critical flows.

### 4.4 Version Control & Documentation

- Write clear, descriptive commit messages.
- Use consistent branch naming conventions aligned with team practices.
- Require code review for all non-trivial changes.
- Keep README and API documentation up to date with behavior changes.
- Use OpenAPI annotations for API documentation.
- Maintain a CHANGELOG for releases.

## 5. Language- and Team-Specific Extensions

- Language- and framework-specific standards **extend or refine** these universal rules.
- When both universal and language/team-specific standards exist, apply this precedence:
  1. Repository practices (good/bad examples, project conventions)
  2. Team and language-specific standards
  3. Universal coding standards (this document)
