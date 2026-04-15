---
title: "087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi"
authors:
  - "Amanpreet Singh"
  - "Joseph Chee Chang"
  - "Dany Haddad"
  - "Aakanksha Naik"
  - "Jena D. Hwang"
date: "2025"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "Ai2 Scholar QA는 과학 문헌에서 검색-증강 생성(RAG)을 활용하여 장문의 과학 질문에 답하는 무료 공개 시스템이다. 전체 파이프라인을 오픈소스로 공개하며 인용 기반의 조직화된 답변 보고서를 생성한다."
tags:
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Research_Literature_Analysis_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singh et al._2025_Ai2 scholar qa Organized literature synthesis with attribution.pdf"
---

# Ai2 Scholar QA: Organized literature synthesis with attribution

> **저자**: Amanpreet Singh, Joseph Chee Chang, Dany Haddad, Aakanksha Naik, Jena D. Hwang, Rodney Kinney, Daniel S. Weld, Doug Downey, Sergey Feldman | **날짜**: 2025 | **DOI**: [미제공]

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: Scholar QA 파이프라인 개요 - 검색(Retrieval), 재순위매김(Reranker), 다단계 생성(Multi-Step Generation)으로 구성*

Ai2 Scholar QA는 과학 문헌에서 검색-증강 생성(RAG)을 활용하여 장문의 과학 질문에 답하는 무료 공개 시스템이다. 전체 파이프라인을 오픈소스로 공개하며 인용 기반의 조직화된 답변 보고서를 생성한다.

## Motivation

- **Known**: OpenScholar, Elicit, Consensus 등 기존 과학 QA 시스템들이 존재하지만, 대부분 유료이며 폐쇄 소스로 재현 및 개선이 어려움
- **Gap**: 연구자들이 과학 문헌 통합 시스템을 연구하고 구축할 수 있는 공개적이고 확장 가능한 인프라의 부재
- **Why**: 투명성 있는 오픈소스 과학 QA 시스템을 통해 연구 커뮤니티의 진입 장벽을 낮추고 재현성을 확보할 필요성
- **Approach**: 다단계 파이프라인(검색→재순위매김→생성)과 인용 기반 답변 생성을 구현하고, 코드, API, 데이터셋을 모두 공개함

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 확장 가능한 섹션(B)으로 구성된 다중 섹션 보고서와 인용 근거 링크(C)*

1. **ScholarQA-CS 벤치마크 최고 성능**: 기존 경쟁 시스템을 능가하는 성능 달성
2. **11.7M 전문 논문 인덱스**: 기존 1억 개 초록 인덱스(Semantic Scholar)와 함께 새로운 전문(full-text) 검색 엔드포인트 제공
3. **포괄적인 공개 자원**: Python 패키지, 웹 앱, 공개 API, 다운로드 가능 데이터셋을 통합 제공
4. **사용자 만족도 85%**: 긍정적인 피드백 비율이 높음

## How

![Figure 3](figures/fig3.webp)
*그림 3: 인라인 테이블로 논문 비교(A) 및 공통 측면 표시(B), 근거 발췌 링크(C)*

**3단계 파이프라인 구조**:

- **검색 단계** (§2.1)
  - 쿼리 분해기(Query Decomposer)로 사용자 쿼리를 각 엔드포인트에 맞게 재구성
  - Semantic Scholar 키워드 검색(100M 초록) 및 새로운 스니펫 검색 엔드포인트(11.7M 전문) 병렬 사용
  - mxbai-embed-large-v1 임베딩으로 밀집 인덱싱, BM25 희소 인덱싱 결합

- **재순위매김 단계** (§2.2)
  - mxbai-rerank-large-v1 크로스-인코더로 상위 50개 passage 선정
  - NVIDIA L40S GPU에서 Modal로 호스팅

- **생성 단계** (§2.3)
  - **인용 추출**: 각 논문의 passage와 초록을 함께 처리하여 관련 인용문 추출
  - **답변 아웃라인 및 클러스터링**: LLM이 주제별 섹션 생성 및 형식(단락/불릿) 결정
  - **보고서 생성**: 각 섹션을 순차적으로 합성, 인용 기반 근거 제공
  - **비교 테이블**: 관련 논문들의 공통 측면(데이터셋 크기, 주석 방식 등) 자동 비교

**사용자 경험**:
  - 실시간 진행 상황 표시로 평균 2.5분 소요 시간 가시화
  - 섹션 스트리밍으로 첫 섹션 50초 내 확인 가능
  - 섹션 축소/확장 인터페이스로 정보 접근 최적화
  - 인라인 인용 클릭으로 원문 발췌 및 논문 검증 가능

## Originality

