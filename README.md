# HAAL Skills

HAAL using Anthropic skills format - Core skill definitions and implementations using the Anthropic Agent Skills format.

## 🔗 HAAL AI Organization

This repository is part of the [HAAL AI](../) organization. See the [main README](../README.md) for an overview of all repositories.

### Related Repositories

- **[`haal-ide`](../haal-ide)** - OLAF  based HAAL (now deprecated in favor of Skills)
- **[`haal-skills-agentic-aws`](../haal-skills-agentic-aws)** - using AWS Strands based Agents with HAAL Skills

## 🧩 What are Agent Skills?

[Agent Skills](https://agentskills.io) are a simple, open format for giving agents new capabilities and expertise. Skills are folders of instructions, scripts, and resources that agents can discover and use to perform better at specific tasks.

## 📋 Features

- Core skill definitions following Anthropic's Agent Skills format
- HAAL-specific skill templates and examples
- Install scripts to deploy skills to supported agent platforms
- Standardized skill structure for consistency

## 🚀 Quick Start

```bash
# Clone the skills repository
git clone https://github.com/haal-ai/haal-skills.git
cd haal-skills

# Browse skills
ls skills/

# Install a collection of skills to a platform (example: "basic" to Kiro)
# Options: --platform all|kiro|claude|windsurf|github
bash .olaf/tools/setup-haal-skills.sh --collection basic --platform kiro --clean
```

## 📚 Documentation (GitHub Pages)

This repo publishes skill documentation (descriptions + tutorials) as a GitHub Pages site.

- Each skill keeps its docs in `/<skill-id>/docs/description.md` and `/<skill-id>/docs/tutorial.md`.
- The site is generated during the Pages build by copying those files into a single `docs/skills/<skill-id>/...` structure.

### Local preview

```bash
python tools/build_docs_site.py
pip install mkdocs
mkdocs serve
```

## 📄 License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
