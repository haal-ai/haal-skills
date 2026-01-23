# Generate Post From Plan - Step-by-Step Tutorial

**How to Execute the "Generate Blog Post from Presentation Plan" Workflow**

This tutorial shows exactly how to transform presentation content or technical documentation into engaging blog posts using the generate-post-from-plan skill.

## Prerequisites

- Source material (presentation plan, technical documentation, or project information)
- Access to OLAF framework
- Clear understanding of target audience
- Basic knowledge of content style preferences

## Step-by-Step Instructions

### Step 1: Invoke the Skill
Brief description: Start the blog post generation process

**User Action:**
1. Use the command: `olaf generate-post-from-plan`
2. Prepare your source content (file path or direct text)
3. Decide on writing style preference

**OLAF Response:**
OLAF will request required parameters and begin content analysis

### Step 2: Provide Required Parameters
**User Action:** Respond to OLAF's parameter requests

**Provide Requirements/Parameters:**
- **source_content**: [Example - "presentation-plan-YYYYMMDD-HHmm.md" or direct text paste]
- **style_preference**: [Example - "brochure" for structured approach or "conversational" for narrative style or "all" for both versions]
- **target_audience**: [Example - "Development teams, IT managers, technical professionals"]
- **language**: [Example - "english" (default)]
- **reading_time**: [Example - "Under 2 minutes (300-600 words)" (default)]

### Step 3: Content Analysis and Generation
**What OLAF Does:**
- Analyzes source material for key messages and value propositions
- Selects appropriate template(s) based on style preference
- Generates blog post content following template structure
- Applies domain-specific writing standards
- Creates compelling title, subtitle, and call-to-action

**You Should See:** 
- Progress updates during content analysis
- Style confirmation message
- File generation completion with output locations

### Step 4: Review Generated Content
**User Action:**
1. Navigate to staging directory to review generated blog post(s)
2. Check content quality and accuracy
3. Verify reading time meets target (under 2 minutes)

**File Locations:**
- Single style: `[staging_dir]/blog-post-[style]-YYYYMMDD-HHmm.md`
- Both styles: `[staging_dir]/blog-post-brochure-YYYYMMDD-HHmm.md` and `[staging_dir]/blog-post-conversational-YYYYMMDD-HHmm.md`

## Verification Checklist

✅ **Source content successfully processed and key messages extracted**
✅ **Appropriate writing style template applied consistently**
✅ **Generated content meets word count target (300-600 words)**
✅ **Reading time under 2 minutes achieved**
✅ **Factual accuracy maintained throughout content**
✅ **Clear call-to-action included with actionable next steps**
✅ **Professional tone appropriate for IT/development audience**

## Troubleshooting

**If source content analysis fails:**
```
Verify source file path is correct or ensure direct text input is complete
```

**If template not found:**
- Check template files exist in skill templates directory
- Verify file permissions for template access
- Use manual template specification as alternative

**If generated content is too long:**
- Review source material for key points only
- Request focus on specific aspects of the topic
- Consider breaking into multiple shorter posts

## Key Learning Points

1. **Style Selection Impact:** Brochure style creates structured, feature-focused content while conversational style produces narrative, story-driven posts
2. **Source Quality Matters:** Better source material with clear value propositions results in higher quality blog posts
3. **Audience Awareness:** Tailoring content to specific audience (development teams, IT managers) improves relevance and engagement

## Next Steps to Try

- Experiment with different source materials (presentations, technical specs, project documentation)
- Test both writing styles to understand their distinct approaches
- Use generated posts as starting points for further customization
- Combine with other OLAF skills for comprehensive content creation workflows

## Expected Timeline

- **Total generation time:** 2-4 minutes
- **User input required:** Parameter specification and source content provision
- **OLAF execution time:** Content analysis and generation typically completes within 1-3 minutes

## Style Comparison Guide

### Brochure Style
- **Structure:** Clear sections with descriptive headings
- **Best for:** Feature announcements, product descriptions, technical specifications
- **Format:** Organized bullet points and structured information
- **Tone:** Professional, informative, direct

### Conversational Style  
- **Structure:** Flowing narrative with natural transitions
- **Best for:** Problem-solution stories, team adoption scenarios, change management
- **Format:** Paragraphs with minimal bullet points
- **Tone:** Engaging, relatable, story-driven