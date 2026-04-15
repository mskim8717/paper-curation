---
title: "356_From_individual_to_society_A_survey_on_social_simulation_dri"
authors:
  - "Xinyi Mou"
  - "Xuanwen Ding"
  - "Qi He"
  - "Liang Wang"
  - "Jingcong Liang"
date: "2024"
doi: "미공개"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM) 기반 에이전트를 활용하여 개별 인간 행동부터 복잡한 사회 역학까지 다층적으로 시뮬레이션하는 포괄적인 체계를 제시한다. 이 논문은 개인 수준의 정교한 모델링에서 사회 규모의 다양한 상호작용까지 진행하는 시뮬레이션의 발전 과정을 체계적으로 분류하고 분석한다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Mou et al._2024_From individual to society A survey on social simulation driven by large language model-based agent.pdf"
---

# From individual to society: A survey on social simulation driven by large language model-based agents

> **저자**: Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun, Jiayu Lin, Jie Zhou, Xuanjing Huang, Zhongyu Wei | **날짜**: 2024 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: LLM 기반 에이전트에 의한 시뮬레이션. 개인 시뮬레이션, 시나리오 시뮬레이션, 사회 시뮬레이션으로 분류*

대규모 언어 모델(LLM) 기반 에이전트를 활용하여 개별 인간 행동부터 복잡한 사회 역학까지 다층적으로 시뮬레이션하는 포괄적인 체계를 제시한다. 이 논문은 개인 수준의 정교한 모델링에서 사회 규모의 다양한 상호작용까지 진행하는 시뮬레이션의 발전 과정을 체계적으로 분류하고 분석한다.

## Motivation

- **Known**: 
  - 전통적 사회학 연구는 실제 인간 참여에 의존하지만 비용이 높고 확장성이 제한적이며 윤리적 문제가 존재
  - LLM은 인간 수준의 추론과 계획 능력을 보유하고 있음

- **Gap**: 
  - LLM 기반 에이전트를 활용한 시뮬레이션 연구가 급속히 확대되고 있으나, 개인 시뮬레이션부터 사회 시뮬레이션까지 통합적으로 다루는 체계적 리뷰가 부재

- **Why**: 
  - 개별 에이전트부터 다중 에이전트 상호작용까지의 계층적 발전 과정을 이해할 필요
  - 정책 수립과 사회 관리 등 실제 응용 분야에서 활용 가능한 통합 프레임워크 필요

- **Approach**: 
  - 시뮬레이션을 개인, 시나리오, 사회 수준 세 가지로 분류하여 아키텍처, 구성 방식, 평가 방법론을 체계적으로 정리

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 개인 시뮬레이션 청사진. 프로필, 메모리, 계획, 액션 모듈로 구성된 에이전트 아키텍처*

1. **삼층적 시뮬레이션 체계 구축**: 
   - 개인 시뮬레이션(특정 개인/인구통계학적 집단 모방)
   - 시나리오 시뮬레이션(소프트웨어 개발, 논문 검토 등 목표 기반 협업)
   - 사회 시뮬레이션(의견 역학, 거시경제 현상 등 대규모 복잡 현상)

2. **포괄적 분류 체계**: 
   - 에이전트 아키텍처: 프로필, 메모리, 계획, 액션의 4가지 핵심 모듈
   - 구성 방법: 프롬프팅(prompt engineering), 학습(파인튜닝, 강화학습)
   - 목표 분류: 캐릭터 기반(파라메트릭/비파라메트릭) 및 인구통계학적 특성
   - 평가 방식: 정적 평가(객관적/주관적), 상호작용 평가

3. **실증적 데이터 제공**: 
   - 개인 시뮬레이션 관련 84개 논문의 아키텍처, 구성 방식, 메모리 타입, 계획 전략, 평가 방법을 상세 표로 정리
   - 시나리오 및 사회 시뮬레이션 연구의 구성 요소와 평가 메트릭 분류

## How

![Figure 2](figures/fig2.webp)
*그림 2: 개인 시뮬레이션 청사진 - 아키텍처 구성과 평가 방법론*

**개인 시뮬레이션 (Individual Simulation)**
- **아키텍처 설계**: 
  - 프로필 모듈: 인구통계학적 정보, 성격, 역사적 배경 저장
  - 메모리 모듈: 단기/장기 메모리 구조(인출 기반, 반영 기반)
  - 계획 모듈: 상황적/공감적 계획 전략으로 의사결정 도출
  - 액션 모듈: 환경과 상호작용하는 행동 실행

- **구성 방법**:
  - 프롬프팅: "You are an expert..." 형태의 역할 기술
  - 학습: 파인튜닝, 강화학습을 통한 적응적 학습
  - 수동/LLM 생성: 프로필 설명(descriptions) 또는 대화(conversations) 기반 구성

- **목표 분류**:
  - 캐릭터 기반: 영화/문학 인물 등 구체적 개인 모방
  - 인구통계학적: 특정 나이, 성별, 직업 등 인구 집단 특성 반영

