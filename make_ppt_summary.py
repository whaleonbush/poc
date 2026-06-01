# -*- coding: utf-8 -*-
"""HW 개발팀 AI 활용 방안 — 쉬운 용어 요약본 (3페이지)"""
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
RED    = RGBColor(0xC0, 0x39, 0x2B)
PEACH  = RGBColor(0xFE, 0xF1, 0xE6)
LINE   = RGBColor(0xD5, 0xDD, 0xE6)
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
         [[(kicker, 11, RGBColor(0x9F,0xC4,0xE8), True)]])
    text(slide, Inches(0.55), Inches(0.4), Inches(12.2), Inches(0.55),
         [[(title, 23, WHITE, True)]])

def section(slide, l, t, w, label, color=BLUE):
    box(slide, l, t, Pt(5), Inches(0.32), fill=color)
    text(slide, l + Inches(0.12), t - Inches(0.02), w, Inches(0.36),
         [[(label, 14.5, NAVY, True)]])

def pnum(slide, n):
    text(slide, Inches(12.4), Inches(7.1), Inches(0.8), Inches(0.3),
         [[(str(n), 10, LGRAY, False)]], align=PP_ALIGN.RIGHT)

def table_simple(slide, l, t, headers, rows, col_w, row_h, head_fill=BLUE,
                 fsize=11, hsize=11.5):
    x = l
    for j, htxt in enumerate(headers):
        cw = col_w[j]
        box(slide, x, t, cw, row_h, fill=head_fill, line=WHITE, line_w=1)
        text(slide, x, t, cw, row_h, [[(htxt, hsize, WHITE, True)]],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        x += cw
    y = t + row_h
    for ri, row in enumerate(rows):
        x = l; fill = WHITE if ri % 2 == 0 else SKY
        for j, cell in enumerate(row):
            cw = col_w[j]
            box(slide, x, y, cw, row_h, fill=fill, line=LINE, line_w=0.75)
            al = PP_ALIGN.CENTER if j == 0 else PP_ALIGN.LEFT
            text(slide, x + Pt(4), y, cw - Pt(8), row_h, [[(cell, fsize, GRAY, False)]],
                 align=al, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.95)
            x += cw
        y += row_h
    return y

# ============================================================
# Slide 1 — 왜 지금 검토하는가
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, "삼성전자 스마트폰 HW 개발팀 AI 활용 방안  (1/4)", "왜 지금 AI 도구를 검토하는가")

section(s, Inches(0.55), Inches(1.22), Inches(6), "1. 우리 팀 업무와 AI가 도울 수 있는 부분")
intro = [
    ("우리 팀 업무", "스마트폰 안의 회로, 센서, 전원, 충전, 통신 부품이 안정적으로 동작하도록 개발·검증합니다."),
    ("AI가 잘 돕는 일", "회로 자체를 대신 설계하기보다, 코드 초안·문서 정리·로그 분석·측정 데이터 정리처럼 반복되는 일을 도와줍니다."),
    ("보고 목적", "현재 사내 도구로 지금 당장 할 수 있는 일과, 현재 조건 때문에 어려운 일을 구분해 보고드립니다."),
]
y = Inches(1.72)
for k, v in intro:
    box(s, Inches(0.55), y, Inches(6.05), Inches(1.18), fill=SKY, line=LINE, line_w=1, round_=True)
    box(s, Inches(0.55), y, Pt(6), Inches(1.18), fill=BLUE)
    text(s, Inches(0.82), y + Inches(0.1), Inches(5.55), Inches(0.35), [[(k, 13.5, BLUE, True)]])
    text(s, Inches(0.82), y + Inches(0.43), Inches(5.55), Inches(0.65), [[(v, 11.7, GRAY, False)]], line_spacing=1.05)
    y += Inches(1.33)

section(s, Inches(7.0), Inches(1.22), Inches(6), "2. 현재 사용 가능한 도구")
tools = [
    ("Cline SR", "VS Code 안에서 일하는 AI 도우미", "개발자가 시키면 코드를 읽고, 고치고, 설명하고, 간단한 명령도 실행합니다."),
    ("Gauss", "회사 안에서 쓰는 AI 두뇌", "외부 유출 부담은 낮지만, 호출 횟수 제한이 있어 속도에 한계가 있습니다."),
    ("API 호출 제한", "AI에게 질문할 수 있는 횟수 제한", "현재 분당 약 3~4회 수준이라 긴 작업은 중간에 기다리는 시간이 생깁니다."),
]
y = Inches(1.72)
for name, easy, desc in tools:
    box(s, Inches(7.0), y, Inches(5.75), Inches(1.13), fill=WHITE, line=LINE, line_w=1, round_=True)
    box(s, Inches(7.0), y, Pt(6), Inches(1.13), fill=ACCENT if name == "API 호출 제한" else BLUE)
    text(s, Inches(7.25), y + Inches(0.08), Inches(5.25), Inches(0.34), [[(name + " : " + easy, 13, NAVY, True)]])
    text(s, Inches(7.25), y + Inches(0.43), Inches(5.25), Inches(0.62), [[(desc, 11.2, GRAY, False)]], line_spacing=1.0)
    y += Inches(1.25)

