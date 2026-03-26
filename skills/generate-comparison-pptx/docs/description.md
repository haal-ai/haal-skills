# generate-comparison-pptx

## Overview
Generate a professional PowerPoint presentation comparing multiple items (models, tools, products, approaches) using charts and visual cards.

## Purpose
Create visually compelling comparison decks from benchmark data, evaluation results, or any structured comparison. Supports charts, scoring cards, and visual grids for clear side-by-side analysis.

## Key Features
- Any comparison data (not limited to LLM models)
- Chart generation (bar, radar, grouped bar)
- Theme-aware design with PowerPoint theme slots
- Visual scoring cards and comparison grids
- Template-based with branded dark theme
- Sources slide with clickable hyperlinks
- 3-8 slides scaled to data complexity

## Usage
Invoke this skill by saying:
- "Create a comparison presentation of these three tools"
- "Generate a PPTX comparing our benchmark results"
- "Make slides showing differences between approaches"
- "Build a deck comparing these LLM models"

## Parameters

### Required
- **items**: Items to compare (models, tools, products, etc.)
- **metrics**: Comparison criteria or benchmark data

### Optional
- **output_location**: Custom output path (default: `.olaf/work/presentations/<name>/`)

## Process Flow
1. **Gather Comparison Data** — Collect items, metrics, and scores
2. **Plan Slide Architecture** — Title + 2-6 content slides + sources
3. **Generate Python Script** — Create self-contained script with chart helpers
4. **Run Script** — Execute to produce `.pptx`
5. **Review** — Open and verify charts and visual accuracy

## Output
- Python generation script (`generate_pptx.py`)
- PowerPoint file (`.pptx`) with native charts and editable shapes
- Saved in `.olaf/work/presentations/<presentation-name>/`

## Related Skills
- **distill-docs-to-pptx**: For distilling documentation (not comparisons)
- **generate-pptx-from-plan**: For generating from markdown presentation plans
