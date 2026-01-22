# Tutorial: augment-code-unit-test

## Introduction

This tutorial guides you through using the `augment-code-unit-test` skill to iteratively improve unit test coverage for your codebase. By the end, you'll understand how to systematically identify testing gaps and add meaningful tests.

## Prerequisites

Before starting, ensure you have:

- [ ] A codebase with existing tests (even if minimal)
- [ ] Git initialized in your project
- [ ] A dedicated Git worktree for augmentation work
- [ ] Test framework configured for your language
- [ ] Clear scope (file or directory) to improve

## Step-by-Step Instructions

### Step 1: Create a Dedicated Worktree

Set up an isolated environment for test augmentation.

**Action:** Create a worktree specifically for this work.

```bash
# From your main repository
git worktree add ../<project>-augment-unit-test -b augment/unit-tests
cd ../<project>-augment-unit-test
```

**Why This Matters:**
- Isolates test changes from main development
- Allows focused work on test improvement
- Easy to discard if needed

### Step 2: Invoke the Skill

Start a test augmentation session.

**Option A: New Session with Specific Scope**

```
Skill: augment-code-unit-test
Parameters:
  - core_dir: "."
  - scope_path: "internal/syncer"
  - test_command: "go test ./internal/syncer/..."
```

**Option B: Browse Existing Sessions**

```
Skill: augment-code-unit-test
Parameters:
  - core_dir: "."
```

When no `scope_path` is provided, the skill will scan for existing sessions and present options:

```
Found existing sessions:

In-progress sessions:
1. internal/syncer (Last-run: 20260115-1430)
2. pkg/auth (Last-run: 20260114-0900)

Completed sessions:
3. pkg/utils (Last-run: 20260110-1600)

Options:
- Resume an in-progress session
- Restart a completed session
- Start a new session for a different scope

Which would you like to do?
```

### Step 3: Review or Create Tasklist

The skill manages a persistent tasklist for your scope.

**For New Sessions:**

A tasklist is created at `[staging_dir]/unittest/<scope_path>/tasklist.md`:

```markdown
# Unit test improvement – internal/syncer

Session:
- Status: in-progress
- Scope: internal/syncer
- Last-run: 20260116-1000

- [ ] Ensure tests pass for scope `internal/syncer`
  - [ ] Run tests for the scope
  - [ ] Fix failing tests (if any)
- [ ] Identify missing or weak tests in `internal/syncer`
  - [ ] Analyze branches and error paths
  - [ ] Analyze edge cases and boundary conditions
- [ ] Add missing tests for `internal/syncer`
  - [ ] Implement agreed new tests
  - [ ] Re-run tests for safety
```

**For Existing Sessions:**

```
Session found for internal/syncer (in-progress)
Last run: 20260115-1430
Next task: Identify missing or weak tests

Options:
1. Resume from next unchecked task
2. Restart session (append new checklist)

Which would you prefer?
```

### Step 4: Ensure Tests Pass First

The skill always verifies existing tests before adding new ones.

**Action:** Wait for test execution.

```
Running tests for scope: internal/syncer
Command: go test ./internal/syncer/...

Results:
✓ TestSyncerInit (0.02s)
✓ TestSyncerStart (0.15s)
✗ TestSyncerStop (0.03s)
  - Expected: nil error
  - Got: context canceled

1 test failing. Proposing fix...
```

**If Tests Fail:**

The skill will propose minimal fixes:

```
Proposed Fix for TestSyncerStop:

The test expects nil error but the implementation returns 
context.Canceled when Stop() is called. This appears to be 
expected behavior.

Proposed change to test:
- assert.NoError(t, err)
+ assert.ErrorIs(t, err, context.Canceled)

Proceed with this fix? (yes/no)
```

**Action:** Review and approve the fix.

### Step 5: Identify Missing Tests

Once tests pass, the skill analyzes code for gaps.

**Expected Output:**

```
Analyzing code in scope: internal/syncer

Functions/Methods found:
- Syncer.Init() - 2 tests
- Syncer.Start() - 1 test
- Syncer.Stop() - 1 test
- Syncer.handleError() - 0 tests ⚠️
- Syncer.retry() - 0 tests ⚠️

Identified Gaps:
1. handleError() - No tests for error handling paths
2. retry() - No tests for retry logic
3. Start() - Missing test for context cancellation
4. Init() - Missing test for invalid config

Updating tasklist with findings...
```

The tasklist is updated:

