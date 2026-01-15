# Delete Stash

## Overview

Provides a safe way to permanently delete stash directories that are no longer needed, freeing up disk space and keeping the stash system organized.

## Purpose

Over time, stash directories can accumulate. This skill allows users to safely remove unwanted stashes with built-in confirmation prompts to prevent accidental deletions.

## Usage

**Command**: `delete stash`, `remove stash`, `clean stash`, `stash delete`

**Protocol**: Act

**When to Use**: When you want to permanently remove old or unnecessary stash directories.

## Parameters

- **stash-name**: Name of the stash directory to delete (can be selected from list)

## Key Features

- **List before delete**: Shows all available stashes for selection
- **Safety confirmation**: Requires user to type "DELETE" before proceeding
- **Permanent deletion**: Completely removes stash directory
- **Clear feedback**: Provides success/failure confirmation
- **Force mode**: Optional `--yes` flag for automated scenarios (use with caution)

## Execution

### Step 1: List Available Stashes
```bash
python tools/stash_manager.py list
```

### Step 2: Delete Selected Stash
```bash
python tools/stash_manager.py delete <stash-name>
```

The tool will prompt for "DELETE" confirmation before proceeding.

### Step 3 (Optional): Force Delete
For automated scenarios only:
```bash
python tools/stash_manager.py delete <stash-name> --yes
```

## User Interaction Flow

1. **List stashes** - View all available stashes
2. **Select target** - Specify stash name to delete
3. **Confirmation** - Type "DELETE" to confirm
4. **Deletion** - Stash permanently removed
5. **Verification** - Optional: list remaining stashes

## Safety Features

- ⚠️ **Confirmation Required**: User must type "DELETE" to proceed
- 🚫 **Cannot Be Undone**: Clear warning about permanent action
- 📋 **List First**: Always show available stashes before deletion
- ✅ **Feedback**: Confirms successful deletion

## Outputs

- List of available stashes
- Deletion confirmation message
- Success/failure feedback

## Integration

This skill works with:
- `stash-work-session` - Creates stashes that can later be deleted
- `stash-restart-session` - May reference stashes that can be cleaned up
- Stash management system in `.olaf/stash/`

## Technical Requirements

- **Recommended LLM**: Validated primarily with Windsurf using GPT Low Reasoning and GitHub Sonnet 4.x
- **Tool Dependency**: Python 3.12+ for stash_manager.py
- **Platform Limitations**: Cross-platform compatible

## Maintenance

- **Team**: admin
- **Primary Maintainer**: OLAF Framework Core Team
- **Status**: experimental
- **Exposure**: internal
