---
title: "315_Enhancing_chart-to-code_generation_in_multimodal_large_langu"
authors:
  - "Zhihan Zhang"
  - "Yixin Cao"
  - "Lizi Liao"
date: "2025"
doi: "10.1145/3746027.3755596"
arxiv: ""
score: 4.25
essence: "차트 이미지를 실행 가능한 플로팅 코드로 변환하는 차트-to-코드 생성 작업에서, 다중모달 대규모 언어 모델(MLLM)의 성능을 향상시키기 위해 이중 모드(code + image) 보상 메커니즘과 반복적 선호도 학습을 결합한 프레임워크를 제시한다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zia et al._2025_Enhancing chart-to-code generation in multimodal large language models via iterative dual preference.pdf"
---

# Enhancing chart-to-code generation in multimodal large language models via iterative dual preference learning

> **저자**: Zhihan Zhang, Yixin Cao, Lizi Liao | **날짜**: 2025 | **DOI**: [10.1145/3746027.3755596](https://doi.org/10.1145/3746027.3755596)

---

## Essence

![Figure 1](figures/fig1.webp)
*차트-to-코드 생성 작업의 예시로, 실행 가능성(Executability), 시각적 충실도(Visual Fidelity), 속성 정확도(Attributes Correctness) 등 다중 차원으로 평가됨*

차트 이미지를 실행 가능한 플로팅 코드로 변환하는 차트-to-코드 생성 작업에서, 다중모달 대규모 언어 모델(MLLM)의 성능을 향상시키기 위해 이중 모드(code + image) 보상 메커니즘과 반복적 선호도 학습을 결합한 프레임워크를 제시한다.

## Motivation

- **Known**: 최근 MLLM들이 차트 질의응답(chart QA)이나 차트-to-텍스트 생성에서 우수한 성능을 보이고 있으나, 세밀한 시각 구조 이해가 필요한 차트-to-코드 생성 작업에서는 부정확하거나 실행 불가능한 코드를 생성하는 경향을 보임

- **Gap**: 차트-to-코드 생성은 본질적으로 제약이 부족한(under-constrained) 작업임. 같은 차트를 여러 코드로 표현 가능하며, 코드 정확성과 시각적 충실도를 동시에 평가해야 함. 표준 감독 학습(SFT)은 단일 참조값과의 정확한 일치만 평가하므로 이러한 다양성을 제대로 포착하지 못함

- **Why**: 차트는 색상, 텍스트, 레이아웃, 스타일, 데이터 등 복합적인 시각 요소의 조합으로 구성되며, 모델은 이러한 다중 차원을 모두 정확하게 캡처해야 함

- **Approach**: 코드와 이미지 양쪽 모드에서 보상 신호를 제공하고, 오프라인 강화학습(RL) 패러다임을 활용하여 반복적으로 모델을 정제하는 이중 선호도 유도 정제(dual preference-guided refinement) 프레임워크 제안

## Achievement

![Figure 2](figures/fig2.webp)
*Chart2Code의 개요: 휴리스틱 F1 기반 코드 점수 매기기와 시각 보상 모델을 포함한 이중 보상 메커니즘, 그리고 구조화된 변형 생성 전략과 종횡별(aspect-level) 피드백 데이터셋*

1. **성과1 - 다중 MLLM에서의 일관된 성능 향상**: 세 개의 기본 MLLM과 두 개의 벤치마크에서 실험하여 프레임워크가 다양한 초기화 설정에서도 실질적인 성능 개선을 달성함을 입증

2. **성과2 - 전문화된 모델과의 경쟁력**: 범용 오픈소스 MLLM들을 차트 전문 모델 및 일부 독점 시스템 수준으로 향상시켜, 고품질의 시각적으로 충실한 플로팅 코드 생성 능력을 확보

3. **성과3 - 스케일 가능하고 타겟팅된 감독**: 구조화된 변형 생성 전략과 시각 보상 모델을 통해 고품질의 종횡별 선호도 쌍 생성을 효율적으로 수행 가능하게 함

## How

![Figure 3](figures/fig3.webp)
*각 반복 단계에서 생성되는 보상 신호의 흐름*

**1. 이중 보상 메커니즘 (Dual Rewarding Mechanism)**
- **코드 측 평가**: 휴리스틱 F1 기반 점수 매기기로 생성 코드의 구조적 완정성과 의미론적 정확성 평가
  - 차트 타입(Type), 데이터(Data), 색상(Color), 텍스트(Text), 레이아웃(Layout), 스타일(Style) 등 6개 종횡에 대해 개별 F1 점수 계산
  
- **이미지 측 평가**: 시각 보상 모델(visual reward model)을 통해 렌더링된 차트의 시각적 충실도 평가
  - 종횡별 피드백 데이터셋으로 훈련된 시각 보상 모델이 레이아웃, 스타일, 지각적 속성 보존 정도 측정

**2. 구조화된 변형 생성 전략 (Structured Variant Generation)**
- 금표준 코드로부터 제어된 편차를 가진 합성 코드 샘플 생성
  - 종횡별 규칙 기반 변형: Shuffling(색상 재정렬), Removing(텍스트 제거), Changing(스타일 변경) 등
  - 다양한 재현 수준에 걸친 선호도 쌍 생성

**3. 반복적 선호도 학습 (Iterative Preference Learning)**
- Direct Preference Optimization (DPO) 목표함수 활용
  - 모델 생성 코드 vs 합성 변형 코드 간 선호도 쌍 구성
  - 각 반복 종료 후 새로운 참조 차트 배치에 대해 모델 평가하여 다음 반복 진행
  - 이중 피드백 기반 최적화로 지속적 정제

**4. 종횡별 피드백 데이터셋 구성**
- 각 생성 결과에 대해 종횡별 설명과 점수 제공
- 시각 보상 모델 훈련의 감독 신호로 사용

## Originality

- **MLLM에서의 오프라인 RL 최초 적용**: 차트-to-코드 생성 작업에 오프라인 선호도 최적화 패러다임을 처음으로 도입

- **이중 모드 보상 메커니즘의 설계**: 코드 정확성(executable quality)과 시각적 충실도(visual fidelity)를 동시에 평가하는 이중 보상 체계로, 작업의 본질적 이중성을 직접 반영

- **구조화된 합성 변형 생성**: 단순한 모델 샘플링이 아닌, 종횡별 규칙 기반의 제어된 변형을 통해 선호도 쌍의 질을 향상시키고 재현성 확보

- **종횡별 피드백 데이터셋 구축**: 시각 보상 모델 훈련을 위한 세밀한 피드백 데이터셋을 체계적으로 구성하여 해석 가능하고 정확한 이미지 측 평가 가능하게 함

## Limitation & Further Study

- **종횡별 규칙의 한계**: 구조화된 변형 생성이 사전 정의된 규칙에 의존하므로, 예상치 못한 차트 특성이나 복잡한 상호작용에 대한 대응이 제한될 수 있음

- **보상 모델의 일반화성**: 시각 보상 모델이 특정 차트 도메인이나 플로팅 라이브러리(matplotlib 중심)에 편향될 가능성

- **계산 비용**: 각 반복마다 새로운 배치를 생성하고 평가해야 하므로, 매우 대규모 데이터셋에서의 확장성이 미검증됨

- **후속 연구 방향**:
  - 적응형 변형 생성 전략으로 규칙 기반 접근의 경직성 완화
  - 다양한 시각화 도메인(Plotly, ggplot 등)으로의 프레임워크 확장
  - 인간 피드백과 자동 평가의 혼합을 통한 보상 신호 정제
  - 더 효율적인 선호도 쌍 구성 방법 탐색

## Evaluation

- **Novelty**: 4.5/5 - 차트-to-코드 생성에 오프라인 RL 적용이 새로우며, 이중 모드 보상 메커니즘과 종횡별 피드백의 조합이 창의적이나, 개별 컴포넌트(DPO, 보상 모델링)는 기존 기법의 응용

- **Technical Soundness**: 4/5 - 방법론이 견고하며 실험 설계가 체계적이나, 보상 함수의 설계(특히 코드 F1 계산)가 일부 휴리스틱 요소를 포함하고, 통계적 유의성 검증이 명확하지 않음

- **Significance**: 4.5/5 - 범용 MLLM을 전문화된 모델 수준으로 향상시키는 실질적 가치가 있으며, 공개 코드와 데이터셋 제공으로 재현성과 활용 가능성이 높음

- **Clarity**: 4/5 - 전반적으로 명확한 설명과 상세한 그림으로 방법론을 잘 설명하나, 변형 생성 규칙의 정확한 정의와 일부 하이퍼파라미터 설정에 대한 상세 기술이 부족함

- **Overall**: 4.25/5

**총평**: 차트-to-코드 생성의 본질적 이중성(코드 정확성 + 시각적 충실도)을 직접 반영한 이중 보상 메커니즘과 반복적 선호도 학습의 결합이 효과적이며, 범용 MLLM의 실질적 향상을 달성한 점이 주목할 만함. 다만 보상 함수의 휴리스틱 성격과 도메인 확장성에 대한 추가 검증이 필요함.

## Related Papers

- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — ChartCoder는 차트-to-코드 변환에 특화된 전용 모델로, 이 논문의 이중 모드 보상 메커니즘과 다른 접근법을 제시한다
- 🏛 기반 연구: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — MMC 데이터셋의 대규모 차트 이해 데이터는 차트-to-코드 생성 모델 훈련에 필요한 기초 자원을 제공한다
- ⚖️ 반론/비판: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — SynChart는 언어모델에서 차트를 생성하는 역방향 작업으로, 차트에서 코드로 변환하는 이 논문과 상반된 관점을 보여준다
- 🔄 다른 접근: [[papers/841_Tree-of-table_Unleashing_the_power_of_llms_for_enhanced_larg/review]] — 대규모 테이블 처리에서 계층적 트리 구조 접근법과 차트-코드 생성 방식은 구조화된 데이터 이해의 서로 다른 전략이다.
- 🏛 기반 연구: [[papers/203_Chartsketcher_Reasoning_with_multimodal_feedback_and_reflect/review]] — 멀티모달 차트 이해의 기반이 되는 코드 생성과 LLM 활용 방법론에 대한 기본적 이해를 제공한다
- 🏛 기반 연구: [[papers/807_Theoremexplainagent_Towards_video-based_multimodal_explanati/review]] — 차트-코드 생성의 멀티모달 대형 언어모델 연구가 비디오 기반 정리 설명의 기술적 기반을 제공한다.
- 🧪 응용 사례: [[papers/551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal/review]] — 차트에서 코드 생성으로 확장한 연구로, 멀티모달 차트 이해를 실제 프로그래밍 작업에 적용한 발전된 사례입니다.
- 🔄 다른 접근: [[papers/197_Chartcoder_Advancing_multimodal_large_language_model_for_cha/review]] — 차트-to-코드 생성에서 이중 모드 보상 메커니즘을 사용하는 접근법으로, ChartCoder의 전문화된 모델 접근과 대비되는 보상 학습 기반 방법을 제시한다
- 🔄 다른 접근: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 차트-to-코드 생성에서 이중 모드 보상 학습을 사용하는 접근법으로, ChartVLM의 기초 모델 중심 접근과 다른 훈련 방법론을 제시한다
