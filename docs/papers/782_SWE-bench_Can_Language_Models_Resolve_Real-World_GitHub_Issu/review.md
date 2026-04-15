---
title: "782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu"
authors:
  - "Carlos E. Jimenez"
  - "John Yang"
  - "Alexander Wettig"
  - "Shunyu Yao"
  - "Kexin Pei"
date: "2024.11"
doi: "10.48550/arXiv.2310.06770"
arxiv: ""
score: 4.6
essence: "실제 GitHub 이슈 2,294개를 기반으로 한 소프트웨어 엔지니어링 벤치마크 SWE-bench를 제시하며, 최고 성능 모델(Claude 2)도 1.96%의 낮은 해결율만 달성하여 대규모 언어 모델의 실제 소프트웨어 엔지니어링 능력의 한계를 명확히 드러낸다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jimenez et al._2024_SWE-bench Can Language Models Resolve Real-World GitHub Issues.pdf"
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

> **저자**: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan | **날짜**: 2024-11-11 | **DOI**: [10.48550/arXiv.2310.06770](https://doi.org/10.48550/arXiv.2310.06770)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: SWE-bench는 GitHub 이슈를 실제 코드베이스와 함께 제시하여 언어 모델이 생성한 패치를 단위 테스트로 검증하는 방식으로 작동*

실제 GitHub 이슈 2,294개를 기반으로 한 소프트웨어 엔지니어링 벤치마크 SWE-bench를 제시하며, 최고 성능 모델(Claude 2)도 1.96%의 낮은 해결율만 달성하여 대규모 언어 모델의 실제 소프트웨어 엔지니어링 능력의 한계를 명확히 드러낸다.

## Motivation

- **Known**: 기존 HumanEval, MBPP 등의 코딩 벤치마크는 수십 줄의 자체 포함된(self-contained) 문제만 평가하며, 기존 NLP 벤치마크들이 포화되어 있음
- **Gap**: 실제 소프트웨어 엔지니어링은 대규모 리포지토리 이해, 다중 파일/함수 간 조율, 복잡한 컨텍스트 처리를 요구하는데 이를 평가할 벤치마크가 부재
- **Why**: 언어 모델의 실제 실무 능력을 정확히 평가하고, 향후 개발 방향을 수립하기 위해 현실적이고 도전적인 벤치마크 필요
- **Approach**: 실제 GitHub 이슈-PR 쌍을 3단계 필터링(속성 필터링, 실행 필터링)으로 정제하여 고품질 작업 인스턴스 구성

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 3단계 데이터 파이프라인: (1) 인기 리포지토리 90,000개 PR 수집 → (2) 이슈 해결 + 테스트 기여 PR 필터링 → (3) 실행 기반 필터링으로 2,294개 최종 작업 구성*

1. **포괄적 벤치마크 구성**: 12개 인기 Python 리포지토리에서 2,294개의 실제 이슈를 기반으로 한 고품질 벤치마크 생성. 각 작업은 평균 438K 라인의 대규모 코드베이스, 195단어의 이슈 설명, 평균 1.7개 파일과 3.0개 함수 수정 필요

2. **상태 최고 모델의 성능 한계 실증**: Claude 2 (BM25 retriever 포함) 1.96%, GPT-4는 미포함되었으나 공개 모델 중 SWE-Llama 13b가 경쟁 가능 수준의 성능 달성

3. **학습 데이터 및 파인튠드 모델 공개**: 37개 추가 리포지토리에서 19,000개 비테스팅 인스턴스로 구성된 SWE-bench-train 및 CodeLlama 기반 SWE-Llama 7b/13b 모델 공개

4. **지속적 확장 가능성**: 최소 인간 개입으로 새로운 Python 리포지토리를 추가할 수 있는 자동화된 파이프라인 설계

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 12개 리포지토리별 작업 분포 (django 850개가 가장 많고, flask 11개가 가장 적음)*

### 데이터 구성 방법론

- **Stage I**: GitHub에서 ~90,000개 PR 수집 (>90% Python 코드, 인기 리포지토리 중심)
- **Stage II**: (1) 이슈 해결 PR (2) 테스트 변경 포함 조건으로 후보 작업 선별
- **Stage III**: PR 적용 전후 테스트 실행, fail-to-pass 테스트 존재 확인, 설치/런타임 오류 제거

### 작업 포뮬레이션

- **입력**: 이슈 텍스트 설명 + 완전한 코드베이스 스냅샷
- **출력**: Unified diff 형식의 패치 파일
- **평가**: `patch` 유틸리티로 패치 적용 후 모든 테스트 통과 확인 (fail-to-pass + 회귀 테스트 ~51개)

### 파인튠 학습 전략

- **모델**: CodeLlama 7b/13b (기존 모델은 지시문 따르기 능력 부족)
- **데이터**: 19,000 (이슈-PR 쌍), 테스트 변경 요구사항 제거로 크기 확대
- **최적화**: LoRA로 주의(attention) 부계층만 파인튠, 30,000 토큰 이상 시퀀스 제외 (10,000개로 축소)

## Originality

- **현실성 기반 구성**: 실제 오픈소스 커뮤니티 데이터로 벤치마크 구축하여 기존 합성 데이터 벤치마크와 차별화
- **자동화된 품질 관리**: 3단계 필터링 파이프라인으로 체계적 품질 보증 및 확장성 확보
- **장문맥 처리 요구**: 438K 라인의 대규모 코드베이스와 평균 195단어 이슈로 다중 파일 추론 능력 평가
- **실행 기반 평가**: 형식적 정확성이 아닌 실제 테스트 통과로 정량적 검증 (fail-to-pass 테스트 평균 9.1개, 회귀 테스트 중앙값 51개)
- **공개 모델 에코시스템 지원**: 별도 학습 데이터셋(SWE-bench-train) 및 파인튠드 모델 공개로 오픈소스 커뮤니티 기여

## Limitation & Further Study

### 한계

- **초기 평가 제한**: Claude 2만 1.96% 해결 (GPT-4 평가 미포함), 대규모 모델의 성능 비교 부족
- **검색 기반 접근의 의존성**: BM25 retriever에 의존하여 실제 현실성 (파일 탐색, 오류 처리) 부분 추상화
- **Python 언어 편향**: 12개 모두 Python 리포지토리로 언어 다양성 부족
- **패치 형식 제약**: Unified diff 형식만 지원하여 구조적 리팩토링 등 복잡한 변환 표현 한계
- **테스트 기여 리포지토리 편향**: Stage II에서 테스트 변경 PR만 선별하여 테스트 커버리지 높은 리포지토리 과대대표

### 후속 연구 방향

- **에이전트 기반 접근**: 코드 실행, 오류 분석, 반복적 디버깅을 포함한 의사결정 에이전트 평가
- **다중 언어 확장**: Java, JavaScript, Go 등 다양한 언어의 리포지토리 추가
- **더 강력한 모델 평가**: GPT-4, Gemini 등 최신 모델 벤치마킹
- **SWE-bench Lite 확대**: 더 큰 규모의 간단한 버전으로 단계적 진입 장벽 낮추기
- **창의적 해결책 평가**: 참조 PR과 다른 해결책의 동등성 판정 메커니즘


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.8/5
- Clarity: 4.7/5
- Overall: 4.6/5

**총평**: SWE-bench는 기존 코딩 벤치마크의 인공성을 벗어나 실제 GitHub 이슈 해결을 통해 언어 모델의 실무 소프트웨어 엔지니어링 능력을 엄격하게 평가하는 중요한 작업이며, 공개 데이터셋과 자동화된 확장성으로 장기적 학술 가치가 높다. 다만 검색 기반 접근과 초기 평가 모델 제한은 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/476_Large_language_models_orchestrating_structured_reasoning_ach/review]] — 실제 소프트웨어 엔지니어링 문제 해결에서 LLM 에이전트의 한계를 보여주는 연구로, 구조화된 추론을 통한 성능 향상 방법과 대조됨
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — SWE-bench를 기반으로 머신러닝 에이전트의 코드 작업 능력을 더 광범위하게 평가하는 벤치마크로 확장됨
- 🏛 기반 연구: [[papers/362_From_LLMs_to_LLM-based_Agents_for_Software_Engineering_A_Sur/review]] — LLM 기반 소프트웨어 엔지니어링 에이전트의 현재 능력과 한계에 대한 종합적인 이해를 제공하는 기초 연구
- ⚖️ 반론/비판: [[papers/320_Evaluating_Large_Language_Models_in_Scientific_Discovery/review]] — 코드 작성에 특화된 LLM의 성능을 긍정적으로 평가한 연구로, SWE-bench의 낮은 성능 결과와 대조적 관점을 제시
- 🔗 후속 연구: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — SWE-bench의 실제 GitHub 이슈 해결이 MLDebugging의 다중 라이브러리 디버깅을 실제 소프트웨어 개발 환경으로 확장함
- 🏛 기반 연구: [[papers/731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit/review]] — 실제 GitHub 이슈 해결 능력을 평가하는 벤치마크로, SciReplicate-Bench의 알고리즘 구현 평가에 필요한 코드 생성 능력의 기초적 평가 틀을 제공한다
- 🔗 후속 연구: [[papers/327_Experiential_co-learning_of_software-developing_agents/review]] — 실제 GitHub 이슈 해결을 위한 언어 모델 연구가 경험적 협력학습을 통한 소프트웨어 개발 에이전트로 구체화되었다
- ⚖️ 반론/비판: [[papers/476_Large_language_models_orchestrating_structured_reasoning_ach/review]] — Kaggle에서 최상위 성능을 달성한 긍정적 결과로, SWE-bench의 낮은 성능과 대조되어 LLM 에이전트 능력의 다른 측면을 보여줌
- 🏛 기반 연구: [[papers/888_X-webagentbench_A_multilingual_interactive_web_benchmark_for/review]] — 실제 GitHub 이슈 해결 능력을 평가하는 기존 벤치마크를 기반으로 다국어 웹 환경에서 에이전트 성능을 평가하는 것으로 확장한 발전된 평가 체계임
- 🏛 기반 연구: [[papers/205_Chatdev_Communicative_agents_for_software_development/review]] — 실제 GitHub 이슈 해결 벤치마크를 소프트웨어 개발 에이전트의 성능 평가 기준으로 활용한다
- 🧪 응용 사례: [[papers/362_From_LLMs_to_LLM-based_Agents_for_Software_Engineering_A_Sur/review]] — 실제 GitHub 이슈 해결 벤치마크가 소프트웨어 공학 에이전트의 실질적 성능 검증을 제공한다
- 🔗 후속 연구: [[papers/590_Openhands_An_open_platform_for_ai_software_developers_as_gen/review]] — OpenHands 플랫폼이 SWE-bench의 GitHub 이슈 해결을 더 포괄적인 소프트웨어 개발 작업으로 확장함
