---
title: "590_Openhands_An_open_platform_for_ai_software_developers_as_gen"
authors:
  - "Xingyao Wang"
  - "Boxuan Li"
  - "Yufan Song"
  - "Frank F. Xu"
  - "Xiangru Tang"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "OpenHands는 AI 에이전트가 소프트웨어 개발자처럼 코드 작성, 커맨드라인 상호작용, 웹 브라우징을 통해 환경과 상호작용할 수 있는 오픈소스 플랫폼이다. Event stream 기반 아키텍처와 Docker 샌드박스 환경을 제공하며 15개 벤치마크로 평가된다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/AI_Human_Science_Collaboration"
  - "sub/Multi-Agent_System_Design"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_Openhands An open platform for ai software developers as generalist agents.pdf"
---

# Openhands: An open platform for ai software developers as generalist agents

> **저자**: Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2407.16741](https://arxiv.org/abs/2407.16741)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

OpenHands는 AI 에이전트가 소프트웨어 개발자처럼 코드 작성, 커맨드라인 상호작용, 웹 브라우징을 통해 환경과 상호작용할 수 있는 오픈소스 플랫폼이다. Event stream 기반 아키텍처와 Docker 샌드박스 환경을 제공하며 15개 벤치마크로 평가된다.

## Motivation

- **Known**: 최근 LLM 기반 AI 에이전트들이 소프트웨어 개발, 웹 네비게이션 등 복잡한 작업을 수행할 수 있게 발전했다. 기존 에이전트 프레임워크들은 함수 호출, 환경 인터페이스, 인간-에이전트 상호작용을 제공한다.
- **Gap**: 인간 개발자처럼 소프트웨어 개발 시 복잡한 코드 생성·수정, 온디맨드 정보 수집, 안전한 실행 환경 보장이 동시에 필요하지만 이를 통합한 플랫폼이 부족하다. 다중 에이전트 협력 및 종합적 평가 벤치마크도 미흡하다.
- **Why**: 소프트웨어는 인간이 세계와 상호작용하는 가장 강력한 도구이므로, AI 에이전트가 개발자처럼 작동할 수 있으면 복잡한 실제 문제 해결이 가능해진다. 통합 플랫폼을 제공하면 연구자와 실무자들이 에이전트 개발·평가를 체계적으로 수행할 수 있다.
- **Approach**: Event stream 기반 상태 관리로 행동-관찰 히스토리를 추적하고, Docker 샌드박스(Bash, IPython, Playwright 브라우저)에서 에이전트가 실행 가능한 작업을 수행하도록 설계했다. CodeAct 아키텍처를 기반으로 일반화 능력을 갖춘 다중 에이전트 위임 메커니즘을 구현했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

- **통합 플랫폼 설계**: Event stream 기반 아키텍처로 agents, runtime, UI를 유연하게 연결하며 188명 이상의 기여자로부터 2.1K 이상의 커밋을 받은 커뮤니티 프로젝트
- **포괄적 상호작용 인터페이스**: IPythonRunCellAction, CmdRunAction, BrowserInteractiveAction을 통해 코드 실행, 커맨드 실행, 웹 브라우징을 단일 프레임워크로 통합
- **안전한 실행 환경**: Docker 샌드박스 기반 격리 실행 환경으로 시스템 안전성 보장
- **다중 에이전트 협력**: Multi-agent delegation 메커니즘으로 특화된 에이전트들의 협력 작업 지원
- **종합 평가 프레임워크**: SWE-BENCH, WebArena 등 15개 벤치마크 통합으로 다양한 작업 평가 가능
- **실제 구현**: 10개 이상의 구현된 에이전트(CodeAct 기반 일반화 에이전트 포함)와 즉시 사용 가능한 구현체 제공

## How

![Figure 2](figures/fig2.webp)

*Figure 2: OpenHands consists of 3 main components: 1) Agent abstraction where community can*

