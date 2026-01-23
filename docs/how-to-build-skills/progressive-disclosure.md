# Progressive Disclosure

Skills run in a code execution environment with filesystem access. This enables progressive disclosure—loading content on-demand rather than all at once.

## How the Agent Accesses Skills

- **Metadata pre-loaded**: At startup, the name and description from all Skills' YAML frontmatter are loaded into the system prompt
- **Files read on-demand**: The agent uses bash Read tools to access skill.md and other files from the filesystem when needed
- **Scripts executed efficiently**: Utility scripts can be executed via bash without loading their full contents into context. Only the script's output consumes tokens
- **No context penalty for large files**: Reference files, data, or documentation don't consume context tokens until actually read

## Best Practices

- **File paths matter**: The agent navigates your skill directory like a filesystem. Use forward slashes (`reference/guide.md`), not backslashes
- **Name files descriptively**: Use names that indicate content: `error_handling_patterns.md`, not `doc2.md`
- **Organize for discovery**: Structure directories by domain or feature
  - Good: `reference/naming.md`, `reference/error-handling.md`
  - Bad: `docs/file1.md`, `docs/file2.md`
- **Bundle comprehensive resources**: Include complete style guides, extensive examples, large pattern libraries; no context penalty until accessed
- **Prefer scripts for deterministic operations**: Write `analyze_complexity.py` rather than asking the agent to generate analysis code
- **Test file access patterns**: Verify the agent can navigate your directory structure by testing with real requests

## Example Structure

```
refactoring-skill/
├── skill.md (overview, points to reference files)
└── reference/
    ├── naming.md (naming conventions)
    ├── error-handling.md (exception patterns)
    └── logging.md (logging standards)
```

When the user asks about error handling, the agent reads skill.md, sees the reference to `reference/error-handling.md`, and reads just that file. The `naming.md` and `logging.md` files remain on the filesystem, consuming zero context tokens until needed.
