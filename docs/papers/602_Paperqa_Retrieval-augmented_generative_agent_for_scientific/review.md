---
title: "602_Paperqa_Retrieval-augmented_generative_agent_for_scientific"
authors:
  - "Jakub Lála"
  - "Odhran O'Donoghue"
  - "Aleksandar Shtedritski"
  - "Sam Cox"
  - "Samuel G. Rodriques"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.25
essence: ""
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Scholarly_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lála et al._2023_Paperqa Retrieval-augmented generative agent for scientific research.pdf"
---

# PaperQA: Retrieval-Augmented Generative Agent for Scientific Research

> **저자**: Jakub Lála, Odhran O'Donoghue, Aleksandar Shtedritski, Sam Cox, Samuel G. Rodriques, Andrew Dickson White | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1: PaperQA Workflow Diagram](figures/fig1.webp)

*PaperQA는 과학 논문 검색 및 합성을 통해 과학적 질문에 답변하는 에이전트 기반 검색 증강 생성(RAG) 시스템이다.* 대규모언어모델(LLM)의 환각(hallucination) 문제를 해결하기 위해 모듈화된 RAG 컴포넌트를 활용하여 전문가 수준의 성능을 달성한다.

## Motivation

- **Known**: 
  - LLM은 언어 작업에서 우수한 일반화 능력을 보유
  - RAG 모델은 환각 감소 및 답변 추적성(provenance) 제공으로 제안됨
  - 연간 500만 이상의 논문이 발행되며 과학 발견 과정은 여전히 수동적

- **Gap**: 
  - 표준 RAG 모델은 고정된 선형 흐름을 따르므로 다양한 과학 질문에 대응 제한
  - 기존 과학 QA 벤치마크(PubMedQA 등)는 초록 기반으로만 구성되어 전문 정보 검색 능력 미흡
  - 사전학습 데이터 이후 발표된 최신 정보 활용 불가능

- **Why**: 
  - 과학에서 부정확한 정보는 정보 없음보다 더 해로울 수 있음
  - 과학자들은 광범위한 문헌을 신뢰성 있게 처리할 시스템 필요

- **Approach**: 
  - RAG를 모듈화하여 에이전트가 질문 특성에 따라 동적으로 검색 및 증거 수집 조정
  - 맵-리듀스(map-reduce) 요약 단계 적용으로 다중 소스 처리 확대
  - LLM 기반 관련성 점수 부여로 벡터 임베딩 기반 검색 보완
  - 사전/사후 프롬프팅(a priori/a posteriori prompting)으로 내재 지식 활용

## Achievement

![Figure 2: Retrieval Probability (Abstract)](figures/fig2.webp)
![Figure 3: Retrieval Probability (Full-Text)](figures/fig3.webp)

1. **벤치마크 성능 우위**: 
   - PubMedQA(초록 기반, 폐쇄형)에서 GPT-4 대비 28.4% 성능 향상 (57.9% → 86.3%)
   - 제안한 LitQA 데이터셋(전문 논문 기반 복합 질문)에서 모든 테스트된 모델 및 상용 도구 능가

2. **인간 전문가 수준 달성**: 
   - LitQA에서 인간 전문가와 동등한 성능 및 소요 시간 달성
   - 상업적 비용 대비 훨씬 저렴한 운영 비용

3. **개선된 지식 경계(knowledge boundary)**: 
   - 경쟁 도구 대비 더 낮은 오류율로 부정확한 답변 제시
   - "불확실함" 응답 비율 증가로 신뢰성 강화

4. **최신 정보 처리**: 
   - 사전학습 데이터 이후 발표된 논문 정보 활용 가능

## How

- **검색 도구(search)**: ArXiv, PubMed 등 온라인 데이터베이스에서 키워드 기반 논문 검색, 선택적 연도 범위 설정
  
- **증거 수집 도구(gather evidence)**:
  - 검색된 논문을 4,000자 단위 중복 청크(chunk)로 분할
  - text-embedding-ada-002 모델로 임베딩 후 벡터 데이터베이스 저장
  - 최대 한계 관련성(maximal marginal relevance, MMR) 검색으로 다양성 확보
  - 각 청크에 대해 요약 LLM이 1-10 점수로 관련성 평가

- **답변 생성 도구(answer question)**:
  - 사전 단계: ask LLM이 사전학습된 지식에서 유용한 정보 추출
  - 맵 단계: 수집된 증거들을 정렬 및 컨텍스트 라이브러리 구성
  - 리듀스 단계: answer LLM이 최종 답변 생성 및 인용 출처 제공

