# Plan Angular Migration

## Overview

This competency creates comprehensive, chapter-based Angular migration plans for version upgrades. It performs in-depth discovery, compatibility analysis, strategic planning, and generates actionable implementation roadmaps with safety-first principles.

## Purpose

Angular version migrations are complex undertakings that require careful planning to avoid breaking changes, dependency conflicts, and runtime failures. This competency systematically analyzes your Angular project, identifies compatibility issues, plans incremental upgrades, and generates detailed roadmaps that account for environment requirements, third-party dependencies, and architectural patterns.

## Usage

**Command**: `plan angular migration` (or aliases: `plan angular upgrade`, `angular migration plan`, `create angular migration strategy`)

**Protocol**: Propose-Confirm-Act

**When to Use**: Use when you need to plan an Angular version upgrade, analyze migration feasibility before starting work, assess risks and breaking changes, or create a detailed implementation strategy for Angular migrations.

## Parameters

### Required Inputs
- **source_angular_version**: Current Angular version (e.g., "13", "16.2.0")
- **target_angular_version**: Desired target Angular version (e.g., "20", "19.0.0")
- **project_path**: Path to Angular project (defaults to current directory)

### Optional Inputs
- **project_name**: Name of project for plan identification
- **incremental_upgrade**: Whether to plan version-by-version migration (default: true for multi-version jumps)
- **backend_integration**: Specify if Angular is integrated with backend build system
- **architecture_notes**: Additional context about micro-frontends, special patterns

### Context Requirements
- Valid Angular project with angular.json and package.json
- Access to project dependencies and configuration files
- Understanding of target Angular version and requirements
- Node.js and npm/yarn available for environment assessment

## Output

Generates a comprehensive 4-chapter migration plan with detailed analysis and actionable roadmap.

**Deliverables**:
- **Chapter 0**: Pre-Planning Validation (compatibility matrix, architecture detection, dependency matrix)
- **Chapter 1**: Discovery and Current State Analysis (project structure, dependencies, features)
- **Chapter 2**: Compatibility Assessment and Gap Analysis (breaking changes, Node.js requirements, library compatibility)
- **Chapter 3**: Migration Planning and Strategy (incremental approach, command sequencing, risk mitigation)
- **Chapter 4**: Implementation Roadmap (step-by-step instructions, validation criteria, rollback procedures)
- **Plan ID**: Unique identifier for tracking execution state
- **Execution Context**: JSON structure for migration state management

**Format**: Markdown plan file saved to `.angular-migration/plan.md`

## Related Competencies

- **execute-angular-migration**: Follow-up competency that executes the generated migration plan step-by-step
- **review-code**: Can be used to review Angular code before migration planning
- **generate-implementation-plan**: Generic implementation planning that can complement migration strategy

## Tips & Best Practices

- Always run Chapter 0 pre-planning validation to access official compatibility matrix
- Plan Node.js upgrades proactively before Angular versions that require them
- Use incremental upgrades for multi-version jumps (safer than direct upgrades)
- Consult bundled dependency matrix for exact third-party library versions
- Review plan carefully before execution - pay attention to environment upgrade points
- Consider running plan multiple times if project structure changes
- Use generated Plan ID for tracking execution state during implementation
- Factor in MDC migration time for Angular 17+ targets (significant UI changes)
- Research third-party library compatibility early using GitHub issues
- Plan for adequate testing time between incremental version steps
