---
title: "194_Chain_of_ideas_Revolutionizing_research_via_novel_idea_devel"
authors:
  - "Long Li"
  - "Weiwen Xu"
  - "Jiayan Guo"
  - "Ruochen Zhao"
  - "Xingxuan Li 외 (DAMO Academy"
date: "2024"
doi: "arXiv:2410.13185"
arxiv: ""
score: 4.2
essence: "LLM 기반 에이전트가 과학 문헌을 체인 구조로 조직하여 연구 분야의 진화 과정을 명확히 반영함으로써, 인간 연구자 수준의 참신한 연구 아이디어 생성을 자동화한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Roumeliotis and Tselikas_2024_Chain of ideas Revolutionizing research via novel idea development with llm agents.pdf"
---

# Chain of Ideas: Revolutionizing research via novel idea development with llm agents

> **저자**: Long Li, Weiwen Xu, Jiayan Guo, Ruochen Zhao, Xingxuan Li 외 (DAMO Academy, Alibaba Group; Zhejiang University) | **날짜**: 2024 | **DOI**: [arXiv:2410.13185](https://arxiv.org/abs/2410.13185)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: Vanilla RAG 기반 연구 에이전트와 Chain-of-Ideas 에이전트의 비교. CoI는 관련 논문들을 체계적 체인으로 조직하여 논리적 일관성 있는 아이디어 생성*

LLM 기반 에이전트가 과학 문헌을 체인 구조로 조직하여 연구 분야의 진화 과정을 명확히 반영함으로써, 인간 연구자 수준의 참신한 연구 아이디어 생성을 자동화한다.

## Motivation

- **Known**: 최근 LLM의 발전으로 수학, 정리 증명, 코딩 등 다양한 과학 작업에서 인간 전문가를 능가하는 성능을 보임. 이론적으로 더 추상적이고 창의적인 연구 아이디어 생성 작업도 가능할 것으로 예상됨.

- **Gap**: 기존 아이디어 생성 방법들은 (1) 광범위한 문헌을 무분별하게 LLM에 제시하거나 (2) 단순히 프롬프팅만 사용. 이로 인해 관련성 낮은 논문의 간섭으로 논리적 일관성 없는 아이디어가 생성되는 문제 발생.

- **Why**: 과학 문헌의 급속한 증가로 인해 연구자들이 최신 동향을 파악하고 의미 있는 연구 방향을 식별하기 어려워짐.

- **Approach**: 인간 연구자가 기초 논문부터 최신 연구까지 진화 과정을 추적하며 아이디어를 개발하는 방식에 영감을 받아, 체계적으로 선택된 논문들을 체인 구조로 조직하는 CoI 에이전트 제안.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: CoI 에이전트의 3단계 프레임워크 - CoI 구성, 아이디어 생성, 실험 설계*

1. **CoI 에이전트의 우수성**: AI 분야 아이디어 생성 태스크에서 모든 자동화 베이스라인을 능가하며, 2위 방법보다 56 ELO 점수 우수. 인간 전문가 수준의 참신성(novelty) 달성.

2. **비용 효율성**: 1개의 후보 아이디어와 실험 설계를 생성하는 최소 비용이 $0.50으로 매우 경제적.

3. **Idea Arena 평가 프레임워크**: 다양한 관점에서 아이디어 생성 방법을 포괄적으로 평가 가능하며, 인간 평가자의 선호도와 높은 일치도를 보임.

4. **핵심 발견**: 아이디어의 참신성을 위해서는 관련 문헌의 '양'보다 명확한 발전 추세 분석이 더 중요함을 규명.

## How

![Figure 2](figures/fig2.webp)

**Stage 1: CoI 구성 (CoI Construction)**
- 주어진 연구 주제에 대해 LLM이 K개의 서로 다른 관점의 쿼리 생성
- 각 쿼리마다 앵커(anchor) 논문 검색 (Semantic Scholar API 활용)
- 앵커 논문으로부터 양방향 확장:
  - **전진(Forward)**: 앵커 논문을 인용하는 후속 논문들 추적
  - **후진(Backward)**: 앵커 논문의 참고 논문들 추적
- 텍스트 임베딩(OpenAI text-embedding-3-large)으로 코사인 유사도 기반 순위 매김
- M+N+1개 논문의 아이디어를 시간순으로 체인화: {I₋ₘ → ··· → I₀ → ··· → Iₙ}

**Stage 2: 아이디어 생성 (Idea Generation)**
- 각 CoI에 대해 LLM이 현재 추세 분석 및 미래 연구 방향 예측
- 단계적 아이디어 구체화:
  - 동기(Motivation) 도출
  - 잠재적 임팩트 평가
  - 최종 아이디어 구현
- 참신성 검증 에이전트가 생성된 아이디어를 기존 문헌과 반복 비교
  - 유사성 높으면 → 아이디어 수정/정제
- 다중 CoI 브랜치로부터 최적 아이디어 선택

**Stage 3: 실험 설계 (Experiment Design)**
- 생성된 아이디어를 검증하기 위한 실험 설계 자동 생성
- 베이스라인 정의, 데이터셋 준비, 구현 방안 제시
- 명확성과 지원 가능성 검증

## Originality

- **구조화된 문헌 조직**: 기존 RAG 기반 방법의 무분별한 문헌 혼합과 달리, 논문들을 진화 체인으로 명확하게 조직하는 혁신적 접근. 이를 통해 LLM이 연구 분야의 발전 궤적을 명확히 인식.

- **인간 연구 프로세스 모방**: 인간이 기초 개념부터 최신 연구까지 추적하는 방식을 형식화하여 자동화. Few-shot 프롬프팅 효과 활용.

- **다중 관점 분석**: 단일 CoI의 한계를 극복하기 위해 K개 서로 다른 쿼리 기반의 CoI 브랜치 구성. 연구 주제의 다차원적 이해 가능.

- **참신성 검증 루프**: 생성 후 반복적 참신성 검증으로 기존 아이디어와의 중복 제거. 동적 정제 메커니즘.

- **Idea Arena 평가 프레임워크**: 경기장 스타일의 쌍(pair) 비교 평가로 인간 평가자 선호도와 높은 상관관계. 기존 정적 평가의 한계 극복.

## Limitation & Further Study

- **스케일 검증 부족**: 현재 AI 분야만 중심으로 평가. 생물학, 화학, 사회과학 등 다른 분야에서의 일반화 가능성 미검증.

- **앵커 논문 선택의 민감성**: Semantic Scholar API 검색 품질과 초기 쿼리 생성에 따른 성능 편차 가능성. 앵커 선택 전략의 강건성 부족.

- **실제 실험 검증 부재**: 생성된 아이디어와 실험 설계의 실제 수행 검증 없음. 이론적 가능성만 입증.

- **계산 비용 vs 품질 트레이드오프**: $0.50 비용은 경제적이나, LLM 모델 크기, CoI 길이, 브랜치 수 등에 따른 성능-비용 분석 부족.

- **후속 연구 방향**:
  - 다양한 학문 분야로의 확대 적용
  - 더 정교한 앵커 선택 알고리즘 개발
  - 생성된 아이디어의 실제 수행 가능성 평가
  - 학계 협력을 통한 장기 추적 조사

## Evaluation

- **Novelty (참신성)**: 4.5/5
  - 문헌 조직의 체인 구조화라는 명확히 새로운 접근
  - 인간 연구 프로세스 모방이라는 개념적 참신성
  - 다만 기본 개념은 기존 RAG와 CoT 방법의 조합 성격

- **Technical Soundness (기술적 타당성)**: 4/5
  - 전반적 방법론 논리 및 구현이 타당함
  - Semantic Scholar API, 텍스트 임베딩 등 기술 선택 합리적
  - 다만 참신성 검증 메커니즘의 구체적 기술 설명 부족

- **Significance (중요성)**: 4.5/5
  - 자동화된 연구 아이디어 생성이라는 실제 학계 문제 해결
  - 대규모 과학 문헌 처리의 실용적 가치 높음
  - AI/ML 커뮤니티에 즉시적 영향력 가능
  - 다만 아직 AI 분야에만 검증된 한계

- **Clarity (명확성)**: 4/5
  - 3단계 프레임워크가 명확하고 Figure 2로 직관적 이해 용이
  - 상세한 프롬프트 예시 제시 (Appendix)
  - 구체적 예시(ToT, CoT, SC, GoT 체인)로 설명 효과적
  - 다만 일부 기술적 상세(e.g., 유사도 임계값, 반복 종료 조건)는 불명확

- **Overall (종합)**: 4.2/5
  - LLM을 활용한 자동화된 아이디어 생성에 실질적 기여
  - 인간 수준의 성능 달성과 경제성의 균형
  - 평가 프레임워크(Idea Arena)의 방법론적 가치
  - 실용성과 학술적 엄밀성의 우수한 조화

**총평**: 이 논문은 LLM의 창의적 능력을 과학 분야에 실질적으로 적용하는 혁신적 프레임워크를 제시하며, 문헌의 체계적 조직화를 통해 아이디어 생성 품질을 획기적으로 향상시킨다. 다만 AI 분야 검증과 실제 실험 수행 검증으로의 확장이 향후 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/143_AutoP2C_An_LLM-Based_Agent_Framework_for_Code_Repository_Gen/review]] — 연구 아이디어 생성이 논문 구현 자동화의 선행 단계로서 전체 연구 자동화를 완성한다
- 🔄 다른 접근: [[papers/509_Llms_can_realize_combinatorial_creativity_generating_creativ/review]] — 체인 구조 아이디어 개발과 조합적 창의성이 모두 LLM의 참신한 아이디어 생성을 다룬다
- 🔗 후속 연구: [[papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/review]] — 아이디어 생성 후 그래프 기반 평가가 연구 아이디어의 품질 검증을 제공한다
- 🔗 후속 연구: [[papers/143_AutoP2C_An_LLM-Based_Agent_Framework_for_Code_Repository_Gen/review]] — 연구 아이디어 생성을 실행 가능한 코드로 구현하는 전체 파이프라인을 완성한다
- 🔄 다른 접근: [[papers/509_Llms_can_realize_combinatorial_creativity_generating_creativ/review]] — 조합적 창의성 이론과 체인 구조 아이디어 개발이 모두 LLM의 창의적 아이디어 생성을 다룬다
- 🔄 다른 접근: [[papers/366_Futuregen_Llm-rag_approach_to_generate_the_future_work_of_sc/review]] — 과학 논문의 미래 연구 방향 생성에서 RAG 기반 접근법과 아이디어 체인 방법론은 서로 다른 창의적 생성 전략이다.
- 🔗 후속 연구: [[papers/442_Iris_Interactive_research_ideation_system_for_accelerating_s/review]] — 연구 아이디어 생성을 몬테카를로 트리 탐색으로 확장한다
- 🔄 다른 접근: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 동적 제어 대신 아이디어 체인 방식으로 연구 아이디어 생성의 창의성과 실현성을 균형 잡는 다른 접근법을 제시한다.
- 🧪 응용 사례: [[papers/714_Scideator_Human-llm_scientific_idea_generation_grounded_in_r/review]] — 아이디어 개발을 위한 체인 방식이 구조화된 요소 재조합의 구체적 실행 방법이다
- 🔄 다른 접근: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 둘 다 연구 아이디어 생성을 다루지만 418은 재료 발견에, Chain of Ideas는 일반적 연구 혁신에 특화
- 🏛 기반 연구: [[papers/392_Grapheval_A_lightweight_graph-based_llm_framework_for_idea_e/review]] — 연구 아이디어 생성 후 그래프 기반 분해와 평가가 아이디어 품질 검증을 제공한다
- 🔗 후속 연구: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — 연구 아이디어 개발의 체계적 접근을 다루어 AI Idea Bench가 측정하려는 아이디어 생성 역량의 실용적 활용 방안을 제시함
- 🔗 후속 연구: [[papers/146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s/review]] — 아이디어 개발을 위한 연쇄적 접근법으로, 데이터 주도 발견을 아이디어 생성 단계까지 확장한 방법론을 제시합니다.
- 🏛 기반 연구: [[papers/411_How_do_humans_and_language_models_reason_about_creativity_a/review]] — 창의성 평가를 위한 아이디어 생성 및 개발 방법론의 기초 프레임워크를 제공한다
- 🔗 후속 연구: [[papers/762_Spark_A_system_for_scientifically_creative_idea_generation/review]] — 아이디어 개발 체인을 과학적 창의성과 자동 평가가 통합된 시스템으로 확장한다
