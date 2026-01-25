# Installer

Installs HAAL skills, powers, and tools to your AI coding assistants.

Supports **Windsurf**, **Claude**, **GitHub Copilot**, and **Kiro**.

## What Gets Installed

- **Skills** - AI agent prompts for various tasks (code review, documentation, etc.)
- **Powers** - Kiro-specific capabilities with steering files
- **Tools** - Helper scripts in `.olaf/tools/`
- **Data** - Knowledge base and context files in `.olaf/data/`

## Prerequisites

- `git` installed
- PowerShell (Windows) or `bash` (macOS/Linux)

## Quick Start

Navigate to your project folder, then run:

### Windows (PowerShell)

```powershell
irm https://haal-ai.github.io/haal-skills/setup-haal.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://haal-ai.github.io/haal-skills/setup-haal.sh | bash
```

That's it! The installer will set up everything in your current folder.

To update later, rerun from your `.olaf/tools/` folder:

**Windows:**
```powershell
.\.olaf\tools\setup-haal.ps1
```

**macOS / Linux:**
```bash
bash .olaf/tools/setup-haal.sh
```

## Options

### Install a Collection

Collections are predefined sets of skills:

```powershell
.\setup-haal.ps1 -Collection basic
```

```bash
bash setup-haal.sh --collection basic
```

Available collections: `starter`, `basic`, `techie`, `full`, `all`

### Install Specific Competencies

```powershell
.\setup-haal.ps1 -Competency developer,git-assistant
```

```bash
bash setup-haal.sh --competency developer --competency git-assistant
```

Available competencies: `developer`, `architect`, `api-producers`, `api-consumers`, `specification`, `git-assistant`, `session-manager`, `prompt-engineer`, `technical-writer`, `business-analyst`, `project-manager`, `researcher`, `base-skills`

### Platform Selection

Install to one platform only:

```powershell
.\setup-haal.ps1 -Platform kiro
```

```bash
bash setup-haal.sh --platform kiro
```

Supported: `all`, `kiro`, `claude`, `windsurf`, `github`

### Clean Install

Remove existing skills before installing:

```powershell
.\setup-haal.ps1 -Clean
```

```bash
bash setup-haal.sh --clean
```

## Advanced Options

### Specify Target Repository

By default, the installer uses your current directory. To install to a different location:

```powershell
.\setup-haal.ps1 -RepoPath "C:\path\to\your\repo"
```

```bash
bash setup-haal.sh --repo-path /path/to/your/repo
```

### Use a Different Source

By default, skills are downloaded from `haal-ai/haal-skills:main`. To use a different branch or fork:

```powershell
.\setup-haal.ps1 -Seed "your-org/your-repo:branch"
```

```bash
bash setup-haal.sh --seed "your-org/your-repo:branch"
```

## What It Does

1. Downloads the HAAL package to a temp folder
2. Copies skills to your platform folder(s)
3. Copies powers to Kiro and updates the registry
4. Syncs tools and data to `~/.olaf` and your project

## Troubleshooting

### Git Bash on Windows

If you see SSL errors, use:

```bash
curl.exe -fsSL --ssl-no-revoke "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal.sh" -o setup-haal.sh && bash setup-haal.sh
```

### Network Errors

Verify you can access `raw.githubusercontent.com`.

### Permission Errors

Try running PowerShell as Administrator.
