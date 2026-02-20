#!/bin/bash
# =============================================================================
# OpenCode Installer Wrapper
# Installs OpenCode and configures GitHub Copilot as the default provider
# =============================================================================

set -e

CONFIG_DIR="$HOME/.config/opencode"
CONFIG_FILE="$CONFIG_DIR/opencode.json"

echo "=== OpenCode Corporate Installer ==="
echo ""

# Step 1: Install or update OpenCode
echo "[1/3] Installing/updating OpenCode..."
if command -v opencode &> /dev/null; then
  CURRENT=$(opencode --version 2>/dev/null || echo "0.0.0")
  LATEST=$(curl -fsSL https://registry.npmjs.org/opencode-ai/latest 2>/dev/null | grep -o '"version":"[^"]*"' | head -1 | cut -d'"' -f4 || echo "")

  if [ -n "$LATEST" ] && [ "$CURRENT" != "$LATEST" ]; then
    echo "  Update available: $CURRENT -> $LATEST"
    echo "  Updating..."
    curl -fsSL https://opencode.ai/install | bash
  else
    echo "  OpenCode $CURRENT is up to date."
  fi
else
  echo "  Installing OpenCode..."
  curl -fsSL https://opencode.ai/install | bash
fi

echo ""

# Step 2: Configure GitHub Copilot as the preferred provider
echo "[2/3] Configuring GitHub Copilot provider..."
mkdir -p "$CONFIG_DIR"

if [ -f "$CONFIG_FILE" ]; then
  echo "  Existing config found at $CONFIG_FILE"
  echo "  Backing up to ${CONFIG_FILE}.bak"
  cp "$CONFIG_FILE" "${CONFIG_FILE}.bak"

  # Merge enabled_providers into existing config using a simple approach
  # If jq is available, use it for proper JSON merge
  if command -v jq &> /dev/null; then
    jq '. + {
      "enabled_providers": ["github-copilot"],
      "model": "github-copilot/claude-sonnet-4"
    }' "$CONFIG_FILE" > "${CONFIG_FILE}.tmp" && mv "${CONFIG_FILE}.tmp" "$CONFIG_FILE"
    echo "  GitHub Copilot configured as provider."
  else
    echo "  WARNING: jq not found. Cannot merge configs safely."
    echo "  Please manually add '\"enabled_providers\": [\"github-copilot\"]' to $CONFIG_FILE"
  fi
else
  cat > "$CONFIG_FILE" << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "enabled_providers": ["github-copilot"],
  "model": "github-copilot/claude-sonnet-4"
}
EOF
  echo "  Config created at $CONFIG_FILE"
fi

# Step 3: Create convenience alias
echo "[3/4] Creating 'occ' shortcut..."
SHELL_RC=""
if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
  SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
  SHELL_RC="$HOME/.bashrc"
fi

ALIAS_LINE='occ() { command -v opencode >/dev/null || export PATH="$PATH:$HOME/.opencode/bin:$HOME/bin"; opencode auth login; }'

if [ -n "$SHELL_RC" ]; then
  if grep -q "occ()" "$SHELL_RC" 2>/dev/null; then
    echo "  Alias already exists in $SHELL_RC"
  else
    echo "" >> "$SHELL_RC"
    echo "# OpenCode - quick connect to GitHub Copilot" >> "$SHELL_RC"
    echo "$ALIAS_LINE" >> "$SHELL_RC"
    echo "  Added 'occ' alias to $SHELL_RC"
  fi
else
  echo "  Could not detect shell config file."
  echo "  Add this manually: $ALIAS_LINE"
fi

# Define occ in the current shell so it works immediately after curl | bash
eval "$ALIAS_LINE"
echo "  'occ' is ready to use now."

echo ""

# Step 4: Verify installation
echo "[4/4] Verifying installation..."
if command -v opencode &> /dev/null; then
  echo "  OpenCode installed successfully."
else
  echo "  WARNING: 'opencode' command not found in PATH."
  echo "  You may need to restart your terminal or add it to your PATH."
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "One last step - connect to GitHub Copilot:"
echo "  Run: occ  (or 'opencode auth login')"
echo "  Select 'GitHub Copilot' -> authenticate in browser -> done."
echo ""
echo "After that, just run 'opencode' in any project. You're set."
