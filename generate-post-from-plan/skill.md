---
name: generate-post-from-plan
description: Generate engaging blog posts from presentation content or technical documentation with choice of brochure or conversational styles
license: Apache-2.0
metadata:
  olaf_tags: [technical-writing, content-creation, blog-post, documentation, presentation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **source_content**: file_path|text - Source material (presentation plan, technical documentation, or project information) (REQUIRED)
- **style_preference**: brochure|conversational|all - Writing style preference (REQUIRED)
- **target_audience**: string - Specific audience (default: "Development teams, IT managers, technical professionals") (OPTIONAL)
- **language**: english|french|spanish|german - Target language (default: "english") (OPTIONAL)
- **reading_time**: string - Target reading time (default: "Under 2 minutes (300-600 words)") (OPTIONAL)

## User Interaction Protocol
Following the "Act" protocol - execute directly without requiring user approval for routine content generation operations.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm source content is provided and accessible
- Validate style preference is specified (brochure, conversational, or all)
- Check template availability for chosen style(s)
- Ensure output directory is accessible

### 2. Execution Phase
You WILL execute these operations:

**Content Analysis**:
- Read and analyze source material thoroughly
- Identify key messages and value propositions
- Determine audience needs and requirements
- Extract factual information only

**Style Selection and Generation**:
- **If "brochure" requested**: Use structured template `templates/blog-post-brochure-template.md`
- **If "conversational" requested**: Use narrative template `templates/blog-post-conversational-template.md`
- **If "all" requested**: Generate both versions using respective templates

**Content Creation**:
- Create compelling title and subtitle in target language
- Structure content according to chosen style(s)
- Ensure readability and engagement (max 20 words per sentence)
- Include practical call-to-action

### 3. Validation Phase
You WILL confirm successful completion:
- Verify factual accuracy of generated content
- Check reading time meets target (under 2 minutes)
- Ensure style consistency throughout
- Validate call-to-action clarity and actionability

## Output Format
Generated blog posts will include:
- **Structure**: Title, subtitle, reading time, audience, keywords, content, call-to-action
- **Format**: Markdown format following template structure
- **File naming**:
  - Single style: `blog-post-[style]-YYYYMMDD-HHmm.md`
  - Both styles: `blog-post-brochure-YYYYMMDD-HHmm.md` and `blog-post-conversational-YYYYMMDD-HHmm.md`
- **Location**: `.olaf/work/staging/blog-post-[style]-YYYYMMDD-HHmm.md`

## User Communication
Communication patterns:
- **Progress updates**: Inform user of content analysis completion and generation start
- **Style confirmation**: Confirm which style(s) are being generated
- **Completion notification**: Report successful generation with file locations
- **Quality metrics**: Report word count and estimated reading time

## Domain-Specific Rules
Technical writing standards:
- **Accuracy**: Stick strictly to documented features and capabilities
- **Clarity**: Use short sentences (max 20 words), clear paragraphs
- **Authenticity**: No fictional testimonials or invented statistics
- **Value focus**: Emphasize reader benefits and practical applications
- **Professional tone**: Maintain appropriate voice for IT/development audience

## Success Criteria
Measurable success outcomes:
- [ ] Source content successfully analyzed and processed
- [ ] Appropriate template(s) selected based on style preference
- [ ] Blog post(s) generated with compelling titles and clear structure
- [ ] Content meets word count target (300-600 words)
- [ ] Reading time under 2 minutes achieved
- [ ] Factual accuracy verified throughout content
- [ ] Clear call-to-action included
- [ ] Files saved with proper naming convention

## Error Handling
Error scenarios and responses:
- **Missing source content**: Request specific source material or file path
- **Invalid style preference**: Present valid options (brochure, conversational, all)
- **Template access issues**: Report missing templates and suggest manual specification
- **Content generation failures**: Analyze source material limitations and suggest alternatives
- **File creation errors**: Check permissions and suggest alternative output locations

## Templates
Style-specific templates for consistent output:
- **Brochure Style**: `templates/blog-post-brochure-template.md`
- **Conversational Style**: `templates/blog-post-conversational-template.md`

## Notes
Implementation details:
- **Dependencies**: Access to template files in skill templates directory
- **Performance**: Content generation typically takes 1-3 minutes depending on source complexity
- **Limitations**: Quality depends on source material quality and completeness
- **Language support**: Currently supports English, French, Spanish, and German output
