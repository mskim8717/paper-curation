---
title: "721_Scientific_Machine_Learning_through_Physics-Informed_Neural"
authors:
  - "Salvatore Cuomo"
  - "Vincenzo Schiano di Cola"
  - "Fabio Giampaolo"
  - "Gianluigi Rozza"
  - "Maziar Raissi"
date: "2022.01"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "물리 방정식을 신경망의 손실함수에 직접 인코딩하는 PINN(Physics-Informed Neural Networks)에 관한 종합적 문헌 리뷰로, 이 기법의 발전, 변형, 적용 사례 및 미해결 이론적 문제들을 다룬다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Physics-Informed_Neural_Operators"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next.pdf"
---

# Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next

> **저자**: Salvatore Cuomo, Vincenzo Schiano di Cola, Fabio Giampaolo, Gianluigi Rozza, Maziar Raissi, Francesco Piccialli | **날짜**: 2022-01-14 | **DOI**: N/A

---

## Essence

물리 방정식을 신경망의 손실함수에 직접 인코딩하는 PINN(Physics-Informed Neural Networks)에 관한 종합적 문헌 리뷰로, 이 기법의 발전, 변형, 적용 사례 및 미해결 이론적 문제들을 다룬다.

## Motivation

- **Known**: 심층 신경망이 컴퓨터 비전, 자연어 처리 등에서 성공했으며, 최근 편미분방정식(PDE) 해결에도 적용되기 시작함. 전통적 수치해석 방법(유한요소법 등)은 고도의 비선형성, 경계층, 불연속점 등에서 어려움.

- **Gap**: PINNs 분야가 급속도로 성장하고 있으나, 명확한 용어 정의, 체계적인 분류, 이론적 기반이 부족함. 다양한 변형(PCNN, hp-VPINN, CPINN 등)과 최적화 기법들이 산발적으로 개발되고 있음.

- **Why**: 딥러닝의 메타모델 구성 능력과 신경망의 보편 근사 정리(universal approximation theorem)는 복잡한 동역학계 해결의 새로운 패러다임을 제시하지만, 고차원 문제의 차원의 저주(curse of dimensionality) 등 근본적 문제 해결이 필요함.

- **Approach**: Raissi et al. (2019)가 2017년 제시한 PINN 프레임워크와 그 변형들을 중심으로, 신경망 구조, 활성함수, 최적화 기법, 손실함수 설계 등의 관점에서 포괄적 문헌 검토 수행.

## Achievement

1. **PINN의 명확한 정의와 역사적 배경**: Dissanayake and Phan-Thien (1994)부터 현대의 Raissi et al. (2019)까지의 발전 과정을 추적. 자동미분(automatic differentiation)과 오픈소스 라이브러리(TensorFlow, PyTorch) 등 기술 발전이 PINN 보급의 핵심임을 규명.

2. **다양한 PINN 변형의 분류**: 기본 PINN(vanilla PINN)뿐 아니라 physics-constrained neural networks(PCNN, 경계조건을 하드 제약으로 처리), 변분형 hp-VPINN(Galerkin 방법 기반), conservative PINN(CPINN, 보존칙 강화) 등을 체계적으로 정리.

3. **핵심 우점의 정량화**: 메시 없는 방법(mesh-free), 데이터 레이블링 불필요, 해석적 미분 제공, 정방향-역방향 문제의 통일된 풀이 등 기존 수치해석법 대비 명확한 장점 입증.

## How

- **손실함수 구성**: PDE 잔차(residual) 항 + 초기/경계조건 항의 다중 작업 학습(multi-task learning) 프레임워크
  
- **배치(collocation point) 기반 최적화**: 무작위 또는 적응적 배치점 선택으로 정의역 내 PDE 만족도 강제

- **신경망 구조 개선**: 은닉층 개수, 노드 수, 활성함수(ReLU, Tanh, GELU 등) 최적화를 통한 수렴성 개선

- **기울기 기반 최적화**: Adam, L-BFGS 등 다양한 옵티마이저 적용 및 학습률 스케줄링

