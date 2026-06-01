# 외부 AI 3종 비교 조사 (ChatGPT · Gemini · Claude)

> 작성 목적: 2026년 6월 외부 AI 도입 검토 전, 각 LLM의 강점·차별화 파악  
> 대상: 삼성전자 스마트폰 HW 개발팀 보고용  
> 조사 기준일: 2026년 6월  
> 조사 방법: 각사 공식 문서(1차) + 웹 사용기·비교 리뷰(2차, 참고)

---

## 1. 한 줄 포지셔닝

| AI | 한 줄 요약 | 공식 근거 |
|----|-----------|-----------|
| **ChatGPT** | 복잡한 추론·코딩·에이전트까지 아우르는 **만능형**, 생태계·도구 연결이 가장 넓음 | [OpenAI Models](https://developers.openai.com/api/docs/models), [AgentKit](https://openai.com/index/introducing-agentkit/) |
| **Gemini** | **Google 연동·긴 문서·검색·멀티모달**에 강하고, 에이전트·코딩 속도·비용 효율을 강조 | [Gemini 3.5 발표](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/), [Gemini API](https://ai.google.dev/gemini-api/docs) |
| **Claude** | **프로덕션 코딩·장기 에이전트 작업·긴 맥락**에 특화, 코드 품질·구조화 출력 강점 | [Claude Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) |

---

## 2. 공식 기능 비교 (2026년 6월 기준)

| 비교 항목 | ChatGPT (OpenAI) | Gemini (Google) | Claude (Anthropic) |
|-----------|------------------|-----------------|---------------------|
| 대표 모델 | GPT-5.5 (플래그십), GPT-5.4-mini/nano | Gemini 3.5 Flash (GA), 3.5 Pro 예정 | Opus 4.6/4.7, Sonnet 4.6, Haiku 4.5 |
| 맥락 길이 | 최대 약 100만 토큰 (GPT-5.5) | 100만 토큰급 (모델·제품별 상이) | Opus/Sonnet 4.6: 최대 100만 토큰 |
| 코딩·추론 | 공식: 복잡 추론·코딩 권장 모델 | 공식: 에이전트·코딩 벤치 상위 (3.5 Flash) | 공식: 복잡 추론·장기 에이전트 코딩 특화 |
| 에이전트 | AgentKit, Responses API, Computer Use, MCP | Managed Agents, Antigravity, Interactions API | Claude Code, Agent SDK, Skills, 도구 호출 |
| 문서·검색 | Web search, File search | Google Search 그라운딩, File Search, URL Context | Web search/fetch, PDF 입력, 구조화 출력 |
| 멀티모달 | 텍스트·이미지 입력, 이미지·음성 등 전용 모델 | 멀티모달·영상 등 확장 (제품별) | 텍스트·이미지·PDF |
| 엔터프라이즈 | Connector Registry, Evals, Enterprise 티어 | Gemini Enterprise, Agent Platform | AWS Bedrock, Vertex AI, Microsoft Foundry |

※ 상세 스펙·가격은 도입 시점에 공식 페이지 재확인 필요.

---

## 3. 사용자 평가 요약 (웹, 참고)

> **상세본**: Reddit·X·GitHub 중심 유저 후기는 [외부AI_3종_유저평가_비교조사.md](외부AI_3종_유저평가_비교조사.md) 참조.  
> 아래는 요약이며, 벤치마크 수치는 출처·측정 방식마다 다를 수 있음.

| 관점 | ChatGPT | Gemini | Claude |
|------|---------|--------|--------|
| 코딩 품질 | 만능·Codex 속도·위임, DevOps·프로토타입 | 대규모 repo·속도, 코딩은 평가 엇갈림 | **코드 가독성·멀티파일** 우위 의견 다수 |
| 긴 문서 | Custom GPT·범용 | **Workspace·긴 PDF** 강점 | 긴 글·구조화·코드 리뷰 |
| 에이전트 | Codex 클라우드 PR, AgentKit | Antigravity·Jewels 성장 | **Claude Code** 개발자 선호 |
| 불만(공통) | 한도·품질 변동 | “검색형”, 코딩 약함 의견 | **사용 한도**, 느릴 때 있음 |

**유저 공통 패턴**: 하나만 쓰기보다 **역할 분담 스택**(예: Claude 코딩 + Gemini 문서 + ChatGPT 만능).

참고 URL:
- [Reddit 요약 (Foxafox)](https://foxafox.com/ai-news/chatgpt-vs-claude-vs-gemini-reddit)
- [GitHub Gist: 에이전트 아키텍처](https://gist.github.com/Haseeb-Qureshi/2213cc0487ea71d62572a645d7582518)
- [Kanerika 2026 workflow](https://medium.com/@kanerika/chatgpt-vs-gemini-vs-claude-choosing-the-right-ai-for-your-workflow-05e2e6a90d8c)

---

## 4. 스마트폰 HW 개발팀 적용 시사점

| 업무 | 추천 우선 검토 | 이유 (쉬운 설명) |
|------|----------------|------------------|
| 펌웨어·드라이버 코드 초안 | Claude, ChatGPT | 코드 구조·주석 품질 평가가 높음 (참고) |
| 긴 데이터시트·사양서 요약 | **Gemini** | 긴 문서·검색 연동이 공식 강점 |
| 측정 로그·표·그래프 정리 | 3종 모두 가능 | 반복 정리 작업은 모두 활용 가능 |
| 스캔 PDF·회로도 글자 읽기(OCR) | **Gemini** (공식 사례) | Google 발표에서 OCR·문서 추론 사례 (Ramp 등) |
| 다단계 에이전트 자동화 | ChatGPT, Claude | AgentKit / Claude Code 등 공식 에이전트 도구 |
| 최종 회로·양산 판단 | **사람** | AI는 보조, 실측·검증 필수 |

---

## 5. 결론 및 제언

### 당장 적용 가능 (PoC 후보)
- 코드·문서 **초안** 작성, 측정 데이터 정리, 로그 분석, 반복 업무 자동화

### 신중 적용
- 부품 최종 선정, 불량 원인 확정, 회로·타이밍 최종 판단, 양산 영향 평가

### 도입 시 선택 가이드 (업무별)
- **코딩 품질·리팩터링 중심** → Claude 우선 검토  
- **Google 문서·검색·긴 사양서** → Gemini 우선 검토  
- **범용·에이전트·도구 연결 폭** → ChatGPT 우선 검토  
- 실무에서는 **복수 도입·역할 분담**이 일반적 (엔터프라이즈 설문에서 다중 모델 사용 증가, 참고)

### 사내 Gauss와의 관계
- **Gauss**: 보안·망분리 환경의 사내 보조  
- **외부 3종**: 외부 도구·최신 자료·고급 에이전트가 필요한 업무 (보안·법무 검토 후)

---

## 6. 출처 (공식)

1. OpenAI Models — https://developers.openai.com/api/docs/models  
2. OpenAI Changelog — https://developers.openai.com/api/docs/changelog  
3. Introducing AgentKit — https://openai.com/index/introducing-agentkit/  
4. Gemini 3.5 Blog — https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/  
5. Gemini API Docs — https://ai.google.dev/gemini-api/docs  
6. Gemini Enterprise Capabilities — https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/supported-capabilities  
7. Claude Models Overview — https://platform.claude.com/docs/en/about-claude/models/overview  
8. Anthropic — https://www.anthropic.com/
