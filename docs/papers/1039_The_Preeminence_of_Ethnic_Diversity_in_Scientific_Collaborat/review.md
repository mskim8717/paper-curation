---
title: "1039_The_Preeminence_of_Ethnic_Diversity_in_Scientific_Collaborat"
authors:
  - "Bedoor K. AlShebli"
  - "Talal Rahwan"
  - "Wei Lee Woon"
date: "2018"
doi: "10.1038/s41467-018-07634-8"
arxiv: ""
score: 4.0
essence: "920만 개 논문과 610만 명 과학자를 분석하여 인종적 다양성(ethnic diversity)이 과학 협업의 영향력(citation impact)과 가장 강한 양의 상관관계(r=0.77)를 보임을 규명했다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "sub/Research_Collaboration_Networks"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/AlShebli et al._2018_The Preeminence of Ethnic Diversity in Scientific Collaboration.pdf"
---

# The Preeminence of Ethnic Diversity in Scientific Collaboration

> **저자**: Bedoor K. AlShebli, Talal Rahwan, Wei Lee Woon | **날짜**: 2018 | **DOI**: [10.1038/s41467-018-07634-8](https://doi.org/10.1038/s41467-018-07634-8)

---

## Essence

![Figure 3](figures/fig3.webp)

*Fig. 3 Group and individual diversity vs. impact in each subﬁeld. In each subplot, the points correspond to subﬁelds, th*

920만 개 논문과 610만 명 과학자를 분석하여 인종적 다양성(ethnic diversity)이 과학 협업의 영향력(citation impact)과 가장 강한 양의 상관관계(r=0.77)를 보임을 규명했다.

## Motivation

- **Known**: 다양성이 사회적, 경제적 이점을 가져오며 학계에서 공저자 선택이 관찰 가능하지만, 어떤 형태의 다양성이 과학적 성과에 가장 기여하는지 미해명 상태였다.
- **Gap**: 인종, 성별, 학문분야, 소속, 학문 경력 등 다양한 다양성 차원 간 상대적 중요성 비교 부재 및 동질성(homophily) 패턴과 시간에 따른 변화 추이 미분석 상태.
- **Why**: 객관적 데이터 기반 다양성 가치 평가는 정책 수립 및 채용 결정에 필수적이며, 감정과 정치성이 가려진 과학적 근거 제시가 중요하다.
- **Approach**: Microsoft Academic Graph 데이터셋을 활용하여 무작위 기준선 모델(randomized baseline model)로 동질성을 정량화하고, 정확한 짝짓기(coarsened exact matching)를 통해 인종 다양성의 인과적 영향을 분리했다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3 Group and individual diversity vs. impact in each subﬁeld. In each subplot, the points correspond to subﬁelds, th*

- **동질성 규명**: 인종, 성별, 소속 측면에서 명확한 동질성 존재 확인, 특히 인종 동질성은 시간에 따라 증가 추세
- **강한 상관성 발견**: 5가지 다양성 유형 중 인종 다양성이 과학 영향력과 가장 강한 상관관계(r=0.77) 보유
- **인과성 입증**: 논문 수준에서 10.63%, 과학자 수준에서 47.67%의 영향력 증가를 정확한 짝짓기로 검증
- **집단 vs 개인 효과**: 개인의 협력자 다양성이 단일 논문의 저자 다양성보다 더 큰 영향력 미침

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 Exploring homophily in real vs. randomized data. Each column corresponds to a different class of diversity, and e*

- Microsoft Academic Graph 데이터셋에서 1,045,401개 다중저자 논문, 1,529,279명 과학자, 8개 주요 분야 분석
- Gini Impurity를 이용한 다양성 지수(dG_eth, dG_age, dG_gen, dG_dsp, dG_aff) 정의
- 속성(인종/성별/소속/학문 경력)별 무작위 기준선 모델 생성으로 동질성 정량화
- 5년 내 인용 횟수(cG_5)를 과학적 영향력 지표로 설정
- 회귀 분석(regression analysis) 및 정확한 짝짓기(coarsened exact matching)로 인과 관계 검증
- 시간, 저자 수, 협력자 수 등 다양한 차원에서 민감도 분석 수행

## Originality

- 단일 속성이 아닌 5가지 다양성 차원을 체계적으로 비교 분석한 최초의 대규모 연구
- 무작위 기준선 모델을 통한 동질성과 인과성 분리 방법론의 혁신적 적용
- 개인 수준 다양성(individual diversity)과 집단 수준 다양성(group diversity)의 구분과 비교
- 920만 개 논문 규모의 전 방위 시계열 및 세부 분야별 분석으로 강건성 입증

## Limitation & Further Study

- 인종 분류가 이름 기반 추론에 의존하여 오류 가능성 존재
- 상관관계 도출이지 인과관계 증명이 아니며, 논문 품질이나 문제의 난이도 등 혼재 변수(confounding variables) 완전 제어 불가
- 5년 인용 기간은 학문분야별 특성(장기 영향력 논문 누락 가능) 미반영
- 후속연구: 인종 분류 정확도 개선, 학문분야별 맞춤형 시간 창(time window) 설정, 논문 주제와 방법론 특성 추가 제어 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 대규모 데이터와 엄격한 통계 방법론을 통해 인종 다양성이 과학적 성과의 주요 결정 요인임을 처음으로 객관적으로 입증했으며, 다양성 정책의 과학적 근거를 제공하는 높은 영향력의 연구이다.

## Related Papers

- ⚖️ 반론/비판: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 소수집단의 혁신이 과소평가된다는 발견과 인종적 다양성이 협업 영향력을 높인다는 결과를 대조한다.
- 🔗 후속 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 성별 다양한 팀의 혁신적 성과를 인종적 다양성의 관점에서 확장하여 분석한다.
- 🏛 기반 연구: [[papers/1010_Remote_collaboration_fuses_fewer_breakthrough_ideas/review]] — 다양성이 협업에 미치는 긍정적 효과를 원격 협업의 혁신 제약과 비교하는 기준을 제공한다.
- 🔗 후속 연구: [[papers/1010_Remote_collaboration_fuses_fewer_breakthrough_ideas/review]] — 인종적 다양성이 협업 영향력을 높이는 발견을 원격 협업 환경에서 재검토할 필요성을 제시한다.
- ⚖️ 반론/비판: [[papers/1029_The_altering_landscape_of_USChina_science_collaboration_from/review]] — 과학 협력에서 민족 다양성의 우월성과 미중 협력 발산은 상반된 국제 협력 트렌드를 보여준다.
- ⚖️ 반론/비판: [[papers/1032_The_Diversity-Innovation_Paradox_in_Science/review]] — 인종적 다양성이 협업 영향력을 높인다는 발견과 소수집단 혁신이 과소평가된다는 역설을 대조한다.
- 🔗 후속 연구: [[papers/1046_The_structure_of_scientific_collaboration_networks/review]] — 과학 협력 네트워크의 구조적 특성을 인종적 다양성의 영향력 관점에서 확장하여 분석한다.
- 🔄 다른 접근: [[papers/976_Intersectional_inequalities_in_science/review]] — 과학 협력에서 민족 다양성의 우월성 연구와 교차적 정체성 불평등 분석을 비교하여 다양성의 복합적 효과를 파악할 수 있다.
