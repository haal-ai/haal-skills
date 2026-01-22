# Create Presentation and Posts Workflow

**Skill ID**: `create-presentation-and-posts-workflow`  
**Version**: 1.0.0  
**Protocol**: Propose-Confirm-Act  
**Status**: Proven

## Overview

This skill orchestrates a complete multi-format content creation workflow that transforms a single topic into three deliverables: a structured presentation plan, a PowerPoint file, and blog posts. It executes a sequential process that ensures consistency across all content formats while adapting to different presentation types and audience needs.

## Purpose

Creating content in multiple formats from the same source material is time-consuming and often results in inconsistent messaging. This workflow solves that problem by automating the generation of presentations and blog posts from a single presentation plan, ensuring all deliverables maintain consistent messaging, tone, and target language while adapting appropriately to each format.

## Usage

**Command**: `olaf create presentation and posts workflow`

**When to Use**: Use this skill when you need to create comprehensive content packages for technical topics, product launches, feature announcements, or educational materials that require both presentation and written formats. Ideal for situations where you need to present information live or as reading material, then follow up with blog posts for broader distribution.

## Parameters

### Required Inputs
- **Topic**: The presentation subject and key objectives you want to communicate
- **Audience**: Target audience description and their specific needs or knowledge level
- **Presentation Type**: Either "reading only" (specify slide count) or "live presentation" (specify duration in minutes)
- **Language**: Target language - English (default), French, Spanish, or German

### Optional Inputs
- **Post Style**: Choose "brochure" (structured, feature-focused), "conversational" (narrative, story-driven), or "all" (both styles)
- **Visual Elements**: Whether to include image prompts in the presentation plan (not included by default)

### Context Requirements
- Access to dependent skills: `create-presentation-plan`, `generate-pptx-from-plan`, `generate-post-from-plan`
- Python environment with python-pptx library installed
- Write permissions to staging directory
- Clear understanding of your topic and target audience

## Output

This skill produces a complete content package from a single source plan.

**Deliverables**:
- Presentation plan (markdown file) with structured slide content
- PowerPoint presentation (pptx file) generated from the plan
- Blog post(s) (markdown file) in requested style(s) - brochure, conversational, or both

**Format**: All files are saved to `.olaf/work/staging/pptx-folder/` with consistent timestamped naming (YYYYMMDD-HHmm format) and use the same source content to ensure messaging consistency across formats.

## Examples

### Example 1: Product Feature Launch

**Scenario**: You need to announce a new API feature to developers, including a 15-minute presentation for a team meeting and a blog post for the developer portal.

**Command**:
```
olaf create presentation and posts workflow
```

**Input**:
- Topic: "New GraphQL API Endpoints for Real-Time Data"
- Audience: Backend developers and API consumers
- Presentation Type: Live presentation, 15 minutes
- Language: English
- Post Style: conversational

**Result**: Generated a 5-slide presentation plan (15÷5+2), PowerPoint file with technical diagrams, and an engaging conversational blog post explaining the feature benefits with code examples.

### Example 2: Technical Documentation for Reading

**Scenario**: Creating comprehensive documentation about a security architecture that stakeholders can review at their own pace, plus a structured blog post for the company blog.

**Command**:
```
olaf create presentation and posts workflow
```

**Input**:
- Topic: "Zero-Trust Security Architecture Implementation"
- Audience: Security engineers and IT managers
- Presentation Type: Reading only, 8 slides
- Language: English
- Post Style: brochure

**Result**: Generated an 8-slide presentation plan optimized for reading, PowerPoint file with architecture diagrams, and a structured brochure-style blog post with clear sections and bullet points.

## Dependencies

### Required Skills
- **create-presentation-plan**: Creates structured presentation outline
- **generate-pptx-from-plan**: Converts plan to PowerPoint file
- **generate-post-from-plan**: Creates blog posts from presentation content

### Technical Dependencies
- Python 3.7+ with python-pptx library
- File system write access to staging directory

## Related Skills

- **create-presentation-plan**: The first step of this workflow - use standalone if you only need a presentation plan
- **generate-pptx-from-plan**: The second step - use standalone if you already have a plan and only need PowerPoint generation
- **generate-post-from-plan**: The third step - use standalone if you have a plan and only need blog post generation

## Tips & Best Practices

- Review and edit the presentation plan after Step 1 before proceeding to PowerPoint generation - this is your opportunity to refine content
- For live presentations, use the formula (duration ÷ 5) + 2 slides to ensure appropriate pacing (5 minutes per content slide)
- For reading-only presentations, consider 5-8 slides for optimal comprehension without overwhelming readers
- Choose "all" for post style if you're unsure - you can decide which blog post version to publish after reviewing both
- Include image prompts only if you have resources to create or source the images - they're optional for a reason
- Ensure all deliverables are reviewed before distribution, especially if content contains technical specifications or product details

## Limitations

- Requires Python environment with python-pptx library for PowerPoint generation
- PowerPoint generation tool has specific formatting capabilities - complex custom layouts may require manual adjustment
- Blog posts are limited to under 2-minute reading time (300-600 words) - longer content requires multiple posts or different format
- Sequential workflow means if one step fails, subsequent steps cannot proceed until the issue is resolved
- All content is generated from the same presentation plan - if plan structure doesn't suit blog format, consider using generate-post-from-plan separately with different source material

## Workflow Steps

1. **Plan Creation** → Gather requirements and create structured presentation plan
2. **PowerPoint Generation** → Convert plan to professional presentation file
3. **Blog Post Generation** → Create written content in requested style(s)
4. **Deliverable Summary** → Provide complete package overview

Each step includes user interaction points and error handling to ensure quality output.