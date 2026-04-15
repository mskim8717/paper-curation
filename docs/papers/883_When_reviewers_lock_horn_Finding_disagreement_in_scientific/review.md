---
title: "883_When_reviewers_lock_horn_Finding_disagreement_in_scientific"
authors:
  - "Sandeep Kumar"
  - "Tirthankar Ghosal"
  - "Asif Ekbal"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 과학 논문의 피어 리뷰 과정에서 리뷰어 간의 모순(disagreement)을 자동으로 탐지하는 새로운 과제를 제시하고, 이를 위한 대규모 데이터셋 ContraSciView와 기준 모델을 제안한다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kumar et al._2023_When reviewers lock horn Finding disagreement in scientific peer reviews.pdf"
---

# When reviewers lock horn: Finding disagreement in scientific peer reviews

> **저자**: Sandeep Kumar, Tirthankar Ghosal, Asif Ekbal | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) 
*Figure 1: 리뷰어 간 모순의 예시 - Reviewer 1은 증거가 강하고 충분하다고 평가하지만, Reviewer 2는 그 증거에 회의적*

본 논문은 과학 논문의 피어 리뷰 과정에서 리뷰어 간의 모순(disagreement)을 자동으로 탐지하는 새로운 과제를 제시하고, 이를 위한 대규모 데이터셋 ContraSciView와 기준 모델을 제안한다.

## Motivation

- **Known**: 피어 리뷰는 과학 출판의 핵심 검증 메커니즘이지만, 비투명성, 편향성, 불일치성 등의 문제를 지속적으로 지적받고 있다. 특히 AI 최상위 학회(ICLR, NeurIPS)의 급증하는 투고로 인해 에디터/의장이 리뷰어 간 합의를 중재하는 데 상당한 노력을 기울이고 있다.

- **Gap**: 리뷰어 간의 모순을 자동으로 탐지하는 연구가 전무한 상태. 기존 모순 탐지 연구는 일반 텍스트나 루머, 온라인 리뷰 등에 제한되어 있으며, 도메인 전문성이 요구되는 학술 피어 리뷰 데이터에는 적용되지 않음.

- **Why**: 리뷰어의 서로 다른 작문 스타일, 전문성, 언어 능력으로 인한 모순 탐지는 복잡한 문제이며, 에디터의 수작업 부담 감소와 공정한 의사결정을 위해 자동화 도구가 필요함.

- **Approach**: (1) ICLR(2017-2020)과 NeurIPS(2016-2019) 데이터로부터 약 8.5k 논문, 28k 리뷰 쌍 기반 ContraSciView 데이터셋 구축, (2) 8개 측면 카테고리(Motivation, Clarity, Soundness 등)와 감정(긍정/부정) 레이블링을 통한 모순 정의, (3) 측면-감정 모델과 모순 분류기 기반의 2단계 기준 모델 제안.

## Achievement

![Figure 2](figures/fig2.webp) 
*Figure 2: 측면별 모순 주석 통계 - Clarity 측면에서 가장 많은 모순 발생*

1. **첫 번째 자동화 작업 수행**: 피어 리뷰 모순 탐지를 처음으로 정형화하고 자동 탐지 시스템 개발. 이는 학술 출판 분야의 AI 적용 범위를 확장함.

