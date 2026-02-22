---
name: distill-docs-to-pptx
description: >
  Distill large or multiple markdown documentation files into a concise,
  professional PowerPoint presentation. Use when the user wants to present
  complex technical documentation without forcing the audience to read
  hundreds of lines of markdown. Not a comparison — a distillation.
license: MIT
compatibility: Requires Python 3.9+ and python-pptx package
metadata:
  author: olaf
  version: "1.0.0"
  tags: "pptx presentation documentation distill summarize slides"
---

# Distill Documentation to PPTX

## When to use this skill

Trigger phrases:
- "create a presentation from this documentation"
- "distill these docs into slides"
- "make a deck explaining this architecture"
- "summarize this design doc as a presentation"
- "I need slides to present this to the team"
- "turn this markdown into a PowerPoint"
- "people won't read all this — make slides"

## When NOT to use this skill

- If the user wants to compare items with numeric metrics, use
  `generate-comparison-pptx` instead.
- If the user wants a written summary (not slides), just summarize directly.

## Overview

This skill reads one or more markdown documentation files, extracts the
key concepts, and generates a professional dark-themed PPTX presentation
that communicates the essential information in 4-8 slides. The goal is
to save the audience from reading 200-800 lines of markdown while
retaining the critical content.

## Prerequisites

```bash
pip install python-pptx
```

## Process

### Step 1 — Read and analyze the source documentation

Read all the markdown files the user points to. As you read, identify:

1. **Core purpose** — what is this thing and why does it exist?
2. **Key concepts** — the 3-6 most important ideas (architecture decisions,
   design patterns, workflows, components)
3. **Visual structures** — anything that maps well to diagrams, flows,
   grids, or cards (pipelines, phase lists, component inventories,
   decision trees)
4. **Numbers and facts** — concrete data points worth highlighting
   (counts, caps, limits, performance figures)
5. **Design principles** — recurring themes or explicit principles

### Step 2 — Plan the slide structure

Decide how many slides based on content density:

| Source size | Recommended slides | Rationale |
|-------------|-------------------|-----------|
| < 200 lines | 3-4 content slides | Light content, keep it tight |
| 200-500 lines | 4-5 content slides | Standard treatment |
| 500-1000 lines | 5-6 content slides | Rich content, needs space |
| 1000+ lines or multiple files | 6-8 content slides | Complex system, max density |

Always include (not counted above):
- Title slide (with intent, data source, AI-generated notice)

The first content slide should always be an **Executive Summary** that
gives the audience the key takeaway upfront.

**Slide type selection guide:**

| Content type | Best slide format |
|-------------|-------------------|
| Overview / what & why | 2-3 cards side by side (problem / solution / output) |
| Pipeline / workflow | Numbered phase boxes with arrows + detail cards below |
| Component inventory | Grid layout (3-4 columns × N rows) with colored dots |
| Quality / validation process | Side-by-side pass cards (what each pass does) |
| Configuration / injection | Cards for the chain + variable table |
| Metrics / operations | Feature cards + principle badges |
| Comparison data | Use `generate-comparison-pptx` skill instead |

### Step 3 — Generate the Python script

Create a Python script using the helper functions and design system
documented below (in the "Reference Script" section). Do NOT reference
any external file — all helpers are inlined in this skill document.

Key rules for distillation slides:

1. **One idea per slide** — if you're cramming two stories, split
2. **Cards over paragraphs** — use `card()` helper for grouped info
3. **Badges for inventories** — colored rounded rects in grids
4. **Phase flows** — numbered boxes with arrows for pipelines
5. **Insight boxes** — one-sentence takeaways at the bottom of each slide
6. **Font sizes**: titles 28pt, card titles 16pt, body 13-14pt, minimum 11pt
7. **Max 6 bullet points per card** — beyond that, split or summarize

### Step 4 — Run the script

```bash
python <path-to-script>
```

