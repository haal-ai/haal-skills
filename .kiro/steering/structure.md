# Project Structure

## Skill Directory Layout

Each skill lives in `skills/<skill-name>/` with this structure:

```
skills/<skill-name>/
├── skill.md           # Main prompt file (REQUIRED)
├── docs/
│   ├── description.md # Skill overview
│   └── tutorial.md    # Usage guide
├── templates/         # External template files (optional)
├── tools/             # Scripts/utilities (optional)
├── kb/                # Knowledge base articles (optional)
└── helpers/           # Reusable prompt fragments (optional)
```

## Root Directories

| Directory | Purpose |
|-----------|---------|
| `skills/` | All skill implementations |
| `competencies/` | Skill groupings (JSON manifests) |
| `common/` | Shared tasks, tools, and knowledge base |
| `docs/` | MkDocs source files |
| `site/` | Generated documentation site |
| `tools/` | Build and utility scripts |
| `plugins/` | IDE plugin integrations |
| `.olaf/` | OLAF-specific data and configuration |

## Skill Frontmatter

Every `skill.md` must include YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description
license: Apache-2.0
metadata:
  olaf_tags: [tag1, tag2]
  author: author-name
  provider: Haal AI
---
```

## Naming Conventions

- Skill names: kebab-case, max 4 words (e.g., `review-code`, `create-skill`)
- Template files: kebab-case with `.md` extension
- Tool scripts: kebab-case with appropriate extension (`.py`, `.sh`, `.ps1`)
