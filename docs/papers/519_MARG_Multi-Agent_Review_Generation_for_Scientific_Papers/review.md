---
title: "519_MARG_Multi-Agent_Review_Generation_for_Scientific_Papers"
authors:
  - "Mike D'Arcy"
  - "Tom Hope"
  - "Larry Birnbaum"
  - "Doug Downey"
date: "2024.01"
doi: "10.48550/arXiv.2401.04259"
arxiv: ""
score: 4.0
essence: "본 연구는 여러 LLM 인스턴스 간의 협력적 대화를 통해 과학 논문에 대한 피어 리뷰 피드백을 생성하는 MARG(Multi-Agent Review Generation) 방법을 제안한다. 이를 통해 기본 모델의 입력 길이 제한을 초과하는 긴 논문도 처리할 수 있으며, 제네릭한 피드백 문제를 크게 개선한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/GPT-Based_Text_Review_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/D'Arcy et al._2024_MARG Multi-Agent Review Generation for Scientific Papers.pdf"
---

# MARG: Multi-Agent Review Generation for Scientific Papers

> **저자**: Mike D'Arcy, Tom Hope, Larry Birnbaum, Doug Downey | **날짜**: 2024-01-08 | **DOI**: [10.48550/arXiv.2401.04259](https://doi.org/10.48550/arXiv.2401.04259)

---

## Essence

![Figure 1](figures/fig1.webp) *다중 에이전트 아키텍처 개요: 논문을 여러 청크로 분할하여 각 GPT 인스턴스에 배치*

본 연구는 여러 LLM 인스턴스 간의 협력적 대화를 통해 과학 논문에 대한 피어 리뷰 피드백을 생성하는 MARG(Multi-Agent Review Generation) 방법을 제안한다. 이를 통해 기본 모델의 입력 길이 제한을 초과하는 긴 논문도 처리할 수 있으며, 제네릭한 피드백 문제를 크게 개선한다.

## Motivation

- **Known**: GPT-4와 같은 현대의 대규모 언어 모델(LLM)은 뛰어난 성능을 보유하고 있으나, 과학 논문과 같은 장문의 기술 텍스트 이해 및 생성에 대해서는 충분히 탐구되지 않았다.

- **Gap**: (1) LLM의 제한된 컨텍스트 윈도우로 인해 긴 논문 전체를 입력할 수 없다. (2) 단일 에이전트 방식은 제네릭하고 비구체적인 피드백을 생성한다(기준 방법의 60% 이상이 제네릭 의견).

- **Why**: 효과적인 피어 리뷰는 논문의 의도, 기술적 세부사항, 실험의 타당성 등을 이해하고 구체적인 개선 제안을 제시해야 하는 복잡한 추론을 요구한다.

- **Approach**: 다중 에이전트 아키텍처를 도입하여 (1) 논문을 여러 청크로 분할해 워커 에이전트에 배치하고, (2) 리더 에이전트의 조율 하에 에이전트 간 협력적 대화를 수행하며, (3) 실험(experiments), 명확성(clarity), 영향력(impact) 등 다양한 측면에 특화된 전문가 에이전트를 추가한다.

## Achievement

![Figure 2](figures/fig2.webp) *MARG-S의 구조: 여러 특화된 다중 에이전트 그룹으로 구성되며, 각 그룹의 피드백이 통합 및 정제됨*

1. **정성적 피드백 품질 대폭 개선**: 사용자 연구에서 MARG-S는 논문당 3.7개의 "좋은" 피드백을 생성했으며, 이는 기준 방법(1.7개)의 2.2배, Liang et al. (2023) 방법(0.3개)의 12배에 해당한다.

2. **구체성과 제네릭성 개선**: MARG-S의 71%가 구체적(specific)으로 평가되었으며, 제네릭 피드백 비율을 60%에서 29%로 감소시켰다. 자동화된 평가에서는 가장 강력한 기준 방법 대비 6.1 recall points 향상을 달성했다.

## How

![Figure 5](figures/fig5.webp) *각 방법에 대한 평균 품질 평가: MARG-S가 특이도, 정확성, 전반적 도움성에서 우수함*

- **멀티 에이전트 아키텍처**:
  - **리더 에이전트**: 전체 작업 조율 및 에이전트 간 통신 관리. 고수준 계획을 먼저 수립한 후 워커/전문가 에이전트에 메시지 전송
  - **워커 에이전트**: 논문의 각 청크를 수신하여 할당된 섹션에 대한 피드백 생성
  - **전문가 에이전트**: 특정 피드백 유형(실험 분석, 명확성 개선, 영향력 평가)에 특화된 보조 역할 수행

- **프롬프트 엔지니어링**: 각 에이전트 유형에 고유한 시스템 메시지 제공. 리더 에이전트는 "SEND MESSAGE" 커맨드를 통해 다른 에이전트와 통신하는 프로토콜 사용

