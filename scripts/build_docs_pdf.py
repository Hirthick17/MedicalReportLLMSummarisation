#!/usr/bin/env python
"""
Render the Review 2 documentation (Markdown) into one PDF for submission.

  python scripts/build_docs_pdf.py                      # -> reports/Review2_Documentation.pdf
  python scripts/build_docs_pdf.py --out my.pdf --no-appendix

A deliberately small Markdown subset is supported (what the docs use): #–#### headings, paragraphs,
bullet / numbered lists, pipe tables, fenced code blocks, images, bold / italic / inline code, links
(rendered as their text). Images are resolved relative to the Markdown file.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (Image, KeepTogether, ListFlowable, ListItem, PageBreak, Paragraph, Preformatted, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent
DOCS = [ROOT / "docs" / "REVIEW2_SUMMARY.md", ROOT / "docs" / "PERSON1_DATA_PIPELINE.md", ROOT / "docs" / "PERSON2_MODEL_TRAINING.md",
        ROOT / "docs" / "PERSON3_EVALUATION.md"]
APPENDIX = [ROOT / "reports" / "eval_baseline" / "comparison.md", ROOT / "reports" / "data_audit" / "data_audit.md",
            ROOT / "reports" / "data_audit" / "cfe_stats.md", ROOT / "STATUS.md"]

# Arial (ships with Windows) carries the arrows / math glyphs the docs use; fall back to Helvetica elsewhere
FONT, FONT_B, FONT_I, MONO = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier"
try:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.fonts import addMapping
    _f = Path("C:/Windows/Fonts")
    if (_f / "arial.ttf").exists():
        pdfmetrics.registerFont(TTFont("Arial", str(_f / "arial.ttf")))
        pdfmetrics.registerFont(TTFont("Arial-Bold", str(_f / "arialbd.ttf")))
        pdfmetrics.registerFont(TTFont("Arial-Italic", str(_f / "ariali.ttf")))
        pdfmetrics.registerFont(TTFont("Arial-BoldItalic", str(_f / "arialbi.ttf")))
        addMapping("Arial", 0, 0, "Arial"); addMapping("Arial", 1, 0, "Arial-Bold"); addMapping("Arial", 0, 1, "Arial-Italic"); addMapping("Arial", 1, 1, "Arial-BoldItalic")
        FONT, FONT_B, FONT_I = "Arial", "Arial-Bold", "Arial-Italic"
    if (_f / "consola.ttf").exists():
        pdfmetrics.registerFont(TTFont("Consolas", str(_f / "consola.ttf"))); MONO = "Consolas"
except Exception:  # noqa: BLE001
    pass

ss = getSampleStyleSheet()
BODY = ParagraphStyle("body", parent=ss["BodyText"], fontName=FONT, fontSize=9.2, leading=12.5, spaceAfter=4)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=7.4, leading=9.2, spaceAfter=0)
H = {1: ParagraphStyle("h1", parent=ss["Heading1"], fontName=FONT_B, fontSize=17, leading=21, spaceBefore=10, spaceAfter=8, textColor=colors.HexColor("#1a3d6d")),
     2: ParagraphStyle("h2", parent=ss["Heading2"], fontName=FONT_B, fontSize=13, leading=16, spaceBefore=10, spaceAfter=5, textColor=colors.HexColor("#1a3d6d")),
     3: ParagraphStyle("h3", parent=ss["Heading3"], fontName=FONT_B, fontSize=11, leading=14, spaceBefore=8, spaceAfter=4),
     4: ParagraphStyle("h4", parent=ss["Heading4"], fontName=FONT_B, fontSize=9.8, leading=12, spaceBefore=6, spaceAfter=3)}
CODE = ParagraphStyle("code", parent=ss["Code"], fontName=MONO, fontSize=6.9, leading=8.4, backColor=colors.HexColor("#f4f4f4"),
                      borderPadding=4, leftIndent=4, spaceAfter=6)
BULLET = ParagraphStyle("bullet", parent=BODY, leftIndent=0, spaceAfter=2)
CAPTION = ParagraphStyle("cap", parent=BODY, fontSize=8, textColor=colors.grey, alignment=TA_LEFT)
PAGE_W = A4[0] - 3.2 * cm


def inline(md: str) -> str:
    """Markdown inline -> reportlab paragraph markup."""
    t = html.escape(md, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: f'<font face="{MONO}" size="7.6">{m.group(1)}</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
    if FONT == "Helvetica":   # core fonts lack these glyphs
        t = t.replace("↓", "(lower is better)").replace("↑", "(higher is better)").replace("→", "->").replace("←", "<-").replace("≤", "<=").replace("≥", ">=")
        t = t.replace("∩", "n").replace("∪", "u").replace("≈", "~")
    return t


def render_table(rows: list[list[str]]) -> Table:
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    data = [[Paragraph(inline(c), SMALL) for c in r] for r in rows]
    widths = [PAGE_W / ncol] * ncol
    # give wider columns to longer content
    lens = [max(len(rows[i][j]) for i in range(len(rows))) for j in range(ncol)]
    tot = sum(min(l, 60) + 6 for l in lens)
    widths = [PAGE_W * (min(l, 60) + 6) / tot for l in lens]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dfe7f2")), ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#1a3d6d")),
        ("GRID", (0, 1), (-1, -1), 0.25, colors.HexColor("#c9c9c9")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f9fc")]),
    ]))
    return t


def md_to_flowables(path: Path, heading_offset: int = 0, max_lines: int | None = None) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    if max_lines:
        lines = lines[:max_lines]
    out: list = []
    i, para, in_code, code, table, lst = 0, [], False, [], [], []

    def flush_para():
        nonlocal para
        if para:
            out.append(Paragraph(inline(" ".join(para)), BODY)); para = []

    def flush_table():
        nonlocal table
        if table:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
            if rows:
                out.append(render_table(rows)); out.append(Spacer(1, 5))
            table = []

    def flush_list():
        nonlocal lst
        if lst:
            items = [ListItem(Paragraph(inline(t), BULLET), leftIndent=12) for _, t in lst]
            out.append(ListFlowable(items, bulletType="bullet" if lst[0][0] == "-" else "1", start=None if lst[0][0] == "-" else 1, leftIndent=12, bulletFontSize=7))
            out.append(Spacer(1, 3)); lst = []

    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            flush_para(); flush_table(); flush_list()
            if in_code:
                txt = "\n".join(code)
                if len(code) > 60:
                    txt = "\n".join(code[:60]) + "\n… (truncated)"
                out.append(Preformatted(txt, CODE)); code, in_code = [], False
            else:
                in_code = True
            i += 1; continue
        if in_code:
            code.append(ln.replace("\t", "    ")); i += 1; continue
        if ln.strip().startswith("|"):
            flush_para(); flush_list(); table.append(ln); i += 1; continue
        else:
            flush_table()
        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m:
            flush_para(); flush_list()
            lvl = min(4, len(m.group(1)) + heading_offset)
            out.append(Paragraph(inline(m.group(2)), H[lvl])); i += 1; continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", ln.strip())
        if m:
            flush_para(); flush_list()
            img = (path.parent / m.group(2)).resolve()
            if img.exists():
                from reportlab.lib.utils import ImageReader
                iw, ih = ImageReader(str(img)).getSize()
                w = min(PAGE_W, 15.5 * cm); h = w * ih / iw
                out.append(KeepTogether([Image(str(img), width=w, height=h), Paragraph(inline(m.group(1) or img.name), CAPTION)])); out.append(Spacer(1, 6))
            i += 1; continue
        m = re.match(r"^\s*([-*]|\d+\.)\s+(.*)", ln)
        if m and not ln.startswith("    "):
            flush_para()
            lst.append(("-" if m.group(1) in "-*" else "1", m.group(2))); i += 1; continue
        if not ln.strip():
            flush_para(); flush_list(); i += 1; continue
        if lst and ln.startswith("  "):
            lst[-1] = (lst[-1][0], lst[-1][1] + " " + ln.strip()); i += 1; continue
        flush_list(); para.append(ln.strip()); i += 1
    flush_para(); flush_table(); flush_list()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "reports" / "Review2_Documentation.pdf"))
    ap.add_argument("--no-appendix", action="store_true")
    a = ap.parse_args()
    doc = SimpleDocTemplate(a.out, pagesize=A4, leftMargin=1.6 * cm, rightMargin=1.6 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm,
                            title="medsum-fact — Review 2 documentation", author="medsum-fact team")
    story: list = []
    for k, p in enumerate(DOCS):
        if not p.exists():
            print("missing", p); continue
        story += md_to_flowables(p)
        story.append(PageBreak())
    if not a.no_appendix:
        story.append(Paragraph("Appendix — generated reports", H[1]))
        story.append(Paragraph("Verbatim copies of the machine-generated Markdown reports referenced above.", BODY))
        for p in APPENDIX:
            if p.exists():
                story.append(Paragraph(f"Appendix: {p.relative_to(ROOT)}", H[2]))
                story += md_to_flowables(p, heading_offset=2, max_lines=400)
                story.append(PageBreak())

    def footer(canvas, d):
        canvas.saveState(); canvas.setFont(FONT, 7.5); canvas.setFillColor(colors.grey)
        canvas.drawString(1.6 * cm, 0.9 * cm, "medsum-fact — Review 2 documentation")
        canvas.drawRightString(A4[0] - 1.6 * cm, 0.9 * cm, f"page {d.page}"); canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("->", a.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
