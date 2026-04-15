---
title: "746_Self-Refine_Iterative_Refinement_with_Self-Feedback"
authors:
  - "Aman Madaan"
  - "Niket Tandon"
  - "Prakhar Gupta"
  - "Skyler Hallinan"
  - "Luyu Gao 외"
date: "2023"
doi: "10.48550/arXiv.2303.17651"
arxiv: ""
score: 4.3
essence: "대규모 언어 모델(LLM)이 자신의 출력에 대해 피드백을 제공하고 이를 바탕으로 자동으로 개선하는 반복적 자기 정제 방식을 제시한다. 추가 훈련이나 외부 보상 모델 없이 단일 LLM만으로 약 20% 절대 성능 향상을 달성한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Human-LLM_Review_Semantics"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Madaan et al._2023_Self-Refine Iterative Refinement with Self-Feedback.pdf"
---

# Self-Refine: Iterative Refinement with Self-Feedback

> **저자**: Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao 외 | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2303.17651](https://doi.org/10.48550/arXiv.2303.17651)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: SELF-REFINE의 기본 작동 원리. 동일한 모델 M이 초기 생성, 피드백 제공, 개선을 반복적으로 수행*

대규모 언어 모델(LLM)이 자신의 출력에 대해 피드백을 제공하고 이를 바탕으로 자동으로 개선하는 반복적 자기 정제 방식을 제시한다. 추가 훈련이나 외부 보상 모델 없이 단일 LLM만으로 약 20% 절대 성능 향상을 달성한다.

## Motivation

- **Known**: LLM은 초기 생성에서 최적의 출력을 항상 만들지 못하며, 기존 개선 방법은 도메인 특정 데이터나 비용이 큰 인간 주석이 필요함
- **Gap**: 감독(supervision) 없이도 LLM 스스로 자신의 출력을 반복적으로 개선할 수 있는 일반적 방법 부재
- **Why**: 인간은 작문 또는 코딩 시 초안을 작성한 후 자체 피드백 기반으로 반복 정제하는 방식으로 문제를 해결함. 이 인간 행동을 LLM에 적용 가능
- **Approach**: 단일 LLM을 생성기, 피드백 제공자, 정제기로 활용하는 자기 반복 정제 프레임워크 개발

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: SELF-REFINE의 실제 예시. 대화 생성(상단)과 코드 최적화(하단) 작업에서의 초기 출력과 피드백, 개선된 출력*

1. **광범위한 성능 향상**: 7가지 다양한 작업에서 GPT-3.5, ChatGPT, GPT-4 등 강력한 기본 LLM에 비해 평균 20% 절대 성능 향상을 달성. 특정 작업(예: 감정 반전, 대화 응답)에서는 30-50% 이상 향상

2. **일반성과 확장성**: 대화 생성, 코드 최적화, 수학 추론, 제약 조건 생성 등 의미론적으로 다른 작업 전반에서 일관되게 개선. 훈련이나 미세 조정 없이 다양한 LLM에 직접 적용 가능

3. **상태-최신 모델 개선**: GPT-4와 같은 이미 고성능인 모델도 테스트 시점에서 추가 개선 가능함을 입증

## How

![Figure 3](figures/fig3.webp)
*Figure 3: SELF-REFINE 알고리즘 구조. 피드백과 정제 단계를 반복하는 의사코드*

- **초기 생성 단계**: 입력 x에 대해 모델 M이 초기 출력 y₀ 생성 (few-shot 프롬프트 활용)

- **피드백 단계**: 동일 모델 M에 입력과 초기 출력을 함께 전달하여 구체적이고 실행 가능한 피드백(actionable feedback) 생성. 피드백은 개선할 구체적 문구와 개선 방법을 명시

- **정제 단계**: 피드백과 함께 이전 출력들의 이력을 모델에 전달하여 개선된 출력 y_{t+1} 생성. 이전 반복들의 오류를 학습할 수 있도록 전체 대화 이력 유지

- **반복 종료**: 사전 정의된 최대 반복 횟수(4회) 도달 또는 모델이 생성한 종료 신호(stop score)로 반복 중단

- **Few-shot 프롬프팅**: 모든 단계(생성, 피드백, 정제)에서 입출력 예제를 포함한 맥락 내 학습(in-context learning) 활용

## Originality

- **새로운 관점**: LLM이 자신의 피드백을 기반으로 반복적으로 자신을 정제할 수 있다는 통찰력. 외부 감독이나 추가 훈련 없이 순수 프롬프팅만으로 구현

- **일반적 프레임워크**: 특정 작업에 종속되지 않은 범용적 접근법으로, 다양한 생성 작업에 적용 가능. 도메인별 특화 데이터 불필요

- **실용성**: 기존 API 기반 LLM(GPT-3.5, GPT-4)에 즉시 적용 가능한 배포 용이한 방법. 코드와 데이터를 오픈소스로 공개하여 재현성 보장

- **광범위한 평가**: 자동 메트릭(pass rate, coverage)과 인간 평가를 결합한 엄밀한 검증 체계. 7개 작업, 3-4개 모델에 걸친 종합적 실험

## Limitation & Further Study

- **반복 비용**: 각 정제 단계마다 모델 추론이 필요하므로 계산 비용과 지연이 증가. 실제 배포 시 4회 반복 시 초기 생성 대비 4배 API 호출 필요

- **피드백 품질 의존성**: 모델이 생성하는 피드백의 품질이 최종 결과를 크게 좌우하는데, 이에 대한 정량적 분석 부재. 나쁜 피드백이 개선을 방해할 가능성

- **수학 추론 작업의 한계**: Math Reasoning 작업에서 거의 개선 없음(0-0.2%). 이미 높은 성능이거나 피드백이 도움되지 않는 경우에 대한 심화 분석 필요

- **최적 반복 횟수 미결정**: 최대 4회 반복이 모든 작업에 최적인지 불명확. 작업별 최적 반복 횟수와 종료 조건의 자동 결정 방법 연구 필요

- **프롬프트 의존성**: Few-shot 프롬프트의 품질과 예제 선택이 성능에 영향을 미칠 가능성 높음. 프롬프트 설계의 일반화 전략 부족

- **후속 연구 방향**: 
  - 강화 학습과의 결합으로 피드백 생성 정책 최적화
  - 작업별 최적 반복 횟수의 동적 결정 메커니즘
  - 계산 비용 감소를 위한 경량화 방법 연구
  - 피드백 품질 평가 메트릭 개발

## Evaluation

- **Novelty**: 4.5/5
  - 자기 피드백 기반 반복 정제라는 신선한 개념이지만, 프롬프팅 기반 방법론으로서 본질적 기술 혁신은 제한적

- **Technical Soundness**: 4/5
  - 방법론이 명확하고 구현이 직관적이나, 반복 종료 조건, 피드백 품질 평가, 역수렴(negative feedback) 처리 등에 대한 기술적 깊이 부족

- **Significance**: 4.5/5
  - 대규모 모델 사용자 관점에서 즉시 실용적인 성과이며, 7개 작업에서 일관된 개선으로 일반성 입증. 다만 수학 추론 등 일부 작업에서 제한적 효과

- **Clarity**: 4.5/5
  - 논문 구조와 설명이 명확하고 다양한 예시 제공. 알고리즘 명시적 제시 우수. 다만 일부 기술 세부사항(프롬프트 예제 수, 모델 선택 기준)은 부족

- **Overall**: 4.3/5

**총평**: 이 논문은 거대 언어 모델이 자신의 피드백을 통해 반복적으로 스스로를 개선할 수 있다는 간단하면서도 효과적인 아이디어를 제시한다. 추가 훈련 없이 기존 LLM에 즉시 적용 가능하면서도 평균 20% 성능 향상을 달성하여 실무적 가치가 높으나, 계산 비용 증가, 피드백 품질 의존성, 일부 작업에서의 제한된 효과 등이 개선과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — SelfCheck의 단계별 추론 검증과 유사하지만 더 포괄적인 출력 개선을 위한 반복적 자기 정제 방법론을 제시한다.
- 🔗 후속 연구: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 자기 디버깅 방법론을 일반적인 출력 개선으로 확장하여 외부 도구 없이 LLM만으로 성능 향상을 달성한다.
- 🏛 기반 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구 통합 자기 수정 연구가 외부 도구 없는 순수 LLM 기반 자기 정제의 이론적 기반을 제공한다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 자기 개선 능력에 대한 상반된 관점을 제시하여 한계와 가능성을 균형있게 이해할 수 있다.
- 🏛 기반 연구: [[papers/887_Wrong-of-thought_An_integrated_reasoning_framework_with_mult/review]] — 자기 피드백을 통한 반복 개선의 일반적 원리는 다중 관점 검증과 오류 정보 활용 추론 프레임워크의 기반이다.
- 🔗 후속 연구: [[papers/182_Can_language_models_falsify_evaluating_algorithmic_reasoning/review]] — 자기 피드백을 통한 반복적 개선 방법론이 언어모델의 반례 생성 능력 향상 방향을 제시한다
- 🏛 기반 연구: [[papers/723_Sciglm_Training_scientific_language_models_with_self-reflect/review]] — 자기 피드백을 통한 반복적 개선의 기초 방법론을 과학 언어 모델 훈련에 적용한다.
- 🔄 다른 접근: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — Self-Refine의 반복적 자기 개선 방식과 유사하지만 단계별 추론의 오류 검증에 특화된 접근법을 제시한다.
- 🔗 후속 연구: [[papers/470_Large_language_models_can_self-improve/review]] — Self-Refine은 자기 피드백을 통한 반복적 개선 방법으로, 이 논문의 자기 개선 개념을 더 구체적인 프레임워크로 발전시켰다
- 🏛 기반 연구: [[papers/314_Enabling_language_models_to_implicitly_learn_self-improvemen/review]] — 자기 피드백을 통한 반복적 개선의 기본 프레임워크로, PIT의 암묵적 자기 개선 학습에 필요한 기초적 자기 개선 메커니즘을 제공한다
- 🔗 후속 연구: [[papers/656_Read_revise_repeat_A_system_demonstration_for_human-in-the-l/review]] — 자기 피드백을 통한 반복적 개선 방법론을 통해 인간 피드백 없이도 텍스트 품질을 향상시킬 수 있는 확장된 접근법을 제시한다.
- 🏛 기반 연구: [[papers/636_Prompt_to_be_consistent_is_better_than_self-consistent_few-s/review]] — 자기 피드백을 통한 반복적 개선의 기초적인 방법론을 일관성 강화에 적용한다.
- 🔄 다른 접근: [[papers/790_Teaching_Large_Language_Models_to_Self-Debug/review]] — 자기 개선이라는 공통 목표를 코드 디버깅 vs 일반적인 자기 개선으로 다르게 접근한다
