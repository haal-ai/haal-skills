# Onboard Me - Skill Description

## Overview

The **onboard-me** skill generates persona-focused quick start guides that help new team members become productive in 30 minutes. It analyzes any repository and creates tailored onboarding documentation for different developer roles (Frontend, Backend, QA, DevOps, etc.).

## Purpose

New team members often face overwhelming documentation or none at all. This skill:
- Analyzes repository structure, tech stack, and build systems automatically
- Detects relevant developer personas based on technologies used
- Generates focused, actionable quick start guides for each persona
- Provides concrete "first task" examples to build confidence

## Key Features

- **Automatic Analysis**: Scans repository to extract languages, frameworks, entry points, and commands
- **Persona Detection**: Identifies 3-6 relevant developer roles based on tech stack
- **30-Minute Guides**: Each guide is structured to get someone productive in half an hour
- **Practical Focus**: Includes setup, build, key files, and a first coding task
- **Universal**: Works with any programming language or framework

## When to Use

Use this skill when:
- Onboarding new team members to a codebase
- Creating developer documentation for a new repository
- Migrating teams to a new project
- Improving existing onboarding materials
- You need quick start guides for multiple developer personas

## Typical Output

For a TypeScript/React + Python/FastAPI project, generates:
- `QUICKSTART-FRONTEND-DEVELOPER.md`
- `QUICKSTART-BACKEND-DEVELOPER.md`
- `QUICKSTART-QA-ENGINEER.md`
- `QUICKSTART-DEVOPS-ENGINEER.md`
- `QUICKSTART-ARCHITECT.md`
- `QUICKSTART-OVERVIEW.md` (linked index of all guides)

Each guide contains:
- What you'll build (concrete goal)
- 5-min setup instructions
- 5-min build & run verification
- 10-min code walkthrough
- 10-min first change exercise
- Common tasks reference

## Benefits

- **Reduces onboarding time** from days to hours
- **Persona-specific** content eliminates irrelevant information
- **Actionable** tasks build confidence through immediate success
- **Consistent** format across all repositories
- **Maintainable** generated from code analysis, stays up-to-date

## Skill Type

**Protocol**: Act  
**Exposure**: Export  
**Status**: Mainstream
