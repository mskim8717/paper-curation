---
title: "984_Mapping_Scholarly_Impact_Citation_Analysis_of_Commerce_Docto"
authors:
  - "SEEMA SAINI"
date: "2026.03"
doi: "10.5281/zenodo.19138724"
arxiv: ""
score: 3.0
essence: "Web of Science에서 2004년 1월부터 2025년 3월까지 graphene의 전자 특성에 관한 1,812개 문서에 대한 종합적인 인용 네트워크 분석을 수행하여 이 분야의 지식 구조와 발전 궤적을 체계적으로 매핑했다."
tags:
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Citation_Analysis_Methods"
  - "topic/scisci"
---

# Mapping Scholarly Impact: Citation Analysis of Commerce Doctoral Dissertations at Maharshi Dayanand University, Rohtak

> **저자**: SEEMA SAINI | **날짜**: 2026-03-20 | **DOI**: [10.5281/zenodo.19138724](https://doi.org/10.5281/zenodo.19138724)

---

## Essence


Web of Science에서 2004년 1월부터 2025년 3월까지 graphene의 전자 특성에 관한 1,812개 문서에 대한 종합적인 인용 네트워크 분석을 수행하여 이 분야의 지식 구조와 발전 궤적을 체계적으로 매핑했다.

## Motivation

- **Known**: Graphene은 2004년 분리된 이후 독특한 전자 특성(선형 에너지 분산, 무질량 Dirac 페르미온, 매우 높은 캐리어 이동도)으로 인해 응축 물질 물리학과 재료과학에서 광범위하게 연구되어 왔으며, 전자 소자, 센서, 투명 전극 등 다양한 응용 분야가 개발되고 있다.
- **Gap**: 빠르게 확대되는 graphene 전자 특성 관련 문헌의 규모와 복잡성으로 인해 지식 기반의 구조적 조직, 주제의 진화, 관계 역학을 체계적으로 이해하기 위한 정량적 분석이 필요하다.
- **Why**: Graphene 전자 특성 연구 분야의 지식 구조를 체계적으로 파악하면 연구자들이 분야의 성숙도와 새로운 기회를 이해하는 데 도움이 되며, 향후 연구 방향 설정의 기반이 된다.
- **Approach**: Web of Science Core Collection에서 검색한 데이터에 대해 Sankey plot을 활용한 시각화, direct citation analysis, bibliographic coupling, co-citation analysis 등 세 가지 상호보완적인 인용 분석 방법을 통합적으로 적용했다.

## Achievement


- **데이터 수집**: Boolean 검색 쿼리 '(Graphene OR Graphene oxide OR Graphite) AND (Electronic Properties)'를 사용하여 1,812개 문서와 6,106명의 저자 데이터 확보", '**지식 구조 시각화**: Sankey plot을 통해 저자, 인용 참고문헌, 키워드 간의 관계를 직관적으로 표시하여 거시적 수준의 개요 제공
- **chronological 진화 추적**: Direct citation analysis로 문헌의 시간적 인용 흐름을 추적하고 분야를 형성한 핵심 논문 및 발전 단계 식별
- **현대 연구 클러스터 탐지**: Bibliographic coupling을 통해 공통 참고문헌을 공유하는 문헌들을 연결하여 활발한 연구 클러스터와 주제 유사성 발견
- **지적 기초 규명**: Co-citation analysis로 두 문헌이 함께 인용되는 빈도를 분석하여 핵심 이론 저작과 개념적 상호연결 파악

## How


- Web of Science Core Collection에서 2004년 1월~2025년 3월 기간의 문헌 데이터 추출
- Boolean 연산자를 사용한 검색 쿼리로 graphene 전자 특성 관련 문헌 필터링
- bibliometrix R package 및 VOSviewer 소프트웨어를 활용한 인용 네트워크 구성
- Sankey plot 생성으로 저자, 인용 참고문헌, 키워드 간 관계 시각화
- Direct citation analysis로 시간적 지식 흐름 추적
- Network centrality 지표 및 clustering metrics 적용으로 영향력 있는 저자, 국가, 핵심 논문 식별
- Fractionalized 계산 방식을 사용한 정규화된 인용(normalized citations) 평가
- Python 스크립트를 이용한 VOSviewer 맵 파일에서 정규화된 인용값 추출
- Bibliographic coupling으로 현대 연구 클러스터 및 부상하는 주제 경계 탐지
- Co-citation analysis로 지적 기초와 개념적 상호연결 파악

## Originality

- Sankey plot, direct citation analysis, bibliographic coupling, co-citation analysis 등 네 가지 상호보완적 방법을 integrated된 방식으로 통합 적용한 다층적 접근법
- Python 기반 데이터 추출 스크립트를 작성하여 VOSviewer 맵 파일에서 정규화된 인용값을 자동으로 추출하는 혁신적인 방식
- Fractionalized/normalized counting methods를 통해 다중 저자 논문에서 개별 저자와 국가의 실제 기여도를 공정하게 평가
- Graphene 전자 특성이라는 특정 분야에 대해 포괄적인 인용 네트워크 분석을 통해 지식 구조의 조직화된 개요 제공

## Limitation & Further Study

- **데이터 제한**: Web of Science Core Collection만 사용하여 Scopus, PubMed 등 다른 주요 데이터베이스의 문헌이 누락될 가능성
- **시간 범위**: 2004년 이후 데이터만 포함하여 graphene 발견 이전의 관련 이론적 기초가 불완전하게 반영될 수 있음
- **완성도**: 논문이 results and discussion 섹션 초반에서 끝나 전체 분석 결과와 해석이 제시되지 않음
- **검색 쿼리 한계**: Boolean 검색이 모든 관련 문헌을 포괄하지 못할 가능성이 있으며, 특정 애플리케이션 영역(예: 센서, 트랜지스터)이 누락될 수 있음
- **후속 연구**: 시간에 따른 주제 진화의 동적 추적, 다양한 데이터베이스의 통합 분석, 머신러닝 기반의 자동 주제 추출, geographic patterns의 심층 분석 필요

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 3/5
- Overall: 3/5

**총평**: 이 연구는 graphene 전자 특성 분야의 지식 구조를 다층적 인용 분석과 시각화 기법으로 포괄적으로 매핑하였으나, 논문 완성도 미흡과 결과 분석 부재로 인해 완전한 평가가 제한적이다.

## Related Papers

- 🔄 다른 접근: [[papers/1195_Mapping_the_Research_Landscape_of_Electronic_Properties_of_G/review]] — 그래핀 전자 특성 연구의 인용 네트워크 분석과 그래핀 전자 특성 연구 지형도 매핑이 동일 주제에 대한 서로 다른 서지계량학적 접근을 보여줍니다.
- 🔗 후속 연구: [[papers/1056_Where_Do_Your_Citations_Come_From_Citation-Constellation_A_F/review]] — 상업 박사논문의 학술적 임팩트 매핑 연구에 인용 출처 추적을 위한 Citation-Constellation 방법론이 유용한 확장을 제공합니다.
- 🔄 다른 접근: [[papers/1155_Corporate_Governance_in_Accounting_A_Bibliometric_Analysis_o/review]] — 상업 박사 논문의 인용 분석과 회계 분야 기업지배구조 연구의 bibliometric 분석을 비교하여 서로 다른 학술 영역의 연구 동향 분석법을 대조할 수 있다.
