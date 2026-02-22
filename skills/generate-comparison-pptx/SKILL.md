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

Create a Python script using the helper functions and design system
documented below (in the "Reference Script" section). Do NOT reference
any external file — all helpers are inlined in this skill document.

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

All helpers are documented in the "Reference Script" section below.

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

A template is bundled with this skill at `scripts/template.pptx` (relative
to the skill folder). When generating the Python script, set `TEMPLATE_PATH`
to resolve relative to the generated script's location, or to `None` if
the template is not available. The script should gracefully fall back to
a blank presentation if the template file is not found.

## Document Properties

The script sets PowerPoint document properties (File → Info):
- Title: from the `TITLE` constant
- Subject: from the `SUBTITLE` constant
- Comments: skill attribution

## Output Location

Both output files (the generator script and the PPTX) MUST be saved under:

```
.olaf/work/presentations/<presentation-name>/
```

The `<presentation-name>` folder is derived from the context — typically
the comparison topic, in kebab-case.

Examples:
- Comparing 5 models → save to
  `.olaf/work/presentations/5-model-comparison/generate_pptx.py` and
  `.olaf/work/presentations/5-model-comparison/5-model-comparison.pptx`
- Comparing CI/CD tools → save to
  `.olaf/work/presentations/cicd-tools-comparison/generate_pptx.py` and
  `.olaf/work/presentations/cicd-tools-comparison/cicd-tools-comparison.pptx`

If the user explicitly requests a different location, use that instead.

Naming convention:
- Script: `generate_pptx.py` (inside the presentation folder)
- PPTX: `<presentation-name>.pptx`

## Output

The skill produces:
1. A Python script (saved alongside the source data for reproducibility)
2. A `.pptx` file ready to present

The PPTX contains native PowerPoint charts (editable) and shapes (editable),
not screenshots or images. The user can customize colors, text, and data
directly in PowerPoint after generation.


## Reference Script — Complete Helper Library

The following is the complete reference implementation. When generating a
script for the user, copy the helpers you need and replace the DATA SECTION
with the actual comparison data. The script must be fully self-contained —
no imports from external skill files.

