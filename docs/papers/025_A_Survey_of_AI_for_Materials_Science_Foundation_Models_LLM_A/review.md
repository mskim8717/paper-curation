---
title: "025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A"
authors:
  - "Minh-Hao Van"
  - "Prateek Verma"
  - "Chen Zhao"
  - "Xintao Wu"
date: "2025.06"
doi: "10.48550/arXiv.2506.20743"
arxiv: ""
score: 4.0
essence: "재료 과학(Materials Science)에서 기초 모델(Foundation Models), LLM 에이전트, 데이터셋, 도구를 종합적으로 조사한 서베이로, 과학 발견을 위한 확장 가능하고 범용적인 멀티모달 AI 시스템의 구현을 다룬다."
tags:
  - "cat/Computational_Molecular_Science_Models"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Molecular_Synthesis_Simulation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Van et al._2025_A Survey of AI for Materials Science Foundation Models, LLM Agents, Datasets, and Tools.pdf"
---

# A Survey of AI for Materials Science: Foundation Models, LLM Agents, Datasets, and Tools

> **저자**: Minh-Hao Van, Prateek Verma, Chen Zhao, Xintao Wu | **날짜**: 2025-06-25 | **DOI**: [10.48550/arXiv.2506.20743](https://doi.org/10.48550/arXiv.2506.20743)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of our survey of AI for materials science (AI4MS), highlighting common tasks, categories of*

재료 과학(Materials Science)에서 기초 모델(Foundation Models), LLM 에이전트, 데이터셋, 도구를 종합적으로 조사한 서베이로, 과학 발견을 위한 확장 가능하고 범용적인 멀티모달 AI 시스템의 구현을 다룬다.

## Motivation

- **Known**: 전통적 기계학습은 작업 특화적이고 일반화 능력이 제한적이지만, NLP와 컴퓨터 비전에서 기초 모델의 성공이 입증되었다. 재료 과학에서도 그래프 신경망(GNN), 생성 모델, LLM 기반 시스템들이 등장하고 있다.
- **Gap**: 기존 연구들은 특정 작업이나 데이터 유형에 집중했으나, 다양한 스케일과 모달리티를 통합하는 포괄적인 기초 모델 개발, 멀티모달 융합, 해석가능성, 데이터 불균형 문제가 미해결 상태이다.
- **Why**: 재료 과학은 원자 구조부터 거시적 특성까지 다양한 스케일의 멀티모달 데이터를 다루며, 기초 모델의 교차 영역 일반화 능력이 이러한 복잡성 해결에 핵심적이기 때문이다.
- **Approach**: 6가지 작업 기반 분류체계(데이터 추출, 원자 시뮬레이션, 특성 예측, 구조 설계, 프로세스 최적화, 멀티스케일 모델링)를 제시하고, 단일모달/멀티모달 기초 모델, LLM 에이전트, 표준 데이터셋, 오픈소스 도구를 종합 분석한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of our survey of AI for materials science (AI4MS), highlighting common tasks, categories of*

- **포괄적 분류체계 제시**: 재료 과학 AI의 6개 핵심 응용 영역과 기초 모델, 에이전트, 데이터셋, 도구를 통합한 체계적 분류
- **주요 성공 사례 문서화**: GNoME의 220만 개 신규 안정 재료 발견, MatterSim의 범용 원자간 포텐셜(MLIP), MatterGen 등 생성 모델의 성과 기록
- **멀티모달 모델 분석**: nach0, MultiMat, MatterChat, ATLANTIC 등 텍스트-구조-특성 데이터를 통합하는 모델들의 능력 평가
- **LLM 에이전트 동향 파악**: HoneyComb, MatAgent, ChatMOF, MatPilot 등 외부 도구와 상호작용하는 자동화 시스템의 발전
- **핵심 제약 및 미래 방향 제시**: 일반화성, 해석가능성, 데이터 불균형, 안전성, 신뢰성 문제와 확장 가능한 사전학습, 지속 학습, 데이터 거버넌스에 대한 제언

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of our survey of AI for materials science (AI4MS), highlighting common tasks, categories of*

- 작업 기반 분류법: 데이터 추출과 Q&A, 원자 시뮬레이션, 특성 예측, 구조·설계·발견, 프로세스 계획과 최적화, 멀티스케일 모델링의 6개 범주로 체계화
- 모달리티별 분석: 원자 구조, 그래프, 분자 표현(SMILES, SELFIES), DFT 계산 등 단일모달과 텍스트-이미지-스펙트럼 등 멀티모달 모델 비교
- 아키텍처 검토: 그래프 신경망(GNN), 트랜스포머, 확산 모델(Diffusion), 변분 오토인코더(VAE) 등 주요 기초 모델 구조 분석
- 에이전트 프레임워크: LLM이 외부 API, 계산 도구, 실험 플랫폼과 상호작용하는 자동화 시스템의 구조와 능력 평가
- 데이터셋 및 벤치마크 조사: 공개 데이터베이스(Materials Project, NOMAD 등), 표준화된 벤치마크, 학습 데이터셋의 규모와 품질 검토
- 도구 생태계 분석: Open MatSci ML Toolkit, FORGE, Python 라이브러리, 워크플로우 시스템 등 인프라 평가

## Originality

- **통합적 분류체계의 신규성**: 재료 과학 AI의 모든 주요 구성요소(모델, 에이전트, 데이터, 도구)를 하나의 프레임워크로 통합한 종합 서베이
- **멀티모달 융합 논의**: 텍스트, 구조, 이미지, 스펙트럼 등 이질적 재료 데이터의 통합 방식을 구체적으로 분석
- **작업 기반 분류법의 타당성**: 추상적 모델 분류보다 실제 재료 과학 연구 문제와 직접 연결되는 6개 작업 범주 정의
- **미래 연구 방향 제시**: 일반화성, 해석가능성, 안전성, 신뢰성, 데이터 거버넌스 등 기술적 과제와 사회적 과제를 균형있게 제시
- **신흥 시스템 포함**: 자동 실험실(A-Lab), 로봇 합성, 프로세스 인식 모델 등 최신 동향 반영

## Limitation & Further Study

- **데이터 부족과 불균형**: 재료 과학은 NLP의 수십억 개 레이블 데이터와 달리 고비용, 불균형 데이터에 의존하며, 이에 대한 해결책이 제한적
- **일반화 능력의 한계**: 현재 모델들이 학습 분포 외 재료(새로운 원소, 구조)에 대해 성능 저하되는 문제 미해결
- **해석가능성 부족**: 블랙박스 신경망 기반 기초 모델이 물리적 법칙(에너지 보존, 대칭성)을 정확히 따르는지 검증 어려움
- **멀티모달 융합의 미성숙**: 이종 모달리티 간 의미 있는 상호작용 학습 방법이 불충분하고, 크로스모달 일관성 유지 문제 존재
- **안전성과 신뢰성**: 합성된 재료의 실제 안전성, 독성, 환경 영향 평가 메커니즘 부재; 모델 실패 시 실험 손실 위험
- **후속 연구 필요 영역**: (1) 물리 정합성이 보장된 아키텍처 개발, (2) 소수 샘플 학습(Few-shot) 및 전이 학습 기법 강화, (3) 자동화된 품질 관리 및 실시간 재훈련 파이프라인, (4) 신뢰성 있는 불확실성 정량화, (5) 국제 표준화된 데이터 거버넌스 체계 구축

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 서베이는 재료 과학에서 기초 모델, LLM 에이전트, 데이터, 도구의 현황을 종합적이고 체계적으로 정리한 중요한 참고 자료로, 해당 분야 연구자들이 기술 현황을 빠르게 파악하고 미해결 문제를 식별하는 데 매우 유용하다.

## Related Papers

- 🧪 응용 사례: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 서베이에서 제시한 멀티모달 AI 시스템 구현 방향이 분자 문법 학습 프레임워크에 구체적으로 적용됨
- 🔗 후속 연구: [[papers/720_Scientific_Large_Language_Models_A_Survey_on_Biological__Che/review]] — 생물학 및 화학 분야 과학 언어 모델에 대한 세부 조사로 재료과학 AI 서베이를 보완함
- 🧪 응용 사례: [[papers/151_Benchmarking_ai_scientists_in_omics_data-driven_biological_r/review]] — 오믹스 데이터 기반 생물학 연구에서 AI 과학자 벤치마킹이 재료과학 AI 평가 방법론에 참고가 됨
- 🔄 다른 접근: [[papers/271_Developing_ChemDFM_as_a_large_language_foundation_model_for/review]] — 재료과학용 AI 설문과 화학 전문 LLM은 서로 다른 물리과학 도메인에서의 AI 적용을 다룬다
- 🔗 후속 연구: [[papers/015_A_Perspective_on_Foundation_Models_in_Chemistry/review]] — 재료과학을 위한 AI 조사와 화학 분야 파운데이션 모델 관점을 결합하면 화학-재료과학 융합 영역의 AI 활용 전략을 수립할 수 있다.
- 🏛 기반 연구: [[papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/review]] — 재료과학 분야 AI 기초 모델 연구가 화학 반응 예측 LLM의 이론적 토대가 된다
- 🧪 응용 사례: [[papers/856_Unimatch_Universal_matching_from_atom_to_task_for_few-shot_d/review]] — 재료과학 AI 기초 모델의 원리를 few-shot 약물 발견의 구체적 문제에 적용한다
- 🏛 기반 연구: [[papers/487_Leveraging_biomolecule_and_natural_language_through_multi-mo/review]] — 재료과학을 위한 AI 서베이가 생분자 다중모달 학습의 기반을 제공한다
- 🏛 기반 연구: [[papers/451_Knowledge-guided_large_language_model_for_material_science/review]] — 재료과학을 위한 AI 조사 연구가 지식 안내형 LLM 개발의 기초 모델과 방법론적 기반을 제공한다
- 🔗 후속 연구: [[papers/344_Foundation_models_in_bioinformatics/review]] — 재료과학을 위한 AI 설문조사와 생물정보학 기초 모델 연구는 상호 보완적인 과학 분야별 AI 적용 현황을 제공한다.
- 🏛 기반 연구: [[papers/465_Large_Language_Model_in_Materials_Science_Roles_Challenges_a/review]] — 재료 발견을 위한 AI 설문조사는 재료과학에서 LLM의 역할과 도전과제를 이해하는 포괄적 배경을 제공한다.
- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — AI와 재료과학을 위한 파운데이션 모델 서베이가 재료 발견에 특화된 파운데이션 모델의 이론적 배경을 제공한다
- 🧪 응용 사례: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 재료 발견을 위한 가설 생성이 재료과학 AI 서베이에서 제시한 LLM 에이전트 활용 방향의 구체적 사례
- 🔗 후속 연구: [[papers/115_Augmenting_large_language_models_with_chemistry_tools/review]] — AI 기반 재료과학 연구의 포괄적 조사를 통해 ChemCrow가 화학에서 보인 성과를 재료과학 전반으로 확장할 수 있는 가능성을 제시함
- 🏛 기반 연구: [[papers/345_Foundation_Molecular_Grammar_Multi-Modal_Foundation_Models_I/review]] — 재료과학 AI 시스템 구축의 포괄적 기반 지식을 제공하여 분자 문법 학습에 필요한 멀티모달 접근법 이해를 도움
- 🧪 응용 사례: [[papers/024_A_sober_look_at_llms_for_material_discovery_Are_they_actuall/review]] — 재료 과학에서 AI 조사와 LLM의 실제 유용성 평가가 재료 발견 분야의 포괄적 이해를 제공한다.
- 🏛 기반 연구: [[papers/398_Harnessing_large_language_models_for_scientific_novelty_dete/review]] — 재료 과학에서 AI/LLM 활용에 대한 포괄적 조사로, MOF 데이터 분석 연구의 이론적 기반을 제공
- 🧪 응용 사례: [[papers/524_MatViX_Multimodal_Information_Extraction_from_Visually_Rich/review]] — 재료과학 분야 AI/ML 조사 연구로, MatViX가 목표로 하는 재료과학 논문에서의 정보 추출 응용 분야에 대한 포괄적 배경을 제공한다
- 🏛 기반 연구: [[papers/701_Scholarchemqa_Unveiling_the_power_of_language_models_in_chem/review]] — 재료 과학을 위한 AI 기반 모델에 대한 종합적 조사를 통해 화학 QA 시스템의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 재료과학 기초 모델과 데이터셋 구축 방향이 위상 물질 발견을 위한 물리 기반 규칙 개발에 필수적 배경 제공
