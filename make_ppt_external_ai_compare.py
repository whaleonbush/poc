# -*- coding: utf-8 -*-
"""외부 AI 3종(ChatGPT·Gemini·Claude) 비교 조사 PPT"""
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

def table_simple(slide, l, t, headers, rows, col_w, row_h, head_fill=BLUE, fsize=10.5, hsize=11):
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
            text(slide, x + Pt(3), y, cw - Pt(6), row_h, [[(cell, fsize, GRAY, False)]],
                 align=al, anchor=MSO_ANCHOR.MIDDLE, line_spacing=0.92)
            x += cw
        y += row_h
    return y

def bullet_card(slide, l, t, w, h, title, bullets, title_color=BLUE):
    box(slide, l, t, w, h, fill=SKY, line=LINE, line_w=1, round_=True)
    box(slide, l, t, Pt(6), h, fill=title_color)
    text(slide, l + Inches(0.2), t + Inches(0.1), w - Inches(0.4), Inches(0.35),
         [[(title, 13, title_color, True)]])
    yy = t + Inches(0.48)
    for b in bullets:
        text(slide, l + Inches(0.25), yy, w - Inches(0.45), Inches(0.38),
             [[("\u2022 " + b, 11, GRAY, False)]], line_spacing=1.0)
        yy += Inches(0.4)

# Slide 1 — 표지
s = add_slide(); set_bg(s, NAVY)
box(s, 0, Inches(3.9), SW, Pt(4), fill=ACCENT)
text(s, Inches(0.9), Inches(1.8), Inches(11.5), Inches(1.5),
     [[("외부 AI 3종 비교 조사", 38, WHITE, True)],
      [("ChatGPT  \u00b7  Gemini  \u00b7  Claude", 22, RGBColor(0x9F,0xC4,0xE8), True)]],
     line_spacing=1.1)
text(s, Inches(0.92), Inches(4.2), Inches(11.5), Inches(0.8),
     [[("삼성전자 스마트폰 HW 개발팀  |  2026년 6월 외부 AI 도입 검토", 15, RGBColor(0xC9,0xD8,0xEA), False)],
      [("공식 문서 + 웹 사용기 교차 검증", 13, LGRAY, False)]])
pnum(s, 1)

# Slide 2 — 보고 목적
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (1/9)", "보고 목적 및 평가 기준")
section(s, Inches(0.55), Inches(1.2), Inches(6), "왜 지금 비교하나")
text(s, Inches(0.7), Inches(1.65), Inches(12), Inches(1.0),
     [[("2026년 6월부터 외부 AI 도입을 검토합니다. 도입 전 ChatGPT·Gemini·Claude 각각의", 13, GRAY, False)],
      [("강점과 차이를 알아두어, 우리 팀 업무에 맞는 도구를 고르기 위한 조사입니다.", 13, GRAY, False)]],
     line_spacing=1.12)
section(s, Inches(0.55), Inches(2.85), Inches(6), "평가 기준 (6가지)")
criteria = ["생산성 (코딩·문서·반복 업무)", "에이전트 (자동으로 여러 단계 수행)",
            "문서·지식 (긴 사양서·검색·OCR)", "멀티모달 (이미지·PDF 등)",
            "엔터프라이즈 (관리·보안·연동)", "비용·속도 (API·사용 제한)"]
y = Inches(3.3)
for c in criteria:
    box(s, Inches(0.7), y, Inches(5.8), Inches(0.48), fill=SKY, line=LINE, line_w=0.8, round_=True)
    text(s, Inches(0.9), y, Inches(5.5), Inches(0.48), [[("\u2022 " + c, 12, GRAY, False)]],
         anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.55)
box(s, Inches(7.0), Inches(2.85), Inches(5.75), Inches(3.5), fill=PEACH, line=ACCENT, line_w=1.2, round_=True)
text(s, Inches(7.25), Inches(3.0), Inches(5.3), Inches(3.0),
     [[("조사 방법", 14, ACCENT, True)],
      [("1차: 각 회사 공식 문서", 12, GRAY, False)],
      [("2차: 웹 사용기·비교 리뷰", 12, GRAY, False)],
      [("(참고로 표기)", 11, LGRAY, False)],
      [("", 8, GRAY, False)],
      [("주의: 보안·라이선스는", 12, GRAY, False)],
      [("별도 법무·보안 검토 필요", 12, RED, True)]],
     line_spacing=1.08, space_after=2)
