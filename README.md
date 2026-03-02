# HAAL Skills & Powers

AI agent skills and powers for **Windsurf**, **Claude**, **GitHub Copilot**, and **Kiro**.

### Related Repositories

- **[`haal-ide`](../haal-ide)** - OLAF based HAAL (now deprecated in favor of Skills)

## 🧩 What's Included?

- **Skills** - AI agent prompts following the [Agent Skills](https://agentskills.io) format
- **Powers** - Kiro-specific capabilities with steering files and documentation
- **Tools** - Helper scripts for installation and management

## 🚀 Quick Start

Navigate to your project folder, then run:

### Windows (PowerShell)

```powershell
irm https://haal-ai.github.io/haal-skills/setup-haal.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://haal-ai.github.io/haal-skills/setup-haal.sh | bash
```

### Options

```bash
# Install a specific collection
bash setup-haal.sh --collection basic

# Install to a specific platform only
bash setup-haal.sh --platform kiro

# Clean install (remove existing skills first)
bash setup-haal.sh --clean
```

See [Installer Documentation](docs/installer.md) for all options.

## 📁 Repository Structure

```
├── skills/           # AI agent skill definitions
├── powers/           # Kiro powers with steering files
├── competencies/     # Skill groupings (JSON manifests)
├── docs/             # Documentation (MkDocs source)
├── .olaf/
│   ├── tools/        # Installation scripts
│   ├── data/         # Knowledge base and context
│   └── work/         # Working files
└── collection-manifest.json
```

## 📚 Documentation

This repo publishes documentation as a GitHub Pages site.

### Local preview

```bash
python tools/build_docs_site.py
pip install mkdocs
mkdocs serve
```

## 📄 License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
