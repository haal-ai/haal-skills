# Tutorial: scaffold-quarkus-microservice

## Introduction

This tutorial guides you through using the `scaffold-quarkus-microservice` skill to create a new Quarkus microservice. By the end, you'll have a fully scaffolded project with tests, health endpoints, and proper Git workflow setup.

## Prerequisites

Before starting, ensure you have:

- [ ] Java 17+ installed (`java -version`)
- [ ] Maven or Gradle installed (`mvn -version` or `gradle -version`)
- [ ] Git repository initialized
- [ ] Understanding of your organization's group ID convention

## Step-by-Step Instructions

### Step 1: Prepare Your Git Environment

The skill requires proper Git setup before scaffolding.

**Create a worktree (if not already in one):**
```bash
git worktree add ../my-feature-worktree feature/new-service
cd ../my-feature-worktree
```

**Or create a new branch:**
```bash
git checkout -b feature/order-service
```

### Step 2: Invoke the Skill

Request the scaffolding:

```
Scaffold a new Quarkus microservice called "order-service" 
with group ID com.mycompany
```

### Step 3: Answer Requirements Questions

The skill will ask clarifying questions:

1. **Service responsibility**: "Handles order creation and status tracking"
2. **REST-only or DB/messaging**: "REST with PostgreSQL database"
3. **Group ID confirmation**: "com.mycompany"
4. **Target runtime**: "JVM only" or "JVM and native"
5. **Port/health conventions**: "Port 8080, health at /q/health"

### Step 4: Review the Proposal

The skill presents a scaffold plan:

```
## Proposed Scaffold

- Output Directory: apps/order-service
- Group ID: com.mycompany
- Artifact ID: order-service
- Base Package: com.mycompany.orderservice
- Java Version: 17
- Build Tool: Maven

Extensions:
- quarkus-resteasy-reactive-jackson
- quarkus-smallrye-health
- quarkus-smallrye-openapi
- quarkus-jdbc-postgresql
- quarkus-hibernate-orm-panache

Structure:
├── src/main/java/com/mycompany/orderservice/
│   ├── resource/
│   └── entity/
├── src/main/resources/
│   └── application.properties
└── src/test/java/

Proceed with scaffolding? (yes/no)
```

### Step 5: Confirm and Execute

Type `yes` to proceed. The skill will:

1. Validate Java and Maven are available
2. Create the project structure
3. Generate application.properties
4. Add health and sample endpoints
5. Create a basic test

### Step 6: Verify the Scaffold

Run the quality gates:

```bash
# Run tests
mvn test

# Start in dev mode
mvn quarkus:dev
```

Verify endpoints:
- Health: http://localhost:8080/q/health
- OpenAPI: http://localhost:8080/q/openapi
- Sample: http://localhost:8080/api/ping

### Step 7: Commit Your Changes

Follow the suggested commit:

```bash
git add .
git commit -m "feat(order-service): scaffold Quarkus microservice with REST and health endpoints"
```

## Verification Checklist

After scaffolding, verify:

- [ ] Project structure exists under output directory
- [ ] `pom.xml` or `build.gradle` is properly configured
- [ ] `application.properties` has correct settings
- [ ] Health endpoint responds at `/q/health`
- [ ] Tests pass with `mvn test`
- [ ] Dev mode starts with `mvn quarkus:dev`
- [ ] Changes are committed to your feature branch

## Troubleshooting

### "Java not found"

**Cause**: Java is not installed or not in PATH.

**Solution**: Install Java 17+ and ensure `JAVA_HOME` is set:
```bash
# Check Java
java -version

# Set JAVA_HOME (example for Linux/Mac)
export JAVA_HOME=/path/to/java
```

### "Maven not found"

**Cause**: Maven is not installed or not in PATH.

**Solution**: Install Maven and add to PATH:
```bash
# Check Maven
mvn -version

# Install via package manager
brew install maven  # macOS
apt install maven   # Ubuntu
```

### "Output directory already exists"

**Cause**: A folder with the service name already exists.

**Solution**: Choose one of:
- Specify a different `output_dir`
- Delete the existing directory
- Rename the existing project

### "Not in a worktree / On main branch"

**Cause**: Git safety check failed.

**Solution**: Create a worktree or switch to a feature branch:
```bash
git checkout -b feature/my-service
```

### "Tests fail after scaffold"

**Cause**: Missing dependencies or configuration issues.

**Solution**: 
1. Check the error message for missing dependencies
2. Verify `application.properties` has correct database settings
3. Ensure all required extensions are included

## Next Steps

After successful scaffolding:

1. **Add Domain Logic**: Implement your service's business logic
2. **Configure Database**: Set up your database connection in `application.properties`
3. **Add More Tests**: Expand test coverage for your endpoints
4. **Set Up CI/CD**: Configure your build pipeline
5. **Document API**: Enhance OpenAPI annotations for better documentation
