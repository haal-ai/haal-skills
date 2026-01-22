# scaffold-quarkus-microservice

## Overview

The `scaffold-quarkus-microservice` skill scaffolds a new Quarkus microservice based on team practices, standards, and Git workflow guidance. It ensures consistent project structure, proper tooling validation, and follows established coding standards.

## Purpose

This skill helps Java developers quickly bootstrap new Quarkus microservices while adhering to organizational standards and best practices. It handles the entire scaffolding process from requirements gathering to commit guidance, ensuring consistency across projects.

## Key Features

- **Practice-Driven Scaffolding**: Loads and applies team coding standards and Quarkus guidance
- **Git Workflow Integration**: Verifies worktree and branch setup before generating code
- **Tooling Validation**: Checks for required Java and build tool availability
- **Flexible Scaffold Modes**: Supports plan-only, scaffold-only, or full scaffold-and-wire
- **Quality Gates**: Runs tests and smoke checks to verify the scaffold
- **Commit Guidance**: Suggests appropriate commit messages for the changes

## Usage

Invoke the skill with the following parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `service_name` | string | Yes | - | Human name for the microservice |
| `output_dir` | string | No | apps/{service_name} | Where to create the service |
| `group_id` | string | Yes | - | Maven groupId / organization namespace |
| `artifact_id` | string | No | {service_name} normalized | Maven artifactId |
| `base_package` | string | No | {group_id} | Java base package |
| `java_version` | string | No | 17 | Java target version |
| `build_tool` | string | No | maven | Build tool: maven or gradle |
| `quarkus_extensions` | string[] | No | REST + health + openapi + jackson | Quarkus extensions to include |
| `scaffold_mode` | string | No | scaffold-and-wire-basics | Mode: plan-only, scaffold-only, or scaffold-and-wire-basics |

## Process Flow

1. **Practices Loading**: Loads universal coding standards, Quarkus guidance, and Git workflow practices
2. **Worktree + Branch Verification**: Ensures proper Git setup before code generation
3. **Requirements Intake**: Confirms service responsibility, DB/messaging needs, and conventions
4. **Proposal Phase**: Presents scaffold plan with parameters and extensions
5. **Execution Phase**: Validates tooling, scaffolds project, wires basics, runs quality gates
6. **Commit Guidance**: Suggests focused commit messages

## Output

The skill generates:

- Complete Quarkus project structure under the specified output directory
- Configured `application.properties` with environment-friendly settings
- Health endpoints enabled
- OpenAPI endpoint (if REST present)
- Sample `GET /api/ping` resource (optional)
- `@QuarkusTest` verifying the endpoint
- Commit message suggestions

## Examples

**Basic scaffolding**:
```
Scaffold a new Quarkus microservice called "order-service" 
with group ID com.example
```

**With specific extensions**:
```
Scaffold a Quarkus microservice "inventory-api" 
with group ID com.myorg
including hibernate-orm-panache and jdbc-postgresql extensions
```

**Plan-only mode**:
```
Plan a Quarkus microservice scaffold for "notification-service"
with group ID com.company (plan-only mode)
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Tooling missing | Provides install options and stops before scaffolding |
| Output directory exists | Asks whether to overwrite, choose another folder, or abort |
| Not in worktree | Stops and guides user to create a worktree |
| On main/master branch | Stops and guides user to create a new branch |
| Extra extensions requested | Proposes minimal additions with tradeoff explanations |

## Related Skills

- `scaffold-api-from-spec` - For scaffolding APIs from OpenAPI specifications
- `scaffold-angular-frontend-from-spec` - For scaffolding Angular frontends
