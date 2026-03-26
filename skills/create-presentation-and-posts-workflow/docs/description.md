# create-presentation-and-posts-workflow

## Overview
Multi-format content creation workflow that transforms a topic into a presentation plan, PowerPoint file, and blog posts (brochure and/or conversational style).

## Purpose
This skill exists to generate a complete content package from a single topic. Use it when you need presentation slides, a PowerPoint file, and blog posts for different audiences all derived from one subject.

## Key Features
- Sequential workflow: plan → PowerPoint → blog posts
- Supports reading-only or live presentation types
- Multilingual support (English, French, Spanish, German)
- Multiple blog post styles (brochure, conversational, both)
- Consistent messaging across all output formats

## Usage
Invoke this skill by saying:
- "create a presentation and blog posts about X"
- "generate content package for topic Y"
- "build slides and posts for my talk"

## Parameters

### Required
- **topic**: Presentation subject
- **audience**: Target audience description
- **presentation_type**: reading-only (slides) | live (duration in minutes)

### Optional
- **language**: English | French | Spanish | German (default: English)
- **post_style**: brochure | conversational | all (default: all)
- **visual_elements**: boolean (default: false)

## Process Flow
1. **Create Presentation Plan** — Generate structured slide plan
2. **Generate PowerPoint** — Build .pptx from plan
3. **Generate Blog Posts** — Create posts in selected style(s)
4. **User review points** — Approval gates between phases
5. **Consolidate outputs** — Deliver complete package

## Output
- Presentation plan (markdown)
- PowerPoint file (.pptx)
- Blog post(s) in requested style(s) and language

## Related Skills
- **generate-pptx-from-plan**: PowerPoint generation step
- **distill-docs-to-pptx**: Alternative for documentation-to-slides
