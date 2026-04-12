---
title: "1054_Whats_In_Your_Field_Mapping_Scientific_Research_with_Knowled"
authors:
  - "Abhipsha Das"
  - "Nicholas Lourie"
  - "Siavash Golkar"
  - "Mariel Pettee"
date: "2025.05"
doi: "10.48550/arXiv.2503.09894"
arxiv: ""
score: 4.0
essence: "LLM과 구조화된 지식 그래프(Knowledge Graph)를 결합하여 30,000개의 과학 논문에서 자동으로 개념을 추출하고 분석하는 시스템을 제시합니다. 이를 통해 과학 분야 전반의 동향을 추적하고 체계적으로 문헌을 탐색할 수 있습니다."
tags:
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Bibliometric_Mapping_Tools"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Das et al._2025_What's In Your Field Mapping Scientific Research with Knowledge Graphs and Large Language Models.pdf"
---

# What's In Your Field? Mapping Scientific Research with Knowledge Graphs and Large Language Models

> **저자**: Abhipsha Das, Nicholas Lourie, Siavash Golkar, Mariel Pettee | **날짜**: 2025-05-29 | **DOI**: [10.48550/arXiv.2503.09894](https://doi.org/10.48550/arXiv.2503.09894)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Illustration of the structured concept extraction pipeline: i) the corpus used, ii) running optimized prompt*

LLM과 구조화된 지식 그래프(Knowledge Graph)를 결합하여 30,000개의 과학 논문에서 자동으로 개념을 추출하고 분석하는 시스템을 제시합니다. 이를 통해 과학 분야 전반의 동향을 추적하고 체계적으로 문헌을 탐색할 수 있습니다.

## Motivation

- **Known**: LLM은 과학 텍스트 이해에 강력하지만 대규모 문헌의 세부 관계 포착이 미흡합니다. Retrieval Augmented Generation(RAG) 같은 비구조화 접근법은 비용이 높고 정확한 패턴 분석이 어렵습니다.
- **Gap**: 기존 반구조화 방식(벡터 기반 유사도)은 개념의 기능적 역할을 구분하지 못하고 정량적 분석에 부적합합니다. 과학 전 분야에 적용 가능한 범용적이고 스케일 가능한 구조화 추출 방식이 부족합니다.
- **Why**: 과학 문헌의 지수적 증가로 인해 연구자들이 분야의 동향, 방법론 발전, 새로운 도구 도입 등을 체계적으로 추적하기 어렵습니다. 구조화된 표현은 대규모 코퍼스 전체에 대한 신뢰할 수 있는 통계 분석을 가능하게 합니다.
- **Approach**: 9개 범주(모델, 작업, 데이터셋, 분야, 모달리티, 방법, 객체, 속성, 기기)로 구성된 범용 스키마를 설계하고, Llama-3 70B로 few-shot 학습 기반 개념 추출을 수행합니다. 추출된 구조화 정보를 SQL 데이터베이스에 저장하고 지식 그래프로 시각화합니다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Illustration of the structured concept extraction pipeline: i) the corpus used, ii) running optimized prompt*

- **범용 과학 개념 스키마 개발**: 9개 카테고리로 천체물리학, 유체역학, 진화생물학 등 이질적 분야에 적용 가능한 스키마 설계
- **효율적 LLM 기반 추출 파이프라인**: 단 20개 수동 주석만으로 프롬프트 최적화(F1점수 기준 정확도 달성)
- **대규모 구조화 데이터 구축**: arXiv의 30,000개 논문에서 개념 추출 및 SQL 데이터베이스 구성 완료
- **대화형 질의-분석 시스템**: 연구자가 방법론 추이, 개념 공출현 등을 체계적으로 분석할 수 있는 인터페이스 제공
- **지식 그래프 시각화**: 추출된 개념 간 관계를 그래프로 표현하여 학문 생태계의 새로운 탐색 방식 제시

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Expanded prompt illustration with schema*

- **스키마 설계**: 저자들이 반복적 논의와 수동 주석을 통해 9개 과학 개념 범주 정의
- **프롬프트 엔지니어링**: Few-shot 예제 개수/선택, 프롬프트 구조, 입력 단위(문장/단락), 출력 형식(JSON/텍스트) 등 체계적 변수 실험
- **문장 단위 추출**: 수동 주석 예제를 활용한 Llama-3 70B 모델의 문장 단위 태깅
- **성능 평가**: 개발 세트(17개 논문)에서 정확도(precision), 재현율(recall), F1점수 메트릭으로 방향성 신호 제공
- **데이터베이스 구축**: Papers 테이블(메타데이터)과 Predictions 테이블(추출 개념)로 구성된 SQL 데이터베이스 설계
- **시각화**: 추출된 개념과 공출현 관계를 지식 그래프로 표현