box(s, Inches(7.0), Inches(5.65), Inches(5.75), Inches(1.1), fill=PEACH, line=ACCENT, line_w=1.2, round_=True)
text(s, Inches(7.25), Inches(5.75), Inches(5.25), Inches(0.85),
     [[("핵심 메시지", 13, ACCENT, True)],
      [("보안 부담 없이 쓸 수 있는 사내 AI 보조 도구이지만, 외부 AI·외부 도구처럼 자유롭고 빠른 환경은 아닙니다.", 11.8, GRAY, False)]],
     line_spacing=1.05, space_after=2)
pnum(s, 1)

# ============================================================
# Slide 2 — 지금 당장 활용 가능한 분야
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, "삼성전자 스마트폰 HW 개발팀 AI 활용 방안  (2/4)", "지금 당장 활용 가능한 분야")
section(s, Inches(0.55), Inches(1.18), Inches(8), "3. 스마트폰 HW 개발 업무 예시")
table_simple(
    s, Inches(0.55), Inches(1.58),
    ["분야", "활용 방법", "스마트폰 HW 개발 예시"],
    [
        ["부품 제어", "코드 초안 작성", "센서·전원 IC·충전 IC 설정 코드를 먼저 만들어 보고, 개발자가 검토"],
        ["부품 설명서", "데이터시트 정리", "복잡한 설정값 표를 사람이 보기 쉬운 요약표로 정리"],
        ["측정", "자동화 코드 작성", "전압·전류·온도·소비전력 측정 스크립트 초안 작성"],
        ["데이터", "로그·측정값 정리", "측정 결과를 표, 그래프, 원인 후보 문장으로 정리"],
        ["품질", "코드 점검", "빠진 예외처리, 반복 코드, 위험해 보이는 부분 확인"],
        ["문서", "보고서 초안 작성", "시험 결과, 이슈 분석, 회의 정리, 개발 가이드 초안 작성"],
    ],
    col_w=[Inches(1.45), Inches(2.75), Inches(7.55)], row_h=Inches(0.62), fsize=11.4, hsize=12
)

yb = Inches(5.72)
box(s, Inches(0.55), yb, Inches(3.95), Inches(1.28), fill=SKY, line=LINE, line_w=1, round_=True)
text(s, Inches(0.78), yb + Inches(0.12), Inches(3.55), Inches(1.05),
     [[("잘 맞는 일", 13, BLUE, True)],
      [("반복되는 코드·문서·정리 작업", 11.6, GRAY, False)],
      [("예: 측정 로그 정리, 코드 초안", 11.2, GRAY, False)]],
     line_spacing=1.08, space_after=2)
box(s, Inches(4.7), yb, Inches(3.95), Inches(1.28), fill=PEACH, line=ACCENT, line_w=1, round_=True)
text(s, Inches(4.93), yb + Inches(0.12), Inches(3.55), Inches(1.05),
     [[("주의할 일", 13, ACCENT, True)],
      [("회로 판단·불량 원인 확정", 11.6, GRAY, False)],
      [("예: 부품 최종 선정, 양산 영향 판단", 11.2, GRAY, False)]],
     line_spacing=1.08, space_after=2)
box(s, Inches(8.85), yb, Inches(3.95), Inches(1.28), fill=NAVY, round_=True)
text(s, Inches(9.08), yb + Inches(0.12), Inches(3.55), Inches(1.05),
     [[("한 줄 결론", 13, RGBColor(0x9F,0xC4,0xE8), True)],
      [("AI가 HW를 대신 설계하는 것이 아니라,", 11.4, WHITE, False)],
      [("개발자의 반복 업무를 줄이는 도구", 11.4, WHITE, False)]],
     line_spacing=1.08, space_after=2)
pnum(s, 2)

# ============================================================
# Slide 3 — 현재 조건에서의 한계
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, "삼성전자 스마트폰 HW 개발팀 AI 활용 방안  (3/4)", "현재 조건에서의 한계")
section(s, Inches(0.55), Inches(1.18), Inches(8), "4. 지금 조건에서 어려운 점")
L = Inches(0.55); W = Inches(12.25)

