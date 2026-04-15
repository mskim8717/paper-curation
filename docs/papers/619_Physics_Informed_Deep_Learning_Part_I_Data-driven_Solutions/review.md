---
title: "619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions"
authors:
  - "Maziar Raissi"
  - "Paris Perdikaris"
  - "George Em Karniadakis"
date: "2017.11"
doi: "미제공"
arxiv: ""
score: 4.8
essence: "물리 법칙을 신경망에 내재화하여 적은 데이터로도 비선형 편미분방정식(PDE)의 해를 정확히 구하는 Physics-Informed Neural Networks (PINNs)을 제시하는 획기적 논문이다."
tags:
  - "cat/Computational_Molecular_Science_Models"
  - "sub/Neural_Operator_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Raissi et al._2017_Physics Informed Deep Learning (Part I) Data-driven Solutions of Nonlinear Partial Differential Equ.pdf"
---

# Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations

> **저자**: Maziar Raissi, Paris Perdikaris, George Em Karniadakis | **날짜**: 2017-11-28 | **DOI**: [미제공](https://doi.org/)

---

## Essence

물리 법칙을 신경망에 내재화하여 적은 데이터로도 비선형 편미분방정식(PDE)의 해를 정확히 구하는 Physics-Informed Neural Networks (PINNs)을 제시하는 획기적 논문이다.

## Motivation

- **Known**: 딥러닝은 이미지 인식, 자연언어처리 등에서 혁신적 성과를 달성했으나, 물리·생물 시스템 분석에서는 데이터 수집 비용이 매우 높음
- **Gap**: 기존 머신러닝은 소량 데이터(small data regime)에서 견고성이 떨어지고 수렴 보장이 없으며, 가우시안 과정 기반 방법은 비선형 문제에서 선형화 근사 필요
- **Why**: 물리 시스템은 PDE로 표현되는 방대한 사전 지식(prior knowledge)을 보유하고 있는데 현대 머신러닝에서 미활용 중
- **Approach**: 자동미분(automatic differentiation)을 활용하여 신경망이 PDE 제약조건을 직접 만족하도록 학습시키는 새로운 패러다임 제시

## Achievement

![Figure 1 - Burgers equation 결과](figures/fig1.webp)
*Burgers 방정식의 데이터 주도 해 복원: (상단) 예측된 시공간 해 및 학습 데이터 위치 (하단) 정확해와의 시간별 비교*

1. **혁신적 방법론**: 연속시간 모델에서 초기·경계 조건 데이터 100개로 Burgers 방정식 해를 상대 L₂ 오차 6.7×10⁻⁴로 복원 (가우시안 과정 대비 100배 정확도 향상)

2. **비선형 전용 처리**: 국소 시간화(local time-stepping) 또는 선형화 없이 일반 비선형 PDE 직접 해결

3. **데이터 효율성**: MSEf 항이 정칙화 기제로 작동하여 과적합(overfitting) 방지 및 소량 데이터 학습 가능

4. **미분가능 서로게이트 모델**: 모든 입력 좌표와 자유 매개변수에 대해 완전 미분가능한 대체 모델 획득

## How

![Figure 2 - Schrödinger equation](figures/fig2.webp)
*복소수 값 비선형 Schrödinger 방정식의 예측 해*

- **연속시간 모델 (Continuous Time Models)**:
  - u(t,x)를 심층 신경망으로 근사
  - f(t,x) = u_t + N[u]를 자동미분으로 구성
  - 손실함수: MSE = MSE_u (초기/경계) + MSE_f (내부 콜로케이션 점)
  
- **구현 간결성**: TensorFlow/PyTorch로 10줄 코드 수준의 단순한 구현

- **최적화**: L-BFGS 전체 배치 최적화 (소규모 데이터) 또는 SGD 미니배치 (대규모 데이터)

- **신경망 구조**: 9층, 각 층 20뉴런, 쌍곡탄젠트 활성화 함수

- **민감도 분석**: 학습 데이터 개수 N_u, 콜로케이션 점 개수 N_f, 신경망 아키텍처에 따른 정확도 체계 평가

## Originality

- **첫 고안**: PDE 제약을 신경망 손실함수에 직접 인코딩하는 개념의 초창기 제시
- **자동미분 활용**: 과학 계산에서 미활용 상태였던 자동미분을 PDE 풀이에 혁신적으로 적용
- **보편적 프레임워크**: 보존법칙, 확산, 반응-이동-확산, 운동론 등 다양한 PDE 클래스를 단일 틀로 처리
- **연속시간 처리**: 시공간 이산화 없이 연속 영역에서 직접 해 획득

## Limitation & Further Study

- **수렴성 보장 부재**: 일반적 수렴 증명 불재; PDE 적형성(well-posedness)과 해의 유일성 가정에 의존

- **충분한 근사용량 필요**: 신경망이 u(t,x)의 복잡도를 충분히 표현할 만큼 표현력(expressiveness) 필요

- **콜로케이션 점 배치**: 최적 배치 전략 미제시; 체계적 샘플링 방법 후속 연구 필요

- **Part II 예고**: 본 논문은 "데이터 주도 해 구하기"에 집중; Part II에서 "데이터 주도 PDE 발견" (매개변수 λ 역추론) 다룰 예정

- **대규모 문제 확장**: 고차원 공간에서의 성능, 복잡한 기하학적 영역 처리 등 미탐색


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4.8/5

**총평**: 물리 제약을 머신러닝에 정교하게 결합함으로써 소량 고가 데이터 환경에서 편미분방정식 풀이의 새로운 패러다임을 개척한 탁월한 논문으로, 이후 PINN 관련 연구의 폭발적 성장을 견인한 선구적 저작이다.

## Related Papers

- 🔗 후속 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — PINNs의 연속 의존성 특성을 활용한 cd-PINN이 기본 PINN 방법론을 발전시킨 접근법이다.
- 🔄 다른 접근: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 칼만 필터를 통합한 PINN과 기본 PINN은 불확실성 처리에서 서로 다른 접근법을 제시한다.
- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 물리정보신경망의 포괄적 과학 머신러닝 프레임워크가 PINN 발전의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/review]] — 물리 정보 딥러닝의 첫 번째 부분으로, LLM 기반 PDE 솔버를 물리 기반 딥러닝으로 확장하는 연구
- 🏛 기반 연구: [[papers/767_SPINONet_Scalable_Spiking_Physics-informed_Neural_Operator_f/review]] — 물리 정보 딥러닝의 일반적 원리는 에너지 효율적 스파이킹 물리 정보 신경 연산자 설계의 이론적 기반이다.
- 🔗 후속 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — cd-PINN의 연속 의존성 활용이 기본 PINN의 물리법칙 내재화를 더 강건한 형태로 발전시킨다.
- 🔄 다른 접근: [[papers/217_Chiral_spin_symmetry_and_hot_QCD/review]] — 물리 정보 딥러닝의 데이터 기반 접근법이 카이랄 스핀 대칭성의 이론적 접근과는 다른 방식으로 QCD 현상을 탐구한다
- 🔄 다른 접근: [[papers/618_Physical_formula_enhanced_multi-task_learning_for_pharmacoki/review]] — 물리 정보 기반 딥러닝의 일반적 접근법을 제시하여 약동학 특화 방법과 비교 관점을 제공한다
- 🏛 기반 연구: [[papers/456_Lang-PINN_From_Language_to_Physics-Informed_Neural_Networks/review]] — Physics Informed Deep Learning의 이론적 배경이 Lang-PINN 설계의 기반을 제공한다.
