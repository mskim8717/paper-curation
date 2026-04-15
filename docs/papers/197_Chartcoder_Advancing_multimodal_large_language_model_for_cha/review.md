---
title: "197_Chartcoder_Advancing_multimodal_large_language_model_for_cha"
authors:
  - "Xuanle Zhao"
  - "Xianzhen Luo"
  - "Qi Shi"
  - "Chi Chen"
  - "Shuo Wang"
date: "2025"
doi: "arXiv:2501.06598v3"
arxiv: ""
score: 4.2
essence: "본 논문은 차트 이미지를 코드로 변환하는 전문화된 멀티모달 대형언어모델(MLLM)인 ChartCoder를 제안하며, 이를 위해 대규모 차트-코드 데이터셋(Chart2Code-160k)과 단계적 생각(Snippet-of-Thought, SoT) 방법론을 소개한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Code_Generation_Multimodal_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhao et al._2025_Chartcoder Advancing multimodal large language model for chart-to-code generation.pdf"
---

# Chartcoder: Advancing multimodal large language model for chart-to-code generation

> **저자**: Xuanle Zhao, Xianzhen Luo, Qi Shi, Chi Chen, Shuo Wang, Zhiyuan Liu, Maosong Sun | **날짜**: 2025 | **DOI**: [arXiv:2501.06598v3](https://arxiv.org/abs/2501.06598)

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: 기존 MLLM과 ChartCoder의 성능 비교. 차트-코드 생성 작업에서 기존 오픈소스 MLLM은 차트 타입 불일치와 크기 오류를 범하지만, ChartCoder는 정확한 코드를 생성한다.*

본 논문은 차트 이미지를 코드로 변환하는 전문화된 멀티모달 대형언어모델(MLLM)인 ChartCoder를 제안하며, 이를 위해 대규모 차트-코드 데이터셋(Chart2Code-160k)과 단계적 생각(Snippet-of-Thought, SoT) 방법론을 소개한다.

## Motivation

- **Known**: 기존 MLLM들은 차트 이해 작업에서 우수한 성능을 보이지만, 주로 자연어 설명 생성에 초점을 맞추고 있다.

- **Gap**: (1) 차트의 밀집된 정보를 자연어로 표현하면 정보손실이 발생하고, (2) 기존 오픈소스 MLLM은 차트-코드 생성에서 낮은 실행 가능성(executability)과 세부 정보 복원 실패, (3) 차트-코드 학습 데이터의 부족이라는 근본적인 문제가 있다.

- **Why**: 코드는 차트의 손실 없는(lossless) 표현이므로, 모든 중요 정보(데이터, 구조, 스타일)를 정확히 포착할 수 있다. 따라서 차트-코드 생성은 더욱 효율적이고 포괄적인 차트 이해 방식이다.

- **Approach**: (1) Code LLM을 언어 백본으로 활용하여 코드 생성에 최적화된 MLLM 구축, (2) 대규모 다양한 차트-코드 데이터셋 자동 생성, (3) 핵심 정보를 강조하는 단계적 생성 방법론 도입

## Achievement

![Figure 2](figures/fig2.webp) *Figure 2: Chart2Code 데이터셋 생성 과정과 ChartCoder의 2단계 학습 프로세스. 단계1은 차트/이미지-텍스트 정렬, 단계2는 차트-코드 지시사항 튜닝.*

1. **모델 성능**: 7B 파라미터만 사용하면서 기존 모든 오픈소스 MLLM을 차트-코드 벤치마크에서 능가하는 우수한 차트 복원 능력과 코드 실행 가능성 달성

2. **데이터셋 구축**: 27가지 차트 타입에 걸친 160,000개의 고품질 차트-코드 쌍으로 구성된 첫 대규모 차트-코드 데이터셋(Chart2Code-160k) 제공

3. **방법론 효과성**: Snippet-of-Thought(SoT) 방법으로 모델의 추론 능력과 세부 정보 포착 능력 향상 입증

## How

![Figure 2](figures/fig2.webp) *ChartCoder의 2단계 학습 구조와 데이터셋 생성 파이프라인*

### Dataset 생성 (Chart2Code-160k)

- **Step 1**: LLM을 이용하여 특정 도메인 내 키워드 생성 및 관련 시뮬레이션 데이터 생성
- **Step 2**: 27개 차트 타입별로 79개의 템플릿 코드를 수동 작성하여 인컨텍스트 시연(in-context demonstration) 제공
- **Step 3**: 표준 라이브러리(Matplotlib, Seaborn) 사용 권장 및 외부 파일 제거로 직접 실행 가능한 코드 확보
- **Step 4**: 생성된 코드 실행 후 불량 차트 필터링으로 200k에서 160k의 고품질 쌍 확보

### Snippet-of-Thought (SoT) 방법

- Chart2Code-160k에서 50k 쌍을 샘플링하여 직접 생성을 3단계 단계적 생성으로 확대
- 각 단계에서 차트 타입, 데이터 값, 스타일 등 핵심 정보를 명시적으로 강조
- Chain-of-Thought(CoT) 원리를 적용하여 모델의 추론 과정을 개선

### 모델 아키텍처 (ChartCoder)

- **Visual Encoder**: 384×384 해상도로 차트 이미지 인코딩 (고해상도 입력도 처리 가능)
- **Vision-Language Connector**: 시각 정보와 언어 모달리티 간 연결
- **Code LLM Backbone**: 일반 MLLM 대신 코드 생성에 특화된 LLM 사용
- **2-Stage Training**: 
  - Stage 1 (차트-텍스트 정렬): 시각 인코더와 커넥터 워밍업
  - Stage 2 (차트-코드 지시사항 튜닝): 직접 및 단계적 생성 모두 학습

## Originality

- **첫 전문화 모델**: 차트-코드 생성에 특화된 첫 번째 MLLM으로, Code LLM을 언어 백본으로 활용하는 새로운 접근법 제시

- **대규모 데이터셋**: 기존 차트-코드 벤치마크(ChartX 6k, Plot2Code 132, ChartMimic 2.4k)와 비교하여 160배 규모의 Chart2Code-160k 구축

- **혁신적 데이터 생성 파이프라인**: LLM 기반의 역생성(reverse generation) 방식으로 비용 효율적으로 대규모 차트-코드 쌍 자동 생성

- **Snippet-of-Thought 방법론**: CoT를 차트-코드 도메인에 적응시켜 단계적 생성으로 핵심 정보 강조 및 추론 능력 개선

- **포괄적 벤치마크 평가**: ChartMimic, ChartX, Plot2Code 등 다양한 기존 벤치마크에서 체계적 성능 비교

## Limitation & Further Study

- **데이터셋 생성의 한계**: 자동 생성 코드가 일부 템플릿을 따르는 경향이 있어 실제 사용자 코드의 다양성을 완전히 반영하지 못할 수 있음

- **차트 타입 제한**: 27가지 차트 타입으로 제한되어 있으며, 매우 복잡하거나 특수한 차트 타입에 대한 확장성 미흡

- **코드 스타일 다양성**: 파라미터 명시화로 인해 생성된 코드의 스타일이 동일화될 수 있는 문제

- **후속 연구 방향**:
  - 실제 사용자 작성 코드를 포함한 혼합 데이터셋 구축
  - 더 광범위한 차트 타입과 비표준 시각화로 확장
  - 다언어(non-English) 차트 및 코드 생성 지원
  - 대화형 차트 수정 및 개선 시스템 개발


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: ChartCoder는 차트-코드 생성이라는 미개척 영역을 개척하면서 Code LLM 백본과 대규모 데이터셋, SoT 방법론을 통해 실제 성능 개선을 달성한 의미 있는 연구이다. 다만 방법론의 이론적 깊이와 응용 범위 확대에서 추가 개선의 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트-to-코드 생성에서 이중 모드 보상 메커니즘을 사용하는 접근법으로, ChartCoder의 전문화된 모델 접근과 대비되는 보상 학습 기반 방법을 제시한다
- 🏛 기반 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 차트 이해를 위한 포괄적 벤치마크와 기초 모델로, ChartCoder의 차트-to-코드 전문화에 필요한 기본적 차트 이해 능력 평가 기준을 제공한다
- ⚖️ 반론/비판: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — 언어모델에서 차트를 합성하는 역방향 작업으로, ChartCoder의 차트에서 코드로의 변환과 정반대 방향의 연구 접근을 보여준다
- 🔄 다른 접근: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — ChartCoder는 차트-to-코드 변환에 특화된 전용 모델로, 이 논문의 이중 모드 보상 메커니즘과 다른 접근법을 제시한다
- 🔗 후속 연구: [[papers/198_ChartGemma_Visual_Instruction-tuning_for_Chart_Reasoning_in/review]] — 차트 코딩 생성까지 확장한 멀티모달 차트 이해 모델로, 차트 추론을 넘어선 활용 가능성을 보여줍니다.
- 🔗 후속 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — ChartCoder는 ChartX의 차트 이해 평가를 차트-to-코드 생성이라는 구체적 응용 작업으로 발전시킨 연구 방향이다
