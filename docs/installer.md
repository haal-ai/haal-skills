# Installer

This installer is for **Windsurf** only (tested with **Windsurf 1.13.9**).

## PowerShell (Windows)

Run this in the destination repository folder (the repo where you want to use HAAL skills):

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.ps1" -OutFile "setup-haal-skills.ps1"; .\setup-haal-skills.ps1
```

## Bash (macOS / Linux)

Run this in the destination repository folder (the repo where you want to use HAAL skills):

```bash
curl -fsSL "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh
```

### Bash on Windows (Git Bash)

If you see an error like `CRYPT_E_NO_REVOCATION_CHECK`, Git Bash `curl` is failing TLS revocation checks on Windows.

Use Windows `curl.exe` with `--ssl-no-revoke`:

```bash
curl.exe -fsSL --ssl-no-revoke "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -o setup-haal-skills.sh \
  && bash setup-haal-skills.sh
```

Or download with PowerShell, then run with Bash:

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/haal-ai/haal-skills/main/.olaf/tools/setup-haal-skills.sh" -OutFile "setup-haal-skills.sh"
```

## What it does

- Downloads the installer script (`setup-haal-skills.ps1`) from the `haal-ai/haal-skills` repository.
- Executes the script in your current folder.

## Recommended usage

- Make sure you are in the repository you want to install into.
- If your execution policy blocks scripts, you may need to allow running local scripts for your session.
- If you want to inspect the script first, run only the download part, open the file, then execute it.

## Troubleshooting

- If you see network errors, verify you can access `raw.githubusercontent.com`.
- If you see permission errors, try running PowerShell as Administrator.
