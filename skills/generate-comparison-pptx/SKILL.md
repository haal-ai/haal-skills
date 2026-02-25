---
name: generate-comparison-pptx
description: >
  Generate a professional PowerPoint presentation comparing multiple items
  (models, tools, products, approaches) using charts and visual cards.
  Use when the user asks to create a comparison presentation, a PPTX deck,
  or wants to visualize benchmark/evaluation results as slides.
  Supports any comparison data — not limited to LLM models.
license: MIT
compatibility: Requires Python 3.9+ and python-pptx package
metadata:
  author: olaf
  version: "1.0.0"
  tags: "pptx presentation comparison charts visualization"
---

# Generate Comparison PPTX

## When to use this skill

Trigger phrases:
- "create a comparison presentation"
- "generate a PPTX comparing..."
- "make slides for my benchmark results"
- "build a deck showing the differences between..."
- "PowerPoint presentation comparing..."
- "visualize these results as a presentation"

## Overview

This skill generates a professional, dark-themed PowerPoint presentation
with charts and visual cards to compare multiple items across dimensions.
It uses `python-pptx` to create native PPTX files with embedded charts
(not images), so everything is editable in PowerPoint.

IMPORTANT: This "skill" is a **process/spec** that guides an agent (LLM) to:

- decide the slide set (count + structure)
- generate a dedicated `generate_pptx.py` for that comparison
- run it to produce a `.pptx`

The bundled `scripts/generate_pptx.py` is a **starter template** and must remain generic.

## Prerequisites

Ensure `python-pptx` is installed:
```bash
pip install python-pptx
```

## Process

### Step 1 — Gather comparison data

Collect from the user or from available files:

1. **Items to compare** — 2 to 8 items (e.g., models, tools, products)
2. **Dimensions/metrics** — numeric scores or categories for each item
   (e.g., cost, speed, quality scores, feature counts)
3. **Key findings** — notable differences, strengths, weaknesses
4. **Recommendation** — which item for which use case

If the user has a markdown comparison file, read it and extract the data.
If the user provides raw data, structure it yourself.

### Step 2 — Generate the Python script

Create a Python script using the template at
[scripts/generate_pptx.py](scripts/generate_pptx.py) as a reference.

IMPORTANT: The files under this skill folder are **templates**. They are **read-only**.
Do **NOT** edit or run:

- `c:\Users\ppaccaud\.agents\skills\generate-comparison-pptx\scripts\generate_pptx.py`
- `c:\Users\ppaccaud\.agents\skills\generate-comparison-pptx\scripts\template.pptx`

Instead, always generate a new presentation folder in the **repo workspace**:

```
<repo>/.olaf/work/presentations/<presentation-name>/
  generate_pptx.py
  template.pptx
  <presentation-name>.pptx
```

The bundled `generate_pptx.py` includes a runtime guard and will refuse to run unless it is located under `.olaf/work/presentations/<presentation-name>/`.

Adapt the script to the user's specific data:

1. **Update the data constants** at the top of the script with the actual
   items, metrics, colors, and findings
2. **Choose appropriate chart types**:
   - Bar charts for cost, duration, token counts (single metric per item)
   - Grouped bar charts for multi-dimension scoring (e.g., quality dimensions)
   - Stacked bars for found/missed, pass/fail breakdowns
3. **Customize the slide structure** (see Slide Architecture below)
4. **Set the output path** to the user's preferred location

### Step 3 — Run the script

```bash
python <path-to-script>
```

The script must be executed from:

```
<repo>/.olaf/work/presentations/<presentation-name>/generate_pptx.py
```

By convention (and by default in the template), the PPTX output is:

```
<repo>/.olaf/work/presentations/<presentation-name>/<presentation-name>.pptx
```

Then open the generated PPTX:
```bash
# Windows
Start-Process "<path-to-pptx>"
# macOS
open "<path-to-pptx>"
# Linux
xdg-open "<path-to-pptx>"
```

## Slide Architecture

The presentation should follow this structure (5 content slides + title):

