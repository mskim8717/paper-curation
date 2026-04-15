---
title: "1106_The_BOS-Lig_Dataset_Accurate_Ligand_Charges_from_a_Consensus"
authors:
  - "Roland G. St. Michel"
  - "Ryan J. Jang"
  - "Aaron G. Garrison"
  - "Ilia Kevlishvili"
  - "Heather J. Kulik"
date: "2026"
doi: "10.48550/ARXIV.2604.06043"
arxiv: ""
score: 4.0
essence: "캠브리지 구조 데이터베이스의 126,985개 단핵 전이금속 착물에서 반복적 전하 균형 워크플로우를 통해 66,810개 리간드의 정확한 순 전하를 결정하고, 주제 모델링으로 25,146개 리간드의 기능적 응용 영역을 분류한 BOS-Lig 데이터세트를 구축했다."
tags:
  - "cat/Computational_Molecular_Science_Models"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Molecular_Synthesis_Simulation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Michel et al._2026_The BOS-Lig Dataset Accurate Ligand Charges from a Consensus Approach for 66,810 Experimentally Syn.pdf"
---

# The BOS-Lig Dataset: Accurate Ligand Charges from a Consensus Approach for 66,810 Experimentally Synthesized Ligands

> **저자**: Roland G. St. Michel, Ryan J. Jang, Aaron G. Garrison, Ilia Kevlishvili, Heather J. Kulik | **날짜**: 2026 | **DOI**: [10.48550/ARXIV.2604.06043](https://doi.org/10.48550/ARXIV.2604.06043)

---

## Essence

![Figure 4](figures/fig4.webp)

*Figure 4. Ligand charge workflow and results. a) Flowchart of the iterative procedure used to*

캠브리지 구조 데이터베이스의 126,985개 단핵 전이금속 착물에서 반복적 전하 균형 워크플로우를 통해 66,810개 리간드의 정확한 순 전하를 결정하고, 주제 모델링으로 25,146개 리간드의 기능적 응용 영역을 분류한 BOS-Lig 데이터세트를 구축했다.

## Motivation

- **Known**: 전이금속 착물(TMC)은 촉매, 광화학, 자성, 생물무기화학 분야에서 광범위하게 연구되고 있으며, 리간드는 착물의 기하학, 전자구조, 반응성을 결정하는 핵심 요소다.
- **Gap**: 결정학 데이터베이스에서 리간드의 순 전하와 응용 영역 정보가 종종 누락되거나 불일치하게 기록되어 있으며, 기존의 리간드 전하 할당 방법들은 특정 배위 기하학에만 제한되거나 일반화 능력이 부족하다.
- **Why**: 정확한 리간드 전하 할당은 고속 전산 스크리닝과 DFT 계산에서 전자구조 및 에너지 오류를 방지하기 위해 필수적이며, 리간드의 응용 영역 정보는 합리적 설계 및 스크리닝 프로토콜 개발에 중요하다.
- **Approach**: 반복적 전하 균형 워크플로우를 통해 단위 세포 전중성을 이용하여 복합 전하를 추론하고, 호모렙틱(homoleptic) 착물부터 시작하여 헤테로렙틱(heteroleptic) 환경으로 할당을 확산시키며, 논문 초록의 주제 모델링으로 리간드의 기능적 용도를 분류했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2. Count, charge and oxidation state distributions for TMCs. a) Funnel diagram illustrating*

- **포괄적 데이터세트 구축**: 94,581개의 고유 리간드 구조 중 66,810개에 대한 신뢰성 높은 순 전하 할당
- **강건한 워크플로우 개발**: 직접 전하 정보가 없을 때도 전하를 추론할 수 있는 반복적 순환 알고리즘
- **품질 관리**: 순 전칙(octet rule)이 실패하는 경우를 분석하고 순도 지표(purity metric)를 도입하여 전하 할당의 신뢰성 평가
- **배위 화학 분류**: 금속 배위 원자 정체성 및 헤미래빌성(hemilability) 변이 식별
- **응용 영역 연결**: 25,146개 리간드를 반응성, 산화환원, 생물화학, 광물리 화학의 4가지 기능 영역과 연결

## How

![Figure 1](figures/fig1.webp)

*Figure 1 and Supporting Information Table S1). Then, we enforced unit cell neutrality, inferring*

- CSD March 2024 업데이트에서 599,180개 항목을 정제하여 126,985개 단핵 TMC 추출
- Weisfeiler-Lehman 그래프 해시를 이용한 분자 성분 동일성 판별
- 267개의 공통 비금속 분자에 대한 수동 전하 정의로 시드 집합 구성
- 단위 세포 전중성 조건을 이용한 반복적 전하 해결 알고리즘 적용
- 호모렙틱 착물에서 리간드 전하 우선 할당 후 가중치 기반 확산
- 저널 초록의 자연언어처리 및 주제 모델링으로 응용 영역 분류
- 불확실성 케이스에 대한 순도 지표 계산 및 신뢰도 평가

## Originality

- 단위 세포 전중성을 이용한 반복적 전하 추론 방법의 대규모 적용 (cell2mol의 한계 극복)
- 호모렙틱→헤테로렙틱 순차 할당을 통한 간접 전하 정보 활용의 창의적 전략
- 결정학 데이터와 문헌 정보(주제 모델링)를 통합한 리간드-중심의 다층적 특성화
- 리간드의 전문성(specificity) 정량화를 통한 광범위 재사용 vs. 특화된 분자 구분

## Limitation & Further Study

- 전하 할당 확신도가 66,810/94,581(70.7%)에 불과하며, 나머지 27,771개 리간드는 미할당 상태
- 주제 모델링으로 기능 영역을 할당한 리간드는 38,115개 중 25,146개(65.9%)로, 데이터 커버리지 제한
- 순도 지표가 불확실한 전하 할당을 식별하지만, 거짓 양성 제거 메커니즘 부족
- 다핵(polynuclear) 착물과 액티나이드/란탄족 원소 함유 착물은 제외되어 화학 공간의 일부만 커버
- 후속 연구: 머신러닝 모델 개선으로 미할당 리간드의 전하 예측, 다중 레이블 분류 정밀도 향상, 계산 검증을 위한 DFT 계산 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 연구는 결정학 데이터의 부정확성과 불완전성 문제를 체계적으로 해결하여 66,810개 리간드의 신뢰성 높은 전하 정보와 기능적 분류를 제공함으로써, 전이금속 착물의 전산 스크리닝과 데이터 기반 리간드 설계를 위한 탄탄한 기초를 마련했다.

## Related Papers

- 🧪 응용 사례: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — BOS-Lig 데이터셋의 정확한 전하 정보가 위상 물질의 전자 채움 특성 예측에 직접 활용됨
- 🔗 후속 연구: [[papers/165_Biokgbench_A_knowledge_graph_checking_benchmark_of_ai_agent/review]] — 바이오메디컬 지식 그래프 검증 프레임워크를 리간드 전하 검증 워크플로우에 적용하여 정확도 향상 가능
- 🧪 응용 사례: [[papers/646_QH9_A_Quantum_Hamiltonian_Prediction_Benchmark_for_QM9_Molec/review]] — 양자 해밀톤 예측에서 정확한 리간드 전하 데이터가 전이금속 착물의 전자구조 계산 정확도를 높임
- 🧪 응용 사례: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 정확한 리간드 전하 데이터가 위상 물질 발견의 화학 규칙에서 전자 채움 예측 정확도를 향상시킴
