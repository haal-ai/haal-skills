# generate-pptx-from-plan

## Overview
Generate dynamic PowerPoint presentations from markdown presentation plans using modern theme-aware architecture with intelligent layout adaptation.

## Purpose
Transform structured markdown presentation plans into professional PowerPoint files. Unlike distill-docs-to-pptx (which distills documentation), this skill is plan-driven and content-flexible — it creates exactly what your plan specifies.

## Key Features
- Smart content analysis (auto-detects bullets, paragraphs, key-value pairs)
- Theme-aware design using PowerPoint theme slots
- Layout resolution by name (not hardcoded indices)
- Flexible structure (no rigid slide count or format constraints)
- Native editable PPTX output with shapes, cards, and visual elements
- Professional dark-themed template support

## Usage
Invoke this skill by saying:
- "Generate a PowerPoint from this presentation plan"
- "Create slides from my outline"
- "Build a PPTX from this markdown plan"

## Parameters

### Required
- **plan_source**: Markdown presentation plan (file path or inline content)

### Optional
- **output_location**: Custom output path (default: `.olaf/work/presentations/<name>/`)
- **template**: Custom PowerPoint template (default: bundled dark theme)

## Process Flow
1. **Parse Plan** — Read and interpret the markdown presentation plan
2. **Content Analysis** — Detect content types per slide (bullets, paragraphs, key-value, etc.)
3. **Layout Selection** — Choose optimal layout for each slide's content
4. **Generate Python Script** — Create self-contained generation script
5. **Run Script** — Execute to produce `.pptx` file
6. **Review** — Open and verify output

## Output
- Python generation script (`generate_pptx.py`)
- PowerPoint file (`.pptx`) with native editable content
- Saved in `.olaf/work/presentations/<presentation-name>/`

## Related Skills
- **distill-docs-to-pptx**: For distilling documentation into slides
- **generate-comparison-pptx**: For comparison-focused presentations
- **create-presentation-and-posts-workflow**: For full content packages
