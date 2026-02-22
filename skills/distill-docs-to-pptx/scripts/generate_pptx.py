#!/usr/bin/env python3
"""
Template: Documentation Distillation PPTX Generator
=====================================================
Reference script for the distill-docs-to-pptx skill.
Generates a professional PowerPoint presentation that distills large markdown
documentation into concise, visual slides.

THEME-AWARE: All colors use PowerPoint theme slots (Accent 1-6, Text 1/2,
Background 1/2) so the user can switch the theme in PowerPoint and all
colors adapt automatically. No hardcoded RGB values in slide content.

Usage:
  1. Copy this script to your working directory
  2. Replace the DATA SECTION with content extracted from your docs
  3. Run: python generate_pptx.py
  4. Open the PPTX → Design tab → pick any theme to restyle

Requirements: pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pathlib import Path


# ╔═══════════════════════════════════════════════════════════════════╗
# ║  THEME COLOR MAPPING                                              ║
# ║                                                                   ║
# ║  All colors reference PowerPoint theme slots. When the user       ║
# ║  switches the theme (Design tab), every element recolors.         ║
# ║                                                                   ║
# ║  Semantic role        → Theme slot        → Default appearance    ║
# ║  ─────────────────────────────────────────────────────────────     ║
# ║  Slide background     → (inherited)       → from theme            ║
# ║  Card background      → LIGHT_2 +0.4 bright → subtle mid-tone     ║
# ║  Primary text         → LIGHT_1           → white                ║
# ║  Body text            → LIGHT_1 -0.25 bright → light gray        ║
# ║  Subtitle/muted text  → LIGHT_2           → mid gray             ║
# ║  Primary accent       → ACCENT_1          → blue                 ║
# ║  Secondary accent     → ACCENT_2          → green                ║
# ║  Tertiary accent      → ACCENT_3          → purple               ║
# ║  Warning accent       → ACCENT_4          → orange               ║
# ║  Danger accent        → ACCENT_5          → red                  ║
# ║  Info accent          → ACCENT_6          → teal                 ║
# ║  Insight box bg       → ACCENT_1 -0.7 bright → dark tinted       ║
# ╚═══════════════════════════════════════════════════════════════════╝

# Semantic names for theme color slots — used in data section
ACCENT_PRIMARY   = MSO_THEME_COLOR.ACCENT_1   # Blue / structural
ACCENT_POSITIVE  = MSO_THEME_COLOR.ACCENT_2   # Green / output / quality
ACCENT_AI        = MSO_THEME_COLOR.ACCENT_3   # Purple / validation
ACCENT_WARNING   = MSO_THEME_COLOR.ACCENT_4   # Orange / config
ACCENT_DANGER    = MSO_THEME_COLOR.ACCENT_5   # Red / problems
ACCENT_INFO      = MSO_THEME_COLOR.ACCENT_6   # Teal / processing


# ╔═══════════════════════════════════════════════════════════════════╗
# ║  HELPERS                                                          ║
# ╚═══════════════════════════════════════════════════════════════════╝

def _apply_theme_color(color_format, theme_color, brightness=0.0):
    """Apply a theme color with optional brightness adjustment."""
    color_format.theme_color = theme_color
    if brightness != 0.0:
        color_format.brightness = brightness


def set_bg(slide):
    """No-op: let the slide inherit its background from the slide master/layout.
    This ensures that when the user switches the PowerPoint theme, the
    background changes along with everything else. If you explicitly set
    a background here, it becomes an override that blocks theme inheritance.
    """
    pass


def txt(slide, l, t, w, h, text, sz=14, theme_color=MSO_THEME_COLOR.LIGHT_1,
        brightness=0.0, bold=False, align=PP_ALIGN.LEFT):
    """Add a positioned text box. Default color is LIGHT_1 (white on dark themes).
    For textboxes (not placeholders), PowerPoint does NOT inherit the
    master's text color, so we must set it explicitly."""
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
    """Add a rounded rectangle. Text defaults to LIGHT_1 (white)."""
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
    """Add an info card with accent top border and bullet lines.
    All body lines are rendered as paragraphs inside a single text frame
    so they stay as one editable text block in PowerPoint.
    Card background is transparent — inherits from slide/theme background.
    A subtle border provides visual separation on any theme.
    """
    # Card background — transparent with accent border
    bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(l), Inches(t), Inches(w), Inches(h))
    bg.fill.background()  # transparent
    bg.line.width = Pt(1.5)
    _apply_theme_color(bg.line.color, accent_theme)
    # Accent bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(l + 0.05), Inches(t + 0.05),
                                 Inches(w - 0.1), Inches(0.06))
    bar.fill.solid()
    _apply_theme_color(bar.fill.fore_color, accent_theme)
    bar.line.fill.background()
    # Title
    txt(slide, l + 0.15, t + 0.18, w - 0.3, 0.35, title,
        sz=tsz, theme_color=accent_theme, bold=True)
    # Body lines as a single text frame with multiple paragraphs
    body_box = slide.shapes.add_textbox(
        Inches(l + 0.15), Inches(t + 0.55),
        Inches(w - 0.3), Inches(h - 0.7)
    )
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
    """Draw a horizontal flow of numbered phase boxes with arrows.
    phases: list of (number, name, description, accent_theme_color)
    """
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
    """Draw a grid of labeled items with colored dots.
    items: list of (name, subtitle, accent_theme_color)
    """
    col_w = 3.0
    row_h = 0.65
    for i, (name, sub, clr) in enumerate(items):
        col = i % cols
        row = i // cols
        x = 0.5 + col * 3.2
        y = y_start + row * 0.85
        rect(slide, x, y, col_w, row_h, clr, 0.85)  # light tint of accent
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                                      Inches(x + 0.1), Inches(y + 0.2),
                                      Inches(0.2), Inches(0.2))
        dot.fill.solid()
        _apply_theme_color(dot.fill.fore_color, clr)
        dot.line.fill.background()
        txt(slide, x + 0.4, y + 0.05, 1.8, 0.3, name, sz=13, bold=True)
        txt(slide, x + 0.4, y + 0.35, 1.8, 0.25, sub, sz=10)