| Slide | Purpose | Visual Elements |
|-------|---------|-----------------|
| Title | Intent, data source, AI-generated note, item badges | Colored rounded rectangles per item |
| Slide 1 | Executive Summary / Recommendation | 2-3 tier recommendation cards with bullets |
| Slide 2 | Cost & Performance | Two side-by-side bar charts |
| Slide 3 | Quality/Scoring | Grouped bar chart (all dimensions × all items) |
| Slide 4 | Key Findings | Stacked bar + callout cards for notable findings |
| Slide 5 | Depth/Detail | Bar chart + profile cards per item |

The conclusion/executive summary is always the FIRST content slide so the
audience gets the recommendation upfront, then supporting data follows.

Adapt slide count based on data richness — do NOT always use all 5 slides.

**Slide count decision rules:**

- **3 slides** (minimum): 2-3 items, 1-2 metrics, no detection/depth data.
  Use: Executive Summary + Cost/Performance + Quality Scores.
- **4 slides**: 3-5 items, multiple metrics but no detection breakdown.
  Drop the Depth/Detail slide.
- **5 slides** (full): 4+ items, multi-dimension scoring, detection data,
  and depth metrics. This is the template default.
- **6-7 slides**: 6+ items or 8+ dimensions. Split Quality Scores across
  two slides (max 5-6 grouped bars per chart for readability), or add a
  dedicated slide for a secondary metric pair.
- **8 slides** (maximum): Only for very data-rich comparisons. Beyond 8,
  the presentation loses focus.

**Readability rules:**
- Max 5-7 data points per single chart (bars become too thin beyond that)
- Max 5 series in a grouped bar chart (colors become hard to distinguish)
- If a chart would have more, split into two slides or use a different
  chart type (e.g., table instead of grouped bars for 8+ items)
- One key idea per slide — if you're cramming two stories, split
- Insight boxes should be one sentence, not paragraphs

The Executive Summary slide is always present regardless of slide count.

## Design System — Theme-Aware

All colors use PowerPoint theme slots (`MSO_THEME_COLOR`) instead of
hardcoded RGB values. This means the user can switch the theme in
PowerPoint (Design tab → Themes) and all colors adapt automatically,
making it easy to match any company's branding.

```python
from pptx.enum.dml import MSO_THEME_COLOR

# Semantic mapping:
# Slide background     → DARK_1
# Card background      → DARK_1 with brightness +0.15
# Primary text         → LIGHT_1
# Body text            → LIGHT_1 with brightness -0.25
# Subtitle/muted text  → LIGHT_2
# Item colors          → ACCENT_1 through ACCENT_6 (one per item)
# Insight box bg       → ACCENT_1 with brightness -0.7

# For charts, use XML-level schemeClr to get theme-aware data points:
_set_chart_point_theme_color(point, "accent1")
_set_series_theme_color(series, "accent2")
```

Key design rules:
- Widescreen 16:9 (13.333 × 7.5 inches)
- Font: Segoe UI (falls back gracefully)
- Title: 28pt LIGHT_1 bold, top-left
- Subtitle: 14pt LIGHT_2, below title
- Body text: 14pt minimum where possible (avoid going below 11pt)
- Charts: colored per item using theme accents, data labels on, LIGHT_1 text
- Cards: rounded rectangles with accent top border
- Insight boxes: dark tinted rectangles (accent with -0.7 brightness)
- Executive summary / recommendation is always the FIRST content slide
- Title slide must include: intent, data source, and "AI-generated" notice

CRITICAL: Never use `RGBColor(...)` for slide content. Always use
`_apply_theme_color(color_format, MSO_THEME_COLOR.XXX, brightness)`
for shapes and text, and `_set_chart_point_theme_color()` /
`_set_series_theme_color()` for chart elements. This ensures all
colors follow the theme when the user switches it.

## Helper Functions

The reference script provides these reusable helpers:

- `set_slide_bg(slide)` — set background to theme's DARK_1
- `add_text_box(slide, left, top, width, height, text, ...)` — positioned text; theme_color=None means inherit
- `add_rounded_rect(slide, left, top, width, height, fill_theme, ...)` — badge/card; fc_theme=None means inherit
- `add_card(slide, left, top, width, height, title, lines, accent_theme)` — info card with accent bar
- `_apply_theme_color(color_format, theme_color, brightness)` — apply theme color to any element
- `_set_chart_point_theme_color(point, scheme_clr_name)` — theme color on chart data points
- `_set_series_theme_color(series, scheme_clr_name)` — theme color on chart series

