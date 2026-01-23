# Package Dependencies

## Runtime Limitations

Skills run in the code execution environment with platform-specific limitations:

- **Web platforms**: Can install packages from npm and PyPI and pull from GitHub repositories
- **API access**: Has no network access and no runtime package installation

List required packages in your skill.md and verify they're available in the code execution tool documentation.

## Don't Assume Tools Are Installed

**Bad example: Assumes installation:**
```
"Use the ast library to analyze the code."
```

**Good example: Explicit about dependencies:**
```
"Install required package: `pip install radon`

Then use it:
```python
from radon.complexity import cc_visit
results = cc_visit(source_code)
```"
```
