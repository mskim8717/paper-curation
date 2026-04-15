---
title: "863_Value_iteration_for_learning_concurrently_executable_robotic"
authors:
  - "Sheikh A. Tahmid"
  - "Gennaro Notomista"
date: "2025"
doi: "정보"
arxiv: ""
score: 3.75
essence: "중복도(redundancy)를 가진 로봇 시스템이 여러 제어 태스크를 동시에 실행할 수 있도록 강화학습(RL)으로 학습된 가치 함수들 간의 독립성(independence)을 정의하고, 이를 만족하도록 학습하는 새로운 방법을 제안한다. 제안된 비용 함수(cost functional)를 통해 훈련된 태스크들을 우선순위 기반 스택으로 시간-변동 방식으로 조합 및 실행할 수 있다."
tags:
  - "cat/Computational_Molecular_Science_Models"
  - "cat/Reinforcement_Learning_Control_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Diffusion_Model_Inference"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tahmid and Notomista_2025_Value iteration for learning concurrently executable robotic control tasks.pdf"
---

# Value iteration for learning concurrently executable robotic control tasks

> **저자**: Sheikh A. Tahmid, Gennaro Notomista | **날짜**: 2025 | **DOI**: [정보 없음](https://doi.org/)

---

## Essence

중복도(redundancy)를 가진 로봇 시스템이 여러 제어 태스크를 동시에 실행할 수 있도록 강화학습(RL)으로 학습된 가치 함수들 간의 독립성(independence)을 정의하고, 이를 만족하도록 학습하는 새로운 방법을 제안한다. 제안된 비용 함수(cost functional)를 통해 훈련된 태스크들을 우선순위 기반 스택으로 시간-변동 방식으로 조합 및 실행할 수 있다.

## Motivation

- **Known**: 
  - 다중-목표 강화학습(multi-objective RL)은 여러 경쟁 목표를 동시에 달성하기 위해 사용되어 왔음
  - 기존 방법들은 목표의 부분집합 실행이나 온라인 우선순위 변경 불가능
  - 최근 작업 조합 방법들(task composition)은 학습된 태스크들의 호환성을 보장하지 않음

- **Gap**: 
  - 기존 다중-목표 RL은 시간-변동 우선순위 스택 구조를 지원하지 않음
  - 학습 단계에서 태스크 간 독립성을 강제하는 메커니즘 부재
  - Min-norm 컨트롤러[21]는 다중 가치 함수 조합은 가능하나 호환성 보장 미흡

- **Why**: 
  - 장기간 운영하는 로봇 시스템에서 목표가 시간에 따라 변함
  - 안전-중요(safety-critical) 태스크의 우선순위 존중 필요
  - 다중 로봇 시스템에서 동적 태스크 조합의 유연성 요구

- **Approach**: 
  - 학습된 비용-이동 함수(cost-to-go function)들 간의 독립성 정의
  - 이 독립성을 만족하도록 유도하는 비용 함수 제시
  - 연속 제어 설정을 위한 적합 가치 반복(fitted value iteration) 알고리즘 개발

## Achievement

1. **태스크 독립성의 수학적 정의**: 
   - 기존 Jacobian-기반 독립성[1,24]을 시스템 동역학을 고려하도록 확장
   - Definition 1에서 동역학을 포함한 새로운 독립성 개념 제시

2. **비용 함수 기반 학습 프레임워크**: 
   - 가치 함수들이 독립성을 만족하도록 하는 비용 함수 제안
   - 이론적 증명으로 제안된 비용 함수를 최소화하면 태스크 독립성 달성 가능함을 보임

3. **연속 제어용 적합 가치 반복**: 
   - CFVI[16]와 유사하나 다른 비용 함수 가정 하의 새로운 버전 개발
   - 신경망을 통한 심층 강화학습 패러다임에서 직접 학습 가능

4. **우선순위 기반 동시 실행**: 
   - Min-norm 컨트롤러[21] 활용으로 시간-변동 우선순위 스택 구현
   - 높은 우선순위 태스크 실행을 방해하지 않으면서 저우선순위 태스크 수행

## How

![Figure 1, 2, 3, 4: 다중 로봇 시스템의 삼각형 형성 및 회피 태스크 동시 실행 예시](figures/fig1234.webp)
*로봇 팀이 장애 영역을 회피하면서 삼각형을 형성하는 장면*

### 문제 설정 및 가정
- **동역학 모델**: 제어-관계(control-affine) 형태 $\dot{x}(t) = f(x) + g(x)u$ 가정
- **순차 학습**: 태스크를 중요도 순서(1번이 최중요)로 순차적으로 학습
- **비용 함수**: 각 태스크 $i$에 무한 지평선 최적화 문제 정의
$$J_i^*(x(t)) = \min_{u(\cdot)} \int_t^\infty e^{-\beta\tau}(q_i(x) + u^T R_i(x)u)d\tau$$

### 핵심 방법론

1. **태스크 독립성 정의**:
   - 높은 우선순위 태스크의 시간 도함수(time derivative)에 영향을 주지 않는 조건 정의
   - 가치 함수들의 Lie 도함수 기반 제약 조건 도입

2. **Min-norm 컨트롤러 활용**:
   - 다중 가치 함수로부터 제어 입력 생성
$$\min_{u,\delta} \|u\|^2 + \kappa\|\delta\|^2$$
$$\text{s.t. } L_f\tilde{J}_i(x) + L_g\tilde{J}_i(x)u \leq -\sigma_i(x) + \delta_i$$
   - 제약 완화 변수 $\delta$ 도입으로 실현 불가능성 대응

3. **비용 함수 설계**:
   - 상위 우선순위 태스크 방해를 최소화하는 추가 비용 항 도입
   - 하위 우선순위 태스크 가치 함수 학습 시 적용

4. **적합 가치 반복 알고리즘**:
   - 목표값 계산: 다단계 룩어헤드로 타겟 비용 계산 (Eq. 1)
   - 신경망 피팅: 최소 제곱 문제로 파라미터 업데이트 (Eq. 2)
   - TD(λ) forward view 활용으로 룩어헤드 길이 편향 제거

## Originality

- **새로운 개념화**: 시스템 동역학을 명시적으로 고려한 태스크 독립성 정의로 기존 기하학적 정의의 한계 극복

- **이론적 기여**: 제안된 비용 함수를 최소화함으로써 태스크 독립성 달성 가능성의 수학적 증명 제시

- **학습 알고리즘의 확장**: 연속 제어 공간에서의 적합 가치 반복을 비용-이동 함수 학습에 맞게 수정하여 제시

- **통합된 프레임워크**: 기존 min-norm 컨트롤러와 RL 기반 학습을 결합하여 유연한 우선순위 기반 태스크 실행 체계 구축

## Limitation & Further Study

- **가정의 한계**:
  - 제어-관계 동역학 가정이 모든 로봇 시스템에 적용 불가능
  - 동역학이 정확히 알려진 경우만 고려 (실제로는 근사 필요)
  - 결정적 환경만 다루며 확률적 동역학 미처리

- **학습 순서의 제약**:
  - 태스크를 중요도 순서대로 순차 학습해야 함 (병렬 학습 불가)
  - 우선순위 재정렬 시 재학습 필요성 (온라인 우선순위 변경 불가)

- **신경망 근사의 문제**:
  - 학습된 가치 함수의 근사 오차가 독립성 조건 위반 가능성
  - Lie 도함수 계산의 수치적 안정성 문제

- **후속 연구 방향**:
  - 확률적 시스템 환경에서의 방법 확장
  - 부분적으로 알려진 동역학을 다루는 알고리즘
  - 태스크의 병렬 학습 메커니즘 개발
  - 신경망 근사 오차에 대한 견고성(robustness) 분석

## Evaluation

- **Novelty (독창성)**: 4/5
  - 시스템 동역학을 포함한 새로운 독립성 정의와 비용 함수는 참신함
  - 다만 min-norm 컨트롤러[21]와의 조합은 자연스러운 확장

- **Technical Soundness (기술적 타당성)**: 4/5
  - 수학적 증명과 알고리즘 설계가 체계적임
  - 제어-관계 동역학 가정 하에서 엄밀함
  - 신경망 근사 오차에 대한 수렴성 분석은 미흡

- **Significance (의의)**: 3.5/5
  - 다중 로봇 시스템 제어에 실용적 가치 있음
  - 시간-변동 우선순위 기능은 실제 응용에 유용
  - 시뮬레이션 검증이 주로 이루어져 실제 로봇 실험 부재

- **Clarity (명확성)**: 3.5/5
  - 전반적 구조는 명확하나 일부 기호 정의 복잡
  - Definition 1의 독립성 개념이 직관적이지 않음
  - 알고리즘 및 실험 절차 설명 충분

- **Overall (종합)**: 3.75/5

**총평**: 제어-관계 동역학을 고려한 새로운 태스크 독립성 개념과 이를 학습하는 프레임워크는 강점이나, 순차 학습 및 정확한 동역학 가정 등 실용성 제약이 있으며, 이론적 수렴성 분석과 실제 로봇 실험 검증이 필요한 상태이다.

## Related Papers

- 🔗 후속 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 로봇 이동 정책의 일반화를 개선하는 연구가 다중 태스크 동시 실행을 위한 독립성 학습으로 확장될 수 있다.
- 🔄 다른 접근: [[papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/review]] — 시뮬레이션에서 실제 환경으로의 전이 문제를 우선순위 기반 태스크 스택으로 해결하는 다른 접근법을 제시한다.
- 🧪 응용 사례: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 화학 증착 공정 제어에서 제안된 독립적 가치함수 학습 방법이 다중 태스크 동시 실행에 적용될 수 있다.
- 🏛 기반 연구: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 계층적 휴머노이드 로컴션 프레임워크가 중복도를 가진 로봇 시스템의 다중 태스크 제어 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/003_A_comprehensive_survey_of_cross-domain_policy_transfer_for_e/review]] — 동시 실행 가능한 로봇 행동을 위한 가치 반복 학습 연구가 크로스 도메인 정책 전이의 구체적인 학습 방법론으로 발전되었다
- 🏛 기반 연구: [[papers/141_Autonomous_robotic_system_with_optical_coherence_tomography/review]] — 동시 실행 가능한 로봇 기술을 위한 가치 반복 학습으로, 자율 로봇 시스템의 제어 알고리즘 기반을 제공
- 🔄 다른 접근: [[papers/010_A_hierarchical_framework_for_measuring_scientific_paper_inno/review]] — 로봇 제어의 동시 실행이라는 공통 관심사를 가지지만 인형형 보행 vs 일반적 로봇 작업이라는 다른 응용 영역을 다룬다.
