---
name: carry-over-session
description: Create a simple carry-over note with next prompt and files needed for session continuation
license: Apache-2.0
metadata:
  olaf_tags: [session, carry-over, continuation, workflow]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

# Create Carry-Over Session Note

## Purpose
Based on the conversation up to now, create a carry-over note with TWO items only:
- **Next Prompt**: Exact prompt you recommend to continue the next session
- **Files Needed**: Absolute paths to files that will best support continuation of the work
- **Optional - Brief Context**: Only if critical: 1–2 lines on current state

## Instructions
**Write Next Prompt**
   - One clear, actionable prompt to resume work
   - Include just enough context to start immediately
**List Files Needed**
   - Use ABSOLUTE paths from workspace root (e.g., `c:\Users\<user>\coderepos\project\...`)
   - Include all files to read and modify
**Save File**
   - Path: `.olaf/work/carry-over/carry-over-YYYYMMDD-HHmm.txt`

## Template
```text
CARRY-OVER - <YYYY-MM-DD HH:mm>
========================

## NEXT PROMPT
<Exact prompt to use next session>

## FILES NEEDED (Absolute Paths)
<c:\Users\<user>\coderepos\project\path\to\file1>
<c:\Users\<user>\coderepos\project\path\to\file2>

## OPTIONAL - Brief Context
<Only if critical: 1–2 lines on current state>
```

## Example
```text
CARRY-OVER - 2025-11-14 14:30
========================

## NEXT PROMPT
Add JWT validation to `AuthService`, update login to return token, and add middleware to protect routes.

## FILES NEEDED (Absolute Paths)
c:\Users\<user>\coderepos\project\src\services\AuthService.ts
c:\Users\<user>\coderepos\project\src\middleware\auth.ts
c:\Users\<user>\coderepos\project\src\routes\api.ts
c:\Users\<user>\coderepos\project\config\jwt.config.ts
c:\Users\<user>\coderepos\project\tests\auth.test.ts
```
