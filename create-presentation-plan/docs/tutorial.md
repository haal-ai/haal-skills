# Create Presentation Plan - Step-by-Step Tutorial

## Overview

This tutorial guides you through using the **create-presentation-plan** skill to create professional, structured presentation plans that serve as the foundation for PowerPoint generation or live presentation delivery.

## Prerequisites

- Access to the OLAF framework with create-presentation-plan skill
- Clear understanding of your presentation topic and audience
- Decision on presentation type (reading-only vs. live presentation)

## Step-by-Step Process

### Step 1: Initiate the Skill

**Command**: `olaf create-presentation-plan`

The skill will start and request the required parameters for your presentation planning.

### Step 2: Provide Core Information

You'll be prompted to provide essential information:

**Required Parameters:**
- **Topic**: Your presentation subject and key objectives
  - Example: "Enterprise Cloud Migration Strategy and Implementation Roadmap"
- **Audience**: Target audience and their needs
  - Example: "Executive leadership team and IT directors with mixed technical knowledge"

**Example Response:**
```
Topic: Enterprise Cloud Migration Strategy and Implementation Roadmap
Audience: Executive leadership team and IT directors with mixed technical knowledge
```

### Step 3: Select Presentation Type

Choose between two presentation types:

**Option A: Reading-Only Presentation**
- For presentations that will be read but not presented live
- You'll need to specify the number of slides (default: 5)
- Example: "Reading only, 7 slides"

**Option B: Live Presentation**
- For presentations delivered to an audience
- You'll need to specify duration in minutes
- Slide count will be calculated automatically: (duration ÷ 5) + 2 slides
- Example: "Live presentation, 30 minutes" → Results in 8 slides

### Step 4: Configure Optional Settings

**Language Selection (Optional)**
- English (default)
- French
- Spanish  
- German

**Visual Elements (Optional)**
- Choose whether to include image prompts for visual elements
- Default: No image prompts
- If yes, descriptions for relevant visuals will be included

**Example Configuration:**
```
Presentation Type: Live presentation
Duration: 25 minutes
Language: English
Include image prompts: No
```

### Step 5: Review the Calculated Structure

The skill will present the planned structure:
- **Calculated slide count**: Based on your type and duration
- **Presentation outline**: Overview of planned structure
- **Content approach**: How information will be organized

**Example Output:**
```
Calculated Slides: 7 slides (25-minute live presentation)
Structure: Title → Agenda → Current State → Migration Strategy → Implementation Plan → Timeline & Next Steps → Q&A
```

### Step 6: Confirm Plan Creation

The skill will ask for your approval before creating the detailed plan:
- Review the proposed structure
- Confirm the approach meets your needs
- Approve creation of the detailed presentation plan

### Step 7: Review Generated Plan

The skill will create and save a comprehensive presentation plan:

**File Location**: `[staging_directory]/[presentation-name]-plan-YYYYMMDD-HHmm.md`

**Plan Content Includes:**
- Presentation metadata (title, audience, type, duration)
- Slide-by-slide breakdown with layout recommendations
- Content guidance for each slide
- Optional image prompts (if requested)
- Implementation notes

### Step 8: Next Steps Options

After plan creation, you can:

**Option A: Edit the Plan**
- Review and modify the generated plan as needed
- Add specific content details
- Adjust structure or messaging

**Option B: Generate Content**
- Use `generate-post-from-plan` to create detailed slide content
- Use `create-presentation-and-posts-workflow` for multi-format content

**Option C: Create PowerPoint**
- Use `generate-pptx-from-plan` to automatically generate PowerPoint slides
- Requires the presentation plan as input

## Example Walkthrough

### Scenario: Technical Team Presentation

**Initial Request:**
"I need to create a presentation about our new API architecture for the development team."

**Step-by-Step Interaction:**

```
User: olaf create-presentation-plan

System: I'll help you create a comprehensive presentation plan. Let me gather the required information.

Topic: New API Architecture Overview and Implementation Guide
Audience: Development team (senior and junior developers)

System: What type of presentation is this?
User: Live presentation, 20 minutes

System: Language preference?
User: English

System: Include image prompts for visual elements?
User: Yes

System: Based on your requirements:
- Topic: New API Architecture Overview and Implementation Guide  
- Audience: Development team (senior and junior developers)
- Type: Live presentation (20 minutes)
- Calculated slides: 6 slides (20÷5 + 2 = 6)
- Language: English
- Visual elements: Yes

Proposed structure:
1. Title Slide
2. Agenda & Objectives  
3. Current Architecture vs. New API Design
4. Key Benefits & Technical Improvements
5. Implementation Timeline & Next Steps
6. Q&A & Discussion

Shall I create this presentation plan?

User: Yes, please create it.

System: ✅ Presentation plan created successfully!
File saved: staging/api-architecture-presentation-plan-20251119-1145.md

The plan is ready for review and can be used for:
- Content generation with generate-post-from-plan
- PowerPoint creation with generate-pptx-from-plan  
- Multi-format content with create-presentation-and-posts-workflow
```

## Common Use Cases and Tips

### Business Presentations
- Focus on outcomes and business value
- Include executive summary and key takeaways
- Consider time for questions and discussion

### Technical Presentations  
- Balance technical depth with audience knowledge
- Include diagrams and visual aids
- Plan for demo time if applicable

### Training Presentations
- Structure for learning progression
- Include practice exercises or examples
- Plan for interaction and engagement

### Client Presentations
- Focus on client value and benefits
- Include clear next steps and calls to action
- Prepare for various question scenarios

## Troubleshooting

### Common Issues and Solutions

**Issue**: "Not enough content for the duration"
**Solution**: Adjust presentation type to reading-only with fewer slides, or add more detailed sections

**Issue**: "Too technical for the audience"
**Solution**: Revise audience description to be more specific about technical knowledge level

**Issue**: "Plan seems too high-level"
**Solution**: Use the plan as foundation and generate detailed content with generate-post-from-plan

**Issue**: "Need visual elements but didn't request them initially"
**Solution**: Re-run with image prompts enabled, or manually add visual descriptions to the plan

## Best Practices

### Effective Planning
- Be specific about audience knowledge and needs
- Consider presentation environment (formal vs. informal)
- Plan for interaction and engagement opportunities
- Allow buffer time for questions and discussion

### Content Organization
- Start with clear objectives and agenda
- Use logical flow from context to conclusion
- Include clear takeaways and next steps
- Balance content depth with time constraints

### Follow-up Actions
- Review and refine the generated plan
- Validate content accuracy with source materials
- Consider integration with other OLAF skills for complete content creation
- Test presentation flow and timing before delivery

## Integration Examples

### Complete Presentation Workflow
1. **Planning**: `create-presentation-plan` → Generate structure
2. **Content**: `generate-post-from-plan` → Create detailed content  
3. **Slides**: `generate-pptx-from-plan` → Produce PowerPoint
4. **Multi-format**: Export to blog posts, documentation, etc.

### Research-Driven Presentations
1. **Research**: `research-and-report` → Gather information
2. **Planning**: `create-presentation-plan` → Structure findings
3. **Content**: `generate-post-from-plan` → Develop detailed slides
4. **Generation**: `generate-pptx-from-plan` → Create final presentation