def badge_row(slide, badges, y=5.0):
    """Draw a horizontal row of principle/feature badges.
    badges: list of (label, description, accent_theme_color)
    """
    n = len(badges)
    total_w = n * 2.1
    x = (13.333 - total_w) / 2
    for label, desc, clr in badges:
        rect(slide, x, y, 2.0, 0.45, clr, text=label, sz=10, bold=True)
        txt(slide, x, y + 0.5, 2.0, 0.35, desc, sz=10,
            align=PP_ALIGN.CENTER)
        x += 2.1


# ╔═══════════════════════════════════════════════════════════════════╗
# ║  DATA SECTION — replace with content from your docs               ║
# ╚═══════════════════════════════════════════════════════════════════╝

TITLE = "System Name"
INTENT = "One-sentence description of what this system does"
SOURCE = "Data: distilled from system-architecture.md (N lines)"
AI_NOTICE = "AI-generated presentation — content verified by author"

# Executive summary: 3 cards (problem / solution / output)
EXEC_CARDS = [
    {
        "title": "📖 The Problem",
        "lines": ["Problem point 1", "Problem point 2", "Problem point 3"],
        "color": ACCENT_DANGER,
    },
    {
        "title": "🤖 The Solution",
        "lines": ["Solution point 1", "Solution point 2", "Solution point 3"],
        "color": ACCENT_POSITIVE,
    },
    {
        "title": "🎯 The Output",
        "lines": ["Output 1", "Output 2", "Output 3"],
        "color": ACCENT_PRIMARY,
    },
]

EXEC_INSIGHT = "One-line key takeaway for the executive summary"

# Sources: list of (label, url) — extracted from source docs
# If the source markdown contains links, list them here.
# A "Sources & References" slide will be auto-generated at the end.
SOURCES = [
    # ("Label shown on slide", "https://full-url"),
    # Example:
    # ("Kiro PBT documentation", "https://kiro.dev/docs/specs/correctness/"),
]

# Template: path to a .pptx template file (optional).
# If provided, the presentation inherits the template's theme, slide master,
# and color scheme. Your company can provide a branded template here.
# If None or file not found, falls back to a blank presentation.
TEMPLATE_PATH = Path(__file__).parent / "template.pptx"

# Output path
OUTPUT_PATH = Path(__file__).parent / "distilled-overview.pptx"


# ╔═══════════════════════════════════════════════════════════════════╗
# ║  SLIDE BUILDERS — adapt these to your content                     ║
# ╚═══════════════════════════════════════════════════════════════════╝

def build_title_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    txt(slide, 1, 1.2, 11, 1.2, TITLE,
        sz=44, bold=True, align=PP_ALIGN.CENTER)
    txt(slide, 1, 2.6, 11, 0.6, INTENT,
        sz=20, theme_color=ACCENT_PRIMARY, align=PP_ALIGN.CENTER)
    txt(slide, 1, 3.6, 11, 0.5, SOURCE,
        sz=14, align=PP_ALIGN.CENTER)
    txt(slide, 1, 6.2, 11, 0.4, AI_NOTICE,
        sz=11, align=PP_ALIGN.CENTER)


