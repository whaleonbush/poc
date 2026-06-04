# -*- coding: utf-8 -*-
"""외부 AI 4종 벤치마크 비교 — 그래프 중심 (2026.6)"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.chart.data import CategoryChartData

NAVY   = RGBColor(0x14, 0x2A, 0x4A)
BLUE   = RGBColor(0x1F, 0x6F, 0xB2)
SKY    = RGBColor(0xE8, 0xF1, 0xFA)
GRAY   = RGBColor(0x44, 0x4A, 0x55)
LGRAY  = RGBColor(0x8A, 0x92, 0x9E)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0xF2, 0x7E, 0x2E)
PEACH  = RGBColor(0xFE, 0xF1, 0xE6)
LINE   = RGBColor(0xD5, 0xDD, 0xE6)
LBLUE  = RGBColor(0x9F, 0xC4, 0xE8)
FONT   = "Apple SD Gothic Neo"

# 모델별 고정 색 (슬라이드 전체 일관)
C_CLAUDE = RGBColor(0xD4, 0x77, 0x4A)
C_GPT    = RGBColor(0x10, 0xA3, 0x7A)
C_GEMINI = RGBColor(0x42, 0x85, 0xF4)
C_GROK   = RGBColor(0x6B, 0x7B, 0x8C)
MODEL_COLORS = [C_CLAUDE, C_GPT, C_GEMINI, C_GROK]
MODEL_SHORT = ["Claude\nOpus 4.8", "GPT-5.5", "Gemini\n3.1 Pro", "Grok 4.3"]

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]
KICKER = "NC HW 개발팀  |  외부 AI 4종 벤치마크 비교 (2026.6)"
TOTAL = 6

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

def pnum(slide, n):
    text(slide, Inches(12.4), Inches(7.1), Inches(0.8), Inches(0.3),
         [[(f"({n}/{TOTAL})", 10, LGRAY, False)]], align=PP_ALIGN.RIGHT)

def _style_chart(chart, title, y_max=None, show_legend=False, horizontal=False):
    chart.has_title = True
    chart.chart_title.text_frame.text = title
    chart.chart_title.text_frame.paragraphs[0].font.size = Pt(13)
    chart.chart_title.text_frame.paragraphs[0].font.bold = True
    chart.chart_title.text_frame.paragraphs[0].font.name = FONT
    chart.chart_title.text_frame.paragraphs[0].font.color.rgb = NAVY
    chart.has_legend = show_legend
    if show_legend:
        chart.legend.position = XL_LEGEND_POSITION.BOTTOM
        chart.legend.include_in_layout = False
        chart.legend.font.size = Pt(9)
        chart.legend.font.name = FONT
    val_axis = chart.category_axis if horizontal else chart.value_axis
    cat_axis = chart.value_axis if horizontal else chart.category_axis
    val_axis.has_major_gridlines = True
    val_axis.tick_labels.font.size = Pt(9)
    val_axis.tick_labels.font.name = FONT
    cat_axis.tick_labels.font.size = Pt(9)
    cat_axis.tick_labels.font.name = FONT
    if y_max is not None:
        val_axis.maximum_scale = y_max
        val_axis.minimum_scale = 0

def _color_series(series, color):
    fill = series.format.fill
    fill.solid(); fill.fore_color.rgb = color
    series.format.line.fill.background()

def _color_single_series_bars(chart, colors):
    plot = chart.plots[0]
    series = plot.series[0]
    for idx, point in enumerate(series.points):
        fill = point.format.fill
        fill.solid(); fill.fore_color.rgb = colors[idx]
        point.format.line.fill.background()

def bar_chart(slide, l, t, w, h, categories, values, title, horizontal=True,
              y_max=None, colors=None, value_suffix=""):
    data = CategoryChartData()
    data.categories = categories
    data.add_series("", values)
    ctype = XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED
    chart = slide.shapes.add_chart(ctype, l, t, w, h, data).chart
    _style_chart(chart, title, y_max=y_max, horizontal=horizontal)
    _color_single_series_bars(chart, colors or MODEL_COLORS)
    plot = chart.plots[0]
    plot.has_data_labels = True
    plot.data_labels.font.size = Pt(9)
    plot.data_labels.font.name = FONT
    plot.data_labels.number_format = f'0"{value_suffix}"'
    plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
    chart.category_axis.reverse_order = horizontal
    return chart

def grouped_bar(slide, l, t, w, h, categories, series_list, title, y_max=100):
    data = CategoryChartData()
    data.categories = categories
    for name, vals in series_list:
        data.add_series(name, vals)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, l, t, w, h, data
    ).chart
    _style_chart(chart, title, y_max=y_max, show_legend=True)
    palette = [C_CLAUDE, C_GPT, C_GEMINI, ACCENT, BLUE]
    for i, s in enumerate(chart.plots[0].series):
        _color_series(s, palette[i % len(palette)])
    chart.value_axis.maximum_scale = y_max
    chart.value_axis.minimum_scale = 0
    return chart

def legend_row(slide, l, t):
    items = [("Claude Opus 4.8", C_CLAUDE), ("GPT-5.5", C_GPT),
             ("Gemini 3.1 Pro", C_GEMINI), ("Grok 4.3", C_GROK)]
    x = l
    for label, col in items:
        box(slide, x, t, Inches(0.18), Inches(0.18), fill=col)
        text(slide, x + Inches(0.24), t - Pt(1), Inches(1.55), Inches(0.22),
             [[(label, 9.5, GRAY, False)]])
        x += Inches(1.85)

def insight_box(slide, l, t, w, h, title, lines):
    box(slide, l, t, w, h, fill=NAVY, round_=True)
    runs = [[(title, 12.5, LBLUE, True)]]
    runs += [[(ln, 11, WHITE, False)] for ln in lines]
    text(slide, l + Inches(0.22), t, w - Inches(0.44), h, runs,
         anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14, space_after=2)

# ── Slide 1: 표지 ──
s = add_slide(); set_bg(s, NAVY)
text(s, Inches(0.95), Inches(2.05), Inches(11.6), Inches(1.4),
     [[("외부 AI 4종 벤치마크 비교", 40, WHITE, True)]])
text(s, Inches(0.97), Inches(3.25), Inches(11.6), Inches(0.5),
     [[("Claude  ·  ChatGPT  ·  Gemini  ·  Grok  (그래프 중심 요약)", 19, LBLUE, True)]])
box(s, Inches(0.97), Inches(4.0), Inches(4.6), Pt(4), fill=ACCENT)
text(s, Inches(0.97), Inches(4.32), Inches(11.6), Inches(1.1),
     [[("NC HW 개발팀  |  2026년 6월  |  임원 보고용", 15, RGBColor(0xC9,0xD8,0xEA), False)],
      [("출처: 공식 Model Card + Artificial Analysis 독립 집계 교차검증", 12.5, LGRAY, False)]],
     line_spacing=1.3)
pnum(s, 1)

# ── Slide 2: [방식 A] 종합 — 지능지수 + API 출력가 ──
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER, "[방식 A] 종합 비교 — 지능지수 · API 비용")
text(s, Inches(0.5), Inches(1.14), Inches(12.3), Inches(0.34),
     [[("막대가 길수록 우수(지능지수) / 비용 차트는 짧을수록 저렴(출력 $/1M tokens)", 11, GRAY, False)]])
legend_row(s, Inches(0.5), Inches(1.48))

bar_chart(s, Inches(0.45), Inches(1.78), Inches(5.95), Inches(4.55),
          MODEL_SHORT, (61, 60, 57, 53),
          "Artificial Analysis Intelligence Index (높을수록 우수)", y_max=70)

bar_chart(s, Inches(6.85), Inches(1.78), Inches(5.95), Inches(4.55),
          MODEL_SHORT, (25, 30, 12, 2.5),
          "API 출력 단가 ($/1M tokens, 낮을수록 저렴)", y_max=35)

insight_box(s, Inches(0.5), Inches(6.42), Inches(12.35), Inches(0.82),
            "한눈에 보기",
            ["상위 3종(Claude·GPT·Gemini) 지능지수 57~61 — 성능 격차 작음",
             "Grok은 지능지수 53이나 출력가 $2.50/1M — 대량·저비용 작업에 유리"])
pnum(s, 2)

# ── Slide 3: [방식 B] 코딩 벤치마크 ──
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER, "[방식 B-1] 코딩 역량 — SWE-bench · Terminal-Bench")
text(s, Inches(0.5), Inches(1.14), Inches(12.3), Inches(0.34),
     [[("실제 소프트웨어·터미널 작업 해결률(%). * GPT SWE Verified·Grok SWE는 근사치", 11, GRAY, False)]])

grouped_bar(s, Inches(0.5), Inches(1.55), Inches(12.3), Inches(4.85),
            MODEL_SHORT,
            [
                ("SWE-bench Verified", (88.6, 75.0, 80.6, 73.5)),
                ("SWE-bench Pro", (69.2, 58.6, 54.2, 0)),
                ("Terminal-Bench 2.x", (69.0, 78.2, 68.5, 0)),
            ],
            "코딩 벤치마크 점수 (%)", y_max=100)

insight_box(s, Inches(0.5), Inches(6.52), Inches(12.35), Inches(0.72),
            "코딩 우위",
            ["SWE-bench(일반 코딩): Claude 1위  |  Terminal-Bench(터미널): GPT 1위",
             "Grok·SWE Pro 미공개 구간은 차트에서 0 처리"])
pnum(s, 3)

# ── Slide 4: [방식 B] 추론 벤치마크 ──
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER, "[방식 B-2] 추론 · 과학 지식 — GPQA · HLE")
text(s, Inches(0.5), Inches(1.14), Inches(12.3), Inches(0.34),
     [[("GPQA는 상위권 포화(90%대) → HLE(최난도)가 실질 변별 지표. * Grok HLE 근사치", 11, GRAY, False)]])

grouped_bar(s, Inches(0.5), Inches(1.55), Inches(7.8), Inches(4.85),
            MODEL_SHORT,
            [
                ("GPQA Diamond", (93.6, 92.0, 94.3, 88.0)),
                ("HLE (no tools)", (49.8, 41.4, 44.4, 50.7)),
            ],
            "추론·과학 벤치마크 (%)", y_max=100)

bar_chart(s, Inches(8.55), Inches(1.55), Inches(4.25), Inches(4.85),
          MODEL_SHORT, (1500, 1400, 1317, 1500),
          "에이전트 GDPval-AA (Elo, 높을수록 우수)", y_max=1600, value_suffix="")

insight_box(s, Inches(0.5), Inches(6.52), Inches(12.35), Inches(0.72),
            "추론·에이전트",
            ["과학(GPQA): Gemini 1위  |  최난도 추론(HLE): Grok·Claude 상위",
             "에이전트(GDPval): Grok 1500 Elo — 저비용 다단계 작업 강점"])
pnum(s, 4)

# ── Slide 5: 성능-비용 매트릭스 (버블 대용 가로 막대) ──
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER, "성능 vs 비용 — 도입 관점 요약")
text(s, Inches(0.5), Inches(1.14), Inches(12.3), Inches(0.34),
     [[("종합 지능지수(성능)와 출력 API 단가(비용)를 동일 축에서 비교 — 우상단=고성능·고비용", 11, GRAY, False)]])

# 정규화 막대: 지능지수 0-70, 비용 역수 스케일
norm_perf = [61/70*100, 60/70*100, 57/70*100, 53/70*100]
norm_cost = [(1 - p/30)*100 for p in (25, 30, 12, 2.5)]  # 낮은 가격 = 높은 점수

grouped_bar(s, Inches(0.5), Inches(1.55), Inches(7.5), Inches(4.9),
            MODEL_SHORT,
            [
                ("성능 (AA Index, 정규화)", norm_perf),
                ("비용 효율 (출력가 역산, 정규화)", norm_cost),
            ],
            "성능 · 비용 효율 (0~100, 높을수록 유리)", y_max=100)

# 포지셔닝 카드 4개
cards = [
    ("Claude Opus 4.8", "코딩·에이전트\n최상위", "고성능·고비용", C_CLAUDE),
    ("GPT-5.5", "터미널·범용\n코딩", "고성능·최고비용", C_GPT),
    ("Gemini 3.1 Pro", "과학추론·\n가성비", "중간성능·중간비용", C_GEMINI),
    ("Grok 4.3", "저비용\n에이전트", "준수능·초저비용", C_GROK),
]
for i, (name, role, cost, col) in enumerate(cards):
    cx = Inches(8.35) + (i % 2) * Inches(2.55)
    cy = Inches(1.72) + (i // 2) * Inches(2.45)
    box(s, cx, cy, Inches(2.35), Inches(2.15), fill=SKY, line=col, line_w=2, round_=True)
    box(s, cx + Inches(0.15), cy + Inches(0.15), Inches(0.55), Pt(4), fill=col)
    text(s, cx + Inches(0.15), cy + Inches(0.28), Inches(2.05), Inches(0.35),
         [[(name, 11.5, NAVY, True)]])
    text(s, cx + Inches(0.15), cy + Inches(0.72), Inches(2.05), Inches(0.9),
         [[(role, 11, GRAY, True)], [(cost, 10, col, False)]],
         line_spacing=1.2)

insight_box(s, Inches(0.5), Inches(6.52), Inches(12.35), Inches(0.72),
            "도입 시사점",
            ["코딩 중심 → Claude  |  터미널·OpenAI 생태계 → GPT  |  가성비 → Gemini  |  대량 에이전트 → Grok"])
pnum(s, 5)

# ── Slide 6: 출처 ──
s = add_slide(); set_bg(s, WHITE)
header(s, KICKER, "출처 및 검증 방법")
text(s, Inches(0.7), Inches(1.55), Inches(12), Inches(2.2),
     [[("1차 — 공식 Model / System Card", 14, NAVY, True)],
      [("Anthropic Claude Opus 4.8  ·  OpenAI GPT-5.5  ·  Google Gemini 3.1 Pro  ·  xAI Grok 4.3", 11.5, GRAY, False)],
      [("", 6, GRAY, False)],
      [("2차 — 독립 집계 (벤더 중립)", 14, NAVY, True)],
      [("Artificial Analysis Intelligence Index  ·  Vellum  ·  LMArena  ·  Stanford HELM", 11.5, GRAY, False)],
      [("", 6, GRAY, False)],
      [("유의: 공식 수치는 self-reported · harness 차이로 직접 비교 주의 · * 근사치 별도 표기", 11, ACCENT, True)]],
     line_spacing=1.35)
pnum(s, 6)

prs.save("외부AI_4종_벤치마크_비교.pptx")
print("saved benchmark charts:", TOTAL, "slides")
