---
title: "447_Iterative_self-incentivization_empowers_large_language_model"
authors:
  - "Zhengliang Shi"
  - "Lingyong Yan"
  - "Dawei Yin"
  - "Suzan Verberne"
  - "Maarten de Rijke"
date: "2025"
doi: "arXiv:2505.20128"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모 언어모델(LLM)을 정보 검색 에이전트로 자동 개선하는 **자기-인센티브화 기반 탐색 프레임워크(EXSEARCH)**를 제안한다. 일반화 EM 알고리즘을 통해 검색 궤적을 잠재변수로 취급하고, LLM이 생성한 데이터로부터 반복적으로 학습하는 자기 루프를 형성한다."
tags:
  - "cat/Reinforcement_Learning_Control_Systems"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Reinforcement_Learning_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rice_2025_Iterative self-incentivization empowers large language models as agentic searchers.pdf"
---

# Iterative self-incentivization empowers large language models as agentic searchers

> **저자**: Zhengliang Shi, Lingyong Yan, Dawei Yin, Suzan Verberne, Maarten de Rijke, Zhaochun Ren | **날짜**: 2025 | **DOI**: [arXiv:2505.20128](https://arxiv.org/abs/2505.20128)

---

## Essence

![Figure 2](figures/fig2.webp)
*그림 2: EXSEARCH의 Expectation-Maximization 프로세스 개요. E-step에서는 탐색 궤적을 샘플링하고 가중치를 할당하며, M-step에서는 재가중치 손실함수로 LLM을 학습시킨다.*

본 논문은 대규모 언어모델(LLM)을 정보 검색 에이전트로 자동 개선하는 **자기-인센티브화 기반 탐색 프레임워크(EXSEARCH)**를 제안한다. 일반화 EM 알고리즘을 통해 검색 궤적을 잠재변수로 취급하고, LLM이 생성한 데이터로부터 반복적으로 학습하는 자기 루프를 형성한다.

## Motivation

- **Known**: LLM이 질의 재작성(query rewriting), 문서 재순위화(document re-ranking) 등으로 정보 검색을 강화할 수 있다는 사실이 알려져 있음

- **Gap**: 다중 홉(multi-hop) 질문이나 복잡한 쿼리에서 LLM이 동적으로 검색을 수행하고, 무관한 검색 결과를 필터링하며, 여러 단계의 검색을 통합 방식으로 최적화하는 능력이 부족함

- **Why**: 기존 방식은 쿼리 분해, 지식 추출 등을 파이프라인 형태로 구성하되 각 단계를 독립적으로 학습시키므로, 엔드-투-엔드 감독(end-to-end supervision)이 부족하고 단계 간 정렬이 미흡함

- **Approach**: 검색 궤적(trajectory) z = {(x_i, d_i, e_i)}을 의사 변수(latent variable)로 모델링하고, 변분 추론(variational inference) 및 일반화 EM을 활용하여 중요도 샘플링(importance sampling)을 통해 LLM 자신이 생성한 궤적에서 자동 가중치를 할당한 후 재가중 손실로 학습하는 자기 개선 루프를 구성

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: HotpotQA 데이터셋에서 다양한 LLM에 EXSEARCH를 적용한 성능. 여러 모델과 스케일에서 안정적인 수렴을 보임.*

1. **성능 향상**: 4개 지식 집약적 벤치마크에서 강력한 베이스라인 대비 정확 일치도(Exact Match) 7.8% 향상 달성

2. **수렴 이론 보장**: 자기-인센티브화 훈련 프로세스의 수렴성을 이론적으로 증명하여 안정성 보장

3. **확장성 검증**: EXSEARCH-Zoo를 통해 다양한 백본 LLM(LLaMA, Qwen, Mistral) 및 모델 규모(3B~24B)에서 일관된 효과 입증

4. **통합 프레임워크**: 동적 문서 검색, 증거 추출, 답변 생성을 단일 LLM으로 통합하여 end-to-end 최적화 실현

## How

![Figure 2](figures/fig2.webp)

**핵심 방법론:**

- **검색 궤적 모델링**: 각 단계에서 사고(thinking: 쿼리 생성) → 검색(search: 외부 리트리버 호출) → 기록(recording: 세부 증거 추출)의 3가지 액션을 반복 수행

  $$p(z | x; \theta) = \prod_{i=1}^{|z|} p(x_i | x, z_{<i}; \theta) \cdot p(e_i | x_i, R(x_i); \theta)$$

- **E-step (궤적 탐색)**: 현재 LLM(θ_t)이 생성한 후보 궤적 z에 대해 중요도 가중치 할당
  $$w(z) \propto p(y | x, z; \theta_t)$$
  (궤적이 정답을 얼마나 잘 지원하는지 반영)

- **M-step (재가중 학습)**: ELBO 최대화로 모델 업데이트
  $$\max_\theta \mathbb{E}_{z \sim p(z|x;\theta_t)} [w(z) \log p(z|x;\theta) + w(z) \log p(y|x,z;\theta)]$$
  
  여기서 첫 항은 검색 학습(L_R), 두 번째 항은 답변 생성 학습(L_A)을 담당

- **자기-인센티브 루프**: E-step과 M-step을 반복 수행하여 LLM이 자신의 생성 데이터로부터 점진적으로 학습

## Originality

- **이론적 기반**: 정보 검색 문제를 변분 추론 프레임워크로 새롭게 형식화하고, 일반화 EM을 통해 검색 궤적을 최적화 대상으로 삼은 점이 혁신적

- **자기 개선 메커니즘**: 외부 라벨링이나 별도 리워드 모델 없이 정답과의 정렬도(alignment)로부터 자동 가중치를 도출하는 자기-감독 학습 방식

- **통합 최적화**: 종래의 단계별 파이프라인 방식을 벗어나 검색, 증거 추출, 답변 생성을 하나의 목적함수로 통합 최적화

- **이론적 보증**: 수렴성 증명으로 학습 안정성을 보장하는 근거 제시

## Limitation & Further Study

- **계산 비용**: E-step에서 여러 궤적을 샘플링하고 가중치 계산 비용이 추가로 발생하며, 대규모 데이터셋에서의 확장성 검토 필요

- **리트리버 의존성**: 외부 리트리버의 성능에 크게 의존하므로, 검색 결과가 매우 낮은 품질인 경우 개선의 한계

- **검색 공간 제약**: 현재는 상위 K개 문서만 고려하므로, 최적 증거가 K 이외의 범위에 있을 경우 놓칠 가능성

- **후속 연구**: 
  - 더 효율적인 중요도 샘플링 방법 개발
  - 리트리버와 LLM의 공동 훈련(joint training)
  - 비정형 데이터(웹, 동영상 등) 검색으로 확장
  - 더 복잡한 다중 홉 추론 벤치마크 개발

## Evaluation

- **Novelty**: 4.5/5
  - 변분 추론과 EM을 검색 문제에 적용한 점은 신선함. 다만 EM 자체는 기존 기법이므로 완전히 새로운 알고리즘은 아님

- **Technical Soundness**: 4.5/5
  - 수학적 유도가 엄밀하고 수렴성 증명이 포함됨. 실험 설정과 비교 대상이 합리적이나, 통계적 유의성 검정 명시 부족

- **Significance**: 4.5/5
  - 지식 집약적 QA 작업에서 실질적 성능 향상(+7.8%)을 달성하고, EXSEARCH-Zoo로 확장성 입증. 다만 더 광범위한 작업 영역(summarization, dialogue 등)에서의 평가 필요

- **Clarity**: 4/5
  - 전체 프레임워크가 명확하게 설명되고 그림이 직관적임. 다만 중요도 가중치 계산의 실제 구현 세부사항(예: 토큰 로짓 활용 방식) 기술 필요

- **Overall**: 4.3/5

**총평**: EXSEARCH는 LLM 기반 정보 검색 에이전트를 자기-인센티브화된 자기 개선 루프로 학습하는 이론적으로 견고한 프레임워크를 제시하며, 지식 집약적 작업에서 일관된 성능 향상을 보여준다. 다만 계산 효율성 개선과 더 광범위한 작업 영역 검증이 이루어진다면 더 강력한 기여가 될 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — 정보 검색에서의 자기개선과 일반적 자가수정을 서로 다른 도메인에서 접근하는 방법이다.
- 🏛 기반 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 검색 궤적의 반복적 개선이 RL을 통한 추론 패턴 개발의 특수한 사례로 볼 수 있다.
- 🔗 후속 연구: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — 정보 검색에서의 자기개선이 일반적인 대화형 환경에서의 능동적 정보 수집으로 확장될 수 있다.
- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 검색 에이전트의 자기개선과 추론 중 검색 활용을 서로 다른 관점에서 다룬다.
- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 추론 중 검색 활용과 검색 에이전트의 자기개선을 서로 다른 관점에서 다룬다.
- 🏛 기반 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 추론 중 자동 검색 학습이 검색 에이전트의 자기개선을 위한 구체적인 메커니즘을 제공한다.
- 🔗 후속 연구: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — 능동적 정보 수집이 검색 에이전트의 자기개선을 위한 구체적인 적용으로 발전될 수 있다.
