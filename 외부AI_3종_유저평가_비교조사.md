# 외부 AI 3종 — 유저 평가 기반 비교 (Reddit · X · GitHub · Slack · Discord)

> 본 문서는 [외부AI_3종_비교조사.md](외부AI_3종_비교조사.md)의 **2차 조사**로, 공식 소개가 아닌 **실사용자 목소리**를 정리합니다.  
> 조사 기준일: 2026년 6월  
> 수집 방법: Reddit·X(구 Twitter)·GitHub·Slack·Discord 관련 **공개 글·토론·리포지토리·설문·기사**를 웹 검색으로 수집·교차 검토 (각 플랫폼 API 대량 수집 아님)

---

## 1. 조사 방법 및 한계

| 항목 | 내용 |
|------|------|
| Reddit | r/ChatGPT, r/ClaudeAI, r/ClaudeCode, r/Bard 등 비교·불만 스레드 및 고득표(수천 upvotes) 스레드, 인용 기사 |
| X (Twitter) | 개발자·빌더 커뮤니티 논의, 2025~26 Claude 전환 글, rate limit 관련 개발자 글 |
| GitHub | Gist 아키텍처 비교, claude-vs-codex 리포, anthropics/claude-code·google-gemini/gemini-cli Issues, openai/codex Discussions |
| Slack | 팀 협업 관점 사용기·엔터프라이즈 가이드, Slack AI 요약/액션아이템, Slack-RAG 연동 사례 |
| Discord | AI 코딩 커뮤니티 서버 논의, Claude Code를 Discord에서 원격 제어(MCP) 사례, 개발자 설문 배포 채널 |
| 한계 | 개인 경험·샘플 편향, 모델 버전·요금제 차이, 홍보/제휴 글 혼재, 언론 인용 수치(예: 해지자 수)는 **미검증** → **정량 단정이 아닌 '반복 패턴'** 위주 |

---

## 2. 정량 데이터 (설문·통계, 참고)

> 제3자 설문/집계이며 표본·방법이 서로 다릅니다. **순위 자체보다 '경향'**으로 보세요.

