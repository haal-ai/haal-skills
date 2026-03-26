# extract-notes-from-skube-site

> Step-by-step tutorial for extracting chapter-by-chapter synthesis notes

## Prerequisites
- Access to the SKube S3J user guide (or target documentation site)
- Understanding of Quarkus baseline concepts (helpful but not required)

## Estimated Time
30–60 minutes (depends on number of chapters)

## Step-by-Step Instructions

### Step 1: Specify the Documentation Source
> "Extract notes from the SKube documentation site"

Provide the site URL or local path to the documentation.

### Step 2: Review Progress Tracker
The skill creates a progress file with all chapters listed as TODO. This enables:
- Resuming interrupted sessions
- Multi-agent coordination
- Clear visibility of completion status

### Step 3: Chapter-by-Chapter Analysis
For each chapter, the skill produces:
- **SKube-specific content** — What SKube adds/changes on top of Quarkus
- **Quarkus-baseline content** — Standard Quarkus behavior
- **SKube-specific synthesis** — Portable takeaways

Progress is tracked as: TODO → WIP → DONE

### Step 4: Review Chapter Notes
Each chapter note is saved individually. Review for:
- Clear separation of SKube vs baseline content
- Accurate technical details
- Useful portable takeaways

### Step 5: Global Synthesis
After all chapters are processed, a global synthesis note consolidates all SKube-specific takeaways into a single aggregated list.

### Step 6: Final Review
Review the complete set:
- Individual chapter notes
- Global synthesis
- Progress tracker (all DONE)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Site not accessible | Verify URL and network access |
| Chapter missed | Check progress tracker and re-run for that chapter |
| Wrong baseline classification | Review Quarkus docs to verify classification |
| Interrupted session | Resume — progress tracker maintains state |

## Verification Checklist
- [ ] All chapters processed (progress tracker shows all DONE)
- [ ] Each chapter has SKube vs baseline separation
- [ ] SKube-specific synthesis included per chapter
- [ ] Global synthesis consolidates all takeaways
- [ ] Notes are accurate and useful