- State는 event stream(시간순 행동-관찰), LLM 비용, 멀티 에이전트 메타데이터 등을 포함하는 데이터 구조로 정의
- IPythonRunCellAction과 CmdRunAction으로 Docker 샌드박스 내 Python 코드 및 Bash 명령 실행
- BrowserInteractiveAction으로 BrowserGym의 도메인 특화 언어를 사용한 웹 브라우징 지원
- 각 Action 실행 후 Observation 반환으로 event stream에 추가하는 action-observation 사이클 구현
- 사용자 제공 Docker 이미지에 자동으로 action execution API 설치
- Chat 기반 UI로 실시간 피드백 제공 (파일 뷰, 실행 커맨드, 브라우저 활동 시각화)
- Agent 구현은 reset() 메서드(시스템 메시지 설정)와 step() 메서드(state → action 변환)로 최소화

## Originality

- Programming language 기반 action space가 일관된 인터페이스로 다양한 도구(Python, REST API 등)를 유연하게 지원하는 CodeAct 영감의 설계
- Event stream으로 전체 상호작용 이력을 불변 형태로 추적하여 재현성과 디버깅 용이성 확보
- Docker 샌드박스와 자동 API 설치로 임의의 사용자 이미지 지원 가능한 확장성
- Multi-agent delegation 메커니즘이 특화된 에이전트 조합을 동적으로 구성 가능
- 15개 벤치마크를 단일 프레임워크에 통합한 종합적 평가 접근

## Limitation & Further Study

- 현재 평가는 15개 벤치마크로 제한되며, 실제 장기 소프트웨어 프로젝트에서의 성능은 미평가
- Sandbox 환경이 네트워크 접근, 외부 라이브러리 설치 등의 제약이 있을 수 있음
- 웹 브라우징의 경우 동적 JavaScript 렌더링이나 복잡한 인터랙션 처리의 한계
- 에이전트 성능이 기저 LLM 모델의 능력에 크게 의존하며, 모델별 성능 편차 분석 부족
- **후속 연구**: 더 큰 규모의 실제 소프트웨어 프로젝트로 장기 평가, 에이전트 간 협력 최적화 알고리즘, 자가 학습 및 개선 메커니즘 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: OpenHands는 AI 에이전트가 실제 소프트웨어 개발자처럼 작동할 수 있는 통합 플랫폼으로, Event stream 기반 설계와 Docker 샌드박스를 통해 안전하고 유연한 실행 환경을 제공한다. 188명 이상의 기여자를 보유한 활발한 오픈소스 커뮤니티이며, 15개 벤치마크로 체계적 평가가 가능해 AI 에이전트 연구의 중요한 기반으로 기여할 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/586_Opendevin_An_open_platform_for_ai_software_developers_as_gen/review]] — OpenHands와 OpenDevin은 동일한 목적의 AI 개발자 플랫폼이지만 서로 다른 구현과 아키텍처 선택을 보여줌
- 🔗 후속 연구: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — OpenHands 플랫폼이 SWE-bench의 GitHub 이슈 해결을 더 포괄적인 소프트웨어 개발 작업으로 확장함
- 🏛 기반 연구: [[papers/205_Chatdev_Communicative_agents_for_software_development/review]] — ChatDev의 커뮤니케이션 기반 다중 에이전트 개발이 OpenHands의 에이전트 상호작용 설계의 방법론적 토대
- 🏛 기반 연구: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — OpenHands의 개발자 에이전트 플랫폼이 다중 라이브러리 디버깅 벤치마크의 실행 및 평가 인프라를 제공함
- 🔗 후속 연구: [[papers/849_UI-TARS_Pioneering_Automated_GUI_Interaction_with_Native_Age/review]] — 오픈소스 플랫폼으로 GUI 에이전트 개발을 확장하고 민주화한다.
- 🧪 응용 사례: [[papers/327_Experiential_co-learning_of_software-developing_agents/review]] — AI 소프트웨어 개발자를 위한 오픈 플랫폼 연구가 경험적 협력학습 프레임워크를 실제 소프트웨어 개발에 적용한 사례다
- 🔄 다른 접근: [[papers/586_Opendevin_An_open_platform_for_ai_software_developers_as_gen/review]] — OpenDevin과 OpenHands는 동일한 AI 소프트웨어 개발자 플랫폼이지만 서로 다른 버전과 구현 세부사항을 가짐
- 🔄 다른 접근: [[papers/416_Hyperagent_Generalist_software_engineering_agents_to_solve_c/review]] — 소프트웨어 개발 에이전트라는 동일한 목표를 가지지만 HyperAgent는 멀티에이전트 구조에, OpenHands는 오픈 플랫폼 접근에 집중한 다른 방법론임