See [scripts/generate_pptx.py](scripts/generate_pptx.py) for the full
implementation of these helpers.

## Text Grouping Rule

When multiple text lines belong together (e.g., bullet points in a card,
recommendation bullets, profile descriptions), they MUST be rendered as
paragraphs within a single text frame — NOT as separate `add_text_box()`
calls. This produces one editable text block in PowerPoint instead of
many independent floating text fields.

Pattern to follow:
```python
body_box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
tf = body_box.text_frame
tf.word_wrap = True
for i, line in enumerate(lines):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.text = line
    p.font.size = Pt(14)
    # Don't set font color — let it inherit from the theme
    p.font.name = "Segoe UI"
    p.space_after = Pt(4)
```

Use separate `add_text_box()` only for truly independent text elements
(titles, subtitles, insight boxes) that are positioned in different areas
of the slide.

## Theme Color Inheritance Rule

To ensure presentations adapt when the user switches the PowerPoint theme
(Design tab), text and shape colors follow this rule:

- `None` / omit the color parameter = **inherit from theme** (auto-adapts
  to light or dark backgrounds). Use this for all body text, subtitles,
  axis labels, data labels, chart tick labels, and any text that should
  be readable on any background.
- Explicit `MSO_THEME_COLOR.ACCENT_*` = use only on **accent-colored
  elements**: card title text, text inside colored shapes, insight box
  text, item badges. These are intentionally colored and should stay
  colored regardless of theme.

Never set `LIGHT_1` or `LIGHT_2` explicitly on text — these are white/gray
in dark themes but invisible on white backgrounds. Let PowerPoint handle
the text color through theme inheritance.

## Example: Adapting for a different comparison

If the user wants to compare CI/CD tools instead of LLM models:

```python
from pptx.enum.dml import MSO_THEME_COLOR

# Items
items = ["GitHub Actions", "GitLab CI", "Jenkins", "CircleCI"]
# Colors auto-assigned from ACCENT_1..ACCENT_4

# Metrics
costs = [0, 19, 0, 30]  # $/month
build_times = [3.2, 2.8, 5.1, 2.5]  # minutes
plugin_counts = [15000, 800, 1800, 300]

# Scoring dimensions
dimensions = ["Ease of Setup", "Scalability", "Plugin Ecosystem", "Cost", "Documentation"]
scores = {
    "GitHub Actions": [9, 8, 9, 9, 8],
    "GitLab CI":      [7, 9, 6, 7, 7],
    "Jenkins":        [4, 7, 10, 10, 6],
    "CircleCI":       [8, 7, 5, 6, 7],
}
```

The slide structure stays the same — just swap the data and labels.

## Sources & References Slide

If the source data contains URLs or citations, extract them into the
`SOURCES` list in the generated script:

```python
SOURCES = [
    ("Original benchmark report", "https://example.com/benchmark"),
    ("Tool documentation", "https://example.com/docs"),
]
```

A "Sources & References" slide is auto-generated at the end with clickable
hyperlinks. Each source shows the label as a blue underlined link, followed
by the URL in muted text. If `SOURCES` is empty, the slide is skipped.

## Template Support

The script supports an optional `.pptx` template file:

```python
TEMPLATE_PATH = Path("path/to/company-template.pptx")
```

If provided, the presentation inherits the template's theme, slide master,
and color scheme. Companies can provide a branded template and all generated
content adapts to their theme colors.

If `TEMPLATE_PATH` is None or the file doesn't exist, a blank presentation
is used (with the default PowerPoint theme).

A template is included at `scripts/template.pptx` — the presentation
inherits its theme, slide master, and color scheme.

The template must provide at least these two layouts:

- **Cover slide**: layout named like `Cover slide` (cover/title slide)
- **Title only**: layout named like `Title only` (used for all non-cover slides)

If `Title only` is missing, the generator script fails fast with a clear error.

## Document Properties

The script sets PowerPoint document properties (File → Info):
- Title: from the `TITLE` constant
- Subject: from the `SUBTITLE` constant
- Comments: skill attribution

## Output

The skill produces:
1. A Python script (saved alongside the output PPTX for reproducibility)
2. A `.pptx` file ready to present

The PPTX contains native PowerPoint charts (editable) and shapes (editable),
not screenshots or images. The user can customize colors, text, and data
directly in PowerPoint after generation.