Then open:
```bash
# Windows
Start-Process "<path-to-pptx>"
# macOS
open "<path-to-pptx>"
# Linux
xdg-open "<path-to-pptx>"
```

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
# Primary accent       → ACCENT_1 (blue in default theme)
# Positive accent      → ACCENT_2 (green)
# AI/validation accent → ACCENT_3 (purple)
# Warning accent       → ACCENT_4 (orange)
# Danger accent        → ACCENT_5 (red)
# Info accent          → ACCENT_6 (teal)
```

Accent colors assigned by topic/section (not by compared items):
- ACCENT_1 for primary/structural concepts
- ACCENT_2 for positive/output/quality
- ACCENT_3 for validation/AI passes
- ACCENT_4 for warnings/configuration
- ACCENT_5 for problems/constraints
- ACCENT_6 for processing/operations

CRITICAL: Never use `RGBColor(...)` for slide content. Always use
`_apply_theme_color(color_format, MSO_THEME_COLOR.XXX, brightness)`
so colors follow the theme. Use `brightness` (-1.0 to 1.0) for
lighter/darker variants of the same theme slot.

## Helper Functions

The reference script provides:

- `set_bg(slide)` — set background to theme's DARK_1
- `txt(slide, l, t, w, h, text, sz, theme_color, brightness, bold, align)` — text box; theme_color=None means inherit
- `rect(slide, l, t, w, h, fill_theme, fill_brightness, text, ...)` — rounded rect; fc_theme=None means inherit
- `header(slide, title, subtitle)` — slide title + subtitle
- `card(slide, l, t, w, h, title, lines, accent_theme, tsz, bsz)` — info card with accent bar
- `_apply_theme_color(color_format, theme_color, brightness)` — apply theme color to any element

All helpers are documented in the "Reference Script" section below.

## Text Grouping Rule

When multiple text lines belong together (e.g., bullet points in a card,
description lines, profile text), they MUST be rendered as paragraphs
within a single text frame — NOT as separate `txt()` calls. This produces
one editable text block in PowerPoint instead of many independent floating
text fields.

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

Use separate `txt()` only for truly independent text elements (titles,
subtitles, insight boxes) that are positioned in different areas of the
slide.

## Theme Color Inheritance Rule

To ensure presentations adapt when the user switches the PowerPoint theme
(Design tab), text and shape colors follow this rule:

- `None` / omit the color parameter = **inherit from theme** (auto-adapts
  to light or dark backgrounds). Use this for all body text, subtitles,
  axis labels, data labels, and any text that should be readable on any
  background.
- Explicit `MSO_THEME_COLOR.ACCENT_*` = use only on **accent-colored
  elements**: card title text, text inside colored shapes, insight box
  text, item badges. These are intentionally colored and should stay
  colored regardless of theme.

Never set `LIGHT_1` or `LIGHT_2` explicitly on text — these are white/gray
in dark themes but invisible on white backgrounds. Let PowerPoint handle
the text color through theme inheritance.

## Distillation Principles

1. **Audience-first**: The reader of the slides is NOT the author of the
   docs. Strip implementation details, keep concepts and decisions.
2. **Visual hierarchy**: Use cards, badges, and color to create scannable
   slides. No walls of text.
3. **Evidence preservation**: If the source doc has concrete numbers
   (line caps, token limits, retry counts), keep them — they build trust.
4. **Flow over detail**: Show the pipeline/workflow shape first, then
   drill into individual phases only if they're interesting.
5. **Insight boxes**: Every data-heavy slide should end with a one-line
   "so what?" takeaway in a tinted box.

## Title Slide Requirements

Every presentation must include on the title slide:
- Clear statement of intent (what is this about)
- Data source reference (which doc(s) this was distilled from)
- "AI-generated presentation" notice with verification note

## Sources & References Slide

If the source documentation contains URLs or citations, extract them into
the `SOURCES` list in the generated script:

```python
SOURCES = [
    ("Kiro PBT documentation", "https://kiro.dev/docs/specs/correctness/"),
    ("Hypothesis library", "https://hypothesis.readthedocs.io/"),
]
```

A "Sources & References" slide is auto-generated at the end with clickable
hyperlinks. Each source shows the label as a blue underlined link, followed
by the URL in muted text. If `SOURCES` is empty, the slide is skipped.

When distilling markdown docs, scan for `[label](url)` patterns and extract
them into the SOURCES list.

## Template Support

The script supports an optional `.pptx` template file:

```python
TEMPLATE_PATH = Path("path/to/company-template.pptx")
```

If provided, the presentation inherits the template's theme, slide master,
and color scheme. This lets companies provide a branded template — the
generated content adapts to whatever theme colors are defined.

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
- Subject: from the `INTENT` constant
- Comments: skill attribution

## Output Location

Both output files (the generator script and the PPTX) MUST be saved under:

```
.olaf/work/presentations/<presentation-name>/
```

The `<presentation-name>` folder is derived from the context — typically
the topic or source document name, in kebab-case.

Examples:
- Distilling `docs/architecture.md` → save to
  `.olaf/work/presentations/architecture/generate_pptx.py` and
  `.olaf/work/presentations/architecture/architecture.pptx`
- Distilling `agentic/straf-cli/docs/documentor-architecture.md` → save to
  `.olaf/work/presentations/documentor-architecture/generate_pptx.py` and
  `.olaf/work/presentations/documentor-architecture/documentor-architecture.pptx`

If the user explicitly requests a different location, use that instead.

Naming convention:
- Script: `generate_pptx.py` (inside the presentation folder)
- PPTX: `<presentation-name>.pptx`

## Output

1. A Python script (saved alongside the source docs for reproducibility)
2. A `.pptx` file with native editable shapes and text (no images)

## Example: Architecture doc → 6 slides

Source: `documentor-architecture.md` (759 lines, 14 sections)

| Slide | Title | Content |
|-------|-------|---------|
| Title | Documentor | Intent + tech badges + AI notice |
| 1 | Executive Summary | Problem / Solution / Output cards + principles |
| 2 | The 11-Phase Pipeline | Phase flow boxes + design decision cards |
| 3 | 12 Technology Profiles | Grid of profiles + fallback chain explanation |
| 4 | 3-Pass Quality System | Validation / Verification / Fix cards |
| 5 | Agent Context Injection | Injection chain + variables + model config |
| 6 | Bulk Execution & Metrics | Features + tracking + logging + principles |


## Reference Script — Complete Helper Library

The following is the complete reference implementation. When generating a
script for the user, copy the helpers you need and replace the DATA SECTION
with content extracted from the user's documentation. The script must be
fully self-contained — no imports from external skill files.

```python
#!/usr/bin/env python3
"""
Documentation Distillation PPTX Generator
==========================================
Generates a professional PowerPoint presentation that distills large markdown
documentation into concise, visual slides.

THEME-AWARE: All colors use PowerPoint theme slots so the user can switch
the theme in PowerPoint and all colors adapt automatically.

Requirements: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pathlib import Path


# ── Theme color semantic names ──
ACCENT_PRIMARY   = MSO_THEME_COLOR.ACCENT_1   # Blue / structural
ACCENT_POSITIVE  = MSO_THEME_COLOR.ACCENT_2   # Green / output / quality
ACCENT_AI        = MSO_THEME_COLOR.ACCENT_3   # Purple / validation
ACCENT_WARNING   = MSO_THEME_COLOR.ACCENT_4   # Orange / config
ACCENT_DANGER    = MSO_THEME_COLOR.ACCENT_5   # Red / problems
ACCENT_INFO      = MSO_THEME_COLOR.ACCENT_6   # Teal / processing


# ── Helpers ──

def _apply_theme_color(color_format, theme_color, brightness=0.0):
    """Apply a theme color with optional brightness adjustment."""
    color_format.theme_color = theme_color
    if brightness != 0.0:
        color_format.brightness = brightness


def set_bg(slide):
    """No-op: let the slide inherit its background from the slide master/layout."""
    pass


def txt(slide, l, t, w, h, text, sz=14, theme_color=MSO_THEME_COLOR.LIGHT_1,
        brightness=0.0, bold=False, align=PP_ALIGN.LEFT):
    """Add a positioned text box."""
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(sz)
    if theme_color is not None:
        _apply_theme_color(p.font.color, theme_color, brightness)
    p.font.bold = bold
    p.font.name = "Segoe UI"
    p.alignment = align
    return box


def rect(slide, l, t, w, h, fill_theme, fill_brightness=0.0,
         text="", sz=14, fc_theme=MSO_THEME_COLOR.LIGHT_1, fc_brightness=0.0,
         bold=False):
    """Add a rounded rectangle."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                   Inches(l), Inches(t), Inches(w), Inches(h))
    shape.fill.solid()
    _apply_theme_color(shape.fill.fore_color, fill_theme, fill_brightness)
    shape.line.fill.background()
    if text:
        tf = shape.text_frame
        tf.word_wrap = True
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(sz)
        if fc_theme is not None:
            _apply_theme_color(p.font.color, fc_theme, fc_brightness)
        p.font.bold = bold
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return shape


