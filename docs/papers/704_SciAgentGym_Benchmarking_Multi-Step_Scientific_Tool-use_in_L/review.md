---
title: "704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L"
authors:
  - "Yujiong Shen"
  - "Yajie Yang"
  - "Zhiheng Xi"
  - "Binze Hu"
  - "Huayu Sha"
date: "2026.02"
doi: "10.48550/arXiv.2602.12984"
arxiv: ""
score: 4.4
essence: "과학적 추론의 복잡성을 다단계 도구 활용으로 평가하기 위해, 본 논문은 4개 과학 분야에 걸쳐 1,780개의 도메인 특화 도구를 통합한 인터랙티브 환경 **SciAgentGym**과 이를 평가하는 **SciAgentBench**를 제시합니다. 나아가 도구 간 논리적 의존성을 학습하기 위해 **SciForge** 데이터 합성 방법을 제안하여, 8B 모델이 235B 이상 규모 모델을 능가하는 성과를 달성합니다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/GIS_Workflow_Automation_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shen et al._2026_SciAgentGym Benchmarking Multi-Step Scientific Tool-use in LLM Agents.pdf"
---

# SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents

> **저자**: Yujiong Shen, Yajie Yang, Zhiheng Xi, Binze Hu, Huayu Sha, Jiazheng Zhang, Qiyuan Peng, Junlin Shang, Jixuan Huang, Yutao Fan, Jingqi Tong, Shihan Dou, Ming Zhang, Lei Bai, Zhenfei Yin, Tao Gui, Xingjun Ma, Qi Zhang, Xuanjing Huang, Yu-Gang Jiang | **날짜**: 2026-02-13 | **DOI**: [10.48550/arXiv.2602.12984](https://doi.org/10.48550/arXiv.2602.12984)

---

## Essence

![Figure 1](https://arxiv.org/abs/2602.12984) 

*Figure 1: 다중 단계 과학적 도구 사용의 벤치마킹. LLM 에이전트가 환경과 상호작용하여 복잡한 화학 작업을 해결하는 대표적인 궤적*

과학적 추론의 복잡성을 다단계 도구 활용으로 평가하기 위해, 본 논문은 4개 과학 분야에 걸쳐 1,780개의 도메인 특화 도구를 통합한 인터랙티브 환경 **SciAgentGym**과 이를 평가하는 **SciAgentBench**를 제시합니다. 나아가 도구 간 논리적 의존성을 학습하기 위해 **SciForge** 데이터 합성 방법을 제안하여, 8B 모델이 235B 이상 규모 모델을 능가하는 성과를 달성합니다.

## Motivation

- **Known**: LLM 에이전트의 도구 사용 능력을 평가하는 벤치마크들이 존재하지만, 대부분 정적 질답 형식이거나 도메인 특화 과학적 추론의 복잡성을 충분히 반영하지 못함
- **Gap**: 현존 벤치마크들이 (1) 과학 도구의 광범위한 분포(1,780개 도구), (2) 다단계 워크플로우 실행의 어려움, (3) 도구 간 의존성 학습을 놓치고 있음
- **Why**: 과학적 문제 해결은 본질적으로 가설 수립→도구 실행→피드백 기반 전략 수정의 반복적 프로세스이며, 이를 벤치마킹할 수 있는 대규모 환경이 필요함
- **Approach**: (1) 4개 과학 분야(물리, 화학, 생물, 재료)의 통합 환경 구축, (2) 다층 평가 세트(L1~L3) 설계, (3) 도구 의존성 그래프 기반 학습 데이터 합성

## Achievement

![Figure 2](https://arxiv.org/abs/2602.12984)

*Figure 2: SciAgentGym 개요. 좌측은 다학제 멀티모달 작업을 처리하는 통합 환경(도구, 파일시스템, 데이터베이스, 인터프리터)을, 우측은 벤치마킹, 에이전트 인터페이스, 학습 방법을 나타냄*

1. **SciAgentGym 환경**: 1,780개 도메인 특화 도구, 안정적 실행 인프라(파일시스템, 데이터베이스, Python 인터프리터)를 갖춘 확장 가능한 인터랙티브 환경 구축
   - 4개 과학 분야, 26개 세부 분야 커버
   - 타입 안전성(Type Safety), 재현성(Reproducibility), 확장성(Extensibility) 설계 원칙 준수

2. **SciAgentBench 벤치마크**: 259개 작업, 1,134개 부분 질문으로 구성된 3단계 평가 세트
   - L1(기초): 507 평균 길이
   - L2(중간): 991 평균 길이  
   - L3(고난도): 1,064 평균 길이
   - GPT-5 기준: 전체 41.3%, 상호작용 증가시 60.6% → 30.9%로 급격한 성능 저하

3. **SciForge 및 SciAgent 모델**: 도구 의존성 그래프 기반 학습 데이터 합성 방법
   - **SciAgent-8B**: Qwen3-VL-235B-Instruct 대비 +6.7% 성능 향상
   - **SciAgent-4B**: +5.5% 성능 향상
   - 도메인 간 양의 전이 학습(positive cross-domain transfer) 확인

## How

![Figure 3](https://arxiv.org/abs/2602.12984)

*Figure 3: t-SNE 시각화로 표현된 도구 임베딩의 의미적 다양성*

### 환경 설계

- **환경 형식화**: E = (S, A, T, O)로 정의
  - **상태 S**: 읽기 전용 파일시스템(문제 맥락, 중간 산출물, 실행 이력)
  - **행동 A**: 1,780개 도구 + execute_code + query_database
  - **전이 함수 T**: 도구 실행 및 환경 상태 업데이트
  - **관찰 O**: 실행 상태, 타입화된 출력, 오류 진단

- **도구 설계**: 
  - 함수 시그니처: v: (α₁ᵛ, ..., αₖᵥᵛ) → (β₁ᵛ, ..., βₘᵥᵛ)
  - 과학 타입 시스템(Float, Int, Vector3D, Matrix, SMILES, Protein Structure)
  - RDKit, ASE, SciPy, BioPython, PyMatGen 등 기존 패키지 캡슐화
  - 4단계 구축: 데이터셋 분석 → 패키지 캡슐화 → 카테고리/그래뉼래리티 조직 → 자동화 단위 테스트(≥75% 통과율)

### 평가 방법론

- **폐쇄 루프 인터랙션**:
  - 도구 레지스트리 쿼리(전체/선택적 도구 로딩)
  - 실행 후 피드백 수신
  - 오류 진단 및 복구 경로 제공

- **평가 지표**:
  - **SR(Success Rate)**: 최종 답변 정확도
  - **Correctness**: 도구 호출의 논리적 일관성
  - **SPL(Success Weighted Path Length)**: 효율성 측정
  - 다단계 워크플로우에서의 오류 누적 분석

### SciForge 데이터 합성

- **도구 의존성 그래프**: 도구 간 입출력 호환성을 DAG(방향성 비순환 그래프)로 모델링
- **경로 샘플링**: 유효한 실행 경로를 체계적으로 샘플링
- **궤적 생성**: 검증된 런타임 추적(runtime trace)을 기반으로 질문 생성
- **논리 인식 학습(Logic-aware training)**: 도구 순서의 의존성을 명시적으로 인코딩

## Originality

- **환경의 규모와 다양성**: 1,780개 도구 × 4개 과학 분야 × 멀티모달 능력(이미지, 구조화 데이터)을 통합한 최초의 대규모 과학 도구 벤치마크
- **인터랙티브 평가 패러다임**: 정적 질답 대신 폐쇄 루프 피드백을 통한 에이전트 행동 평가 (기존 과학 벤치마크는 ScienceQA, GPQA 등 정적 형식)
- **도구 의존성 그래프 기반 학습**: 도구 액션 공간을 구조화하여 "논리적 의존성 학습"이라는 새로운 패러다임 제시
- **효율적 스케일링**: 8B 모델이 235B+ 모델을 능가하는 초효율적 성능 달성 (모델 크기 대비 능력의 재분배)

## Limitation & Further Study

- **제한사항**:
  1. 도구 오류 복구 메커니즘의 복잡성: 현재 모델들이 오류 진단 후 전략 조정에 어려움을 겪으며, 특히 중간 단계의 오류가 누적되는 문제 존재
  2. 도메인 간 전이 학습의 효과가 증명되었지만, 완전히 새로운 과학 분야로의 일반화 가능성 미검증
  3. 도구 조합의 폭증(combinatorial explosion): 1,780개 도구의 조합으로 인한 탐색 공간의 기하급수적 증가
  4. 멀티모달 데이터의 평가 복잡성: 이미지, 구조 데이터 등 다양한 형식의 출력 검증 방법 표준화 필요

- **후속 연구 방향**:
  1. 더 강력한 오류 복구 메커니즘 개발 (과학적 도메인 지식 통합)
  2. 도구 검색 최적화(Tool retrieval refinement) - 관련성 높은 도구 사전 필터링
  3. 강화학습(RL) 기반 정책 학습으로 도구 선택 및 시퀀싱 개선
  4. 실제 과학 논문의 실험 워크플로우를 작업으로 추가하여 현실성 강화

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - 대규모 다학제 도구 환경과 논리적 의존성 학습 방법이 혁신적이나, 인터랙티브 벤치마킹 개념 자체는 기존 연구(AgentGym, MedAgentGym)에서 부분적 선행

- **Technical Soundness (기술적 타당성)**: 4.3/5
  - 환경 설계와 평가 방법론이 견고하고 재현성을 잘 갖춤
  - 다만 도구 의존성 그래프의 자동 구성 과정이 상세히 기술되지 않았으며, 일부 평가 지표의 정의가 모호함

- **Significance (중요도)**: 4.6/5
  - 과학 에이전트 개발의 중요한 표준 벤치마크 제공
  - 8B 모델이 235B 모델을 능가하는 결과는 효율적 과학 AI 개발의 가능성 제시
  - 산업/학계에서 활용 가능성이 높음

- **Clarity (명확성)**: 4.2/5
  - 전체 구조와 동기부여는 명확하나, SciForge의 데이터 합성 알고리즘이 수식 없이 텍스트로만 설명되어 기술적 세부사항 파악이 어려움
  - Figure 2의 우측 Training 파이프라인 부분이 추상적으로 표현됨

- **Overall: 4.4/5**

**총평**: 본 논문은 과학 AI 에이전트의 다단계 도구 사용 능력을 평가하는 최초의 포괄적 벤치마크를 제시하며, 도구 의존성 기반 학습을 통해 모델 효율성과 성능의 새로운 패러다임을 제시합니다. 규모와 실용성에서 탁월하지만, 기술적 세부사항의 완전성과 명확한 기여의 경계 구분에서는 개선의 여지가 있습니다.

## Related Papers

- 🔄 다른 접근: [[papers/429_Infiagent-dabench_Evaluating_agents_on_data_analysis_tasks/review]] — 데이터 분석 작업에서 에이전트 평가를 위한 다른 벤치마크로, 단일 작업 평가와 다중 단계 도구 사용 평가를 비교
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 머신러닝 에이전트 벤치마크로, 과학적 도구 사용을 머신러닝 실험 전반으로 확장하는 평가 프레임워크
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 언어 모델이 도구 사용을 스스로 학습하는 방법에 대한 연구로, 다단계 과학적 도구 사용의 이론적 기반
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 도구를 활용한 LLM에 대한 포괄적 조사로, 과학적 도구 사용 벤치마킹의 기초 이론을 제공
- 🔄 다른 접근: [[papers/556_MolQuest_A_Benchmark_for_Agentic_Evaluation_of_Abductive_Rea/review]] — 화학 구조 해석 대신 다단계 과학 도구 사용을 벤치마킹한다
- 🏛 기반 연구: [[papers/261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear/review]] — 다단계 과학 도구 사용 벤치마크가 깊이 있는 연구 에이전트의 복합적 연구 과제 수행 능력 평가의 기반을 제공한다.
- 🏛 기반 연구: [[papers/147_Aviary_training_language_agents_on_challenging_scientific_ta/review]] — SciAgentGym의 과학 도구 사용 벤치마크가 Aviary의 과학적 언어 에이전트 훈련을 위한 평가 기반을 제공한다
- 🧪 응용 사례: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — 의료 QA 성능을 실제 과학 도구 사용 벤치마크에서 평가할 수 있는 테스트 환경을 제공한다.
