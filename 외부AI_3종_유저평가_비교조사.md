# 외부 AI 3종 — 유저 평가 기반 비교 (Reddit · X · GitHub)

> 본 문서는 [외부AI_3종_비교조사.md](외부AI_3종_비교조사.md)의 **2차 조사**로, 공식 소개가 아닌 **실사용자 목소리**를 정리합니다.  
> 조사 기준일: 2026년 6월  
> 수집 방법: Reddit·X(구 Twitter)·GitHub 관련 **공개 글·토론·리포지토리**를 웹 검색으로 수집·교차 검토 (API 대량 수집 아님)

---

## 1. 조사 방법 및 한계

| 항목 | 내용 |
|------|------|
| Reddit | r/ChatGPT, r/ClaudeAI, r/Bard 등 비교 스레드 및 고득표(~2,000 upvotes) 스레드 인용 기사·요약본 참조 |
| X (Twitter) | 개발자·빌더 커뮤니티 논의, 2026년 전환(Claude 채택) 관련 글 참조 |
| GitHub | Gist 아키텍처 비교, claude-vs-codex 리포, openai/codex Discussions, claude-code-tips 비교 문서 |
| 한계 | 개인 경험·샘플 편향, 모델 버전·요금제 차이, 홍보성 글 혼재 → **정량 순위가 아닌 ‘반복되는 패턴’** 위주로 정리 |

---

## 2. 플랫폼별에서 반복되는 메시지

### Reddit (요약)