def header(slide, title, subtitle=""):
    """Add standard slide title + subtitle."""
    set_bg(slide)
    txt(slide, 0.5, 0.3, 12, 0.6, title, sz=28, bold=True)
    if subtitle:
        txt(slide, 0.5, 0.85, 12, 0.4, subtitle, sz=14)


def card(slide, l, t, w, h, title, lines, accent_theme, tsz=16, bsz=14):
    """Add an info card with accent top border and bullet lines."""
    bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(l), Inches(t), Inches(w), Inches(h))
    bg.fill.background()
    bg.line.width = Pt(1.5)
    _apply_theme_color(bg.line.color, accent_theme)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(l + 0.05), Inches(t + 0.05),
                                 Inches(w - 0.1), Inches(0.06))
    bar.fill.solid()
    _apply_theme_color(bar.fill.fore_color, accent_theme)
    bar.line.fill.background()
    txt(slide, l + 0.15, t + 0.18, w - 0.3, 0.35, title,
        sz=tsz, theme_color=accent_theme, bold=True)
    body_box = slide.shapes.add_textbox(
        Inches(l + 0.15), Inches(t + 0.55),
        Inches(w - 0.3), Inches(h - 0.7))
    tf = body_box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(bsz)
        _apply_theme_color(p.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        p.font.name = "Segoe UI"
        p.space_after = Pt(4)


def phase_flow(slide, phases, y_top=1.5):
    """Draw a horizontal flow of numbered phase boxes with arrows."""
    x = 0.3
    for num, name, desc, clr in phases:
        rect(slide, x, y_top, 1.1, 0.5, clr, text=num, sz=16, bold=True)
        txt(slide, x, y_top + 0.55, 1.1, 0.35, name,
            sz=11, bold=True, align=PP_ALIGN.CENTER)
        txt(slide, x, y_top + 0.9, 1.1, 0.6, desc,
            sz=9, align=PP_ALIGN.CENTER)
        if num != phases[-1][0]:
            txt(slide, x + 1.05, y_top + 0.05, 0.15, 0.4, "→",
                sz=16, align=PP_ALIGN.CENTER)
        x += 1.18


def grid_items(slide, items, y_start=1.5, cols=4):
    """Draw a grid of labeled items with colored dots."""
    col_w = 3.0
    row_h = 0.65
    for i, (name, sub, clr) in enumerate(items):
        col = i % cols
        row = i // cols
        x = 0.5 + col * 3.2
        y = y_start + row * 0.85
        rect(slide, x, y, col_w, row_h, clr, 0.85)
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                      Inches(x + 0.1), Inches(y + 0.2),
                                      Inches(0.2), Inches(0.2))
        dot.fill.solid()
        _apply_theme_color(dot.fill.fore_color, clr)
        dot.line.fill.background()
        txt(slide, x + 0.4, y + 0.05, 1.8, 0.3, name, sz=13, bold=True)
        txt(slide, x + 0.4, y + 0.35, 1.8, 0.25, sub, sz=10)


