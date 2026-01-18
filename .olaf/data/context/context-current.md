# Windows PowerShell Context

<!-- LOADING_ANNOUNCEMENT_START -->
🪟 Windows PowerShell context loaded  
Use `switch context` if this environment doesn't match yours.
<!-- LOADING_ANNOUNCEMENT_END -->

## Environment Configuration

### Shell & Platform
- **Shell**: PowerShell 5.1+ (Windows)
- **Platform**: Windows environment assumed

### Enforcement Rules
- **Use PowerShell only**: Commands and examples must be valid in Windows PowerShell (not bash/zsh).
- **No bash utilities**: Do not suggest `grep`, `sed`, `awk`, `ls -la`, `cat`, `find`, pipelines that rely on GNU tools, or `cd` inside commands.
- **PowerShell equivalents**: Prefer `Get-ChildItem` / `dir`, `Select-String`, `Get-Content`, `Get-Location`, `Resolve-Path`, etc.
- **If another shell is required**: Ask the user to `switch context` (new context takes effect in a new session) rather than using another shell implicitly.

### Development Tools
- **JDK Location**: `$env:USERPROFILE\.olaf\jdk`
- **Python**: 3.12 or higher (for new scripts)
- **Script Preference**: Python scripts preferred over PowerShell/bash/zsh scripts

### User-Specific Paths
- **User Profile**: `$env:USERPROFILE` (Windows-specific)
- **OLAF Tools Directory**: `$env:USERPROFILE\.olaf\`

## User Preferences

### Documentation Policy
**CRITICAL - DO NOT CREATE SUMMARY DOCUMENTS**:
- **NEVER** create markdown files to summarize work unless explicitly requested
- **NEVER** create documentation files like "CHANGES.md", "SUMMARY.md", "WORK_COMPLETED.md" etc.
- User finds unsolicited summary documents annoying and wasteful
- Only create documentation when user specifically asks for it
- Focus on doing the work, not documenting that you did the work

## Notes
This file contains Windows PowerShell-specific configurations.
For cross-platform support, these values should be detected or configured per installation.