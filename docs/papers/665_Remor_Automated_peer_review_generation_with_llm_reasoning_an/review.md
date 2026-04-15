---
title: "665_Remor_Automated_peer_review_generation_with_llm_reasoning_an"
authors:
  - "Pawin Taechoyotin"
  - "Daniel Acuna"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 추론(reasoning) 기능을 갖춘 대형언어모델(LLM)과 다목적 강화학습(MORL)을 결합하여 인간 수준 이상의 깊이 있고 균형잡힌 학술 논문 심사평을 자동 생성하는 REMOR 시스템을 제안한다. 기존 AI 심사평의 얕은 분석과 과도한 칭찬 문제를 다목적 보상함수와 추론 능력으로 극복한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Reinforcement_Learning_Control_Systems"
  - "sub/Human-LLM_Review_Semantics"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Taechoyotin and Acuna_2025_Remor Automated peer review generation with llm reasoning and multi-objective reinforcement learnin.pdf"
---

# Remor: Automated peer review generation with llm reasoning and multi-objective reinforcement learning

> **저자**: Pawin Taechoyotin, Daniel Acuna | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *REMOR의 작동 방식: (A) 다중 차원 보상 함수(HPRR)를 통한 AI 리뷰 생성 시스템, (B) PeerRT 데이터셋을 이용한 감독 미세조정(SFT) 및 GRPO 학습 프로세스*

본 논문은 추론(reasoning) 기능을 갖춘 대형언어모델(LLM)과 다목적 강화학습(MORL)을 결합하여 인간 수준 이상의 깊이 있고 균형잡힌 학술 논문 심사평을 자동 생성하는 REMOR 시스템을 제안한다. 기존 AI 심사평의 얕은 분석과 과도한 칭찬 문제를 다목적 보상함수와 추론 능력으로 극복한다.

## Motivation

- **Known**: LLM 기반 자동 심사평 생성 시스템이 발전했으나, 여전히 얕은 피드백(shallow suggestions), 과도한 칭찬(overpraising), 일반적인 코멘트 생성 문제가 존재함. 현재의 다중 에이전트 시스템은 20분 이상 소요되며 수백만 토큰을 사용함.

- **Gap**: (1) 심사평 품질 평가의 다차원성을 자동으로 정량화하는 방법 부재, (2) 인간 선호도와 정렬된 명확한 보상 함수 없음, (3) 추론 능력과 강화학습을 결합한 심사평 생성 시스템 부재.

- **Why**: 학술 출판 시스템의 과부하(reviewer fatigue), 낮은 품질 리뷰 증가, 다양성 부족 문제를 자동화된 고품질 심사평으로 해결 필요.

- **Approach**: (1) 추론 트레이스가 풍부한 고품질 심사평 데이터셋(PeerRT) 구축, (2) 인간 선호도 정렬 다중 차원 보상함수(HPRR) 설계, (3) Group Relative Policy Optimization(GRPO)으로 두 가지 모델(인간정렬 가중치 REMOR-H, 균일 가중치 REMOR-U) 학습.

## Achievement

![Figure 2](figures/fig2.webp) *각 모델별 평균 보상 점수 비교: REMOR-U와 REMOR-H가 인간 리뷰 및 기존 AI 시스템 대비 2배 이상의 보상 달성*

1. **성능 우수성**: REMOR-U와 REMOR-H가 인간 리뷰, 비추론 다중 에이전트 시스템, 상용 LLM 베이스라인 대비 평균 보상에서 2배 이상 달성. 최고 품질 AI 리뷰와 인간 리뷰가 비교 가능한 수준이나, REMOR은 저품질 인간 리뷰의 긴 꼬리 분포 회피.

2. **다차원 평가 메커니즘**: HPRR 함수가 비판(criticism), 예시(example), 중요도(importance), 제안(suggestion) 등 8개 차원을 종합적으로 평가하여 단순 정량 지표 이상의 통합적 품질 측정 가능.

3. **추론의 중요성 입증**: 추론 기능이 심사평 깊이 향상의 핵심 요소임을 실증적으로 입증. REMOR-U(균일 가중치)가 인간정렬 가중치 REMOR-H보다 정성적으로 더 실질적인 피드백 생성.

4. **공개 자산**: PeerRT 데이터셋, HPRR 함수, REMOR 모델 공개로 향후 연구 활성화 기반 제공.

## How

![Figure 3](figures/fig3.webp) *각 메트릭별 평균 보상: REMOR이 비판(criticism), 예시(example), 중요도(importance) 등에서 현저히 높은 점수 달성*

**데이터셋 구축**:
- ICLR 2017-2020 공개 데이터 기반 16.8K 심사평 수집 (5.5K 제출물)
- GROBID를 통한 PDF 텍스트 추출로 전체 논문 텍스트 통합
- Claude Sonnet 3.7 Extended Thinking으로 각 심사평에 추론 트레이스(thinking traces) 생성

**모델 학습**:
- **1단계 감독 미세조정(SFT)**: DeepSeek-R1-Distill-Qwen-7B를 LoRA로 PeerRT 데이터에 학습하여 도메인 특화 언어 스타일 습득
- **2단계 강화학습**: GRPO(Group Relative Policy Optimization) 적용으로 다목적 보상 최적화
  - 문장 수준 평가 모델: 비판, 예시, 중요도/관련성, 자료/방법, 표현/보고, 결과/논의, 제안/해결책 (8개 차원)
  - 관련성 점수: METEOR를 통한 리뷰-논문 텍스트 유사도 측정
  - 보상 결합: 정규화된 8개 메트릭 + METEOR의 가중합 (uniform vs. human-aligned weights)