## Originality

- 기존의 벡터 유사도 기반 반구조화 방식과 달리, **명확한 범주 스키마 기반의 구조화 추출** 도입으로 개념의 기능적 역할 구분 가능
- **최소한의 수동 주석(20개 논문)**으로 프롬프트를 최적화하여 대규모 확장 달성 - few-shot 학습의 실용적 입증
- 단순하면서도 **과학 전 분야에 통용 가능한 범용 스키마** 설계로 도메인 특이성과 일반성의 균형 추구
- 구조화된 추출 결과를 인터랙티브 질의 시스템과 결합하여 **정량적 패턴 분석과 시각화** 동시 지원

## Limitation & Further Study

- **낮은 정확도**: 최적화된 프롬프트의 정확도 44%±12%, 재현율 31%±11%로 여전히 노이즈 존재 - 상충관계(Coverage vs. Precision) 의존
- **개념 모호성**: 분야 간 개념 정의 불일치로 인해 다중 태그 가능성이 있으며, 복잡한 중의성 해결 메커니즘 부재
- **스키마 한계**: 9개 카테고리의 조정 불가능성으로 인한 도메인 특화 요구사항 미충족 가능성
- **후속 연구**: (1) 강화학습 또는 인간-in-the-loop 반복으로 정확도 개선, (2) 개념 간 계층적 관계 및 시간적 진화 추적 고도화, (3) 다국어 과학 문헌 확장, (4) 동적 스키마 적응 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM의 의미 이해 능력과 구조화된 지식 표현을 결합하여 대규모 과학 문헌의 체계적 분석을 가능하게 하는 실용적이고 확장 가능한 시스템을 제시합니다. 비록 추출 정확도는 개선의 여지가 있으나, 최소한의 주석으로 범용적 스키마를 설계하고 대규모 코퍼스에 적용한 점에서 높은 학술적 가치와 실무적 활용 가능성을 보여줍니다.

## Related Papers

- 🔄 다른 접근: [[papers/1118_Paper_Circle_An_Open-source_Multi-agent_Research_Discovery_a/review]] — 둘 다 LLM과 지식 그래프를 활용하여 과학 연구를 분석하지만 Paper Circle은 다중 에이전트 접근법을 사용한다.
- 🏛 기반 연구: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 컴퓨터 과학 분야의 대규모 지식 그래프인 CS-KG가 과학 연구 매핑을 위한 구조화된 지식의 모델을 제공한다.
- 🔄 다른 접근: [[papers/929_A_network_approach_to_topic_models/review]] — 토픽 모델링을 위한 네트워크 접근법과 LLM 기반 지식 그래프 접근법이 서로 다른 연구 분야 매핑 방법을 제시한다.
- 🏛 기반 연구: [[papers/1017_Science_as_exploration_in_a_knowledge_landscape_tracing_hots/review]] — 과학 연구 분야 매핑 방법론이 지식공간에서의 과학자 탐색 패턴을 분석하는 기술적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/1018_Science_Mapping_and_Science_Maps/review]] — 전통적인 인용 기반 과학 지도 대신 LLM과 지식 그래프를 활용한 새로운 연구 분야 매핑 방법을 제안한다.
- 🔄 다른 접근: [[papers/1118_Paper_Circle_An_Open-source_Multi-agent_Research_Discovery_a/review]] — 둘 다 LLM과 지식 그래프로 과학 연구를 분석하지만 Paper Circle은 다중 에이전트 파이프라인을 특징으로 한다.
- 🔄 다른 접근: [[papers/952_Design_and_Update_of_a_Classification_System_The_UCSD_Map_of/review]] — UCSD 과학 지도의 분류 체계 구축과 지식 그래프를 활용한 과학 연구 매핑이 서로 다른 접근법의 과학 분류 시스템을 제시합니다.
- 🔗 후속 연구: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 지식 그래프를 활용한 과학 연구 매핑 기법을 연구자 위치 매핑에 적용하여 더 풍부한 맥락 정보를 제공할 수 있다.
