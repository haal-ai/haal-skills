# Advanced Quarkus Patterns

## Agent Directives

When assisting experienced Quarkus developers, YOU MUST:

1. **Suggest MicroProfile Fault Tolerance** — `@Retry`, `@CircuitBreaker`, `@Timeout`, `@Fallback`
2. **Recommend health checks** — Liveness and readiness probes
3. **Use OpenTelemetry for tracing** — Distributed tracing across services
4. **Apply native image patterns** — Avoid reflection, register for native
5. **Suggest reactive patterns when appropriate** — Mutiny, reactive routes
6. **Know Dev Services** — Auto-provisioned containers for development

---

## MicroProfile Fault Tolerance

### Retry Pattern

```java
@ApplicationScoped
public class ExternalServiceClient {

    @Retry(maxRetries = 3, delay = 1000, retryOn = {IOException.class, TimeoutException.class})
    public Response callExternalService(String payload) {
        // External call that might fail
        return restClient.post(payload);
    }
}
```

### Circuit Breaker

```java
@ApplicationScoped
public class PaymentService {

    @CircuitBreaker(
        requestVolumeThreshold = 4,
        failureRatio = 0.5,
        delay = 10000,
        successThreshold = 2
    )
    @Fallback(fallbackMethod = "fallbackPayment")
    public PaymentResult processPayment(PaymentRequest request) {
        return paymentGateway.process(request);
    }

    public PaymentResult fallbackPayment(PaymentRequest request) {
        // Queue for later processing or return cached response
        return PaymentResult.queued(request.getId());
    }
}
```

### Timeout

```java
@Timeout(5000) // 5 seconds
public Response fetchData(String id) {
    return slowExternalService.getData(id);
}
```

### Bulkhead (Limit Concurrent Calls)

```java
@Bulkhead(value = 5, waitingTaskQueue = 10)
public Response limitedResource(String id) {
    return heavyProcessing(id);
}
```

### Combined Patterns

```java
@ApplicationScoped
public class ResilientService {

    @Timeout(5000)
    @Retry(maxRetries = 2, delay = 500)
    @CircuitBreaker(requestVolumeThreshold = 4, failureRatio = 0.5, delay = 10000)
    @Fallback(fallbackMethod = "fallback")
    public String resilientCall(String input) {
        return externalService.call(input);
    }

    public String fallback(String input) {
        return "Fallback response for: " + input;
    }
}
```

---

## Health Checks

### Liveness Probe

```java
@Liveness
@ApplicationScoped
public class LivenessCheck implements HealthCheck {

    @Override
    public HealthCheckResponse call() {
        return HealthCheckResponse.up("Application is alive");
    }
}
```

### Readiness Probe

```java
@Readiness
@ApplicationScoped
public class ReadinessCheck implements HealthCheck {

    private final DataSource dataSource;

    public ReadinessCheck(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public HealthCheckResponse call() {
        try (Connection conn = dataSource.getConnection()) {
            if (conn.isValid(5)) {
                return HealthCheckResponse.up("Database connection is ready");
            }
        } catch (SQLException e) {
            return HealthCheckResponse.down("Database connection failed");
        }
        return HealthCheckResponse.down("Database not ready");
    }
}
```

### Custom Health Check with Data

```java
@Readiness
@ApplicationScoped
public class ExternalServiceHealthCheck implements HealthCheck {

    @ConfigProperty(name = "external.service.url")
    String serviceUrl;

    @Override
    public HealthCheckResponse call() {
        try {
            // Check external service
            boolean healthy = checkService();
            return HealthCheckResponse.named("external-service")
                .status(healthy)
                .withData("url", serviceUrl)
                .withData("responseTime", "45ms")
                .build();
        } catch (Exception e) {
            return HealthCheckResponse.named("external-service")
                .down()
                .withData("error", e.getMessage())
                .build();
        }
    }
}
```

### Health Endpoints

```
GET /q/health          # All health checks
GET /q/health/live     # Liveness only
GET /q/health/ready    # Readiness only
GET /q/health/started  # Startup checks
```

---

## Observability

### OpenTelemetry Tracing

```properties
# application.properties
quarkus.otel.exporter.otlp.endpoint=http://localhost:4317
quarkus.otel.service.name=my-service
quarkus.otel.traces.enabled=true
```

### Custom Spans

```java
@ApplicationScoped
public class OrderService {

    @Inject
    Tracer tracer;

    public Order processOrder(OrderRequest request) {
        Span span = tracer.spanBuilder("process-order")
            .setAttribute("order.id", request.getId())
            .setAttribute("order.items", request.getItems().size())
            .startSpan();

        try (Scope scope = span.makeCurrent()) {
            // Process order
            Order order = createOrder(request);
            span.setAttribute("order.total", order.getTotal().toString());
            return order;
        } catch (Exception e) {
            span.recordException(e);
            span.setStatus(StatusCode.ERROR, e.getMessage());
            throw e;
        } finally {
            span.end();
        }
    }
}
```

