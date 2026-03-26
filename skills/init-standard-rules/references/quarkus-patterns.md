# Quarkus Patterns

Detect Quarkus-specific patterns: REST endpoints, CDI beans, Panache entities, native image, and reactive routes.

## Search Patterns

### File Roles

```
# REST endpoints
*Resource.java
*Endpoint.java
*Controller.java

# Services
*Service.java
*ServiceImpl.java

# Repositories
*Repository.java
*PanacheRepository.java

# Entities
*Entity.java
*Entity.java (Panache)

# Configuration
application.properties
application.yml
application-*.properties
```

### Structure Markers

```
# REST annotations
@Path("/...")
@GET
@POST
@PUT
@DELETE
@PATCH
@Produces("application/json")
@Consumes("application/json")

# CDI annotations
@Inject
@ApplicationScoped
@RequestScoped
@Dependent
@Singleton
@Produces
@Named
@Qualifier

# JAX-RS
@PathParam
@QueryParam
@FormParam
@HeaderParam
@Context
@Context UriInfo
@Context HttpHeaders

# JSON
@Json
@JsonIgnore
@JsonProperty
```

### Panache Patterns

```
# Panache Entity
extends PanacheEntity
extends PanacheEntityBase

# Panache Repository
implements PanacheRepository<*>
implements PanacheRepositoryBase<*>

# Panache methods
.findById(
.findByIdOptional(
.list(
.listAll(
.persist(
.delete(
.deleteById(
.count(
```

### Reactive Patterns

```
# Mutiny
Uni<*>
Multi<*>
.await()
.onItem()
.onFailure()
.onTermination()
.repeat()

# Reactive REST
@GET
Uni<Response>
Multi<*>

# Reactive routes
Route
Router
RoutingContext
```

### Native Image Patterns

```
# Native hints
@RegisterForReflection
@NativeImageTest
native-image.properties

# GraalVM substitutions
@Substitute
@TargetClass
```

### Configuration Patterns

```
# application.properties
quarkus.*
%dev.quarkus.*
%test.quarkus.*
%prod.quarkus.*

# Config injection
@ConfigProperty(name = "...")
@ConfigProperties
ConfigProvider

# Profiles
quarkus.profile
%dev.
%test.
%prod.
```

### Testing Patterns

```
# Quarkus test
@QuarkusTest
@QuarkusTestResource
@TestHTTPResource
@NativeImageTest

# Test annotations
@Inject in test
@Mock
@Alternative
@Priority
```

## Analysis Method

1. **Enumerate REST resources**: Group by `@Path` classes
2. **Sample CDI beans**: Read 3-5 `@ApplicationScoped` classes
3. **Detect Panache usage**: Check for `PanacheEntity` or `PanacheRepository`
4. **Analyze reactive patterns**: Check `Uni`/`Multi` usage
5. **Check native hints**: Look for `@RegisterForReflection`

## Reporting Threshold

Report only if:
- ≥3 REST resources with similar structure
- ≥2 entities using Panache pattern
- Inconsistent CDI scope usage

## Insight Template

```
INSIGHT:
  id: QUARKUS-[n]
  title: "QUARKUS PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - rest_pattern: [JAX-RS|Reactive]
    - persistence: [Panache|Traditional]
    - scope: [ApplicationScoped|RequestScoped]
    - native_ready: [true|false]
```

## Command Template

When a Quarkus pattern is detected, propose a command:

```yaml
name: "create-quarkus-[pattern]"
summary: "Scaffold a new [Pattern] in Quarkus"
whenToUse:
  - "Adding a new REST resource"
  - "Creating a new entity with Panache"
contextValidationCheckpoints:
  - "What is the resource path?"
  - "What HTTP methods are needed?"
steps:
  - name: "Create REST resource"
    description: "Create JAX-RS resource class"
    codeSnippet: |
      @Path("/api/[resource]")
      @ApplicationScoped
      public class [Name]Resource {
          
          @GET
          @Produces("application/json")
          public Uni<List<[Entity]>> list() {
              return [Entity].listAll();
          }
      }
  - name: "Create Panache entity (if needed)"
    description: "Create entity with Panache"
    codeSnippet: |
      @Entity
      public class [Name] extends PanacheEntity {
          public String field;
      }
```

## Common Quarkus Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **REST Resource** | `@Path`, `@GET/@POST`, `@Produces` | Command: "create-quarkus-resource" |
| **Panache Entity** | `extends PanacheEntity`, `persist()` | Standard: "Panache entity pattern" |
| **CDI Service** | `@ApplicationScoped`, `@Inject` | Command: "create-quarkus-service" |
| **Reactive endpoint** | `Uni<Response>`, `Multi<*>` | Standard: "Reactive REST pattern" |
| **Native-ready** | `@RegisterForReflection`, native-image.properties | Standard: "Native image hints pattern" |
