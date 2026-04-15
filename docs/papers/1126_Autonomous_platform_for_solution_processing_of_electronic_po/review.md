---
title: "1126_Autonomous_platform_for_solution_processing_of_electronic_po"
authors:
  - "Chengshi Wang"
  - "Yeon-Ju Kim"
  - "Aikaterini Vriza"
  - "Rohit Batra"
  - "Arun Baskaran"
date: "2025.02"
doi: "10.1038/s41467-024-55655-3"
arxiv: ""
score: 4.0
essence: "Polybot이라는 AI 기반 자동화 연구실을 개발하여 중요도 기반 베이지안 최적화(importance-guided Bayesian optimization)로 7차원 처리 공간을 탐색하고, 전자 고분자 박막의 고전도성(>4500 S/cm)과 저결함을 동시에 달성했다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Computational_Molecular_Science_Models"
  - "sub/Autonomous_Biological_Discovery_AI"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Autonomous platform for solution processing of electronic polymers.pdf"
---

# Autonomous platform for solution processing of electronic polymers

> **저자**: Chengshi Wang, Yeon-Ju Kim, Aikaterini Vriza, Rohit Batra, Arun Baskaran, Naisong Shan, Nan Li, Pierre Darancet, Logan Ward, Yuzi Liu, Maria K. Y. Chan, Subramanian K.R.S. Sankaranarayanan, H. Christopher Fry, C. Suzanne Miller, Henry Chan, Jie Xu | **날짜**: 2025-02-17 | **DOI**: [10.1038/s41467-024-55655-3](https://doi.org/10.1038/s41467-024-55655-3)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | A closed-loop electronic thin ﬁlm discovery platform in self-driving*

Polybot이라는 AI 기반 자동화 연구실을 개발하여 중요도 기반 베이지안 최적화(importance-guided Bayesian optimization)로 7차원 처리 공간을 탐색하고, 전자 고분자 박막의 고전도성(>4500 S/cm)과 저결함을 동시에 달성했다.

## Motivation

- **Known**: 전자 고분자(electronic polymer)는 인쇄 전자, 웨어러블, 에너지 장치 등에 광범위하게 사용되고 있으나, 용액 처리를 통해 원하는 특성의 박막을 제조하는 것은 매우 어려운 문제로 남아있다.
- **Gap**: 기존 AI/ML 기반 박막 처리 연구는 제한된 수의 처리 인자와 단일 특성 최적화만 수행했으며, 소규모 데이터셋과 높은 실험 불확실성으로 인해 다중 목적 최적화를 다루지 못했다.
- **Why**: 전자 고분자의 처리-특성 관계는 고차원적이고 복잡하며, 수십 년의 휴리스틱 기반 연구에도 불구하고 체계적인 이해가 부족하여, AI 자동화를 통한 효율적인 최적화가 필수적이다.
- **Approach**: Polybot 플랫폼은 로봇 기반 완전 자동화 실험 워크플로우(용액 혼합, 블레이드 코팅, 어닐링, 전기적 특성 측정)와 중요도 기반 베이지안 최적화 알고리즘을 결합하여 다중 목적을 동시에 최적화한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3 | AI-guided closed-loop optimization and their scaled-up fabrication. a–c*

- **높은 실험 처리량**: 샘플당 약 15분으로 하루 약 100개 샘플 처리 가능하며 높은 재현성 확보
- **우수한 전기적 특성**: PEDOT:PSS 박막의 평균 전도도 4500 S/cm 이상 달성 및 투명 전도성 박막 스케일업 제조 레시피 개발
- **다중 목적 최적화**: 전도도 최대화와 코팅 결함 최소화를 동시에 추구하는 효율적인 최적화 전략 구현
- **통계적 데이터 품질**: 실험 재현성 보장을 위한 통계 분석 방법 적용으로 신뢰성 높은 데이터셋 구축
- **해석 가능성**: 특성 중요도 분석(feature importance analysis)과 형태학적 특성화로 핵심 설계 인자 규명

## How

![Figure 2](figures/fig2.webp)

*Fig. 2 | Automated characterization of ﬁlm defects and electrical conductivity.*

- 완전 자동화 플랫폼: 액체/기판/바이알 핸들링, 용액 혼합, 블레이드 코팅, 세척, 어닐링, 온라인 특성화 시스템 통합
- 7차원 처리 매개변수 동시 탐색: 첨가제 종류/비율, 블레이드 코팅 속도/온도, 후처리 용매, 후처리 속도/온도
- 중요도 기반 베이지안 최적화: 확률적 샘플링으로 미탐색 영역 전략적 탐색 및 기존 데이터 활용
- 결함 정량화: 이미지 처리 및 컴퓨터 비전 기술(색상/휴(hue) 정보, Harris 코너 검출, 투시 변환)을 이용한 박막 균일성 평가
- 전도도 측정: 8개 I-V 곡선을 통한 신뢰성 높은 전기적 특성 평가
- PEDOT:PSS 선정: 전도도와 코팅 결함이 처리 조건에 민감한 모델 재료로 선택하여 방법론 효과 입증

## Originality

- 완전 자동화 솔루션 처리 플랫폼: 용액 제조부터 전기적 특성 측정까지 전체 공정을 통합한 최초의 자동 실험실
- 다중 목적 최적화 프레임워크: 기존 단일 특성 최적화를 넘어 전도도 최대화와 결함 최소화를 동시에 달성
- 고차원 처리 공간 탐색: 이전 연구의 제한된 인자(2-3개)를 넘어 7개의 처리 매개변수를 동시에 최적화
- 통계적 데이터 품질 관리: 실험 재현성 확보를 위한 체계적인 통계 방법 도입으로 소규모 데이터셋의 신뢰성 향상
- 해석 가능한 AI: 블랙박스 최적화를 넘어 특성 중요도 분석과 형태학적 특성화로 물리적 인사이트 제공

## Limitation & Further Study

- 단일 재료 시스템: PEDOT:PSS만 시험되었으므로 다른 전자 고분자 시스템에 대한 일반화 필요
- 처리 공간의 제한: 7개 매개변수로 제한되었으며, 추가 공정 변수(예: 상대 습도, 기판 종류)의 영향 미탐색
- 스케일업 검증 부족: 실험실 규모 성능이 대규모 산업 생산으로 얼마나 전이되는지 명확하지 않음
- 데이터 불확실성 원인: 고분자 처리의 본질적 비평형성(non-equilibrium)으로 인한 근본적인 예측 불확실성 존재
- 후속 연구 방향: (1) 다양한 전자 고분자 시스템 적용, (2) 공정 인자 확대 및 계층적 최적화, (3) 실시간 모니터링 센서 통합, (4) 강화학습(reinforcement learning) 등 고급 AI 알고리즘 적용

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 전자 고분자 박막 처리의 복잡한 다중 목적 최적화 문제를 자동화 실험실과 AI 알고리즘으로 체계적으로 해결한 혁신적 연구로, 자동 재료 발견(autonomous materials discovery) 분야의 중요한 진전을 보여준다. 다만 단일 재료 시스템과 제한된 처리 공간의 확대, 그리고 산업 스케일로의 전이 효과 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/1125_Accelerating_cell_culture_media_development_using_Bayesian_o/review]] — 둘 다 베이지안 최적화 기반 자동화 시스템이지만 Polybot은 전자 고분자에, 1125는 세포배양에 특화됨
- 🏛 기반 연구: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 화학기상증착의 자율 강화학습 에이전트가 고분자 처리 최적화의 자동화 접근법에 기본 아이디어를 제공함
- 🔗 후속 연구: [[papers/099_An_autonomous_laboratory_for_the_accelerated_synthesis_of_in/review]] — 무기 재료 합성 자동화 실험실과 고분자 처리 자동화를 통합하여 포괄적인 재료 개발 플랫폼 구축
- 🧪 응용 사례: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 전자 재료의 용액 공정을 위한 자율 플랫폼으로, 자율 실험실 개념의 다른 재료 과학 분야 적용
- 🔄 다른 접근: [[papers/1125_Accelerating_cell_culture_media_development_using_Bayesian_o/review]] — 둘 다 베이지안 최적화를 자동화 시스템에 활용하지만 1125는 생물학적 배지 최적화에, 1126은 전자 고분자 처리에 적용