- **적응형 가중치 기법**: 손실함수의 PDE 항과 데이터 항 간 가중치 동적 조정으로 수렴 가속화

## Originality

- **포괄적 분류 체계**: "physics-informed", "physics-based", "physics-guided", "theory-guided" 등 혼용되던 용어를 Kim et al. (2021b)의 분류법(신경망 종류, 물리 정보 표현 방식, 통합 방식) 적용으로 정리

- **역사적 연속성 강조**: 1990년대 제약 신경망부터 현대 PINN까지의 계승 관계 제시로, 최근 성공이 기술 발전(GPU, 자동미분)에 기인함을 명확히 함

- **실무적 비교**: PINN과 Deep Ritz Method(DRM), Deep Galerkin Method(DGM), Feynman-Kac 정리 기반 방법 등과의 차별성 제시

## Limitation & Further Study

- **미해결 이론적 문제**: 수렴성 증명, 근사 오차 한계, 차원의 저주에 대한 엄밀한 분석 부족. PINN이 고차원 문제(10차원 이상)에서 성능 저하를 보이는 메커니즘 규명 필요.

- **학습 불안정성**: 배치점 선택의 무작위성, 손실함수 항 간 스케일 불균형(scale imbalance), 어려운 기울기 최적화 문제(ill-conditioned Hessian) 해결 필요.

- **경계 조건 처리**: 복잡한 기하학적 영역에서 경계조건 만족도 보장 메커니즘 부족. PCNN의 경계 강제 방식이 모든 문제에 적용 가능하지 않음.

- **적응형 배치 전략**: 균일 배치 대비 적응형 배치(residual-based, importance sampling)의 효율성에 관한 이론적 근거 및 일반화된 알고리즘 개발 필요.

- **후속 연구 방향**: (1) 보편 근사성(universal approximation) 이론을 PDE 설정으로 확장, (2) 구조화된 신경망(그래프 신경망, 연산자 신경망) 활용, (3) 불확실성 정량화(uncertainty quantification) 통합, (4) 다물리 다중 스케일 문제 확장.

## Evaluation

- **Novelty**: 3.5/5 — PINN 자체의 혁신성보다는 기존 문헌의 포괄적 정리. 다만 명확한 분류 체계와 역사적 맥락화 제공으로 후속 연구의 기초 마련.

- **Technical Soundness**: 4/5 — 다양한 기법 소개는 정확하나, 각 변형의 정량적 비교와 성능 분석이 제한적. 이론적 근거 부재 지적은 타당.

- **Significance**: 4.5/5 — 급속 성장하는 PINN 분야의 현황을 체계적으로 정리함으로써 신규 연구자의 진입장벽을 낮추고, 미해결 문제를 명확히 제시하여 연구 방향 제시.

- **Clarity**: 4/5 — 논리적 구성과 명확한 용어 정의. Figure 1에서 논문 수의 지수적 증가를 시각화하여 분야의 중요성 강조. 다만 일부 기술적 세부사항(활성함수별 비교, 배치점 선택 전략)은 더 자세한 설명 필요.

- **Overall**: 4/5

