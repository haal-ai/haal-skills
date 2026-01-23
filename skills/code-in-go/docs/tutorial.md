# Tutorial: code-in-go

## Introduction

This tutorial guides you through using the `code-in-go` skill to receive Go coding assistance that enforces team practices, SOLID principles, and Git workflow standards. By the end, you'll understand how to get practice-compliant code assistance for your Go projects.

## Prerequisites

Before starting, ensure you have:

- [ ] A Go project in your workspace
- [ ] Git initialized in your project
- [ ] Practice files available (or willingness to create them):
  - `.olaf/data/practices/standards/universal-coding-standards.md`
  - `.olaf/data/practices/guidances/coding/go-coding-guidance.md`
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
Skill: code-in-go
Parameters:
  - task_description: "Implement retry logic for HTTP client with exponential backoff"
  - working_directory: "./pkg/httpclient"
```

**Or with a work item reference:**

```
Skill: code-in-go
Parameters:
  - reference: "PROJ-789"
```

**Expected Response:**
```
🔧 Go Coding Session Active

Loaded practices:
- Universal Coding Standards (SOLID, DI, complexity limits)
- Go Coding Guidance (idioms, error handling, testing)
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
- Files impacted: pkg/httpclient/client.go, pkg/httpclient/retry.go (new)
- New interfaces: Retryer interface for dependency injection
- Risks: May affect existing timeout behavior

## Proposed Solution
1. Create Retryer interface with configurable strategy
2. Implement ExponentialBackoff strategy
3. Inject Retryer into HTTPClient
4. Add table-driven tests for retry scenarios

## Test Plan
- Test successful retry after transient failure
- Test max retries exceeded
- Test backoff timing
- Test context cancellation during retry
```

**Action:** Review the analysis and confirm to proceed.

```
Proceed with implementation? (yes/no)
```

### Step 5: Receive Implementation

After approval, receive practice-compliant code.

**Example Output:**

```go
// retry.go - New file
package httpclient

import (
    "context"
    "time"
)

// Retryer defines the interface for retry strategies
type Retryer interface {
    ShouldRetry(attempt int, err error) bool
    Delay(attempt int) time.Duration
}

// ExponentialBackoff implements Retryer with exponential delay
type ExponentialBackoff struct {
    MaxAttempts int
    BaseDelay   time.Duration
    MaxDelay    time.Duration
}

// ShouldRetry returns true if another attempt should be made
func (e *ExponentialBackoff) ShouldRetry(attempt int, err error) bool {
    if attempt >= e.MaxAttempts {
        return false
    }
    return isRetryableError(err)
}

// Delay calculates the delay before the next retry
func (e *ExponentialBackoff) Delay(attempt int) time.Duration {
    delay := e.BaseDelay * time.Duration(1<<uint(attempt))
    if delay > e.MaxDelay {
        return e.MaxDelay
    }
    return delay
}
```

**Notice:**
- Functions under 30 lines
- Clear interface definition for DI
- Proper error handling patterns

### Step 6: Review Generated Tests

The skill generates table-driven tests.

**Example Test Output:**

```go
// retry_test.go
package httpclient

import (
    "testing"
    "time"
)

func TestExponentialBackoff_ShouldRetry(t *testing.T) {
    tests := []struct {
        name        string
        maxAttempts int
        attempt     int
        err         error
        want        bool
    }{
        {
            name:        "first attempt with retryable error",
            maxAttempts: 3,
            attempt:     0,
            err:         errTemporary,
            want:        true,
        },
        {
            name:        "max attempts exceeded",
            maxAttempts: 3,
            attempt:     3,
            err:         errTemporary,
            want:        false,
        },
        // ... more test cases
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            eb := &ExponentialBackoff{MaxAttempts: tt.maxAttempts}
            got := eb.ShouldRetry(tt.attempt, tt.err)
            if got != tt.want {
                t.Errorf("ShouldRetry() = %v, want %v", got, tt.want)
            }
        })
    }
}
```

### Step 7: Follow Commit Guidance

After implementation, receive commit suggestions.

**Expected Output:**
```markdown
## Commit Suggestion
feat(httpclient): add retry logic with exponential backoff

## Commit Checklist
- [ ] Code compiles: `go build ./...`
- [ ] Tests pass: `go test ./...`
- [ ] Linter passes: `golangci-lint run`
- [ ] Single concern per commit
```

**Action:** Run the checklist and commit your changes.

```bash
go build ./...
go test ./...
golangci-lint run
git add .
git commit -m "feat(httpclient): add retry logic with exponential backoff"
```

## Verification Checklist

After completing your coding session, verify:

- [ ] All practice files loaded and applied
- [ ] Worktree status verified (or deviation acknowledged)
- [ ] Code assistance provided following ALL practices
- [ ] Functions under 30 lines with complexity under 10
- [ ] Proper error handling with wrapping
- [ ] Dependency injection applied for external dependencies
- [ ] Table-driven tests generated for all changes
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

### Issue: Complex Requirement

**Symptom:** Task is too large for single implementation.

**Solution:**
- Allow the skill to break down into smaller increments
- Implement one increment at a time
- Commit after each logical change

### Issue: Git Not Available

**Symptom:** Skill warns about Git workflow enforcement.

**Solution:**
- Initialize Git in your project: `git init`
- Or acknowledge that Git workflow guidance won't be enforced

## Next Steps

After completing your coding session:

1. **Push Changes:** Push your feature branch to remote
2. **Create PR:** Open a pull request for code review
3. **Continue Development:** Start new session for next task
4. **Review Code:** Use `review-code` skill for self-review
5. **Improve Tests:** Use `augment-code-unit-test` for coverage improvement
