---
title: "970_Historical_Comparison_of_Gender_Inequality_in_Scientific_Car"
authors:
  - "Junming Huang"
  - "Alexander J. Gates"
  - "Roberta Sinatra"
  - "Albert-László Barabási"
date: "2020"
doi: "10.1073/pnas.1914221117"
arxiv: ""
score: 4.0
essence: "1955-2010년 간 150만 명 이상의 과학자 데이터를 분석하여 STEM 분야 전 학문과 83개국에 걸친 성별 불평등의 장기 추이를 규명했다. 역설적으로 여성 과학자 비율 증가가 생산성(productivity)과 영향력(impact)의 성별 격차 증가를 동반했으나, 동일한 논문 수에 대해 남녀의 연간 발표율(annual rate)과 커리어 영향력이 동등함을 발견했다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "sub/Gender_Research_Diversity"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2020_Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines.pdf"
---

# Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines

> **저자**: Junming Huang, Alexander J. Gates, Roberta Sinatra, Albert-László Barabási | **날짜**: 2020 | **DOI**: [10.1073/pnas.1914221117](https://doi.org/10.1073/pnas.1914221117)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1.*

1955-2010년 간 150만 명 이상의 과학자 데이터를 분석하여 STEM 분야 전 학문과 83개국에 걸친 성별 불평등의 장기 추이를 규명했다. 역설적으로 여성 과학자 비율 증가가 생산성(productivity)과 영향력(impact)의 성별 격차 증가를 동반했으나, 동일한 논문 수에 대해 남녀의 연간 발표율(annual rate)과 커리어 영향력이 동등함을 발견했다.

## Motivation

- **Known**: 학계의 성별 차이는 널리 문서화되었으나 대부분 특정 국가, 학문, 기관의 활동 과학자 부분집합에 한정된 사례연구에 불과했다. 여성 과학자들이 남성에 비해 적게 발표하고 인용도 적다는 '생산성 퍼즐(productivity puzzle)'이 보고되어 왔다.
- **Gap**: 완전한 커리어 출판 이력 재구성의 방법론적 난제로 인해 전 학문 분야와 국가를 아우르는 종단적(longitudinal), 학문적, 지리적 전경이 부재했다. 작은 표본크기에서 무거운 꼬리 분포(heavy-tailed distribution)의 효과가 증폭되는 한계가 있었다.
- **Why**: 성별 불평등의 근본 원인을 이해하기 위해서는 전체 커리어 궤적을 추적할 수 있는 대규모 데이터 기반 분석이 필수적이며, 이는 학계 제도 개선과 정책 수립에 중요한 시사점을 제공할 수 있다.
- **Approach**: Web of Science 데이터베이스에서 1900-2016년 786만 명 과학자의 출판 기록을 수집하고, 머신러닝 기반 성별 식별 방법으로 356만 명 이상의 저자 성별을 판정했다. 1955-2010년 사이 커리어가 종료된 152만 명 과학자의 완전한 출판 이력을 재구성하여 비교분석했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2.*

- **성별 참여 증가와 격차 역설**: 지난 60년간 여성 과학자 비율이 12%(1955)에서 35%(2005)로 증가했으나, 동시에 생산성과 영향력의 성별 격차도 함께 증가했다.
- **성별 불변성 발견**: 남녀 과학자가 연간 동일한 속도로 논문을 발표하며, 동일한 규모의 논문집에 대해 동등한 커리어 영향력을 가지고 있다 (gender invariants).
- **커리어 길이와 탈락률의 설명력**: 생산성과 영향력의 커리어 누적 차이의 대부분은 여성의 단축된 커리어 길이(career length)와 높은 탈락률(dropout rate)로 설명되며, 이는 지속 가능성(sustainability) 문제를 지시한다.
- **광범위한 학문-국가 간 일관성**: 13개 주요 학문과 83개국 모두에서 성별 생산성 격차가 관찰되며, 특히 수학/물리/컴퓨터과학(15%)과 심리학(33%) 간 여성 비율 차이가 뚜렷하다.
- **상위 저자층에서 심화된 격차**: 상위 20% 생산성 저자에서 남성이 여성보다 37% 더 많이 발표하나, 중간층과 하위층에서는 격차가 없거나 역전된다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1.*

- Web of Science (WoS) 데이터베이스에서 1900-2016년 출판 기록 조회
- 머신러닝 기반 상태-최신 성별 식별 방법 적용 (state-of-the-art gender identification method)
- 1955-2010년 커리어 종료 과학자 152만 3천여 명 선별 (여성 41만 2천, 남성 111만)
- 연간 생산성(yearly productivity), 총 생산성(total productivity), 10년 후 인용 수(citations after 10 years c₁₀) 추출
- 커리어 길이(career length) 계산: 첫 논문과 마지막 논문 사이 기간
- 상대 성별 격차(relative gender difference) = (남성 평균 - 여성 평균) / 여성 평균
- Microsoft Academic Graph (MAG)와 DBLP 데이터셋에서 독립적 재현(replication) 수행
- t-test 등 통계적 유의성 검증 (P < 10⁻⁴)

## Originality

- 전례 없는 규모의 완전한 커리어 출판 이력 재구성: 단편적 사례연구를 벗어나 83개국, 13개 학문, 152만 명의 종단 데이터 통합 분석
- 성별 불변성(gender invariants) 개념의 발견: 동일 논문 수 조건에서 남녀의 연간 발표율과 커리어 영향력이 동등하다는 역직관적 통찰
- 생산성 퍼즐의 재해석: 절대 생산성 차이가 아닌 커리어 지속성 문제로서의 재프레이밍은 정책 방향을 근본적으로 전환
- 다중 데이터셋 독립 재현(WoS, MAG, DBLP): 데이터베이스 편향과 저자 동명이인(disambiguation) 오류에 대한 견고성 입증
- 계층별, 학문별, 국가별, 기관순위별 다차원 분층 분석으로 일반화 가능성 강화

## Limitation & Further Study

- **데이터 커버리지 편향**: 중국, 일본, 한국, 브라질, 말레이시아, 싱가포르 저자가 체계적으로 누락되어 비서구권 과소 표현
- **출판 활동 한정**: 교육, 행정, 산업 연구, 정부 연구 활동은 포착 불가능하며 출판 커리어만 분석
- **성별 이진 분류**: 비이분법적 성별 정체성, 문화적 성명 차이(예: 동아시아 가족명)로 인한 성별 식별 오류 가능성
- **생존 편향**: 1955-2010년 커리어 종료자만 대상으로 진행 중인 활동 과학자 제외
- **인과관계 미분석**: 상관관계 기반이며, 탈락이 의도적 선택인지 제도적 배제인지 미분석
- **후속연구 제언**: (1) 커리어 단축과 탈락의 원인 심층 질적 분석, (2) 육아 휴직, 겸임금지(dual-career) 정책 효과 측정, (3) 피어 리뷰와 협력 네트워크의 성별 편향 분석, (4) 비서구권 데이터 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: STEM 분야 성별 불평등에 대한 가장 포괄적인 종단 분석으로, 생산성 퍼즐의 새로운 해석(커리어 지속성 문제)을 제시하여 학계 정책과 제도 개혁의 방향을 재설정하는 혁신적 연구이다. 다만 비서구권 데이터 누락과 인과 메커니즘 분석의 미흡이 후속 심층 연구의 기초가 될 것이다.

## Related Papers

- 🔗 후속 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 성별 불평등의 역사적 패턴 분석을 성별 다양성이 실제 연구 성과에 미치는 효과 연구로 발전시킨다.
- 🔄 다른 접근: [[papers/966_Global_citation_inequality_is_on_the_rise/review]] — 성별 차원의 불평등과 전반적 인용 불평등은 과학계 불평등을 서로 다른 관점에서 조명한다.
- 🏛 기반 연구: [[papers/1059_Women_are_credited_less_in_science_than_men/review]] — 여성이 과학에서 적게 인정받는 현상이 장기적 성별 불평등 패턴의 지속적 원인임을 보여준다.
- 🔗 후속 연구: [[papers/1026_Systematic_Inequality_and_Hierarchy_in_Faculty_Hiring_Networ/review]] — 교수 채용의 위계 구조가 과학 경력에서 성별 불평등을 역사적으로 어떻게 심화시켜왔는지 확장 분석합니다.
- 🔗 후속 연구: [[papers/1028_Tenure_and_research_trajectories/review]] — 과학 경력에서 성별 불평등의 역사적 변화를 종신교수제가 연구 궤적에 미치는 영향으로 확장하여 분석했다.
- 🔗 후속 연구: [[papers/1048_Unequal_effects_of_the_COVID-19_pandemic_on_scientists/review]] — 팬데믹의 성별별 차별적 영향이 과학계 성별 불평등의 역사적 패턴을 더욱 심화시킬 수 있음을 보여준다.
- 🔄 다른 접근: [[papers/940_Bibliometrics_Global_Gender_Disparities_in_Science/review]] — 과학 경력에서 성별 불평등의 역사적 비교를 통해 성별 격차의 변화 양상을 분석한다
- 🏛 기반 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 성별 불평등의 역사적 추이 분석이 성별 다양성이 연구 성과에 미치는 긍정적 효과를 이해하는 배경을 제공한다.
- 🔄 다른 접근: [[papers/966_Global_citation_inequality_is_on_the_rise/review]] — 글로벌 인용 불평등과 성별 불평등은 모두 과학계 내 구조적 불평등 문제를 다른 차원에서 다룬다.
- 🔗 후속 연구: [[papers/976_Intersectional_inequalities_in_science/review]] — 과학 경력에서의 성별 불평등 연구를 인종과 성별의 교차적 관점으로 확장하여 더 포괄적인 분석을 제공한다.
- 🏛 기반 연구: [[papers/1146_BIBLIOMETRIC_ANALYSIS_ON_PARENTING_STYLES_AND_ADOLESCENTS_HA/review]] — 과학 경력에서의 성별 불평등 역사적 비교가 청소년 발달 연구에서의 젠더 관점을 이해하는 배경을 제공한다.
- 🏛 기반 연구: [[papers/1180_Global_research_trends_on_depression-related_stigma_in_the_2/review]] — 우울증 낙인화 연구에서 성별 차이를 이해하기 위해 과학 경력에서의 역사적 성별 불평등 비교 연구가 기반이 된다.
- 🔗 후속 연구: [[papers/1132_A_bibliometric_analysis_of_the_traditional_African_dental_pr/review]] — 과학 경력에서의 성별 불평등 역사적 비교가 전통 의료 관행 연구에서의 지역별 기여도 차이를 이해하는 틀을 확장한다.
- 🏛 기반 연구: [[papers/1155_Corporate_Governance_in_Accounting_A_Bibliometric_Analysis_o/review]] — 과학 경력에서 성별 불평등의 역사적 변화 분석이 회계 분야 거버넌스 연구에서 ESG 패러다임으로의 전환을 이해하는 사회적 배경을 제공한다.
