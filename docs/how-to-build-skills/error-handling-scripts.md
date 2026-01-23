# Error Handling in Scripts

When writing scripts for Skills, handle error conditions explicitly rather than letting them fail and leaving the agent to figure it out.

## Good Example: Handle Errors Explicitly

```python
def process_file(path):
    """Process a file, creating it if it doesn't exist."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        # Create file with default content instead of failing
        print(f"File {path} not found, creating default")
        with open(path, 'w') as f:
            f.write('')
        return ''
    except PermissionError:
        # Provide alternative instead of failing
        print(f"Cannot access {path}, using default")
        return ''
```

## Bad Example: Let It Fail

```python
def process_file(path):
    # Just fail and let the agent figure it out
    return open(path).read()
```

## Self-Documenting Configuration

Configuration parameters should be justified and documented to avoid unexplained "magic numbers." If you don't know the right value, how will the agent determine it?

**Good example: Self-documenting:**

```python
# Functions with more than 20 lines often indicate need for extraction
# This threshold balances readability vs over-fragmentation
MAX_FUNCTION_LINES = 20

# Cyclomatic complexity above 10 suggests refactoring needed
# Based on industry standard thresholds
MAX_COMPLEXITY = 10
```

**Bad example: Magic numbers:**

```python
MAX_LINES = 47  # Why 47?
COMPLEXITY = 15   # Why 15?
```
