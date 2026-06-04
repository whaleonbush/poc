# -*- coding: utf-8 -*-
"""외부 AI 4종(Claude·GPT·Gemini·Grok) 최신 모델 벤치마크 비교 — 2026.6"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NAVY   = RGBColor(0x14, 0x2A, 0x4A)
BLUE   = RGBColor(0x1F, 0x6F, 0xB2)
SKY    = RGBColor(0xE8, 0xF1, 0xFA)
GRAY   = RGBColor(0x44, 0x4A, 0x55)
LGRAY  = RGBColor(0x8A, 0x92, 0x9E)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0xF2, 0x7E, 0x2E)
GREEN  = RGBColor(0x27, 0xAE, 0x60)
RED    = RGBColor(0xC0, 0x39, 0x2B)
PEACH  = RGBColor(0xFE, 0xF1, 0xE6)
LINE   = RGBColor(0xD5, 0xDD, 0xE6)
LBLUE  = RGBColor(0x9F, 0xC4, 0xE8)
FONT   = "Apple SD Gothic Neo"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def add_slide(): return prs.slides.add_slide(BLANK)
def set_bg(slide, color):
    slide.background.fill.solid(); slide.background.fill.fore_color.rgb = color

def box(slide, l, t, w, h, fill=None, line=None, line_w=1.0, round_=False):
    shp = MSO_SHAPE.ROUNDED_RECTANGLE if round_ else MSO_SHAPE.RECTANGLE
    sp = slide.shapes.add_shape(shp, l, t, w, h)
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = Pt(line_w)
    sp.shadow.inherit = False
    return sp

def text(slide, l, t, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space_after=4, line_spacing=1.0):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Pt(2); tf.margin_top = tf.margin_bottom = Pt(2)
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space_after); p.line_spacing = line_spacing
        for (txt, size, color, bold) in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(size); r.font.color.rgb = color
            r.font.bold = bold; r.font.name = FONT
    return tb

def header(slide, kicker, title):
    box(slide, 0, 0, SW, Inches(1.0), fill=NAVY)
    box(slide, 0, Inches(1.0), SW, Pt(3), fill=ACCENT)
    text(slide, Inches(0.55), Inches(0.13), Inches(12), Inches(0.3),
         [[(kicker, 11, LBLUE, True)]])
    text(slide, Inches(0.55), Inches(0.4), Inches(12.2), Inches(0.55),
         [[(title, 23, WHITE, True)]])

def section(slide, l, t, w, label, color=BLUE):
    box(slide, l, t, Pt(5), Inches(0.32), fill=color)
    text(slide, l + Inches(0.12), t - Inches(0.02), w, Inches(0.36),
         [[(label, 14.5, NAVY, True)]])

def pnum(slide, n):
    text(slide, Inches(12.4), Inches(7.1), Inches(0.8), Inches(0.3),
         [[(str(n), 10, LGRAY, False)]], align=PP_ALIGN.RIGHT)

def grid_table(slide, l, t, headers, rows, col_w, row_h, head_fill=NAVY,
               fsize=10.5, hsize=11, label_fill=SKY, highlight=None):
    """highlight: dict {(row_idx, col_idx): color} 셀 배경 강조 (col_idx는 데이터 열 1부터)"""
    highlight = highlight or {}
    x = l
    for j, htxt in enumerate(headers):
        cw = col_w[j]
        box(slide, x, t, cw, row_h, fill=head_fill, line=WHITE, line_w=1)
        text(slide, x, t, cw, row_h, [[(htxt, hsize, WHITE, True)]],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        x += cw
    y = t + row_h
    for ri, row in enumerate(rows):
        x = l
        for j, cell in enumerate(row):
            cw = col_w[j]
            if j == 0:
                fill = label_fill; bold = True; col = NAVY; al = PP_ALIGN.LEFT; pad = Pt(8)
            else:
                fill = highlight.get((ri, j), WHITE if ri % 2 == 0 else RGBColor(0xF6,0xF9,0xFC))
                bold = (ri, j) in highlight; col = GRAY; al = PP_ALIGN.CENTER; pad = Pt(3)
            box(slide, x, y, cw, row_h, fill=fill, line=LINE, line_w=0.75)
            text(slide, x + pad, y, cw - pad - Pt(3), row_h, [[(cell, fsize, col, bold)]],
                 align=al, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            x += cw
        y += row_h
    return y

MODELS = ["Claude Opus 4.8", "GPT-5.5", "Gemini 3.1 Pro", "Grok 4.3"]
KICKER = "NC HW 개발팀  |  외부 AI 4종 벤치마크 비교 (2026.6)"

# ============================================================
# Slide 1 — 표지
# ============================================================
s = add_slide(); set_bg(s, NAVY)
text(s, Inches(0.95), Inches(2.05), Inches(11.6), Inches(1.4),
     [[("외부 AI 4종 벤치마크 비교", 40, WHITE, True)]], line_spacing=1.0)
text(s, Inches(0.97), Inches(3.25), Inches(11.6), Inches(0.5),
     [[("Claude  ·  ChatGPT  ·  Gemini  ·  Grok  (각 사 최신 플래그십)", 19, LBLUE, True)]])
box(s, Inches(0.97), Inches(4.0), Inches(4.6), Pt(4), fill=ACCENT)
text(s, Inches(0.97), Inches(4.32), Inches(11.6), Inches(1.1),
     [[("NC HW 개발팀  |  2026년 6월  |  임원 보고용", 15, RGBColor(0xC9,0xD8,0xEA), False)],
      [("출처: 각 사 공식 Model/System Card + Artificial Analysis·Vellum 등 독립 집계 교차검증", 12.5, LGRAY, False)]],
     line_spacing=1.3)
pnum(s, 1)

# ============================================================
# Slide 2 — [방식 A] Artificial Analysis 기준 종합 비교
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER + "  (2/4)", "[방식 A] 종합 비교 — Artificial Analysis 기준")
text(s, Inches(0.5), Inches(1.16), Inches(12.3), Inches(0.36),
     [[("독립 집계기관 Artificial Analysis의 종합 지능지수(Intelligence Index)와 가격·맥락을 한눈에 비교", 11.5, GRAY, False)]])

grid_table(
    s, Inches(0.5), Inches(1.62),
    ["구분", "Claude Opus 4.8", "GPT-5.5", "Gemini 3.1 Pro", "Grok 4.3"],
    [
        ["종합 지능지수 (AA Index)", "61  (1위)", "60", "57", "53"],
        ["강점 포지션", "코딩·에이전트 최상", "범용·터미널 코딩", "가성비 추론", "초저가 에이전트"],
        ["입력 가격 ($/1M)", "$5", "$5", "$2", "$1.25"],
        ["출력 가격 ($/1M)", "$25", "$30", "$12", "$2.50"],
        ["컨텍스트 길이", "200K (1M 베타)", "272K (최대 1M)", "1M", "1M"],
        ["개발사", "Anthropic", "OpenAI", "Google", "xAI"],
    ],
    col_w=[Inches(2.9), Inches(2.45), Inches(2.3), Inches(2.3), Inches(2.3)],
    row_h=Inches(0.6), fsize=11, hsize=11,
    highlight={(0, 1): SKY, (2, 4): PEACH, (3, 4): PEACH}
)

box(s, Inches(0.5), Inches(5.95), Inches(12.35), Inches(1.05), fill=NAVY, round_=True)
text(s, Inches(0.78), Inches(5.95), Inches(11.8), Inches(1.05),
     [[("해석", 13, LBLUE, True)],
      [("\u2022 성능: 상위 3종(Claude·GPT·Gemini)은 지능지수 57~61로 격차가 작음 → '동급 최상위권'", 11.3, WHITE, False)],
      [("\u2022 비용: Grok은 성능은 한 단계 낮으나 출력가가 1/10 수준 → 대량·저비용 작업에 유리", 11.3, WHITE, False)]],
     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.16, space_after=3)
pnum(s, 2)

# ============================================================
# Slide 3 — [방식 B] 벤치마크별 상세 비교
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER + "  (3/4)", "[방식 B] 벤치마크별 상세 비교")
text(s, Inches(0.5), Inches(1.16), Inches(12.3), Inches(0.36),
     [[("역량별 대표 벤치마크 점수 (높을수록 우수). 굵은 값 = 해당 항목 최고", 11.5, GRAY, False)]])

grid_table(
    s, Inches(0.5), Inches(1.62),
    ["벤치마크 (역량)", "Claude Opus 4.8", "GPT-5.5", "Gemini 3.1 Pro", "Grok 4.3"],
    [
        ["SWE-bench Verified (코딩)", "88.6%", "약 75%*", "80.6%", "약 72~75%"],
        ["SWE-bench Pro (난이도↑ 코딩)", "69.2%", "58.6%", "54.2%", "미공개"],
        ["Terminal-Bench 2.x (터미널 코딩)", "약 69%", "78.2%", "68.5%", "미공개"],
        ["GPQA Diamond (대학원 과학)", "93.6%", "약 92%", "94.3%", "약 88%"],
        ["HLE (도구 없음, 최난도 추론)", "49.8%", "41.4%", "44.4%", "50.7%*"],
        ["에이전트 (GDPval-AA, Elo)", "최상위군", "높음", "1317", "1500"],
    ],
    col_w=[Inches(3.35), Inches(2.3), Inches(2.1), Inches(2.3), Inches(2.2)],
    row_h=Inches(0.56), fsize=10.5, hsize=10.5,
    highlight={(0, 1): SKY, (1, 1): SKY, (2, 2): SKY, (3, 3): SKY, (4, 4): SKY, (5, 4): SKY}
)

box(s, Inches(0.5), Inches(5.66), Inches(12.35), Inches(1.34), fill=PEACH, line=ACCENT, line_w=1.2, round_=True)
text(s, Inches(0.75), Inches(5.66), Inches(11.85), Inches(1.34),
     [[("읽는 법 및 유의사항", 12.5, ACCENT, True)],
      [("\u2022 코딩(SWE-bench)·지식작업은 Claude, 터미널 코딩은 GPT, 가성비 과학추론은 Gemini, 저비용 에이전트는 Grok 우위", 10.8, GRAY, False)],
      [("\u2022 * 표시: 측정 harness·조건이 달라 직접 비교 주의 (GPT-5.5 SWE Verified·Grok HLE는 일부 공식 미공개 → 근사치)", 10.8, RED, False)],
      [("\u2022 GPQA는 상위권이 90%대 포화 상태로 변별력 낮음 → HLE·SWE-bench Pro가 실질 변별 지표", 10.8, GRAY, False)]],
     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14, space_after=2)
pnum(s, 3)

# ============================================================
# Slide 4 — 출처 및 유의사항
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER + "  (4/4)", "출처 및 검증 방법")

section(s, Inches(0.55), Inches(1.25), Inches(12), "1차 출처 — 각 사 공식 (Model / System Card)")
text(s, Inches(0.7), Inches(1.68), Inches(12), Inches(1.15),
     [[("\u2022 Anthropic — Claude Opus 4.8 System Card / anthropic.com/news/claude-opus-4-8", 11.5, GRAY, False)],
      [("\u2022 OpenAI — GPT-5.5 System Card / OpenAI Deployment Safety Hub", 11.5, GRAY, False)],
      [("\u2022 Google DeepMind — Gemini 3.1 Pro Model Card (deepmind.google/models)", 11.5, GRAY, False)],
      [("\u2022 xAI — Grok 4.3 Model Card (docs.x.ai)", 11.5, GRAY, False)]],
     line_spacing=1.25)

section(s, Inches(0.55), Inches(3.35), Inches(12), "2차 출처 — 독립 집계 (벤더 중립)")
text(s, Inches(0.7), Inches(3.78), Inches(12), Inches(1.15),
     [[("\u2022 Artificial Analysis — 종합 지능지수·가격·속도 (artificialanalysis.ai)", 11.5, GRAY, False)],
      [("\u2022 Vellum — 모델별 벤치마크 해설 / LMArena — 사용자 블라인드 선호(Elo)", 11.5, GRAY, False)],
      [("\u2022 Stanford HELM·Epoch AI·Scale SEAL — 학술·오염통제 독립 평가", 11.5, GRAY, False)]],
     line_spacing=1.25)

box(s, Inches(0.55), Inches(5.55), Inches(12.25), Inches(1.45), fill=NAVY, round_=True)
text(s, Inches(0.82), Inches(5.55), Inches(11.7), Inches(1.45),
     [[("유의사항 (임원 보고 시)", 13, LBLUE, True)],
      [("\u2022 공식 수치는 자가보고(self-reported)이며 측정 harness에 따라 점수가 달라짐 → 독립 집계와 교차검증", 11, WHITE, False)],
      [("\u2022 모델·가격은 업데이트가 잦으므로 도입 시점에 공식 페이지에서 재확인 필요", 11, WHITE, False)]],
     anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.18, space_after=3)
pnum(s, 4)

prs.save("외부AI_4종_벤치마크_비교.pptx")
print("saved benchmark:", len(prs.slides._sldIdLst), "slides")
