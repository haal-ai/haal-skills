---
name: create-presentation-plan
description: Create comprehensive presentation plan based on requirements for PowerPoint generation or live presentation delivery
license: Apache-2.0
metadata:
  olaf_tags: [presentation, planning, technical-writing, content-creation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **topic**: string - Presentation subject and key objectives (REQUIRED)
- **audience**: string - Target audience and their needs (REQUIRED)
- **presentation_type**: reading_only|live_presentation - Type of presentation delivery (REQUIRED)
- **slide_count**: number - Number of slides for reading-only presentations (OPTIONAL, default: 5)
- **duration**: number - Duration in minutes for live presentations (REQUIRED if live_presentation)
- **language**: english|french|spanish|german - Target language (OPTIONAL, default: english)
- **include_image_prompts**: boolean - Whether to include visual element descriptions (OPTIONAL, default: false)

## User Interaction

You MUST follow these interaction guidelines:
- Present presentation plan structure for user approval before creating
- Provide clear progress updates during slide count calculations
- Confirm content accuracy and source validation with user
- Report completion with file location and next steps

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm topic and audience are clearly defined
- Validate presentation type (reading_only or live_presentation)
- For live presentations: ensure duration is provided
- For reading-only: validate slide count (default to 5 if not provided)
- Check language preference is supported

### 2. Execution Phase
You WILL execute these operations:

**Presentation Planning Operations**:
- Analyze user requirements for topic, audience, and objectives
- Calculate appropriate slide count:
  - **Reading only**: Use specified slide count (default: 5)
  - **Live presentation**: Use formula (duration ÷ 5) + 2 slides (intro + conclusion)
- Structure presentation with logical flow in target language
- Define slide titles, layouts, and content for each slide

**Content Development Guidelines**:
- **CRITICAL**: ONLY use content from provided source materials - NEVER invent, assume, or extrapolate beyond what was explicitly analyzed or documented
- **IMPORTANT**: Do NOT use bullet point prefixes (•, -, *) in slide content - write content directly without prefixes
- **SOURCE VALIDATION**: Each slide must reference actual findings from source documents - if content wasn't analyzed, state "Not covered in current analysis phase"

**Template Usage**:
- Use presentation plan template: `templates/presentation-plan-template.md`
- Apply calculated slide count based on presentation type
- Include image prompts only if specifically requested by user

**File Operations**:
- Create timestamped filename using YYYYMMDD-HHmm format
- Ensure staging directory exists: `.olaf/work/staging/`
- Save plan file: `.olaf/work/staging/[presentation-name]-plan-YYYYMMDD-HHmm.md`

### 3. Validation Phase
You WILL confirm successful completion:
- Verify presentation plan has logical flow and structure
- Confirm appropriate slide count for presentation type
- Validate content is in requested target language
- Check file is saved to staging directory with proper naming

## Output Format
- **Format**: Structured markdown following presentation plan template
- **Structure**: 
  - Header with presentation metadata (title, audience, type, duration/slides, language, objective)
  - Slide-by-slide breakdown with layout and content specifications
  - Optional image prompts (only if requested)
  - Implementation notes and requirements
- **File outputs**: Presentation plan saved as timestamped markdown file
- **Naming conventions**: `[presentation-name]-plan-YYYYMMDD-HHmm.md`

## User Communication
- **Progress updates**: Inform user of slide count calculations and structure decisions
- **Confirmations**: Present plan outline for approval before detailed creation
- **Error reporting**: Clear communication of any missing requirements or validation issues
- **Success indicators**: Confirm plan is ready for review, editing, or PowerPoint generation

## Domain-Specific Rules
- **Content Accuracy**: Only include information from provided source materials
- **No Speculation**: If information wasn't covered in analysis, clearly state this rather than making assumptions
- **Formatting Standards**: Use clear, professional presentation structure without bullet prefixes
- **Language Consistency**: Maintain target language throughout all content
- **Visual Elements**: Include image prompts only when explicitly requested by user

## Success Criteria
- [ ] All required parameters provided (topic, audience, presentation_type)
- [ ] Appropriate slide count calculated based on type and duration
- [ ] Presentation plan follows template structure
- [ ] Content maintains professional quality and accuracy
- [ ] File saved to staging directory with proper timestamp naming
- [ ] Plan ready for PowerPoint generation or user editing

## Error Handling
- **Missing parameters**: Request specific missing information (topic, audience, or presentation type)
- **Invalid duration**: For live presentations, ensure duration is realistic (minimum 5 minutes)
- **Language not supported**: Default to English if unsupported language requested
- **Template access issues**: Use fallback structure if template file unavailable
- **File save failures**: Provide alternative manual copy option for presentation plan

## Notes
- **Dependencies**: Requires presentation plan template in templates/ directory
- **Performance**: Plan creation typically completed within 2-3 minutes
- **Limitations**: Content quality depends on provided source materials and requirements clarity
- **Integration**: Plan output designed for seamless integration with PowerPoint generation tools
