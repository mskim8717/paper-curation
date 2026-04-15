---
title: "187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S"
authors:
  - "Chenglei Si"
  - "Diyi Yang"
  - "Tatsunori Hashimoto"
date: "2024.09"
doi: "10.48550/arXiv.2409.04109"
arxiv: ""
score: 4.0
essence: "100명 이상의 NLP 연구자를 모집하여 LLM이 생성한 연구 아이디어와 인간 전문가의 아이디어를 맹검 비교한 결과, LLM 생성 아이디어가 신규성(novelty)에서 유의미하게 우수함을 발견했다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Research_Concept_Extraction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Si et al._2024_Can LLMs Generate Novel Research Ideas A Large-Scale Human Study with 100+ NLP Researchers 1.pdf"
---

# Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

> **저자**: Chenglei Si, Diyi Yang, Tatsunori Hashimoto | **날짜**: 2024-09-06 | **DOI**: [10.48550/arXiv.2409.04109](https://doi.org/10.48550/arXiv.2409.04109)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Comparison of the three experiment conditions across all review metrics. Red asterisks*

100명 이상의 NLP 연구자를 모집하여 LLM이 생성한 연구 아이디어와 인간 전문가의 아이디어를 맹검 비교한 결과, LLM 생성 아이디어가 신규성(novelty)에서 유의미하게 우수함을 발견했다.

## Motivation

- **Known**: LLM의 성능 향상으로 과학 발견 가속화 가능성에 대한 낙관론이 존재하며, 자율적으로 연구 아이디어를 생성하는 AI 에이전트들이 제안되고 있다. 다만 LLM이 전문가 수준의 신규 아이디어 생성 능력을 보였다는 실증적 평가는 부재했다.
- **Gap**: LLM 기반 연구 아이디어 생성 능력에 대한 대규모 전문가 평가 체계와 정량적 증거가 없다. 기존 연구들은 샘플 크기 부족, 주관적 평가 기준, LLM 자체 평가 신뢰성 부족 등의 한계를 가지고 있다.
- **Why**: 연구 아이디어 생성은 과학 연구 프로세스의 첫 단계로서, 자율 AI 연구 에이전트의 가능성을 판단하는 핵심 지표이다. 전문가 수준의 능력 평가를 위해서는 대규모 전문가 평가가 필수적이다.
- **Approach**: 79명의 NLP 전문가 리뷰어를 모집하여 인간 전문가(N=49), LLM 생성(N=49), LLM+인간 재순위(N=49) 세 조건의 아이디어를 맹검 평가하도록 했다. 주제 분포 일치, 형식 표준화 등으로 교란 변수를 통제하고 통계적 검정을 수행했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Comparison of the three experiment conditions across all review metrics. Red asterisks*

- **LLM 신규성 우위성**: LLM 생성 아이디어가 인간 전문가 아이디어보다 신규성(novelty) 점수에서 유의미하게 높음 (p<0.05, 5.64 vs 4.84)
- **다중 검정 견고성**: Bonferroni 보정 및 다양한 통계 검정을 통해 신규성 우위성이 견고함을 확인
- **흥분도 연관성**: LLM 아이디어의 신규성 향상이 흥분도(excitement) 및 종합 점수와 양의 상관관계
- **실행 가능성 트레이드오프**: 신규성 향상이 실행 가능성(feasibility)에서는 약간의 약세를 보임
- **LLM 에이전트 한계 규명**: LLM의 자체 평가 실패, 아이디어 생성 다양성 부족 등 개방 문제 식별

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of our study: we recruit 79 expert researchers to perform blind review of 49 ideas*

- 7개 특정 NLP 연구 주제(Bias, Coding, Safety, Multilinguality, Factuality, Math, Uncertainty) 정의로 주제 편향 통제
- 동일 지시사항, 아이디어 템플릿, 시연 예제를 모든 참가자에게 제공
- 제목, 문제진술, 동기, 제안 방법, 단계별 실험 계획 등을 포함하는 표준화 템플릿으로 작성 형식 통일
- 인간 전문가 아이디어와 LLM 생성 아이디어의 형식과 스타일 표준화를 blind review 전 수행
- LLM 에이전트: retrieval augmentation 및 inference-time scaling (과생성 및 재순위) 기법 적용
- Welch's t-test 및 Bonferroni 보정을 사용한 통계적 검정

## Originality

- 100명 이상 전문가를 모집한 대규모 맹검 비교 설계로 선행 소규모 연구의 한계 극복
- 주제 분포 일치, 형식 표준화 등 다층적 교란 변수 통제로 엄밀한 인과 추론 가능
- 신규성 판단의 어려움을 인정하고 아이디어 실행 프로젝트 추적 연구(end-to-end study)를 제안
- LLM-as-judge가 아닌 인간 전문가 평가 중심의 평가 패러다임 제시
- 연구 아이디어 생성이라는 구체적 과학 작업에서 LLM의 역량을 정량적으로 입증한 첫 연구

## Limitation & Further Study

- **범위 제한**: 프롬핑(prompting) 기반 NLP 연구로만 국한되어 다른 연구 분야 일반화 어려움
- **아이디어 깊이**: 단기 실행 가능한 아이디어에 초점으로 장기 대규모 연구 프로그램 평가 미포함
- **통계 검정력 부족**: 신규성 외 다른 지표(실행 가능성, 효과성 등)의 차이를 통계적으로 검증하기 위한 샘플 크기 부족
- **평가자 편향**: 인간 평가자도 신규성 판단에 어려움을 겪을 수 있으며, 전문가 간 일치도 검증 필요
- **후속 연구**: 제안된 end-to-end 실행 연구로 신규성 및 실행 가능성 판단이 실제 연구 성과로 이어지는지 검증 필요
- **LLM 다양성 개선**: 아이디어 과생성 시 중복성 문제 해결 및 다양성 강화 기법 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 5/5
- Overall: 4/5

**총평**: 대규모 전문가 평가 설계를 통해 LLM의 연구 아이디어 신규성 능력을 처음으로 정량적으로 입증한 중요한 실증 연구이다. 다만 평가 대상 연구 분야의 한계와 신규성 판단 자체의 주관성 문제를 인정하며, 후속 아이디어 실행 연구로 이를 보완할 계획을 제시했다.

## Related Papers

- ⚖️ 반론/비판: [[papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/review]] — LLM이 인간보다 참신한 연구 아이디어를 생성한다는 발견이 AI 도구가 탐색 범위를 축소시킨다는 결과와 상반된 관점을 제시한다.
- 🏛 기반 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — LLM 생성 아이디어의 신규성 평가 연구가 AI 과학자의 혁신성 인식 알고리즘 개발의 실증적 기반을 제공한다.
- 🔗 후속 연구: [[papers/376_Generation_and_human-expert_evaluation_of_interesting_resear/review]] — LLM 아이디어 생성 능력 평가를 전문가 평가와 결합하여 더 포괄적인 연구 아이디어 품질 평가 시스템을 구축한다.
- 🏛 기반 연구: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 인간 대비 LLM의 새로운 연구 아이디어 생성 능력에 대한 기초 연구가 동적 제어 시스템의 필요성을 뒷받침한다.
- 🧪 응용 사례: [[papers/580_Oag-bench_A_human-curated_benchmark_for_academic_graph_minin/review]] — OAG-Bench의 학술 그래프 데이터가 LLM의 새로운 연구 아이디어 생성 능력 평가에 활용될 수 있음
- 🔄 다른 접근: [[papers/632_Predicting_the_future_of_ai_with_ai_High-quality_link_predic/review]] — AI 연구 예측을 위해 의미적 네트워크 기반 링크 예측과 LLM 기반 아이디어 생성이라는 서로 다른 접근법을 제시함
- 🔗 후속 연구: [[papers/557_MOOSE-Chem_Large_Language_Models_for_Rediscovering_Unseen_Ch/review]] — LLM의 새로운 연구 아이디어 생성 능력이 MOOSE-Chem의 미발견 화학 가설 재발견을 더 창의적인 형태로 확장한다.
- 🏛 기반 연구: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — AI 연구 아이디어 생성 성능을 인간과 비교 평가하는 기본 방법론을 제시하여 AI Idea Bench의 평가 프레임워크 설계에 핵심 기반이 됨
- ⚖️ 반론/비판: [[papers/107_Artificial_intelligence_tools_expand_scientists_impact_but_c/review]] — AI 도구가 과학자의 탐색 범위를 축소시킨다는 발견과 LLM이 더 참신한 연구 아이디어를 생성한다는 결과가 대조적인 관점을 제시한다.
- 🏛 기반 연구: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — LLM의 새로운 연구 아이디어 생성 능력이 AI 아이디어가 인간 창의성에 미치는 영향 연구의 기초가 된다.
- 🔗 후속 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — LLM 생성 아이디어의 신규성 평가를 상대 이웃 밀도 알고리즘으로 자동화하여 대규모 아이디어 혁신성 평가를 가능하게 한다.
