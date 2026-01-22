# Tutorial: code-in-rust

## Introduction

This tutorial guides you through using the `code-in-rust` skill to receive Rust coding assistance that enforces team practices, SOLID principles, and Git workflow standards. By the end, you'll understand how to get practice-compliant code assistance for your Rust projects.

## Prerequisites

Before starting, ensure you have:

- [ ] A Rust project in your workspace (with `Cargo.toml`)
- [ ] Git initialized in your project
- [ ] Practice files available (or willingness to create them):
  - `.olaf/data/practices/standards/universal-coding-standards.md`
  - `.olaf/data/practices/guidances/coding/rust-coding-guidance.md`
  - `.olaf/data/practices/guidances/git/git-workflow-guidance.md`
- [ ] A clear task or work item reference

## Step-by-Step Instructions

### Step 1: Prepare Your Development Environment

Set up a proper Git worktree for isolated development.

**Action:** Create a worktree for your feature work.

```bash
# From your main repository
git worktree add ../feature-worktree -b feature/my-feature
cd ../feature-worktree
```

**Why This Matters:**
- Isolates your changes from the main codebase
- Allows parallel development on multiple features
- Follows Git workflow best practices

### Step 2: Invoke the Skill

Start a coding session with your task details.

**Action:** Provide the required parameters.

```
Skill: code-in-rust
Parameters:
  - task_description: "Implement configuration file parser with validation"
  - working_directory: "./crates/config"
```

**Or with a work item reference:**

```
Skill: code-in-rust
Parameters:
  - reference: "PROJ-789"
```

**Expected Response:**
```
🔧 Rust Coding Session Active

Loaded practices:
- Universal Coding Standards (SOLID, DI, complexity limits)
- Rust Coding Guidance (idioms, error handling, testing)
- Git Workflow Guidance (worktree, small commits)

All code assistance will strictly follow these practices.
```

### Step 3: Verify Worktree and Branch

The skill will check your Git environment.

**If Not in Worktree:**
```
⚠️ WORKTREE REQUIRED

You are not working in a Git worktree. Per our Git workflow guidance,
you should isolate your changes in a worktree before coding.

Setup commands:
git worktree add ../feature-worktree -b feature/<your-feature>
cd ../feature-worktree

Shall I help you set up a worktree now?
```

**If on Protected Branch:**
```
⚠️ NEW BRANCH REQUIRED

You are on a protected branch. Per our Git workflow guidance,
you MUST create a new branch before starting coding.

Example:
git checkout -b feature/<issue-id>-<short-description>
```

**Action:** Follow the guidance to set up proper environment, or acknowledge deviation.

### Step 4: Review Impact Analysis

The skill analyzes your request before implementation.

**Expected Output:**
```markdown
## Impact Analysis
- Files impacted: crates/config/src/lib.rs, crates/config/src/parser.rs (new)
- New interfaces: ConfigParser trait for dependency injection
- Risks: May need to update existing config consumers

## Proposed Solution
1. Define ConfigError enum with thiserror
2. Create ConfigParser trait for abstraction
3. Implement TomlConfigParser
4. Add validation logic with descriptive errors
5. Write unit tests for parsing and validation

## Test Plan
- Test valid configuration parsing
- Test missing required fields
- Test invalid field values
- Test malformed TOML handling
```

**Action:** Review the analysis and confirm to proceed.

```
Proceed with implementation? (yes/no)
```

### Step 5: Receive Implementation

After approval, receive practice-compliant code.

**Example Output:**

```rust
// error.rs - New file
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ConfigError {
    #[error("failed to read config file: {0}")]
    IoError(#[from] std::io::Error),
    
    #[error("failed to parse TOML: {0}")]
    ParseError(#[from] toml::de::Error),
    
    #[error("validation failed: {field} - {message}")]
    ValidationError {
        field: String,
        message: String,
    },
}

pub type Result<T> = std::result::Result<T, ConfigError>;
```

```rust
// parser.rs - New file
use crate::error::{ConfigError, Result};
use std::path::Path;

/// Trait for configuration parsing strategies
pub trait ConfigParser {
    type Config;
    
    fn parse(&self, content: &str) -> Result<Self::Config>;
    fn parse_file(&self, path: &Path) -> Result<Self::Config>;
}

/// TOML configuration parser implementation
pub struct TomlConfigParser<T> {
    _marker: std::marker::PhantomData<T>,
}

impl<T> TomlConfigParser<T> {
    pub fn new() -> Self {
        Self {
            _marker: std::marker::PhantomData,
        }
    }
}

impl<T> ConfigParser for TomlConfigParser<T>
where
    T: serde::de::DeserializeOwned,
{
    type Config = T;
    
    fn parse(&self, content: &str) -> Result<Self::Config> {
        toml::from_str(content).map_err(ConfigError::from)
    }
    
    fn parse_file(&self, path: &Path) -> Result<Self::Config> {
        let content = std::fs::read_to_string(path)?;
        self.parse(&content)
    }
}
```

