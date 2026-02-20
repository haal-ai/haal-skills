# Portability and Frontmatter

Skills built with OLAF follow the [Agent Skills open standard](https://agentskills.io), originally developed by Anthropic and adopted by VS Code / GitHub Copilot, Claude Code, OpenCode, Augment, Vercel AI SDK, and others.

To keep your skills portable across all these platforms, stick to the spec.

## The Open Standard Frontmatter

The specification defines only these top-level frontmatter fields:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | Max 64 chars, lowercase, hyphens only |
| `description` | Yes | Max 1024 chars. What the skill does AND when to use it |
| `license` | No | License name or reference |
| `compatibility` | No | Max 500 chars. Environment requirements |
| `metadata` | No | Freeform key-value map for extensions |

That's it. Anything else is a vendor extension.

## Use `metadata` for Extensions, Not Top-Level Fields

The spec provides `metadata` as the escape hatch for tool-specific or organization-specific data. OLAF uses it for tags, author, and provider:

```yaml
---
name: review-code
description: Comprehensive code review with quality, security, and maintainability focus.
license: Apache-2.0
metadata:
  olaf_tags: [code-quality, review]
  author: your-name
  provider: Haal AI
---
```

This is safe — any agent that doesn't understand `olaf_tags` will simply ignore the `metadata` block.

## Avoid Vendor-Specific Top-Level Fields

Some platforms add their own top-level frontmatter fields. For example, VS Code / GitHub Copilot defines:

- `argument-hint` — hint text for slash command input
- `user-invokable` — controls slash command visibility
- `disable-model-invocation` — prevents auto-loading by the agent

These work fine inside VS Code, but:

- Agents with strict frontmatter validation may reject the skill entirely
- There is already [an open issue](https://github.com/microsoft/vscode/issues/294520) about this breaking extensibility
- Other platforms will silently ignore these fields at best, or fail at worst

**Rule: Do not use vendor-specific top-level frontmatter fields in OLAF skills.**

If you need vendor-specific behavior, place it in `metadata` where it won't break other consumers.

## Why `disable-model-invocation` Is an Anti-Pattern for Portable Skills

Setting `disable-model-invocation: true` means the agent cannot auto-discover and load the skill — it must be manually invoked via a `/` slash command. This creates a problem:

- Most platforms outside VS Code don't have slash commands
- The skill becomes invisible and unreachable on those platforms
- It defeats the core design of progressive disclosure (agent reads `name` + `description` → decides to load → reads body)

If you want a skill that is only triggered on explicit user request rather than auto-loaded, the portable approach is:

1. Keep the skill auto-discoverable (no `disable-model-invocation`)
2. Write the `description` to clearly state when it should be used
3. Create a **prompt file** or **command** that explicitly invokes the skill

This way the skill works everywhere: on platforms with slash commands, users can call it directly; on platforms without, the agent can still find and use it when the task matches.

## Summary

| Do | Don't |
|----|-------|
| Use `name` and `description` (required) | Add unknown top-level frontmatter fields |
| Put extensions in `metadata` | Use `user-invokable`, `argument-hint`, etc. at top level |
| Keep skills auto-discoverable | Use `disable-model-invocation: true` |
| Create commands/prompts for explicit invocation | Rely on platform-specific slash command mechanics |
| Test skills on multiple agents | Assume VS Code is the only consumer |
