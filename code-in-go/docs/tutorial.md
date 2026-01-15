# Code in Go - Tutorial

## Quick Start

### Step 1: Invoke the Skill

```
olaf code in go
```

The skill will:
1. Load all practice files
2. Check your Git worktree status
3. Be ready to assist with Go coding

### Step 2: Describe Your Task

Tell the skill what you want to implement:

```
I need to create a User service that fetches users from a database
```

### Step 3: Follow the Guidance

The skill will:
- Suggest setting up a worktree if you haven't
- Provide code that follows all loaded practices
- Remind you to commit after changes

## Example Session

**User**: olaf code in go - I need to add a function to validate email addresses

**Skill Response**:
```
🔧 Go Coding Session Active

Loaded practices:
- Universal Coding Standards (SOLID, DI, complexity limits)
- Go Coding Guidance (idioms, error handling, testing)
- Git Workflow Guidance (worktree, small commits)

## Worktree Check
[Verifies you're in a worktree or guides setup]

## Implementation

Here's an email validation function following our practices:

```go
package validation

import (
    "fmt"
    "regexp"
)

var emailRegex = regexp.MustCompile(`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)

// ValidateEmail checks if the provided email address is valid.
// Returns an error with context if validation fails.
func ValidateEmail(email string) error {
    if email == "" {
        return fmt.Errorf("validate email: %w", ErrEmptyEmail)
    }
    if !emailRegex.MatchString(email) {
        return fmt.Errorf("validate email %q: %w", email, ErrInvalidFormat)
    }
    return nil
}
```

## Commit Suggestion
```
feat(validation): add email validation function

Implements RFC 5322 basic email format validation.
```

## Next Steps
1. Add unit tests using table-driven pattern
2. Commit this change
3. Continue with next validation function
```

## Practice Violation Example

If you request code that violates practices:

**User**: Can you add a function that ignores the error from the database call?

**Skill Response**:
```
⚠️ Practice Violation Detected

The requested approach violates: Go Coding Guidance - Error Handling
Guidance says: "Always check errors: Never ignore returned errors with _"

Compliant alternative:

```go
func GetUser(ctx context.Context, id string) (*User, error) {
    user, err := db.FindUser(ctx, id)
    if err != nil {
        return nil, fmt.Errorf("get user %s: %w", id, err)
    }
    return user, nil
}
```

This properly handles and wraps the error with context.
```

## Tips

1. **Always start with worktree**: The skill will remind you, but it's faster to set up beforehand
2. **Describe intent, not implementation**: Let the skill suggest practice-compliant approaches
3. **Commit frequently**: Follow the skill's commit suggestions to maintain small changesets
4. **Ask about violations**: If you disagree with a practice, discuss it - the skill will explain the rationale