- **에이전트 루프**: 
  - 초기 질문으로 검색 수행 후, 증거 부족 시 LLM이 다양한 키워드로 반복 검색 결정
  - 5개 이상의 다중 소스 증거 또는 충분한 시도 후 답변 생성
  - 불완전한 답변은 거절하고 재시도 가능

## Originality

- **에이전트 기반 RAG 분해**: 표준 고정형 RAG 파이프라인을 모듈화하여 각 단계를 도구화, 에이전트가 동적으로 제어 가능하게 개선

- **LLM 기반 관련성 점수 부여**: 벡터 거리 이외에 LLM이 의미론적 관련성을 1-10 척도로 평가하여 검색 정확도 강화

- **맵-리듀스 증거 수집**: 다중 소스 처리 확대 및 중간 추론 단계(scratchpad) 제공으로 복잡한 질문 처리 능력 향상

- **LitQA 벤치마크 도입**: 전문 논문 전문(full-text) 기반으로 정보 합성이 필요한 복잡한 QA 데이터셋 신규 제시

- **사전/사후 프롬프팅 통합**: LLM의 내재 지식과 검색 기반 정보를 결합하는 프롬프팅 전략 체계화

## Limitation & Further Study

- **검색 엔진 의존성**: ArXiv, PubMed 등 외부 검색 API의 실패율(PDF 파싱 오류 등)에 영향받으며, 이는 부록 C에서만 다룸

- **청크 크기 고정**: 4,000자 고정 청크로 설정하여 최적 크기 탐색 미흡

- **계산 비용**: 맵-리듀스 단계에서 다중 LLM 호출로 인한 계산 비용 증가 (동시 처리로 완화하나 여전히 부담)

- **평가 데이터셋 규모**: LitQA가 "최근 문헌"에서 구성되었으나 정확한 규모 및 분야 다양성 제시 부족

- **후속 연구**:
  - 더 큰 규모의 LitQA 확장 및 다양한 과학 분야 포괄
  - 청크 크기, 검색 알고리즘, LLM 모델 조합 최적화 연구
  - 다국어 과학 논문 지원 확대
  - 실시간 과학 발견 시나리오에서 사용성 검증

## Evaluation

- **Novelty**: 4/5
  - 에이전트 기반 RAG 분해 및 LLM 기반 관련성 평가는 참신하나, 개별 컴포넌트(벡터 검색, 맵-리듀스)는 기존 기법의 조합

- **Technical Soundness**: 4/5
  - 시스템 설계는 논리적이고 구현 세부사항 충분하나, 검색 실패율 및 청크 최적화 분석 부족

- **Significance**: 5/5
  - 과학 커뮤니티의 실질적 필요를 해결하며, 인간 전문가 수준 성능 달성은 높은 임팩트

- **Clarity**: 4/5
  - 전체 워크플로우는 명확하나, 일부 프롬프트 상세사항과 에러 처리 절차가 부록에만 기술됨

- **Overall**: 4.25/5

**총평**: PaperQA는 모듈화된 에이전트 기반 RAG를 통해 과학 문헌 기반 질답에서 인간 전문가 수준의 성능을 달성한 실질적 기여로, LitQA라는 새로운 벤치마크 도입으로 분야 발전에 촉매 역할을 할 것으로 기대된다. 다만 외부 API 의존성과 계산 비용 최적화 측면에서의 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 검색 증강 생성과 과학문헌 합성은 과학 연구에서 서로 다른 정보 활용 접근법을 제시한다
- 🏛 기반 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — 검색 증강 언어모델 사전훈련이 과학 연구용 RAG 에이전트의 기초 방법론을 제공한다
- 🔗 후속 연구: [[papers/874_WebWatcher_Breaking_New_Frontier_of_Vision-Language_Deep_Res/review]] — PaperQA의 과학 문헌 검색 기능이 WebWatcher의 멀티모달 정보 추구 능력과 결합될 수 있다.
- 🔄 다른 접근: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — PaperQA의 검색 증강 생성과 유사하지만 단일 질의가 아닌 포괄적 기사 작성을 위한 다관점 연구 접근법을 제시한다.
- 🏛 기반 연구: [[papers/457_Language_agents_achieve_superhuman_synthesis_of_scientific_k/review]] — PaperQA의 초기 버전으로, PaperQA2의 환각 문제 해결과 성능 향상의 기술적 기반을 제공한다
- 🧪 응용 사례: [[papers/021_A_Review_on_Scientific_Knowledge_Extraction_using_Large_Lang/review]] — 과학적 지식 추출 이론을 실제 논문 검색 및 요약 에이전트로 구현한 실용적 사례를 제시한다.
