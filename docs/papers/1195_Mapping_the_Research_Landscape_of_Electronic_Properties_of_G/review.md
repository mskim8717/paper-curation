---
title: "1195_Mapping_the_Research_Landscape_of_Electronic_Properties_of_G"
authors:
  - "Richa Agrawal and Arnav Jain"
date: "2026"
doi: "10.48175/ijarsct-31487"
arxiv: ""
score: 4.0
essence: "본 논문은 2004년 1월부터 2025년 3월까지 Web of Science에서 수집한 1,812개의 문헌을 대상으로 graphene의 전자 특성에 관한 연구 동향을 bibliometric 분석 기법을 통해 체계적으로 분석한 연구이다."
tags:
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Domain-Specific_Analysis_Studies"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jain_2026_Mapping the Research Landscape of Electronic Properties of Graphene A Citation Network Analysis.pdf"
---

# Mapping the Research Landscape of Electronic Properties of Graphene: A Citation Network Analysis

> **저자**: Richa Agrawal and Arnav Jain | **날짜**: 2026 | **DOI**: [10.48175/ijarsct-31487](https://doi.org/10.48175/ijarsct-31487)

---

## Essence


본 논문은 2004년 1월부터 2025년 3월까지 Web of Science에서 수집한 1,812개의 문헌을 대상으로 graphene의 전자 특성에 관한 연구 동향을 bibliometric 분석 기법을 통해 체계적으로 분석한 연구이다.

## Motivation

- **Known**: Graphene은 2004년 분리된 이후 sp² 결합된 탄소 원자의 2D 육각형 격자 구조로 특이한 전자 대역 구조, 초고속 캐리어 이동도, 비정질 전기 장 효과 등 독특한 전자 특성을 보유하고 있다. Bibliometrics는 과학 문헌을 정량적으로 분석하여 연구 동향, 영향력 있는 저자·국가·출판물을 파악하는 확립된 방법론이다.
- **Gap**: Graphene 전자 특성에 관한 광범위하고 복잡한 문헌의 지적 구조와 발전 궤적을 이해하기 위해 체계적인 정량적 매핑이 필요하나, 기존 연구에서는 이러한 종합적인 citation network 분석이 부재하다.
- **Why**: Graphene 전자 특성 연구의 지식 아키텍처를 체계적으로 파악함으로써 연구자들이 이 빠르게 발전하는 분야의 성숙도와 신흥 기회를 이해할 수 있는 참조 프레임워크를 제공할 수 있다.
- **Approach**: 본 연구는 Sankey plot, direct citation analysis, bibliographic coupling, co-citation analysis의 네 가지 보완적 citation 방법론을 통합하여 graphene 전자 특성 연구의 지식 구조를 다층적으로 분석하고, bibliometrix R package와 VOSviewer 소프트웨어를 활용하여 citation network를 구성하고 시각화한다.

## Achievement


- **종합적 문헌 데이터베이스 구축**: Web of Science에서 1,812개 문헌과 6,106명의 저자 메타데이터를 수집하여 graphene 전자 특성 연구의 전체 지형도를 파악했다.
- **다층적 Citation 분석 통합**: Sankey plot을 통한 초기 구조 개요, direct citation analysis를 통한 시간적 지식 흐름 추적, bibliographic coupling을 통한 현대적 연구 클러스터 탐지, co-citation analysis를 통한 지적 기초 규명의 네 가지 방법론을 통합적으로 적용했다.
- **정규화된 계량지표 개발**: Fractionalized counting methods와 normalized citations을 Python 스크립트로 추출하여 저자·국가·저널의 실제 기여도를 정확히 평가했다.
- **연구 영향력 식별**: Network centrality indicators와 clustering metrics을 적용하여 영향력 있는 저자, 국가, 핵심 출판물과 seminal contributions을 체계적으로 규명했다.

## How


- Web of Science Core Collection에서 Boolean 검색 쿼리 '(Graphene OR Graphene oxide OR Graphite) AND (Electronic Properties)'를 사용하여 2004년 1월부터 2025년 3월까지의 문헌 수집", 'bibliometrix R package를 활용한 기본 bibliometric 지표(문서 수, citation 수, total linking strength) 계산
- VOSviewer 소프트웨어를 통한 citation network 구성 및 시각화
- Sankey plot을 생성하여 저자, 인용된 참고문헌, 키워드 간의 관계성 가시화
- Direct citation analysis를 수행하여 시간적 지식 흐름 추적 및 seminal contribution 식별
- Network centrality indicators와 clustering metrics 적용으로 영향력 있는 개체 식별
- Fractionalized counting methods를 적용하여 공동 저자 연구에서의 개별 기여도 정량화
- Python 스크립트를 통해 VOSviewer map file에서 normalized citations 추출
- Bibliographic coupling을 통한 현대적 연구 클러스터 및 신흥 주제 경계 탐지
- Co-citation analysis를 수행하여 학문적 기초 및 개념적 상호연결성 규명

## Originality

- Graphene 전자 특성 연구에 대한 최초의 종합적 citation network 분석으로, 기존 개별 측면 분석을 넘어 지적 구조를 전체론적으로 파악했다.
- Sankey plot을 citation 분석에 통합하여 저자-참고문헌-키워드 간의 비례적 흐름과 구조적 관계를 직관적으로 시각화하는 새로운 접근을 제시했다.
- Fractionalized bibliometric indicators와 normalized citations를 체계적으로 적용하여 다중 저자 연구 환경에서의 공정한 기여도 평가 방법론을 구현했다.
- Direct citation, bibliographic coupling, co-citation analysis의 세 가지 citation 방법론을 보완적으로 통합하여 다층적 지식 구조 분석을 수행했다.
- Python 기반 데이터 추출 스크립트를 개발하여 VOSviewer에서 normalized citations를 자동으로 추출하는 기술적 혁신을 달성했다.

## Limitation & Further Study

- 분석 기간이 2004-2025년으로 제한되어 graphene 발견 이전의 관련 2D 전자계 연구나 이론적 기초가 누락될 수 있다.
- Web of Science Core Collection만을 데이터 소스로 사용하여 다른 주요 데이터베이스(Scopus, PubMed 등)의 문헌이 포함되지 않았으며, 회색 문헌(학위논문, 보고서)이 제외되었다.
- 1,812개 문헌의 전체 full text 분석이 없이 메타데이터에만 기반하므로 연구의 실제 내용적 깊이나 질적 기여도 평가가 제한적이다.
- Citation count의 시간적 편향성(오래된 논문이 더 많은 인용을 받는 경향)이 고려되지 않아, normalized citations만으로는 시간 대 영향력의 부분적 비교만 가능하다.
- 후속 연구로는 다중 데이터베이스 통합, full text 기반 content analysis, 시간 가중치 적용 메트릭 개발, graphene 기술의 특정 응용 분야(소자, 센서, 에너지) 별 세분화 분석이 권장된다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 graphene 전자 특성 연구의 지식 구조를 다층적 citation 분석과 시각화 기법으로 종합적으로 파악한 의미 있는 bibliometric 연구이다. Sankey plot의 창의적 활용과 정규화된 지표의 체계적 적용이 돋보이나, 단일 데이터베이스 의존성과 메타데이터 기반 분석의 한계가 있다.

## Related Papers

- 🧪 응용 사례: [[papers/1075_Open_Catalyst_2020_OC20_Dataset_and_Community_Challenges/review]] — 그래핀 전자 특성 연구의 bibliometric 분석이 촉매 연구 데이터셋과 커뮤니티 챌린지에서 실제 적용될 수 있다.
- 🏛 기반 연구: [[papers/972_Identifying_interdisciplinary_emergence_in_the_science_of_sc/review]] — 그래핀 연구의 학제간 특성을 이해하기 위해 과학의 학제간 emergence 식별 방법론이 기반이 된다.
- 🔄 다른 접근: [[papers/984_Mapping_Scholarly_Impact_Citation_Analysis_of_Commerce_Docto/review]] — 그래핀 전자 특성 연구의 인용 네트워크 분석과 그래핀 전자 특성 연구 지형도 매핑이 동일 주제에 대한 서로 다른 서지계량학적 접근을 보여줍니다.