### Micrometer Metrics

```java
@ApplicationScoped
public class OrderService {

    private final MeterRegistry registry;
    private final Counter ordersCreated;
    private final Timer orderProcessingTime;

    public OrderService(MeterRegistry registry) {
        this.registry = registry;
        this.ordersCreated = Counter.builder("orders.created")
            .description("Number of orders created")
            .register(registry);
        this.orderProcessingTime = Timer.builder("orders.processing.time")
            .description("Order processing time")
            .register(registry);
    }

    public Order createOrder(OrderRequest request) {
        return orderProcessingTime.record(() -> {
            Order order = processOrder(request);
            ordersCreated.increment();
            return order;
        });
    }
}
```

### Metrics Endpoints

```
GET /q/metrics           # All metrics (Prometheus format)
GET /q/metrics/json      # JSON format
```

---

## Native Image Patterns

### Avoid Reflection

```java
// Bad - uses reflection
Object obj = Class.forName(className).getDeclaredConstructor().newInstance();

// Good - use CDI or factory
@ApplicationScoped
public class ProcessorFactory {
    @Inject
    Instance<Processor> processors;

    public Processor getProcessor(String type) {
        return processors.stream()
            .filter(p -> p.supports(type))
            .findFirst()
            .orElseThrow();
    }
}
```

### Register for Reflection (when unavoidable)

```java
@RegisterForReflection
public class ExternalDTO {
    public String name;
    public int value;
}

// Or register multiple classes
@RegisterForReflection(targets = {ExternalDTO.class, AnotherDTO.class})
public class ReflectionConfiguration {}
```

### Native Image Configuration

```properties
# application.properties
quarkus.native.additional-build-args=--initialize-at-run-time=org.some.Class
quarkus.native.resources.includes=templates/*,data/*.json
```

### Build Native Image

```bash
# With GraalVM installed
./mvnw package -Dnative

# With container build (no GraalVM needed)
./mvnw package -Dnative -Dquarkus.native.container-build=true

# Run native executable
./target/my-app-1.0.0-runner
```

---

## Reactive Patterns with Mutiny

### Basic Uni/Multi

```java
@ApplicationScoped
public class ReactiveUserService {

    @Inject
    UserRepository userRepository;

    public Uni<User> findById(Long id) {
        return userRepository.findById(id);
    }

    public Multi<User> streamAll() {
        return userRepository.streamAll();
    }

    public Uni<User> createUser(CreateUserRequest request) {
        User user = new User();
        user.name = request.name();
        user.email = request.email();
        return userRepository.persist(user);
    }
}
```

### Reactive REST Endpoint

```java
@Path("/users")
@ApplicationScoped
public class ReactiveUserResource {

    @Inject
    ReactiveUserService userService;

    @GET
    @Path("/{id}")
    public Uni<Response> getById(@PathParam("id") Long id) {
        return userService.findById(id)
            .onItem().transform(user -> Response.ok(user).build())
            .onFailure(NotFoundException.class)
                .recoverWithItem(Response.status(Status.NOT_FOUND).build());
    }

    @GET
    @Produces(MediaType.SERVER_SENT_EVENTS)
    @RestStreamElementType(MediaType.APPLICATION_JSON)
    public Multi<User> streamUsers() {
        return userService.streamAll();
    }

    @POST
    public Uni<Response> create(@Valid CreateUserRequest request) {
        return userService.createUser(request)
            .onItem().transform(user -> 
                Response.status(Status.CREATED).entity(user).build());
    }
}
```

### Combining Async Operations

```java
public Uni<OrderSummary> getOrderSummary(Long orderId) {
    Uni<Order> orderUni = orderService.findById(orderId);
    Uni<Customer> customerUni = orderUni
        .onItem().transformToUni(order -> customerService.findById(order.customerId));
    Uni<List<OrderItem>> itemsUni = orderItemService.findByOrderId(orderId);

    return Uni.combine().all()
        .unis(orderUni, customerUni, itemsUni)
        .asTuple()
        .onItem().transform(tuple -> new OrderSummary(
            tuple.getItem1(),
            tuple.getItem2(),
            tuple.getItem3()
        ));
}
```

---

## REST Client

### Declarative REST Client

```java
@Path("/api")
@RegisterRestClient(configKey = "external-api")
public interface ExternalApiClient {

    @GET
    @Path("/users/{id}")
    User getUser(@PathParam("id") Long id);

    @POST
    @Path("/users")
    User createUser(CreateUserRequest request);

    @GET
    @Path("/users")
    List<User> listUsers(@QueryParam("page") int page, @QueryParam("size") int size);
}

// Configuration
// application.properties
quarkus.rest-client.external-api.url=https://api.example.com
quarkus.rest-client.external-api.scope=jakarta.inject.Singleton
```

### Using the Client

```java
@ApplicationScoped
public class UserSyncService {

    @RestClient
    ExternalApiClient externalApi;

    public User syncUser(Long externalId) {
        return externalApi.getUser(externalId);
    }
}
```

