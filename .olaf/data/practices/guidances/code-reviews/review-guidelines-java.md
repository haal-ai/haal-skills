# Java Code Review Standards

## Java-Specific Review Areas

### 1. Modern Java Features and Best Practices

#### Java Version Compliance
- **Target Java Version**: Verify code uses appropriate Java version features (8, 11, 17, 21+)
- **Deprecated APIs**: Flag usage of deprecated classes/methods
- **Modern Syntax**: Encourage use of lambda expressions, streams, var keyword where appropriate

#### Memory Management
- **Resource Management**: Verify proper use of try-with-resources for AutoCloseable objects
- **Memory Leaks**: Check for potential memory leaks (listeners, static references, collections)
- **Object Creation**: Minimize unnecessary object creation in loops

### 2. Code Quality and Style

#### Naming Conventions
- **Classes**: PascalCase (e.g., `UserService`, `PaymentProcessor`)
- **Methods/Variables**: camelCase (e.g., `getUserById`, `totalAmount`)
- **Constants**: SCREAMING_SNAKE_CASE (e.g., `MAX_RETRY_COUNT`)
- **Packages**: lowercase with dots (e.g., `com.company.module`)

#### Code Organization
- **Package Structure**: Logical organization by feature/layer
- **Class Size**: Classes should have single responsibility, typically < 500 lines
- **Method Length**: Methods should be focused, typically < 20 lines
- **Imports**: Organize imports, remove unused ones, avoid wildcards

### 3. Exception Handling

#### Exception Best Practices
- **Specific Exceptions**: Use specific exception types over generic Exception
- **Resource Cleanup**: Ensure proper cleanup in finally blocks or try-with-resources
- **Exception Documentation**: Document thrown exceptions with @throws
- **Don't Swallow**: Avoid empty catch blocks

#### Logging
- **Appropriate Levels**: Use correct log levels (ERROR, WARN, INFO, DEBUG)
- **Parameterized Messages**: Use parameterized logging to avoid string concatenation
- **Sensitive Data**: Don't log passwords, tokens, or PII

### 4. Spring Framework (if applicable)

#### Dependency Injection
- **Constructor Injection**: Prefer constructor injection over field injection
- **Component Scanning**: Proper use of @Component, @Service, @Repository annotations
- **Configuration**: Use @Configuration classes properly

#### Data Access
- **JPA/Hibernate**: Proper entity relationships, avoid N+1 queries
- **Transaction Management**: Appropriate @Transactional usage
- **Repository Pattern**: Proper repository implementations

### 5. Testing

#### Unit Testing
- **JUnit Version**: Use JUnit 5 for new projects
- **Test Naming**: Clear, descriptive test method names
- **Assertions**: Use AssertJ or appropriate assertion libraries
- **Mock Usage**: Proper use of Mockito or other mocking frameworks

#### Test Coverage
- **Critical Paths**: Ensure business logic is covered
- **Edge Cases**: Test boundary conditions and error scenarios
- **Integration Tests**: Appropriate use of @SpringBootTest

### 6. Security

#### Input Validation
- **SQL Injection**: Use parameterized queries, avoid string concatenation
- **XSS Prevention**: Proper input sanitization and output encoding
- **Authentication**: Secure password handling, proper session management

#### Data Protection
- **Sensitive Data**: Encrypt sensitive data at rest and in transit
- **Access Control**: Implement proper authorization checks
- **Security Headers**: Use appropriate security headers in web applications

### 7. Performance

#### Collections and Streams
- **Collection Choice**: Use appropriate collection types (ArrayList vs LinkedList)
- **Stream Operations**: Efficient use of parallel streams where beneficial
- **Optional Usage**: Proper use of Optional, avoid excessive chaining

#### Database Optimization
- **Query Efficiency**: Avoid N+1 queries, use proper indexing
- **Connection Pooling**: Configure appropriate connection pool sizes
- **Caching**: Implement caching where beneficial (@Cacheable)

### 8. Concurrency

#### Thread Safety
- **Immutable Objects**: Favor immutable objects where possible
- **Concurrent Collections**: Use ConcurrentHashMap over synchronized HashMap
- **Atomic Operations**: Use AtomicInteger, AtomicReference for simple counters

#### CompletableFuture
- **Async Operations**: Proper use of CompletableFuture for asynchronous processing
- **Exception Handling**: Handle exceptions in async operations
- **Thread Pool Management**: Use appropriate thread pools

### Severity Guidelines for Java

#### HIGH Severity
- SQL injection vulnerabilities
- Resource leaks (unclosed connections, streams)
- Thread safety violations in concurrent code
- Security vulnerabilities (hardcoded credentials, weak encryption)
- Memory leaks (static references, listeners not removed)

#### MEDIUM Severity
- Deprecated API usage
- Missing input validation
- Poor exception handling (empty catch blocks)
- Performance issues (inefficient queries, wrong collection types)
- Missing @Override annotations
- Improper use of Optional

#### LOW Severity
- Code style violations (naming conventions, formatting)
- Missing JavaDoc for public APIs
- Unnecessary imports or variables
- Long methods or classes that could be refactored
- Missing final keywords on parameters/variables