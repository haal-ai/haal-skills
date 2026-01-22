# Store Conversation Record: Step-by-Step Tutorial

**How to Create Comprehensive Conversation Records**

This tutorial shows how to create detailed conversation records that capture dialogue, actions taken, files affected, and AI models used for future reference and continuity.

## Prerequisites

- OLAF framework loaded and active
- Completed conversation session to record
- Conversation record template available
- Knowledge of AI model being used
- Understanding of record purpose and scope

## Step-by-Step Instructions

### Step 1: Request Record Creation (CRITICAL)

**User Action:**
1. Explicitly request record creation: `store conversation record`
2. Press Enter

**IMPORTANT:** 
- Records are NEVER created automatically
- User must explicitly request record creation
- AI will confirm permission before proceeding

**AI Response:**
Acknowledges request and confirms permission to create record.

### Step 2: Clarify Record Purpose

**AI Asks:** "What is the purpose and scope of this conversation record?"

**User Provides:**
- **conversation_scope**: Purpose of the conversation being recorded
- **record_purpose**: Why this record is being created
- **ai_model_used**: The AI model name (MUST be provided by user)

**CRITICAL:** 
- AI model information MUST come from user
- AI will NOT infer or guess the model name
- User must explicitly specify which AI model is being used

**Example:**
```
Scope: OAuth 2.0 token refresh implementation session
Purpose: Document implementation decisions and code changes for team reference
AI Model: Claude Sonnet 4.5
```

### Step 3: Timestamp Generation

**What AI Does:**
- Retrieves current time using time tools or shell command
- Generates timestamp in `YYYYMMDD-HHmm` format

**Result:** Unique timestamp like "20251027-1530"

**You Should See:** Confirmation of timestamp retrieved.

### Step 4: Validate File Location (CRITICAL)

**What AI Does:**
1. Verifies staging directory exists at `.olaf/work/staging/`
2. Ensures `conversation-records/` subdirectory exists
3. Creates directory if missing
4. STOPS if path resolution fails

**MANDATORY PATH VALIDATION:**
- Path MUST resolve correctly before proceeding
- If validation fails, AI HALTS and asks for clarification
- No guessing or assuming paths

**You Should See:** Confirmation of validated path.

### Step 5: Create New File

**What AI Does:**
- Creates NEW file: `.olaf/work/staging/conversation-records/conversation-record-[timestamp].md`
- Uses unique timestamp to prevent filename conflicts
- NEVER appends to existing files
- Initializes file with proper structure

**File Naming:** `conversation-record-[timestamp].md`

### Step 6: Apply Template Structure

**What AI Does:**
Loads and applies conversation record template with sections:

1. Metadata (date, time, AI model, participants)
2. Conversation Purpose
3. Complete Conversation Narrative
4. Actions Taken
5. Files Affected
6. Key Decisions
7. Next Steps

### Step 7: Capture Complete Conversation

**What AI Does:**
Documents conversation with complete narrative:

**Format Example:**
```markdown
# Conversation Record - OAuth 2.0 Token Refresh Implementation

**Date:** 2025-10-27
**Time:** 15:30 EST
**AI Model:** Claude Sonnet 4.5
**Participants:** Jane Smith (Developer)

## Purpose
Document OAuth 2.0 token refresh implementation decisions and code changes

## Conversation Narrative

### Topic 1: Initial Requirements Discussion

**USER said:** "We need to implement automatic token refresh for OAuth 2.0"

**AI said:** "I'll help you implement OAuth 2.0 token refresh with PKCE flow. 
Let's start by reviewing the current authentication implementation."

**AI did:**
1. Read current authentication files
2. Analyzed token validation logic
3. Identified integration points

### Topic 2: Implementation

**USER said:** "Let's implement the token refresh endpoint"

**AI said:** "I'll create the refresh endpoint with proper error handling..."

**AI did:**
1. Created `src/auth/token-refresh.js`
2. Implemented refresh endpoint logic
3. Added error handling
4. Created test file

## Files Affected

**Created:**
- `src/auth/token-refresh.js` - Token refresh endpoint
- `tests/auth/token-refresh.test.js` - Test coverage

**Modified:**
- `src/auth/token-validator.js` - Updated validation
- `docs/authentication.md` - Added documentation

**Deleted:**
- None

## Key Decisions
1. Use PKCE flow for enhanced security
2. Implement automatic refresh 5 minutes before expiry
3. Store refresh tokens in secure HTTP-only cookies

## Next Steps
1. Complete error handling edge cases
2. Deploy to staging environment
3. Update client libraries
```

**Formatting Rules:**
- Clear headings for each distinct topic
- Format: **USER said:** / **AI said:** / **AI did:**
- Numbered lists for actions
- Bullet lists for files
- Relative paths from project root
- Complete narrative, NEVER summarize
- Correct user typos in record

### Step 8: Confirmation

**AI Provides:**
- Conversation record created with file path
- Number of distinct topics documented
- Number of actions captured
- Number of files affected
- Record location confirmation

**You Should See:** 
```
✓ Conversation record created: .olaf/work/staging/conversation-records/conversation-record-20251027-1530.md
✓ Topics documented: 3
✓ Actions captured: 12
✓ Files affected: 4
```

## Verification Checklist

✅ **Explicit user request confirmed** (never automatic)
✅ **AI model specified by user** (not inferred)
✅ **New file created** with unique timestamp
✅ **Path validated** before file creation
✅ **Complete conversation captured** (not summarized)
✅ **All actions documented** with tool calls
✅ **Files listed** with relative paths
✅ **Template structure followed** exactly
✅ **Clean markdown formatting** applied

## Troubleshooting

**If path validation fails:**
- Check staging directory exists
- Verify conversation-records subdirectory
- Manually specify path if needed

**If file creation fails:**
- Check directory permissions
- Verify sufficient disk space
- Ensure no file locks

**If timestamp conflicts:**
- Wait one minute and retry
- Manually specify different timestamp

**If conversation seems incomplete:**
- Review conversation history manually
- Add missing context explicitly
- Include references to external files

## Key Learning Points

1. **Explicit Permission**: Records only created when explicitly requested
2. **AI Model Transparency**: User must specify AI model, never inferred
3. **Complete Narrative**: Full conversation captured, never summarized
4. **Path Validation**: Mandatory validation prevents incorrect file locations
5. **Unique Files**: Each record is separate file, never appended

## Next Steps After Recording

- Use stored records for project continuity
- Reference records in handover documents
- Create records at end of significant sessions
- Link records to job files and decision records
- Archive records for project history

## Expected Timeline

- **Total time:** 5-10 minutes
- **User input:** 1-2 minutes for purpose and AI model
- **AI execution:** 4-8 minutes for conversation analysis and documentation