**총평**: 본 논문은 Physics-Informed Neural Networks 분야의 종합적이고 신뢰할 수 있는 현황 보고서로, 명확한 분류 체계와 미해결 이론적 문제를 제시함으로써 과학계산 기계학습의 다음 단계 발전을 위한 로드맵을 제공한다. 다만 각 기법의 정량적 성능 비교와 이론적 분석이 더 심화되면 더욱 값진 참고자료가 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/103_Architectures_variants_and_performance_of_neural_operators_A/review]] — 신경 연산자의 아키텍처와 변형에 관한 연구는 물리 정보 신경망 발전의 핵심 기술적 기반을 제공한다.
- 🔗 후속 연구: [[papers/767_SPINONet_Scalable_Spiking_Physics-informed_Neural_Operator_f/review]] — 전통적 PINN과 에너지 효율적 스파이킹 PINN은 물리 정보 신경망의 서로 다른 발전 방향을 보여준다.
- 🔄 다른 접근: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 물리 방정식 인코딩과 보상 기반 정렬은 모두 과학적 제약 조건을 AI 모델에 통합하는 서로 다른 방법론이다.
- 🏛 기반 연구: [[papers/276_Discovery_of_Unstable_Singularities/review]] — 물리학 기반 신경망이 특이점의 수치적 불안정성을 해결하는 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/232_CodePDE_An_Inference_Framework_for_LLM-driven_PDE_Solver_Gen/review]] — 물리 정보 신경망을 통한 과학적 기계학습에 대한 포괄적 조사로, PDE 솔버 생성의 이론적 기반을 제공
- 🧪 응용 사례: [[papers/275_Discovering_symbolic_differential_equations_with_symmetry_in/review]] — 물리학 기반 신경망이 대칭성 제약 하 미분방정식 발견에 직접 적용된다
- 🏛 기반 연구: [[papers/286_Domain-specific_ReAct_for_physics-integrated_iterative_model/review]] — 물리학 정보 신경망이 도메인 특화 AI 적용의 기반을 제공한다.
- 🧪 응용 사례: [[papers/428_Inference-Time_Alignment_in_Diffusion_Models_with_Reward-Gui/review]] — 물리 정보 신경망과 확산 모델의 보상 기반 정렬은 모두 과학적 제약 조건을 AI 모델에 통합하는 방법론이다.
- 🔗 후속 연구: [[papers/767_SPINONet_Scalable_Spiking_Physics-informed_Neural_Operator_f/review]] — 기존 PINN의 에너지 효율성을 개선한 스파이킹 기반 접근법으로, 물리 정보 신경망의 실용적 발전을 보여준다.
- 🏛 기반 연구: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — 물리정보신경망의 포괄적 과학 머신러닝 프레임워크가 PINN 발전의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/799_The_frontier_of_simulation-based_inference/review]] — 물리 정보 신경망을 통한 과학적 기계학습이 시뮬레이션 기반 추론의 물리학적 제약 조건 통합 방법론을 제공한다
- 🔄 다른 접근: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 물리 정보 신경망 기반의 과학 머신러닝 접근법으로, 이 논문의 신경 연산자 중심 파운데이션 모델과 다른 물리 기반 접근을 보여준다
- 🏛 기반 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 물리정보신경망의 과학 머신러닝이 cd-PINN의 연속 의존성 활용 방법론에 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/082_Ai-assisted_design_of_experiments_at_the_frontiers_of_comput/review]] — 물리 정보 신경망을 통한 과학적 기계학습이 계산 전계의 AI 보조 실험 설계를 위한 물리학적 제약 조건 통합 방법론을 제공한다
- 🔗 후속 연구: [[papers/307_Efficient_Prediction_of_SO3-Equivariant_Hamiltonian_Matrices/review]] — 물리 정보 신경망과 SO(3) 등변성을 결합하여 더 정확한 전자구조 예측 프레임워크 구축
- 🧪 응용 사례: [[papers/576_Nonlinear_stochastic_and_quantum_motion_from_Coulomb_forces/review]] — 물리 정보 신경망을 통해 쿨롱 상호작용의 3차 비선형 항이 실제 양자 센서 설계에 적용됨
- 🏛 기반 연구: [[papers/758_Simulations_in_the_era_of_exascale_computing/review]] — 물리 정보 기반 신경망의 과학적 기계학습 기초를 제공하며 엑사스케일 시뮬레이션과 연계된다
- 🏛 기반 연구: [[papers/497_LLM_and_Simulation_as_Bilevel_Optimizers_A_New_Paradigm_to_A/review]] — 물리 정보 신경망 연구가 LLM과 물리 시뮬레이션 결합 접근법의 과학적 기반을 제공함
- 🏛 기반 연구: [[papers/620_Physics-Informed_Autonomous_LLM_Agents_for_Explainable_Power/review]] — 물리 정보 신경망 과학기계학습이 전력전자 자율 에이전트의 물리 기반 설계 원리를 제공한다
