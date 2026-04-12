---
title: "1120_SciEvo_A_2_Million_30-Year_Cross-disciplinary_Dataset_for_Te"
authors:
  - "Yiqiao Jin"
  - "Yijia Xiao"
  - "Yiyang Wang"
  - "Jindong Wang"
date: "2024"
doi: "10.48550/ARXIV.2410.09510"
arxiv: ""
score: 4.0
essence: "arXiv의 210만 개 논문으로 구성된 30년 종단 scientometric 데이터셋(Scito2M)을 제시하고, 학문 용어 진화, 인용 패턴, 학제 간 지식 교류를 분석하여 기초 vs 응용 연구의 인식론적 차이를 규명한다."
tags:
  - "cat/Academic_Impact_and_Mobility"
  - "sub/Statistical_Robustness_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2024_SciEvo A 2 Million, 30-Year Cross-disciplinary Dataset for Temporal Scientometric Analysis.pdf"
---

# SciEvo: A 2 Million, 30-Year Cross-disciplinary Dataset for Temporal Scientometric Analysis

> **저자**: Yiqiao Jin, Yijia Xiao, Yiyang Wang, Jindong Wang | **날짜**: 2024 | **DOI**: [10.48550/ARXIV.2410.09510](https://doi.org/10.48550/ARXIV.2410.09510)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Keyword trajectories reflect critical paradigm shifts in AI and epidemiology research over*

arXiv의 210만 개 논문으로 구성된 30년 종단 scientometric 데이터셋(Scito2M)을 제시하고, 학문 용어 진화, 인용 패턴, 학제 간 지식 교류를 분석하여 기초 vs 응용 연구의 인식론적 차이를 규명한다.

## Motivation

- **Known**: Scientometrics는 학술 문헌의 정량적·정성적 분석을 통해 과학 지식의 구조와 동역학을 이해하는 분야이며, 현존하는 데이터셋은 장기간의 포괄적 콘텐츠 및 인용 정보를 제공하지 못하고 있다.
- **Gap**: 대규모 종단(longitudinal) scientometric 데이터셋의 부재와 제한된 분석 범위(특정 분야·기간·출판지만 포함)로 인해 과학 지식 교류의 폭(topical diversity)과 깊이(long-term impact)를 종합적으로 이해하기 어렵다.
- **Why**: 팬데믹, 기후변화, 윤리적 AI 등 복잡한 글로벌 과제를 해결하기 위해 학제 간 과학 지식 창출·진화·확산의 메커니즘을 이해하는 것이 필수적이다.
- **Approach**: arXiv의 전체 논문과 Semantic Scholar API를 통한 인용 그래프를 통합하여 메타데이터, 전문(full-text), 키워드를 포함한 포괄적 데이터셋을 구축하고, 용어 진화(diachronic analysis), 인용 네트워크, 학제 간 지식 흐름을 30년 간 분석한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Evolution in the ranks of math and machine-learning terms among all keywords over time.*

- **Scito2M 데이터셋**: 1991-2024년 210만 개 논문, 156개 arXiv 카테고리, 포괄적 메타데이터(제목, 초록, 전문, 키워드, 인용 그래프) 및 분석 도구 제공
- **Paradigm Shift 발견**: 기계학습 관련 용어가 2010년 이전 상위 20 키워드의 0.31개에서 2015년 이후 9.5개로 급증하여 이론 중심 → 응용 중심 연구로의 전환 증명
- **Disciplinary Homophily**: 인용의 91% 이상이 학제 내부(intra-disciplinary)에서 발생하여 학제 간 지식 교류의 한계 규명
- **Epistemic Culture 차이**: LLM(2.48년) vs Oral History(9.71년) 등 응용 vs 기초 연구의 인용 나이(Citation Age of Citation) 격차로 지식 검증·축적 방식의 학제별 차이 규명
- **Citation Amnesia**: 응용 연구가 기초 연구 대비 최근 저작에 편향되어 역사적 기여를 간과하는 현상 발견

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Citation diversity in terms of Simpson’s Diversity Index, Shannon Diversity Index, and Gini*

- **데이터 수집**: arXiv API를 통해 1991-2024년 전체 논문 수집, Semantic Scholar API를 활용하여 인용 관계, 발행처, 저자 정보 추출
- **키워드 추출**: GPT-4o를 이용하여 제목과 초록에서 의미 있는 키워드 추출, 연평균 14.62개 추상 키워드 확보
- **용어 진화 분석**: 시간별 스냅샷으로 논문 분할 후 키워드 빈도 순위 추이 분석(macro-level), Graph Convolutional Network(GCN)을 통한 키워드 동시출현 패턴의 고차 관계 학습(micro-level)
- **인용 네트워크 분석**: 학제 내/간 인용 비율, Simpson/Shannon 다양성 지수를 계산하여 인용 다양성 및 homophily 정량화
- **통계 검증**: 평균, 표준편차, 중앙값(median citation age) 등을 통한 학제별 인용 패턴 비교

## Originality

- **규모와 포괄성**: 단순한 메타데이터를 넘어 전문, 인용 그래프, GPT 기반 키워드 추출을 모두 포함한 가장 큰 규모의 종단 scientometric 데이터셋
- **시공간적 심화 분석**: macro(연도별 키워드 순위)와 micro(GCN 기반 용어 동시출현) 수준에서의 이중 분석으로 패러다임 시프트의 단계적 메커니즘 규명
- **Epistemic Culture 개념의 정량화**: 인용 나이, 인용 다양성 지수, 학제 내/간 인용 비율 등 다층적 지표를 통해 抽象的 인식론적 차이를 구체적으로 증명
- **공개 데이터셋 및 도구**: GitHub, Kaggle, HuggingFace를 통한 재현성 높은 자료 공개로 후속 연구 활성화

## Limitation & Further Study

- **arXiv 한정성**: arXiv는 특정 분야(물리, 수학, CS 등)에 편향되어 있어 생의학, 사회과학 등 다른 주요 분야의 대표성 부족
- **인용 데이터의 불완전성**: Semantic Scholar API의 인용 정보 누락 또는 지연으로 인한 분석 오차 가능성
- **키워드 추출의 자동화 한계**: GPT-4o 기반 키워드 추출이 수작업 검증 없이 진행되어 도메인 특화 용어의 오분류 위험
- **시간적 해석의 주의**: 논문 출판 증가 추세가 실제 연구 패러다임 시프트와 혼동될 가능성 (normalizing 필요)
- **후속 연구**: (1) 다른 출판 플랫폼(PubMed, bioRxiv) 통합, (2) 자동화된 citation intent 분석(인용이 긍정/부정/중립인지 구분), (3) 저자 네트워크 기반 신흥 연구자 영향력 분석, (4) 국가별·기관별 지식 흐름의 지정학적 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Scito2M은 규모, 포괄성, 분석 깊이에서 scientometrics 분야의 주요 기여 자료이며, 학제별 인식론적 문화 차이를 정량적으로 규명한 새로운 통찰을 제공한다. 다만 데이터 편향성과 인용 정보의 완전성 개선이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/1015_S2ORC_The_Semantic_Scholar_Open_Research_Corpus/review]] — S2ORC 데이터셋은 SciEvo와 같은 대규모 종단 과학계량 데이터셋 구축의 방법론적 선례를 제공한다.
- 🧪 응용 사례: [[papers/972_Identifying_interdisciplinary_emergence_in_the_science_of_sc/review]] — 과학학의 학제간 출현 특성은 SciEvo 데이터셋으로 분석할 수 있는 지식 교류 패턴의 구체적 사례이다.
- 🔗 후속 연구: [[papers/1124_The_Science_of_Science/review]] — 과학학 이론은 SciEvo 데이터셋이 다루는 과학 진화 현상의 개념적 틀을 제공한다.
- 🏛 기반 연구: [[papers/1215_Total_Fertility_Rate_Studies_Bibliometric_Analysis_with_R_Pr/review]] — 출산율 연구의 진화 분석을 위해 30년간의 학제간 데이터셋이 제공하는 장기적 관점을 활용할 수 있음
