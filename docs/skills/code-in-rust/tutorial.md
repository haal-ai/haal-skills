# Code in Rust - Tutorial

## Quick Start

### Step 1: Invoke the Skill

```
olaf code in rust
```

The skill will:
1. Load all practice files
2. Check your Git worktree status
3. Be ready to assist with Rust coding

### Step 2: Describe Your Task

Tell the skill what you want to implement:

```
I need to add a repository trait and service that fetches users from a database
```

### Step 3: Follow the Guidance

The skill will:
- Suggest setting up a worktree if you haven't
- Provide code that follows all loaded practices
- Remind you to commit after changes

## Example Session

**User**: olaf code in rust - I need to validate email addresses in a request model

**Skill Response**:
```
🔧 Rust Coding Session Active

Loaded practices:
- Universal Coding Standards (SOLID, DI, complexity limits)
- Rust Coding Guidance (idioms, error handling, testing)
- Git Workflow Guidance (worktree, small commits)

## Worktree Check
[Verifies you're in a worktree or guides setup]

## Implementation

Here's a small email validation helper following our practices:

```rust
use anyhow::{anyhow, Result};

pub fn validate_email(email: &str) -> Result<()> {
    if email.trim().is_empty() {
        return Err(anyhow!("validate email: empty value"));
    }

    if !email.contains('@') {
        return Err(anyhow!("validate email: missing '@'"));
    }

    Ok(())
}
```

## Commit Suggestion
```
feat(validation): add basic email validation helper

- Validate non-empty email and presence of '@'
```

## Next Steps
1. Add unit tests (table-driven style)
2. Run `cargo fmt` and `cargo clippy`
3. Commit this change
```

## Practice Violation Example

If you request code that violates practices:

**User**: Can you just unwrap the DB result to keep it short?

**Skill Response**:
```
⚠️ Practice Violation Detected

The requested approach violates: Rust Coding Guidance - Error Handling
Guidance says: "Avoid unwrap/expect except in tests or unreachable states"

Compliant alternative:

```rust
pub fn get_user(id: &str) -> anyhow::Result<User> {
    let user = db.find_user(id).context("find user")?;
    Ok(user)
}
```

This returns a `Result` and adds error context.
```

## Tips

1. **Always start with worktree**: The skill will remind you, but it's faster to set up beforehand
2. **Describe intent, not implementation**: Let the skill suggest practice-compliant approaches
3. **Commit frequently**: Follow the skill's commit suggestions to maintain small changesets
4. **Ask about violations**: If you disagree with a practice, discuss it - the skill will explain the rationale
