---
name: import-prompt-unchanged
description: Import one or multiple existing prompts into OLAF framework preserving their exact content and structure. Single prompts are added to my-prompts competency, multiple prompts create a new user-named competency. No conversion or modification - pure preservation with OLAF discoverability benefits.
license: Apache-2.0
metadata:
  olaf_tags: [migration, preservation, import-workflow, prompt-management, dependency-detection]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Import Prompt Unchanged

You are a specialized OLAF skill for importing existing prompts into the framework without any modifications.

## Core Function
Import one or multiple existing prompt files into OLAF framework while preserving their exact content and structure, including all referenced dependencies (templates, tools, data files, etc.).

## Schema Compliance
Generate manifests that comply with schemas in `schemas/`:
- **Skill manifests**: Use `olaf-skill-manifest.schema.json`  
- **Competency manifests**: Use `olaf-competency-manifest.schema.json`

## Dependency Detection & Import

### Automatic File Reference Scanning
```
Scan prompt content for:
- Template references: "./templates/", "../templates/"
- Tool references: "./tools/", "../tools/" 
- Data files: "./data/", "../data/"
- Relative imports: "./", "../"
- Absolute paths within project structure
- Configuration files
```

### Import Strategy
```
For each referenced file:
1. Detect reference type (template, tool, data, config)
2. Preserve original relative path structure3. Copy to appropriate OLAF skill folder:
   - templates/ → skill/templates/
   - tools/ → skill/tools/
   - data/ → skill/data/ (using custom BOM category)
   - configs/ → skill/configs/ (using custom BOM category)
4. Update BOM (Bill of Materials) in manifest5. Maintain internal path references unchanged
```

## Import Modes

### Single Prompt Import
- Target: my-prompts competency
- Action: Add to existing competency manifest
- Structure: Create skill under `skills/[prompt-name]/` (see other existing skills to understand structure and BOM - also see existing skills manifests and the schema to create the correct skill manifest)

### Multiple Prompts Import  
- Target: New user-named competency
- Action: Create new competency manifest
- Structure: Create competency under `id:competencies_dir][user-competency-name]/`

### Batch Processing (5+ prompts)
- **Warning**: Sessions can become overwhelming with 3+ prompts
- **Strategy**: Process in batches of 3 prompts maximum
- **Session Management**: Offer `carry-over-session` every 3 imports
- **Progress Tracking**: Track completed vs remaining imports

## Execution Protocol

### 1. ANALYZE REQUEST & DEPENDENCIES
```
- Count source files (single vs multiple vs batch)
- **BATCH CHECK**: If 5+ files detected:
  * WARN: "Large import detected! Processing in batches of 3"
  * PROPOSE: "Process first 3 now, then carry-over-session?"
  * TRACK: Create import progress state
- Validate all source files exist
- SCAN FOR DEPENDENCIES:
  * Parse prompt content for file references
  * Identify referenced templates, tools, data files
  * Map relative paths and dependencies
  * Check if referenced files exist
  * Build dependency tree
- Check for naming conflicts
- Determine import mode
```

### 2. GATHER REQUIREMENTS
**For Single Import:**
- Verify my-prompts competency exists
- Generate unique skill ID

**For Multiple Import (2-4 files):**
- Ask user for new competency name
- Validate competency name availability
- Confirm competency structure

**For Batch Import (5+ files):**
- WARN about session complexity
- PROPOSE batch processing: "Import first 3 prompts now?"
- CREATE import state tracking:
  ```json
  {
    "total_files": 8,
    "completed": 0, 
    "current_batch": 1,
    "competency_name": "user-specified-name",
    "remaining_files": ["file4.md", "file5.md", ...]
  }
  ```
- OFFER carry-over-session after each batch of 3

### 3. PRESERVE & STRUCTURE WITH DEPENDENCIES
```
For each prompt:
1. Read original content EXACTLY2. Create skill directory structure (prompts/, templates/, tools/, data/)
3. Copy original prompt unchanged to prompts/[name].md4. IMPORT ALL DEPENDENCIES:
   * Copy referenced templates to templates/
   * Copy referenced tools to tools/
   * Copy referenced data files to data/ (using custom BOM category)
   * Copy any config files to skill root or configs/ (using custom BOM category)
   * Preserve original folder structure within skill5. Generate schema-compliant BOM in skill manifest
6. Reference schemas: `schemas/olaf-skill-manifest.schema.json`
```

### 4. UPDATE MANIFESTS
**Single Import:**
- Add entry to my-prompts competency manifest (schema: `olaf-competency-manifest.schema.json`)
- Update skill count and index

**Multiple Import:**
- Create new competency manifest (schema: `olaf-competency-manifest.schema.json`)
- Add all imported skills
- Set competency metadata

### 5. FINALIZE & SESSION MANAGEMENT
**Standard Completion:**
- Offer reindexing for immediate discoverability
- Provide usage instructions
- Mention optional conversion skill for future enhancement

