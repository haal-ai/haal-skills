---
name: generate-pptx-from-plan
description: >
  Generate dynamic PowerPoint presentations from markdown presentation plans using
  modern theme-aware architecture. Creates flexible, professional presentations
  that adapt content layout based on plan structure without rigid constraints.
license: Apache-2.0
metadata:
  olaf_tags: [presentation, powerpoint, automation, technical-writer, content-creation, dynamic-layout]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and time, use time tools, fallback to shell command if needed

## What This Skill Does

This skill transforms your markdown presentation plans into professional PowerPoint presentations with **intelligent, dynamic layout adaptation**:

🎯 **Smart Content Analysis** - Automatically detects content types (bullets, paragraphs, key-value pairs) and applies optimal layouts  
🎨 **Theme-Aware Design** - Uses PowerPoint theme slots so colors adapt when you switch themes  
📐 **Modern Layout System** - Resolves layouts by name, not hardcoded indices for maximum compatibility  
🔄 **Flexible Structure** - No rigid constraints on slide count or format - creates what serves your content best  
✨ **Professional Output** - Native editable PPTX with shapes, cards, and visual elements

**Key difference from distill-docs-to-pptx**: This skill is **plan-driven** and **content-flexible**, while distill-docs-to-pptx is **documentation-driven** and **structure-optimized**.

## Input Parameters
You MUST request these parameters if not provided by the user:

1. **plan_file_path**: string - Path to existing presentation plan (.md file) (REQUIRED)

2. **output_directory**: string - Target directory for PowerPoint file (OPTIONAL - auto-generated as `.olaf/work/presentations/[presentation-name]/`)

3. **confirmation**: boolean - User approval to proceed with generation (REQUIRED)

## User Interaction
You MUST follow these interaction guidelines:
- Present plan summary and slide count before generation
- Request user confirmation before proceeding
- Provide clear progress updates during generation
- Report any errors immediately with actionable resolution steps
- Confirm successful generation with file location

## Prerequisites
You MUST validate:
- Plan file exists and is readable
- Python environment has `python-pptx` library installed
- Output directory is writable
- Plan follows basic markdown structure with slide headers

## Process Overview

The skill follows a structured workflow that ensures professional output:

### Phase 1: Analysis & Planning
1. **Read and analyze** the presentation plan file
2. **Extract slide structure** and content patterns
3. **Determine optimal layouts** based on content analysis
4. **Create dedicated output folder**: `.olaf/work/presentations/[presentation-name]/`

### Phase 2: Generation & Validation  
1. **Copy template** from `scripts/template.pptx` to output folder
2. **Generate dedicated Python script** with enhanced visual logic
3. **Execute script** to create presentation
4. **Validate output** and open generated presentation

### Phase 3: Delivery & Confirmation
1. **Confirm successful generation** with file location
2. **Open presentation** for user review
3. **Provide summary** of visual enhancements applied

---

## Process Details

### 1) Analysis Phase
You WILL:
- Read and validate the presentation plan file
- Extract slide titles, content, and layout instructions
- Analyze content patterns for optimal visual treatment
- Create output directory: `.olaf/work/presentations/[presentation-name]/`

### 2) Generation Phase (Only after approval)
You WILL:
- **Copy template**: `scripts/template.pptx` → output folder
- **Generate script**: Create `generate_pptx.py` with enhanced visual logic
- **Execute script**: Run from output directory to create presentation
- **Apply visual enhancements**: Icons, colors, layouts, progress bars, etc.

### 3) Output & Validation
You WILL:
- Save presentation as: `[presentation-name].pptx`
- Verify file opens correctly with all visual elements
- Confirm presentation structure matches plan intent
- Provide user with file location and visual summary

## Supported Plan Formats

The skill accepts flexible markdown plan structures:

```markdown
# Presentation Title

### Slide 1: Introduction
**Layout**: title slide
**Content**: 
- Welcome to this presentation
- Today we'll explore...
- Let's begin our journey

### Slide 2: Key Points
**Layout**: title-only
**Content**:
• First important concept
• Second critical insight  
• Third key takeaway

### Slide 3: Detailed Analysis
**Content**:
Point 1: This is the first major point with detailed explanation
Point 2: Here's the second point with supporting information
Point 3: The third point concludes our analysis

### Slide 4: Conclusion
**Content**:
Thank you for your attention
Questions and discussion welcome
```

## Dynamic Layout Intelligence

The skill automatically adapts based on content:

| Content Pattern | Applied Layout | Visual Style |
|-----------------|----------------|-------------|
| Bullet points (`-` or `*`) | Clean bullet list | Aligned bullets with proper spacing |
| Short phrases (≤3 lines) | Centered emphasis | Large, centered text |
| Key-value pairs (`:`) | Card layout | Colored cards with accent borders |
| Long paragraphs | Text columns | Multi-column readable layout |
| Mixed content | Hybrid layout | Combination of elements |

## Success Criteria
You WILL consider the task complete when:
- [ ] Plan file is successfully parsed and analyzed
- [ ] User approval obtained for generation
- [ ] Presentation generated with dynamic layouts
- [ ] All content properly formatted and readable
- [ ] Output file saved in specified location
- [ ] User provided with file location and summary

## Error Handling
You WILL handle these scenarios:
- **Missing plan file**: Ask user for correct file path
- **Malformed markdown**: Provide specific formatting guidance
- **Missing dependencies**: Guide user through python-pptx installation
- **Permission issues**: Suggest alternative output locations

## Output Format
- **Format**: PowerPoint presentation (.pptx file)
- **Structure**: Dynamic slides based on content analysis
- **File naming**: `[presentation-title]_YYYYMMDD_HHMM.pptx`
- **Location**: `.olaf/work/presentations/[presentation-name]/`

## User Communication
You WILL provide these updates:

### Progress Updates
- Plan analyzed and structure identified
- Content types detected and layout strategy planned
- Presentation generation in progress
- File saved successfully

### Completion Summary
- Total slides created and layout types used
- Dynamic adaptations applied
- File location and naming details
- Any content optimizations made

### Next Steps
- Review generated presentation
- Customize further in PowerPoint if needed
- Share with audience or use for intended purpose

## Technical Requirements

### Dependencies
- Python environment (3.10+ recommended)
- python-pptx library (will be checked and installed if needed)
- Access to `scripts/generate_pptx.py` automation tool
- Write access to `.olaf/work/presentations/`

### File Formats
- **Input**: Markdown presentation plan (.md)
- **Output**: PowerPoint presentation (.pptx)
- **Naming**: Timestamped format YYYYMMDD-HHmm

### Output Location
Generated PowerPoint file: `.olaf/work/presentations/[presentation-name]/[presentation-name].pptx`

## Notes
This skill specializes in automated PowerPoint generation from structured presentation plans using Python automation tools. It maintains compatibility with existing presentation planning workflows and ensures professional output formatting.
