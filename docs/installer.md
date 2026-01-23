# Installer

This installer supports **Windsurf**, **Claude**, **GitHub Copilot**, and **Kiro**.

## Quick Start

### PowerShell (Windows)

Run in your target repository folder:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.ps1" -OutFile "setup-haal-skills.ps1"; .\setup-haal-skills.ps1
```

### Bash (macOS / Linux)

```bash
curl -fsSL "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh
```

## Options

### Install a Collection

Collections are predefined sets of competencies:

```powershell
.\setup-haal-skills.ps1 -Collection "developer"
```

```bash
bash setup-haal-skills.sh --collection developer
```

Available collections:
- `starter` - Basic skills for getting started
- `developer` - Full developer toolkit
- `architect` - Architecture and specification skills
- `full` - All skills

### Install Specific Competencies

```powershell
.\setup-haal-skills.ps1 -Competency "code-review","documentation"
```

```bash
bash setup-haal-skills.sh --competency code-review,documentation
```

Available competencies:
- `code-review` - Code review and diff analysis
- `documentation` - JSDoc, tech specs, code mapping
- `git-workflow` - Git commits, merges, PR workflows
- `specification` - Spec review and transformation
- `scaffolding` - API and frontend scaffolding
- `session-management` - Session carry-over and context switching
- `prompting` - Prompt and skill creation
- `analysis` - Code and API analysis

### Combine Collection and Competencies

```powershell
.\setup-haal-skills.ps1 -Collection "starter" -Competency "scaffolding"
```

```bash
bash setup-haal-skills.sh --collection starter --competency scaffolding
```

### Install All Skills (Default)

If no collection or competency is specified, all skills are installed.

## What It Does

1. Clones the `haal-skills` repository to a temp folder
2. Prunes deprecated skills from all destinations
3. Resolves skills from collection/competency selection
4. Copies selected skills to all IDE skill folders:
   - `~/.codeium/windsurf/skills/`
   - `~/.claude/skills/`
   - `~/.github/skills/`
   - `~/.kiro/skills/`
5. Syncs `.olaf/` and `.windsurf/` files to your repository

## Troubleshooting

### Git Bash on Windows

If you see `CRYPT_E_NO_REVOCATION_CHECK`, use:

```bash
curl.exe -fsSL --ssl-no-revoke "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh
```

### Network Errors

Verify you can access `raw.githubusercontent.com`.

### Permission Errors

Try running PowerShell as Administrator.
