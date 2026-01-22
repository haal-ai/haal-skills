---
name: scaffold-quarkus-microservice
description: Scaffold a new Quarkus microservice based on team practices, standards, and Git workflow guidance
license: Apache-2.0
metadata:
  olaf_tags: [java, quarkus, microservice, scaffolding, practices, git]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full reference/.condensed/olaf-framework-condensed.md.

## Time Retrieval
Get current timestamp using time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **service_name**: string - Human name for the microservice (REQUIRED)
- **output_dir**: string - Where to create the service (OPTIONAL - default: `apps/{service_name}`)
- **group_id**: string - Maven groupId / organization namespace (REQUIRED)
- **artifact_id**: string - Maven artifactId (OPTIONAL - default: `{service_name}` normalized)
- **base_package**: string - Java base package (OPTIONAL - default: `{group_id}`)
- **java_version**: string - Java target version (OPTIONAL - default: `17`)
- **build_tool**: maven|gradle - Build tool (OPTIONAL - default: `maven`)
- **quarkus_extensions**: string[] - Quarkus extensions to include (OPTIONAL - default: minimal REST + health + openapi + jackson)
- **scaffold_mode**: plan-only|scaffold-only|scaffold-and-wire-basics - How far to go (OPTIONAL - default: scaffold-and-wire-basics)

## User Interaction
- Always ask for user approval before writing or modifying files

## Process

### 1. Practices Loading Phase
You MUST load and internalize ALL practice files before scaffolding:

**Required Practices (MUST load all):**
- Read and apply: `.olaf/data/practices/standards/universal-coding-standards.md`
  - Covers: SRP, Dependency Injection, function size, complexity, naming, error handling
- Read and apply: `.olaf/data/practices/guidances/coding/quarkus-microservice-scaffolding-guidance.md`
  - Covers: Quarkus baseline choices, extensions, structure, tests, quality gates
- Read and apply: `.olaf/data/practices/guidances/git/git-workflow-guidance.md`
  - Covers: Worktree setup, new branch, small commits

You WILL confirm practices are loaded before proceeding.

### 2. Worktree + Branch Verification Phase
You MUST verify Git worktree AND a new branch before starting any file generation:

**Check worktree status:**
- Execute: `git worktree list`
- If user is NOT in a worktree, STOP and guide them to create one.

**Check branch status:**
- Execute: `git status -sb`
- If user is on `main`, `master`, or `develop`, STOP and guide them to create a new branch before any code changes.

### 3. Requirements Intake Phase
You MUST confirm the microservice intent and baseline before proposing scaffolding:

You MUST ask:
- What is the service responsibility (1–2 sentences)?
- Is it REST-only or does it need DB/messaging?
- Confirm `group_id` (org namespace) and any org standards for base package naming.
- Target runtime: JVM only, or also native?
- Required ports, health endpoints path conventions, and logging expectations?

### 4. Proposal Phase (Plan)
You WILL propose:
- Concrete parameter values (output_dir, group_id, artifact_id, base_package)
- Minimal extensions set (default: REST + Jackson + Health + OpenAPI)
- Module structure and first endpoints to include (health + one sample resource if requested)
- Build/run/test commands (`mvn quarkus:dev`, `mvn test`, etc.)
- A small commit plan (scaffold → run → tests → commit)

You MUST ask for explicit agreement:
```
Proceed with scaffolding? (yes/no)
```

### 5. Execution Phase (Only After User Agreement)
You WILL:

#### 5.1 Tooling validation
You MUST validate required tooling is available:
- Java (matching `java_version`)
- Maven/Gradle (matching `build_tool`)

If missing, explain what is missing and propose minimal install steps.

#### 5.2 Scaffold project
You WILL scaffold the Quarkus project under `output_dir`.

Preferred Maven scaffolding approach (example):
- Use Quarkus Maven plugin create goal.

You MUST ensure:
- `application.properties` exists and is minimal, environment-friendly
- Health endpoints are enabled
- OpenAPI endpoint is enabled (if REST present)

#### 5.3 Wire basics (if scaffold_mode=scaffold-and-wire-basics)
You WILL add a minimal baseline:
- A health-style endpoint (or keep default if Quarkus health extension provides)
- A sample `GET /api/ping` resource (optional, but recommended)
- One `@QuarkusTest` verifying the endpoint

#### 5.4 Quality gates
You WILL run or instruct the user to run:
- `mvn test`
- `mvn quarkus:dev` (smoke)

### 6. Commit Guidance Phase
You WILL guide the user toward small, focused commits:
- After scaffolding + green tests, suggest a commit message.

## Output Format
You WILL structure your assistance as:

```
## Practices Applied

## Requirements

## Proposed Scaffold

## Confirmation

## Execution

## Commit Suggestion

## Next Steps
```

## Error Handling
You WILL handle these scenarios:
- **Tooling missing**: Provide minimal install options and stop before scaffolding.
- **output_dir exists**: Stop and ask whether to overwrite, choose another folder, or abort.
- **User wants extra extensions**: Propose minimal additions and explain tradeoffs.

## Success Criteria
You WILL consider the task complete when:
- [ ] Practices are loaded and confirmed
- [ ] Worktree + branch safety verified (or user acknowledged deviation)
- [ ] Quarkus microservice scaffold exists under `output_dir`
- [ ] Basic test(s) exist and pass (or user accepted plan-only mode)
- [ ] Commit suggestion provided
