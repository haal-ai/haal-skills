# OpenCode Setup

Install and configure [OpenCode](https://opencode.ai) with GitHub Copilot as your AI provider.

## Install

Open a terminal and paste the command for your platform:

### Windows (PowerShell)

```powershell
irm https://haal-ai.github.io/haal-skills/install-opencode.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://haal-ai.github.io/haal-skills/install-opencode.sh | bash
```

The installer will set up OpenCode and configure GitHub Copilot automatically.

## After Install

Once the installer finishes, type:

```
opencode
```

On first launch, OpenCode will ask you to log in.
Select **GitHub Copilot**, authenticate in your browser with your GitHub credentials, and you're set.

!!! note "Quick connect shortcut"
    You can also type `occ` to go straight to the GitHub Copilot login screen.

## What the Installer Does

1. Installs or updates OpenCode to the latest version
2. Configures GitHub Copilot as the available provider
3. Sets a recommended default model (Claude Sonnet 4)
4. Creates the `occ` shortcut for quick authentication

## Daily Use

After your initial login, just run `opencode` in any project directory to start coding with AI.

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

- Default models (GPT-5 mini, GPT-4.1, GPT-4o) are included on paid plans
- Premium models have multipliers (e.g., Claude Sonnet 4 = 1x, Claude Opus 4.5 = 3x)
- Overage: $0.04 per additional premium request (if budget is set)

## Troubleshooting

### `opencode` not found after install

On Windows with npm, restart your terminal. The npm global bin directory (`%APPDATA%\npm`) must be in your PATH.

### `occ` not recognized

Restart your terminal or reload your shell profile:

- PowerShell: `. $PROFILE`
- Bash/Zsh: `source ~/.bashrc` or `source ~/.zshrc`

## Prerequisites

- `npm` or `scoop` installed (for OpenCode)
- A GitHub Copilot subscription (Pro, Pro+, Business, or Enterprise)
