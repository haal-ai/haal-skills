# Quarkus Microservice Scaffolding Guidance

This guidance extends `[id:practices_dir]standards/universal-coding-standards.md` with Quarkus + microservice scaffolding practices.

## 1. Goals (What “good” looks like)

A newly scaffolded Quarkus microservice SHOULD:
- Start locally with a single command (`mvn quarkus:dev` by default).
- Expose health endpoints (liveness/readiness).
- Provide OpenAPI docs (when REST endpoints exist).
- Have consistent logging and configuration (`application.properties`).
- Have a clean module structure (thin `main`, SRP services, DI via CDI).
- Include tests and quality gates (`mvn test`, optional formatting/lint).

## 2. Baseline Technology Choices

### Build tool
- Default to **Maven** unless the repository is standardized on Gradle.

### Java version
- Default to **Java 17** (LTS) unless org constraints require otherwise.

### Quarkus version
- Prefer the latest stable Quarkus platform version used in the repo.
- If unknown, choose a recent stable release compatible with Java 17.

## 3. Recommended Extensions (Baseline)

Choose extensions based on need; keep the baseline minimal.

**Common baseline for REST microservices:**
- `rest` (or RESTEasy Reactive / REST)
- `jackson`
- `smallrye-health`
- `smallrye-openapi`

**Optional, as needed:**
- Persistence: `hibernate-orm-panache`, `jdbc-postgresql` (or other JDBC driver)
- Validation: `hibernate-validator`
- Observability: `micrometer`, `micrometer-registry-prometheus`
- Resilience: `smallrye-fault-tolerance`
- Messaging: `smallrye-reactive-messaging-kafka`
- Container builds: `container-image-jib` (or Docker)

Guidance:
- Don’t add DB/messaging extensions “just in case”. Add them when a requirement exists.

## 4. Project Structure

Prefer a structure that makes boundaries explicit:

```
service/
├── pom.xml
├── src/main/java/<basePackage>/
│   ├── app/            # App wiring / entry-level configuration
│   ├── api/            # JAX-RS resources (HTTP boundary)
│   ├── domain/         # Domain types + business rules
│   ├── service/        # Use-cases / application services
│   └── infra/          # External IO adapters (db/http/fs)
├── src/main/resources/
│   └── application.properties
└── src/test/java/<basePackage>/
```

Rules:
- Keep JAX-RS Resources thin: parameter parsing, auth, calling services, mapping results.
- Put business logic in `service/` (SRP) and domain invariants in `domain/`.
- Put IO in `infra/` and inject via CDI.

## 5. Configuration & Secrets

- Prefer config in `application.properties` with environment overrides.
- Never hardcode secrets.
- Use Quarkus config mapping (`@ConfigMapping`) or typed config objects for non-trivial settings.

## 6. Error Handling (HTTP)

- Prefer mapping errors to proper HTTP responses via `ExceptionMapper`.
- Don’t leak internal exception messages in responses.
- Log with enough context for diagnosis (but no secrets).

## 7. Testing

- Always scaffold at least:
  - one happy-path test for the health endpoint
  - if REST endpoints exist: a `@QuarkusTest` verifying one endpoint

Guidance:
- Use unit tests for pure business logic.
- Use `@QuarkusTest` sparingly to keep the suite fast.

## 8. Quality Gates (Suggested)

Before committing, ensure:
- [ ] `mvn test` passes
- [ ] `mvn -DskipTests=false verify` passes if your repo uses `verify`
- [ ] Formatting conventions are followed (if enforced in repo)

## 9. Scaffolding Commands (Reference)

Maven-based scaffolding (typical):

```sh
mvn io.quarkus.platform:quarkus-maven-plugin:create \
  -DprojectGroupId=<groupId> \
  -DprojectArtifactId=<artifactId> \
  -DclassName=<basePackage>.api.HealthResource \
  -Dpath=/healthz \
  -Dextensions="smallrye-health,smallrye-openapi,rest,jackson"
```

Then run:

```sh
cd <outputDir>
mvn quarkus:dev
```

## 10. Propose → Confirm → Act

When scaffolding a microservice, you MUST:
- Propose the tech choices (build tool, Java version, extensions, output dir)
- Ask for explicit approval
- Only then generate files / run scaffolding commands
