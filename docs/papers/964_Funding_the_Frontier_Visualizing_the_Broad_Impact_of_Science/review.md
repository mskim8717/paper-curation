---
title: "964_Funding_the_Frontier_Visualizing_the_Broad_Impact_of_Science"
authors:
  - "Yifang Wang"
  - "Yifan Qian"
  - "Xiaoyu Qi"
  - "Yian Yin"
  - "Shengqi Dang"
date: "2025.09"
doi: "10.48550/arXiv.2509.16323"
arxiv: ""
score: 4.0
essence: "과학 펀딩(7M 그랜트)과 그 다운스트림 영향(140M 논문, 160M 특허, 10.9M 정책문서 등)을 연결하는 대규모 데이터 기반의 시각분석 시스템(FtF)을 개발하여 펀딩의 다차원적 사회적 영향을 평가하고 의사결정을 지원한다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "sub/Public_Science_Funding"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Funding the Frontier Visualizing the Broad Impact of Science and Science Funding.pdf"
---

# Funding the Frontier: Visualizing the Broad Impact of Science and Science Funding

> **저자**: Yifang Wang, Yifan Qian, Xiaoyu Qi, Yian Yin, Shengqi Dang, Ziqing Qian, Benjamin F. Jones, Nan Cao, Dashun Wang | **날짜**: 2025-09-19 | **DOI**: [10.48550/arXiv.2509.16323](https://doi.org/10.48550/arXiv.2509.16323)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The science ecosystem, from the upstream funding to the science to the broader downstream*

과학 펀딩(7M 그랜트)과 그 다운스트림 영향(140M 논문, 160M 특허, 10.9M 정책문서 등)을 연결하는 대규모 데이터 기반의 시각분석 시스템(FtF)을 개발하여 펀딩의 다차원적 사회적 영향을 평가하고 의사결정을 지원한다.

## Motivation

- **Known**: 기존 연구는 과학 펀딩과 논문 산출의 관계에만 집중하며, 과학의 다운스트림 사회적 영향(정책, 임상시험, 뉴스 등)을 추적하는 연구가 부족하다. 펀딩 정책 수립을 위해 투명하고 포괄적인 영향 평가 도구가 필요하다.
- **Gap**: 펀딩에서 특허, 정책문서, 임상시험, 뉴스미디어 등 다양한 다운스트림 영향으로의 연결고리가 체계적으로 분석되지 못하고 있으며, 펀딩 의사결정자들을 위한 통합적 시각분석 도구가 부재하다.
- **Why**: 과학 펀딩의 사회적 영향을 종합적으로 이해하면 펀딩 정책이 사회 수요와 부합하도록 할 수 있고, 펀더, 정책입안자, 대학지도자 등 다양한 의사결정자의 전략 수립을 지원할 수 있다.
- **Approach**: 대규모 데이터 수집(7M 그랜트를 140M 논문, 160M 특허, 10.9M 정책문서 등과 1.8B 인용링크로 연결)과 과학계량학(SciSci) 및 시각분석(Visual Analytics) 방법론을 결합하여, 다차원 영향지표와 예측모델을 포함한 통합 시각분석 시스템을 설계·개발하였다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: The FtF system UI. The Query View (A) is for data filtering. The Grant View (B) and PI View (C)*

- **대규모 통합 데이터셋**: 7M 연구 그랜트, 140M 논문, 160M 특허, 10.9M 정책문서, 800K 임상시험, 5.8M 뉴스피드를 1.8B 인용링크로 연결하는 최대 규모의 과학 펀딩-영향 데이터베이스 구축
- **다차원 영향 분석 프레임워크**: 학술, 기술, 정책, 임상, 공공인식 등 다양한 차원의 영향지표 정의 및 통합 평가 체계 제안
- **대화형 시각분석 시스템(FtF)**: Query View, Grant View, Impact View 등 조정된 다중 뷰를 통한 직관적 탐색 및 비교 분석 인터페이스 제공
- **예측 모델**: 역사 데이터 기반 머신러닝 모델로 고영향 연구 주제 및 연구자 식별하여 미래 펀딩 기회 제시

## How

![Figure 2](figures/fig2.webp)

*Figure 2: FtF system overview. The system consists of a preprocessing module, an analysis module, and*

- 도메인 전문가(펀더, 연구자, 정책가) 인터뷰를 통해 요구사항 파악
- 다양한 데이터소스(그랜트DB, 논문(SCOPUS), 특허(USPTO), 정책문서, 임상시험, 뉴스) 수집 및 전처리
- 인용 네트워크 기반 연결 및 다차원 영향지표(publication count, citation impact, patent citations, policy mentions 등) 계산
- 신경망 기반 예측모델 학습 및 향후 영향 가능성 점수 부여
- ImpactGlyph 등 혁신적 시각 인코딩과 다중 조정 뷰 설계
- 사례 연구, 전문가 인터뷰, 정량 평가를 통한 시스템 검증

## Originality

- 펀딩의 다운스트림 영향을 처음으로 체계적으로 추적하는 통합 데이터 연결 아키텍처 제시
- 학술-기술-정책-임상-공공인식을 아우르는 5차원 영향 평가 프레임워크 개발
- 복잡한 이질적 네트워크와 다차원 데이터를 직관적으로 탐색할 수 있는 ImpactGlyph 등 혁신적 시각화 설계
- 펀딩 의사결정 지원을 위한 예측 모델 통합으로 과학 정책 수립에 실질적 가치 제공
- 과학계량학과 시각분석의 학제간 통합으로 새로운 과학정책 연구 방향 개척

## Limitation & Further Study

- 데이터 수집의 시간차와 불완전성(특히 장기 영향 측정의 어려움) - 실시간 업데이트 메커니즘과 시계열 분석 강화 필요
- 단편적 영향지표(citation count 등)에 의존으로 질적 영향 평가 미흡 - 정성적 분석과 혼합방법론 도입 필요
- 인과관계 규명의 한계(관측 데이터 기반 인과추론의 어려움) - 대조군 설계 등 준실험적 방법 고려 필요
- 특정 국가·분야 데이터 편향 가능성 - 글로벌 데이터 수집 확대 및 지역별 검증 필요
- 예측 모델의 흑박스성 - 해석가능성(Explainable AI) 개선으로 신뢰성 제고 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 과학 펀딩의 사회적 영향을 최초로 체계적으로 추적·분석하는 대규모 통합 데이터 기반 시각분석 시스템을 제시함으로써, 과학정책 수립과 펀딩 의사결정에 혁신적 도구를 제공한다. 과학계량학과 시각분석의 효과적 통합, 5차원 영향 평가 프레임워크, 그리고 실제 의사결정자 피드백 기반 검증으로 높은 학술·실무적 가치를 실현한다.

## Related Papers

- 🔄 다른 접근: [[papers/996_Partisan_disparities_in_the_funding_of_science_in_the_United/review]] — 과학 펀딩의 다차원적 영향 분석과 정당별 펀딩 격차 분석은 과학 투자 정책을 다른 관점에서 평가한다.
- 🏛 기반 연구: [[papers/1002_Public_use_and_public_funding_of_science/review]] — 과학의 공공 활용과 공공 펀딩에 대한 이론적 논의가 펀딩 영향 시각화 시스템의 필요성을 뒷받침한다.
- 🔗 후속 연구: [[papers/1016_Sci2Pol_Evaluating_and_Fine-tuning_LLMs_on_Scientific-to-Pol/review]] — 과학-정책 연결 평가 모델을 LLM을 활용한 자동화된 분석으로 확장하여 더 효율적인 영향 추적이 가능하다.
- 🏛 기반 연구: [[papers/1082_The_Open_Catalyst_2022_OC22_Dataset_and_Challenges_for_Oxide/review]] — 과학 연구 자금 지원의 광범위한 영향 분석이 촉매 연구 데이터셋 구축을 뒷받침함
- 🔗 후속 연구: [[papers/1111_A_Strategic_Guide_to_White_Space_Analysis_for_Pharmaceutical/review]] — 기초 과학 펀딩의 광범위한 영향을 시각화하는 방법론을 제약 R&D의 특허-임상 데이터 통합 분석으로 확장한다.
- 🧪 응용 사례: [[papers/931_AI-Driven_Automation_Can_Become_the_Foundation_of_Next-Era_S/review]] — 과학 연구 프런티어 자금 지원 패턴 분석에 AI4SoS 자동화 프레임워크를 적용할 수 있다.
- 🔄 다른 접근: [[papers/996_Partisan_disparities_in_the_funding_of_science_in_the_United/review]] — 정당별 과학 펀딩 격차와 펀딩 영향 시각화는 모두 과학 투자 정책을 서로 다른 관점에서 분석한다.
- 🔗 후속 연구: [[papers/975_Interdisciplinary_papers_supported_by_disciplinary_grants_ga/review]] — 연구 자금 지원의 시각화와 광범위한 영향 분석을 통해 학제간 그랜트 전략의 효과를 더 깊이 이해할 수 있다.
- 🧪 응용 사례: [[papers/980_Linking_Global_Science_Funding_to_Research_Publications/review]] — 펀딩 인정 문자열의 체계적 정규화 데이터셋을 과학 연구의 광범위한 영향 시각화 연구에 실제 적용할 수 있습니다.
- 🔄 다른 접근: [[papers/983_Mapping_Research_Funding_and_Outputs_at_the_Topic_Level_in_t/review]] — 북유럽 지역의 세부적 분석과 글로벌 차원의 연구 자금 시각화라는 서로 다른 규모와 범위에서 자금-성과 관계를 탐구한다.
- 🔗 후속 연구: [[papers/1184_Hamemayu_Hayuning_Nagara_A_Bibliometric_Analysis_of_the_Poli/review]] — VAT 정책과 공공 복지 조화 분석이 과학 연구 자금 지원의 광범위한 영향 시각화로 확장될 수 있다.
- 🔗 후속 연구: [[papers/1135_AI-Augmented_Mobile_and_Data-Driven_Decision_Making_in_Busin/review]] — AI와 SDG의 연결을 매핑하는 연구가 혁신적 논문이 사회적 주목을 받는 현상을 지속가능성 맥락으로 확장한다.
