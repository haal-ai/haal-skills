# Store Conversation Record

## Overview

Store Conversation Record creates comprehensive conversation records that capture complete dialogue, actions taken, files affected, and AI models used. It preserves project history and enables future reference by documenting the full narrative of important work sessions.

## Purpose

Important conversations and work sessions contain valuable context, decisions, and rationale that can be lost over time. This skill solves the problem of lost institutional knowledge by creating detailed, structured records that capture the complete narrative, all actions performed, files modified, and context needed to understand what happened and why.

## Key Features

### 1. Explicit Permission Model
- Records are NEVER created automatically
- Requires explicit user request before proceeding
- Confirms permission and scope before documentation

### 2. AI Model Transparency
- AI model information MUST be provided by user
- Never infers or guesses the AI model name
- Ensures accurate attribution in records

### 3. Complete Narrative Capture
- Full conversation documented without summarization
- Each user request and AI response captured
- All tool calls and operations recorded

### 4. Structured File Operations
- Files created/modified/deleted listed with relative paths
- Clean markdown formatting applied
- User typos corrected for readability

### 5. Unique Timestamped Files
- Each record gets unique timestamp filename
- Never appends to existing files
- Prevents filename conflicts

## Usage

**Command**: `store conversation record`

**Protocol**: Act

**When to Use**: Use this skill only when explicitly requested to preserve important conversations, document significant work sessions, capture decision-making processes, or create historical records for future reference, audits, or knowledge transfer.

## Parameters

### Required Inputs
- **user_request**: Explicit user request for record creation (CRITICAL: never create automatically)
- **conversation_scope**: Purpose and scope of the record being created
- **ai_model_used**: Name of the AI model used in the conversation (must be provided by user)

### Optional Inputs
- **record_purpose**: Specific use case or reason for creating this record

### Context Requirements
- Explicit user permission to create the record
- Access to conversation history and context
- Access to conversation records directory
- Access to conversation record template
- System time for unique timestamp generation

## Output

**Deliverables**:
- Comprehensive conversation record file with unique timestamp
- Complete conversation narrative (never summarized)
- Accurate dialogue capture (each user request and AI response)
- All actions documented (tool calls, file operations, searches)
- File operations listed (created/modified/deleted with relative paths)
- Clean markdown formatting with corrected user typos

**Format**: Markdown file following conversation record template with structured sections, clear headings for each topic, and formatted dialogue using **USER said:** / **AI said:** / **AI did:** patterns.

**Location**: `.olaf/work/staging/conversation-records/conversation-record-[timestamp].md`

## Examples

### Example 1: Feature Development Session

**Scenario**: User wants to preserve a complex feature implementation conversation

**Input**:
```
User Request: Please create a conversation record for this OAuth implementation session
Conversation Scope: OAuth2 authentication feature implementation
AI Model Used: Claude Sonnet 4.5
Record Purpose: Document implementation decisions and approach for team reference
```

**Result**: Created `conversation-record-20251027-1430.md` with complete dialogue, all code changes, design decisions, and implementation steps documented

### Example 2: Debugging Session

**Scenario**: Debugging session that identified root cause of production issue

**Input**:
```
User Request: Store this debugging conversation for the incident report
Conversation Scope: Memory leak investigation and root cause analysis
AI Model Used: Claude Sonnet 4.5
Record Purpose: Incident documentation and future reference
```

**Result**: Created record capturing investigation process, profiling results, root cause identification, and fix implementation

### Example 3: Architecture Decision

**Scenario**: Important architectural discussion that needs to be preserved

**Input**:
```
User Request: Create a record of this architecture discussion
Conversation Scope: Microservices vs monolithic architecture decision
AI Model Used: Claude Sonnet 4.5
Record Purpose: Preserve decision rationale for future team members
```

**Result**: Created record with complete discussion, options considered, trade-offs analyzed, and final decision with rationale

## Related Skills

- **carry-over-session**: Handovers capture next steps, records capture complete history
- **create-decision-record**: Formal decisions discussed in conversations can be extracted to decision records
- **create-changelog-entry**: Significant conversations can be logged in the changelog
- **review-progress**: Conversation records provide detailed context for progress reviews

## Tips & Best Practices

1. **Only create when requested**: Never automatically create records
2. **Always ask for AI model**: Get this information directly from user
3. **Create new files**: Each record is a separate file with unique timestamp
4. **Capture completely**: Include full narrative, never summarize
5. **Validate paths**: Ensure file path resolution before creating files
6. **Organize by topics**: Use clear headings for easy navigation
7. **Correct typos**: Fix obvious user typos for readability
8. **Use relative paths**: Reference files from project root
9. **Document all actions**: Include tool calls and operations, not just results
10. **Format consistently**: Use **USER said:** / **AI said:** / **AI did:** patterns

## Limitations

- Requires explicit user request - cannot be triggered automatically
- Cannot infer AI model information - must be provided by user
- Creates new files only - cannot append to or update existing records
- Does not automatically categorize or tag conversations for searchability
- File path must be validated - cannot guess locations
- Does not integrate with external documentation systems
- Cannot automatically extract decisions or action items
- Record quality depends on conversation clarity and completeness

