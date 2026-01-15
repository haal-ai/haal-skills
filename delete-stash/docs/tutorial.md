# Delete Stash Tutorial

## Quick Start

To delete an unwanted stash:
```
delete stash
```

The system will guide you through listing available stashes and confirming the deletion.

## Step-by-Step Guide

### Step 1: List Your Stashes

First, see what stashes are available:

```bash
python tools/stash_manager.py list
```

**Example Output**:
```
Available stashes:
1. stash-20251110-1430 (4 days ago)
2. stash-20251112-0915 (2 days ago)
3. stash-20251114-1015 (today)
```

### Step 2: Select Stash to Delete

Identify the stash you want to remove. You can use either the full name or the number from the list.

**Example**: You want to delete the oldest stash `stash-20251110-1430`

### Step 3: Execute Delete Command

```bash
python tools/stash_manager.py delete stash-20251110-1430
```

### Step 4: Confirm Deletion

The tool will prompt:
```
⚠️  WARNING: This will permanently delete stash-20251110-1430
Type 'DELETE' to confirm:
```

**Type exactly**: `DELETE` (in capitals)

### Step 5: Verification

After successful deletion:
```
✅ Successfully deleted stash-20251110-1430
```

Optionally, list stashes again to verify:
```bash
python tools/stash_manager.py list
```

## Advanced Usage

### Force Delete (Skip Confirmation)

For automated scripts or when you're absolutely certain:

```bash
python tools/stash_manager.py delete stash-20251110-1430 --yes
```

⚠️ **Warning**: This skips the confirmation prompt. Use with extreme caution!

## Common Scenarios

### Scenario 1: Clean Up Old Stashes

You have many old stashes and want to keep only recent ones:

1. List all stashes
2. Identify stashes older than needed (e.g., > 1 week)
3. Delete each old stash one by one
4. Verify with final list

### Scenario 2: Remove Failed Experiment

You created a stash for an experiment that didn't work out:

1. List stashes to find the experiment stash
2. Delete the specific stash
3. Continue with other work

### Scenario 3: Free Up Disk Space

Your stash directory is taking up too much space:

1. List all stashes
2. Review size/age of each
3. Delete stashes that are no longer needed
4. Keep recent or important stashes

## Best Practices

### ✅ Do's

- **Always list first**: Check available stashes before deleting
- **Review content**: If unsure, use `stash-restart-session` to review stash content before deleting
- **Keep recent**: Generally keep stashes from the last few days
- **Clean regularly**: Periodically review and clean old stashes

### ❌ Don'ts

- **Don't rush**: Double-check the stash name before confirming
- **Don't use --yes carelessly**: Force delete should only be used in automated scripts
- **Don't delete active work**: Ensure the stash isn't related to current work
- **Don't delete without backup**: If the stash contains important work, consider archiving it first

## Understanding Stash Names

Stash names follow the pattern: `stash-YYYYMMDD-HHmm`

**Example**: `stash-20251114-1530`
- `20251114` = November 14, 2025
- `1530` = 3:30 PM

This helps you identify when the stash was created.

## Safety Net

The deletion process has multiple safety features:

1. **Explicit confirmation**: You must type "DELETE" exactly
2. **Warning message**: Clear indication this is permanent
3. **No undo**: Once deleted, stash is gone forever
4. **List before delete**: Always see what you're deleting

## Troubleshooting

**Q**: What if I accidentally type the wrong stash name?  
**A**: The tool will show you the name and ask for confirmation. Review carefully before typing "DELETE".

**Q**: Can I recover a deleted stash?  
**A**: No, deletion is permanent. Make sure you don't need the content before deleting.

**Q**: What if the delete command fails?  
**A**: Check if the stash directory exists and you have proper file permissions.

**Q**: How do I delete multiple stashes at once?  
**A**: Delete them one by one, or create a script with `--yes` flag (use carefully).

## Integration with Other Skills

### Before Deleting

Use these skills to review stash content:
- `stash-restart-session`: Resume a stashed session to review its contents
- Manual inspection: Navigate to `.olaf/stash/` directory

### After Deleting

Continue with:
- `stash-work-session`: Create new stashes as needed
- Regular workflow: Work continues with active session

## Command Reference

```bash
# List all stashes
python tools/stash_manager.py list

# Delete with confirmation
python tools/stash_manager.py delete <stash-name>

# Force delete (no confirmation)
python tools/stash_manager.py delete <stash-name> --yes
```

## Tips

- Set a reminder to clean stashes monthly
- Keep stashes from important milestones
- Document important stashes before deleting
- Use descriptive commit messages when you stash work, so you can identify it later
