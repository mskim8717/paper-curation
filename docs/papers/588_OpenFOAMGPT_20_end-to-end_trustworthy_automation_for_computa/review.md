---
title: "588_OpenFOAMGPT_20_end-to-end_trustworthy_automation_for_computa"
authors:
  - "Jingsen Feng"
  - "Ran Xu"
  - "Xu Chu"
date: "2025.04"
doi: "10.48550/arXiv.2504.19338"
arxiv: ""
score: 4.0
essence: "자연어 쿼리로부터 완전히 자동화된 전산유체역학(CFD) 시뮬레이션을 수행하는 첫 번째 다중 에이전트 LLM 프레임워크를 제안하며, 450개 이상의 시뮬레이션에서 100% 성공률을 달성했다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Agent-Based_CFD_Simulation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2025_OpenFOAMGPT 2.0 end-to-end, trustworthy automation for computational fluid dynamics.pdf"
---

# OpenFOAMGPT 2.0: end-to-end, trustworthy automation for computational fluid dynamics

> **저자**: Jingsen Feng, Ran Xu, Xu Chu | **날짜**: 2025-04-27 | **DOI**: [10.48550/arXiv.2504.19338](https://doi.org/10.48550/arXiv.2504.19338)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The design of multi-Agent framework for CFD. Red components represent user interfaces*

자연어 쿼리로부터 완전히 자동화된 전산유체역학(CFD) 시뮬레이션을 수행하는 첫 번째 다중 에이전트 LLM 프레임워크를 제안하며, 450개 이상의 시뮬레이션에서 100% 성공률을 달성했다.

## Motivation

- **Known**: Large Language Models는 다양한 분야에서 다중 에이전트 시스템으로 활용되고 있으며, CFD는 정확한 수치 사양과 전문성을 요구하는 복잡한 계산 작업이다.
- **Gap**: CFD 시뮬레이션의 높은 진입장벽과 복잡한 워크플로우로 인해 접근성이 제한되어 있으며, LLM을 활용한 자동화된 end-to-end CFD 시뮬레이션 프레임워크가 부족하다.
- **Why**: CFD의 자동화를 통해 과학 컴퓨팅의 접근성을 높이고 생산성을 향상시킬 수 있으며, 신뢰성 높은 다중 에이전트 시스템이 과학 계산의 엄격한 요구 사항을 충족할 수 있음을 입증하는 것이 중요하다.
- **Approach**: Pre-processing, Prompt Generation, OpenFOAMGPT (simulator), Post-processing의 네 개의 특화된 에이전트를 통합하여 자동으로 메시 생성, 시뮬레이션 구성, 실행, 후처리를 수행하는 다중 에이전트 프레임워크를 구성한다.

## Achievement


- **완전 자동화 end-to-end 워크플로우**: 자연어 쿼리로부터 메시 생성, CFD 시뮬레이션 실행, 결과 후처리까지 인간 개입 없이 완전 자동화
- **높은 신뢰성과 재현성**: 450개 이상의 시뮬레이션에서 100% 성공률과 100% 재현성 달성
- **다양한 유동 현상 검증**: Poiseuille 흐름, 단일·다중상 다공질 매질 흐름, 항공역학 분석 등 다양한 케이스 스터디로 검증
- **매개변수 연구 자동화**: 단일 케이스뿐만 아니라 다중 케이스 매개변수 연구를 자동으로 식별하고 실행
- **접근성 개선**: 전문가가 아닌 사용자도 자연언어 인터페이스를 통해 복잡한 CFD 시뮬레이션 수행 가능

## How

![Figure 1](figures/fig1.webp)

*Figure 1: The design of multi-Agent framework for CFD. Red components represent user interfaces*

- Pre-processing Agent: 사용자 쿼리 분석을 통해 단일/다중 케이스 분류, blockMesh 대 snappyHexMesh 메시 전략 자동 선택
- Prompt Generation Agent: 단일 케이스는 직접 쿼리 사용, 다중 케이스는 매개변수 변수를 체계적으로 분해하여 케이스별 프롬프트 생성 및 Prompt Pool에 저장
- OpenFOAMGPT Agent: (1) Configuration Generation - 작업별 요구사항을 OpenFOAM 구성 파일로 매핑, 온도 0으로 설정하여 결정론적 출력 보장, (2) Automated Execution Management - OpenFOAM v2406 Docker 컨테이너에서 시뮬레이션 실행 및 모니터링
- Post-processing Agent: 시뮬레이션 결과를 시각화하고 분석하여 사용자에게 제공
- 자동 오류 수정 루프: 시뮬레이션 실패 시 오류 메시지를 분석하여 자동으로 수정 및 재실행

## Originality

- CFD 분야 최초의 다중 에이전트 LLM 기반 end-to-end 자동화 프레임워크
- 매개변수 연구에서 파일 수정 방식 대신 완전한 프롬프트 재생성 방식 채택으로 OpenFOAM의 엄격한 문법 요구사항 충족
- 온도 0 설정과 시스템 프롬프트 설계를 통해 LLM의 결정론적 고정밀 출력 보장
- 조율된 다중 에이전트 아키텍처를 통해 과학 계산의 zero-tolerance 신뢰성 요구사항 달성

## Limitation & Further Study

- 현재 OpenFOAM에 국한되어 있으며 다른 CFD 소프트웨어로의 확장성 미검증
- 복잡한 기하학적 구조나 고도로 비선형적인 흐름 문제에 대한 성능이 제한적일 수 있음
- 메시 품질 자동 검증 및 최적화 메커니즘 부재
- 사용자가 생성된 구성 파일의 물리적 타당성을 검증할 방법 제공 필요
- **후속 연구**: 다른 CFD 플랫폼 지원, 고급 메시 최적화 에이전트 추가, 물리 기반 오류 검증 메커니즘 개발, 실시간 시뮬레이션 피드백 루프 구현

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CFD의 자동화와 접근성 향상에 대한 실질적이고 검증된 솔루션을 제시하며, 다중 에이전트 LLM 아키텍처가 과학 계산의 엄격한 신뢰성 요구사항을 충족할 수 있음을 입증하는 중요한 기여이다.

## Related Papers

- 🔄 다른 접근: [[papers/559_Mooseagent_A_llm_based_multi-agent_framework_for_automating/review]] — OpenFOAMGPT와 MooseAgent 모두 시뮬레이션 소프트웨어 자동화를 목표로 하지만 각각 CFD와 유한요소법이라는 다른 영역에 특화됨
- 🔗 후속 연구: [[papers/535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD/review]] — MetaOpenFOAM의 다중 에이전트 CFD 프레임워크가 OpenFOAMGPT 2.0의 자동화 접근법을 더 체계적인 에이전트 시스템으로 발전시킴
- 🏛 기반 연구: [[papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/review]] — OpenFOAMGPT 1.0의 RAG 기반 접근법이 2.0 버전의 엔드투엔드 자동화 시스템 개발의 기술적 기반
- 🔄 다른 접근: [[papers/535_MetaOpenFOAM_an_LLM-based_multi-agent_framework_for_CFD/review]] — CFD 자동화라는 동일한 목표를 가지지만 MetaOpenFOAM은 다중 에이전트 접근에, OpenFOAMGPT 2.0은 신뢰성 있는 종단간 자동화에 집중한 다른 방법론임
- 🔄 다른 접근: [[papers/559_Mooseagent_A_llm_based_multi-agent_framework_for_automating/review]] — MooseAgent와 OpenFOAMGPT 모두 엔지니어링 시뮬레이션 자동화를 목표로 하지만 각각 유한요소법과 전산유체역학이라는 다른 도메인에 특화됨
- 🔗 후속 연구: [[papers/589_OpenFOAMGPT_A_retrieval-augmented_large_language_model_LLM_a/review]] — OpenFOAMGPT 2.0의 종단간 신뢰성 있는 자동화가 기존 OpenFOAMGPT의 기능을 확장한다.
