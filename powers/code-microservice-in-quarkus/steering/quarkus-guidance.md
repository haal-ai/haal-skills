# Quarkus Coding Guidance

## Agent Directives

YOU MUST apply these rules to ALL Quarkus code you generate:

1. **Use constructor injection** — Not field injection with `@Inject`
2. **Prefer `@ApplicationScoped`** — Over `@Singleton` for most beans
3. **Use Panache for data access** — Repository pattern preferred
4. **Return proper HTTP responses** — Use `Response` or exception mappers
5. **Follow Jakarta REST conventions** — `@Path`, `@GET`, `@POST`, etc.
6. **Add Bean Validation** — `@Valid`, `@NotNull`, `@Size`, etc.

---

## Reference: Quarkus Idioms

### CDI & Dependency Injection

- **Constructor injection over field injection**: More testable, explicit dependencies.
- **Use `@ApplicationScoped`**: One instance per application, lazy initialization.
- **Use `@RequestScoped`**: For request-specific state (e.g., security context).
- **Avoid `@Singleton`**: Use `@ApplicationScoped` unless you need eager initialization.

```java
// Good - Constructor injection
@ApplicationScoped
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;

    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
}

// Bad - Field injection
@ApplicationScoped
public class UserService {
    @Inject
    UserRepository userRepository; // Harder to test
}
```

### CDI Scopes Reference

| Scope | Lifecycle | Use Case |
|-------|-----------|----------|
| `@ApplicationScoped` | One per app, lazy | Services, repositories |
| `@RequestScoped` | One per HTTP request | Request context, user info |
| `@SessionScoped` | One per HTTP session | User session data |
| `@Dependent` | New instance each injection | Stateless utilities |
| `@Singleton` | One per app, eager | Config, startup tasks |

### REST Endpoints

- **Use `@Path` at class and method level**: Clear URL structure.
- **Return `Response` for control**: Status codes, headers.
- **Use `@Valid` for input validation**: Bean Validation integration.
- **Handle exceptions with `ExceptionMapper`**: Consistent error responses.

```java
@Path("/users")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
@ApplicationScoped
public class UserResource {
    private final UserService userService;

    public UserResource(UserService userService) {
        this.userService = userService;
    }

    @GET
    public List<UserDTO> list() {
        return userService.findAll();
    }

    @GET
    @Path("/{id}")
    public Response getById(@PathParam("id") Long id) {
        return userService.findById(id)
            .map(user -> Response.ok(user).build())
            .orElse(Response.status(Status.NOT_FOUND).build());
    }

    @POST
    public Response create(@Valid CreateUserRequest request) {
        UserDTO created = userService.create(request);
        return Response.status(Status.CREATED)
            .entity(created)
            .build();
    }

    @PUT
    @Path("/{id}")
    public Response update(@PathParam("id") Long id, @Valid UpdateUserRequest request) {
        return userService.update(id, request)
            .map(user -> Response.ok(user).build())
            .orElse(Response.status(Status.NOT_FOUND).build());
    }

    @DELETE
    @Path("/{id}")
    public Response delete(@PathParam("id") Long id) {
        if (userService.delete(id)) {
            return Response.noContent().build();
        }
        return Response.status(Status.NOT_FOUND).build();
    }
}
```

### Error Handling

Use `ExceptionMapper` for consistent error responses:

```java
@Provider
public class ApplicationExceptionMapper implements ExceptionMapper<ApplicationException> {
    
    @Override
    public Response toResponse(ApplicationException e) {
        ErrorResponse error = new ErrorResponse(
            e.getErrorCode(),
            e.getMessage(),
            LocalDateTime.now()
        );
        return Response.status(e.getStatus())
            .entity(error)
            .build();
    }
}

// Custom exception
public class NotFoundException extends ApplicationException {
    public NotFoundException(String message) {
        super(message, "NOT_FOUND", Status.NOT_FOUND);
    }
}

// Error response DTO
public record ErrorResponse(
    String code,
    String message,
    LocalDateTime timestamp
) {}
```

### Bean Validation

```java
public record CreateUserRequest(
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    String name,

    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    String email,

    @NotNull(message = "Age is required")
    @Min(value = 18, message = "Must be at least 18 years old")
    Integer age
) {}
```

## 2. Project Structure

