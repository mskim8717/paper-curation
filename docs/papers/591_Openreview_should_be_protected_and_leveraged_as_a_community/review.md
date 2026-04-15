---
title: "591_Openreview_should_be_protected_and_leveraged_as_a_community"
authors:
  - "Hao Sun"
  - "Yunyi Shen"
  - "Mihaela van der Schaar"
date: "2025"
doi: "10.48550/arXiv.2505.21537"
arxiv: ""
score: 4.0
essence: "대규모 언어모델(LLM) 시대에 OpenReview 플랫폼—논문, 리뷰, 저자 반박, 메타리뷰, 최종 결정을 포함한 구조화된 전문가 피드백 저장소—을 학술 공동체의 핵심 자산으로 보호하고 활용해야 함을 주장하는 입장 논문이다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Automated_Scientific_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cowls et al._2025_Openreview should be protected and leveraged as a community asset for research in the era of large l.pdf"
---

# OpenReview Should be Protected and Leveraged as a Community Asset for Research in the Era of Large Language Models

> **저자**: Hao Sun, Yunyi Shen, Mihaela van der Schaar | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.21537](https://doi.org/10.48550/arXiv.2505.21537)

---

## Essence

![Figure 1](figures/fig1.webp)
*OpenReview 데이터 생성 과정(좌), 피어리뷰 규제, LLM 오픈-엔디드 작업 연구, 정렬 및 추론 후훈련을 지원하는 세 가지 주요 응용 분야(중), 연구 기회(우)*

대규모 언어모델(LLM) 시대에 OpenReview 플랫폼—논문, 리뷰, 저자 반박, 메타리뷰, 최종 결정을 포함한 구조화된 전문가 피드백 저장소—을 학술 공동체의 핵심 자산으로 보호하고 활용해야 함을 주장하는 입장 논문이다.

## Motivation

- **Known**: LLM 개발은 고품질의 인간-중심 피드백에 의존하나, 현재 사용되는 데이터셋은 범위가 제한적이고 합성적이며 정적 구조를 가짐. 동시에 LLM 도구의 확산으로 학술 투고 증가로 인해 피어리뷰 시스템에 극심한 부담 발생.

- **Gap**: 피어리뷰 상호작용의 풍부함을 포착할 수 있는 대규모 체계적 데이터셋과 방법론이 부재함. 합성 또는 크라우드소싱 데이터는 실제 전문가 심의의 깊이와 미묘함을 반영하지 못함.

- **Why**: OpenReview는 진정한 과학 탐구, 다양한 전문가 관점, 합의 형성 과정을 반영하는 대규모 구조화된 전문가 생성 데이터로서 고유한 기회를 제공함.

- **Approach**: OpenReview의 가치를 세 가지 영역에서 분석: (1) 피어리뷰 품질 및 확장성 개선, (2) 오픈-엔디드 작업 벤치마크 제공, (3) 과학적 가치 정렬 연구 지원.

## Achievement

![Figure 2](figures/fig2.webp)
*ICLR (2017–2025) 성장 추세: 투고 수는 500→11,600, 저자는 1,500→38,500, 리뷰어는 1,000→18,300으로 증가했으나 리뷰어 증가가 투고 증가를 따라가지 못함*

1. **규모와 구조 분석**: ICLR을 사례로 2017-2025년 간 36,000+의 상호작용 스레드, 100,000+의 리뷰 데이터 축적을 정량화. 리뷰어 부족 문제(리뷰어 증가 24-25년 약 2,000명 vs 투고 계속 증가)를 시각화.

2. **데이터셋 우월성 입증**: OpenReview를 기존 요약(See et al. 2017, 310K), 정렬/대화(Bai et al. 2022a, 170K) 등 관련 데이터셋과 비교하여 유일하게 '전문가 생성', '지속적 업데이트', '오픈-엔디드' 모두를 만족함을 Table 1에서 제시.

3. **세 가지 응용 기회 체계화**:
   - 피어리뷰 보조: 리뷰어 초안 작성, 점수 조정, 논증 갭 식별, 응답 요약 지원
   - 벤치마킹: 학술 글쓰기, 연구 평가, 설득, 요약 등 오픈-엔디드 작업 평가
   - 정렬 연구: 증거 기반 논증, 불일치 처리, 합의 구축을 통한 다차원 정렬

## How

- **데이터 특성 활용**: 구조화된 포맷(논문→리뷰 3+개→반박→메타리뷰→결정), 시간 경과에 따른 추적 가능성, 다양한 관점의 전문가 의견 포함

- **질적 우월성**: 합성 데이터가 아닌 실제 과학 진행과 연결된 평가, 실제 불일치와 합의 과정 기록

- **지속적 진화 메커니즘**: 매년 새로운 주제, 논문, 논의로 벤치마크 최신성 유지

- **LLM 활용**: 최첨단 범용 언어모델(Google DeepMind, OpenAI, Anthropic, xAI 등)이 학습할 수 있는 수준의 데이터 복잡도 제공

- **사회적 가치 포착**: 가치 다원주의(value pluralism), 논쟁식 정렬(debate-style alignment) 등 현실 과학 공동체의 가치 체계 반영

## Originality

- **새로운 관점**: 기존에 각각 논의된 피어리뷰 자동화, LLM 벤치마킹, 정렬 연구를 OpenReview라는 단일 자산으로 통합한 첫 시도

- **체계적 규모 분석**: ICLR 8년 데이터 기반의 양적 성장 분석과 리뷰어 부족 문제의 정량화

- **질적 비교**: Table 1의 존재하는 데이터셋(14개)과의 비교를 통해 OpenReview의 독특성 증명

- **구조적 위험 제시**: Wright-Fisher 모델을 활용한 훈련 부족 리뷰어의 장기적 영향 분석 (논문 일부 추출에서 언급)

## Limitation & Further Study

- **윤리적 고려사항 미흡**: 저자 프라이버시, 익명성 보호, 데이터 사용 동의 등 구체적인 윤리 가이드라인 부재

- **구현 세부사항 부족**: 벤치마크 표준화, 책임 있는 데이터 관리 메커니즘의 구체적 설계 제시 부족

- **리뷰 품질 저하 위험**: 빠르게 증가하는 미훈련 리뷰어가 편향된 관행을 내재화할 가능성에 대한 형식적 모델링이 불완전

- **대안적 관점 탐색 부족**: 논문이 긍정적 가능성에 집중하여 OpenReview 활용의 부정적 영향(저자 프라이버시 침해, 과도한 감시, 학파 편향 강화 등)에 대한 심층 논의 필요

- **후속 연구**: (1) 커뮤니티 기반 벤치마크 개발 실행, (2) 책임 있는 데이터 관리 정책 수립, (3) 다양한 분야(생물학, 물리학 등)로의 확장 검토


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 학술 공동체의 피어리뷰 데이터를 LLM 시대의 핵심 자산으로 재조명한 중요한 입장 논문이나, 윤리적 고려사항과 구현 세부사항이 보강되어야 완전한 실행 가능성을 확보할 수 있다. 특히 OpenReview 보호와 공동체적 관리 방식에 대한 구체적 제안이 후속 작업에서 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie/review]] — 피어 리뷰 데이터셋의 일관성과 품질 보장을 위한 기본 구조를 제공한다
- 🔗 후속 연구: [[papers/628_Position_The_ai_conference_peer_review_crisis_demands_author/review]] — 피어 리뷰 시스템 개선을 위한 구체적인 개혁 방안과 실행 전략을 제시한다
- 🧪 응용 사례: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — 임상 리뷰 생성에서 피어 리뷰 품질 개선의 실제 적용 사례를 보여준다
- 🧪 응용 사례: [[papers/113_Attracting_new_users_or_business_as_usual_A_case_study_of_co/review]] — OpenReview 커뮤니티 자원 보호가 오픈액세스 학술 출판의 실제적 구현 사례를 보여준다.
- 🏛 기반 연구: [[papers/628_Position_The_ai_conference_peer_review_crisis_demands_author/review]] — 피어 리뷰 시스템의 구조적 문제 해결을 위한 데이터 기반 접근의 기초를 마련한다
- 🏛 기반 연구: [[papers/244_Cross_sectional_pilot_study_on_clinical_review_generation_us/review]] — 임상 리뷰 품질 개선을 위한 피어 리뷰 시스템 활용의 기초적 접근을 제공한다