- **파이프라인**: (1) 논문을 단락 경계에서 텍스트 청크로 분할, (2) 각 청크에 섹션명과 순서 정보 주석 추가, (3) 특화된 에이전트 그룹이 피드백 생성, (4) 최종 다중 에이전트 그룹이 피드백 정제 및 중복 제거

## Originality

- **새로운 응용**: 다중 에이전트 LLM 상호작용을 긴 기술 문서 처리의 제약 극복에 활용한 첫 시도

- **특화된 에이전트 도입**: 단순한 다중 에이전트 협력을 넘어 서로 다른 리뷰 측면에 특화된 전문가 에이전트를 설계함으로써 성능 향상 (기준 방법 대비 2.2배)

- **실제 문제 해결**: API 기반 LLM의 컨텍스트 제한이라는 실용적 제약 조건에서 아키텍처 수정 없이 해결책 제시

- **포괄적 평가**: 자동 메트릭뿐 아니라 정성적 사용자 연구를 통해 구체성, 정확성, 도움성을 다각도로 검증

## Limitation & Further Study

- **높은 비용**: 다중 에이전트 시스템은 단일 에이전트 대비 상당히 높은 API 호출 비용 소요 (상용화 시 경제성 문제)

- **에이전트 간 통신 오류**: 메시지 누락, 정보 전달 실패 등 에이전트 간 협력 과정에서 발생하는 오류로 인한 성능 저하

- **멀티모달 정보 부재**: 텍스트만 처리 가능하여 논문의 그림, 표, 수식 등 중요한 시각 정보를 활용하지 못함

- **후속 연구 방향**:
  - 더 효율적인 에이전트 간 통신 프로토콜 개발 및 오류 감소
  - 비용 최적화를 위한 경량 모델 적용 가능성 탐색
  - 시각 정보 포함 시 성능 변화 분석
  - 다양한 도메인(생물학, 물리학 등)으로의 확장 성능 평가

## Evaluation

- **Novelty**: 4/5 - 다중 에이전트를 입력 길이 극복에 활용한 창의적 접근이나, 일부 관련 동시 연구 존재

- **Technical Soundness**: 4/5 - 체계적인 설계와 사용자 연구를 통한 검증이 견고하나, 에이전트 간 통신 오류 분석이 제한적

- **Significance**: 5/5 - 과학 커뮤니티에서 급증하는 피어 리뷰 자동화 수요에 직결된 실질적 기여로 높은 영향력 보유

- **Clarity**: 4/5 - 전반적으로 명확한 설명이나, 일부 프롬프트 세부사항은 부록에만 제시

- **Overall**: 4/5

**총평**: 본 논문은 다중 에이전트 LLM 협력을 통해 긴 과학 논문의 구체적 피드백 생성이라는 실질적 문제를 효과적으로 해결한 우수한 연구이다. 사용자 연구로 2.2배의 성능 개선을 실증했으나, 높은 비용과 에이전트 통신 오류라는 한계를 극복해야 한다.

## Related Papers

- 🔗 후속 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 체크리스트 기반 메타리뷰 생성을 다중 에이전트 협력으로 발전시켜 더 포괄적이고 상호보완적인 피어 리뷰 시스템을 구현했다.
- 🔄 다른 접근: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — LLM을 활용한 논문 리뷰 생성의 탐색적 연구와 다중 에이전트 기반 리뷰 생성은 모두 AI 지원 피어 리뷰의 서로 다른 접근법이다.
- 🏛 기반 연구: [[papers/083_AI-Driven_Review_Systems_Evaluating_LLMs_in_Scalable_and_Bia/review]] — 확장 가능한 편향 없는 AI 기반 리뷰 시스템 연구가 다중 에이전트 리뷰 생성의 공정성과 신뢰성 확보 기반을 제공한다.
- 🧪 응용 사례: [[papers/677_Reviewer2_Optimizing_Review_Generation_Through_Prompt_Genera/review]] — 프롬프트 생성을 통한 리뷰 최적화 연구에서 다중 에이전트 협력 메커니즘이 실제 구현된 사례를 보여준다.
- 🏛 기반 연구: [[papers/385_Glimpse_Pragmatically_informative_multi-document_summarizati/review]] — 다중 에이전트 리뷰 생성에서 합의와 차이점 추출이라는 핵심 방법론을 공유한다.
- 🔄 다른 접근: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — LLM 리뷰의 blind spot 분석과 다중 에이전트 협력 리뷰는 모두 AI 기반 리뷰 품질 향상을 다른 방식으로 접근한다.
- 🔄 다른 접근: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 다중 에이전트 리뷰 생성과 달리 단일 생성 모델로 인용 추천 문제를 해결하는 상이한 접근법을 제시한다.
- 🏛 기반 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 다중 에이전트 리뷰 생성의 협력적 접근법이 체크리스트 기반 메타리뷰 생성의 체계적 검증 방법론으로 발전되었다.
