---
title: "593_Openscholar_Synthesizing_scientific_literature_with_retrieva"
authors:
  - "Akari Asai"
  - "Jacqueline He"
  - "Rulin Shao"
  - "Weijia Shi"
  - "Amanpreet Singh"
date: "2024"
doi: "---"
arxiv: ""
score: 4.4
essence: "본 논문은 4,500만 개의 오픈 액세스 과학 논문에서 관련 구절을 검색하고 인용 기반 응답을 합성하는 검색 증강 대규모 언어모델(RAG-LM) 기반 시스템 OpenScholar를 제안하며, 함께 과학 논문 합성 평가를 위한 대규모 벤치마크 ScholarQA-Bench를 소개한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Scholarly_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Asai et al._2024_Openscholar Synthesizing scientific literature with retrieval-augmented lms.pdf"
---

# Openscholar: Synthesizing scientific literature with retrieval-augmented lms

> **저자**: Akari Asai, Jacqueline He, Rulin Shao, Weijia Shi, Amanpreet Singh, Joseph Chee Chang, Kyle Lo, Luca Soldaini, Sergey Feldman, Mike D'Arcy, David Wadden, Matt Latzke, Mingliang Tian, Peng Ji, Shengyan Liu, Tong Hao, Borong Wu, Yi Xiong, Luke Zettlemoyer, Graham Neubig | **날짜**: 2024 | **DOI**: 

---

## Essence

![Figure 1](figures/fig1.webp)

*OpenScholar의 전체 개요: 전문화된 데이터스토어, 검색기 및 언어모델로 구성되며, 검색 기반 자체 피드백 추론 루프를 통해 반복적으로 응답을 개선한다.*

본 논문은 4,500만 개의 오픈 액세스 과학 논문에서 관련 구절을 검색하고 인용 기반 응답을 합성하는 검색 증강 대규모 언어모델(RAG-LM) 기반 시스템 OpenScholar를 제안하며, 함께 과학 논문 합성 평가를 위한 대규모 벤치마크 ScholarQA-Bench를 소개한다.

## Motivation

- **Known**: 대규모 언어모델(LLM)은 과학 문헌 합성에 도움을 줄 수 있지만, 환각(hallucination), 구식 학습 데이터, 투명한 인용 부족 등의 심각한 한계를 가지고 있다. 특히 GPT-4는 최신 문헌 인용 시 78-90%의 사례에서 가짜 인용을 생성한다.

- **Gap**: 기존 문헌 검색 시스템은 독점 API나 일반용 LLM에 의존하거나, 평가가 단일 분야의 소규모 인간 평가에 제한되어 있으며, 현실적인 다중 논문 합성 작업을 평가하기 어렵다.

- **Why**: 과학 연구자들의 급증하는 문헌을 효과적으로 종합하려면, 정확한 검색, 신뢰할 수 있는 인용 속성, 실시간 현재 문헌 접근이 필수적이다.

- **Approach**: 과학 문헌 전문화 데이터스토어(45M 논문), 학습된 검색기와 재순위 지정기, 자체 피드백 반복 개선 루프를 포함한 통합 RAG 시스템을 구축하고, 전문가가 작성한 질의-응답 쌍(2,967개)으로 구성된 ScholarQA-Bench 벤치마크를 개발한다.

## Achievement

![Figure 2](figures/fig2.webp)

*OpenScholar의 상세한 추론(상) 및 학습(하) 파이프라인. 추론 시에는 검색기를 통해 관련 논문을 식별하고 재순위 지정기로 상위 N개를 정제한 후, LM이 초기 응답과 자체 피드백을 생성하여 반복적으로 개선한다.*

1. **성능 우수성**: OpenScholar-8B가 GPT-4o보다 정확도에서 5%, PaperQA2보다 7% 우수한 성능을 보이며, GPT-4o의 인용 환각률(78-90%)을 인간 전문가 수준으로 개선(인용 정확도 대폭 향상)

2. **인간 평가 선호도**: OpenScholar-8B는 전문가 작성 응답 대비 51% 승률, OpenScholar-GPT4o는 70% 승률을 달성하여 GPT-4o의 32%를 크게 상회

3. **범용성**: OpenScholar 파이프라인이 GPT-4o 개선(정확도 12% 향상), 오픈소스 모델 학습(OpenScholar-8B), 검색기 학습 등 다양한 용도로 활용 가능

4. **자원 공개**: 코드, 학습된 모델 체크포인트, 45M 논문 데이터스토어(237M 임베딩), ScholarQA-Bench 데이터셋, 공개 데모 전부 공개

## How

![Figure 2](figures/fig2.webp)

