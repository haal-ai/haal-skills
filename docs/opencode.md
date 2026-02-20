# OpenCode Setup

Install and configure OpenCode with GitHub Copilot as your AI provider.

## What Gets Installed

- **OpenCode** - AI coding agent for the terminal
- **GitHub Copilot provider** - Pre-configured as your AI provider
- **`occ` shortcut** - Quick command to connect to GitHub Copilot

## Prerequisites

- `npm` or `scoop` installed (for OpenCode)
- A GitHub Copilot subscription (Pro, Pro+, Business, or Enterprise)

## Quick Start

### Windows (PowerShell)

```powershell
irm https://haal-ai.github.io/haal-skills/install-opencode.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://haal-ai.github.io/haal-skills/install-opencode.sh | bash
```

After the script completes, connect to GitHub Copilot:

```
occ
```

Select **GitHub Copilot**, authenticate in your browser, and you're set.

## What Happens

1. Installs or updates OpenCode to the latest version
2. Configures GitHub Copilot as the available provider
3. Sets a recommended default model
4. Creates the `occ` shortcut for quick authentication

## Daily Use

Once connected, just run `opencode` in any project directory:

```bash
opencode
```

## Re-running the Installer

The script is safe to run multiple times. It will:

- Update OpenCode if a newer version is available
- Preserve your existing config (backs up before merging)
- Skip alias creation if already present

## Billing

GitHub Copilot uses **premium requests**, not tokens:

| Plan | Monthly Allowance |
|------|-------------------|
| Pro | 300 premium requests |
| Pro+ | 1,500 premium requests |
| Business | 300 per user |
| Enterprise | 1,000 per user |

- Default models (GPT-5 mini, GPT-4.1, GPT-4o) are free on paid plans
- Premium models have multipliers (e.g., Claude Sonnet 4 = 1x, Claude Opus 4.5 = 3x)
- Overage: $0.04 per additional premium request (if budget is set)

## Troubleshooting

### `opencode` not found after install

On Windows with npm, you may need to restart your terminal. The npm global bin
directory (`%APPDATA%\npm`) must be in your PATH.

### `occ` not recognized

Restart your terminal or reload your shell profile:

- PowerShell: `. $PROFILE`
- Bash/Zsh: `source ~/.bashrc` or `source ~/.zshrc`
