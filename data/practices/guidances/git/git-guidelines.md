# Git Commit Guidelines

## Commit Message Format

### Structure
```
type: Brief description of what was accomplished

- Key change or improvement made
- Another significant change
- Additional context or benefit
```

### Commit Types
- **feat**: New feature or capability
- **fix**: Bug fix or issue resolution
- **docs**: Documentation updates
- **refactor**: Code restructuring without behavior change
- **chore**: Maintenance tasks, dependencies
- **test**: Adding or updating tests

## Writing Guidelines

### Focus on Accomplishments
✅ **Good**: Describe what was accomplished
- "feat: Add changelog system with template-driven generation"
- "fix: Resolve authentication timeout issues"
- "docs: Update installation guide for simplified setup"

❌ **Avoid**: File listings or technical details
- "feat: Add files changelog.md, template.md, manifest.json"
- "fix: Change line 42 in auth.js and update config.json"

### Content Principles
1. **Lead with impact**: What capability was added or problem solved?
2. **Be action-oriented**: Use active voice and clear verbs
3. **Keep it concise**: Focus on essential changes only
4. **Skip file details**: Git tracks files automatically
5. **Highlight benefits**: Why this change matters

## Examples

### Feature Addition
```
feat: Add product changelog system with dual functional/technical tracking

- Add new competency for template-driven changelog generation
- Implement functional and technical changelog templates
- Create dual changelog structure with linked detail files
- Enable web-publishable format for improved user communication
```

### Bug Fix
```
fix: Resolve competency loading timeout in large repositories

- Optimize competency indexing for better performance
- Add fallback mechanisms for network issues
- Improve error handling for missing dependencies
```

### Documentation
```
docs: Update contribution guidelines for new workflow

- Clarify setup steps for development environment
- Add examples for common contribution scenarios
- Update testing procedures for quality assurance
```

## Team Standards

- Maximum 72 characters for the first line
- Use bullet points for multiple changes
- Present tense, imperative mood ("Add" not "Added" or "Adds")
- No period at the end of the subject line
- Separate subject from body with blank line if using multi-line format

## Team Conventions (lightweight)

- **Scope (optional)**: Use `type(scope): subject` when it clarifies the area (e.g., `docs(rules): ...`). Keep scopes short.
- **Issue linking**: In the body, add `Refs #123` or `Fixes #123` when relevant.
- **When to add a body**: Add a body if the change is non-trivial, touches multiple files, or benefits from 1–3 bullets. Otherwise, a single-line commit is fine.
- **Breaking changes**: If applicable, include a body line starting with `BREAKING CHANGE:` followed by a short description.
- **Mechanical changes**: Use `chore:` for mass renames, formatting, or dependency bumps. Avoid mixing with feature or fix changes.
- **Subject casing**: Sentence case after the type (e.g., `feat: Add CLI to seed collections`).
- **Trailers (optional)**: Support `Co-authored-by:` and `Signed-off-by:` lines when appropriate.
- **Emojis**: Avoid using emojis in commit subjects.

## Quick examples

Single-line, trivial change:
```
docs: Update install steps for Windows
```

Non-trivial with body and issue reference:
```
feat(rules): Add intent-based context injector

- Detect git, review, code, and testing intents
- Load matching practices into assistant context
Refs #123
```

Breaking change called out:
```
refactor(api): Simplify prompt conversion interface

- Remove deprecated convertV1 function
- Align options with new schema
BREAKING CHANGE: convertV1 removed; use convert(options) instead