```markdown
- [x] Identify missing or weak tests in `internal/syncer`
  - [x] Analyze branches and error paths
  - [x] Analyze edge cases and boundary conditions
  - Findings:
    - handleError(): No coverage
    - retry(): No coverage  
    - Start(): Missing context cancellation test
    - Init(): Missing invalid config test
```

### Step 6: Add Missing Tests

The skill proposes concrete test cases for approval.

**Proposed Tests:**

```
Proposed Test Cases for internal/syncer:

1. TestHandleError_LogsAndReturns
   - Scenario: Error occurs during sync
   - Arrange: Create syncer, inject error
   - Assert: Error logged, returned correctly

2. TestRetry_SucceedsAfterTransientFailure
   - Scenario: First attempt fails, second succeeds
   - Arrange: Mock that fails once then succeeds
   - Assert: Operation completes, retry count = 1

3. TestRetry_ExhaustsAttempts
   - Scenario: All retry attempts fail
   - Arrange: Mock that always fails
   - Assert: Returns error after max attempts

4. TestStart_CancelsOnContextDone
   - Scenario: Context cancelled during start
   - Arrange: Cancel context immediately
   - Assert: Start returns context error

Proceed with implementing these tests? (yes/no/modify)
```

**Action:** Review and approve, or request modifications.

### Step 7: Review Implemented Tests

After approval, tests are implemented and run.

**Example Implementation:**

```go
func TestHandleError_LogsAndReturns(t *testing.T) {
    // Arrange
    logger := &mockLogger{}
    syncer := NewSyncer(WithLogger(logger))
    testErr := errors.New("sync failed")
    
    // Act
    result := syncer.handleError(testErr)
    
    // Assert
    assert.Equal(t, testErr, result)
    assert.Contains(t, logger.LastMessage(), "sync failed")
}

func TestRetry_SucceedsAfterTransientFailure(t *testing.T) {
    // Arrange
    attempts := 0
    operation := func() error {
        attempts++
        if attempts < 2 {
            return errors.New("transient")
        }
        return nil
    }
    
    // Act
    err := retry(operation, 3)
    
    // Assert
    assert.NoError(t, err)
    assert.Equal(t, 2, attempts)
}
```

**Test Results:**

```
Running tests after additions...

✓ TestHandleError_LogsAndReturns (0.01s)
✓ TestRetry_SucceedsAfterTransientFailure (0.02s)
✓ TestRetry_ExhaustsAttempts (0.01s)
✓ TestStart_CancelsOnContextDone (0.03s)

All tests passing. Updating tasklist...
```

### Step 8: Iteration Authorization

After completing a task, the skill asks for next steps.

**Expected Output:**

```
Results Summary:
- 4 new tests added
- All tests passing
- handleError() and retry() now covered

Recommendation: Continue
Next task: Final validation and cleanup

Options:
1. Continue to next task
2. Stop here for now
3. Add more tests for current scope

Proceed to next task? (yes/no)
```

## Verification Checklist

After completing the augmentation session, verify:

- [ ] All checklist items in tasklist.md marked complete
- [ ] Tests for the scope pass successfully
- [ ] Identified missing/weak tests addressed or documented as deferred
- [ ] No trivial or redundant tests added
- [ ] Tests follow team coding standards
- [ ] Changes committed to augmentation branch

## Troubleshooting

### Issue: Tasklist Cannot Be Parsed

**Symptom:** Skill reports tasklist corruption.

**Solution:**
- The skill will back up the corrupted file
- A new minimal tasklist will be created
- Previous content preserved as comments

### Issue: Test Execution Fails

**Symptom:** Tests fail with unexpected errors.

**Solution:**
- Review the failure output provided
- Approve proposed fixes or provide guidance
- Ensure test environment is properly configured

### Issue: Scope Path Not Found

**Symptom:** Skill reports scope doesn't exist.

**Solution:**
- Verify the path is relative to `core_dir`
- Check for typos in the path
- Ensure the directory/file exists

### Issue: No Test Gaps Found

**Symptom:** Skill reports scope is fully covered.

**Solution:**
- Consider expanding scope to parent directory
- Review if coverage metrics are accurate
- Check if complex branches need additional tests

## Next Steps

After completing test augmentation:

1. **Review Changes:** Examine all added tests for quality
2. **Merge to Main:** Create PR from augmentation branch
3. **Clean Up Worktree:** Remove worktree when done
4. **Document Coverage:** Note coverage improvements
5. **Schedule Regular Augmentation:** Plan periodic test improvement sessions
