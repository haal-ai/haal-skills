# distill-docs-to-pptx

> Step-by-step tutorial for distilling documentation into PowerPoint slides

## Prerequisites
- Python 3.9+ installed
- `python-pptx` package (`pip install python-pptx`)
- One or more markdown documentation files to distill

## Estimated Time
10–20 minutes (depending on documentation size)

## Step-by-Step Instructions

### Step 1: Identify Source Documentation
Point the skill to your markdown files:
> "Distill docs/architecture.md into a presentation"

Multiple files can be combined:
> "Create slides from docs/architecture.md and docs/design-decisions.md"

### Step 2: Review the Slide Plan
The skill analyzes your documentation and proposes a slide structure:
- Source < 200 lines → 3-4 content slides
- Source 200-500 lines → 4-5 content slides
- Source 500-1000 lines → 5-6 content slides
- Source 1000+ lines → 6-8 content slides

Review the proposed structure and request adjustments if needed.

### Step 3: Generate the Python Script
A self-contained `generate_pptx.py` is created in `.olaf/work/presentations/<name>/` with:
- All helper functions inlined
- Template file copied alongside
- Slide content extracted from your docs

### Step 4: Run the Script
```bash
cd .olaf/work/presentations/<name>/
python generate_pptx.py
```

### Step 5: Open and Review
```bash
# Windows
Start-Process ".olaf/work/presentations/<name>/<name>.pptx"
```

Check that:
- Title slide has intent, source reference, and AI-generated notice
- Each content slide has one clear idea
- Insight boxes provide takeaways
- Sources slide has clickable links (if applicable)

### Step 6: Customize Theme (Optional)
Open in PowerPoint → Design tab → switch themes. All colors adapt automatically since they use theme slots.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: python-pptx` | Run `pip install python-pptx` |
| Slides look blank/white | Ensure `template.pptx` was copied to the output folder |
| Layout error on generation | Check that template has "Title Only" layout |
| Too many bullets on a slide | Ask the skill to split dense slides |

## Verification Checklist
- [ ] Python script generated in `.olaf/work/presentations/` folder
- [ ] `template.pptx` copied alongside the script
- [ ] Script runs without errors
- [ ] PPTX opens correctly in PowerPoint
- [ ] Each slide has one clear idea with visual hierarchy
- [ ] Insight boxes present on data-heavy slides
- [ ] Sources slide included (if source docs had URLs)
