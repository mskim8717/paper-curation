---
title: "196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model"
authors:
  - "Fanqing Meng"
  - "Wenqi Shao"
  - "Quanfeng Lu"
  - "Peng Gao"
  - "Kaipeng Zhang"
date: "2024"
doi: "10.48550/arXiv.2401.02384"
arxiv: ""
score: 4.0
essence: "차트-테이블 사전학습(pre-training)과 다중작업 명령어 튜닝(instruction tuning)을 통해 다양한 차트 이해 작업을 단일 모델로 수행할 수 있는 보편적 차트 멀티모달 언어모델을 제안한다. 기존 모델의 차트-텍스트 정렬 부족과 제한된 데이터를 극복하기 위해 39M 규모의 대규모 ChartSFT 데이터셋과 2단계 학습 전략을 도입했다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Code_Generation_Multimodal_Models"
  - "topic/ai4s"
---

# ChartAssisstant: A Universal Chart Multimodal Language Model via Chart-to-Table Pre-training and Multitask Instruction Tuning

> **저자**: Fanqing Meng, Wenqi Shao, Quanfeng Lu, Peng Gao, Kaipeng Zhang | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2401.02384](https://doi.org/10.48550/arXiv.2401.02384)

---

## Essence

차트-테이블 사전학습(pre-training)과 다중작업 명령어 튜닝(instruction tuning)을 통해 다양한 차트 이해 작업을 단일 모델로 수행할 수 있는 보편적 차트 멀티모달 언어모델을 제안한다. 기존 모델의 차트-텍스트 정렬 부족과 제한된 데이터를 극복하기 위해 39M 규모의 대규모 ChartSFT 데이터셋과 2단계 학습 전략을 도입했다.

## Motivation

- **Known**: 차트는 데이터 시각화의 핵심이며, LLaVA 등 일반 목적 멀티모달 모델들도 존재하지만 차트의 복잡한 시각 요소(막대, 선 등), 암시적 수치 정보, 요소 간 공간 관계로 인해 차트 이해에 어려움을 겪음.

- **Gap**: 기존 차트 전문 모델(MatCha, UniChart)들은: (1) 차트와 구조화된 텍스트 테이블 간 정렬 부족, (2) 차트 관련 작업의 제한된 데이터 커버리지, (3) 시각 요소 이해 및 수학 추론 학습용 주석 데이터 부족, (4) 특화된 차트 유형(박스플롯 등) 포함 부족으로 인해 일반화 성능이 낮고 작업별 미세조정이 필요.

- **Why**: 차트 이해는 공간 추론, 수치 이해, 특화된 도메인 지식을 요구하므로 단일 모델이 모든 차트 작업을 효과적으로 수행하려면 충분한 규모의 다양한 데이터와 체계적 학습 전략이 필수.

- **Approach**: (1) 9가지 차트 유형을 포함하는 39M 규모의 ChartSFT 데이터셋 구축, (2) 차트-테이블 번역 사전학습으로 정렬 강화, (3) 5가지 작업(수치 QA, 참조 QA, 개방형 QA, 요약, 차트-테이블 번역)의 다중작업 명령어 튜닝.

## Achievement

![Figure 1](figures/fig1.webp)
*기존 차트 모델과 ChartAssistant의 학습 파이프라인 비교*

1. **성능 향상**: UniChart 대비 수치 QA에서 50.0%, ChartQA에서 28.1% 성능 향상. 영점학습(zero-shot) 설정에서 RealCQA 데이터셋에서 29.5%, ChartLLM에서 23.6% 성능 향상 달성.

2. **데이터셋 규모**: MatCha 대비 4.75배, UniChart 대비 5.62배 큰 39M 규모의 ChartSFT 데이터셋 구축으로 더 나은 일반화 가능성 제공.

3. **모델 다양성**: 경량 모델(ChartAst-D, 260M 파라미터)과 고성능 모델(ChartAst-S, 13B 파라미터) 두 가지 변형 제공으로 다양한 응용 시나리오 지원.

4. **포괄적 차트 커버리지**: 기본 차트(막대, 선, 산점선, 원형)와 특화된 차트(레이더, 박스플롯 등) 포함으로 더 넓은 차트 유형 대응.

## How

![Figure 2](figures/fig2.webp)
*ChartAssistant가 수행하는 다양한 차트 이해 작업들*

**ChartSFT 데이터셋 구성**:
- 기본 차트 유형: 기존 벤치마크(ChartQA, PlotQA, OpenCQA 등) 활용 및 arXiv 테이블에서 데이터 증강
- 특화된 차트: 레이더, 박스플롯 등을 위해 ChatGPT를 이용한 테이블 데이터 합성
- 9가지 차트 유형 × 5가지 작업 조합으로 총 39M 주석 데이터 수집

**2단계 학습 전략**:
- **사전학습 단계**: 차트를 마크다운 테이블로 변환하는 차트-테이블 번역 작업으로 사전학습. 이를 통해 자연 이미지의 이미지 캡셔닝처럼 차트 요소와 관계 해석 능력 및 차트-텍스트 정렬 학습.
- **명령어 튜닝 단계**: ChartSFT로 5가지 작업(차트-테이블 번역, 수치 QA, 참조 QA, 개방형 QA, 요약)에 대해 다중작업 명령어 튜닝 수행.

**모델 아키텍처**:
- **ChartAst-D**: Donut 기반의 경량 OCR-프리 모델로 문서 이해에 최적화
- **ChartAst-S**: SPHINX 기반의 13B 파라미터 모델로 동적 해상도 처리(dynamic resolution)와 복합 시각 인코더(mixed visual encoder) 활용으로 강화된 차트 표현 학습

## Originality

- **대규모 통합 데이터셋**: 기존 벤치마크보다 5배 이상 큰 ChartSFT 데이터셋으로 포괄적 차트 커버리지 달성. 특히 특화된 차트 유형의 합성 데이터 추가가 혁신적.

- **사전학습-튜닝 2단계 전략**: 단순 다중작업 튜닝에서 벗어나 차트-테이블 번역 사전학습으로 명시적 정렬 학습을 도입한 점이 기존과 차별화.

- **메타 작업 설계 개선**: 체인-오브-생각(CoT) 주석으로 수학 추론 향상, 참조 QA 작업으로 시각 요소 관계 이해 강화 등 작업 수준의 창의적 개선.

- **다중 아키텍처 지원**: 경량/고성능 모델 변형으로 다양한 배포 환경 대응 가능하게 설계.

## Limitation & Further Study

- **데이터 소스의 불균형**: 기본 차트는 기존 벤치마크에서 수집하고 특화된 차트는 합성되어 자연 분포와의 차이 가능성.

- **실제 차트 다양성 부족**: arXiv 테이블과 ChatGPT 기반 생성으로 인해 실제 도메인(금융, 의료 등)의 복잡한 차트 표현 미흡 가능.

- **해석 가능성 부족**: 모델이 어떤 시각 요소에 주목하여 답변을 생성하는지에 대한 설명이 제한적. 시각 어텐션(visual attention) 시각화 추가 연구 필요.

- **언어 확장성**: 영어 중심 데이터셋으로 다국어 차트 이해 능력 미검증. 다국어 데이터셋 확장 필요.

- **전문 도메인 차트**: 과학, 의료 등 도메인 특화 차트의 성능 평가 부족. 도메인별 미세조정 전략 개발 필요.

## Evaluation

- **Novelty**: 4/5
  - 대규모 데이터셋과 2단계 학습 전략은 좋은 아이디어이나, 개별 기술 요소는 기존 기법의 조합. 차트-테이블 정렬 아이디어는 상대적으로 자연스러운 확장.

- **Technical Soundness**: 4/5
  - 전반적으로 체계적이고 견고한 설계. 다만 차트-테이블 번역의 사전학습 효과에 대한 절제된 실험(ablation study) 상세 분석 부족. 특화 차트 합성 방법의 타당성 검증 필요.

- **Significance**: 5/5
  - 일반화된 단일 차트 모델 달성으로 실무 응용 가치 높음. 5배 규모의 데이터셋과 강력한 성능 개선은 커뮤니티에 유의미한 기여. 영점학습에서의 우수한 성능은 실제 배포 환경에서 실용적.

- **Clarity**: 4/5
  - 논문 구조와 그림이 명확하고 쉽게 이해 가능. 다만 ChartSFT 데이터 추출 과정의 세부사항(예: 품질 보증, 주석자 간 일관성) 설명 부족.

- **Overall**: 4/5

**총평**: ChartAssistant는 체계적인 데이터셋 구축과 2단계 학습 전략으로 차트 이해 모델의 일반화 성능을 크게 향상시킨 실용적이고 견고한 연구이다. 대규모 데이터셋 구축과 다양한 차트 유형 지원이 주요 강점이나, 개별 기술 혁신 측면에서는 기존 기법의 효과적 조합에 가까우며, 절제된 실험을 통한 각 구성요소의 기여도 상세 분석이 추가되면 더욱 강화될 것으로 판단된다.

## Related Papers

- 🔗 후속 연구: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 범용 차트 멀티모달 언어모델을 작업 기반 안구 움직임 제어로 확장하여 더 인간다운 차트 이해 시스템을 구현한다.
- 🏛 기반 연구: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 차트 멀티모달 언어모델의 텍스트-시각 정렬 기법이 멀티모달 풍자 탐지에서 모달리티 간 정렬 문제 해결의 기반을 제공한다.
- 🔄 다른 접근: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — ChartAssistant의 범용 차트 이해와 MMC의 대규모 차트 데이터셋 기반 접근법이 차트 AI의 서로 다른 발전 방향을 제시한다.
- 🔄 다른 접근: [[papers/199_ChartInstruct_Instruction_Tuning_for_Chart_Comprehension_and/review]] — 범용 차트 언어 모델과 특화된 차트 이해 시스템이 상호 보완적 접근법을 제공한다
- 🔗 후속 연구: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 범용 차트 언어모델의 기능을 인간의 인지 과정을 모방하는 안구 움직임 제어로 확장하여 더 자연스러운 차트 분석을 구현한다.
- 🔄 다른 접근: [[papers/201_ChartLlama_A_Multimodal_LLM_for_Chart_Understanding_and_Gene/review]] — 차트 이해를 위한 멀티모달 LLM을 다른 아키텍처와 접근법으로 구현한 대안적 연구
- 🔄 다른 접근: [[papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/review]] — 차트 이해에서 반복적 스케칭과 범용 어시스턴트라는 서로 다른 접근 전략을 보여준다
- 🧪 응용 사례: [[papers/092_Align_then_Fusion_Generalized_Large-scale_Multi-view_Cluster/review]] — 멀티뷰 클러스터링 기술이 차트의 다양한 시각적 정보를 통합하는 멀티모달 언어모델 개발에 직접 적용될 수 있다.
- 🏛 기반 연구: [[papers/1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst/review]] — 멀티모달 언어모델의 차트-텍스트 정렬 기법이 풍자 탐지에서 텍스트-이미지 정렬 문제 해결의 기반을 제공한다.