**Notice:**
- Functions under 30 lines
- Trait-based dependency injection
- Proper error handling with `Result` and `thiserror`
- No `unwrap()` or `expect()` in production code

### Step 6: Review Generated Tests

The skill generates comprehensive unit tests.

**Example Test Output:**

```rust
// parser_test.rs
#[cfg(test)]
mod tests {
    use super::*;
    use serde::Deserialize;

    #[derive(Debug, Deserialize, PartialEq)]
    struct TestConfig {
        name: String,
        port: u16,
    }

    #[test]
    fn test_parse_valid_toml() {
        let parser = TomlConfigParser::<TestConfig>::new();
        let content = r#"
            name = "test-app"
            port = 8080
        "#;
        
        let result = parser.parse(content);
        
        assert!(result.is_ok());
        let config = result.unwrap();
        assert_eq!(config.name, "test-app");
        assert_eq!(config.port, 8080);
    }

    #[test]
    fn test_parse_missing_field() {
        let parser = TomlConfigParser::<TestConfig>::new();
        let content = r#"name = "test-app""#;
        
        let result = parser.parse(content);
        
        assert!(result.is_err());
        assert!(matches!(result, Err(ConfigError::ParseError(_))));
    }

    #[test]
    fn test_parse_invalid_toml() {
        let parser = TomlConfigParser::<TestConfig>::new();
        let content = "this is not valid toml {{{";
        
        let result = parser.parse(content);
        
        assert!(result.is_err());
    }
}
```

### Step 7: Follow Commit Guidance

After implementation, receive commit suggestions.

**Expected Output:**
```markdown
## Commit Suggestion
feat(config): add TOML configuration parser with validation

## Commit Checklist
- [ ] Code builds: `cargo build`
- [ ] Tests pass: `cargo test`
- [ ] Formatting applied: `cargo fmt`
- [ ] Clippy clean: `cargo clippy`
- [ ] Single concern per commit
```

**Action:** Run the checklist and commit your changes.

```bash
cargo build
cargo test
cargo fmt
cargo clippy -- -D warnings
git add .
git commit -m "feat(config): add TOML configuration parser with validation"
```

## Verification Checklist

After completing your coding session, verify:

- [ ] All practice files loaded and applied
- [ ] Worktree status verified (or deviation acknowledged)
- [ ] Code assistance provided following ALL practices
- [ ] Functions under 30 lines with complexity under 10
- [ ] Proper error handling with `Result` and context
- [ ] Dependency injection applied via traits
- [ ] Unit tests generated for all changes
- [ ] No `unwrap()`/`expect()` in production code (only tests)
- [ ] Commit guidance provided for changes made
- [ ] User's coding task addressed

## Troubleshooting

### Issue: Practice File Not Found

**Symptom:** Skill reports missing practice files.

**Solution:**
- Create the missing practice files in the expected locations
- Or acknowledge that you want to proceed without certain practices

### Issue: Practice Violation Detected

**Symptom:** Skill warns about practice violation.

```
⚠️ Practice Violation Detected

The requested approach violates: [specific practice]
Guidance says: [quote from practice file]

Compliant alternative: [provided alternative]
```

**Solution:**
- Review the compliant alternative provided
- If you must deviate, explicitly acknowledge the risks
- Document the deviation for future reference

### Issue: Unsafe Code Requested

**Symptom:** Task requires `unsafe` block.

**Solution:**
- Provide clear justification for why `unsafe` is necessary
- The skill will require extra tests for unsafe code
- Consider if there's a safe alternative

### Issue: Complex Requirement

**Symptom:** Task is too large for single implementation.

**Solution:**
- Allow the skill to break down into smaller increments
- Implement one increment at a time
- Commit after each logical change

## Next Steps

After completing your coding session:

1. **Push Changes:** Push your feature branch to remote
2. **Create PR:** Open a pull request for code review
3. **Continue Development:** Start new session for next task
4. **Review Code:** Use `review-code` skill for self-review
5. **Improve Tests:** Use `augment-code-unit-test` for coverage improvement