### Client with Fault Tolerance

```java
@ApplicationScoped
public class ResilientApiClient {

    @RestClient
    ExternalApiClient externalApi;

    @Retry(maxRetries = 3, delay = 1000)
    @Timeout(5000)
    @CircuitBreaker(requestVolumeThreshold = 4, failureRatio = 0.5)
    @Fallback(fallbackMethod = "fallbackGetUser")
    public User getUser(Long id) {
        return externalApi.getUser(id);
    }

    public User fallbackGetUser(Long id) {
        return cachedUserService.getCached(id)
            .orElse(User.unknown(id));
    }
}
```

---

## Dev Services

Quarkus automatically starts containers for development:

```properties
# Enabled by default in dev/test mode
# PostgreSQL
quarkus.datasource.db-kind=postgresql
# Dev Services starts PostgreSQL container automatically

# Kafka
quarkus.kafka.devservices.enabled=true

# Redis
quarkus.redis.devservices.enabled=true

# Keycloak
quarkus.keycloak.devservices.enabled=true
```

### Custom Dev Services Configuration

```properties
# Use specific image
quarkus.datasource.devservices.image-name=postgres:15

# Disable for specific profile
%prod.quarkus.datasource.devservices.enabled=false
```

---

## Caching

### Simple Caching

```java
@ApplicationScoped
public class ProductService {

    @CacheResult(cacheName = "products")
    public Product findById(Long id) {
        // Expensive operation
        return productRepository.findById(id);
    }

    @CacheInvalidate(cacheName = "products")
    public void invalidateProduct(Long id) {
        // Cache entry for this id will be removed
    }

    @CacheInvalidateAll(cacheName = "products")
    public void invalidateAllProducts() {
        // All cache entries removed
    }
}
```

### Cache Configuration

```properties
# application.properties
quarkus.cache.caffeine.products.expire-after-write=10M
quarkus.cache.caffeine.products.maximum-size=1000
```

---

## Scheduled Tasks

```java
@ApplicationScoped
public class ScheduledTasks {

    @Scheduled(every = "10s")
    void everyTenSeconds() {
        // Runs every 10 seconds
    }

    @Scheduled(cron = "0 0 * * * ?")
    void everyHour() {
        // Runs at the start of every hour
    }

    @Scheduled(every = "{app.cleanup.interval}")
    void configuredInterval() {
        // Interval from configuration
    }
}
```

---

## Event-Driven Patterns

### CDI Events

```java
// Event class
public record OrderCreatedEvent(Long orderId, String customerEmail) {}

// Producer
@ApplicationScoped
public class OrderService {

    @Inject
    Event<OrderCreatedEvent> orderCreatedEvent;

    @Transactional
    public Order createOrder(OrderRequest request) {
        Order order = // create order
        orderCreatedEvent.fire(new OrderCreatedEvent(order.id, order.customerEmail));
        return order;
    }
}

// Consumer
@ApplicationScoped
public class NotificationService {

    public void onOrderCreated(@Observes OrderCreatedEvent event) {
        sendEmail(event.customerEmail(), "Order " + event.orderId() + " created");
    }
}
```

### Async Events

```java
public void onOrderCreated(@ObservesAsync OrderCreatedEvent event) {
    // Processed asynchronously
    sendEmail(event.customerEmail(), "Order confirmed");
}

// Fire async
orderCreatedEvent.fireAsync(new OrderCreatedEvent(order.id, order.customerEmail));
```

---

## Security

### Basic Authentication

```java
@Path("/api/admin")
@RolesAllowed("admin")
@ApplicationScoped
public class AdminResource {

    @GET
    public String adminOnly() {
        return "Admin content";
    }
}

@Path("/api/users")
@Authenticated
@ApplicationScoped
public class UserResource {

    @Inject
    SecurityIdentity identity;

    @GET
    @Path("/me")
    public String currentUser() {
        return identity.getPrincipal().getName();
    }
}
```

### Configuration

```properties
# application.properties
quarkus.http.auth.basic=true
quarkus.security.users.embedded.enabled=true
quarkus.security.users.embedded.plain-text=true
quarkus.security.users.embedded.users.admin=admin123
quarkus.security.users.embedded.roles.admin=admin,user
```

---

## Common Maven Commands

```bash
# Development mode with live reload
./mvnw quarkus:dev

# Run tests
./mvnw test

# Run tests continuously
./mvnw quarkus:test

# Package JVM mode
./mvnw package

# Package native
./mvnw package -Dnative

# Add extension
./mvnw quarkus:add-extension -Dextensions="rest-client,smallrye-fault-tolerance"

# List extensions
./mvnw quarkus:list-extensions

# Generate project
mvn io.quarkus.platform:quarkus-maven-plugin:3.8.0:create \
    -DprojectGroupId=com.example \
    -DprojectArtifactId=my-service \
    -Dextensions="rest,hibernate-orm-panache,jdbc-postgresql"
```
