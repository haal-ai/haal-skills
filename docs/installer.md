# Installer

This installer supports **Windsurf**, **Claude**, **GitHub Copilot**, and **Kiro**.

It is intentionally **script-based**: there is no HAAL CLI and no `haal-skills-sdk`.

## Prerequisites

- `git` installed (used to clone the seed repo)
- Either PowerShell (Windows) or `bash` (macOS/Linux/Git Bash)
- No Python required for installation
- Optional: `jq` (only used as a faster JSON parser when available)

## Quick Start

### PowerShell (Windows)

Run in your target repository folder:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.ps1" -OutFile "setup-haal-skills.ps1"; .\setup-haal-skills.ps1
```

Example: install the `basic` collection to Kiro and wipe existing skills first:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.ps1" -OutFile "setup-haal-skills.ps1"; .\setup-haal-skills.ps1 -Collection basic -Platform kiro -Clean
```

### Bash (macOS / Linux)

```bash
curl -fsSL "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh
```

Example: install the `basic` collection to Kiro and wipe existing skills first:

```bash
curl -fsSL "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh --collection basic --platform kiro --clean
```

## Options

### Install a Collection

Collections are predefined sets of competencies:

```powershell
.\setup-haal-skills.ps1 -Collection "basic"
```

```bash
bash setup-haal-skills.sh --collection basic
```

Available collections:
- `starter` - Minimal set for getting started
- `basic` - Recommended default set
- `techie` - Heavier technical toolkit
- `full` - Full set
- `all` - All competencies (equivalent to installing everything)

### Install Specific Competencies

```powershell
.\setup-haal-skills.ps1 -Competency "developer","git-assistant"
```

```bash
bash setup-haal-skills.sh --competency developer --competency git-assistant
```

Available competencies:
- `developer`
- `architect`
- `api-producers`
- `api-consumers`
- `specification`
- `git-assistant`
- `session-manager`
- `prompt-engineer`
- `technical-writer`
- `business-analyst`
- `project-manager`
- `researcher`
- `base-skills`

### Combine Collection and Competencies

```powershell
.\setup-haal-skills.ps1 -Collection "basic" -Competency "technical-writer"
```

```bash
bash setup-haal-skills.sh --collection basic --competency technical-writer
```

### Platform Selection

Install to one platform only:

```powershell
.\setup-haal-skills.ps1 -Collection basic -Platform kiro
```

```bash
bash setup-haal-skills.sh --collection basic --platform kiro
```

Supported values: `all`, `kiro`, `claude`, `windsurf`, `github`.

### Install From a Specific Branch

Use `--seed` / `-Seed` to pick a branch:

```powershell
.\setup-haal-skills.ps1 -Seed "haal-ai/haal-skills:integration" -Collection basic -Platform kiro -Clean
```

```bash
bash setup-haal-skills.sh --seed "haal-ai/haal-skills:integration" --collection basic --platform kiro --clean
```

### Install All Skills (Default)

If no collection or competency is specified, all skills are installed.

## What It Does

1. Clones the seed repo (`haal-ai/haal-skills:main` by default) to a temp folder
2. Optionally clones additional repos listed in `repos-manifest.json` (if present)
3. Prunes deprecated skills from destinations (if `.olaf/prune-skills.txt` exists)
4. Resolves skills from collection/competency selection (from `collection-manifest.json` + `competencies/*.json`)
5. Copies selected skills to the chosen platform folder(s):
   - `~/.codeium/windsurf/skills/`
   - `~/.claude/skills/`
   - `~/.github/skills/`
   - `~/.kiro/skills/`
6. Syncs `.olaf/` to your global location (`~/.olaf`)
7. Optionally syncs `.olaf/` files into your target repo when `--repo-path` / `-RepoPath` is provided

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