```python
#!/usr/bin/env python3
"""
Comparison PPTX Generator
==========================
Generates a professional PowerPoint presentation comparing multiple items
across dimensions with native editable charts.

THEME-AWARE: All colors use PowerPoint theme slots so the user can switch
the theme in PowerPoint and all colors adapt automatically.

Requirements: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.chart.data import CategoryChartData
from pptx.oxml.ns import qn
from pathlib import Path


# ── Theme accent slots for items (up to 8) ──
ACCENT_SLOTS = [
    MSO_THEME_COLOR.ACCENT_1, MSO_THEME_COLOR.ACCENT_2,
    MSO_THEME_COLOR.ACCENT_3, MSO_THEME_COLOR.ACCENT_4,
    MSO_THEME_COLOR.ACCENT_5, MSO_THEME_COLOR.ACCENT_6,
]
ACCENT_SLOTS_EXTENDED = ACCENT_SLOTS + [
    (MSO_THEME_COLOR.ACCENT_1, 0.4),
    (MSO_THEME_COLOR.ACCENT_2, 0.4),
]
SCHEME_CLR_NAMES = ["accent1", "accent2", "accent3", "accent4", "accent5", "accent6"]


# ── Helpers ──

def _apply_theme_color(color_format, theme_color, brightness=0.0):
    """Apply a theme color with optional brightness adjustment."""
    color_format.theme_color = theme_color
    if brightness != 0.0:
        color_format.brightness = brightness


def _get_item_accent(index):
    """Get (theme_color, brightness) for item at given index."""
    entry = ACCENT_SLOTS_EXTENDED[index % len(ACCENT_SLOTS_EXTENDED)]
    if isinstance(entry, tuple):
        return entry
    return (entry, 0.0)


def set_slide_bg(slide):
    """No-op: let the slide inherit its background from the slide master/layout."""
    pass


def add_text_box(slide, left, top, width, height, text,
                 font_size=14, theme_color=MSO_THEME_COLOR.LIGHT_1,
                 brightness=0.0, bold=False,
                 alignment=PP_ALIGN.LEFT, font_name="Segoe UI"):
    """Add a positioned text box."""
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    if theme_color is not None:
        _apply_theme_color(p.font.color, theme_color, brightness)
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_rounded_rect(slide, left, top, width, height,
                     fill_theme, fill_brightness=0.0,
                     text="", font_size=12,
                     fc_theme=MSO_THEME_COLOR.LIGHT_1, fc_brightness=0.0,
                     bold=False):
    """Add a rounded rectangle."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    _apply_theme_color(shape.fill.fore_color, fill_theme, fill_brightness)
    shape.line.fill.background()
    if text:
        tf = shape.text_frame
        tf.word_wrap = True
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(font_size)
        if fc_theme is not None:
            _apply_theme_color(p.font.color, fc_theme, fc_brightness)
        p.font.bold = bold
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape


def add_card(slide, left, top, width, height, title, lines,
             accent_theme, title_size=14, body_size=11):
    """Add an info card with accent top border and bullet lines."""
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.background()
    card.line.width = Pt(1.5)
    _apply_theme_color(card.line.color, accent_theme)
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left + 0.05), Inches(top + 0.05),
        Inches(width - 0.1), Inches(0.06))
    bar.fill.solid()
    _apply_theme_color(bar.fill.fore_color, accent_theme)
    bar.line.fill.background()
    add_text_box(slide, left + 0.15, top + 0.15, width - 0.3, 0.35,
                 title, font_size=title_size, theme_color=accent_theme, bold=True)
    body_box = slide.shapes.add_textbox(
        Inches(left + 0.15), Inches(top + 0.55),
        Inches(width - 0.3), Inches(height - 0.7))
    tf = body_box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(body_size)
        _apply_theme_color(p.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        p.font.name = "Segoe UI"
        p.space_after = Pt(4)
    return card


def add_slide_header(slide, title, subtitle=""):
    """Add standard title + subtitle to a slide."""
    set_slide_bg(slide)
    add_text_box(slide, 0.5, 0.3, 12, 0.6, title, font_size=28, bold=True)
    if subtitle:
        add_text_box(slide, 0.5, 0.85, 12, 0.4, subtitle, font_size=14)


# ── Chart helpers (XML-level theme colors) ──

def _get_solid_fill_element(fill_obj):
    """Get the XML solidFill element, handling different python-pptx internals."""
    sf = fill_obj._fill
    if hasattr(sf, 'tag'):
        return sf
    if hasattr(sf, '_solidFill'):
        return sf._solidFill
    if hasattr(sf, '_element'):
        return sf._element
    return sf


def _set_chart_point_theme_color(point, scheme_clr_name, brightness=0.0):
    """Set a chart data point's fill to a theme color via XML."""
    fill = point.format.fill
    fill.solid()
    solid_fill = _get_solid_fill_element(fill)
    for child in list(solid_fill):
        if child.tag.endswith(('srgbClr', 'schemeClr', 'sysClr')):
            solid_fill.remove(child)
    scheme_clr = solid_fill.makeelement(qn('a:schemeClr'), {'val': scheme_clr_name})
    if brightness != 0.0:
        if brightness > 0:
            mod = scheme_clr.makeelement(qn('a:lumMod'),
                                          {'val': str(int((1 - brightness) * 100000))})
            off = scheme_clr.makeelement(qn('a:lumOff'),
                                          {'val': str(int(brightness * 100000))})
            scheme_clr.append(mod)
            scheme_clr.append(off)
        else:
            mod = scheme_clr.makeelement(qn('a:lumMod'),
                                          {'val': str(int((1 + brightness) * 100000))})
            scheme_clr.append(mod)
    solid_fill.append(scheme_clr)


def _set_series_theme_color(series, scheme_clr_name, brightness=0.0):
    """Set an entire chart series fill to a theme color via XML."""
    fill = series.format.fill
    fill.solid()
    solid_fill = _get_solid_fill_element(fill)
    for child in list(solid_fill):
        if child.tag.endswith(('srgbClr', 'schemeClr', 'sysClr')):
            solid_fill.remove(child)
    scheme_clr = solid_fill.makeelement(qn('a:schemeClr'), {'val': scheme_clr_name})
    if brightness != 0.0:
        if brightness > 0:
            mod = scheme_clr.makeelement(qn('a:lumMod'),
                                          {'val': str(int((1 - brightness) * 100000))})
            off = scheme_clr.makeelement(qn('a:lumOff'),
                                          {'val': str(int(brightness * 100000))})
            scheme_clr.append(mod)
            scheme_clr.append(off)
        else:
            mod = scheme_clr.makeelement(qn('a:lumMod'),
                                          {'val': str(int((1 + brightness) * 100000))})
            scheme_clr.append(mod)
    solid_fill.append(scheme_clr)


def _get_scheme_clr_name(item_index):
    """Get the XML scheme color name for an item index."""
    if item_index < len(SCHEME_CLR_NAMES):
        return SCHEME_CLR_NAMES[item_index]
    return SCHEME_CLR_NAMES[item_index % len(SCHEME_CLR_NAMES)]


def _get_item_brightness(item_index):
    """Get brightness adjustment for items beyond the 6 native accents."""
    if item_index < len(SCHEME_CLR_NAMES):
        return 0.0
    return 0.4


def style_bar_chart(chart, num_items, data_label_format='#,##0',
                    axis_label=None, max_scale=None):
    """Apply consistent theme-aware styling to a single-series bar chart."""
    chart.has_legend = False
    chart.style = 2
    plot = chart.plots[0]
    plot.gap_width = 80
    series = plot.series[0]
    for i in range(num_items):
        pt = series.points[i]
        _set_chart_point_theme_color(
            pt, _get_scheme_clr_name(i), _get_item_brightness(i))
    series.data_labels.show_value = True
    series.data_labels.font.size = Pt(12)
    _apply_theme_color(series.data_labels.font.color, MSO_THEME_COLOR.LIGHT_1)
    series.data_labels.font.bold = True
    series.data_labels.number_format = data_label_format
    chart.category_axis.tick_labels.font.size = Pt(10)
    _apply_theme_color(chart.category_axis.tick_labels.font.color,
                       MSO_THEME_COLOR.LIGHT_1, -0.25)
    chart.value_axis.tick_labels.font.size = Pt(9)
    _apply_theme_color(chart.value_axis.tick_labels.font.color,
                       MSO_THEME_COLOR.LIGHT_1, -0.4)
    if axis_label:
        chart.value_axis.has_title = True
        ax_title = chart.value_axis.axis_title.text_frame.paragraphs[0]
        ax_title.text = axis_label
        ax_title.font.size = Pt(10)
        _apply_theme_color(ax_title.font.color, MSO_THEME_COLOR.LIGHT_1, -0.4)
    if max_scale is not None:
        chart.value_axis.maximum_scale = max_scale


def build_sources_slide(prs, sources):
    """Final slide: Sources & References with clickable hyperlinks."""
    if not sources:
        return
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_slide_header(slide, "Sources & References")
    body = slide.shapes.add_textbox(
        Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, (label, url) in enumerate(sources):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        run_bullet = p.add_run()
        run_bullet.text = "• "
        run_bullet.font.size = Pt(14)
        _apply_theme_color(run_bullet.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        run_bullet.font.name = "Segoe UI"
        run_link = p.add_run()
        run_link.text = label
        run_link.font.size = Pt(14)
        run_link.font.name = "Segoe UI"
        _apply_theme_color(run_link.font.color, MSO_THEME_COLOR.HYPERLINK)
        run_link.font.underline = True
        run_link.hyperlink.address = url
        run_url = p.add_run()
        run_url.text = f"  ({url})"
        run_url.font.size = Pt(10)
        run_url.font.name = "Segoe UI"
        _apply_theme_color(run_url.font.color, MSO_THEME_COLOR.LIGHT_2)


# ── DATA SECTION — replace with your comparison data ──

TITLE = "Item Comparison"
SUBTITLE = "N Items  •  Same Conditions"
ITEMS = ["Item A", "Item B", "Item C"]
SOURCES = []
TEMPLATE_PATH = None  # Set to Path("path/to/template.pptx") if available
OUTPUT_PATH = Path("comparison.pptx")


# ── MAIN ──

def main():
    if TEMPLATE_PATH and Path(TEMPLATE_PATH).exists():
        prs = Presentation(str(TEMPLATE_PATH))
    else:
        prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Build slides here using the helpers above
    # build_title_slide(prs)
    # build_recommendation_slide(prs)
    # build_cost_performance_slide(prs)
    # ...
    # build_sources_slide(prs, SOURCES)

    prs.core_properties.title = TITLE
    prs.core_properties.subject = SUBTITLE
    prs.core_properties.comments = "Generated by generate-comparison-pptx skill"
    prs.save(str(OUTPUT_PATH))
    print(f"✅ Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
```