- **“하나만 고르지 않고 스택을 쓴다”** — ChatGPT Plus vs Claude Pro 30일 비교 등에서, 만능 칼(ChatGPT) vs 정밀 메스(ChatGPT) 비유가 자주 등장 ([Foxafox Reddit 요약](https://foxafox.com/ai-news/chatgpt-vs-claude-vs-gemini-reddit)).
- **ChatGPT**: 메시지 한도·이미지·음성·웹 검색·기억(메모리) 등 **일상 사용 편의** 호평.
- **Claude**: 긴 글·코드 리뷰·자연스러운 문체, **사용 한도·불안정** 불만도 함께 제기.
- **Gemini**: Google 앱 안에서의 편의는 호평, **코딩·깊은 추론은 약하다**는 의견과 **검색 레이어에 가깝다**는 의견이 공존.

### X / 개발자 커뮤니티 (요약)

- 2025~2026년 **“빌더·개발자층이 Claude로 이동”** 패턴이 여러 글에서 언급 ([Vapvarun](https://vapvarun.com/builder-crowd-chatgpt-to-claude/), [Stackademic](https://blog.stackademic.com/chatgpt-vs-claude-in-2026-which-ai-is-actually-better-for-writing-coding-everyday-tasks-98920173030d)).
- 동시에 **Codex vs Claude Code** 논쟁: 속도·비용·클라우드 위임은 Codex, 코드 품질·확장성은 Claude Code ([CatDoes](https://catdoes.com/blog/claude-code-vs-codex), [Ken Imoto](https://kenimoto.dev/blog/claude-code-vs-chatgpt-codex-official-agents/)).

### GitHub (요약)

| 출처 | 핵심 유저 메시지 |
|------|------------------|
| [Haseeb Qureshi Gist](https://gist.github.com/Haseeb-Qureshi/2213cc0487ea71d62572a645d7582518) | Claude Code=확장성·맥락, Codex=OS 샌드박스 보안, Cline=모델 교체 자유 |
| [rohittcodes/claude-vs-codex](https://github.com/rohittcodes/claude-vs-codex) | Claude=문서·구조·Figma 충실도, Codex=속도·비용·간결함 |
| [openai/codex Discussion #5118](https://github.com/openai/codex/discussions/5118) | 성능 저하·한도 불만 vs “Codex가 여전히 우수” 의견 대립 |
| [anipotts/claude-code-tips](https://github.com/anipotts/claude-code-tips) | Claude=hooks/plugins 생태계, Gemini=무료 티어·보완용 |

---

## 3. 업무별 유저 평가 비교표

| 업무·관점 | ChatGPT (유저 평가) | Gemini (유저 평가) | Claude (유저 평가) |
|-----------|----------------------|-------------------|-------------------|
| **코딩 품질** | 만능·빠른 프로토타입, Codex는 터미널·위임 강점 | 대규모 repo 한 번에 넣기·속도 호평, 가끔 구식 패턴 | **코드 가독성·멀티파일** 우위 의견 다수 |
| **디버깅·설명** | 빠른 수정, 니치 스택·레거시 약간 유리 | 보안·논리 맥락 설명 강점 사례 | **원인 설명·엣지 케이스** 호평 |
| **긴 문서·연구** | Custom GPT·범용 | **긴 PDF·Workspace 연동** 강점 | 긴 초안·구조화 글쓰기 |
| **에이전트·자동화** | Codex 클라우드 PR, AgentKit | Jewels·Antigravity 성장 중 | **Claude Code** 개발자 선호 다수 |
| **일상·멀티모달** | 음성·이미지·플러그인 **최강** | Android·Google 생태 **통합** | 앱에서는 ‘게스트’ 느낌 |
| **불만(공통)** | 요금·한도, 품질 변동 | 코딩 약함·자신만만한 답 | **사용 한도**, 가끔 느림 |

출처 예: [Playcode 코딩 비교](https://playcode.io/blog/chatgpt-vs-claude-vs-gemini-coding-2026), [OneLessHour 30일 테스트](https://onelesshour.com/gemini-vs-chatgpt-2026/), [TechTide 코딩 2026](https://techtidetv.com/blog/claude-vs-chatgpt-for-coding-2026)

---

## 4. 공식 소개 vs 유저 평가 — 차이만 짚기

| 구분 | 공식 자료가 강조 | 유저가 추가로 말하는 것 |
|------|------------------|-------------------------|
| ChatGPT | GPT-5.x, AgentKit, Responses API, 생태계 | “만능”, Codex **속도·비용**, 한도/품질 변동 불만 |
| Gemini | 3.5 Flash 벤치, Google 연동, Managed Agents | **Workspace 편의**는 실감, **코딩·깊은 추론**은 기대 이하 의견도 |
| Claude | Opus/Sonnet, 1M 맥락, Claude Code | **코드 품질 1위** 인상 강함, **한도·속도**가 실사용 병목 |

→ **도입 시**: 공식 기능으로 “할 수 있는지”를 보고, 유저 평가로 “매일 쓸 때 불편한지”를 PoC에서 확인하는 것이 안전합니다.

---

## 5. HW 개발팀 — 유저 평가 기반 선택 힌트

| HW 업무 | 유저들이 많이 쓰는 조합 | 이유 (쉬운 말) |
|---------|-------------------------|----------------|
| 펌웨어·드라이버 초안 | Claude (+ ChatGPT 보조) | “프로덕션 코드” 후기가 Claude에 쏠림 |
| 수백 페이지 데이터시트 | Gemini | “한 번에 긴 문서” 후기 |
| 측정 로그·스크립트·CI | ChatGPT Codex 또는 Claude Code | 터미널·자동화 후기 |
| 문서·보고 초안 | Claude 또는 ChatGPT | 글·구조 vs 만능 |
| 최종 판단 | 사람 | 유저도 “AI는 보조”라고 반복 |

**유저들이 추천하는 실무 패턴**: 복수 도입 — 예) `Claude Code(코딩) + Gemini(문서) + ChatGPT(만능·음성)` ([DEV Playbook](https://dev.to/truongpx396/building-production-grade-fullstack-products-with-ai-coding-agents-a-practical-playbook-2idd), [Kanerika](https://medium.com/@kanerika/chatgpt-vs-gemini-vs-claude-choosing-the-right-ai-for-your-workflow-05e2e6a90d8c))

---

## 6. 출처 (유저 평가 조사)

### Reddit·요약
- https://foxafox.com/ai-news/chatgpt-vs-claude-vs-gemini-reddit  
- https://www.dreamhost.com/blog/chatgpt-vs-gemini/ (Reddit 스레드 인용)

### GitHub
- https://gist.github.com/Haseeb-Qureshi/2213cc0487ea71d62572a645d7582518  
- https://github.com/rohittcodes/claude-vs-codex  
- https://github.com/openai/codex/discussions/5118  
- https://github.com/anipotts/claude-code-tips (comparisons/codex.md, gemini.md)

### X·개발자 커뮤니티·비교 글
- https://vapvarun.com/builder-crowd-chatgpt-to-claude/  
- https://catdoes.com/blog/claude-code-vs-codex  
- https://kenimoto.dev/blog/claude-code-vs-chatgpt-codex-official-agents/  
- https://techtidetv.com/blog/claude-vs-chatgpt-for-coding-2026  
- https://onelesshour.com/gemini-vs-chatgpt-2026/  
- https://playcode.io/blog/chatgpt-vs-claude-vs-gemini-coding-2026  
