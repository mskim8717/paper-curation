---
title: "820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating"
authors:
  - "Guangzhi Xiong"
  - "Eric Xie"
  - "Corey Williams"
  - "Myles Kim"
  - "Amir Hassan Shariatmadari"
date: "2025"
doi: "10.24963/ijcai.2025/873"
arxiv: ""
score: 4.0
essence: "LLM이 생성한 과학 가설의 신뢰성을 평가하기 위해 TruthHypo 벤치마크와 KnowHD 할루시네이션 탐지 프레임워크를 제안하며, 기존 지식에 기반한 가설 필터링의 효과를 입증한다."
tags:
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/LLM_Hypothesis_Generation_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xiong et al._2025_Toward Reliable Scientific Hypothesis Generation Evaluating Truthfulness and Hallucination in Large.pdf"
---

# Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models

> **저자**: Guangzhi Xiong, Eric Xie, Corey Williams, Myles Kim, Amir Hassan Shariatmadari | **날짜**: 2025 | **DOI**: [10.24963/ijcai.2025/873](https://doi.org/10.24963/ijcai.2025/873)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the TruthHypo benchmark, including dataset construction, task formulation, and truthfulness evalua*

LLM이 생성한 과학 가설의 신뢰성을 평가하기 위해 TruthHypo 벤치마크와 KnowHD 할루시네이션 탐지 프레임워크를 제안하며, 기존 지식에 기반한 가설 필터링의 효과를 입증한다.

## Motivation

- **Known**: LLM은 광대한 과학 문헌을 분석하여 가설 생성에 활용될 수 있으나, 이들이 생성하는 가설의 정확성 검증은 시간과 자원 소비가 크다. 또한 LLM의 할루시네이션 문제로 인해 그럴듯하지만 부정확한 가설이 생성될 수 있다.
- **Gap**: LLM 기반 과학 가설 생성의 신뢰성 평가 방법이 체계적으로 제시되지 않았으며, 할루시네이션과 가설의 참성 간의 관계가 충분히 탐구되지 않았다.
- **Why**: LLM이 과학 발견 가속화에 활용되려면 생성된 가설이 기존 지식에 얼마나 기반하는지 정량화하고, 불신뢰할 수 있는 가설을 체계적으로 걸러낼 수 있어야 한다.
- **Approach**: PubTator 3.0 기반 생의학 지식 그래프를 활용하여 TruthHypo 벤치마크를 구축하고, 추론 과정을 분석하는 KnowHD 프레임워크를 통해 가설의 기반성(groundedness) 점수를 산출하여 신뢰할 수 있는 가설 선별을 수행한다.

## Achievement


- **TruthHypo 벤치마크**: 시간적 분할(2023년 이전/2024년 이후)을 통해 미래 발견을 시뮬레이션하는 생의학 가설 생성 평가 벤치마크 제시
- **KnowHD 프레임워크**: 가설 생성 근거를 분석하여 기반성 점수를 제공하고 할루시네이션된 가설을 탐지하는 지식 기반 프레임워크 개발
- **LLM 성능 분석**: LLM들이 신뢰할 수 있는 가설 생성에서 상당한 어려움을 겪으며, KnowHD의 기반성 점수가 신뢰할 수 있는 가설 선별의 효과적인 지표임을 입증
- **인간 평가 검증**: 개방형 가설 생성 작업에서 KnowHD이 과학적으로 타당한 가설 식별을 가속화할 수 있음을 확인

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the TruthHypo benchmark, including dataset construction, task formulation, and truthfulness evalua*

- PubTator 3.0의 생의학 지식 그래프에서 Chemical & Gene, Disease & Gene, Gene & Gene 관계 유형에 대해 PMID 기반 시간 분할 수행
- 음성 샘플을 구성하여 LLM이 관계 부재 사례에 대해 거짓 양성을 만드는 경향을 평가
- 매개변수 지식, 구조화된 KG, retrieval-augmented generation (RAG) 파이프라인, 혼합 설정 등 다양한 지식 보강 시나리오에서 LLM 평가
- KnowHD는 LLM의 추론 단계를 분석하여 각 가설에 대한 기반성 점수를 계산하고, 이를 통해 신뢰할 수 있는 가설 필터링 수행
- F1-score와 Accuracy로 가설의 신뢰성을 평가하고, 기반성 점수의 유효성을 검증

## Originality

- 시간 기반 지식 분할을 통해 미래 발견을 시뮬레이션하는 현실적인 벤치마크 설계
- LLM의 추론 과정 분석을 통한 할루시네이션 탐지라는 새로운 접근으로, 단순 사실 검증을 넘어 기반성 평가 수행
- 생의학 도메인의 세 가지 관계 유형에 대한 포괄적 평가로 일반화 가능성 제시

## Limitation & Further Study

- 현재 생의학 도메인에만 국한되어 있어, 다른 과학 분야(화학, 물리학 등)로의 확장성이 미검증
- PubTator 3.0의 관계 유형 제한으로 인해 더 복잡한 다중 항목 관계나 조건부 관계를 평가하지 못함
- 인간 평가가 제한적으로 수행되어 KnowHD 점수와 실제 과학적 가치 간의 관계가 더 광범위하게 검증되어야 함
- LLM 할루시네이션의 근본 원인에 대한 심층 분석이 부족하며, 향후 연구에서 다양한 모델의 할루시네이션 메커니즘 비교 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 과학 가설 생성의 신뢰성 평가라는 중요한 문제를 체계적으로 다루며, 시간 기반 벤치마크와 추론 과정 분석을 통한 할루시네이션 탐지라는 혁신적 접근을 제시한다. 다만 생의학 도메인 한정과 인간 평가의 제한 등을 개선한다면 더욱 강력한 기여가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/819_Toward_reliable_biomedical_hypothesis_generation_Evaluating/review]] — 생의학 특화 버전으로 일반 과학 분야 접근법과의 비교 분석이 가능합니다.
- 🔗 후속 연구: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — 과학적 아이디어 생성 평가에 신뢰성 검증 요소를 추가합니다.
- ⚖️ 반론/비판: [[papers/728_SciMON_Scientific_Inspiration_Machines_Optimized_for_Novelty/review]] — 참신성 추구와 신뢰성 확보 간의 균형점을 찾는 대조적 관점을 제시합니다.
- 🔄 다른 접근: [[papers/819_Toward_reliable_biomedical_hypothesis_generation_Evaluating/review]] — 동일한 연구팀의 생의학 분야 특화 버전으로 일반 과학 분야와 비교 연구가 가능합니다.
- 🔗 후속 연구: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — 아이디어 생성 평가에 신뢰성과 진실성 검증 요소를 통합합니다.
- 🧪 응용 사례: [[papers/468_Large_Language_Models_are_Zero_Shot_Hypothesis_Proposers/review]] — 생의학 가설 생성의 신뢰성 평가가 제로샷 가설 생성의 실제 적용 검증 사례이다
- 🔗 후속 연구: [[papers/123_Automated_Hypothesis_Validation_with_Agentic_Sequential_Fals/review]] — 신뢰할 수 있는 과학적 가설 생성 평가로 확장하여, 가설 검증을 넘어 가설 생성까지 포괄하는 연구
- 🔗 후속 연구: [[papers/149_Bayes-Entropy_Collaborative_Driven_Agents_for_Research_Hypot/review]] — 베이지안 추론 기반 가설 생성에서 신뢰할 수 있는 생물의학 가설 생성이라는 더 특화된 응용으로 발전한다