def build_exec_summary(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header(slide, "Executive Summary")
    x = 0.5
    for ec in EXEC_CARDS:
        card(slide, x, 1.4, 3.9, 2.8, ec["title"], ec["lines"], ec["color"])
        x += 4.15
    rect(slide, 1.5, 4.5, 10.3, 0.55,
         ACCENT_PRIMARY, fill_brightness=-0.7,
         text=EXEC_INSIGHT, sz=14, fc_theme=ACCENT_POSITIVE)


def build_example_pipeline(prs):
    """Example: a pipeline/workflow slide. Adapt phases to your content."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header(slide, "Pipeline Overview", "End-to-end flow")

    example_phases = [
        ("1", "Input", "Receive\ndata", ACCENT_PRIMARY),
        ("2", "Process", "Transform\n& validate", ACCENT_POSITIVE),
        ("3", "Enrich", "Add\nmetadata", ACCENT_AI),
        ("4", "Output", "Write\nresults", ACCENT_WARNING),
    ]
    phase_flow(slide, example_phases)

    card(slide, 0.5, 3.5, 6.0, 2.5, "Key Design Decision", [
        "Explain why this pipeline is structured this way",
        "What trade-offs were made",
        "What alternatives were considered",
    ], ACCENT_PRIMARY, bsz=13)

    card(slide, 6.8, 3.5, 6.0, 2.5, "Error Handling", [
        "What happens when a phase fails",
        "Retry strategy",
        "Graceful degradation approach",
    ], ACCENT_WARNING, bsz=13)


def build_example_inventory(prs):
    """Example: a grid inventory slide. Adapt items to your content."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header(slide, "Component Inventory", "Auto-detected from configuration")

    items = [
        ("Component A", "signal-a.yaml", ACCENT_PRIMARY),
        ("Component B", "signal-b.json", ACCENT_AI),
        ("Component C", "signal-c.toml", ACCENT_POSITIVE),
        ("Component D", "signal-d.xml", ACCENT_WARNING),
    ]
    grid_items(slide, items)

    card(slide, 0.5, 3.5, 12.3, 2.5, "How Detection Works", [
        "Explain the detection/selection mechanism",
        "Priority order if multiple matches",
        "Fallback behavior when nothing matches",
    ], ACCENT_PRIMARY, bsz=13)


def build_sources_slide(prs):
    """Final slide: Sources & References with clickable hyperlinks."""
    if not SOURCES:
        return
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    header(slide, "Sources & References")

    body = slide.shapes.add_textbox(
        Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.5)
    )
    tf = body.text_frame
    tf.word_wrap = True
    for i, (label, url) in enumerate(SOURCES):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        # Bullet prefix as plain run
        run_bullet = p.add_run()
        run_bullet.text = "• "
        run_bullet.font.size = Pt(14)
        _apply_theme_color(run_bullet.font.color, MSO_THEME_COLOR.LIGHT_1, -0.25)
        run_bullet.font.name = "Segoe UI"
        # Label as clickable hyperlink run
        run_link = p.add_run()
        run_link.text = label
        run_link.font.size = Pt(14)
        run_link.font.name = "Segoe UI"
        _apply_theme_color(run_link.font.color, MSO_THEME_COLOR.HYPERLINK)
        run_link.font.underline = True
        run_link.hyperlink.address = url
        # URL shown in muted text after the label
        run_url = p.add_run()
        run_url.text = f"  ({url})"
        run_url.font.size = Pt(10)
        run_url.font.name = "Segoe UI"
        _apply_theme_color(run_url.font.color, MSO_THEME_COLOR.LIGHT_2)


# ╔═══════════════════════════════════════════════════════════════════╗
# ║  MAIN                                                             ║
# ╚═══════════════════════════════════════════════════════════════════╝

def main():
    # Use template if provided, otherwise blank presentation
    if TEMPLATE_PATH and Path(TEMPLATE_PATH).exists():
        prs = Presentation(str(TEMPLATE_PATH))
        print(f"📎 Using template: {TEMPLATE_PATH}")
    else:
        prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    build_title_slide(prs)
    build_exec_summary(prs)
    build_example_pipeline(prs)
    build_example_inventory(prs)
    build_sources_slide(prs)

    # Set document properties
    prs.core_properties.title = TITLE
    prs.core_properties.subject = INTENT
    prs.core_properties.comments = "Generated by distill-docs-to-pptx skill"

    prs.save(str(OUTPUT_PATH))
    print(f"✅ Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