2. **고품질 대규모 데이터셋 구축**: 8.5k 논문, 25.8k 리뷰, 28.5k 리뷰 쌍으로 구성된 ContraSciView 데이셋 공개. 4년 이상 연구 경험을 가진 박사과정 학생 6명과 10년 이상 경험의 전문가 2명이 주석 작성(Cohen's kappa = 0.62, substantial agreement).

3. **리뷰어 간 불일치 패턴 분석**: Clarity 측면에서 가장 많은 모순(전문성, 도메인 지식, 언어 능력 차이 등), Replicability와 Meaningful Comparison에서는 적은 모순 발견.

## How

![Figure 3](figures/fig3.webp) 
*Figure 3: 제안된 기준 모델의 흐름도 - SDAP(Sentiment Disparity Aspect Pair) 추출 후 모순 여부 판정*

### 데이터셋 구축 방법
- ASAP-Review 데이터셋에서 ICLR과 NeurIPS 논문 8,582개 선정
- n개 리뷰 보유 논문에서 C(n,2) 쌍 생성으로 28k 리뷰 쌍 구성
- 모순 정의: 같은 측면에서 반대 감정을 표현하는 리뷰 쌍 코멘트

### 주석 프로세스
- 기본 모순 정의: De Marneffe et al. (2008) 채택 - "두 문장이 동시에 참일 가능성이 매우 낮은가?"
- 2단계 전문가 검토 + 6시간 일일 제한으로 주석자 피로도 관리
- 분쟁 발생 시 10년+ 경험 전문가가 최종 판단

### 기준 모델 구조
- **Aspect Sentiment Model**: Multi-Instance Multi-Label Learning Network(MIMLL) 사용
  - 측면 카테고리 탐지(ACD)와 측면 감정 분석(ACSA)을 동시 수행
  - 문장 내 핵심 단어 식별하여 각 측면별 감정 예측

- **Sentiment Disparity Aspect Pair(SDAP) 추출**: 같은 측면이지만 반대 감정의 코멘트 쌍 식별

- **Contradiction Classifier**: SDAP 쌍을 입력으로 최종 모순 여부 판정

## Originality

- **첫 번째 시도**: 피어 리뷰에 특화된 모순 탐지 작업 및 데이터셋 공개 (기존 연구는 일반 NLI, 온라인 리뷰, 루머 등에만 적용)

- **도메인 특화 데이터셋**: 학술 출판의 8개 표준화된 측면 카테고리와 감정 레이블을 포함한 고품질 주석

- **현실적 적용 가능성**: 에디터/의장의 실제 업무 부담 감소에 직결되는 실용적 과제 정의

- **엄격한 주석 절차**: 전문 경험이 풍부한 주석자 선정, 다단계 학습, 전문가 감수를 통한 데이터 품질 보증

## Limitation & Further Study

- **해석 가능성 부족**: 기준 모델이 모순을 탐지하는 메커니즘에 대한 심화 분석 부재. 어떤 언어적/의미적 특징이 모순을 야기하는지 불명확.

- **제한된 도메인**: ICLR과 NeurIPS만 포함되어 있어 다른 분야의 학술 리뷰(생물학, 화학 등)로의 일반화 가능성 미불명.

- **모순의 미묘한 차이**: 일부 모순은 완전히 반대되는 의견이 아닌 정도(degree)의 차이로 인한 것인데, 현 정의로는 이를 구분하기 어려움.

- **후속 연구 방향**:
  - 계층적/세밀한 모순 분류 체계 개발
  - BERT 등 사전학습 모델의 성능 벤치마킹
  - 모순의 근본 원인 분석(전문성 차이, 주관적 해석 등)
  - 다중 리뷰(3명 이상)의 합의 도출 문제로 확장
  - 컨텍스트 기반 모순 탐지(리뷰의 순서, 시간 정보 반영)

## Evaluation

- **Novelty**: 4.5/5
  - 피어 리뷰 도메인에서 처음 시도된 과제이며 공개 데이터셋 제공이 의의 있음
  - 다만 모순 탐지 자체는 기존 기법의 응용 범위에 있음

- **Technical Soundness**: 3.5/5
  - 기준 모델이 MIMLLN 등 기존 기법의 조합이며 특별한 기술 혁신 부재
  - 주석 프로세스는 견고하나, 모델 평가 및 비교 분석 상세도 낮음
  - Cohen's kappa 0.62는 substantial이지만 높은 수준은 아님

- **Significance**: 4/5
  - 학술 출판의 실제 문제 해결에 기여할 수 있는 높은 잠재력
  - 에디터와 저자들의 의사결정 지원 도구로 활용 가능
  - 다만 시스템이 보조 도구임을 강조하며 한계 명시

- **Clarity**: 4/5
  - 논문 구조와 방법론 설명이 명확함
  - 주석 지침과 프로세스 상세 기술
  - 일부 모순의 정의와 경계 사례에 대한 예시 부족

- **Overall**: 4/5

**총평**: 피어 리뷰 프로세스에서 리뷰어 간 모순을 자동으로 탐지하는 새로운 과제를 개척한 의의 있는 연구로, 정교하게 구축된 고품질 데이터셋과 현실적 적용 가치가 강점이다. 다만 기준 모델의 기술적 혁신이 제한적이고, 평가 분석의 깊이를 높인다면 학술 출판 커뮤니티의 큰 관심을 받을 수 있을 것으로 판단된다.

## Related Papers

- 🔗 후속 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 리뷰어 간 모순 탐지를 다중 턴 대화 형태의 피어 리뷰 시스템으로 발전시킨다
- 🔄 다른 접근: [[papers/676_Reviewagents_Bridging_the_gap_between_human_and_ai-generated/review]] — 자동 모순 탐지와 AI 생성 리뷰 품질 평가가 서로 다른 방식으로 피어 리뷰 개선을 추구한다
