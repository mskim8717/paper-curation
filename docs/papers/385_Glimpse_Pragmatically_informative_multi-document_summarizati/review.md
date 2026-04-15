---
title: "385_Glimpse_Pragmatically_informative_multi-document_summarizati"
authors:
  - "Maxime Darrin"
  - "Ines Arous"
  - "Pablo Piantanida"
  - "Jackie Chi Kit Cheung (MILA"
  - "McGill University 등)"
date: "2024"
doi: "arXiv:2406.07359"
arxiv: ""
score: 4.1
essence: "학술 동료 평가(peer review) 과정에서 영역 의장(area chair)이 다수의 리뷰를 효율적으로 처리하도록 돕기 위해, 합의(consensus)만이 아닌 공통점과 고유한 의견을 모두 추출하는 차별적 다중 문서 요약(discriminative multi-document summarization) 방법인 GLIMPSE를 제안한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Veletsianos et al._2024_Glimpse Pragmatically informative multi-document summarization for scholarly reviews.pdf"
---

# Glimpse: Pragmatically informative multi-document summarization for scholarly reviews

> **저자**: Maxime Darrin, Ines Arous, Pablo Piantanida, Jackie Chi Kit Cheung (MILA, McGill University 등) | **날짜**: 2024 | **DOI**: [arXiv:2406.07359](https://arxiv.org/abs/2406.07359)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 학술 리뷰에 적용된 RSA 기반 점수의 예시. 공통 의견은 파란색, 고유한 의견은 빨간색으로 강조됨*

학술 동료 평가(peer review) 과정에서 영역 의장(area chair)이 다수의 리뷰를 효율적으로 처리하도록 돕기 위해, 합의(consensus)만이 아닌 공통점과 고유한 의견을 모두 추출하는 차별적 다중 문서 요약(discriminative multi-document summarization) 방법인 GLIMPSE를 제안한다.

## Motivation

- **Known**: 컨퍼런스 투고 건수 증가(ICLR과 ACL은 2017년 이후 5배 증가)로 인해 동료 평가 과정의 부담이 급증하고 있으며, 기존 요약 방법들은 합의 기반의 공통 의견만을 추출함

- **Gap**: 기존 다중 문서 요약 기법(주제, 감정 극성, 중심성 기반)은 피어 리뷰 도메인의 핵심 요구사항인 "검토자 간의 공통점, 차이점, 발산된 의견"을 동시에 반영하지 못함

- **Why**: 영역 의장은 종이의 강점과 약점을 모두 파악해야 하므로, 단순히 합의된 의견뿐만 아니라 각 리뷰의 고유한 관점을 이해해야 함

- **Approach**: 언어 화행론의 Rational Speech Act(RSA) 프레임워크를 "참조 게임(reference game)" 문제로 재해석하여, 각 리뷰를 다른 리뷰들과 구별하는 차별적 요약을 생성

## Achievement

1. **새로운 문제 정의**: 차별적 다중 문서 요약(D-MDS) 과제를 참조 게임으로 형식화하고, 각 리뷰에 대해 다른 리뷰들로부터 그것을 식별 가능하게 하는 요약 생성

2. **RSA 기반 점수 개발**: 정보성(informativeness)과 고유성(uniqueness)을 측정하는 두 가지 새로운 RSA 기반 점수 도입으로, 기존 합의 기반 방식보다 판별력 있는 요약 생성

3. **실증적 검증**: ICLR 4년간의 실제 피어 리뷰 데이터셋으로 평가하여, 자동 메트릭과 인간 평가에서 기존 방법보다 우수한 판별력 달성

## How

![Figure 2](figures/fig2.webp)
*그림 2: 모든 기저선 대비 판별력 비교*

- **RSA 프레임워크 적용**: 
  - 청자(listener) 모델: P(d|s) = 리뷰 d가 요약 s와 일치할 확률
  - 화자(speaker) 모델: 정보성과 길이의 트레이드오프 고려하여 최적 요약 선택
  
- **점수 정의**:
  - 정보성(informativeness): RSA 화자 모델을 기반으로 문장이 특정 리뷰를 얼마나 잘 구별하는지 측정
  - 고유성(uniqueness): 다른 리뷰들과의 차이를 강조하여 발산된 의견 포착

- **두 가지 구현 변형**:
  - 추출적(extractive): 기존 문장 선택
  - 추상적(abstractive): 선택된 문장으로부터 새로운 텍스트 생성

- **집계 전략**: 각 리뷰별로 개별 요약을 생성하고, 전체 요약 집합을 구성하여 영역 의장에게 포괄적 관점 제공

## Originality

- 다중 문서 요약 문제를 참조 게임으로 처음 형식화하고 RSA를 적용한 연구
- 피어 리뷰 도메인에 특화된 "고유성(uniqueness)" 개념 도입으로 기존 합의 기반 접근과 차별화
- 속성성(attributability)과 투명성을 보장하여 각 요약을 특정 리뷰와 연결 가능하게 설계
- 실제 학술 피어 리뷰 데이터에 대한 실증적 평가 제공

## Limitation & Further Study

- **한계**: 
  - 추상적 변형에서는 생성된 텍스트의 충실성(faithfulness) 검증이 제한적
  - 영역 의장의 실제 의사결정 과정에 미치는 영향에 대한 직접적 평가 부재
  - 소수 리뷰(예: 2-3개)만 있는 경우의 효과성이 검증되지 않음

- **후속 연구**:
  - 메타 리뷰 생성 단계와의 통합 방안 탐색
  - 대규모 언어 모델(LLM)과의 결합 가능성
  - 다른 학문 분야(의학, 공학 등)로의 일반화 검증


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4.1/5

**총평**: 동료 평가 과정의 효율성을 높이기 위해 언어 화행론의 이론을 창의적으로 적용한 실용적이고 참신한 연구로, 특히 피어 리뷰라는 구체적 도메인에서의 실증적 검증이 강점이다. 다만 실제 영역 의장의 의사결정에 미치는 영향에 대한 심화 평가와 대규모 도입 가능성 검토가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 다중 문서 요약에서 차별적 접근법과 구조화된 요약 생성이라는 서로 다른 전략을 제시한다.
- 🧪 응용 사례: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 차별적 다중 문서 요약 기법이 피어리뷰 프로세스에서 검토자 의견 분석에 실제 적용된다.
- 🔗 후속 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 체크리스트 기반 메타리뷰 생성과 차별적 요약이 리뷰 품질 향상을 위한 상호 보완적 방법을 제공한다.
- 🏛 기반 연구: [[papers/519_MARG_Multi-Agent_Review_Generation_for_Scientific_Papers/review]] — 다중 에이전트 리뷰 생성에서 합의와 차이점 추출이라는 핵심 방법론을 공유한다.
- 🔄 다른 접근: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 다중 문서 요약에서 구조화된 접근법과 차별적 요약 방식이라는 서로 다른 전략을 제시한다.
- 🏛 기반 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 다중 문서 요약 기법이 피어리뷰 프로세스에서 여러 검토자 의견의 통합적 분석을 위한 토대를 제공한다.