*OpenScholar의 상세 구조: (1)검색 단계: 질의로부터 데이터스토어의 관련 구절 검색, (2)재순위: 신경망 재순위 지정기로 상위 N개 정제, (3)생성: LM이 초기 응답 생성, (4)피드백: LM이 자신의 출력에 대해 자연언어 피드백 생성, (5)반복 개선: 피드백을 반영하여 응답 업데이트를 여러 번 수행*

- **OpenScholar-DataStore (OSDS)**: Semantic Scholar에서 수집한 45M 개의 오픈 액세스 논문과 237M 개의 대응 구절 임베딩으로 구성된 전문화된 데이터스토어

- **검색 및 재순위 지정**: 기본 검색기로 후보 문서 식별 후, 학습된 신경망 재순위 지정기가 상위 N개 구절 선별하여 검색 품질 향상

- **자체 피드백 반복 개선 (Self-Feedback Inference Loop)**: 
  - (1) 초기 응답 y₀ 생성
  - (2) 응답에 대한 자연언어 피드백 f₁ 생성 (예: "더 많은 실증적 발견 추가")
  - (3) 피드백을 반영하여 개선된 응답 y₁ 생성
  - 이 과정을 미리 정의된 횟수만큼 반복

- **인용 검증**: 생성된 인용이 실제 논문과 구절에 대응되는지 자동 검증

- **학습 데이터 생성**: 데이터스토어의 샘플링된 논문에서 합성 질의 및 지시사항 생성 → OpenScholar 추론 파이프라인 실행 → 중간 및 최종 출력을 활용하여 OpenScholar-8B 학습

- **ScholarQA-Bench**: 컴퓨터과학, 물리학, 신경과학, 생의학 4개 분야의 2,967개 전문가 작성 질의와 208개 장문형 응답(평균 작성 시간 1시간, Ph.D./박후 작성자)

- **다면적 평가**: 인용 정확도, 사실 정확성, 내용 커버리지, 응집성, 전체 품질을 자동 지표와 인간 평가로 측정

## Originality

- **최대 규모 공개 과학 데이터스토어**: 4,500만 개 논문의 전문화된 검색 가능 데이터스토어는 기존 공개 자원 중 최대 규모

- **다중 분야 전문가 기준 벤치마크**: 4개 과학 분야의 2,967개 질의와 전문가(Ph.D./박후) 작성 장문형 응답으로 구성된 ScholarQA-Bench는 현실적인 다중 논문 합성 작업의 평가 기준 제시

- **자체 피드백 반복 개선 루프의 실용화**: LM의 자체 피드백을 활용한 반복 개선이 추론 시간과 학습 모두에서 일관된 성능 향상을 도출

- **확장 가능한 RAG 프레임워크**: 개발된 파이프라인이 다양한 기반 모델(오픈소스 8B, GPT-4o 등)과 호환되며 성능 향상을 보임

- **포괄적 공개**: 모든 코드, 모델 체크포인트, 데이터스토어, 벤치마크, 공개 데모를 함께 제공하여 재현성과 확장성 극대화

## Limitation & Further Study

- **검색 품질 의존성**: 시스템의 성능이 초기 검색 단계의 품질에 상당히 의존하며, 매우 전문적이거나 최신 분야의 논문 검색 성능 한계 가능성

- **인용 정확도 검증**: 자동 인용 검증이 모든 오류를 포착하지 못할 수 있으며, 구절 수준의 정밀한 매칭에서 거짓 양성 가능성

- **계산 비용**: 반복적 피드백 루프로 인한 추론 시간 증가 (여러 번의 LM 호출 필요)

- **도메인 편향**: 오픈 액세스 논문 중심 데이터스토어로 인한 특정 출판사나 학파에 대한 편향 가능성

- **후속 연구 방향**:
  - 매우 새로운 논문(최근 수개월)에 대한 검색 성능 개선
  - 다중 언어 과학 문헌 지원 확대
  - 인용 검증의 더욱 정교한 자동화 방법 개발
  - 실시간 논문 인덱싱 갱신 메커니즘 구현
  - 도메인 특화 LM의 추가 학습 및 최적화

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 최대 규모 공개 과학 데이터스토어와 다중 분야 전문가 벤치마크의 구축이 우수하나, 자체 피드백 반복 개선의 기본 개념은 기존 연구의 적용

- **Technical Soundness (기술적 건전성)**: 4.5/5
  - 검색, 재순위, 생성, 피드백 루프의 각 단계가 체계적으로 설계되고 구현되었으나, 일부 설계 선택(피드백 반복 횟수, 재순위 top-N 크기 등)에 대한 상세 정당화 부족

- **Significance (중요도)**: 4.5/5
  - 과학 문헌 합성이라는 실질적 문제 해결 및 인용 정확도 개선의 실무적 가치가 높으나, 생의학/신경과학 등 특정 분야에 제한된 평가

- **Clarity (명확성)**: 4/5
  - 시스템 구조와 파이프라인이 명확하게 설명되었으나, 일부 기술적 세부 사항(LM 학습 데이터 필터링, 재순위 지정기 아키텍처)에 대한 상세 설명 부족

