---
title: "006_A_deep_subgrouping_framework_for_precision_drug_repurposing"
authors:
  - "Seungyeon Lee"
  - "Ruoqi Liu"
  - "Feixiong Cheng"
  - "Ping Zhang"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "STEDR은 환자 하위군의 이질적 치료 반응을 고려하여 실제 환자 데이터에서 임상시험을 모의실험하고 정밀 약물 재창출(precision drug repurposing)을 수행하는 딥러닝 프레임워크이다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Computational_Molecular_Science_Models"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lee et al._2024_A deep subgrouping framework for precision drug repurposing via emulating clinical trials on real-wo.pdf"
---

# A deep subgrouping framework for precision drug repurposing via emulating clinical trials on real-world patient data

> **저자**: Seungyeon Lee, Ruoqi Liu, Feixiong Cheng, Ping Zhang | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2412.20373](https://arxiv.org/abs/2412.20373)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Flowchart of a deep subgrouping framework for*

STEDR은 환자 하위군의 이질적 치료 반응을 고려하여 실제 환자 데이터에서 임상시험을 모의실험하고 정밀 약물 재창출(precision drug repurposing)을 수행하는 딥러닝 프레임워크이다.

## Motivation

- **Known**: 기존 약물 재창출 연구는 전체 인구를 동질적으로 취급하며, 신경망 기반 치료 효과 추정(TEE, Treatment Effect Estimation) 방법들이 제안되어 있다.
- **Gap**: 기존 방법들은 환자 하위군 간의 이질적 치료 반응을 무시하며, 시간 변동적이고 고차원의 실제 의료 데이터(RWD)에 직접 적용되지 않고, 임상적으로 관련된 변수로 하위군을 특성화하지 못한다.
- **Why**: 알츠하이머병(AD)처럼 승인된 약물이 적고 환자 간 치료 반응이 다양한 질환에서 정밀 의약학 기반의 약물 재창출은 임상 효과를 높이고 더 많은 재창출 후보를 발굴할 수 있다.
- **Approach**: STEDR은 이중 수준 주의 메커니즘(covariate-level, visit-level attention)으로 시간 데이터를 인코딩하고, VAE(Variational Auto-Encoder) 기반 하위군 네트워크로 환자를 이질적 분포를 가진 하위군으로 분류하여 하위군 특화 치료 효과를 추정한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: Drug selection and screening criteria. From 1,134*

- **첫 통합 프레임워크**: 하위군 분석과 치료 효과 추정을 결합한 약물 재창출의 첫 사례
- **대규모 임상시험 모의실험**: 800만+ 환자 MarketScan MDCR 데이터베이스에서 1,134개 약물 중 100회씩 임상시험을 모의실험하여 14개 AD 재창출 후보 약물 발굴
- **임상적 해석성**: 병력(comorbidity), 인구통계학적 특성 등 AD 관련 위험 요인으로 정의된 임상적으로 관련성 높은 환자 하위군 특성화
- **우수한 성능**: 기존 방법론 대비 재창출 후보 약물 식별에서 우수성 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: An illustration of STEDR. The EHR data is processed through patient-level attention to learn individualized re*

- 이중 수준 주의 메커니즘: 공변량 수준 주의로 각 진단 코드의 영향도 학습, 방문 수준 주의로 시간 역학 관계 포착
- 환자 인코더: 종단 EHR 데이터를 개인화된 환자 표현으로 변환
- 하위군 표현 네트워크: VAE를 통해 각 환자를 특정 하위군에 할당하고 하위군 특화 표현 추출
- 치료 효과 추정: 하위군별 표현에서 경향 점수(propensity score)와 잠재 결과(potential outcomes) 예측
- 약물 선별 및 필터링: 1,134개 약물 중 포함 기준을 충족한 약물만 선정
- 임상시험 모의실험(trial emulation): 각 약물별 100회 반복 시뮬레이션으로 하위군별 처리 효과 추정

## Originality

- 하위군 기반 정밀 약물 재창출이라는 새로운 문제 정의
- VAE 기반 동적 하위군 식별 아키텍처로 기존 단일 공유 잠재공간의 한계 극복
- 이중 수준 주의로 시간 변동적 고차원 데이터의 복합적 특성 처리
- 실제 대규모 EHR 데이터에서 임상적으로 해석 가능한 하위군 도출

## Limitation & Further Study

- 선택 편향(selection bias) 완전 제거 불가 - 관찰 데이터의 근본적 한계
- 하위군 수의 사전 결정 필요 - 최적 하위군 개수 자동 결정 메커니즘 부재
- 알츠하이머병 중심 평가 - 다른 질환군에 일반화 가능성 검증 필요
- 약물 안전성 정보 미포함 - 식별된 후보의 재창출 가능성 검증에 약리학적 검토 필수
- 후속연구: (1) 동적 하위군 수 결정 알고리즘 개발, (2) 다중 질환군 전이 학습 연구, (3) 실제 임상 검증 수행

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: STEDR은 약물 재창출 분야에 정밀 의약학 관점의 하위군 분석을 처음 통합하여 새로운 문제 정의를 제시하며, 이중 수준 주의와 VAE 기반 하위군 네트워크로 기술적 혁신을 이루었다. 800만+ 환자 대규모 데이터에서 14개 AD 약물 후보를 발굴하고 임상적 해석성을 확보한 점에서 강한 실무 가치를 보유하나, 관찰 데이터의 편향 문제와 다질환군 일반화 검증이 후속 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 정밀 약물 재창출에서 환자 하위군 분석과 대조적 약물-질병 상호작용 모델링은 서로 다른 관점에서 개인화된 치료법을 탐구한다.
- 🏛 기반 연구: [[papers/618_Physical_formula_enhanced_multi-task_learning_for_pharmacoki/review]] — 약동학을 위한 물리학 공식 강화 다중 작업 학습이 환자 하위군별 치료 반응 예측의 이론적 기반을 제공한다.