def badge_row(slide, badges, y=5.0):
    """Draw a horizontal row of principle/feature badges."""
    n = len(badges)
    total_w = n * 2.1
    x = (13.333 - total_w) / 2
    for label, desc, clr in badges:
        rect(slide, x, y, 2.0, 0.45, clr, text=label, sz=10, bold=True)
        txt(slide, x, y + 0.5, 2.0, 0.35, desc, sz=10,
            align=PP_ALIGN.CENTER)
        x += 2.1


def build_sources_slide(prs, sources):
    """Final slide: Sources & References with clickable hyperlinks."""
    if not sources:
        return
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header(slide, "Sources & References")
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


# ── DATA SECTION — replace with content from your docs ──

TITLE = "System Name"
INTENT = "One-sentence description"
SOURCE = "Data: distilled from system-architecture.md"
AI_NOTICE = "AI-generated presentation — content verified by author"
SOURCES = []
TEMPLATE_PATH = None  # Set to Path("path/to/template.pptx") if available
OUTPUT_PATH = Path("distilled-overview.pptx")


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
    # build_exec_summary(prs)
    # ...
    # build_sources_slide(prs, SOURCES)

    prs.core_properties.title = TITLE
    prs.core_properties.subject = INTENT
    prs.core_properties.comments = "Generated by distill-docs-to-pptx skill"
    prs.save(str(OUTPUT_PATH))
    print(f"✅ Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
```