- **Overall (종합)**: 4.4/5

**총평**: 본 논문은 과학 문헌 합성을 위한 현실적이고 포괄적인 RAG 시스템을 제시하며, 최대 규모의 공개 데이터스토어와 다중 분야 전문가 벤치마크를 통해 중요한 평가 기반을 마련했다. 특히 인용 정확도 개선과 전문가 수준의 성능 달성이 실무적 가치가 크며, 모든 자원을 공개하여 재현성과 확장성을 확보한 점이 우수하다.

## Related Papers

- 🏛 기반 연구: [[papers/659_REALM_Retrieval-Augmented_Language_Model_Pre-Training/review]] — REALM의 검색 증강 사전훈련 방법론이 OpenScholar의 과학논문 검색 증강 생성의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/034_A_Survey_on_RAG_Meeting_LLMs_Towards_Retrieval-Augmented_Lar/review]] — RAG 기반 LLM 서베이의 방법론을 과학문헌 특화 도메인으로 확장하여 구체적인 구현체를 제시한다.
- 🔄 다른 접근: [[papers/087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi/review]] — AI2 Scholar QA와 유사하게 학술 문헌 종합을 다루지만 더 대규모 오픈 액세스 데이터로 접근한다.
- 🏛 기반 연구: [[papers/373_Generalization_Bias_in_Large_Language_Model_Summarization_of/review]] — 과학 문헌 합성에서 LLM의 신뢰성 있는 요약 생성을 위한 기반 시스템을 제공한다.
- 🔄 다른 접근: [[papers/493_Litllm_A_toolkit_for_scientific_literature_review/review]] — 문헌 리뷰 자동화와 과학 문헌 종합이 서로 다른 접근으로 학술 정보 처리 문제를 해결한다
- 🏛 기반 연구: [[papers/604_Pasa_An_llm_agent_for_comprehensive_academic_paper_search/review]] — 과학 문헌 합성을 위한 검색 증강 기법의 기반을 제공한다
- 🔗 후속 연구: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — RAG의 일반적 프레임워크가 과학 문헌 합성에 특화된 OpenScholar 시스템으로 구체화됨
- 🔄 다른 접근: [[papers/404_Hiperrag_High-performance_retrieval_augmented_generation_for/review]] — 과학 문헌 검색과 합성을 위한 서로 다른 접근법을 제시하여, 대규모 과학 지식 처리 시스템 설계 관점을 비교할 수 있다.
- 🔗 후속 연구: [[papers/862_Using_artificial_intelligence_for_systematic_review_the_exam/review]] — OpenScholar의 과학문헌 합성 기능을 체계적 문헌고찰로 특화한 구체적 적용이다
- 🔗 후속 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 과학 문헌 검색 및 합성 기능을 통해 분자 문법 학습에 필요한 화학 지식을 체계적으로 확장할 수 있음
- 🧪 응용 사례: [[papers/773_Stealing_creators_workflow_A_creator-inspired_agentic_framew/review]] — 과학 문헌 합성 기술을 짧은 형식 동영상 제작이라는 새로운 매체에 적용한다
- 🔗 후속 연구: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 과학 문헌 합성을 위한 검색 기반 시스템으로, 극단적 요약을 넘어 포괄적인 문헌 종합 기능을 제공합니다.
- 🔄 다른 접근: [[papers/457_Language_agents_achieve_superhuman_synthesis_of_scientific_k/review]] — OpenScholar는 과학 문헌 합성에 특화된 검색 증강 모델로, PaperQA2와 다른 아키텍처로 유사한 문제를 해결한다
- 🔄 다른 접근: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 검색 증강 생성과 과학문헌 합성은 과학 연구에서 서로 다른 정보 활용 접근법을 제시한다
- 🔗 후속 연구: [[papers/087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi/review]] — OpenScholar의 과학 문헌 합성 기능을 질의응답 형태로 확장하여 더 직관적인 사용자 인터페이스를 제공한다.
- 🏛 기반 연구: [[papers/178_Can_ai_examine_novelty_of_patents_Novelty_evaluation_based_o/review]] — 과학 문헌의 검색 증강 합성이 특허 신규성 평가를 위한 선행 기술 분석의 토대를 제공한다.
- 🧪 응용 사례: [[papers/897_Can_AI_review_the_scientific_literature__and_figure_out_what/review]] — 과학 문헌 종합을 위한 검색 증강 시스템으로 AI 문헌 검토의 구체적 구현 사례를 제시한다
- 🧪 응용 사례: [[papers/318_Estimating_optimal_context_length_for_hybrid_retrievalaugmen/review]] — 과학 문헌 합성 시스템에 최적화된 검색 컨텍스트 길이 추정을 실제 적용한다
