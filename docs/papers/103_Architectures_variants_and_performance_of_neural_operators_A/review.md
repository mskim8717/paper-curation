---
title: "103_Architectures_variants_and_performance_of_neural_operators_A"
authors:
  - "Shengjun Liu"
  - "Yu Yu"
  - "Ting Zhang"
  - "Hanchao Liu"
  - "Xinru Liu"
date: "2025.10"
doi: "10.1016/j.neucom.2025.130518"
arxiv: ""
score: 4.1
essence: "편미분방정식(PDE) 해법으로 전통 수치해석 방법을 대체할 수 있는 신경 연산자(Neural Operators, NOs)의 아키텍처, 변형, 성능을 종합적으로 비교 분석한 체계적 리뷰 논문이다. DeepONet, 적분 커널 연산자, 트랜스포머 기반 신경 연산자의 세 가지 주요 아키텍처와 이들의 물리정보 통합 변형, 복잡계 응용을 다룬다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Physics-Informed_Neural_Operators"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2025_Architectures, variants, and performance of neural operators A comparative review.pdf"
---

# Architectures, variants, and performance of neural operators: A comparative review

> **저자**: Shengjun Liu, Yu Yu, Ting Zhang, Hanchao Liu, Xinru Liu, Deyu Meng | **날짜**: 2025-10-01 | **DOI**: [10.1016/j.neucom.2025.130518](https://doi.org/10.1016/j.neucom.2025.130518)

---

## Essence

![Figure 1](figures/fig1.webp)
*신경 연산자의 발전 역사*

편미분방정식(PDE) 해법으로 전통 수치해석 방법을 대체할 수 있는 신경 연산자(Neural Operators, NOs)의 아키텍처, 변형, 성능을 종합적으로 비교 분석한 체계적 리뷰 논문이다. DeepONet, 적분 커널 연산자, 트랜스포머 기반 신경 연산자의 세 가지 주요 아키텍처와 이들의 물리정보 통합 변형, 복잡계 응용을 다룬다.

## Motivation

- **Known**: 전통 수치 해석법(유한차분법, 유한요소법)은 격자 이산화에 의존하며, 고차원 PDE에서 계산량이 크고, 매개변수 변화 시마다 재계산 필요. Physics-Informed Neural Networks(PINNs)는 단일 PDE만 해결 가능하고 저차원 문제에서 성능 저하

- **Gap**: 기존 문헌은 특정 적분 커널 연산자만 다루거나 DeepONet과 FNO만 비교하여, 신경 연산자 전체 프레임워크에 대한 포괄적 개요 부재

- **Why**: 신경 연산자는 한 번의 학습으로 PDE 계열 전체를 해결할 수 있고, 메시 독립적이며 다양한 경계조건과 복잡한 기하 형태를 처리할 수 있어 실용적 가치가 높음

- **Approach**: 세 가지 기본 아키텍처의 구조와 성질을 소개하고, (1) 연산자 기저 기반 변형, (2) 물리정보 통합 변형, (3) 복잡계 응용 변형을 분석한 후, 수치 실험으로 성능 비교

## Achievement

![Figure 2](figures/fig2.webp)
*DeepONet 네트워크 아키텍처: 트렁크 네트워크(trunk network)와 p개의 브랜치 네트워크(branch network)로 구성*

1. **포괄적 분류 체계 수립**: 신경 연산자를 세 가지 주요 아키텍처(DeepONet, 적분 커널 연산자, 트랜스포머 기반)로 체계화하고 각각의 기본 구조, 장단점, 적용 조건을 명확히 정의

2. **다층적 변형 분석**: 연산자 기저(operator basis) 변형, 물리정보 통합, 복잡계 응용 세 방향으로 신경 연산자 확장을 체계적으로 정리하여 상호연관성과 차이점 제시

3. **성능 비교 실험**: 수치 실험을 통해 서로 다른 연산자 방법의 특성, 정확도, 계산 효율을 비교하여 각 방법의 적용 시나리오 제시

4. **실무 가이드라인 제공**: 신경 연산자의 한계(대량 학습 데이터 필요, 고차원 문제에서 성능 저하)와 개선 방향을 제시하여 실제 응용과 개발을 위한 체계적 지침 제공

## How

![Figure 3](figures/fig3.webp)
*적분 커널 연산자 프레임워크: 입력 함수 a가 점별 리프팅 연산자를 통해 고차원 공간으로 변환*

**DeepONet 방식**:
- 트렁크 네트워크: 쿼리 좌표점 x에서 기저 함수 t_k(x) 학습
- 브랜치 네트워크: 입력 함수 a로부터 계수 b_k(a) 학습
- 최종 출력: G(a)(x) = Σ b_k(a)t_k(x) + b_0 형태로 조합

**적분 커널 연산자 방식**:
- 리프팅(Lifting): 저차원 입력 함수를 고차원 특성 공간으로 변환
- 커널 적분 계층(Integral Kernel Layer): Nyström 근사를 이용한 점별 함수 변환
- 투영(Projection): 고차원 특성을 다시 저차원 함수 공간으로 투영
- Graph Neural Operator(GNO)와 Fourier Neural Operator(FNO)가 대표 사례

**트랜스포머 기반 방식**:
- 자기 주의(Self-attention) 메커니즘으로 함수 공간의 전역 의존성 포착
- Galerkin-Transformer, General Neural Operator Transformer(GNOT) 등이 위치 인코딩 없이 연속 함수 처리

**물리정보 통합**:
- PDE 잔차(residual)를 손실함수에 추가하여 물리 법칙 제약
- 경계조건과 초기조건을 명시적으로 인코딩

## Originality

- **포괄적 비교 분석**: 기존 리뷰가 특정 아키텍처만 다룬 반면, 이 논문은 세 가지 주요 아키텍처를 동등한 수준에서 체계적으로 비교 분석

- **다차원적 변형 분류**: 연산자 기저, 물리정보, 복잡계 응용이라는 세 개의 직교하는 차원에서 신경 연산자 확장을 분류하여 새로운 분류 체계 제시

- **실험적 성능 벤치마킹**: 단순 비교에 그치지 않고 수치 실험으로 다양한 조건에서의 성능 차이를 정량화

- **실무 지향적 가이드라인**: 이론적 분석과 실험 결과를 바탕으로 각 방법의 적용 시나리오와 한계를 구체적으로 제시

## Limitation & Further Study

- **데이터 의존성**: 신경 연산자는 복잡한 PDE 해결을 위해 대량의 고품질 학습 데이터 필요하나, 데이터 생성 비용이 높아 실무 적용 제약

- **고차원 확장성**: 고차원 PDE에서 아직도 성능 저하가 발생하며, 차원의 저주(curse of dimensionality) 극복이 완전하지 않음

- **수렴성 보장 부재**: 신경 연산자의 수렴성, 오차 추정, 안정성에 대한 이론적 분석이 부족하여 신뢰성 검증 어려움

- **후속 연구 방향**:
  - 데이터 효율적 학습 기법 개발(전이 학습, 메타 러닝 활용)
  - 신경 연산자의 수학적 기초 강화(수렴성 증명, 오차 경계)
  - 불규칙한 격자, 비균질 영역에서의 강건성 개선
  - 시간 의존 PDE와 비선형 문제에 대한 특화된 아키텍처 개발


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.1/5

**총평**: 신경 연산자의 주요 아키텍처와 변형을 체계적으로 정리하고 성능을 실증적으로 비교한 가치 있는 종합 리뷰로, PDE 해법 분야에서 신경 연산자 적용을 추진하는 연구자와 실무자에게 실질적 가이드라인을 제공한다. 다만 이론적 수렴성 분석이 부족하고 고차원 문제에서의 근본적 한계가 여전히 미해결 상태인 점이 한계이다.

## Related Papers

- 🔄 다른 접근: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — 둘 다 신경 연산자를 다루지만, 첫 번째는 포괄적 비교 분석에, Neural-POD는 플러그 앤 플레이 프레임워크에 집중한다
- 🔗 후속 연구: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 언센티드 칼만 필터를 결합한 물리정보 신경망 연구가 물리정보 통합 변형을 포함한 신경 연산자 아키텍처로 발전되었다
- 🏛 기반 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 과학 머신러닝을 위한 기초 모델 연구가 전통 수치해석 방법을 대체하는 신경 연산자 개발의 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 신경 연산자의 아키텍처와 변형에 관한 연구는 물리 정보 신경망 발전의 핵심 기술적 기반을 제공한다.
- 🏛 기반 연구: [[papers/572_Neural_Ordinary_Differential_Equations/review]] — 신경 연산자의 아키텍처와 변형들이 Neural ODE와 같은 연속 신경망 모델의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch/review]] — 신경 연산자의 다양한 아키텍처와 변형을 체계적으로 정리한 조사 연구로, 과학 머신러닝 파운데이션 모델의 기술적 기반을 제공한다
- 🏛 기반 연구: [[papers/364_From_Theory_to_Application_A_Practical_Introduction_to_Neura/review]] — 신경 연산자 아키텍처와 변형들에 대한 종합적 이해가 실용적 응용의 기반 지식을 제공함
- 🏛 기반 연구: [[papers/354_From_GPU_Engineering_to_Scientific_Discovery_Parallelism_Tec/review]] — 신경망 연산자의 다양한 아키텍처와 성능 분석의 이론적 기반을 제공합니다.
