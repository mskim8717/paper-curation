---
title: "1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio"
authors:
  - "Xi Chen"
  - "Huan-jing Zhao"
  - "Shu Zhao"
  - "Jie Chen"
  - "Yan-ping Zhang"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "SciRGC 프레임워크는 인용 의도(citation intent) 인식과 인용 네트워크를 활용하여 학술 논문의 적절한 인용 문헌을 추천하고 고품질의 인용 문장을 생성하는 다단계 시스템을 제안한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Citation-Based_Evidence_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_Scirgc Multi-granularity citation recommendation and citation sentence preference alignment.pdf"
---

# Scirgc: Multi-granularity citation recommendation and citation sentence preference alignment

> **저자**: Xi Chen, Huan-jing Zhao, Shu Zhao, Jie Chen, Yan-ping Zhang | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2505.20103](https://arxiv.org/abs/2505.20103)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Process for implementing citation recommendation and generation in the SciRGC framework*

SciRGC 프레임워크는 인용 의도(citation intent) 인식과 인용 네트워크를 활용하여 학술 논문의 적절한 인용 문헌을 추천하고 고품질의 인용 문장을 생성하는 다단계 시스템을 제안한다.

## Motivation

- **Known**: 인용 추천(citation recommendation)과 인용 생성(citation generation)은 기존 연구에서 분리되어 다루어져 왔으며, 인용 의도 분류, 임베딩 기반 유사도 매칭, BERT/GCN 활용 등의 방법들이 개발되었다.
- **Gap**: 기존 연구들은 인용 의도의 제어 가능성과 인용 추천 및 생성 간의 상관관계를 충분히 탐구하지 못했으며, 생성된 인용 문장의 품질을 공정하게 평가할 메트릭이 부족하다.
- **Why**: 과학 논문 작성 시 관련 선행 연구를 찾아 적절히 인용하는 과정은 시간이 많이 소요되고 특히 신진 연구자들에게 어려우므로, 자동화된 인용 추천 및 생성 시스템은 학제간 연구자들을 위한 실질적인 도구가 될 수 있다.
- **Approach**: 두 단계 인용 추천 모듈(회상 및 재순위 단계)에서 인용 네트워크 기반 협업 필터링과 인용 의도 특성을 통합하고, Chain-of-Thought 추론 기반 인용 문장 생성을 위해 LLM(Large Language Model)에 LoRA 미세 조정과 DPO(Direct Preference Optimization) 정렬을 적용한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Process for implementing citation recommendation and generation in the SciRGC framework*

- **향상된 인용 문헌 추천**: 인용 네트워크와 인용 의도를 통합하여 ACL-200, FullTextPeerRead, RefSeer, arXiv 등 4개 데이터셋에서 MRR 및 R@K 메트릭으로 기존 방법들을 일관되게 초과 달성
- **고품질 인용 문장 생성**: Chain-of-Thought 추론 기반 방식과 DPO를 통한 인간 선호도 정렬로 주류 대규모 언어 모델과 비교하여 우수한 성능 달성
- **새로운 평가 메트릭**: 기존 자동 평가 메트릭의 체계적 편향을 해결하기 위해 다차원 인용 생성 품질 평가 프레임워크 도입 및 인간 평가를 통한 검증

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Two collaborative filtering algorithms, dashed boxes represent two papers that are similar, and single arrows*

- **회상 단계(Recall Stage)**: 로컬 정보를 위해 인코더 모델 사용, 글로벌 관점을 위해 인용 네트워크 기반 협업 필터링(ScCF, CcCF) 알고리즘 설계 및 결합
- **재순위 단계(Re-ranking Stage)**: 인용 의도 인식을 통해 추천 문헌 리스트 조정으로 정확도와 제어 가능성 향상
- **인용 문장 생성**: 원본 논문 초록, 로컬 컨텍스트, 인용 의도, 추천 논문 초록을 입력으로 LLM에 LoRA를 통한 지시 미세 조정 수행
- **선호도 정렬**: DPO(Direct Preference Optimization)를 적용하여 생성 결과를 인간 선호도에 정렬 및 고품질 추론 기반 인용 문장 생성

## Originality

- 기존에 분리된 인용 의도 추론과 인용 추천 및 생성을 통합적으로 다루는 다중 단계 프레임워크 제안
- 인용 네트워크의 협업 필터링 알고리즘(ScCF, CcCF)을 새롭게 설계하여 글로벌 정보 활용
- Chain-of-Thought 추론과 DPO 정렬을 결합한 LLM 기반 인용 문장 생성 방식 개발
- 기존 자동 평가 메트릭의 한계를 지적하고 다차원 평가 프레임워크 제안

## Limitation & Further Study

- 논문에서 제시된 두 가지 협업 필터링 알고리즘의 계산 복잡도 분석과 확장성 논의가 미흡함
- 대규모 학술 데이터셋(S2ORC 등)에 대한 실험 검증이 명시적으로 제시되지 않음
- 다양한 학문 분야(예: 생명과학, 공학 등)에 대한 도메인 특화 성능 평가 부재
- 후속 연구에서는 실시간 인용 추천 시스템의 운영 효율성, 새로운 논문에 대한 적응 메커니즘, 다국어 인용 생성으로의 확장을 고려할 수 있음

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3/5
- Overall: 4/5

**총평**: 이 논문은 인용 의도 인식이라는 핵심 개념과 협업 필터링, LLM 미세 조정 및 DPO 정렬 등의 최신 기술을 활용하여 인용 추천과 생성의 일관성 있는 통합 솔루션을 제시한다. 실험적 검증이 포괄적이고 새로운 평가 메트릭 제안도 의의가 있으나, 일부 기술적 세부사항과 도메인별 성능에 대한 심화 분석이 보강되면 더욱 강력한 기여가 될 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/238_Controllable_citation_sentence_generation_with_language_mode/review]] — 제어 가능한 인용 문장 생성을 다단계 인용 추천 및 문장 생성 시스템으로 확장하여 더 포괄적인 학술 글쓰기 지원을 제공한다.
- 🏛 기반 연구: [[papers/329_Explaining_relationships_among_research_papers/review]] — 논문 간 관계 설명 연구가 인용 의도 인식과 네트워크 기반 추천 시스템의 핵심 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 증거 기반 해석 가능한 지역 인용 추천과 의도 기반 다단계 인용 추천이 서로 다른 접근법으로 같은 문제를 해결한다.
- 🏛 기반 연구: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 다중 세분화 인용 추천 시스템 개발을 위한 평가 방법론적 기초를 제공한다.
- 🏛 기반 연구: [[papers/238_Controllable_citation_sentence_generation_with_language_mode/review]] — 제어 가능한 인용 문장 생성 기법이 다단계 인용 추천 및 문장 생성 시스템의 핵심 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/329_Explaining_relationships_among_research_papers/review]] — 논문 간 관계 설명을 인용 의도 인식과 결합하여 더 정교하고 맥락적으로 적절한 학술 글쓰기 지원 시스템을 구축한다.
