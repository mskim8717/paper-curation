---
title: "586_Opendevin_An_open_platform_for_ai_software_developers_as_gen"
authors:
  - "Chia-Tung Ho"
  - "Haoxing Ren"
  - "Brucek Khailany"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "OpenHands는 AI 소프트웨어 개발자 에이전트를 위한 오픈 플랫폼으로, 에이전트가 코드 작성, 커맨드라인 상호작용, 웹 브라우징을 통해 인간 개발자처럼 세계와 상호작용할 수 있게 한다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ho et al._2024_Opendevin An open platform for ai software developers as generalist agents.pdf"
---

# Opendevin: An open platform for ai software developers as generalist agents

> **저자**: Chia-Tung Ho, Haoxing Ren, Brucek Khailany | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2407.16741](https://arxiv.org/abs/2407.16741)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

OpenHands는 AI 소프트웨어 개발자 에이전트를 위한 오픈 플랫폼으로, 에이전트가 코드 작성, 커맨드라인 상호작용, 웹 브라우징을 통해 인간 개발자처럼 세계와 상호작용할 수 있게 한다.

## Motivation

- **Known**: LLM 기반 AI 에이전트의 발전으로 소프트웨어 개발, 웹 네비게이션 등 복잡한 작업이 가능해졌다. 다양한 오픈소스 에이전트 프레임워크들이 개발되고 있다.
- **Gap**: 기존 에이전트 프레임워크들은 소프트웨어 개발에 필요한 복잡한 코드 작성 및 수정, 온더플라이 정보 수집, 안전한 실행 환경을 종합적으로 지원하지 못한다. 여러 에이전트의 협력 메커니즘과 표준화된 평가 프레임워크도 부족하다.
- **Why**: 소프트웨어는 인간이 세계와 상호작용하는 가장 강력한 도구이며, AI 에이전트가 인간 개발자처럼 소프트웨어를 통해 작업할 수 있다면 AI의 실질적 영향력을 크게 향상시킬 수 있다.
- **Approach**: event stream 기반 아키텍처로 에이전트, 사용자, 환경 간 상호작용을 추상화하고, Docker 샌드박스 환경에서 IPython, Bash, 웹 브라우저(Playwright)를 제공한다. CodeAct 기반 generalist 에이전트와 다양한 specialist 에이전트를 구현하며, 15개 벤치마크로 평가한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

- **Event Stream 아키텍처**: 모든 Action과 Observation을 시간순으로 추적하여 에이전트, UI, 환경 간 유연하고 강력한 상호작용을 제공
- **포괄적 런타임 환경**: Docker 샌드박스, IPython 서버, Bash 셸, Playwright 브라우저를 통합하여 소프트웨어 개발에 필요한 전체 인터페이스 제공
- **다중 액션 지원**: IPythonRunCellAction, CmdRunAction, BrowserInteractiveAction으로 코드 실행, 시스템 명령, 웹 브라우징을 모두 지원
- **Multi-Agent 위임**: 여러 전문 에이전트가 협력하여 복잡한 작업을 해결할 수 있는 메커니즘 제공
- **포괄적 평가 프레임워크**: SWE-BENCH, WEBARENA 등 15개 벤치마크를 포함한 표준화된 평가 체계
- **강한 커뮤니티 기반**: MIT 라이선스로 공개되었으며 188명 이상의 기여자로부터 2.1K+ contributions, 32K GitHub stars 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

- State 데이터 구조로 event stream(과거 action-observation 쌍), LLM 호출 누적 비용, multi-agent 위임 메타데이터 등을 관리
- IPythonRunCellAction과 CmdRunAction으로 샌드박스 환경에서 임의의 Python 코드와 Bash 명령 실행
- BrowserInteractiveAction으로 BrowserGym의 domain-specific language를 이용한 웹 브라우싱
- CodeAct 기반 generalist 에이전트 구현에 웹 브라우징(ServiceNow) 및 코드 편집 specialist(Yang et al., 2024) 추가
- Agent 클래스의 reset() 메서드와 step(state) 메서드로 간단하게 새로운 에이전트 구현 가능하도록 설계
- Chat 기반 사용자 인터페이스로 에이전트 액션을 시각화하고 실시간 피드백 제공
- Docker 이미지에 OpenHands action execution API를 자동 설치하여 다양한 환경 지원

## Originality

- 소프트웨어 개발을 AI 에이전트의 중심 인터페이스로 하는 설계는 기존 챗봇이나 API 기반 에이전트와 차별화됨
- Event stream 기반 상태 관리는 action-observation 쌍의 완전한 추적으로 다양한 분석과 multi-agent 위임을 가능하게 함
- IPython, Bash, 브라우저를 통합한 포괄적 런타임 환경은 실제 소프트웨어 개발 워크플로우를 충실히 재현
- Programming language를 기반으로 한 액션 설계로 다양한 도구(Python 함수, REST API 등)를 유연하게 통합 가능

## Limitation & Further Study

- 평가가 주로 SWE-BENCH, WEBARENA 등 제한된 벤치마크 세트에 기반하며, 실제 복잡한 소프트웨어 프로젝트에서의 성능은 미검증
- Docker 샌드박스 환경의 리소스 제약과 네트워크 접근 제한이 실제 개발 작업의 제약이 될 수 있음
- Multi-agent 위임의 구체적 메커니즘과 에이전트 간 협력 방식에 대한 상세 설명이 부족함
- 에이전트의 일반화 능력과 새로운 작업 유형에 대한 적응성에 대한 체계적 분석 필요
- **후속 연구**: 더 복잡한 real-world 소프트웨어 프로젝트에 대한 평가, multi-agent 협력 전략의 최적화, 안전성과 보안 측면의 강화, 장시간 실행 작업에 대한 안정성 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: OpenHands는 AI 에이전트가 인간 소프트웨어 개발자처럼 동작하도록 하는 통합 플랫폼으로, event stream 기반 아키텍처와 포괄적 런타임 환경의 설계가 우수하며, 강한 커뮤니티 기반의 실용적인 오픈소스 프로젝트로서 AI 에이전트 연구의 중요한 인프라가 될 가능성이 높다.

## Related Papers

- 🔄 다른 접근: [[papers/590_Openhands_An_open_platform_for_ai_software_developers_as_gen/review]] — OpenDevin과 OpenHands는 동일한 AI 소프트웨어 개발자 플랫폼이지만 서로 다른 버전과 구현 세부사항을 가짐
- 🔗 후속 연구: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — OpenDevin의 범용 개발 플랫폼이 MLDebugging의 특화된 디버깅 작업을 포괄적인 소프트웨어 개발로 확장함
- 🏛 기반 연구: [[papers/205_Chatdev_Communicative_agents_for_software_development/review]] — ChatDev의 다중 에이전트 소프트웨어 개발 연구가 OpenDevin 플랫폼의 에이전트 협력 방식의 기초를 제공함
- 🏛 기반 연구: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — OpenDevin의 범용 소프트웨어 개발 플랫폼이 MLDebugging 같은 특화된 디버깅 벤치마크의 평가 환경 기반을 제공함
- 🔄 다른 접근: [[papers/1098_BloClaw_An_Omniscient_Multi-Modal_Agentic_Workspace_for_Next/review]] — AI 소프트웨어 개발자를 위한 오픈 플랫폼과 AI 과학자를 위한 멀티모달 워크스페이스라는 서로 다른 AI 개발 환경을 제시한다
- 🔄 다른 접근: [[papers/590_Openhands_An_open_platform_for_ai_software_developers_as_gen/review]] — OpenHands와 OpenDevin은 동일한 목적의 AI 개발자 플랫폼이지만 서로 다른 구현과 아키텍처 선택을 보여줌
