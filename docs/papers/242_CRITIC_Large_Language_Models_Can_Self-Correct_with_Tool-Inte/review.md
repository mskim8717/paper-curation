---
title: "242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte"
authors:
  - "Zhibin Gou"
  - "Zhihong Shao"
  - "Yeyun Gong"
  - "Yelong Shen"
  - "Yujiu Yang"
date: "2023"
doi: "10.48550/arXiv.2305.11738"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)이 외부 도구(검색엔진, 코드 인터프리터 등)와 상호작용하여 자신의 출력을 검증하고 반복적으로 자가수정(self-correct)할 수 있도록 하는 통합 프레임워크를 제안한다. 인간의 비판적 사고 방식을 모방하여 할루시네이션, 코드 오류, 독성 콘텐츠 등의 문제를 완화한다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Reinforcement_Learning_Control_Systems"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Scientific_Agent_Framework_Design"
  - "topic/ai4s"
---

# CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

> **저자**: Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2305.11738](https://doi.org/10.48550/arXiv.2305.11738)

---

## Essence

![Figure 1](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *CRITIC 프레임워크: 외부 도구와 상호작용하여 검증(Verify)한 후 비판(Critique)에 기반해 수정(Correct)하는 반복 과정*

대규모 언어모델(LLM)이 외부 도구(검색엔진, 코드 인터프리터 등)와 상호작용하여 자신의 출력을 검증하고 반복적으로 자가수정(self-correct)할 수 있도록 하는 통합 프레임워크를 제안한다. 인간의 비판적 사고 방식을 모방하여 할루시네이션, 코드 오류, 독성 콘텐츠 등의 문제를 완화한다.

## Motivation

- **Known**: ChatGPT 등 최신 LLM은 인상적인 성능을 보이지만, 사실 오류(hallucination), 코드 결함, 독성 콘텐츠 등의 일관성 없는 문제를 드러낸다. 기존 해결책은 대규모 인간 주석이나 과제 특화 학습을 필요로 한다.

- **Gap**: 인간은 검색엔진으로 팩트체크하거나 코드 인터프리터로 디버깅하는 등 외부 도구를 활용해 내용을 검증하고 수정하지만, 블랙박스 LLM은 이런 도구 상호작용 기반 자가수정 능력이 부족하다.

- **Why**: 외부 피드백(external feedback)없이 LLM의 자체 검증만으로는 신뢰성이 낮고, 자가수정(self-correction) 효과가 제한적이다. 도구 기반 객관적 검증이 필수적이다.

- **Approach**: 인컨텍스트 러닝(in-context learning)과 몇샷 데모(few-shot demonstration)를 통해, 추가 학습 없이 블랙박스 LLM이 적절한 외부 도구와 상호작용하여 비판을 생성하고 이를 기반으로 반복 수정하도록 유도한다.

## Achievement

![Figure 2](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *다양한 과제(QA, 수학 프로그램 합성, 독성 감소)에서 CRITIC 프롬프트 예시: 검증 후 비판 생성, 수정된 답변 제시*

1. **정량적 성과**: ChatGPT 적용 시 3개 QA 과제에서 7.7 F1 향상, 3개 수학추론 과제에서 7.0% 절대 성능 향상, 독성 확률 79.2% 감소 달성. LLaMA-2(7B, 13B, 70B) 등 다양한 모델에서 일관된 개선 확인.

2. **방법론 유효성**: 외부 도구 상호작용이 없는 순수 자가수정은 효과 미미하거나 성능 저하를 초래하지만, CRITIC의 검증-수정 반복 과정은 지속적 개선을 보장한다. 자가수정의 필수 조건으로 외부 피드백의 중요성을 입증.

## How

![Figure 3-5](https://github.com/microsoft/ProphetNet/tree/master/CRITIC) *반복 과정을 통한 성능 변화: QA, GSM8k 수학 추론, 독성 감소 과제별 반복 횟수에 따른 개선 추이*

**알고리즘 (Algorithm 1)**:
- **초기화(1단계)**: 입력 x에 대해 모델 M이 초기 출력 ŷ₀ 생성
- **검증(3단계)**: 프롬프트 ℘, 초기 출력 ŷᵢ를 포함한 컨텍스트에서 LLM이 외부 도구 T(검색엔진, 코드 인터프리터, 계산기 등)와 상호작용하여 비판 cᵢ 생성
- **중단 조건(4-6단계)**: 생성된 비판이 현재 출력이 정확함을 나타내면 반환
- **수정(7단계)**: 입력, 이전 출력, 비판을 모두 포함한 컨텍스트에서 개선된 출력 ŷᵢ₊₁ 생성
- **반복(2-8단계)**: n번 반복하거나 중단 조건 만족 시 종료

**핵심 프롬프트 전략**:
- 검증 단계: "위 답변의 문제점은 무엇인가?" 형태로 LLM의 평가 능력 활용
- 비판 생성: 타당성(Plausibility), 정확성(Correctness), 진실성(Truthfulness) 등 다차원적 검증
- 도구 활용: API 호출 결과(검색 쿼리, 코드 실행 결과 등)를 프롬프트에 자동 포함
- 과제 특화: QA는 팩트체크, 수학은 코드 실행 검증, 독성은 독성 감지기 활용

## Originality

- **도구-상호작용 기반 자가수정**: 기존의 인간 피드백이나 학습 기반 접근과 달리, 외부 객관적 도구를 통한 검증을 자가수정의 핵심으로 제시. 인간의 비판적 사고(critical thinking) 프로세스를 체계화한 첫 시도.

- **블랙박스 모델의 범용성**: 추가 학습, 파인튜닝, 거대 규모 인간 주석을 요구하지 않고 순수 인컨텍스트 러닝으로 ChatGPT, GPT-3.5, LLaMA 등 이질적 모델에 적용 가능한 범용 프레임워크.

- **외부 피드백의 필수성 입증**: 순수 자가수정의 한계를 실증적으로 보이고, LLM은 자체 검증 능력이 부족하므로 객관적 외부 도구가 필수임을 강조(Kadavath et al. 등 선행 연구 재확인 및 확장).

- **다과제 통합**: QA(사실성), 수학(논리성), 독성 감소(안전성) 등 이질적 평가 차원의 과제에 단일 프레임워크를 적용, 방법의 범용성 입증.

## Limitation & Further Study

- **도구 의존성**: CRITIC의 성능은 사용 가능한 외부 도구의 품질과 정확성에 크게 의존. 검색 결과가 부정확하거나 코드 인터프리터가 에러 처리를 잘못하면 잘못된 비판 생성 가능. 도구 신뢰도 평가 메커니즘 부재.

- **반복 횟수 결정**: 현재 중단 기준은 LLM이 "출력이 정확하다"고 판단하는 것인데, 이 판단 자체의 신뢰성이 불명확. 최적 반복 횟수를 동적으로 결정하는 방법 필요.

- **프롬프트 민감도**: 검증 및 수정 프롬프트 설계가 성능에 미치는 영향에 대한 체계적 분석 부족. 과제별 최적 프롬프트 발견이 수작업(manual)에 의존.

- **계산 비용**: 반복적 도구 호출로 인한 API 비용과 지연 시간 증가. 수렴 속도 분석 및 계산 효율성 개선 방안 제시 부족.

- **후속 연구 방향**:
  - 도구 신뢰도를 고려한 적응적 검증(adaptive verification) 메커니즘
  - 강화학습(RL) 기반 최적 도구 선택 및 반복 횟수 결정
  - 멀티홉(multi-hop) 도구 조합을 통한 복잡한 추론 문제 확장
  - 인간-LLM 협업 설정에서 도구 설명(tool explanation) 제공

## Evaluation

| 항목 | 평가 |
|------|------|
| **Novelty (독창성)** | 4/5 |
| **Technical Soundness (기술 타당성)** | 4.5/5 |
| **Significance (중요성)** | 4.5/5 |
| **Clarity (명확성)** | 4/5 |
| **Overall (종합)** | 4.25/5 |

**총평**: CRITIC은 LLM의 자가수정 문제를 외부 도구 상호작용으로 우아하게 해결하며, 추가 학습 없이 범용적으로 적용 가능한 실용적 프레임워크를 제시한다는 점에서 높은 가치가 있다. 다만 도구 품질 의존성, 프롬프트 설계의 수작업 필요성, 계산 비용 증가 등의 실무적 제약이 있으며, 이들을 보완하는 추가 연구가 필요하다. ICLR 2024 채택된 것을 고려하면 LLM 신뢰성 개선 분야에서 의미 있는 기여를 한 것으로 평가된다.

## Related Papers

- 🔗 후속 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 자가감독 도구 학습이 외부 도구와의 상호작용을 통한 자가수정으로 발전된 형태이다.
- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 도구 상호작용을 통한 자가수정과 추론 중 검색 통합을 서로 다른 관점에서 접근한다.
- 🔗 후속 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 검색을 포함한 도구 사용을 통한 자가수정이 추론 중 자동 검색 활용으로 구체화될 수 있다.
- 🧪 응용 사례: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 외부 도구를 통한 검증과 수정이 편향 완화를 위한 추론 시간 개입에 활용될 수 있다.
- ⚖️ 반론/비판: [[papers/471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet/review]] — LLM의 자기 수정 불가능성과 도구 지원을 통한 자기 수정 가능성 사이의 대조를 보여준다.
- 🔗 후속 연구: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 도구 상호작용을 통한 자가수정이 추론 중 검색 통합이라는 특화된 형태로 발전될 수 있다.
- 🔗 후속 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — 도구 상호작용을 통한 자가수정이 추론 중 자동 검색 활용이라는 특화된 형태로 발전될 수 있다.
- 🔗 후속 연구: [[papers/655_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/review]] — CRITIC의 도구 통합 자기 교정이 ReAct의 추론-행동 시너지를 오류 수정 능력으로 확장한 발전된 형태
- 🔗 후속 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — CRITIC의 도구 기반 자기 수정 방법론을 외부 도구 없이 순수하게 LLM 내부 검증으로 확장한다.
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 외부 도구 사용의 자가학습이 도구와의 상호작용을 통한 자가수정으로 확장되는 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 도구 통합 자기 수정 연구가 외부 도구 없는 순수 LLM 기반 자기 정제의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/223_Clarify_when_necessary_Resolving_ambiguity_through_interacti/review]] — 도구 통합 자기 수정과 달리 사용자와의 명확화 질문을 통한 상호작용으로 모호성을 해결하는 접근법을 제시한다.
