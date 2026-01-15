# Windows PowerShell Context

<!-- LOADING_ANNOUNCEMENT_START -->
🪟 Windows PowerShell context loaded  
Use `olaf switch context` if this environment doesn't match yours.
<!-- LOADING_ANNOUNCEMENT_END -->

## Environment Configuration

### Shell & Platform
- **Shell**: PowerShell 5.1+ (Windows)
- **Platform**: Windows environment assumed

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