limits = [
    ("외부 MCP·API 도구 사용 제한", "외부 문서 검색, 외부 코드 저장소, 외부 분석 도구와 자동 연결이 어렵습니다. 예: AI가 스스로 최신 부품 예제나 외부 자료실을 찾아오지 못함."),
    ("임베딩·청킹 특화 모델 제한", "긴 데이터시트·회로 설명서를 잘게 나누고 의미별로 찾는 고급 문서 검색 품질이 제한됩니다. 예: 500페이지 사양서에서 필요한 설정값을 정확히 찾는 능력이 부족할 수 있음."),
    ("OCR 특화 도구 제한", "이미지, 스캔 PDF, 회로도 캡처 속 글자를 읽는 성능이 제한됩니다. 예: 캡처된 회로도나 스캔 데이터시트를 바로 읽어 정리하기 어려움."),
    ("Gauss API 호출 제한", "분당 약 3~4회만 AI를 부를 수 있어 Cline SR이 여러 번 생각하고 수정하는 긴 작업에서 속도가 느려집니다."),
    ("최신 정보 접근 제한", "외부 인터넷 검색이나 최신 예제 확인이 어렵습니다. 예: 새 부품의 공개 자료나 최신 오픈소스 예제를 바로 참고하기 어려움."),
    ("AI 결과 검증 필요", "그럴듯하지만 틀린 답을 줄 수 있습니다. 예: 전원 시퀀스나 타이밍 조건은 반드시 개발자가 데이터시트와 실측으로 확인해야 함."),
]

y = Inches(1.58)
for idx, (title, desc) in enumerate(limits):
    bh = Inches(0.82)
    fill = PEACH if idx in (0, 1, 2, 3) else SKY
    line = ACCENT if idx in (0, 1, 2, 3) else LINE
    box(s, L, y, W, bh, fill=fill, line=line, line_w=1.1, round_=True)
    box(s, L, y, Pt(6), bh, fill=ACCENT if idx in (0, 1, 2, 3) else BLUE)
    text(s, L + Inches(0.25), y + Inches(0.07), Inches(3.0), Inches(0.35), [[(title, 12.2, NAVY, True)]])
    text(s, L + Inches(3.35), y + Inches(0.08), Inches(9.0), Inches(0.6), [[(desc, 10.6, GRAY, False)]], line_spacing=1.0)
    y += bh + Inches(0.09)

box(s, L, Inches(6.83), W, Inches(0.42), fill=NAVY, round_=True)
text(s, L, Inches(6.83), W, Inches(0.42),
     [[("핵심: 현재 조건에서는 '보안이 필요한 사내 보조 도구'로는 유용하지만, 외부 도구까지 연결된 완전 자동 개발 도우미는 아닙니다.", 11.7, WHITE, True)]],
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
pnum(s, 3)

# ============================================================
# Slide 4 — 결론 및 제언
# ============================================================
s = add_slide(); set_bg(s, WHITE)
header(s, "삼성전자 스마트폰 HW 개발팀 AI 활용 방안  (4/4)", "결론 및 제언")

cols = [
    ("당장 적용 가능", BLUE, [
        "코드 초안 작성",
        "문서 초안 작성",
        "측정 데이터 정리",
        "로그 분석",
        "반복 업무 자동화",
    ]),
    ("신중 적용", ACCENT, [
        "회로 동작 최종 판단",
        "부품 최종 선정",
        "실제 불량 원인 확정",
        "양산 영향 판단",
        "안전·품질 영향 큰 결정",
    ]),
    ("개선 필요", RED, [
        "외부 도구 연결 제한",
        "문서 검색 성능",
        "OCR 성능",
        "Gauss 호출 속도",
        "팀 공통 사용 가이드",
    ]),
]
left = Inches(0.65); top = Inches(1.45); cw = Inches(3.95); gap = Inches(0.25); ch = Inches(3.6)
for i, (title, color, items) in enumerate(cols):
    x = left + i * (cw + gap)
    box(s, x, top, cw, ch, fill=WHITE, line=color, line_w=1.8, round_=True)
    box(s, x, top, cw, Inches(0.62), fill=color, round_=True)
    text(s, x, top, cw, Inches(0.62), [[(title, 15, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    yy = top + Inches(0.9)
    for item in items:
        text(s, x + Inches(0.28), yy, cw - Inches(0.5), Inches(0.32), [[("- " + item, 11.7, GRAY, False)]])
        yy += Inches(0.48)

box(s, Inches(0.65), Inches(5.35), Inches(12.05), Inches(1.35), fill=SKY, line=LINE, line_w=1.2, round_=True)
text(s, Inches(0.92), Inches(5.48), Inches(11.5), Inches(1.05),
     [[("최종 결론", 15, NAVY, True)],
      [("Cline SR과 Gauss는 스마트폰 HW 개발자의 반복 업무를 줄이는 데 바로 쓸 수 있습니다. 다만 외부 도구 연결, 문서 검색/OCR, API 호출 제한 때문에 '완전 자동 개발'은 어렵습니다. 따라서 낮은 위험의 정리·초안·검토 업무부터 적용하고, 사내 전용 문서 검색·OCR·호출 제한 개선을 다음 과제로 검토하는 것이 현실적입니다.", 12.3, GRAY, False)]],
     line_spacing=1.1, space_after=2)
pnum(s, 4)

prs.save("HW개발팀_AI활용방안_요약.pptx")
print("saved summary:", len(prs.slides._sldIdLst))
