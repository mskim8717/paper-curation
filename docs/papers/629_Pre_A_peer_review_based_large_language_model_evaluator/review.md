---
title: "629_Pre_A_peer_review_based_large_language_model_evaluator"
authors:
  - "Zhumin Chu"
  - "Qingyao Ai"
  - "Y. L. Tu"
  - "Haitao Li"
  - "Yiqun Liu"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "학술지의 동료 평가(peer review) 메커니즘에서 영감을 받아, 여러 대규모 언어모델(LLM)을 평가자로 활용하여 다른 LLM들의 성능을 자동으로 평가하는 프레임워크를 제안한다. 자격 시험으로 신뢰할 수 있는 평가자를 선별한 후 이들의 평가 결과를 집계하여 편향 없는 LLM 평가를 실현한다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Retrieval-Augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chu et al._2024_Pre A peer review based large language model evaluator.pdf"
---

# Pre: A peer review based large language model evaluator

> **저자**: Zhumin Chu, Qingyao Ai, Y. L. Tu, Haitao Li, Yiqun Liu | **날짜**: 2024 | **DOI**: N/A

---

## Essence

학술지의 동료 평가(peer review) 메커니즘에서 영감을 받아, 여러 대규모 언어모델(LLM)을 평가자로 활용하여 다른 LLM들의 성능을 자동으로 평가하는 프레임워크를 제안한다. 자격 시험으로 신뢰할 수 있는 평가자를 선별한 후 이들의 평가 결과를 집계하여 편향 없는 LLM 평가를 실현한다.

## Motivation

- **Known**: 현재 LLM 평가는 인간 평가자 방식과 모델 기반 평가 방식 두 가지로 나뉨. 인간 평가는 신뢰할 수 있지만 비용이 높고, GPT-4 등 단일 LLM을 평가자로 사용하는 방식은 비용 효율적이나 고유한 편향성 문제 존재

- **Gap**: 기존 평가 방법들이 안고 있는 세 가지 근본적 문제
  1. 높은 비용: 인간 평가는 다양한 LLM 응답으로 인해 평가 비용이 LLM 수에 정비례
  2. 낮은 일반화 가능성: 과제별 데이터셋 구성과 평가자 재훈련 필요, 다른 과제로의 전이 불가능
  3. 내재된 편향: 모델별 고유 특성으로 인한 편향(예: GPT-4는 GPT 계열 모델 응답을 선호)

- **Why**: 학술 출판에서 동료 평가 시스템이 신뢰성 있는 평가를 제공하듯이, 다수의 LLM 평가자를 활용하면 개별 모델의 편향을 상쇄하고 더 객관적인 평가 가능

- **Approach**: 자격 시험을 통해 신뢰할 수 있는 LLM 평가자 선별 → 선별된 평가자들이 여러 후보 LLM의 응답 평가 → 모든 평가자의 결과 집계하여 최종 순위 결정

## Achievement

1. **편향성 감소**: 단일 LLM 평가의 편향성을 실증적으로 증명(Preference Gap 메트릭). Figure 3은 7개의 강력한 LLM 간의 심각한 편향 차이를 보여줌

2. **높은 인간 평가 일관성**: 텍스트 요약 및 비정형 질의응답 과제에서 PRE 모델이 모든 기준선(GPT-4 포함)을 능가하며 인간 선호도와 가장 높은 일관성 달성

3. **비용 효율성 및 일반화**: 과제별 재훈련 불필요하고 다양한 과제로 쉽게 전이 가능하여 기존 방법 대비 월등한 확장성 제공

4. **견고성**: 특정 모델 구조나 LLM에 대한 의존성 제거로 더 견고한 평가 결과 생성

## How

![Figure 1](figures/fig1.webp) *PRE의 전체 아키텍처: 자격 시험 모듈, 평가 모듈, 결과 집계 모듈로 구성*

![Figure 2](figures/fig2.webp) *자격 시험 모듈의 과정: 평가 후보자 LLM들의 신뢰성을 사전에 검증*

- **자격 시험 모듈**: 
  - 각 평가 과제에 대해 작은 규모의 자격 시험 데이터셋 구성
  - 후보 LLM들이 시험 응답 생성 및 인간 판정 결과와 비교
  - 신뢰도 임계값 이상의 LJM만 최종 평가자로 선정

- **평가 모듈**:
  - 선별된 평가자 LLM들이 후보 LLM들의 응답에 대해 점수 부여 또는 쌍별 비교(pairwise comparison) 수행
  - 평가자별 평가 결과는 정형화된 프롬프트를 통해 수집

