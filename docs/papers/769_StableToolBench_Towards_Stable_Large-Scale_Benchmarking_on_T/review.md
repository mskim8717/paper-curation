---
title: "769_StableToolBench_Towards_Stable_Large-Scale_Benchmarking_on_T"
authors:
  - "Zhicheng Guo"
  - "Sijie Cheng"
  - "Hao Wang"
  - "Shihao Liang"
  - "Yujia Qin"
date: "2025.03"
doi: "10.48550/arXiv.2403.07714"
arxiv: ""
score: 4.3
essence: "대규모 언어 모델(LLM)이 도구를 활용하는 능력을 평가하기 위해 안정적인 벤치마크가 필수적인데, 기존 ToolBench는 실시간 API의 불안정성으로 인해 결과 재현성이 떨어진다. 본 논문은 가상 API 서버와 안정적인 평가 시스템을 통해 이 문제를 해결한 StableToolBench를 제안한다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Retrieval-Augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Guo et al._2025_StableToolBench Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models.pdf"
---

# StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models

> **저자**: Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, Yang Liu | **날짜**: 2025-03-05 | **DOI**: [10.48550/arXiv.2403.07714](https://doi.org/10.48550/arXiv.2403.07714)

---

## Essence

![Figure 1](figures/fig1.webp)
*ToolBench에서 보고된 성능과 재현된 성능의 비교: 몇 개월 후 동일한 설정에서 재현했을 때 상당한 성능 저하 발생*

대규모 언어 모델(LLM)이 도구를 활용하는 능력을 평가하기 위해 안정적인 벤치마크가 필수적인데, 기존 ToolBench는 실시간 API의 불안정성으로 인해 결과 재현성이 떨어진다. 본 논문은 가상 API 서버와 안정적인 평가 시스템을 통해 이 문제를 해결한 StableToolBench를 제안한다.

## Motivation

- **Known**: 기존 도구 학습 벤치마크는 손으로 만든 소규모 도구 또는 대규모 온라인 API를 사용. 대규모 API 기반 벤치마크(ToolBench)는 실제 시나리오에 더 가깝지만 안정성이 떨어짐.

- **Gap**: ToolBench 논문 발표 후 몇 개월이 지나자 동일한 조건에서도 성능을 재현할 수 없음(Figure 1). API 상태 변화(44.4%만 작동), 평가자(GPT-3.5)의 판단 불일치 등으로 인한 높은 변동성.

- **Why**: 벤치마크는 시간이 지나도 안정적이어야 하고 모델 성능이 비교 가능해야 함. API 불안정성(55.6%의 API가 신뢰성 부족)과 평가 시스템의 약한 판별력이 근본 원인.

- **Approach**: 실시간 API 호출 대신 (1) 캐싱 시스템으로 이전 결과 저장, (2) LLM 기반 API 시뮬레이터로 누락된 API 모방, (3) GPT-4 기반 개선된 평가 지표(SoPR, SoWR) 도입.

## Achievement

![Figure 3](figures/fig3.webp)
*ToolBench의 API 상태 변화: 성공 44.4%, 연결 불가 14.8%, 파싱 오류 25.9% 등*

1. **안정적 벤치마크 구축**: 가상 API 서버(캐싱 + 시뮬레이터)와 개선된 평가 시스템으로 API 변화에 강건한 평가 환경 제공

2. **성능 안정성 입증**: Figure 4에서 API 실패율이 증가해도 새로운 평가 지표는 일관된 결과 유지(기존 방식은 10-50% API 실패 시 5-25% 성능 저하)

3. **평가 시스템 개선**: GPT-3.5의 판별 불가 문제(Table 1의 "Unsure" 항목)를 GPT-4로 대체하여 안정성 향상

## How

![Figure 2](figures/fig2.webp)
*ToolBench의 Pass Rate 평가 방식: "Unsure" 상태에서 임의 결정으로 인한 불안정성*

**가상 API 서버 (Virtual API Server)**
- **캐싱 시스템**: 카테고리, 도구, API 이름, 인자로 구성된 키를 사용하여 API 응답 저장. 첫 번째 우선순위는 캐시 조회
- **API 시뮬레이터**: 캐시 미스 시 LLM(GPT-4)에 API 문서와 몇 가지 실제 예시를 제공하여 API 동작 모방
- **호출 규칙**: 캐시 → 실시간 API 호출 → 시뮬레이터 순서로 진행

**안정적 평가 시스템 (Stable Evaluation System)**
- **SoPR (Solvable Pass Rate)**: 먼저 GPT-4로 작업이 해결 가능한지 판단한 후, 해결 가능한 작업에 대해서만 Pass Rate 계산
- **SoWR (Solvable Win Rate)**: 두 모델의 성능을 해결 가능한 작업 범위에서만 비교
- **평가자 업그레이드**: GPT-3.5 대신 GPT-4 사용으로 "Unsure" 상태 제거

## Originality

- **첫 번째 캐싱 + 시뮬레이션 하이브리드 접근**: 기존 벤치마크는 실시간 API 또는 모의 API만 사용했으나, 두 가지를 결합하여 안정성과 현실성 균형

- **정량적 안정성 분석**: ToolBench의 불안정성을 체계적으로 분석(성능, 평가, API 상태 3개 차원)하고 실증적 증거 제시

- **"해결 가능한" 기반 메트릭 설계**: 기존 Pass/Win Rate의 개념적 문제(Unsure 상태의 임의 결정)를 근본적으로 해결하는 새로운 평가 지표

## Limitation & Further Study

- **캐시 범위 제한**: 벤치마크의 제한된 쿼리로는 캐시가 충분하지만, 새로운 쿼리 추가 시 시뮬레이터 정확도에 의존 (LLM 시뮬레이터의 완벽성 보증 불가)

- **LLM 의존성**: API 시뮬레이터와 평가자 모두 LLM(GPT-4) 기반이므로, GPT-4의 가용성과 비용이 지속적 이슈. GPT-4 버전 변화 시 다시 불안정화 가능성

- **도메인 특화성 부족**: 금융, 의료 등 고위험 도메인에서는 시뮬레이션된 API 응답의 신뢰성이 중요한데, 검증 방법 제시 부족

- **후속 연구**: (1) 시뮬레이터 정확도 향상을 위한 더 나은 프롬프팅 전략, (2) 오픈소스 LLM 기반 평가자 개발, (3) 실제 API 변화에 대한 장기 추적 평가

## Evaluation

- **Novelty**: 4/5 — 캐싱과 시뮬레이션의 결합은 창의적이나, 각 요소 자체는 기존 아이디어의 응용

- **Technical Soundness**: 4/5 — 실증적 분석과 설계가 타당하나, 시뮬레이터의 정확도 검증 방법론이 제한적

- **Significance**: 4/5 — 도구 학습 벤치마크의 실질적 문제 해결로 커뮤니티에 즉시 가치 제공. 다만 범용성은 ToolBench 기반으로 제한

- **Clarity**: 5/5 — 문제 정의부터 해결책까지 명확하게 구조화. 다양한 실증 데이터로 주장 뒷받침

- **Overall**: 4.3/5

**총평**: StableToolBench는 기존 대규모 도구 학습 벤치마크의 재현성 위기에 대한 실질적이고 효과적인 해결책을 제시한다. 특히 API 불안정성과 평가 시스템의 약점을 동시에 해결한 점이 가치 있으나, LLM 기반 시뮬레이터의 신뢰성 검증과 장기 안정성 보장 측면에서 보완이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/717_Scienceboard_Evaluating_multimodal_autonomous_agents_in_real/review]] — 안정적인 도구 학습 벤치마크가 과학 에이전트의 멀티모달 워크플로우 평가 신뢰성 확보에 직접 활용됨
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 일반적인 기계학습 에이전트 벤치마크가 과학 도구 사용에 특화된 안정적 평가로 확장됨
- 🏛 기반 연구: [[papers/268_Democratizing_AI_scientists_using_ToolUniverse/review]] — 안정적인 대규모 벤치마킹이 AI 과학자 시스템 구축의 기반을 제공한다.
- 🏛 기반 연구: [[papers/717_Scienceboard_Evaluating_multimodal_autonomous_agents_in_real/review]] — 과학 에이전트 평가의 신뢰성을 위해 안정적인 대규모 벤치마킹 방법론이 필수적임
- 🏛 기반 연구: [[papers/496_LLM_Agents_Making_Agent_Tools/review]] — 대규모 도구 사용 벤치마킹을 통해 과학 논문에서 도구를 자동 생성하는 ToolMaker의 성능 평가 기준과 안정성 검증 방법을 제공함
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 안정적인 대규모 벤치마킹이 LLM 도구 활용 능력 평가의 기반 인프라를 제공한다.
- 🔗 후속 연구: [[papers/815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R/review]] — 대규모 도구 사용 벤치마크의 안정성을 다루어 ToolLLM의 대규모 도구 마스터링 능력을 더 신뢰할 수 있고 일관된 성능으로 발전시킴
- 🔄 다른 접근: [[papers/101_AnyTool_Self-Reflective_Hierarchical_Agents_for_Large-Scale/review]] — 안정적인 대규모 벤치마킹과 계층적 API 검색은 도구 사용 에이전트의 서로 다른 평가 접근법을 제시한다
