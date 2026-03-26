# create-presentation-and-posts-workflow

> Step-by-step tutorial for generating a full content package

## Prerequisites
- A clear topic and target audience
- Understanding of presentation type (reading-only vs live)
- PowerPoint-compatible viewer for output review

## Estimated Time
15–25 minutes (depending on topic complexity and review cycles)

## Step-by-Step Instructions

### Step 1: Define Your Topic
Provide the subject and target audience. Be specific about what angle you want to cover.

**Example prompt:**
> "Create a presentation and blog posts about microservices observability for platform engineering teams"

### Step 2: Choose Presentation Type
- **reading-only**: Self-contained slides with detailed notes
- **live**: Optimized for live delivery, specify duration (e.g., "30 minutes")

### Step 3: Select Language and Post Style
Specify language (default: English) and blog post style:
- **brochure**: Formal, marketing-oriented
- **conversational**: Informal, technical blog
- **all**: Both styles generated

### Step 4: Review Presentation Plan
The skill produces a markdown slide plan first. Review it for:
- Logical flow and structure
- Coverage of key points
- Appropriate depth for audience

Approve the plan or request changes before proceeding.

### Step 5: Generate PowerPoint
Once the plan is approved, the PowerPoint file is generated. Open the .pptx to verify:
- Slide layout and formatting
- Content accuracy
- Visual consistency

### Step 6: Generate Blog Posts
Blog posts are generated from the same content. Review for:
- Tone matching the selected style
- Appropriate length and depth
- Correct language

### Step 7: Collect Outputs
All files are saved in the output directory:
- `presentation-plan.md`
- `presentation.pptx`
- Blog post file(s)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| PowerPoint formatting issues | Check that python-pptx dependencies are available |
| Blog post tone is wrong | Re-run with explicit post_style parameter |
| Missing content in slides | Improve the topic description with more detail |

## Verification Checklist
- [ ] Presentation plan reviewed and approved
- [ ] PowerPoint opens correctly and slides are well-formatted
- [ ] Blog post(s) match requested style and language
- [ ] All outputs saved in expected location