- **결과 집계 모듈**:
  - 모든 평가자의 점수 또는 선호도 결과를 집계
  - ELO 레이팅 시스템 등의 방법으로 최종 순위 도출
  - 개별 평가자의 편향이 상쇄되도록 설계

- **다양한 PRE 변형**: Figure 4에서 여러 집계 전략(평균, 중앙값, 투표 등)의 성능 비교

## Originality

- **혁신적 프레임워크**: 학술 동료 평가 메커니즘을 LLM 평가 영역에 처음으로 적용한 창의적 접근

- **자격 시험 메커니즘**: 평가자의 신뢰성을 사전 검증하는 선별 단계는 기존 다중 모델 평가(PRD, CHATEVAL) 연구들과 차별화되는 실질적 개선

- **편향성 분석의 깊이**: 개별 LLM의 내재된 편향을 체계적으로 측정하고 이를 해결하는 방법론 제시

- **일반화 가능성**: 특정 과제나 모델에 종속되지 않는 범용 평가 프레임워크로 설계

## Limitation & Further Study

- **자격 시험 데이터의 의존성**: 자격 시험 결과가 일반 평가 성능을 좌우할 수 있으므로, 효과적인 시험 데이터 구성의 전략 부재

- **평가자 선택의 민감성**: 어떤 LJM을 평가자로 선택하는지에 따른 성능 변동성에 대한 상세 분석 부족

- **제한된 과제 범위**: 텍스트 요약과 비정형 QA 두 과제만으로 검증되었으며, 분류, 번역 등 다른 유형의 과제 확대 필요

- **비용 분석의 구체성**: 인간 평가 대비 실제 계산 비용 절감 정도의 정량적 분석 부재

- **후속 연구 방향**:
  - 자격 시험의 최소 규모 및 최적 구성 방법 연구
  - 평가자 다양성과 평가 성능 간의 관계 분석
  - 새로운 과제 영역으로의 확대 및 도메인 적응(domain adaptation) 연구
  - 시간 경과에 따른 LLM 성능 변화 추적 시스템 구축

## Evaluation

- **Novelty**: 4.5/5
  - 동료 평가 메커니즘의 창의적 적용이 돋보이나, 다중 모델 평가 자체는 기존 연구에서 제안됨

- **Technical Soundness**: 4/5
  - 방법론이 명확하고 실험 설계가 합리적이나, 자격 시험 메커니즘의 이론적 근거와 민감도 분석이 강화될 필요

- **Significance**: 4.5/5
  - LLM 평가의 근본적 문제들(비용, 편향, 일반화)을 실질적으로 해결하는 실용적 가치 높음
  - 다만 제한된 과제 범위에서의 검증으로 인한 일반화 주장의 강도 약화

- **Clarity**: 4/5
  - 전체 프레임워크 설명이 명확하고 동기 부여가 강렬하나, 자격 시험 상세 절차와 집계 알고리즘 기술이 더 구체화 가능

- **Overall**: 4.2/5

**총평**: 본 논문은 학술적 동료 평가 원리를 LLM 자동 평가에 창의적으로 도입하여 비용, 편향, 일반화 문제를 동시에 해결하는 실질적인 해결책을 제시한 의미 있는 연구이다. 다만 평가 과제의 다양화와 메커니즘의 이론적 심화를 통해 주장의 보편성을 더욱 강화할 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 둘 다 LLM을 활용한 동료 평가 시스템이지만, PRE는 다중 LLM 평가자 활용에, 다른 논문은 다중 턴 대화 구조에 집중한다
- 🔗 후속 연구: [[papers/677_Reviewer2_Optimizing_Review_Generation_Through_Prompt_Genera/review]] — 프롬프트 생성을 통한 리뷰 최적화 연구가 PRE의 동료 평가 기반 LLM 평가 프레임워크로 발전되었다
- 🏛 기반 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — AI 생성 리뷰에 대한 평가 프레임워크 연구가 PRE의 동료 평가 메커니즘을 활용한 LLM 평가 시스템의 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/1088_Lag_Llm_agents_for_leaderboard_auto_generation_on_demanding/review]] — 피어리뷰 기반 LLM 평가가 리더보드 생성을 위한 성과 측정의 방법론적 토대를 제공한다.
- 🔄 다른 접근: [[papers/237_Confidence_in_Large_Language_Model_Evaluation_A_Bayesian_App/review]] — 베이지안 접근법 대신 동료 심사 기반 LLM 평가를 제시한다
- 🔄 다른 접근: [[papers/877_What_Can_Natural_Language_Processing_Do_for_Peer_Review/review]] — NLP 동료 심사 지원 대신 LLM 기반 평가자를 개발하는 다른 접근법
