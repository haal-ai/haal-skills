# Scaffold Quarkus Microservice

## Overview

The **Scaffold Quarkus Microservice** skill helps developers start a new Quarkus microservice in a standards-compliant way.

It strictly enforces practices loaded from `.olaf/data/practices/` (universal coding standards, Quarkus scaffolding guidance, and Git workflow guidance) and follows **Propose → Confirm → Act** before writing files.

## Key Features

- **Practice Enforcement**: Loads and applies required practices before scaffolding
- **Git Safety**: Requires Git worktree + new branch checks before generating files
- **Minimal-by-default**: Proposes a small extension set unless requirements demand more
- **Runnable Baseline**: Produces a service that can run locally with `mvn quarkus:dev`
- **Testing Baseline**: Adds at least one smoke test (`@QuarkusTest`) when generating code

## Practices Loaded

1. **Universal Coding Standards** (`standards/universal-coding-standards.md`)
2. **Quarkus Microservice Scaffolding Guidance** (`guidances/coding/quarkus-microservice-scaffolding-guidance.md`)
3. **Git Workflow Guidance** (`guidances/git/git-workflow-guidance.md`)

## When to Use

Use this skill when:
- Creating a new microservice from scratch
- You want consistent Quarkus baselines across projects
- You want scaffolding done with Git workflow safety checks

## Trigger Phrases

- "olaf scaffold quarkus microservice"
- "olaf create quarkus microservice"
- "olaf scaffold quarkus service"
- "olaf scaffold qurkus microservice"
