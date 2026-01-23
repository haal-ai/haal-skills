# Utility Scripts

Even if the agent could write a script, pre-made scripts offer advantages.

## Benefits of Utility Scripts

- More reliable than generated code
- Save tokens (no need to include code in context)
- Save time (no code generation required)
- Ensure consistency across uses

## Execution vs Reference

Make clear in your instructions whether the agent should:

- **Execute the script** (most common): "Run analyze_complexity.py to find functions needing refactoring"
- **Read it as reference** (for complex logic): "See analyze_complexity.py for the complexity calculation algorithm"

For most utility scripts, execution is preferred because it's more reliable and efficient.

## Example Documentation

```markdown
## Utility scripts

**analyze_complexity.py**: Find functions with high cyclomatic complexity

```bash
python scripts/analyze_complexity.py src/ > complexity_report.json
```

Output format:
```json
{
  "src/auth/login.py::authenticate": {"complexity": 15, "lines": 45},
  "src/utils/parser.py::parse_config": {"complexity": 12, "lines": 30}
}
```

**find_duplicates.py**: Detect duplicate code blocks

```bash
python scripts/find_duplicates.py src/
# Returns: list of similar code blocks with file locations
```

**extract_method.py**: Helper to extract a method from a function

```bash
python scripts/extract_method.py src/auth/login.py authenticate 10 25 validate_credentials
```
```
