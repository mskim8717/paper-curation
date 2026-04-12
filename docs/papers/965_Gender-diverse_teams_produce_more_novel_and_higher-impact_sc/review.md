---
title: "965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc"
authors:
  - "Yang Yang"
  - "Tanya Y. Tian"
  - "Teresa K. Woodruff"
  - "Benjamin F. Jones"
  - "Brian Uzzi"
date: "2022"
doi: "10.1073/pnas.2200841119"
arxiv: ""
score: 4.0
essence: "의료 과학의 660만 개 논문 분석을 통해 성별 다양성 높은 팀이 동일 규모의 단일 성별 팀보다 더 신규적이고 영향력 있는 연구 결과를 생산함을 입증했다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "sub/Gender_Research_Diversity"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2022_Gender-diverse teams produce more novel and higher-impact scientific ideas.pdf"
---

# Gender-diverse teams produce more novel and higher-impact scientific ideas

> **저자**: Yang Yang, Tanya Y. Tian, Teresa K. Woodruff, Benjamin F. Jones, Brian Uzzi | **날짜**: 2022 | **DOI**: [10.1073/pnas.2200841119](https://doi.org/10.1073/pnas.2200841119)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1A plots the upward trend of women’s participation in medical science from 2000*

의료 과학의 660만 개 논문 분석을 통해 성별 다양성 높은 팀이 동일 규모의 단일 성별 팀보다 더 신규적이고 영향력 있는 연구 결과를 생산함을 입증했다.

## Motivation

- **Known**: 여성 과학자 참여 증가와 팀 과학(Team Science)으로의 전환이 진행 중이며, 실험실 연구에서 혼성 팀이 문제 해결에 우수함이 알려져 있다.
- **Gap**: 현실의 전문적 환경에서 성별 역학이 동일 성별 팀 선호를 유발할 수 있으며, 실험실 연구 결과가 실제 과학 환경에 일반화되는지 불명확하다.
- **Why**: 과학 팀 구성의 변화가 연구 성과와 다양성·포용성(DEI) 정책에 미치는 영향을 이해하는 것이 중요하기 때문이다.
- **Approach**: 2000-2019년 의료 과학 논문 6.6백만 개를 대상으로 이름 기반 성별 추론 알고리즘(Name-to-gender inference method)을 적용하여 팀 구성을 분석하고, 신규성(Novelty)과 영향도(Impact)를 측정했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Fig. 1A plots the upward trend of women’s participation in medical science from 2000*

- **혼성 팀의 급속한 증가**: 2000년 약 60%에서 2019년 70%로 증가했으나 기대값 대비 여전히 17% 정도 과소 대표되어 있다.
- **우수한 성과**: 혼성 팀의 논문이 동등 규모 단일 성별 팀 대비 현저히 높은 신규성과 영향도를 보인다.
- **성별 균형 효과**: 팀의 성별 균형이 높을수록 성과 지표 점수가 우수하다.
- **일반화 가능성**: 의료 분야 45개 세부 분야 전반, 소규모/대규모 팀, 여성/남성 주도 팀 등 거의 모든 상황에서 패턴이 일관되게 나타난다.
- **강건성**: 개별 연구자 고정 효과(Fixed effects), 팀 구조, 네트워크 위치 등 다양한 통제 변수 고려 시에도 결과가 유지된다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1A plots the upward trend of women’s participation in medical science from 2000*

- 6.6백만 개 의료 과학 논문 데이터셋 구축 (15,000개 이상 저널, 20년 기간)
- 이름 기반 성별 추론 알고리즘으로 저자 성별 분류 (확률 기반 추정)
- 혼합 성별(Mixed gender) 이진 변수와 성별 다양성(Gender diversity) 연속 변수 측정
- Null Model(임의 재배치) 설계로 예상 혼성 팀 비율 계산
- 논문별 신규성 측정: 저널 인용 쌍(Journal pairings)의 드물기(Uncommonness) 정도
- 영향도 측정: 논문 인용 수 및 미래 연구에 미치는 영향
- 개별 연구자 고정 효과, 팀 구조, 네트워크 위치를 포함한 회귀 분석

## Originality

- 실험실 환경이 아닌 실제 660만 개 논문이라는 대규모 실제 데이터(Real-world data)를 기반으로 성별 다양성 효과 입증
- Null Model을 통해 관찰된 성별 팀 구성이 기대값 대비 어떻게 벗어나는지 정량화
- 신규성과 영향도를 구분하여 측정하고 별도 분석 (두 지표가 서로 다른 요인으로 구동됨을 인식)
- 45개 의료 분야, 다양한 팀 규모, 팀 리더십 성별 등 다층적 분석을 통한 일반화 가능성 확보

## Limitation & Further Study

- **이진 성별 분류의 한계**: 알고리즘이 남성/여성 이진 분류만 가능하여 비이진 젠더(Non-binary gender) 표현 불가
- **개별 저자 오분류 가능성**: 일부 저자의 성별이 오분류될 수 있으며, SI Appendix 3에서 오류 민감도 분석 시도
- **인과성 vs 상관성**: 연구 설계상 성별 다양성이 신규성/영향도를 **인과적으로** 증가시키는지 확인 어려움 (역인과성 가능)
- **메커니즘 미해명**: 혼성 팀이 왜 더 우수한 성과를 내는지에 대한 구체적 메커니즘(예: 인지 다양성, 상호작용 동학)이 밝혀지지 않음
- **후속 연구 방향**: 성별 다양성과 성과 간 인과관계 규명을 위한 준실험(Quasi-experimental) 설계 필요, 비이진 성별 분류 방법 개발, 팀 상호작용과 의사결정 과정에 대한 심층 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 성별 다양성이 과학 혁신과 영향도에 미치는 긍정적 영향을 대규모 실증 데이터로 명확히 입증한 강력한 연구로, DEI 정책의 과학적 근거를 제공하며 팀 구성의 중요성을 강조한다. 다만 인과성 확인과 메커니즘 해명이 필요하다.

## Related Papers

- ⚖️ 반론/비판: [[papers/940_Bibliometrics_Global_Gender_Disparities_in_Science/review]] — 성별 다양성 팀의 혁신적 연구 생산은 과학계 글로벌 성별 불균형 문제에 대한 해결책으로서 다양성의 긍정적 효과를 보여준다.
- 🔗 후속 연구: [[papers/981_Making_gender_diversity_work_for_scientific_discovery_and_in/review]] — 성별 다양성 팀의 과학적 성과 연구는 성별 다양성이 과학적 발견과 혁신에 효과적으로 작용하도록 하는 방법론적 확장을 제공한다.
- ⚖️ 반론/비판: [[papers/1010_Remote_collaboration_fuses_fewer_breakthrough_ideas/review]] — 다양성이 혁신에 미치는 긍정적 효과와 대조적으로 원격 협업의 혁신 저해 효과를 보여준다.
- 🔗 후속 연구: [[papers/1039_The_Preeminence_of_Ethnic_Diversity_in_Scientific_Collaborat/review]] — 성별 다양한 팀의 혁신적 성과를 인종적 다양성의 관점에서 확장하여 분석한다.
- 🔗 후속 연구: [[papers/1110_A_cross-disciplinary_research_framework_at_institution_level/review]] — 성별 다양성이 과학적 발견에 미치는 긍정적 효과를 분석하여 다학제 협력의 다양성 가치를 보강한다.
- 🔗 후속 연구: [[papers/1066_Accelerating_science_with_human-aware_artificial_intelligenc/review]] — 성별 다양성 팀이 더 혁신적인 과학을 생산한다는 발견을 인간 중심 AI 모델에 통합하여 팀 구성 최적화에 활용할 수 있다.
- 🔗 후속 연구: [[papers/940_Bibliometrics_Global_Gender_Disparities_in_Science/review]] — 전 세계 과학계 성별 불균형 분석은 성별 다양한 팀의 혁신적 연구 생산을 보여준 연구로 확장되어 다양성의 긍정적 효과를 입증한다.
- ⚖️ 반론/비판: [[papers/966_Global_citation_inequality_is_on_the_rise/review]] — 다양성 증진이 혁신을 촉진한다는 관점과 소수 엘리트의 인용 독점 현상 간의 모순을 탐구할 수 있음
- ⚖️ 반론/비판: [[papers/976_Intersectional_inequalities_in_science/review]] — 성별 다양 팀의 혁신성 증대 결과와 교차적 불평등이 연구 성과에 미치는 부정적 영향을 대조하여 다양성의 복잡한 효과를 분석할 수 있다.
- 🔗 후속 연구: [[papers/981_Making_gender_diversity_work_for_scientific_discovery_and_in/review]] — 성별 다양한 팀이 혁신을 촉진한다는 실증 결과를 체계적 프레임워크로 설명할 수 있음
- 🔗 후속 연구: [[papers/1170_Evolution_of_Social_Work_Knowledge_Production_Over_35_Years/review]] — 사회복지 분야의 35년 지식생산 진화를 성별 다양성과 혁신성이라는 더 넓은 과학사회학적 관점으로 확장합니다.
- 🔗 후속 연구: [[papers/1205_Rethinking_team_science_metrics_through_Collaborative_Guidep/review]] — 성별 다양성이 과학적 발견에 미치는 영향을 분석하여 Collaborative Guideposts 프레임워크의 다양성 고려 방안을 보완한다.