pnum(s, 2)

# Slide 3 — 3종 한눈에
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (2/9)", "3종 한눈에 보기")
table_simple(
    s, Inches(0.55), Inches(1.55),
    ["AI", "한 줄 포지션", "강점 (공식·참고)", "주의"],
    [
        ["ChatGPT", "만능형 올라운더", "추론·코딩·AgentKit·MCP·도구 생태계 최대", "범용이라 업무별 최적은 다를 수 있음"],
        ["Gemini", "Google 연동·긴 문서", "3.5 Flash 에이전트·코딩·검색·멀티모달·속도", "Google 생태계 의존"],
        ["Claude", "코딩·장기 에이전트", "Opus/Sonnet·1M 맥락·Claude Code·구조화 출력", "창의·범용은 ChatGPT 대비 평가 분산"],
    ],
    col_w=[Inches(1.35), Inches(2.2), Inches(5.5), Inches(3.2)],
    row_h=Inches(0.95), fsize=11, hsize=11.5
)
box(s, Inches(0.55), Inches(5.0), Inches(12.25), Inches(1.5), fill=NAVY, round_=True)
text(s, Inches(0.8), Inches(5.15), Inches(11.8), Inches(1.2),
     [[("핵심 메시지", 14, RGBColor(0x9F,0xC4,0xE8), True)],
      [("세 AI 모두 '최고 하나'가 아니라, 업무 유형별로 맞는 도구가 다릅니다. 실무에서는 복수 도입·역할 분담도 흔합니다.", 12.5, WHITE, False)]],
     line_spacing=1.1, space_after=2)
pnum(s, 3)

# Slide 4 — ChatGPT
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (3/9)", "ChatGPT (OpenAI)")
bullet_card(s, Inches(0.55), Inches(1.35), Inches(6.0), Inches(2.5), "공식 강점",
    ["GPT-5.5: 복잡 추론·코딩용 플래그십 (맥락 약 100만 토큰)",
     "Responses API: 추론·도구·웹/파일 검색·Computer Use",
     "AgentKit: 에이전트 설계·ChatKit·MCP·Evals",
     "이미지·음성 등 전용 모델 라인업"], BLUE)
bullet_card(s, Inches(6.75), Inches(1.35), Inches(6.05), Inches(2.5), "사용자 평가 (참고)",
    ["만능형: DevOps·인프라·프로토타입에 강점",
     "도구·플러그인 생태계가 가장 넓음",
     "엔터프라이즈 도입 사례·지원 체계 풍부"], ACCENT)
text(s, Inches(0.7), Inches(4.1), Inches(12), Inches(0.4), [[("HW 예시", 13, NAVY, True)]])
text(s, Inches(0.7), Inches(4.5), Inches(12), Inches(1.2),
     [[("\u2022 측정 자동화 스크립트 초안, CI/CD 로그 분석, 회의록·시험 보고서 초안", 12, GRAY, False)],
      [("\u2022 MCP로 사내 도구 연동 검토 시 후보 (보안 승인 후)", 12, GRAY, False)]],
     line_spacing=1.1)
pnum(s, 4)

# Slide 5 — Gemini
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (4/9)", "Gemini (Google)")
bullet_card(s, Inches(0.55), Inches(1.35), Inches(6.0), Inches(2.5), "공식 강점",
    ["Gemini 3.5 Flash: 에이전트·코딩·멀티모달 (2026.5 GA)",
     "Google Search·File Search·URL Context 그라운딩",
     "Managed Agents, Antigravity 개발 플랫폼",
     "100+ 페이지 문서 추론 사례 (금융 등)"], BLUE)
bullet_card(s, Inches(6.75), Inches(1.35), Inches(6.05), Inches(2.5), "사용자 평가 (참고)",
    ["긴 코드베이스·사양서 한 번에 분석",
     "검색·최신 정보·비용 효율 강점",
     "보안·논리 분석 맥락 이해 평가"], ACCENT)
