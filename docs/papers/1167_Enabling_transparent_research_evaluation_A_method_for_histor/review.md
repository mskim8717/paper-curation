---
title: "1167_Enabling_transparent_research_evaluation_A_method_for_histor"
authors:
  - "Fabian Haupt"
  - "J. Senge"
  - "Hendrik von Tengg-Kobligk"
  - "W. Bosbach"
date: "2026"
doi: "10.1371/journal.pone.0340697"
arxiv: ""
score: 4.0
essence: "NIH 데이터베이스의 공개 메타데이터로부터 역사적 RCR(Relative Citation Ratio) 데이터를 추출하는 Python 기반 방법을 제시하여, 연구 평가의 투명성과 책임성을 향상시킨다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Research_Reproducibility_Crisis"
  - "topic/scisci"
---

# Enabling transparent research evaluation: A method for historical RCR retrieval using public NIH metadata

> **저자**: Fabian Haupt, J. Senge, Hendrik von Tengg-Kobligk, W. Bosbach | **날짜**: 2026 | **DOI**: [10.1371/journal.pone.0340697](https://doi.org/10.1371/journal.pone.0340697)

---

## Essence


NIH 데이터베이스의 공개 메타데이터로부터 역사적 RCR(Relative Citation Ratio) 데이터를 추출하는 Python 기반 방법을 제시하여, 연구 평가의 투명성과 책임성을 향상시킨다.

## Motivation

- **Known**: NIH에서 도입한 RCR은 동일 연구 분야의 논문 간 상대적 인용 영향력을 측정하는 지표이며, 현재의 RCR 값은 열람 가능하지만 역사적 데이터는 직접적으로 접근하기 어렵다.
- **Gap**: NIH 데이터베이스 내에 존재하는 역사적 RCR 데이터가 연구자들이 직접 접근할 수 있는 방식으로 공개되지 않아, 장시간에 걸친 논문의 인용 영향력 추이를 분석하기 어렵다.
- **Why**: DORA(Declaration on Research Assessment)와 개방과학(open science) 이니셔티브의 목표에 부응하여 학술 평가에서 메트릭스의 투명하고 책임감 있는 사용을 가능하게 한다.
- **Approach**: Python 기반 자동화 도구를 개발하여 NIH 데이터베이스에서 RCR 데이터를 추출하고, 데이터베이스 도입 이후 모든 시점의 RCR 값을 시각화한다.

## Achievement


- **역사적 RCR 데이터 복구**: 기존에 직접 접근 불가능했던 NIH 데이터베이스의 역사적 RCR 데이터를 체계적으로 추출하는 방법론 개발
- **자동화 솔루션**: Python 기반 도구를 통해 반복적이고 확장 가능한 데이터 복구 프로세스 구현
- **시계열 시각화**: 논문 발표 이후 시간 경과에 따른 RCR 값의 동적 변화를 추적 및 시각화
- **투명한 평가 지원**: figshare에 공개된 원본 데이터로 연구 평가의 재현성과 투명성 보장

## How


- NIH 공개 메타데이터베이스에 접근하여 구조화된 RCR 데이터 추출
- Python 스크립트를 활용한 자동화된 데이터 수집 및 정제 파이프라인 구축
- 시간 축(월별/연도별)에 따른 RCR 값 변화를 그래프로 도시
- 추출된 원본 데이터를 figshare(DOI: 10.6084/m9.figshare.30067852)에 공개

## Originality

- NIH의 폐쇄된 RCR 데이터를 공개 메타데이터로부터 체계적으로 복구하는 새로운 접근법
- 기존에 취할 수 없었던 역사적 인용 메트릭 데이터의 장시간 추적 분석 가능성 제시
- DORA와 개방과학의 원칙을 구체적으로 구현하는 실제 사례 제공

## Limitation & Further Study

- NIH 데이터베이스의 구조 변경 시 방법론의 유지보수 필요성
- 추출 방법이 NIH 데이터베이스에 특화되어 다른 데이터 제공자로의 일반화 가능성 제한
- 역사적 데이터의 완전성과 정확성 검증 절차에 대한 상세한 논의 부족
- 후속 연구: 다양한 계량학적 지표(h-index, IF 등)에 대한 유사한 방법론 개발 및 국제적 확대

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 NIH의 폐쇄된 RCR 데이터에 대한 접근성 문제를 해결하는 실용적인 방법론을 제시하여, 연구 평가의 투명성 향상에 직접적으로 기여한다. DORA와 개방과학 이니셔티브의 목표 달성을 위한 구체적이고 재현 가능한 솔루션이라는 점에서 의미 있는 연구이다.

## Related Papers

- 🏛 기반 연구: [[papers/1009_Relative_Citation_Ratio_A_New_Metric_That_Uses_Citation_Rate/review]] — RCR 메트릭에 대한 기본 개념과 이론적 배경을 제공하여 역사적 데이터 추출 방법의 토대가 됩니다.
- 🧪 응용 사례: [[papers/1204_Rethinking_Research_Evaluation_in_India_Is_the_Ecosystem_Rea/review]] — 투명한 연구 평가 방법론을 인도의 연구 생태계 재고라는 구체적 맥락에 적용한 사례입니다.
- 🔗 후속 연구: [[papers/1052_Updated_science-wide_author_databases_of_standardized_citati/review]] — 표준화된 인용 데이터베이스 연구를 확장하여 투명한 연구 평가를 위한 구체적 방법론을 제시한다.
- 🧪 응용 사례: [[papers/1182_Governing_Science_through_Evaluation_A_Global_Heuristic_of_R/review]] — 글로벌 연구 평가 체계 분석에 필요한 투명한 데이터 추출 방법을 제공하여 비교 연구의 실증적 기반을 마련한다.
- 🏛 기반 연구: [[papers/1192_Large_language_models_and_responsible_research_evaluation_an/review]] — 투명한 연구 평가 방법론의 역사적 분석이 LLM 기반 평가 시스템의 윤리적 프레임워크 설계에 중요한 기반을 제공한다.
- 🔗 후속 연구: [[papers/1182_Governing_Science_through_Evaluation_A_Global_Heuristic_of_R/review]] — 투명한 연구 평가 방법론을 제시하여 글로벌 연구 평가 체계의 투명성과 책임성 향상 방안을 보완한다.
- 🔗 후속 연구: [[papers/1204_Rethinking_Research_Evaluation_in_India_Is_the_Ecosystem_Rea/review]] — 투명한 연구 평가 방법론을 제시하여 인도의 책임 있는 연구 평가 도입에 필요한 구체적 도구를 보완한다.
- 🏛 기반 연구: [[papers/1156_Correction_Enabling_transparent_research_evaluation_A_method/review]] — 원본 논문의 투명한 연구 평가 방법론이 데이터 가용성 수정을 통해 재현가능성을 높임