```
src/
├── main/
│   ├── java/com/example/
│   │   ├── domain/           # Business entities
│   │   │   ├── User.java
│   │   │   └── Order.java
│   │   ├── repository/       # Data access (Panache)
│   │   │   ├── UserRepository.java
│   │   │   └── OrderRepository.java
│   │   ├── service/          # Business logic
│   │   │   ├── UserService.java
│   │   │   └── OrderService.java
│   │   ├── resource/         # REST endpoints
│   │   │   ├── UserResource.java
│   │   │   └── OrderResource.java
│   │   ├── dto/              # Data transfer objects
│   │   │   ├── UserDTO.java
│   │   │   └── CreateUserRequest.java
│   │   ├── mapper/           # Entity <-> DTO mappers
│   │   │   └── UserMapper.java
│   │   └── exception/        # Custom exceptions
│   │       ├── ApplicationException.java
│   │       └── NotFoundException.java
│   └── resources/
│       ├── application.properties
│       └── META-INF/
│           └── resources/    # Static files
├── test/
│   └── java/com/example/
│       ├── resource/         # Integration tests
│       │   └── UserResourceTest.java
│       └── service/          # Unit tests
│           └── UserServiceTest.java
```

## 3. Panache Data Access

### Repository Pattern (Recommended)

```java
@ApplicationScoped
public class UserRepository implements PanacheRepository<User> {
    
    public Optional<User> findByEmail(String email) {
        return find("email", email).firstResultOptional();
    }

    public List<User> findByStatus(Status status) {
        return list("status", status);
    }

    public List<User> findActive() {
        return list("status = ?1 and deletedAt is null", Status.ACTIVE);
    }

    public long countByStatus(Status status) {
        return count("status", status);
    }

    // Pagination
    public PanacheQuery<User> findAllPaged() {
        return findAll(Sort.by("createdAt").descending());
    }
}

// Usage in service
@ApplicationScoped
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User create(CreateUserRequest request) {
        User user = new User();
        user.name = request.name();
        user.email = request.email();
        userRepository.persist(user);
        return user;
    }

    public List<User> findAll(int page, int size) {
        return userRepository.findAllPaged()
            .page(page, size)
            .list();
    }
}
```

### Entity Definition

```java
@Entity
@Table(name = "users")
public class User extends PanacheEntity {
    
    @Column(nullable = false)
    public String name;

    @Column(unique = true, nullable = false)
    public String email;

    @Enumerated(EnumType.STRING)
    public Status status = Status.ACTIVE;

    @Column(name = "created_at")
    public LocalDateTime createdAt = LocalDateTime.now();

    @Column(name = "updated_at")
    public LocalDateTime updatedAt;

    @PreUpdate
    public void preUpdate() {
        this.updatedAt = LocalDateTime.now();
    }
}
```

## 4. Configuration

### application.properties

```properties
# Database
quarkus.datasource.db-kind=postgresql
quarkus.datasource.username=${DB_USER:postgres}
quarkus.datasource.password=${DB_PASSWORD:postgres}
quarkus.datasource.jdbc.url=jdbc:postgresql://${DB_HOST:localhost}:5432/${DB_NAME:myapp}

# Hibernate
quarkus.hibernate-orm.database.generation=validate
quarkus.hibernate-orm.log.sql=false

# HTTP
quarkus.http.port=8080
quarkus.http.cors=true

# Logging
quarkus.log.level=INFO
quarkus.log.category."com.example".level=DEBUG

# Health
quarkus.smallrye-health.root-path=/health
```

### Profile-Specific Configuration

```properties
# Dev profile (default in dev mode)
%dev.quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/myapp_dev
%dev.quarkus.hibernate-orm.database.generation=drop-and-create
%dev.quarkus.log.category."com.example".level=DEBUG

# Test profile
%test.quarkus.datasource.jdbc.url=jdbc:h2:mem:test
%test.quarkus.datasource.db-kind=h2
%test.quarkus.hibernate-orm.database.generation=drop-and-create

# Prod profile
%prod.quarkus.datasource.jdbc.url=${DATABASE_URL}
%prod.quarkus.hibernate-orm.database.generation=none
%prod.quarkus.log.level=WARN
```

### Type-Safe Configuration