text(s, Inches(0.7), Inches(4.1), Inches(12), Inches(0.4), [[("HW 예시", 13, NAVY, True)]])
text(s, Inches(0.7), Inches(4.5), Inches(12), Inches(1.2),
     [[("\u2022 센서·PMIC 데이터시트(수백 페이지)에서 설정값 찾기", 12, GRAY, False)],
      [("\u2022 스캔 PDF·회로도 캡처 OCR 후 텍스트 정리 (공식 OCR 사례)", 12, GRAY, False)]],
     line_spacing=1.1)
pnum(s, 5)

# Slide 6 — Claude
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (5/9)", "Claude (Anthropic)")
bullet_card(s, Inches(0.55), Inches(1.35), Inches(6.0), Inches(2.5), "공식 강점",
    ["Opus 4.6/4.7, Sonnet 4.6: 복잡 추론·장기 에이전트 코딩",
     "맥락 최대 100만 토큰 (Opus/Sonnet 4.6)",
     "Claude Code, Agent SDK, Skills, 구조화 출력",
     "코드 실행·웹 검색·PDF 입력"], BLUE)
bullet_card(s, Inches(6.75), Inches(1.35), Inches(6.05), Inches(2.5), "사용자 평가 (참고)",
    ["프로덕션 코딩 품질·가독성 우위 평가 다수",
     "멀티파일 리팩터링·레거시 코드 이해",
     "규제·보안 민감 업무 선호 사례"], ACCENT)
text(s, Inches(0.7), Inches(4.1), Inches(12), Inches(0.4), [[("HW 예시", 13, NAVY, True)]])
text(s, Inches(0.7), Inches(4.5), Inches(12), Inches(1.2),
     [[("\u2022 I2C/SPI 드라이버·HAL 코드 초안, MISRA-C 스타일 점검", 12, GRAY, False)],
      [("\u2022 옛날 펌웨어 코드 설명·인수인계 문서 초안", 12, GRAY, False)]],
     line_spacing=1.1)
pnum(s, 6)

# Slide 7 — 기능 비교 매트릭스
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (6/9)", "기능 비교 매트릭스")
table_simple(
    s, Inches(0.45), Inches(1.5),
    ["항목", "ChatGPT", "Gemini", "Claude"],
    [
        ["코딩·추론", "◎", "◎", "◎"],
        ["에이전트·MCP", "◎", "◎", "◎"],
        ["긴 문서·맥락", "○", "◎", "◎"],
        ["검색·최신정보", "○", "◎", "△"],
        ["멀티모달·OCR", "○", "◎", "○"],
        ["Google 연동", "△", "◎", "△"],
        ["코드 품질(참고)", "○", "○", "◎"],
    ],
    col_w=[Inches(2.5), Inches(3.2), Inches(3.2), Inches(3.2)],
    row_h=Inches(0.58), fsize=12, hsize=11.5
)
text(s, Inches(0.55), Inches(6.35), Inches(12), Inches(0.5),
     [[("◎ 강함  ○ 보통  △ 상대적 약함  |  '코드 품질'은 웹 사용기 참고, 공식 벤치 아님", 10.5, LGRAY, False)]],
     align=PP_ALIGN.CENTER)
pnum(s, 7)

# Slide 8 — HW팀 시사점 + 선택 가이드
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (7/9)", "HW 개발팀 적용 및 선택 가이드")
table_simple(
    s, Inches(0.55), Inches(1.5),
    ["업무", "우선 검토", "이유 (쉬운 말)"],
    [
        ["펌웨어·드라이버 초안", "Claude, ChatGPT", "코드 구조·주석 품질 평가 높음"],
        ["긴 데이터시트 요약", "Gemini", "긴 문서·검색이 공식 강점"],
        ["측정 로그·표 정리", "3종 모두", "반복 정리는 모두 활용 가능"],
        ["스캔 PDF·회로도 OCR", "Gemini", "문서·이미지 추론 공식 사례"],
        ["다단계 자동화", "ChatGPT, Claude", "AgentKit / Claude Code"],
        ["최종 회로·양산 판단", "사람", "AI는 보조, 실측 필수"],
    ],
    col_w=[Inches(2.8), Inches(2.5), Inches(6.95)], row_h=Inches(0.55), fsize=11, hsize=11.5
)
box(s, Inches(0.55), Inches(5.35), Inches(12.25), Inches(1.35), fill=SKY, line=LINE, line_w=1, round_=True)
text(s, Inches(0.8), Inches(5.5), Inches(11.8), Inches(1.05),
     [[("선택 가이드", 14, BLUE, True)],
      [("코딩 중심 \u2192 Claude  |  긴 사양서·검색 \u2192 Gemini  |  범용·도구 연결 \u2192 ChatGPT", 12, GRAY, False)],
      [("복수 도입·역할 분담 권장 (예: Claude 코딩 + Gemini 문서)", 12, GRAY, False)]],
     line_spacing=1.1, space_after=2)
