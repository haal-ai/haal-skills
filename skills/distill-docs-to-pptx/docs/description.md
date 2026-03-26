# distill-docs-to-pptx

## Overview
Distill large or multiple markdown documentation files into a concise, professional PowerPoint presentation. Transforms hundreds of lines of technical docs into 4-8 visual slides.

## Purpose
Save audiences from reading extensive markdown documentation by extracting key concepts into scannable, professional slides. Use when you need to present complex technical documentation to a team without forcing them to read the source files.

## Key Features
- Automatic content density analysis (scales slides to source size)
- Theme-aware design using PowerPoint theme slots (colors adapt when switching themes)
- Layout resolution by name (not hardcoded indices)
- Professional dark-themed template with branded slide masters
- Visual hierarchy using cards, badges, and phase flows
- Insight boxes on every content slide for key takeaways
- Sources slide with clickable hyperlinks

## Usage
Invoke this skill by saying:
- "create a presentation from this documentation"
- "distill these docs into slides"
- "make a deck explaining this architecture"
- "turn this markdown into a PowerPoint"

## Parameters

### Required
- **source_files**: One or more markdown documentation files to distill

### Optional
- **output_location**: Custom output path (default: `.olaf/work/presentations/<name>/`)

## Process Flow
1. **Read & Analyze** — Identify core purpose, key concepts, visual structures, numbers, and design principles
2. **Plan Slide Structure** — Decide slide count based on content density (3-8 content slides)
3. **Generate Python Script** — Create self-contained `generate_pptx.py` with inlined helpers
4. **Pre-run Checklist** — Verify template usage, layout helpers, theme colors
5. **Run Script** — Execute to produce `.pptx` file
6. **Open & Review** — Present the generated file

## Output
- Python generation script (`generate_pptx.py`)
- PowerPoint file (`.pptx`) with native editable shapes and text
- Saved in `.olaf/work/presentations/<presentation-name>/`

## Related Skills
- **generate-comparison-pptx**: For comparing items with metrics (not distillation)
- **generate-pptx-from-plan**: For generating from a markdown presentation plan
- **create-presentation-and-posts-workflow**: For full content packages (slides + blog posts)
