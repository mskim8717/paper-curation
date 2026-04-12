---
title: "1017_Science_as_exploration_in_a_knowledge_landscape_tracing_hots"
authors:
  - "Feifan Liu"
  - "Shuang Zhang"
  - "Haoxiang Xia"
date: "2024.04"
doi: "10.1140/epjds/s13688-024-00468-z"
arxiv: ""
score: 4.0
essence: "본 논문은 지리정보시스템(GIS) 기법을 활용하여 과학자들의 연구주제 선택을 지식공간(knowledge space)에서의 탐색 과정으로 모델링하고, 과학자들이 주로 보수적으로 국소적 지식공간을 탐색하는 패턴을 실증적으로 규명한다."
tags:
  - "cat/Academic_Impact_and_Mobility"
  - "sub/Thematic_Network_Detection"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_Science as exploration in a knowledge landscape tracing hotspots or seeking opportunity.pdf"
---

# Science as exploration in a knowledge landscape: tracing hotspots or seeking opportunity?

> **저자**: Feifan Liu, Shuang Zhang, Haoxiang Xia | **날짜**: 2024-04-02 | **DOI**: [10.1140/epjds/s13688-024-00468-z](https://doi.org/10.1140/epjds/s13688-024-00468-z)

---

## Essence

![Figure 3](figures/fig3.webp)

*Figure 3 The aggregated inter-ﬂow of scientists in the knowledge space under two types of tessellations*

본 논문은 지리정보시스템(GIS) 기법을 활용하여 과학자들의 연구주제 선택을 지식공간(knowledge space)에서의 탐색 과정으로 모델링하고, 과학자들이 주로 보수적으로 국소적 지식공간을 탐색하는 패턴을 실증적으로 규명한다.

## Motivation

- **Known**: 과학자의 연구주제 선택이 개인의 인지 제약과 사회적 요인에 의해 영향을 받으며, 이는 과학 생태계의 발전에 중대한 영향을 미친다는 이론적 연구가 존재한다.
- **Gap**: 기존 이론 연구에도 불구하고 현대 과학의 복잡성으로 인해 과학자들의 주제 전환 패턴과 메커니즘을 대규모 실증 데이터로 분석한 연구가 부족하다.
- **Why**: 과학자들의 주제 선택 행동을 이해하면 과학 진보의 메커니즘을 규명할 수 있으며, 과학 정책 설계와 자원 배분 최적화에 중요한 기초를 제공한다.
- **Approach**: 6개 대규모 학문 분야에서 지식공간을 구축하고, GIS 기법과 머신러닝을 통해 과학자들의 주제 전환 궤적을 추적하며, 중력 모델(gravity model)과 복사 모델(radiation model)을 적용하여 전환 패턴을 설명한다.

## Achievement


- **지식공간 기반 궤적 분석 방법론**: Voronoi 다이어그램과 격자(grid) 분할을 통해 과학자들의 출판 궤적을 Origin-Destination(OD) 흐름으로 변환하고 주제 전환 패턴을 정량화하는 방법론을 개발했다.
- **보수적 주제 전환 패턴 발견**: 과학자들의 주제 간 이동 거리가 로그정규분포(log-normal distribution)를 따르며, 장거리 전환이 드물게 발생하는 보수적 탐색 패턴을 실증적으로 규명했다.
- **중력 모델의 우월성 입증**: 복사 모델보다 중력 모델이 과학자들의 주제 전환을 더 잘 설명하며, 연구 강도(research intensity)가 주요 촉진 요인이고 필드 간 지식거리가 주요 장애 요인임을 규명했다.
- **기회 발견의 약한 영향력**: 분야 교집합에서의 혁신 기회에도 불구하고 과학자들이 친숙한 연구 영역을 선호하는 경향을 실증적으로 입증했다.

## How


- 과학 논문 데이터를 주제 거리 기반으로 고차원 지식공간에 임베딩(representation learning 활용)
- 지식공간을 등거리(equidistant) 격자와 등밀도(equal-density) Voronoi 다이어그램으로 분할하여 부분 필드(subfield) 정의
- 과학자별 출판 논문 궤적을 OD 흐름으로 변환하여 주제 전환 패턴 추출
- OD 흐름의 거리 분포 분석 및 생존 분포 함수(CCDF) 계산
- 중력 모델(거리, 인구 크기)과 복사 모델(거리, 기회)을 적용하여 주제 전환 흐름 설명력 비교
- 시뮬레이션 모델링을 통해 연구 강도와 지식거리의 영향 메커니즘 분석

## Originality

- GIS 기법을 추상적 지식공간 분석에 처음 적용하여 과학자의 주제 선택을 물리적 이동 패턴과 유사하게 분석한 혁신적 접근
- 머신러닝 기반 표현 학습(representation learning)으로 필드 간 지식거리를 정량화하여 추상적 지식공간을 실증적으로 매핑한 기술적 기여
- 개인 수준의 보수적 주제 전환 행동과 집단 수준의 사회적 요인(연구 강도) 간의 메커니즘 규명
- 기존 인구 이동 모델(중력, 복사 모델)을 과학 생태계에 적용하여 검증한 이론적 확장

## Limitation & Further Study

- 6개 대규모 학문 분야로 제한되어 있어 더 세분화된 학제(discipline) 또는 특정 분야(예: 신흥 분야)에 대한 분석 결과의 일반화 가능성 제약
- 논문 메타데이터(저자, 키워드 등)만 사용하여 과학자의 실제 인지적 동기, 자금 지원, 지도자-제자 관계 등 직접적 사회적 요인을 포착하지 못함
- 정적 시간 윈도우 분석으로 인해 시간에 따른 지식공간 구조 변화와 주기적 패턴의 동적 진화 분석 부재
- 후속 연구로 시계열 분석(temporal dynamics)을 통한 지식공간의 진화 메커니즘 규명, 개별 과학자의 개인적 배경 정보 통합, 그리고 정책 개입의 효과성 검증이 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 GIS와 머신러닝을 활용하여 과학자의 주제 선택을 지식공간에서의 탐색으로 새롭게 모델링하고, 과학자들이 보수적으로 국소 영역을 탐색하며 혁신적 교집합 영역을 회피하는 경험적 증거를 제시함으로써 과학 생태계의 메커니즘 이해에 중요한 기여를 한다.

## Related Papers

- 🔗 후속 연구: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 비전형적 조합의 과학적 영향과 지식공간 탐색 패턴을 연결하여 혁신의 공간적 메커니즘을 이해할 수 있다.
- 🏛 기반 연구: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 토픽 수준의 과학 지도 작성은 지식공간 모델링의 실증적 기반을 제공한다.
- 🔄 다른 접근: [[papers/1054_Whats_In_Your_Field_Mapping_Scientific_Research_with_Knowled/review]] — 지식 그래프를 통한 과학 연구 매핑은 GIS 기반 접근과 다른 지식공간 구성 방법을 제시한다.
- 🏛 기반 연구: [[papers/1004_Quantifying_spatialtemporal_citation_diffusion_of_individual/review]] — 지식공간에서의 탐색 패턴 이론은 인용 확산의 공간적 모델링에 이론적 기반을 제공한다.
- 🧪 응용 사례: [[papers/1116_Harnessing_the_Power_of_Adversarial_Prompting_and_Large_Lang/review]] — 지식 경관에서 과학 탐험을 추적하는 방법론을 천문학 분야 적대적 프롬프팅 연구에 적용하여 가설 생성의 탐험적 패턴을 분석할 수 있다.
- 🔗 후속 연구: [[papers/986_Mapping_the_changing_structure_of_science_through_diachronic/review]] — 지식 경관에서 핫스팟 추적 연구를 학술지 임베딩을 통한 물리-생명-보건 삼각형의 동적 변화 분석으로 확장한다.
- 🧪 응용 사례: [[papers/936_Atypical_Combinations_and_Scientific_Impact/review]] — 지식의 비전형적 조합 개념은 지식 경관에서 핫스팟을 추적하는 탐험적 과학 연구의 구체적 적용 사례를 제공한다.