pnum(s, 8)

# Slide 9 — 결론
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (8/9)", "결론 및 제언")
cols = [
    ("당장 PoC 가능", GREEN, ["코드·문서 초안", "측정 데이터 정리", "로그 분석", "반복 업무 자동화"]),
    ("신중 적용", ACCENT, ["회로·부품 최종 판단", "불량 원인 확정", "양산 영향 평가"]),
    ("개선·검토 과제", RED, ["보안·법무 승인", "사내 Gauss와 역할 분리", "팀 공통 가이드", "도구별 라이선스"]),
]
left = Inches(0.65); top = Inches(1.45); cw = Inches(3.95); gap = Inches(0.25); ch = Inches(3.2)
for i, (title, color, items) in enumerate(cols):
    x = left + i * (cw + gap)
    box(s, x, top, cw, ch, fill=WHITE, line=color, line_w=1.8, round_=True)
    box(s, x, top, cw, Inches(0.55), fill=color, round_=True)
    text(s, x, top, cw, Inches(0.55), [[(title, 14, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    yy = top + Inches(0.75)
    for item in items:
        text(s, x + Inches(0.25), yy, cw - Inches(0.5), Inches(0.35), [[("- " + item, 11.5, GRAY, False)]])
        yy += Inches(0.5)
box(s, Inches(0.65), Inches(4.95), Inches(12.05), Inches(1.55), fill=NAVY, round_=True)
text(s, Inches(0.9), Inches(5.1), Inches(11.5), Inches(1.25),
     [[("최종 결론", 15, RGBColor(0x9F,0xC4,0xE8), True)],
      [("외부 AI는 사내 Gauss를 대체하기보다, 보안 검토 후 '고급 보조'로 쓰는 것이 현실적입니다.", 12.5, WHITE, False)],
      [("6월 도입 전: 업무별 PoC 1~2건 선정 \u2192 효과·보안 측정 \u2192 팀 표준 가이드화를 제안합니다.", 12.5, WHITE, False)]],
     line_spacing=1.1, space_after=2)
pnum(s, 9)

# Slide 10 — 출처
s = add_slide(); set_bg(s, WHITE)
header(s, "외부 AI 3종 비교  (9/9)", "출처")
sources = [
    ("공식", "OpenAI Models / Changelog / AgentKit 소개"),
    ("공식", "Google Gemini 3.5 Blog / Gemini API / Enterprise Capabilities"),
    ("공식", "Anthropic Claude Models Overview / API Docs"),
    ("참고", "Kanerika 2026 Workflow Comparison (Medium)"),
    ("참고", "IntuitionLabs Enterprise Guide 2026"),
    ("참고", "PickYourAITool / HeyChappie 코딩 비교 리뷰"),
]
y = Inches(1.55)
for tag, desc in sources:
    box(s, Inches(0.7), y, Inches(1.1), Inches(0.42), fill=BLUE if tag == "공식" else ACCENT, round_=True)
    text(s, Inches(0.7), y, Inches(1.1), Inches(0.42), [[(tag, 11, WHITE, True)]],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(2.0), y, Inches(10.5), Inches(0.42), [[(desc, 12, GRAY, False)]],
         anchor=MSO_ANCHOR.MIDDLE)
    y += Inches(0.55)
text(s, Inches(0.7), Inches(5.5), Inches(12), Inches(1.2),
     [[("상세 URL은 동봉 마크다운 '외부AI_3종_비교조사.md' 참조", 11, LGRAY, False)],
      [("모델명·기능은 도입 시점에 공식 페이지에서 재확인 필요", 11, LGRAY, False)]],
     line_spacing=1.1)
pnum(s, 10)

prs.save("외부AI_3종_비교조사.pptx")
print("saved:", len(prs.slides._sldIdLst), "slides")
