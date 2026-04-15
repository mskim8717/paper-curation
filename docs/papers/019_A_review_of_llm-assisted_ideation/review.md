---
title: "019_A_review_of_llm-assisted_ideation"
authors:
  - "Sitong Li"
  - "Stefano Padilla"
  - "Pierre Le Bras"
  - "Junyu Dong"
  - "Mike J. Chantler"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)을 활용한 아이디에이션(ideation) 지원에 관한 61개 연구를 체계적으로 검토하고, 아이디에이션 프로세스의 7단계와 3단계를 포함하는 '모래시계 아이디에이션 프레임워크(Hourglass Ideation Framework)'를 제시한다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Research_Ideation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2025_A review of llm-assisted ideation.pdf"
---

# A review of llm-assisted ideation

> **저자**: Sitong Li, Stefano Padilla, Pierre Le Bras, Junyu Dong, Mike J. Chantler | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2503.00946](https://arxiv.org/abs/2503.00946)

---

## Essence

![Figure 3](figures/fig3.webp)

*Figure 3. The Hourglass Ideation Framework for LLM-assisted Ideation. The hourglass shape of the framework visualizes*

본 논문은 대규모 언어모델(LLM)을 활용한 아이디에이션(ideation) 지원에 관한 61개 연구를 체계적으로 검토하고, 아이디에이션 프로세스의 7단계와 3단계를 포함하는 '모래시계 아이디에이션 프레임워크(Hourglass Ideation Framework)'를 제시한다.

## Motivation

- **Known**: 전통적 브레인스토밍 및 아이디어 관리 시스템이 광범위하게 도입되었으며, 기계학습 기반 보조 아이디에이션 도구들이 개발되었다. 그러나 이러한 접근법들은 인지적 편향 극복 및 대규모 아이디어 평가에 어려움을 겪고 있다.
- **Gap**: LLM의 아이디에이션 지원 능력에도 불구하고, 어느 단계에서 활용되는지, 인간-시스템 상호작용 설계가 어떻게 이루어지는지 체계적으로 분석한 연구가 부족하다. 특히 그룹 협업과 다중 모달리티 상호작용 설계는 미흡한 상태이다.
- **Why**: LLM의 자연어 처리 능력은 고정관념 극복, 광대한 문제 공간 탐색, 신규성 있는 아이디어 생성을 촉진할 수 있으며, 이를 체계적으로 이해하면 더 효율적인 아이디에이션 시스템 개발에 기여할 수 있다.
- **Approach**: Web of Science, Scopus 등 4개 데이터베이스에서 체계적 문헌 탐색을 수행하여 61개 논문을 선별하였고, 제안된 모래시계 프레임워크를 기준으로 각 연구의 아이디에이션 단계별 LLM 활용 방식, 상호작용 설계, 사용자 연구 방법을 분석하였다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Publication Statistics of Analysed Papers*

- **모래시계 아이디에이션 프레임워크 제시**: 아이디에이션 프로세스를 준비-개발-평가 3단계와 범위 규정, 기초 자료 구조화, 아이디어 생성, 아이디어 정제, 다중 아이디어 평가 및 선택, 최종 평가, 실행 7개 세부 단계로 체계화
- **LLM 활용 현황 분석**: 아이디어 생성과 정제에는 빈번히 사용되나, 범위 규정(scope specification)과 기초 자료 구조화에는 제한적으로 활용되는 불균형을 발견
- **상호작용 설계 연구**: 개인 아이디에이션과 텍스트 기반 상호작용이 주를 이루며, 다중모달(multimedia) 요소 통합 추세가 증가하지만 그룹 협업(동기/비동기) 도구는 부족함을 규명
- **포괄적 메타 분석**: 창의성 도메인, 발행 매체, 사용자 연구 설계, 평가 방법 등 61개 연구의 상세 카탈로그 작성 및 온라인 자료 제공

## How

![Figure 1](figures/fig1.webp)

*Figure 1. PRISMA Flow Diagram for Screening*

- PRISMA 지침에 따른 체계적 문헌 검토 프로토콜 적용
- 포함 기준: LLM을 활용하여 아이디에이션을 지원하는 학술 논문
- 배제 기준: 교과서, 워크숍, 리뷰 논문, 아이디에이션 미지원 연구, LLM 비사용 연구 제외
- 4개 데이터베이스(Web of Science, Scopus, ACM Digital Library, DOAJ) 검색
- 초록/전문 스크리닝을 통한 2단계 선별 과정
- 모래시계 프레임워크를 분석 틀로 활용한 질적·양적 데이터 추출
- Figure 1의 PRISMA 플로우 다이어그램에 따른 체계적 절차 문서화

## Originality

- LLM 아이디에이션 지원의 단계별 특성을 명시적으로 분류한 첫 번째 포괄적 체계적 검토
- 기존의 6단계 기업 아이디어 관리 프레임워크를 개선하여 LLM 특성을 반영한 7단계 프레임워크 개발
- 상호작용 설계(interaction design) 차원에서 개인/그룹 협업, 모달리티(text, multimedia, multimodal) 분류
- 사용자 연구 방법론(user study design), 평가 방법(assessment methods)의 체계적 분류

## Limitation & Further Study

- 61개 논문 분석이 빠르게 확장 중인 필드를 완전히 포착하지 못했을 가능성
- LLM 아이디에이션 시스템의 실제 효과성(effectiveness) 측정에 관한 메타분석 부족
- 문화적 맥락, 다언어(multilingual) LLM 활용에 대한 분석 미흡
- 후속 연구 방향: (1) 범위 규정과 기초 자료 구조화 단계의 LLM 활용 방안 개발, (2) 동기/비동기 그룹 협업 도구 설계, (3) LLM 아이디에이션의 장기적 창의성 영향 평가, (4) 멀티모달·인터랙티브 상호작용 모델 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 리뷰는 빠르게 성장하는 LLM 아이디에이션 분야의 현황을 최초로 체계적으로 정리하고, 모래시계 프레임워크를 통해 단계별 활용 격차를 명확히 규명하여 향후 연구 및 개발의 방향성을 제시하는 중요한 기여를 한다.

## Related Papers

- 🔗 후속 연구: [[papers/425_Improving_research_idea_generation_through_data_An_empirical/review]] — 데이터 기반 연구 아이디어 생성 개선과 LLM 지원 아이디에이션 조사를 결합하면 더 효과적인 창의적 발상 지원 시스템을 구축할 수 있다.
- 🧪 응용 사례: [[papers/442_Iris_Interactive_research_ideation_system_for_accelerating_s/review]] — 아이디에이션 프레임워크를 대화형 연구 아이디어 시스템에 적용하여 연구자의 창의적 사고 과정을 체계적으로 지원할 수 있다.
- 🏛 기반 연구: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — LLM 기반 아이디어 생성의 포괄적 리뷰를 통해 Nova의 반복적 계획 및 검색 접근법의 이론적 배경과 기존 연구와의 관계를 제공함
