---
name: store-conversation-record
description: Create comprehensive conversation record capturing dialogue, actions taken, files affected, and AI models used
license: Apache-2.0
metadata:
  olaf_tags: [conversation, record, documentation, archive, history]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **user_request**: string - Explicit user request for record creation
- **conversation_scope**: string - Purpose and scope of the record
- **ai_model_used**: string - AI model name used in conversation (must be provided by user)
- **record_purpose**: string - Optional specific use case for the record

## Process
1. **Verify Record Creation Permission**:
   - Confirm explicit user request for record creation (CRITICAL: never create automatically)
   - Clarify purpose and scope of the record with user
   - **IMPORTANT**: Explicitly ask user to specify which AI model is being used
   - Do not attempt to infer or guess AI model - get this information directly from user
2. **Validate File Location Before Creation**:
   - **CRITICAL**: Conversation records go to `.olaf/work/staging/conversation-records/`
   - **MANDATORY**: Verify staging directory exists
   - **ENSURE**: Create conversation-records subdirectory if missing using create_directory tool
3. **Create New File**:
   - Write file: `.olaf/work/staging/conversation-records/conversation-record-[timestamp].md`
   - **Create new file for each record - never append to existing files**
   - Use unique timestamp to ensure no filename conflicts
   - Initialize file with proper structure
4. **Follow Template Structure**:
   - Read file: `templates/project-manager/conversation-record-template.md`
   - Apply template structure to organize content:
     - Complete conversation narrative (never summarize)
     - Accurate dialogue capture (each user request and AI response)
     - All actions documented (tool calls, file operations, searches)
     - File operations listed (created/modified/deleted with relative paths)
     - Clean Markdown formatting with corrected user typos

## Output Format

Follow template structure: `templates/project-manager/conversation-record-template.md`

Structure with logical topic sections:
- Clear headings for each distinct request/topic
- Format: **USER said:** / **AI said:** / **AI did:**
- Numbered lists for actions, bullet lists for files
- Relative paths from project root (e.g., `\ack\prompts\file.md`)

## Output to USER
- Conversation record created: [file path with timestamp]
- Topics documented: [number of distinct conversation topics]
- Actions captured: [number of tool calls and operations]
- Files affected: [number of files created/modified/deleted]
- Record location: `.olaf/work/staging/conversation-records/conversation-record-[timestamp].md`

## Record Creation Rules
- Rule 1: CRITICAL - Only create records when explicitly requested by user, never automatically
- Rule 2: Always get AI model information directly from user - never infer or guess
- Rule 3: Create new file for each record with unique timestamp - never append to existing
- Rule 4: Capture complete conversation - include full narrative, never summarize content
- Rule 5: **MANDATORY PATH** - Always save to `.olaf/work/staging/conversation-records/`
- Rule 6: **FAIL-SAFE** - Create conversation-records subdirectory if it doesn't exist
