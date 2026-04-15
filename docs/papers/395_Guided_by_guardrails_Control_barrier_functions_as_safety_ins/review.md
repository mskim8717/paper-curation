---
title: "395_Guided_by_guardrails_Control_barrier_functions_as_safety_ins"
authors:
  - "Maeva Guerrier"
  - "Karthik Soma"
  - "Hassan Fouad"
  - "Giovanni Beltrame"
date: "2025"
doi: "arXiv:2505.18858"
arxiv: ""
score: 4.0
essence: "강화학습(RL)의 안전성 문제를 제어 장벽 함수(Control Barrier Functions, CBFs)를 활용하여 해결하는 혁신적 접근법을 제시한다. 세 가지 CBF 통합 방식을 통해 로봇이 안전한 행동을 학습하면서도 목표 달성 성능을 유지하도록 한다."
tags:
  - "cat/Reinforcement_Learning_Control_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Computational_Molecular_Science_Models"
  - "sub/Robust_Robotic_Control"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Taylor and Ames_2025_Guided by guardrails Control barrier functions as safety instructors for robotic learning.pdf"
---

# Guided by guardrails: Control barrier functions as safety instructors for robotic learning

> **저자**: Maeva Guerrier, Karthik Soma, Hassan Fouad, Giovanni Beltrame | **날짜**: 2025 | **DOI**: [arXiv:2505.18858](https://arxiv.org/abs/2505.18858)

---

## Essence

강화학습(RL)의 안전성 문제를 제어 장벽 함수(Control Barrier Functions, CBFs)를 활용하여 해결하는 혁신적 접근법을 제시한다. 세 가지 CBF 통합 방식을 통해 로봇이 안전한 행동을 학습하면서도 목표 달성 성능을 유지하도록 한다.

## Motivation

- **Known**: 강화학습은 로봇 제어에 효과적이지만, 종래의 RL은 안전을 단순한 음의 보상과 에피소드 즉시 종료로 모델링함
- **Gap**: 이러한 방식은 실제 세계의 시간적 피해 축적(예: 지속적인 충돌 손상)을 포착하지 못하며, 탐색 과정에서 에이전트가 위험한 상태에 갇힐 수 있음
- **Why**: 안전성은 학습 기반 로봇 시스템의 실제 적용을 가로막는 핵심 장애물
- **Approach**: CBF의 이론적 안전 보장을 RL 프레임워크에 "가드레일(guardrail)"로 통합하여 안전 제약을 동적으로 강제

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 세 가지 안전 가드레일 변형 - 필터(초록색), 보상 기반(주황색), 감쇠(파란색)*

1. **세 가지 CBF-RL 통합 방식 제안**:
   - **CBF Filter**: 에이전트가 위험 영역에 진입 시 액션을 최소한으로 개입하여 교정
   - **CBF Reward**: CBF 제안 액션으로부터의 편차를 보상 함수에 포함시켜 페널티 부여
   - **CBF Decay**: 커리큘럼 학습 방식으로 훈련 과정에서 CBF의 영향을 점진적으로 제거

2. **실제 적용 가능성 입증**:
   - 단순 유니사이클(unicycle) 모델로 추상화하여 다양한 로봇 동역학에 적용 가능
   - 시뮬레이션에서 훈련한 정책을 4륜 차동 구동 로봇(four-wheel differential drive robot)에 성공적으로 배포
   - 시뮬레이션-현실 이전(sim2real transfer) 성능 평가

## How

![Figure 2](figures/fig2.webp)
*그림 2: 유니사이클 모델의 장애물 회피 CBF 구성 - 로봇 축을 따라 ε만큼 이동한 점 x'를 사용*

**기술적 구현**:

- **CBF 공식화**: 전통적 장애물 회피 CBF h = ||x-x₀||² - δ²의 상대 차수(relative degree) 문제를 해결하기 위해, 로봇 축을 따라 ε만큼 이동한 점 x'를 기준으로 h = ||x'-x₀||² - (δ+ε)² 형태로 개선

- **우선순위 파라미터 κ**: 선형 속도와 각속도 제어의 우선순위를 조정하여 제한된 제어 액션에서도 장애물 회피 가능

- **SAC 기반 통합**: Soft Actor-Critic 알고리즘을 기본으로 하여 세 가지 방식의 CBF 통합 메커니즘 구현

- **환경 설계**: 시작점, 목표, 장애물 위치를 무작위화하고, 에피소드를 종료하지 않으면서 지속적인 음의 보상으로 시간적 피해 효과 모델링

## Originality

- **CBF를 안전 가드레일로 재해석**: 기존의 CBF-RL 통합 방식과 달리, 행동 필터링, 보상 설계, 커리큘럼 학습의 세 가지 구별되는 접근법 제시

- **추상화된 동역학 모델**: 유니사이클 모델을 통해 CBF의 복잡한 설계를 단순화하면서도 다양한 로봇 플랫폼에의 일반화 가능성 증대

- **현실적 안전 모델링**: 기존의 즉시 에피소드 종료 방식을 지양하고, 지속적인 음의 보상으로 실제 피해 축적을 반영

- **우선순위 파라미터 도입**: κ 값을 통해 선형/각속도 제어의 가중치를 동적으로 조정하여 대형 시간 스텝에 대응 가능

## Limitation & Further Study

**한계점**:
- CBF 설계 시 장애물의 정확한 위치 정보가 필요하며, 동적 장애물이나 불확실성 있는 환경에는 제한적
- 실험이 단일 장애물 환경에 국한되어 복잡한 다중 장애물 시나리오에서의 성능 미검증
- 세 가지 방식의 이론적 안전 보장 차이가 명확하게 분석되지 않음

**후속 연구 방향**:
- 동적 장애물 및 모델 불확실성을 처리하는 적응형 CBF 개발
- 고차원 상태 공간(시각 정보 등)에 대한 CBF 적용 방법 연구
- 다중 제약 조건(에너지, 이동 범위 등)을 동시에 고려하는 확장된 프레임워크
- 신경망 기반 CBF와의 비교 분석 및 안전 보장성 검증

## Evaluation

| 평가 항목 | 점수 |
|---------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 이 논문은 강화학습의 안전성 문제를 CBF라는 이론적으로 견고한 도구를 통해 해결하는 실질적이고 창의적인 접근을 제시하며, 세 가지 통합 방식의 비교와 sim2real 검증을 통해 실무적 가치를 입증한다. 다만 더 복잡한 환경과 동적 장애물에 대한 성능 평가가 후속 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 제어 장벽 함수를 통한 안전한 학습이 로봇 정책의 일반화 성능 향상에 필요한 안전성 기반을 제공한다.
- 🔗 후속 연구: [[papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/review]] — RL 안전성 제약이 소프트 로봇의 복잡한 동역학에서도 안전한 심-투-리얼 전이를 보장할 수 있다.
- 🏛 기반 연구: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 제어 장벽 함수의 안전성 제약 원리가 추론 시간 편향 완화에서 안전성 지침으로 확장될 수 있다.
- 🧪 응용 사례: [[papers/688_Robustness_evaluation_of_offline_reinforcement_learning_for/review]] — CBF 기반 안전성 제약이 오프라인 RL의 행동 섭동에 대한 견고성 평가에 활용될 수 있다.
- 🔗 후속 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 샤프니스 인식 최적화가 안전한 학습을 위한 제어 장벽 함수와 결합되어 더 견고한 정책을 생성할 수 있다.
- 🏛 기반 연구: [[papers/688_Robustness_evaluation_of_offline_reinforcement_learning_for/review]] — 오프라인 RL의 행동 섭동 취약성이 제어 장벽 함수 기반 안전성 제약의 필요성을 보여준다.
- 🔗 후속 연구: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 추론 시간 편향 완화가 안전성 지침을 통한 제약 기반 학습으로 확장될 수 있다.
- 🔗 후속 연구: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 제어 장벽 함수를 초과 사지 로봇의 계층적 제어에 통합하여 안전성을 보장하면서도 동적 평형을 유지할 수 있는 확장된 방법론을 제시한다.
