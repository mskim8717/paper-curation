---
title: "429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks"
authors:
  - "Xueyu Hu"
  - "Ziyu Zhao"
  - "Shuang Wei"
  - "Ziwei Chai"
  - "Qianli Ma"
date: "2024"
doi: "arXiv:2401.05507"
arxiv: ""
score: 4.5
essence: "본 논문은 LLM 기반 에이전트의 데이터 분석 능력을 평가하기 위한 최초의 종합 벤치마크 **InfiAgent-DABench**를 제안한다. 257개의 폐쇄형(closed-form) 데이터 분석 질문과 52개의 CSV 파일로 구성된 DAEval 데이터셋과, 이를 평가하기 위한 에이전트 프레임워크를 제공한다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2024_Infiagent-dabench Evaluating agents on data analysis tasks.pdf"
---

# InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks

> **저자**: Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli Ma, Guoyin Wang, Xuwu Wang, Jing Su, Jingjing Xu, Ming Zhu, Yao Cheng, Jianbo Yuan, Jiwei Li, Kun Kuang, Yang Yang, Hongxia Yang, Fei Wu | **날짜**: 2024 | **DOI**: [arXiv:2401.05507](https://arxiv.org/abs/2401.05507)

---

## Essence

![Figure 1](figures/fig1.webp) *LLM 기반 에이전트가 CSV 파일을 입력받아 ReAct 방식으로 코드를 작성, 실행하고 결과를 도출하는 데이터 분석 태스크의 평가 프로세스*

본 논문은 LLM 기반 에이전트의 데이터 분석 능력을 평가하기 위한 최초의 종합 벤치마크 **InfiAgent-DABench**를 제안한다. 257개의 폐쇄형(closed-form) 데이터 분석 질문과 52개의 CSV 파일로 구성된 DAEval 데이터셋과, 이를 평가하기 위한 에이전트 프레임워크를 제공한다.

## Motivation

- **Known**: 
  - LLM 기반 에이전트(AutoGPT, BabyAGI 등)는 추론, 계획, 메모리, 도구 활용 능력을 보유하고 있음
  - 데이터 분석은 LLM 기반 에이전트가 도전할 수 있는 실무적으로 중요한 태스크 영역임
  - OpenAI Advanced Data Analysis(ADA)와 같은 상용 솔루션과 오픈소스 에이전트들이 등장

- **Gap**: 
  - 데이터 분석 태스크를 평가하기 위한 종합적인 벤치마크가 부재함
  - 기존 코드 완성 벤치마크(HumanEval, MBPP, DS-1000)는 작은 코드 스니펫 완성만 요구하며, 계획, 자체 디버깅, 엔드-투-엔드(end-to-end) 문제 해결 능력을 평가하지 못함

- **Why**: 
  - 개방형(open-ended) 데이터 분석 질문은 정확한 자동 평가가 어려움
  - GPT-4 기반 자동 평가의 신뢰성이 낮음(인간 전문가와 67% 일치도만 달성)

- **Approach**: 
  - 포맷 프롬팅(format-prompting) 기법을 통해 개방형 질문을 폐쇄형 포맷으로 변환
  - "@answer_name[answer]" 형식의 구조화된 답변으로 정규표현식 기반 자동 평가 가능하게 함

## Achievement

![Figure 2](figures/fig2.webp) *DAEval 구성 워크플로우: CSV 파일 수집 → 설명 생성 → 개념 기반 질문 생성 → 제약조건 및 포맷 요구사항 생성 → 인간 검증*

1. **최초의 데이터 분석 벤치마크**: 257개 질문, 52개 CSV 파일, 다양한 도메인과 18개 데이터 분석 핵심 개념 포함

2. **광범위한 평가**: 34개 최신 LLM 평가를 통해 현재 LLM의 데이터 분석 능력의 한계 규명

3. **개선된 오픈소스 에이전트**: DAInstruct 명령어 튜닝 데이터셋을 기반으로 학습한 DAAgent-34B가 GPT-3.5를 3.9% 상회하는 성능 달성

## How

![Figure 2](figures/fig2.webp) *데이터 분석 개념, CSV 파일 설명, 제약조건을 통한 폐쇄형 질문 생성 프로세스*

- **데이터셋 구축**:
  - GitHub에서 수집한 실제 CSV 파일을 사용 (의미성, 영어 사용, 충분한 규모 기준)
  - GPT-3.5로 파일 설명 자동 생성 (컬럼명, 데이터타입, 결측값 정보)
  - 데이터 분석 전문가 인터뷰를 통해 18개 핵심 개념 추출

- **포맷 프롬팅 기법**:
  - GPT-4에 지시하여 개방형 질문에 대한 상세 제약조건 및 포맷 요구사항 생성
  - 방법론, 워크플로우, 통계 파라미터에 대한 명시적 지시사항 포함
  - 구조화된 답변 포맷으로 정규표현식 기반 정확한 매칭 가능

- **품질 보증**:
  - 모든 질문과 답변을 인간 전문가가 검증
  - 부적절한 샘플 필터링으로 고품질 데이터셋 확보

- **에이전트 프레임워크**:
  - ReAct 패러다임 기반 에이전트 구현 (계획 → 코드 작성 → Python 샌드박스 실행 → 결론)
  - 자동 평가 및 성능 분석을 지원

- **명령어 튜닝 데이터셋 구성**:
  - 데이터 분석 키워드와 실제 CSV 파일 기반 명령어 자동 생성
  - GPT-4와 에이전트 프레임워크로 응답 생성
  - 오픈소스 LLM의 데이터 분석 특화 학습용 DAInstruct 제작

## Originality

- **최초성**: 데이터 분석 에이전트 평가를 위한 첫 번째 종합 벤치마크로 신규 연구 영역 개척

- **혁신적 평가 방법론**: 
  - 포맷 프롬팅 기법으로 개방형 질문의 자동 평가 문제를 우아하게 해결
  - GPT-4 자동 평가의 불신뢰성(67%) 문제를 포맷 표준화로 극복

- **종합적 데이터셋 설계**:
  - 실제 CSV 파일과 전문가 인터뷰 기반 핵심 개념 통합
  - 정보 밀도 높은 질문 생성 (단일 또는 다중 개념 포함)
  - 체계적 인간 검증 프로세스

- **실무 기여**: 
  - DAInstruct 명령어 튜닝 데이터셋으로 오픈소스 LLM의 데이터 분석 능력 강화
  - 34개 LLM 벤치마킹으로 산업 현황 파악

## Limitation & Further Study

- **평가 방법론의 한계**:
  - 폐쇄형 질문으로의 변환 과정에서 원래 문제의 일부 뉘앙스 손실 가능성
  - 데이터 시각화 관련 질문을 명시적으로 제외 (폐쇄형 변환 어려움)
  - 복잡한 다단계 분석이나 해석적 판단이 필요한 질문의 표현 제약

- **데이터셋 범위**:
  - CSV 형식만 고려 (JSON, XML 등 다른 구조화된 데이터 형식 미포함)
  - 52개 파일로 제한적 (도메인 다양성 추가 필요)

- **후속 연구 방향**:
  - 시각화 관련 태스크를 위한 대안적 평가 방법 개발
  - 더 큰 규모의 데이터셋 확장 (도메인, 문제 난이도 다양화)
  - 멀티모달 데이터 분석 에이전트 평가 프레임워크 구축
  - 에이전트의 자체 디버깅 및 오류 회복 능력에 대한 심화 분석

## Evaluation

- **Novelty**: 5/5 - 데이터 분석 에이전트 벤치마크의 최초 제안이며, 포맷 프롬팅을 통한 폐쇄형 평가 방법이 혁신적

- **Technical Soundness**: 4/5 - 방법론이 체계적이고 포맷 프롬팅 기법이 효과적이나, 개방형→폐쇄형 변환 과정에서의 정보 손실에 대한 심화 분석 부족

- **Significance**: 5/5 - LLM 에이전트의 실무 능력(데이터 분석) 평가라는 중요한 문제를 해결하며, 산업적·학술적 가치가 높음

- **Clarity**: 4/5 - 전반적으로 명확하지만, 포맷 프롬팅의 구체적 프롬프트 예시와 인간 검증 기준이 본문에 부족

- **Overall**: 4.5/5

**총평**: 본 논문은 LLM 기반 에이전트의 데이터 분석 능력을 평가하기 위한 최초의 종합 벤치마크를 제시하며, 포맷 프롬팅을 통한 폐쇄형 평가 방법론이 실용적이고 창의적이다. 광범위한 LLM 벤치마킹과 오픈소스 DAAgent 개발로 실제 임팩트를 제공하지만, 평가 방식의 표현 한계와 데이터셋 규모 제약이 개선될 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/review]] — 데이터 기반 과학 발견에서 언어 에이전트의 능력을 평가하는 또 다른 종합적 벤치마크로, 데이터 분석에 특화된 평가와 비교됨
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 머신러닝 에이전트 평가를 위한 벤치마크로, 데이터 분석 작업 평가를 머신러닝 실험 전반으로 확장
- 🧪 응용 사례: [[papers/253_Data_Interpreter_An_LLM_Agent_For_Data_Science/review]] — 데이터 과학을 위한 LLM 에이전트의 실제 구현체로, InfiAgent-DABench에서 평가할 수 있는 구체적 시스템 사례
- 🔄 다른 접근: [[papers/294_Dsbench_How_far_are_data_science_agents_to_becoming_data_sci/review]] — 데이터 과학 에이전트가 실제 데이터 과학자가 되기까지의 거리를 측정하는 다른 관점의 벤치마크
- 🔄 다른 접근: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 데이터 분석 작업에서 에이전트 평가를 위한 다른 벤치마크로, 단일 작업 평가와 다중 단계 도구 사용 평가를 비교
- 🔄 다른 접근: [[papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/review]] — LLM 기반 에이전트의 데이터 분석 능력 평가에 특화된 벤치마크로, 과학 발견 전반과 데이터 분석 특화 평가를 비교
- 🔄 다른 접근: [[papers/888_X-webagentbench_A_multilingual_interactive_web_benchmark_for/review]] — 에이전트 평가 벤치마크라는 동일한 목표를 가지지만 X-WebAgentBench는 다국어 웹 환경에, InfiAgent-DABench는 데이터 분석 작업에 특화된 다른 평가 영역임
- 🔄 다른 접근: [[papers/294_Dsbench_How_far_are_data_science_agents_to_becoming_data_sci/review]] — 데이터 분석 작업 평가와 AutoML 도구 평가는 데이터 과학 자동화의 서로 다른 측면을 벤치마킹한다