**다목적 강화학습(MORL)**:
- 균일 가중치(U): 모든 차원에 동등한 가중치
- 인간정렬 가중치(H): 선행연구의 인간 선호도 기반 가중치 적용 (파레토 최적성 고려)

## Originality

- **추론 기능 + 강화학습 결합**: 심사평 생성에 Chain-of-Thought 스타일 추론을 도입하고 이를 강화학습으로 최적화한 최초 시도. 기존 일반 LLM이나 비추론 다중 에이전트 시스템과 차별화.

- **인간정렬 다목적 보상함수(HPRR)**: 심사평 품질의 다양한 측면(비판, 예시, 중요도 등)을 체계적으로 정의하고 인간 선호도와 정렬한 새로운 평가 프레임워크. 기존 ROUGE, BERTScore 등 단순 텍스트 유사도 지표의 한계 극복.

- **PeerRT 데이터셋**: 추론 트레이스가 풍부한 최초의 구조화된 심사평 데이터셋. 고급 추론 모델 학습의 기초 자료로 활용 가능.

- **역설적 발견**: 인간정렬 가중치가 오히려 낮은 성능을 보이고 균일 가중치(REMOR-U)가 정성적으로 더 나은 리뷰 생성. 이는 인간 선호도의 비일관성을 시사하는 중요한 통찰.

## Limitation & Further Study

**한계점**:
- 평가 대상이 주로 AI 생성 리뷰 간 비교에 한정되며, 대규모 인간 평가 부재. Arena-style 평가나 실제 저자/편집자 피드백 수집이 필요.
- METEOR 사용의 적절성 미검증. 관련성 평가를 위해 더 정교한 의미론적 유사도 측정 필요.
- 데이터셋이 ICLR만 포함하여 다른 학문분야(생물학, 물리학, 의학 등)로의 일반화 불명확.
- 추론 트레이스 생성을 Claude Sonnet으로 수행하여 모델 의존성 존재. 오픈소스 모델로의 재현성 검증 필요.
- 계산 비용(추론 시간, 메모리) 분석 부재. 실제 운영 확장성 미불명.

**후속 연구 방향**:
- 다학제 논문(생물정보학, 화학, 의학 등)으로 확대하여 일반화 검증
- 인간 평가자(저자, 편집자, 동료 리뷰어)를 통한 대규모 정성 평가 수행
- 보상함수의 인간정렬 방식 개선: 다양한 개인 선호도 반영 또는 적응형 가중치
- 다른 MORL 방법(스칼라화 외 방법)과의 비교
- 실시간 피드백 루프: 실제 심사평 사용 후 저자/에디터 피드백으로 보상함수 지속 개선


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: REMOR은 추론과 강화학습을 심사평 생성에 창의적으로 결합하여 인간 수준 이상의 성능을 달성한 의미 있는 기여이다. 특히 다차원 보상함수와 PeerRT 데이터셋의 공개는 학계에 실질적 자산이 될 것이다. 다만 인간 평가의 규모, 보상함수 설계의 정당성, 타분야 일반화 가능성에 대한 더 깊은 검증이 논문의 영향력을 강화할 것이다.

## Related Papers

- 🔄 다른 접근: [[papers/592_Openreviewer_A_specialized_large_language_model_for_generati/review]] — 학술 논문 심사평 생성에서 다목적 강화학습과 전문화된 모델이라는 서로 다른 접근법을 비교할 수 있다.
- 🔗 후속 연구: [[papers/676_Reviewagents_Bridging_the_gap_between_human_and_ai-generated/review]] — 다중 에이전트 협업을 통해 REMOR의 추론 기반 심사평 생성을 더욱 정교하게 발전시킨다.
- 🏛 기반 연구: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 정책 집계를 통한 다중 턴 강화학습의 기초적인 방법론을 학술 심사평 생성에 적용한다.
- 🧪 응용 사례: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — LLM 기반 추론을 활용한 자동 피어리뷰 생성이 평가 프레임워크의 실제 적용 사례를 보여준다.
- 🏛 기반 연구: [[papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/review]] — LLM 추론을 통한 자동 동료평가 생성 연구가 질문 기반 동적 리뷰 프레임워크의 기반 방법론을 제공한다.
- 🔄 다른 접근: [[papers/592_Openreviewer_A_specialized_large_language_model_for_generati/review]] — 학술 논문 심사평 생성에서 전문화된 모델과 다목적 강화학습이라는 서로 다른 접근법을 비교할 수 있다.
- 🔄 다른 접근: [[papers/676_Reviewagents_Bridging_the_gap_between_human_and_ai-generated/review]] — 학술 심사에서 다중 에이전트 협업과 강화학습 기반 추론이라는 서로 다른 접근법을 비교할 수 있다.
- 🔗 후속 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — 초기 탐색적 연구를 바탕으로 추론 능력과 다목적 최적화를 통해 더 정교한 심사 시스템을 구축한다.
- 🔗 후속 연구: [[papers/809_Three_AI-powered_steps_to_faster_smarter_peer_review/review]] — LLM 추론 기반 동료평가 생성으로 3단계 워크플로우의 자동화 수준을 더욱 발전시킨다