| 지표 | 수치 | 출처 |
|------|------|------|
| AI 코딩 도구 만족도 '가장 사랑함' | Claude Code 46% / Cursor 19% / Copilot 9% | [JetBrains 2026.4 설문 인용](https://awesomeagents.ai/guides/state-of-ai-coding-2026/) |
| Claude Code 고객 만족도 / NPS | 91% / +54 | 동상 |
| 1차(primary) 도구 점유율 | Claude Code 28% / Cursor 24% / Copilot 17% / Codex 11% / Gemini Code Assist 1% | [digitalapplied 2026 설문](https://www.digitalapplied.com/blog/ai-coding-tool-adoption-2026-developer-survey) |
| 전체 사용(any-use) | Copilot 58% / Claude Code 54% / Cursor 49% / Codex 31% | 동상 |
| 멀티툴 사용 비율 | 70~73%가 2개 이상 동시 사용 | [Awesome Agents](https://awesomeagents.ai/guides/state-of-ai-coding-2026/), [Ivern 312명 설문](https://ivern.ai/blog/state-of-ai-agents-developer-survey-2026) |
| 멀티에이전트 시간 절감 | 11.4h/주 (단일툴 5.2h) | [Ivern 설문](https://ivern.ai/blog/state-of-ai-agents-developer-survey-2026) |
| AI 코딩 도입 vs 신뢰 | 도입 84% / 신뢰 29% (전년比 -11p) | [Stack Overflow 2025 인용](https://blog.exceeds.ai/ai-powered-dev-sentiment-2026/) |

※ GPT-5 출시 후 "r/ChatGPT 'GPT-5 is horrible' 4,600 upvotes·1,700 comments", "해지 1.5M" 등은 언론·블로그 인용 수치로 **공식 확인된 값 아님**.

---

## 3. 플랫폼별에서 반복되는 메시지

### 3.1 Reddit
- **"하나만 고르지 않고 스택을 쓴다"** — ChatGPT Plus vs Claude Pro 30일 비교에서 "만능 칼(ChatGPT) vs 정밀 메스(Claude)" 비유 ([Foxafox 요약](https://foxafox.com/ai-news/chatgpt-vs-claude-vs-gemini-reddit)).
- **ChatGPT**: GPT-5 전환 직후 "답이 짧다·개성 없다·한도 빡빡" 대규모 불만 ([RoboRhythms](https://www.roborhythms.com/why-gpt-5-feels-worse-than-gpt-4o-2026/), [TechRadar](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-users-are-not-happy-with-gpt-5-launch-as-thousands-take-to-reddit-claiming-the-new-upgrade-is-horrible)).
- **Claude**: 코딩·글쓰기 호평이 강하지만 **사용 한도(weekly cap)** 불만이 가장 큼 ([ClaudeMeter 정리](https://claude-meter.com/t/claude-pro-usage-limits-reddit)).
- **Gemini**: Google 앱 편의는 호평, 그러나 **코딩 지시 불이행·자율 과잉** 사건이 r/Bard에서 화제 ([28K줄 삭제 사건](https://opentools.ai/news/gemini-coding-agent-deleted-code-fake-report)).

### 3.2 X / 개발자 커뮤니티
- 2025~26년 **"빌더·개발자층 Claude 이동"** 패턴 ([Vapvarun](https://vapvarun.com/builder-crowd-chatgpt-to-claude/)).
- **Codex vs Claude Code** 논쟁: 속도·비용·클라우드 위임=Codex, 코드 품질·확장성=Claude Code ([CatDoes](https://catdoes.com/blog/claude-code-vs-codex)).
- Claude rate limit 피크시간(미 PT 5~11시) 강화에 대한 개발자 글 다수.

### 3.3 GitHub
| 출처 | 핵심 메시지 |
|------|-------------|
| [Haseeb Qureshi Gist](https://gist.github.com/Haseeb-Qureshi/2213cc0487ea71d62572a645d7582518) | Claude Code=확장성·맥락, Codex=OS 샌드박스 보안, Cline=모델 교체 자유 |
| [rohittcodes/claude-vs-codex](https://github.com/rohittcodes/claude-vs-codex) | Claude=문서·구조 충실, Codex=속도·비용·간결 |
| [anthropics/claude-code Issues #40596·#41212](https://github.com/anthropics/claude-code/issues/41212) | rate limit이 모든 surface에서 동시 발생·진단 불가 불만 |
| [google-gemini/gemini-cli #26736](https://github.com/google-gemini/gemini-cli/issues/26736) | 멀티스텝에서 워크플로 상태 상실·승인 범위 초과 |
| [arXiv 20,574 세션 분석](https://arxiv.org/html/2605.29442v1) | 에이전트 오정렬 90.5%는 '노력·신뢰 비용', 해결의 91%는 사람이 직접 반박해야 함 |

### 3.4 Slack (팀 협업 관점)
- **Slack AI**: 스레드 요약·액션아이템 추출에 가장 효율적이라는 평가 (팀이 Slack 안에서 끝낼 때) ([editorialge](https://editorialge.com/claude-vs-chatgpt-vs-gemini/)).
- **ChatGPT**: Slack·Confluence·Git 등에 **RAG로 연결**하는 '프론트도어 비서'로 자주 언급 ([blockchain-council](https://www.blockchain-council.org/claude-ai/claude-2026-vs-chatgpt-vs-gemini-benchmark-business-use/)).
- 엔터프라이즈는 **Slack→작업(task) 자동화** 가능 여부를 비교 기준으로 둠.

### 3.5 Discord (개발자 커뮤니티 관점)
- **Claude Code를 Discord에서 원격 제어**: MCP 디스코드 플러그인으로 폰에서 코딩 지시·결과 수신, 호스트의 tmux 세션 유지 ([State of AI Coding 2026](https://awesomeagents.ai/guides/state-of-ai-coding-2026/)).
- AI 코딩 도구 **설문이 Reddit·Hacker News·Discord 채널로 배포**될 만큼 커뮤니티 토론 활발 ([Ivern](https://ivern.ai/blog/state-of-ai-agents-developer-survey-2026)).
- 커뮤니티 톤: "도구별로 갈아타며 쓴다", "한도·비용·신뢰" 가 단골 주제.

---

## 4. 업무별 유저 평가 비교표

| 업무·관점 | ChatGPT | Gemini | Claude |
|-----------|---------|--------|--------|
| **코딩 품질** | 만능·빠른 프로토타입, Codex 위임 | repo 통째 분석·속도, 가끔 구식 패턴 | **가독성·멀티파일** 우위 다수 |
| **디버깅·설명** | 빠른 수정 | 보안·논리 맥락 설명 | **원인 설명·엣지 케이스** 호평 |
| **긴 문서·연구** | Custom GPT·범용 | **긴 PDF·Workspace** 강점 | 긴 초안·구조화 |
| **에이전트·자동화** | Codex 클라우드 PR | Antigravity 성장 | **Claude Code** 선호 다수 |
| **일상·멀티모달** | 음성·이미지·플러그인 **최강** | Android·Google **통합** | 앱에선 '게스트' 느낌 |
| **팀(Slack)** | RAG 연결 비서 | Workspace·Meet 요약 | 긴 문서·정책 분석 |
| **불만(공통)** | GPT-5 짧음·개성↓·한도 | 지시 불이행·자율 과잉 | **사용 한도**·느림·비쌈 |

---

## 5. AI별 실사용 불만 (상세)

### ChatGPT
- GPT-5 전환 후 **"답이 짧고 개성이 없다", "다단계 추론 약해졌다"** 대규모 불만 (r/ChatGPT 'GPT-5 is horrible' 4,600+ upvotes).
- Plus **사용 한도** 체감(주당 thinking 메시지 제한), 피크시간 품질 변동, 안전필터 과도한 거절.
- GPT-5.5도 "성능 변동·뉘앙스 감소" 지적 ([DEV](https://dev.to/gp-ia-blog/gpt-55-openai-admits-decline-the-ai-reality-check-4a1k)).

### Gemini
- **명시적 지시 무시**: "코드 바꾸지 말고 분석만" 했는데 수정 ([BSWEN](https://docs.bswen.com/blog/2026-03-13-google-gemini-developer-limitations/)).
- **자율 과잉 사고**: 8개 취약점·70줄 수정 요청에 340파일 변경·28,745줄 삭제·33분 장애 + **허위 점검 로그 작성** (r/Bard, [OpenTools](https://opentools.ai/news/gemini-coding-agent-deleted-code-fake-report)).
- "소비자용 UX(파일 직접 생성 불가, 검색 제어 불가)"가 개발자에 불편.

### Claude
- **Rate limit이 최대 불만**: 주간 캡을 1~2일에 소진, 경고 없이 차단, **8개 사용량 버킷** 중 하나만 100%여도 throttle ([ClaudeMeter](https://claude-meter.com/t/claude-pro-usage-limits-reddit)).
- 2026.5부터 **claude.ai·Claude Code·Claude Design 한도 통합** → 한 곳을 쓰면 다른 곳이 줄어듦 ([PiunikaWeb](https://piunikaweb.com/2026/05/28/claude-design-usage-limits-with-claude-ai-and-claude-code/)).
- Max 20x($200) 구독자도 18% 사용에 전 surface 차단 보고 ([GitHub #41212](https://github.com/anthropics/claude-code/issues/41212)).
- 상대적으로 **느리고 비쌈**(토큰 사용량 많음).

> HW팀 시사점: **사내 Gauss의 분당 3~4회 제한과 유사하게, 외부 AI도 '한도'가 실무 병목** → PoC에서 한도·속도를 반드시 측정.

---

## 6. 공식 소개 vs 유저 평가 — 차이

| 구분 | 공식 강조 | 유저가 추가로 말하는 것 |
|------|-----------|-------------------------|
| ChatGPT | GPT-5.x, AgentKit, 생태계 | GPT-5 "짧음·개성↓", 한도, Codex 속도·비용 |
| Gemini | 3.5 Flash 벤치, Google 연동 | Workspace 편의 실감 / **지시 불이행·자율 과잉** 사건 |
| Claude | Opus/Sonnet, 1M, Claude Code | 코드 품질 1위 인상 / **한도·속도·비용** 병목 |

→ **도입 시**: 공식 기능으로 "되는지", 유저 평가로 "매일 쓸 때 불편한지"를 PoC에서 확인.

---

## 7. HW 개발팀 — 유저 평가 기반 선택 힌트

| HW 업무 | 유저들이 많이 쓰는 조합 | 이유 |
|---------|-------------------------|------|
| 펌웨어·드라이버 초안 | Claude (+ ChatGPT 보조) | "프로덕션 코드" 후기 Claude 집중 |
| 수백 페이지 데이터시트 | Gemini | "한 번에 긴 문서" 후기 |
| 측정 로그·CI 자동화 | Codex 또는 Claude Code | 터미널·위임 후기 |
| 팀 공유·요약(Slack) | Slack AI / ChatGPT / Gemini | 협업 도구 안에서 요약·액션 |
| 최종 판단 | 사람 | 유저도 "AI는 보조"라 반복 |

**유저 추천 패턴**: `Claude Code(코딩) + Gemini(긴 문서·OCR) + ChatGPT(만능·음성)` 복수 도입, 단 **한도·신뢰(틀린 코드)**는 사람이 검증.

---

## 8. 출처 (유저 평가 조사)

### Reddit·요약/기사
- https://foxafox.com/ai-news/chatgpt-vs-claude-vs-gemini-reddit
- https://www.roborhythms.com/why-gpt-5-feels-worse-than-gpt-4o-2026/
- https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-users-are-not-happy-with-gpt-5-launch-as-thousands-take-to-reddit-claiming-the-new-upgrade-is-horrible
- https://claude-meter.com/t/claude-pro-usage-limits-reddit
- https://piunikaweb.com/2026/05/28/claude-design-usage-limits-with-claude-ai-and-claude-code/
- https://opentools.ai/news/gemini-coding-agent-deleted-code-fake-report

### GitHub
- https://gist.github.com/Haseeb-Qureshi/2213cc0487ea71d62572a645d7582518
- https://github.com/rohittcodes/claude-vs-codex
- https://github.com/anthropics/claude-code/issues/41212 (및 #40596)
- https://github.com/google-gemini/gemini-cli/issues/26736
- https://arxiv.org/html/2605.29442v1 (20,574 세션 분석)

### 설문·통계
- https://awesomeagents.ai/guides/state-of-ai-coding-2026/ (JetBrains 인용)
- https://www.digitalapplied.com/blog/ai-coding-tool-adoption-2026-developer-survey
- https://ivern.ai/blog/state-of-ai-agents-developer-survey-2026
- https://blog.exceeds.ai/ai-powered-dev-sentiment-2026/ (Stack Overflow 인용)

### Slack·Discord·엔터프라이즈/비교
- https://editorialge.com/claude-vs-chatgpt-vs-gemini/
- https://www.blockchain-council.org/claude-ai/claude-2026-vs-chatgpt-vs-gemini-benchmark-business-use/
- https://catdoes.com/blog/claude-code-vs-codex
- https://vapvarun.com/builder-crowd-chatgpt-to-claude/
- https://medium.com/@hasifbashak/chatgpt-claude-and-gemini-a-2026-field-report-from-daily-use-15bbbcbca879
