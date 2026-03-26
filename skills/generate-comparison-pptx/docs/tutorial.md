# generate-comparison-pptx

> Step-by-step tutorial for generating comparison presentations

## Prerequisites
- Python 3.9+ installed
- `python-pptx` package (`pip install python-pptx`)
- Comparison data (items + metrics/scores)

## Estimated Time
10–20 minutes

## Step-by-Step Instructions

### Step 1: Prepare Your Data
Gather the items and metrics you want to compare. Examples:
- Three LLM models with benchmark scores
- Five CI/CD tools with feature matrices
- Project approaches with cost/time/risk ratings

### Step 2: Invoke the Skill
> "Create a comparison presentation of Claude, GPT-4, and Gemini using these benchmarks"

Provide the data inline or point to a file containing comparison results.

### Step 3: Review Slide Plan
The skill proposes a slide structure:
- Title slide with comparison overview
- 2-6 content slides with charts and cards
- Sources slide (if data has references)

### Step 4: Generate and Run
A Python script is created and executed:
```bash
cd .olaf/work/presentations/<name>/
python generate_pptx.py
```

### Step 5: Open and Verify
```bash
Start-Process ".olaf/work/presentations/<name>/<name>.pptx"
```

Check:
- Charts accurately represent the data
- Color coding is consistent across slides
- Legend labels are correct
- Key insights are highlighted

### Step 6: Customize (Optional)
Switch PowerPoint themes (Design tab) — all colors adapt automatically.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Charts look wrong | Verify data values in the Python script DATA section |
| Missing items in comparison | Ensure all items were provided in the prompt |
| Colors hard to distinguish | Theme uses accent slots — try a different PowerPoint theme |
| Script error | Check `python-pptx` is installed and `template.pptx` is present |

## Verification Checklist
- [ ] All comparison items represented
- [ ] Metrics/scores accurately reflected
- [ ] Charts readable and correctly labeled
- [ ] Consistent color coding across slides
- [ ] Key insights highlighted
- [ ] PPTX opens and edits correctly in PowerPoint