```java
@ConfigMapping(prefix = "app")
public interface AppConfig {
    String name();
    
    @WithDefault("1.0.0")
    String version();
    
    Optional<String> description();
    
    FeatureFlags features();
    
    interface FeatureFlags {
        @WithDefault("false")
        boolean newUserFlow();
        
        @WithDefault("true")
        boolean emailNotifications();
    }
}

// Usage
@ApplicationScoped
public class MyService {
    private final AppConfig config;

    public MyService(AppConfig config) {
        this.config = config;
    }

    public void doSomething() {
        if (config.features().newUserFlow()) {
            // New flow
        }
    }
}
```

## 5. Testing

### Integration Tests with RestAssured

```java
@QuarkusTest
class UserResourceTest {

    @Test
    void shouldCreateUser() {
        CreateUserRequest request = new CreateUserRequest("John", "john@example.com", 25);

        given()
            .contentType(ContentType.JSON)
            .body(request)
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .body("name", equalTo("John"))
            .body("email", equalTo("john@example.com"));
    }

    @Test
    void shouldReturnNotFoundForUnknownUser() {
        given()
        .when()
            .get("/users/999999")
        .then()
            .statusCode(404);
    }

    @Test
    void shouldValidateInput() {
        CreateUserRequest invalid = new CreateUserRequest("", "not-an-email", 10);

        given()
            .contentType(ContentType.JSON)
            .body(invalid)
        .when()
            .post("/users")
        .then()
            .statusCode(400);
    }

    @Test
    void shouldListUsers() {
        given()
        .when()
            .get("/users")
        .then()
            .statusCode(200)
            .body("$", hasSize(greaterThanOrEqualTo(0)));
    }
}
```

### Unit Tests with Mocking

```java
@QuarkusTest
class UserServiceTest {

    @InjectMock
    UserRepository userRepository;

    @Inject
    UserService userService;

    @Test
    void shouldFindUserById() {
        User user = new User();
        user.id = 1L;
        user.name = "John";

        when(userRepository.findByIdOptional(1L)).thenReturn(Optional.of(user));

        Optional<User> result = userService.findById(1L);

        assertTrue(result.isPresent());
        assertEquals("John", result.get().name);
    }

    @Test
    void shouldReturnEmptyForUnknownUser() {
        when(userRepository.findByIdOptional(999L)).thenReturn(Optional.empty());

        Optional<User> result = userService.findById(999L);

        assertTrue(result.isEmpty());
    }
}
```

### Testcontainers for Integration

```java
@QuarkusTest
@QuarkusTestResource(PostgresTestResource.class)
class UserRepositoryIntegrationTest {

    @Inject
    UserRepository userRepository;

    @Test
    @Transactional
    void shouldPersistAndFindUser() {
        User user = new User();
        user.name = "Test User";
        user.email = "test@example.com";

        userRepository.persist(user);

        assertNotNull(user.id);

        Optional<User> found = userRepository.findByEmail("test@example.com");
        assertTrue(found.isPresent());
        assertEquals("Test User", found.get().name);
    }
}

// Test resource
public class PostgresTestResource implements QuarkusTestResourceLifecycleManager {
    private static final PostgreSQLContainer<?> POSTGRES = 
        new PostgreSQLContainer<>("postgres:15");

    @Override
    public Map<String, String> start() {
        POSTGRES.start();
        return Map.of(
            "quarkus.datasource.jdbc.url", POSTGRES.getJdbcUrl(),
            "quarkus.datasource.username", POSTGRES.getUsername(),
            "quarkus.datasource.password", POSTGRES.getPassword()
        );
    }

    @Override
    public void stop() {
        POSTGRES.stop();
    }
}
```

## 6. Code Quality Checks

Before committing, ensure:

- [ ] `./mvnw compile` succeeds
- [ ] `./mvnw test` passes
- [ ] No field injection (use constructor injection)
- [ ] All endpoints have tests
- [ ] Bean Validation on request DTOs
- [ ] Proper HTTP status codes returned
- [ ] No `TODO` comments without issue references

## References

- [Quarkus Guides](https://quarkus.io/guides/)
- [Quarkus CDI Reference](https://quarkus.io/guides/cdi-reference)
- [Hibernate ORM with Panache](https://quarkus.io/guides/hibernate-orm-panache)
- [Writing REST Services](https://quarkus.io/guides/rest)
- [Testing Quarkus Applications](https://quarkus.io/guides/getting-started-testing)
