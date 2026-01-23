# HAAL Skills

Skills are reusable capability “packs” for agent platforms (Kiro, Claude, Windsurf, GitHub Copilot).

Use this site to:
- Install skill bundles (collections)
- Browse competencies (role-based groupings)
- Read skill descriptions + tutorials

## Get started

Recommended: install the `basic` collection.

### Bash

```bash
bash .olaf/tools/setup-haal-skills.sh --collection basic --platform kiro --clean
```

### PowerShell

```powershell
./.olaf/tools/setup-haal-skills.ps1 -Collection basic -Platform kiro -Clean
```

Full details: [Installer](installer.md)

## Explore

- Start with [Collections](collections.md) (bundles you can install)
- Then review [Competencies](competencies.md) (what’s inside)
- Browse all published docs under [Skills](skills/index.md)

If you want a curated subset, see [Verified](skills/verified.md) and the full [Catalog](skills/catalog.md).

## How it’s organized

- A **collection** maps to one or more **competencies** (see `collection-manifest.json`)
- A **competency** maps to a list of **skills** (see `competencies/*.json`)
- A **skill** lives in `skills/<skill-id>/` and may publish docs in `skills/<skill-id>/docs/`