- **포괄적 오픈소스 공개**: 기존 폐쇄 과학 QA 시스템과 달리, 파이프라인 코드, 웹 앱, API, 데이터셋을 모두 공개하여 재현성 확보
- **주제별 아웃라인 프레임워크**: 단순 순차 합성이 아닌 논리적 주제 구조화로 답변 조직화 향상
- **다중 검색 전략 결합**: 키워드 검색(초록)과 의미론적 검색(전문) 병렬 처리로 재현율과 정밀도 모두 확보
- **인용 근거 추출 및 검증**: 모든 주장에 대해 원문 발췌 제공으로 투명성과 신뢰성 강화
- **비교 테이블 자동 생성**: 구조화된 논문 비교로 관련 작업(related work) 이해 용이
- **LLM 메모리 명시**: 생성된 내용과 근거 기반 내용 구분으로 환각(hallucination) 추적 가능

## Limitation & Further Study

- **모델 의존성**: 클로드 3.7과 같은 폐쇄 LLM 사용으로 완전한 오픈소스 구현 미달성
- **응답 지연**: 평균 2.5분 소요로 실시간성 요구 서비스에 부적합
- **전문 인덱스 제한**: 11.7M 논문으로 의학, 생물학 등 특정 분야에 치우칠 수 있는 커버리지 불균형
- **평가 제한**: ScholarQA-CS 벤치마크에만 평가, 다양한 과학 분야 및 질문 유형에 대한 포괄적 평가 필요
- **사용자 피드백 분석 부재**: 85% 긍정 평가는 제시하지만, 부정 15%에 대한 구체적 문제점 분석 미흡

**향후 연구**:
  - 오픈 LLM 통합으로 완전 오픈소스 구현
  - 다단계 생성 병렬화 등으로 응답 속도 개선
  - 비영어권 과학 문헌 인덱싱 확대
  - 도메인별 평가 벤치마크 개발 및 다중 평가 지표 적용
  - 부정적 피드백에 대한 근인 분석 및 개선안 도출

## Evaluation

- **Novelty**: 4/5
  - 오픈소스 공개와 통합 파이프라인은 창신적이나, 개별 기술(RAG, 크로스-인코더 등)은 기존 기법의 조합

- **Technical Soundness**: 4/5
  - 다단계 설계와 인용 추출 로직이 타당하고 구현 세부사항이 명확함
  - 단, LLM 평가 라벨링의 80% 일치도가 평가 신뢰성을 제한

- **Significance**: 4/5
  - 과학 연구 커뮤니티에 실제 가치 있는 무료 도구 제공
  - 85% 사용자 만족도와 벤치마크 성능이 실용적 영향력 입증
  - 다만 학술 공헌보다 엔지니어링/도구 기여에 더 가까움

- **Clarity**: 5/5
  - 파이프라인 개요(Figure 1)부터 상세 구현까지 명확히 설명
  - 사용자 인터페이스와 아키텍처 모두 이해하기 쉬움

- **Overall**: 4/5

**총평**: Ai2 Scholar QA는 기존의 폐쇄 과학 QA 시스템에 대한 효과적인 오픈소스 대안을 제시하며, 투명한 인용 기반 답변 생성과 포괄적인 공개 자원을 통해 과학 정보 검색의 민주화를 실현한 실질적으로 가치 있는 시스템이다.

## Related Papers

- 🔄 다른 접근: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 과학 문헌 질의응답과 문서 요약 모두 RAG 기반 접근법을 사용하지만 서로 다른 출력 형태를 제공한다.
- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — OpenScholar의 과학 문헌 합성 기능을 질의응답 형태로 확장하여 더 직관적인 사용자 인터페이스를 제공한다.
- 🏛 기반 연구: [[papers/235_Comparing_knowledge_sources_for_open-domain_scientific_claim/review]] — 과학적 주장 검증을 위한 지식 소스 비교 연구가 문헌 기반 질의응답 시스템의 신뢰성 확보에 중요한 기반을 제공한다.
- 🔄 다른 접근: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — AI2 Scholar QA와 유사하게 학술 문헌 종합을 다루지만 더 대규모 오픈 액세스 데이터로 접근한다.
- 🔗 후속 연구: [[papers/457_Language_agents_achieve_superhuman_synthesis_of_scientific_k/review]] — AI2 Scholar QA는 문헌 기반 질의응답에서 속성 부여 기능을 추가하여, PaperQA2의 신뢰성 있는 과학 지식 합성 능력을 확장한다
- 🔄 다른 접근: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 과학 문헌 요약과 질의응답 모두 RAG 기반이지만 서로 다른 정보 제시 방식을 통해 사용자의 다양한 요구를 충족한다.
- 🔗 후속 연구: [[papers/215_Chime_Llm-assisted_hierarchical_organization_of_scientific_s/review]] — 계층적 문헌 조직화를 질의응답 시스템에 통합하여 더 체계적이고 맥락화된 문헌 검색 및 답변 생성을 가능하게 한다.
- 🏛 기반 연구: [[papers/235_Comparing_knowledge_sources_for_open-domain_scientific_claim/review]] — 과학적 주장 검증을 위한 지식 소스 비교 연구가 문헌 기반 질의응답 시스템의 신뢰성과 정확성 확보에 중요한 기반을 제공한다.
- 🔗 후속 연구: [[papers/913_Semantic_Scholar/review]] — 대규모 학술 코퍼스를 구조화된 문헌 합성과 인용 분석이라는 구체적 응용으로 확장한다
