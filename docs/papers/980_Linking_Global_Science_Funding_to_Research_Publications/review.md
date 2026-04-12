---
title: "980_Linking_Global_Science_Funding_to_Research_Publications"
authors:
  - "Jacob Aarup Dalsgaard"
  - "Filipi Nascimento Silva"
  - "Jin AI"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "7.4백만 개의 펀딩 인정(funding acknowledgment) 문자열을 체계적으로 정규화하고 1.9백만 개를 표준 조직 식별자에 매칭하여 글로벌 과학 펀딩과 연구 출판물을 연결하는 대규모 데이터셋을 구축했다."
tags:
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Domain-Specific_Analysis_Studies"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Dalsgaard et al._2026_Linking Global Science Funding to Research Publications.pdf"
---

# Linking Global Science Funding to Research Publications

> **저자**: Jacob Aarup Dalsgaard, Filipi Nascimento Silva, Jin AI | **날짜**: 2026-03-25 | **URL**: [https://arxiv.org/abs/2603.24147v1](https://arxiv.org/abs/2603.24147v1)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the funder name disambiguation pipeline.*

7.4백만 개의 펀딩 인정(funding acknowledgment) 문자열을 체계적으로 정규화하고 1.9백만 개를 표준 조직 식별자에 매칭하여 글로벌 과학 펀딩과 연구 출판물을 연결하는 대규모 데이터셋을 구축했다.

## Motivation

- **Known**: 과학 펀딩은 현대 과학 아키텍처를 구조화하지만, 기존 데이터베이스(IRIS UMETRICS, OpenAlex, Dimensions)는 지역적 편향, 불완전한 커버리지, 투명하지 않은 매칭 알고리즘으로 인해 글로벌 펀딩 분석이 단편적이고 비교 불가능한 상태이다.
- **Gap**: 펀딩 인정은 자유 텍스트로 기록되어 명명 규칙, 약자, 번역, 조직 단위가 다양하게 나타나며, 조화된 글로벌 펀더 신원 매핑과 투명한 정규화 절차가 부재하다.
- **Why**: 펀딩 정보의 체계적 정규화는 펀딩 흐름 추적, 지역별 자금 배분 공평성 평가, 글로벌 연구 시스템의 집중도 분석을 가능하게 하며, 이는 과학 정책 수립과 자금 배분 의사결정에 중요하다.
- **Approach**: 다단계 정규화 파이프라인(어휘 정규화, 유사도 기반 클러스터링, 규칙 기반 매칭, 명명 엔티티 인식, 수동 검증)을 구축하고, WoS, OpenAlex, Dimensions 간 종이 수준의 비교와 전문 텍스트 수동 검증으로 기술 검증을 수행했다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Geographic distribution of funding agencies across biblio-*

- **대규모 정규화 데이터셋 구축**: 7.4백만 개의 펀딩 인정 문자열을 1.9백만 개의 표준 조직 식별자에 매칭하여 투명성을 위해 매칭 타입과 미해결 사례 기록
- **다단계 파이프라인 개발**: 어휘 정규화, MinHash LSH, 규칙 기반 매칭, NER 지원, 유사도 기반 폴백 방식을 통합한 체계적 정규화 방법론 제시
- **기술 검증 수행**: 재현율(recall)과 정확도(precision) 메트릭을 보고하고 세 데이터베이스 간 펀더 표현의 실질적 차이 정량화
- **지역적 불균형 실증**: 특히 저빈도 조직과 글로벌 남부(Global South) 펀더에서 데이터베이스 간 커버리지 편향 증명

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Overview of the funder name disambiguation pipeline.*

- Web of Science CORE-ESCI 2023 스냅샷에서 펀딩 에이전시 필드 추출
- Research Organization Registry(ROR v1.72)의 110,000+ 조직에 대한 표준 식별자 사용
- OpenAlex(2025-09-29 스냅샷)의 Crossref 메타데이터 및 ROR 기반 기관 식별자 활용
- Dimensions 상업 플랫폼의 펀드 데이터베이스 통합 및 텍스트 마이닝 데이터 활용
- 어휘 정규화(대소문자 통일, 구두점 제거), 약자 감지 실행
- MinHash LSH를 이용한 확장성 있는 유사도 기반 클러스터링
- 규칙 기반 매칭 규칙 정의 및 적용
- 명명 엔티티 인식(NER) 모델을 보조 도구로 활용
- 불확실한 경우 유사도 기반 폴백 메서드 적용
- 표본 추출을 통한 수동 검증 및 전문 텍스트 펀딩 섹션과의 비교

## Originality

- 기존 데이터베이스의 편향을 명시적으로 정량화하는 종이 수준의 직접 비교 수행 (WoS vs OpenAlex vs Dimensions)
- 매칭되지 않거나 다중 매칭된 경우를 보존하여 투명성과 하위 유연성을 동시에 확보하는 설계
- 글로벌 남부 펀더의 과소 표현을 구체적으로 증명하고 데이터베이스 선택이 연구 결론에 미치는 영향 명시
- 7.4백만 문자열 규모의 대규모 정규화 과제를 체계적 다단계 파이프라인으로 처리한 방법론적 기여

## Limitation & Further Study

- 펀딩 인정은 완전하지 않으며, 데이터베이스 간 추출 방식(반자동 파이싱 vs 전문 마이닝 vs 그랜트 메타데이터)의 차이로 인한 근본적 커버리지 편향 해결 불가
- 영문 출판물과 비영문 출판물 간 기존 편향(특히 WoS)이 파이프라인으로 완전히 제거되지 않음
- 수동 검증은 표본 기반이므로 전체 데이터셋의 오류율을 완전히 정량화하지 못함
- 펀더 조직의 계층적 구조(예: 지부 vs 모조직) 처리에 대한 명확한 기준 부재
- **후속 연구**: 시계열 펀더 이름 변화 추적, 비영문 펀더명에 대한 다언어 정규화 개선, 기계학습 기반 자동 매칭 모델 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 글로벌 과학 펀딩 데이터의 단편화 문제를 체계적으로 해결하고 투명한 정규화 파이프라인을 제시하여, 과학정책 연구와 펀딩 분석의 재현 가능성을 크게 향상시키는 중요한 데이터 인프라 기여이다.

## Related Papers

- 🔗 후속 연구: [[papers/1036_The_Matthew_effect_in_science_funding/review]] — 글로벌 펀딩 데이터와 매튜 효과 분석을 결합하여 연구 자금 배분의 불평등 구조를 체계적으로 파악할 수 있음
- 🧪 응용 사례: [[papers/964_Funding_the_Frontier_Visualizing_the_Broad_Impact_of_Science/review]] — 표준화된 펀딩 데이터를 활용하여 프론티어 연구 자금 지원의 광범위한 영향을 시각화하고 분석할 수 있음
- 🔄 다른 접근: [[papers/991_Open_Datasets_in_Learning_Analytics_Trends_Challenges_and_Be/review]] — 연구 자금과 출판물 연계 분석과 오픈 데이터셋 현황 분석이 모두 과학 연구의 투명성과 재현성 향상이라는 동일한 목표를 다른 각도에서 접근한다.
- 🏛 기반 연구: [[papers/964_Funding_the_Frontier_Visualizing_the_Broad_Impact_of_Science/review]] — 글로벌 과학 펀딩과 연구 출판물 연결 연구는 펀딩의 다차원적 영향 시각화 시스템 개발의 데이터 연결 방법론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/983_Mapping_Research_Funding_and_Outputs_at_the_Topic_Level_in_t/review]] — 글로벌 과학 자금과 연구 출판물 연결 연구를 북유럽 지역의 주제별 세분화 분석으로 확장하여 지역적 특성을 규명한다.
- 🏛 기반 연구: [[papers/1184_Hamemayu_Hayuning_Nagara_A_Bibliometric_Analysis_of_the_Poli/review]] — 글로벌 과학 펀딩과 연구 성과의 연계를 주제 수준에서 분석한 연구로 VAT 정책과 연구 생산성의 관계를 이해하는 기반을 제공한다.
