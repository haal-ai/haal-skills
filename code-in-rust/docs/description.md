# Code in Rust

## Overview

The **Code in Rust** skill provides Rust development assistance while strictly enforcing team practices. It loads coding standards, Rust-specific guidance, and Git workflow practices from the local `.olaf/data/practices/` folder and ensures all code assistance adheres to these standards.

## Key Features

- **Practice Enforcement**: Automatically loads and enforces all relevant practices
- **SOLID Principles**: Ensures code follows SRP, Dependency Injection, and other SOLID principles
- **Rust Idioms**: Applies Rust best practices for error handling, naming, module structure, and ownership
- **Git Workflow**: Verifies worktree usage, requires a new branch before coding, and guides toward small, frequent commits
- **Violation Alerts**: Warns when requested code would violate loaded practices
- **Phased Delivery**: Collects requirements, performs impact analysis, proposes a solution, and asks for explicit approval before generating code

## Practices Loaded

1. **Universal Coding Standards** (`standards/universal-coding-standards.md`)
   - Single Responsibility Principle
   - Dependency Injection
   - Function size and complexity limits
   - Naming and readability

2. **Rust Coding Guidance** (`guidances/coding/rust-coding-guidance.md`)
   - Rust idioms and conventions
   - Error handling patterns
   - Project structure
   - Testing practices

3. **Git Workflow Guidance** (`guidances/git/git-workflow-guidance.md`)
   - Worktree setup before coding
   - Small, focused commits
   - Commit message format
   - Branch strategy

## When to Use

Use this skill when:
- Starting a Rust coding session
- Implementing new Rust features
- Refactoring existing Rust code
- You want strict enforcement of team practices

## Trigger Phrases

- "olaf code in rust"
- "olaf rust coding"
- "olaf rust assistance"
- "olaf rust development"