- **평가 방법**:
  - 정적 평가: 프롬프트에 직접 응답하는 방식, 객관적 점수화 또는 인간 판단
  - 상호작용 평가: 복수 에이전트 대화 또는 실제 환경과의 상호작용을 통한 평가

**시나리오 시뮬레이션 (Scenario Simulation)**
- 다중 에이전트가 특정 목표(소프트웨어 개발, 의료 진단, 사법 판단) 달성을 위해 협업
- 역할 분담, 계층적/중앙화된 조직 구조, 다양한 통신 메커니즘 활용
- 집단 지능의 활용으로 복잡한 문제 해결

**사회 시뮬레이션 (Society Simulation)**
- 다양한 개인으로 구성된 대규모 에이전트 네트워크 구축
- 사회적 영향(social influence), 네트워크 구조, 상호작용 규칙을 통해 창발적 행동 생성
- 의견 역학(opinion dynamics), 전염병 모델링, 경제 현상 등 실제 사회 현상 재현

## Originality

- **통합적 분류 체계**: 개인→시나리오→사회로 이어지는 점진적 복잡성 증가를 명확히 정의한 첫 포괄적 분류
  
- **다차원적 평가 프레임워크**: 정적/상호작용 평가, 객관적/주관적 평가 등 다양한 평가 관점을 체계화
  
- **광범위한 문헌 수집**: 개인 시뮬레이션 84개, 시나리오 및 사회 시뮬레이션 다수의 논문을 정리하여 최신 동향 파악
  
- **상호보완적 관점**: 개인 모델의 정교함(정밀도)과 개체군 규모(다양성)의 역관계(trade-off)를 명시적으로 제시
  
- **학제간 응용성**: 정책 수립, 사회 관리, 심리학, 경제학 등 다양한 분야의 응용 가능성을 제시

## Limitation & Further Study

- **검증 부재**: 
  - 시뮬레이션된 행동이 실제 인간 행동을 얼마나 정확히 재현하는지에 대한 체계적 검증 메커니즘 부족
  - 알고리즘적 충실도(algorithmic fidelity) 측정의 표준화 부재

- **확장성 문제**: 
  - 대규모 사회 시뮬레이션에서 계산 복잡도와 일관성 유지의 어려움
  - LLM 기반 에이전트의 반복 가능성과 재현성 문제 미해결

- **윤리적 고려 부족**: 
  - 민감한 인구 집단 모방 시 편향(bias) 및 고정관념(stereotype) 재현 위험
  - 시뮬레이션 결과의 정책 적용 시 발생 가능한 사회적 영향에 대한 논의 부족

- **후속 연구 방향**:
  - 다중 LLM 모델 간 일관성 및 호환성 연구 필요
  - 실제 사회 데이터와의 검증을 통한 시뮬레이션 타당성 확보
  - 개인-시나리오-사회 세 수준의 유기적 통합 메커니즘 개발
  - 장기 시간 스케일에서의 사회 역학 시뮬레이션 개선


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4/5

**총평**: 이 논문은 LLM 기반 에이전트의 사회 시뮬레이션 활용을 개인→시나리오→사회로 계층화하여 최초로 통합적으로 정리한 중요한 서베이이다. 광범위한 문헌 수집과 다차원적 분류 체계는 해당 분야의 나침반 역할을 할 것이나, 실제 인간 행동과의 검증 및 윤리적 함의에 대한 심화 논의가 향후 과제로 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — LLM 인구의 문화진화가 개별-사회 시뮬레이션 체계의 핵심 구성요소가 된다
- 🧪 응용 사례: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 사회 시뮬레이션 체계를 과학 발견 자동화에 구체적으로 적용하는 방법을 제시한다
- 🏛 기반 연구: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 사회 시뮬레이션 기반 연구의 포괄적 조사가 시뮬레이션된 인간 사회에서의 언어모델 학습 방법론의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — 개별 에이전트 문화진화를 사회 전체 시뮬레이션으로 확장하는 포괄적 체계를 제시한다
- 🔗 후속 연구: [[papers/660_Reimagining_urban_science_Scaling_causal_inference_with_larg/review]] — 사회 시뮬레이션 설문과 도시 인과 추론 자동화는 모두 사회과학 연구의 AI 기반 확장을 다루는 상호 보완적 연구이다.
- 🔗 후속 연구: [[papers/188_Can_we_automatize_scientific_discovery_in_the_cognitive_scie/review]] — 사회 시뮬레이션 기반 개인에서 사회로의 서베이가 인지과학 자동화의 사회적 확장 방향을 제시한다
- 🔗 후속 연구: [[papers/358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin/review]] — 사회 시뮬레이션 연구의 포괄적 조사를 통해 인문사회과학에서 AI 에이전트 활용을 개별 연구에서 사회 전체 현상 연구로 확장함
