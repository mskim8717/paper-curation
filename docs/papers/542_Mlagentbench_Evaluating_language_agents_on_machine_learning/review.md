---
title: "542_Mlagentbench_Evaluating_language_agents_on_machine_learning"
authors:
  - "Qian Huang"
  - "Jian Vora"
  - "Percy Liang"
  - "Jure Leskovec"
date: "2023"
doi: "arXiv:2310.03302"
arxiv: ""
score: 4.2
essence: "본 논문은 **머신러닝 실험을 자동으로 수행할 수 있는 언어 모델 기반 에이전트를 평가하기 위한 벤치마크(MLAgentBench)**를 제안한다. 13개의 다양한 ML 작업을 통해 최신 언어 모델들의 ML 실험 수행 능력을 체계적으로 평가한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Cross-lingual_Language_Model_Pretraining"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2023_Mlagentbench Evaluating language agents on machine learning experimentation.pdf"
---

# MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation

> **저자**: Qian Huang, Jian Vora, Percy Liang, Jure Leskovec | **날짜**: 2023 | **DOI**: [arXiv:2310.03302](https://arxiv.org/abs/2310.03302)

---

## Essence

![Figure 1](figures/fig1.webp) *MLAgentBench의 개요. 각 환경은 작업 설명, 시작 파일, 평가기를 포함하며, 에이전트는 파일을 읽고/쓰고 Python 코드를 반복적으로 실행하여 최종 제출 파일을 생성*

본 논문은 **머신러닝 실험을 자동으로 수행할 수 있는 언어 모델 기반 에이전트를 평가하기 위한 벤치마크(MLAgentBench)**를 제안한다. 13개의 다양한 ML 작업을 통해 최신 언어 모델들의 ML 실험 수행 능력을 체계적으로 평가한다.

## Motivation

- **Known**: 신경망 구조 탐색(NAS)과 AutoML 같은 부분 자동화 기술이 존재하며, 강력한 언어 모델이 텍스트 이해와 생성에 뛰어남
- **Gap**: ML 실험 전체 파이프라인(가설 수립→실험 설계→결과 분석→반복)을 자동으로 수행할 수 있는 에이전트의 능력과 한계를 체계적으로 평가할 벤치마크가 부재
- **Why**: ML 연구는 광범위한 도메인 지식, 함수형 코드 작성, 실험 결과 해석을 요구하는 복잡한 반복 과정이며, 이를 자동화할 수 있다면 ML 연구 접근성을 크게 높일 수 있음
- **Approach**: 명확한 목표와 자동 평가 시스템을 갖춘 13개의 ML 작업 벤치마크를 구축하고, ReAct 프레임워크 기반의 에이전트를 설계하여 여러 최신 언어 모델(Claude v3 Opus, GPT-4, Gemini-Pro 등)을 평가

## Achievement

![Figure 2](figures/fig2.webp) *LM 기반 에이전트의 개요. 각 단계에서 프롬프트와 문맥은 단계별 반영(reflection), 고차원 계획, 사실 확인, 추론을 포함*

1. **벤치마크 구축**: CIFAR-10 같은 고전적 데이터셋부터 BabyLM, Kaggle 챌린지 등 최신 연구 문제까지 포함하는 13개 태스크로 구성된 포괄적 벤치마크 생성
   
2. **성능 평가**: Claude v3 Opus 기반 에이전트가 **평균 37.5% 성공률**을 달성하며, 기존 ReAct 및 AutoGPT 에이전트 대비 우수한 성능 입증

3. **작업별 편차 분석**:
   - 고전적 작업(house-price): 100% 성공률
   - Kaggle 챌린지 및 BabyLM: 0~25% 성공률
   - 이는 사전학습 시기 이후의 새로운 데이터셋에서의 일반화 한계를 시사

4. **해석가능성**: 에이전트의 연구 계획과 행동이 높은 해석가능성을 보여 인간의 개입과 감시가 가능함을 입증

## How

![Figure 3](figures/fig3.webp) *시간 스텝별 성능 평가*

### 환경 설계
- **작업 사양**: 텍스트 설명, 시작 파일(데이터, 기본 코드), 평가기로 구성
- **통일된 인터페이스**: 파일 시스템 작업(읽기, 쓰기), 스크립트 실행, 문제 이해 등 기본 및 복합 액션 12개 정의(Table 1)
- **상태 관리**: 작업 공간의 파일/디렉토리 상태 추적

### 에이전트 아키텍처
- **ReAct 프레임워크 기반**: 각 타임스텝에서
  1. 메모리(이전 액션, 관찰, 계획) 정보로 프롬프트 구성
  2. LM이 반성(rationale) 및 액션 생성
  3. 환경 실행 후 메모리 업데이트
  
- **복합 액션**: 단순 파일 조작 넘어 LM을 활용한 "파일 이해(Understand File)", "스크립트 편집(Edit Script)" 등으로 추상화 수준 향상

- **프롬프트 구성 요소**:
  - 현재까지의 상호작용 기록
  - 단계별 반성 및 고차원 계획
  - 사실 확인(fact-checking) 섹션
  - 추론-행동 순서(reasoning-before-action)

### 평가 지표
- **역량(Competence)**: 기본선 대비 성능 메트릭 10% 이상 개선 달성 비율
- **효율성(Efficiency)**: LM 쿼리에 소비된 토큰 수 및 시간

## Originality

- **첫 종합 벤치마크**: ML 실험 전체 파이프라인의 자동화 능력을 평가하는 최초의 체계적 벤치마크 제시
- **다양한 시간 지평의 작업**: 고전적 데이터셋(CIFAR-10)부터 사전학습 이후의 최신 Kaggle/연구 과제까지 포함하여 시간 외삽(temporal extrapolation) 능력 평가
- **해석가능성 중시**: 자동화와 함께 에이전트 행동의 추적 가능성과 인간 개입 가능성을 명시적으로 설계
- **포괄적 비교**: 7개 최신 언어 모델에 대한 광범위한 벤치마킹
- **구조화된 액션 추상화**: 기본 파일/코드 실행 액션과 LM 기반 복합 액션의 계층적 설계

## Limitation & Further Study

### 한계
- **낮은 절대 성능**: 평균 37.5% 성공률은 신뢰성 있는 자동화에 부족하며, Kaggle 등 최신 과제에서 0% 성공 가능
- **사전학습 데이터 의존성**: 사전학습 시기 이후의 새로운 데이터셋에 대한 일반화 실패
- **장기 계획 부재**: 장기적 실험 전략 수립보다 단기적 액션 반복에 의존
- **할루시네이션**: 현재 진행 상황에 대한 부정확한 이해로 인한 무의미한 반복
- **비용 고려 미흡**: 토큰 사용량과 계산 비용의 상세한 분석 부재
- **작업 선정 편향**: 실행 시간이 수분 수준의 경량 작업으로 제한

### 향후 연구 방향
- 장기적 계획 및 재계획 메커니즘 개발
- 할루시네이션 감소 기법 연구
- 메모리 활용도 최적화를 통한 효율성 개선
- 대규모/장시간 실행 작업에 대한 확장성 연구
- 인간-에이전트 협력 프레임워크의 실제 구현
- 새로운 데이터셋/방법론에 대한 적응 능력 강화

## Evaluation

- **Novelty**: 4.5/5 
  - ML 자동화 평가 벤치마크로서 참신하고, 시간 외삽 과제 포함이 우수하나, 개별 기법의 혁신성은 제한적
  
- **Technical Soundness**: 4/5 
  - 환경 설계와 평가 메트릭이 명확하고 재현 가능하나, 사전학습 데이터 누출 가능성과 장기 계획 기법의 이론적 근거 부족
  
- **Significance**: 4.5/5 
  - ML 연구 자동화의 가능성과 한계를 체계적으로 규명하는 중요한 기여이나, 절대 성능의 낮음으로 실무 적용성은 제한적
  
- **Clarity**: 4/5 
  - 전반적으로 명확한 설명이나, 프롬프트 구성의 세부 사항과 일부 평가 기준이 불충분
  
- **Overall**: 4.2/5

**총평**: 본 논문은 **언어 모델 기반 ML 자동화의 가능성과 한계를 체계적으로 평가하는 첫 종합 벤치마크**를 제시하여 학계에 중요한 기준점을 제공한다. 다양한 작업 범위와 포괄적 모델 비교는 강점이나, 37.5%의 제한적 성공률과 시간 외삽 과제의 대규모 실패는 현재 언어 모델 에이전트의 신뢰성에 대한 현실적인 인식을 제시한다. 향후 계획 수립 및 재계획 메커니즘 연구에 방향성을 제시하는 가치 있는 기초 연구이다.

## Related Papers

- 🔄 다른 접근: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — 머신러닝 실험 자동화라는 같은 목표를 가지지만 언어모델 기반 vs 기존 ML 방법론이라는 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/121_Autokaggle_A_multi-agent_framework_for_autonomous_data_scien/review]] — 데이터 사이언스 작업의 완전 자동화를 통해 MLAgentBench의 평가 범위를 실제 업무 환경으로 확장한다.
- 🧪 응용 사례: [[papers/549_Mlr-copilot_Autonomous_machine_learning_research_based_on_la/review]] — LLM 기반 MLR 연구 자동화의 실제 적용 사례를 통해 벤치마크 결과의 실용성을 검증할 수 있다.
- 🧪 응용 사례: [[papers/016_A_practical_evaluation_of_AutoML_tools_for_binary_multiclass/review]] — AutoML 도구 벤치마킹 방법론을 머신러닝 에이전트 평가 프레임워크에 적용하여 에이전트 성능 측정 기준을 개선할 수 있다.
- 🔗 후속 연구: [[papers/546_Mlgym_A_new_framework_and_benchmark_for_advancing_ai_researc/review]] — 머신러닝 에이전트 벤치마킹을 포괄적인 AI 연구 환경으로 확장한다
- 🔗 후속 연구: [[papers/731_Scireplicate-bench_Benchmarking_llms_in_agent-driven_algorit/review]] — 머신러닝 작업에서 언어 에이전트를 평가하는 벤치마크로, SciReplicate-Bench의 NLP 알고리즘 복제를 더 넓은 ML 도메인으로 확장한다
- 🏛 기반 연구: [[papers/670_ResearchCodeAgent_An_LLM_Multi-Agent_System_for_Automated_Co/review]] — 머신러닝 에이전트 평가 벤치마크가 ResearchCodeAgent의 코드 생성 품질을 측정하는 기반 제공
- 🏛 기반 연구: [[papers/253_Data_Interpreter_An_LLM_Agent_For_Data_Science/review]] — LLM의 기계학습 작업 수행 능력을 평가하는 기반 벤치마크
- 🔗 후속 연구: [[papers/769_StableToolBench_Towards_Stable_Large-Scale_Benchmarking_on_T/review]] — 일반적인 기계학습 에이전트 벤치마크가 과학 도구 사용에 특화된 안정적 평가로 확장됨
- 🔗 후속 연구: [[papers/069_Agentomics-ML_Autonomous_Machine_Learning_Experimentation_Ag/review]] — 머신러닝 벤치마킹을 생물학적 데이터 분석이라는 특화된 도메인으로 확장한 응용 사례이다
- 🔗 후속 연구: [[papers/782_SWE-bench_Can_Language_Models_Resolve_Real-World_GitHub_Issu/review]] — SWE-bench를 기반으로 머신러닝 에이전트의 코드 작업 능력을 더 광범위하게 평가하는 벤치마크로 확장됨
- 🔗 후속 연구: [[papers/429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks/review]] — 머신러닝 에이전트 평가를 위한 벤치마크로, 데이터 분석 작업 평가를 머신러닝 실험 전반으로 확장
- 🔗 후속 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 머신러닝 에이전트 벤치마크로, 과학적 도구 사용을 머신러닝 실험 전반으로 확장하는 평가 프레임워크
- 🔄 다른 접근: [[papers/147_Aviary_training_language_agents_on_challenging_scientific_ta/review]] — MLAgentBench의 기계학습 에이전트 평가와 Aviary의 과학 언어 에이전트 훈련은 서로 다른 관점에서 AI 에이전트의 과학적 능력을 다룬다
- 🏛 기반 연구: [[papers/293_Ds-agent_Automated_data_science_by_empowering_large_language/review]] — MLAgentBench가 제공하는 머신러닝 에이전트 평가 프레임워크는 DS-Agent 같은 데이터 사이언스 자동화 시스템의 성능 측정 기반이 됨
- 🔗 후속 연구: [[papers/463_Large_language_model_agent_for_hyper-parameter_optimization/review]] — MLAgentBench의 머신러닝 에이전트 평가가 AgentHPO 같은 특화된 최적화 에이전트의 성능 검증으로 확장됨
- 🔗 후속 연구: [[papers/596_OWL_Optimized_Workforce_Learning_for_General_Multi-Agent_Ass/review]] — 기계학습 에이전트 평가를 통해 OWL의 워크포스 학습 패러다임을 기계학습 태스크 수행 능력 평가로 확장하여 실무 적용성을 검증함
- 🔄 다른 접근: [[papers/121_Autokaggle_A_multi-agent_framework_for_autonomous_data_scien/review]] — 데이터 과학 자동화라는 동일한 목표를 가지지만 AutoKaggle은 경진대회에, MLAgentBench는 일반적인 기계학습 벤치마킹에 특화된 다른 접근법임
- 🧪 응용 사례: [[papers/059_Agent_Laboratory_Using_LLM_Agents_as_Research_Assistants/review]] — 일반적인 연구 지원 프레임워크를 기계학습 실험 평가라는 구체적인 도메인에 적용한 사례를 보여준다
- 🏛 기반 연구: [[papers/543_Mlcopilot_Unleashing_the_power_of_large_language_models_in_s/review]] — 기계학습 에이전트 평가 벤치마크가 과거 경험 기반 ML 솔루션 제시 시스템의 성능을 객관적으로 측정할 수 있는 기준을 제공한다.
- 🔄 다른 접근: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — 머신러닝 에이전트 평가를 위한 다른 벤치마크로, 실제 연구 환경에서의 에이전트 능력 측정 방법론을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — MLAgentBench의 기계학습 실험 평가 프레임워크를 최신 연구논문 구현이라는 더 도전적 과제로 확장한다.
- 🏛 기반 연구: [[papers/1092_Table-llm-specialist_Language_model_specialists_for_tables_u/review]] — 테이블 전문가 모델이 머신러닝 에이전트 벤치마킹을 위한 구조화된 데이터 처리 기반을 제공한다.
- 🔗 후속 연구: [[papers/548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin/review]] — 언어 모델 기반 에이전트의 머신러닝 실험 자동화 능력을 더 포괄적으로 평가하는 발전된 형태다.
- 🔗 후속 연구: [[papers/421_Improving_demonstration_diversity_by_human-free_fusing_for_t/review]] — 기계학습 에이전트 벤치마크에서 Text-to-SQL 시연 다양성 개선 방법론이 더 넓은 ML 작업으로 확장된 응용을 보여준다.
- 🔗 후속 연구: [[papers/635_Productivity_assessment_of_neural_code_completion/review]] — 머신러닝 에이전트 평가를 위한 더 포괄적인 벤치마킹 체계를 제시한다
