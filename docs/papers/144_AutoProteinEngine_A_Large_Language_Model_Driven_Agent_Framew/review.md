---
title: "144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew"
authors:
  - "Yungeng Liu"
  - "Zan Chen"
  - "Yu Guang Wang"
  - "Yiqing Shen"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "단백질 공학 분야에 특화된 대규모 언어 모델(LLM) 기반 자동화 머신러닝(AutoML) 프레임워크를 제시하여, 딥러닝 전문 지식이 없는 생물학자들도 자연언어로 단백질 엔지니어링 작업을 수행할 수 있도록 한 혁신적 시스템이다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Multimodal_Protein_Reasoning_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_AutoProteinEngine A Large Language Model Driven Agent Framework for Multimodal AutoML in Protein En.pdf"
---

# AutoProteinEngine: A Large Language Model Driven Agent Framework for Multimodal AutoML in Protein Engineering

> **저자**: Yungeng Liu, Zan Chen, Yu Guang Wang, Yiqing Shen | **날짜**: 2024 | **DOI**: [미제공](https://doi.org/)

---

## Essence

단백질 공학 분야에 특화된 대규모 언어 모델(LLM) 기반 자동화 머신러닝(AutoML) 프레임워크를 제시하여, 딥러닝 전문 지식이 없는 생물학자들도 자연언어로 단백질 엔지니어링 작업을 수행할 수 있도록 한 혁신적 시스템이다.

## Motivation

- **Known**: ESM, AlphaFold 등 딥러닝 모델은 단백질 구조 예측 및 단백질 엔지니어링 성능 향상에 효과적이며, AutoML은 머신러닝 모델 개발 자동화에 성공

- **Gap**: 기존 AutoML 프레임워크는 여전히 높은 딥러닝 및 프로그래밍 전문성을 요구하며, 단백질 시퀀스-구조 그래프의 멀티모달 데이터 처리 불가능

- **Why**: 생물학 배경의 연구자들은 초매개변수 최적화, 데이터 전처리, 모델 아키텍처 이해에 어려움을 겪으며, 멀티모달 단백질 데이터 처리의 복잡성이 진입장벽 상승

- **Approach**: LLM 에이전트를 핵심으로 자연언어 인터페이스, 멀티모달 AutoML, 자동 하이퍼파라미터 최적화(HPO), 자동 데이터 검색을 통합한 통합 프레임워크 개발

## Achievement

![Figure 1: AutoProteinEngine 프레임워크 개요](figures/fig1.webp)
*Figure 1: 자연언어 작업 명세부터 AutoML 실행, 자동 데이터 검색까지의 엔드-투-엔드 워크플로우*

1. **멀티모달 AutoML 프레임워크**: 단백질 시퀀스(ESM 시리즈)와 구조 그래프 데이터를 모두 처리 가능한 최초의 전문화된 AutoML 시스템으로, 레이트 퓨전(late fusion) 전략으로 멀티모달 정보 통합

2. **자동화된 하이퍼파라미터 최적화**: Tree-structured Parzen Estimator(TPE)와 Asynchronous Successive Halving Algorithm(ASHA)을 결합하여 효율적 하이퍼파라미터 탐색 및 동적 리소스 할당 달성

3. **자동 데이터 검색 모듈**: 자연언어 입력을 PDB, UniProt 데이터베이스 쿼리로 자동 변환하여 구조화된 데이터 획득 및 상호작용 기반 데이터 완성도 보증

4. **실무 검증**: Brazzein(분류), Arylsulfatase A(회귀) 두 단백질 엔지니어링 작업에서 영점 샷(zero-shot) 및 수동 미세조정(manual fine-tuning) 대비 현저한 성능 향상 입증

## How

![Figure 2: 대화형 인터페이스 작업 흐름](figures/fig2.webp)
*Figure 2: AutoPE 대화형 인터페이스와 기존 코드 기반 딥러닝 워크플로우 비교*

### LLM 기반 AutoML 모듈
- **작업 검증**: 사용자 자연언어 입력을 프롬프팅으로 AutoPE 기능 범위(단백질 안정성, PPi, 효소 활성, 돌연변이 예측) 내 유효성 검토
- **계획 수립**: 검색강화생성(RAG)으로 단백질 공학 문헌 통합 및 데이터 전처리, 모델 선택, 구성 전략 수립
- **데이터 전처리**: 불완전 데이터 시 자동 데이터 검색 모듈 활성화로 온라인 데이터소스 보충
- **모델 선택 및 구성**: 사전정의된 모델 동물원에서 적절 모델 선택, 멀티모달 데이터의 경우 레이트 퓨전 방식 적용
- **훈련 최적화**: LLM이 손실함수, 배치 크기, 학습률, 조기 중단(early stopping), 모델 체크포인팅 자동 선정 및 시퀀스 무작위 돌연변이, 그래프 섭동 등 작업 특화 데이터 증강 적용

### 자동 하이퍼파라미터 최적화
- TPE 알고리즘으로 확률 모델링: $x^* = \arg\max_x \frac{l(x)}{g(x)}$ (고성능/저성능 가능도 함수)
- ASHA 스케줄러로 다중 충실도 리소스 할당: $r_i = r_{min} \cdot \eta^i$, $n_i = \lceil \frac{n}{\eta^i} \rceil$
- Ray.Tune 관리하에 LLM이 사용자 입력 확인 및 최적화 과정 자연언어 요약으로 해석성 향상

### 자동 데이터 검색
- 자연언어를 구조화 쿼리로 변환 (예: "human insulin" → UniProt/PDB 정규 쿼리)
- 미회수 데이터 발생 시 LLM 기반 상호작용 대화로 대체 옵션 제시
- 사용자 수동 입력 및 검증 인터페이스로 미공개 데이터 통합 가능

## Originality

- **최초성**: 단백질 엔지니어링 전문화 멀티모달 AutoML의 첫 시스템으로, 시퀀스-구조 그래프 모두 처리
- **혁신성**: LLM 에이전트를 AutoML 자동화의 중심축으로 설정하여 자연언어 사용자 인터페이스 실현
- **통합성**: 작업 검증, 데이터 검색, HPO, 멀티모달 모델 선택을 일관되게 통합한 엔드-투-엔드 파이프라인
- **실용성**: 도메인 지식 미보유 사용자의 접근성 대폭 개선 및 Ray.Tune 활용 실제 리소스 효율화

## Limitation & Further Study

- **평가 범위 제한**: 두 가지 단백질만으로 검증하여 다양한 단백질 엔지니어링 작업(항체 설계, 단백질-약물 상호작용 등)에 대한 일반화성 미흡
- **LLM 의존성**: 프롬프트 엔지니어링 품질이 성능을 크게 좌우할 가능성 높으며, 모델의 할루시네이션(hallucination) 위험성 미상세 검토
- **멀티모달 융합**: 레이트 퓨전의 단순성으로 시퀀스-구조 정보의 상호작용 학습 제한 가능
- **데이터베이스 의존성**: PDB/UniProt의 데이터 가용성과 품질에 의존하며, 신규/미등록 단백질 처리 능력 불명확
- **후속 연구**: (1) 어리-퓨전(early fusion) 또는 크로스 모달 어텐션 등 고급 멀티모달 학습 기법 도입, (2) 대규모 단백질 엔지니어링 벤치마크에 기반한 광범위 검증, (3) LLM 프롬프트 최적화 및 불확실성 정량화, (4) 실험실 검증 및 실제 단백질 설계 프로젝트 적용


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.2/5

**총평**: AutoProteinEngine은 LLM 기반 자동화를 통해 단백질 공학에서 계산 전문성의 진입장벽을 획기적으로 낮춘 혁신적 시스템이다. 멀티모달 데이터 처리와 자동화된 HPO는 강점이나, 한정된 실험 검증과 LLM 신뢰성 이슈가 현장 도입의 과제로 남아 있다. 더 광범위한 단백질 엔지니어링 작업에 대한 검증과 실험실 협업 사례가 추가되면 학문적·산업적 영향력이 대폭 상승할 것으로 기대된다.

## Related Papers

- 🏛 기반 연구: [[papers/543_Mlcopilot_Unleashing_the_power_of_large_language_models_in_s/review]] — LLM의 기계학습 자동화 능력을 보여주어 단백질 공학에서 AutoML 프레임워크 구축의 기술적 기반을 제공함
- 🔗 후속 연구: [[papers/112_Atomically_accurate_de_novo_design_of_antibodies_with_RFdiff/review]] — 원자 수준의 정확한 항체 설계 방법을 제시하여 AutoProteinEngine의 단백질 엔지니어링 범위를 더 정밀한 분자 수준으로 확장함
- 🏛 기반 연구: [[papers/240_Crispr-gpt_An_llm_agent_for_automated_design_of_geneediting/review]] — 단백질 엔지니어링을 위한 LLM 기반 에이전트 프레임워크를 CRISPR 실험 설계의 기반 기술로 활용한다