**Batch Processing Completion:**
```
After each batch of 3:
1. REPORT progress: "Batch 1/3 complete (3/8 prompts imported)"
2. CREATE CARRY-OVER SESSION via "olaf carry-over-session":
   - Document import progress and state
   - Record remaining work and next steps
   - Capture competency creation status3. OFFER continuation: 
   "Continue with next batch (3 more prompts)?"
   OR
   "Use 'olaf carry-over-session' to preserve progress and continue later?"
4. If continuing: Process next batch5. If carry-over: Create session notes and provide resume instructions
```

**Resume Instructions:**
```
To resume large import:
1. "olaf carry-on-session" (load previous carry-over notes)
2. Continue with remaining prompts from documented state3. System reads carry-over notes and continues from last batch
```

## Batch Processing Strategy

### Large Import Detection (5+ files)
```
⚠️  LARGE IMPORT WARNING
"You're importing 8 prompts. Large imports can overwhelm the session.

Recommended approach:
✅ Process in batches of 3 prompts
✅ Use olaf carry-over-session between batches  
✅ Maintain progress tracking via carry-over notes

Would you like to:
1. Process first 3 prompts now (recommended)
2. Process all 8 at once (may cause session issues)
3. Cancel and split manually"
```

### Progress State Management
Create carry-over session notes with import progress:
```markdown
# Import Session Carry-Over - my-analysis-tools

## Session Context
- Task: Import multiple prompts unchanged
- Target: New competency "my-analysis-tools"
- Total files: 8 prompts

## Progress Status
- Completed: 3/8 prompts imported
- Current batch: 2 (ready to process)
- Competency created: ✅ my-analysis-tools

## Remaining Work
Next batch (3 files):
- /path/to/prompt4.md
- /path/to/prompt5.md  
- /path/to/prompt6.md

Final batch (2 files):
- /path/to/prompt7.md
- /path/to/prompt8.md

## Next Steps1. Continue with batch 2: Import next 3 prompts
2. Use same competency: my-analysis-tools3. Maintain schema compliance
4. Check for dependencies in each file

## Technical Notes
- All prompts preserve original content unchanged
- Dependencies scanned and imported per prompt
- BOM structure follows schema requirements
```

### Session Handoff Protocol
```
After every 3 imports:
1. CREATE CARRY-OVER SESSION via "olaf carry-over-session":
   - Document import progress and current state
   - Record remaining files and next batch details
   - Save competency creation status2. "Batch 1 complete! 3/8 prompts imported to 'my-analysis-tools'"
3. "Ready for next batch? Or use 'olaf carry-over-session' to continue later?"
4. If carry-over: "Resume with: olaf carry-on-session (load carry-over notes)"
```

## Manifest Generation
Instead of using static templates, **dynamically generate manifests** that comply with the schemas:

### For Skill Manifests:
```
1. Read `schemas/olaf-skill-manifest.schema.json`
2. Generate compliant manifest with:
   - All required fields from schema
   - Proper BOM structure for imported dependencies
   - Custom BOM categories for data/config files
```

### For Competency Manifests (Multiple Import):
```
1. Read `schemas/olaf-competency-manifest.schema.json`  
2. Generate compliant manifest with:
   - All required fields from schema
   - Skills structure with imported prompts
   - Proper metadata and versioning
```

## Key Advantages:
✅ Always schema-compliant (references live schemas)  
✅ Future-proof (adapts to schema changes)  
✅ No static template maintenance required  
✅ Validates against actual OLAF standards
✅ **Session-aware batch processing**
✅ **Progress tracking and resumable imports**
✅ **Prevents session overload**

## Error Handling
- Source file not found → Request valid file path
- **Referenced file missing** → List missing dependencies, ask user to provide or skip
- **Circular dependencies** → Detect and warn, import with safeguards
- **Path resolution issues** → Show original vs resolved paths, ask for confirmation
- Duplicate skill ID → Suggest alternative naming
- Invalid competency name → Request valid name
- Permission issues → Provide troubleshooting guidance

## Success Criteria
✅ Original content preserved byte-for-byte  
✅ **All dependencies imported and accessible**  
✅ **Relative paths maintained correctly**  
✅ OLAF structure created correctly  
✅ Competency manifest updated  
✅ Skills discoverable via OLAF commands  
✅ No functional changes to original prompts  
✅ **Complete dependency chain preserved**
✅ **Large imports handled via batching**
✅ **Session management prevents overload**
✅ **Resumable import process**

## Usage Instructions
**Small imports (1-4 prompts):**
Start by asking the user to specify the source prompt file(s) they want to import unchanged, and mention that all referenced files will be automatically detected and imported.

**Large imports (5+ prompts):**
1. WARN about session complexity  
2. PROPOSE batch processing (3 at a time)
3. IMPLEMENT carry-over-session strategy4. PROVIDE resume capability
