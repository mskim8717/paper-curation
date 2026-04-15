---
title: "419_Hypothesis_Generation_with_Large_Language_Models"
authors:
  - "Yangqiaoyu Zhou"
  - "Haokun Liu"
  - "Tejes Srivastava"
  - "Hongyuan Mei"
  - "Chenhao Tan"
date: "2024"
doi: "10.18653/v1/2024.nlp4science-1.10"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)을 이용하여 데이터 기반 과학적 가설(hypothesis)을 자동으로 생성하고 개선하는 HypoGeniC 알고리즘을 제안한다. 다중 슬롯 머신(multi-armed bandit) 이론에 영감을 받아 탐색-활용(exploration-exploitation) 균형을 조절하며 반복적으로 가설 풀을 업데이트하여, 소수 샘플 프롬프팅을 크게 능가하는 해석 가능한 가설 기반 분류기를 구현한다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhou et al._2024_Hypothesis Generation with Large Language Models.pdf"
---

# Hypothesis Generation with Large Language Models

> **저자**: Yangqiaoyu Zhou, Haokun Liu, Tejes Srivastava, Hongyuan Mei, Chenhao Tan | **날짜**: 2024 | **DOI**: [10.18653/v1/2024.nlp4science-1.10](https://doi.org/10.18653/v1/2024.nlp4science-1.10)

---

## Essence

본 논문은 대규모 언어 모델(LLM)을 이용하여 데이터 기반 과학적 가설(hypothesis)을 자동으로 생성하고 개선하는 HypoGeniC 알고리즘을 제안한다. 다중 슬롯 머신(multi-armed bandit) 이론에 영감을 받아 탐색-활용(exploration-exploitation) 균형을 조절하며 반복적으로 가설 풀을 업데이트하여, 소수 샘플 프롬프팅을 크게 능가하는 해석 가능한 가설 기반 분류기를 구현한다.

## Motivation

- **Known**: 과학적 진전은 효과적인 가설 생성에 의존하며, 현재까지 가설 생성은 연구자의 수동적 데이터 분석과 직관에 의존해왔다. LLM의 급속한 발전으로 새로운 기회가 열렸다.

- **Gap**: 기존 LLM 프롬프팅 방식은 장문의 맥락을 효과적으로 활용하지 못하며, 생성 과정에서 가설 품질을 평가하고 개선할 수 있는 체계적 방법이 부족하다.

- **Why**: 단순한 few-shot 프롬프팅으로 생성한 가설은 전체 데이터 공간을 충분히 설명하지 못하고, 잘못된 예측을 하는 경우들이 축적되어 있지만 이를 체계적으로 해결할 메커니즘이 없다.

- **Approach**: (1) 초기 가설 생성 → (2) 훈련 예제에 대한 반복적 평가 및 보상 업데이트 → (3) 잘못 분류된 예제들을 수집하는 "틀린 예제 은행(wrong example bank)" 구축 → (4) 은행의 예제들로부터 새로운 가설 생성 및 통합 → (5) 여러 추론 전략을 통한 해석 가능한 예측

## Achievement

![Figure 1 설명: HypoGeniC의 update 단계에서 상위 k개 가설을 새 훈련 예제에 평가하고, 보상을 예측 정확성에 따라 업데이트한다. 잘못된 예제가 임계값을 초과하면 틀린 예제 은행에 추가되고, 은행이 최대 크기에 도달하면 이를 기반으로 새 가설을 생성한다.](figures/fig1.webp)

1. **분류 성능 향상**: 합성 데이터에서 31.7%, 실제 데이터에서 13.9%, 3.3%, 24.9% 정확도 개선 (few-shot 대비). DECEPTIVE REVIEWS와 TWEET POPULARITY 작업에서 RoBERTa, Llama-2-7B 등 감독학습(supervised learning) 방식을 12.1%, 11.6% 초과 달성

2. **모델 간 교차 호환성**: GPT-3.5-turbo로 생성한 가설을 Mixtral 등 다른 LLM으로도 효과적으로 활용 가능하며, 분포 외(out-of-distribution) 데이터셋에서도 미세조정된 RoBERTa를 능가

3. **해석 가능한 발견**: 생성된 가설이 기존 문헌의 이론을 검증하면서도 새로운 통찰 제시 (예: "개인적 경험이나 생일, 기념일 등을 언급한 리뷰가 더 신뢰할 수 있다"는 새로운 발견)

4. **강건한 합성 작업 성능**: 단일의 알려진 유효 가설이 있는 합성 작업에서 가설을 정확히 복구

## How

- **초기 가설 생성(Initialization)**: 훈련 집합 S의 부분집합 S_init에 대해 LLM에 프롬프트하여 고수준의 가설들 생성 → 초기 가설 은행 H 구성

- **반복적 가설 업데이트(Iterative Update)**:
  - 각 훈련 예제 s에 대해 현재 가설 풀에서 보상이 높은 상위 k개 가설 선정
  - 각 가설으로 s를 예측하고 정확성 평가 후 보상 업데이트
  - 오예측 가설 수가 임계값 이상이면 s를 틀린 예제 은행 W에 추가
  - |W|이 최대값 w_max에 도달하면 W의 예제들로부터 새 가설 생성 및 통합

- **UCB 기반 보상 함수**:
  ```
  r_i = [정확도 항] + α√(log t / |S_i|)
  ```
  첫 번째 항은 가설의 훈련 정확도, 두 번째 항은 탐색 보너스로 선택 빈도가 낮은 가설을 장려

- **다양한 추론 전략**:
  - **Best-accuracy hypothesis**: 가장 높은 정확도의 단일 가설 사용
  - **Filter and weighted vote**: 관련 가설들 필터링 후 가중 투표
  - **Single-step adaptive inference**: 한 번의 장문 프롬프트로 가장 적절한 가설 선정
  - **Two-step adaptive inference**: 적절한 가설 선정과 예측을 두 단계로 분리

## Originality

- **새로운 문제 정의**: 데이터 기반 과학적 가설 자동 생성이라는 학제 간(interdisciplinary) 문제를 명확히 공식화하고 계산 가능한 형태로 구현

- **다중 슬롯 머신 이론의 창의적 적용**: 표준 UCB 알고리즘을 새로운 맥락(동적 팔, 다중 팔 평가)에 맞게 변형하여 탐색-활용 균형 달성

- **틀린 예제 은행 메커니즘**: 현재 가설 풀의 지식 격차를 명시적으로 추적하고 이를 기반으로 새로운 가설을 생성하는 반복적 개선 루프는 기존 가설 생성 방식과 차별화

- **포괄적 평가 프레임워크**: 단순 분류 정확도를 넘어 모델 간 호환성, 분포 외 일반화, 정성적 가설 평가를 통합하여 가설의 진정한 품질을 측정

## Limitation & Further Study

- **LLM 의존성**: 방법론의 성능이 LLM의 능력에 크게 의존하며, 더 작은 또는 오픈소스 모델에서의 성능이 충분히 탐색되지 않음. 비용(cost) 측면에서 실제 과학 응용에 제약 가능성

- **가설 평가의 주관성**: 생성된 가설의 "품질"을 어떻게 정의하고 측정할지에 대한 철학적 문제. 정확도는 유용한 지표이지만 과학적 가치, 참신성, 이해 가능성에 대한 체계적 평가 방법 부재

- **하이퍼파라미터 민감도**: k, w_max, α 등 여러 하이퍼파라미터의 설정이 성능에 미치는 영향에 대한 깊이 있는 분석 부족. 최적값 선택의 일반화 가능성 불명확

- **확장성 한계**: 현재 방법은 분류 작업에 초점을 두고 있으며, 회귀, 인과관계 추론, 복잡한 구조적 관계 발견으로의 확장 방향이 명확하지 않음

- **인간 검증 부족**: 실제 도메인 전문가에 의한 생성 가설의 검증이 DECEPTIVE REVIEWS 작업 외에는 제한적. 과학적 새로운 발견의 실질적 가치 검증 필요

- **후속 연구 방향**:
  - 더 정교한 보상 함수 설계로 탐색-활용 균형 최적화
  - 다중 작업 또는 도메인 간 전이 학습(transfer learning) 연구
  - 인간-LLM 협업 가설 생성 프레임워크 개발
  - 시간 기반 데이터, 인과 데이터 등 특수 형태의 데이터에 대한 적용


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM을 과학적 가설 생성에 활용하는 새로운 시도로, 다중 슬롯 머신 이론에 기반한 체계적이고 실용적인 알고리즘을 제시하며 실증적으로 강력한 결과를 도출했다. 특히 생성된 가설의 모델 간 호환성과 해석 가능성은 LLM의 일반화 능력을 시사하는 중요한 발견이다. 다만, 더 깊은 이론적 분석과 실제 과학 커뮤니티와의 협력을 통한 가설 품질의 검증이 이루어진다면 더욱 설득력 있는 기여가 될 것으로 기대된다.

## Related Papers

- 🏛 기반 연구: [[papers/376_Generation_and_human-expert_evaluation_of_interesting_resear/review]] — 대규모 지식 그래프 기반 연구 아이디어 생성의 실제 검증 사례로서 가설 생성 알고리즘의 효용성을 입증한다.
- 🔗 후속 연구: [[papers/492_Literature_meets_data_A_synergistic_approach_to_hypothesis_g/review]] — 문헌과 데이터의 시너지 접근법을 다중 슬롯 머신 이론으로 체계화하여 더 정교한 가설 생성 메커니즘을 제시한다.
- 🔄 다른 접근: [[papers/468_Large_Language_Models_are_Zero_Shot_Hypothesis_Proposers/review]] — LLM의 제로샷 가설 제안과 반복적 가설 개선 알고리즘은 모두 AI 기반 가설 생성의 서로 다른 접근법이다.
- 🧪 응용 사례: [[papers/149_Bayes-Entropy_Collaborative_Driven_Agents_for_Research_Hypot/review]] — 베이즈-엔트로피 협업 에이전트가 연구 가설 생성에서 탐색-활용 균형을 실제 구현한 사례를 제공한다.
- 🏛 기반 연구: [[papers/473_Large_Language_Models_for_Automated_Open-domain_Scientific_H/review]] — LLM을 이용한 가설 생성의 기본 방법론과 이론적 배경을 제공한다
- 🏛 기반 연구: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — LLM의 가설 생성 능력에 대한 기초 연구가 자기검증 시스템의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/468_Large_Language_Models_are_Zero_Shot_Hypothesis_Proposers/review]] — 제로샷 가설 생성에서 LLM 기반 일반적 가설 생성으로 확장된 연구 방향이다
- 🏛 기반 연구: [[papers/031_A_Survey_on_Hypothesis_Generation_for_Scientific_Discovery_i/review]] — 과학적 가설 생성의 기본 원리와 LLM 활용 방법론에 대한 기초적 이해를 제공한다
- 🏛 기반 연구: [[papers/363_From_Reasoning_to_Learning_A_Survey_on_Hypothesis_Discovery/review]] — 대규모 언어모델을 활용한 가설 생성 연구가 LLM 기반 가설 발견과 규칙 학습의 기본 방법론을 제공한다
- 🏛 기반 연구: [[papers/763_Sparks_of_science_Hypothesis_generation_using_structured_pap/review]] — LLM을 활용한 가설 생성의 기본 방법론을 제공하며 구조화된 접근법의 이론적 기반이 된다
- 🏛 기반 연구: [[papers/757_Simulating_tabular_datasets_through_llms_to_rapidly_explore/review]] — LLM을 활용한 가설 생성 연구가 표 데이터 시뮬레이션을 통한 가설 검증의 이론적 기반을 제공한다
- 🔗 후속 연구: [[papers/376_Generation_and_human-expert_evaluation_of_interesting_resear/review]] — 데이터 기반 가설 생성 알고리즘을 대규모 지식 그래프와 결합하여 더 체계적이고 검증된 연구 아이디어 생성으로 발전시켰다.
- 🏛 기반 연구: [[papers/492_Literature_meets_data_A_synergistic_approach_to_hypothesis_g/review]] — LLM 기반 가설 생성에 대한 체계적 조사로, 문헌과 데이터를 통합한 가설 생성 방법론의 이론적 배경을 제공한다
