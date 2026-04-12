---
title: "1075_Open_Catalyst_2020_OC20_Dataset_and_Community_Challenges"
authors:
  - "Lowik Chanussot"
  - "Abhishek Das"
  - "Siddharth Goyal"
  - "Thibaut Lavril"
  - "Muhammed Shuaibi"
date: "2021.05"
doi: "10.1021/acscatal.0c04525"
arxiv: ""
score: 4.0
essence: "촉매 발견을 위한 1.2백만 개의 DFT 계산 데이터로 구성된 Open Catalyst 2020 (OC20) 데이터셋을 제시하고, 그래프 신경망 기반 베이스라인 모델과 커뮤니티 챌린지를 제공한다."
tags:
  - "cat/AI-Assisted_Scientific_Discovery"
  - "sub/Knowledge_Graphs_and_Data_Integration"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chanussot et al._2021_Open Catalyst 2020 (OC20) Dataset and Community Challenges.pdf"
---

# Open Catalyst 2020 (OC20) Dataset and Community Challenges

> **저자**: Lowik Chanussot, Abhishek Das, Siddharth Goyal, Thibaut Lavril, Muhammed Shuaibi, Morgane Riviere, Kevin Tran, Javier Heras-Domingo, Caleb Ho, Weihua Hu, Aini Palizhati, Anuroop Sriram, Brandon Wood, Junwoong Yoon, Devi Parikh, C. Lawrence Zitnick, Zachary Ulissi | **날짜**: 2021-05-21 | **DOI**: [10.1021/acscatal.0c04525](https://doi.org/10.1021/acscatal.0c04525)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Adsorbates, materials, calculations,*

촉매 발견을 위한 1.2백만 개의 DFT 계산 데이터로 구성된 Open Catalyst 2020 (OC20) 데이터셋을 제시하고, 그래프 신경망 기반 베이스라인 모델과 커뮤니티 챌린지를 제공한다.

## Motivation

- **Known**: 촉매 최적화는 재생에너지 및 환경 문제 해결에 필수적이지만, 기존 촉매 관련 데이터셋은 다른 분야 대비 매우 작아 머신러닝 모델의 일반화 성능이 제한적이다.
- **Gap**: 촉매 모델링을 위한 충분히 큰 규모의 다양한 원소 조성, 표면, 흡착질을 포함한 DFT 데이터셋이 부재하여, 머신러닝 모델의 일반화 능력 향상이 어렵다.
- **Why**: 대규모 고품질 데이터셋은 머신러닝 모델의 정확성과 일반화 능력을 향상시킬 수 있으며, 이는 재생 연료 합성, 에너지 저장, 비료 생산 등 사회적 과제 해결에 중요하다.
- **Approach**: Materials Project에서 안정적인 재료를 선별하여 55개 원소의 저 밀러 지수 면들에 82개의 흡착질을 배치한 후 DFT 이완 계산을 수행하고, 분자동역학 궤적과 전자구조 분석 정보를 추가로 포함하여 대규모 데이터셋을 구성한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: The adsorbates used to generate the Open Catalyst Dataset contain oxygen, hydrogen, C1,*

- **대규모 데이터셋 구축**: 1,281,040개의 DFT 이완 계산 (~264,890,000 단일점 평가)을 포함하는 OC20 데이터셋 개발
- **포괄적 화학 공간 커버**: 82개의 흡착질(N, C, O 화학), 55개 원소 조성의 다양한 표면 포함
- **보강된 데이터 제공**: 무작위 섭동 구조, 고온 분자동역학 궤적, Bader 전하 및 LOBSTER 궤도 정보 포함
- **3가지 핵심 작업 정의**: S2EF(구조→에너지/힘), IS2RS(초기→이완 구조), IS2E(초기→이완 에너지) 과제 설정
- **베이스라인 모델 제공**: CGCNN, SchNet, DimeNet++ 등 3개 최신 그래프신경망 모델의 벤치마크 결과 제시
- **개방형 자원 제공**: 데이터셋, 소프트웨어 저장소, 리더보드를 공개하여 커뮤니티 참여 유도

## How


- Materials Project의 구조 데이터베이스에서 안정적인 결정 구조 선별
- 각 재료에 대해 저 밀러 지수 표면(예: 100, 110, 111면)을 무작위 샘플링
- 선택된 각 표면에 82개 흡착질을 다양한 위치에 배치
- DFT 계산을 이용한 구조 이완(relaxation) 수행 및 에너지/힘 데이터 수집
- 이완 궤적 전체 저장 및 중간 구조에서 무작위 섭동 적용
- 일부 구조에 대해 고온 ab initio 분자동역학 시뮬레이션 수행
- 전자구조 정보(Bader 전하, LOBSTER 궤도)를 계산하여 추가 특성 제공
- Train/Validation/Test 분할을 이전의 미확인 흡착질, 미확인 재료 조성, 또는 둘 다를 예측하는 시나리오로 설정

## Originality

- 촉매 분야에서 이전 O(100,000) 규모를 넘어 처음으로 O(1,000,000) 이상의 대규모 DFT 데이터셋 구축
- 단순 이완 에너지를 넘어 이완 전체 궤적, 전자구조 정보, 섭동 구조 등 다양한 데이터 형태 포함
- 세 가지 계층적으로 연관된 실질적인 촉매 모델링 작업 정의 및 명확한 평가 프레임워크 제공
- 공개 소프트웨어, 베이스라인 모델, 리더보드를 통해 커뮤니티 주도의 경쟁 기반 개발 환경 조성

## Limitation & Further Study

- **단순화된 모델링**: 단일 흡착질과 이상화된 표면 구조만 고려하며, 반응 조건, 용매화 효과, 반응 동역학 등 실제 촉매 복잡성 미포함
- **희박한 샘플링**: 가능한 모든 촉매 공간의 극히 일부만 다루고 있어 외삽(extrapolation) 성능 제한 가능
- **계산 방법 제약**: DFT를 기반으로 하므로 DFT의 내재적 오차(xc-functional 선택 등)가 데이터에 반영됨
- **후속연구 방향**: 다중 흡착질 상호작용, 온도/압력 효과, 용매 효과, 반응 경로 예측, 실험 검증 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: OC20은 촉매 분야의 머신러닝 연구를 획기적으로 촉진할 수 있는 대규모 고품질 데이터셋으로, 명확한 작업 정의, 공개 자원, 커뮤니티 챌린지를 통해 재생에너지 촉매 발견의 가속화에 중요한 기여를 한다.

## Related Papers

- 🔄 다른 접근: [[papers/1070_Challenges_in_High-Throughput_Inorganic_Materials_Prediction/review]] — 고처리량 재료 예측에서 촉매 발견과 무기재료의 다른 접근법과 과제를 다룸
- 🔄 다른 접근: [[papers/980_Linking_Global_Science_Funding_to_Research_Publications/review]] — 과학 연구와 자금 지원의 연결에서 촉매 데이터셋과 글로벌 자금-출판 매핑의 다른 접근법임
- 🔄 다른 접근: [[papers/1228_OpenRad_a_Curated_Repository_of_Open-access_AI_models_for_Ra/review]] — AI 모델의 오픈 접근에서 촉매 발견과 방사선학의 다른 과학 영역 접근법임
- 🔗 후속 연구: [[papers/1051_Unsupervised_Word_Embeddings_Capture_Latent_Knowledge_from_M/review]] — 재료과학 텍스트 마이닝과 촉매 발견 데이터셋을 결합하여 더 강력한 AI 모델 개발 가능
- 🔗 후속 연구: [[papers/1082_The_Open_Catalyst_2022_OC22_Dataset_and_Challenges_for_Oxide/review]] — Open Catalyst 데이터셋을 OC20에서 OC22로 확장하여 산화물 전기촉매까지 포함함
- 🧪 응용 사례: [[papers/1195_Mapping_the_Research_Landscape_of_Electronic_Properties_of_G/review]] — 그래핀 전자 특성 연구의 bibliometric 분석이 촉매 연구 데이터셋과 커뮤니티 챌린지에서 실제 적용될 수 있다.
