---
title: "598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as"
authors:
  - "Yuhua Jiang"
  - "Yuwen Xiong"
  - "Yufeng Yuan"
  - "Chao Xin"
  - "Wenyuan Xu"
date: "2025"
doi: "10.48550/arXiv.2506.10406"
arxiv: ""
score: 4.3
essence: "대형 언어모델(LLM)의 자기 수정(self-correction) 능력을 강화하기 위해, 정책(policy)과 검증자(verifier) 역할을 전환하며 다중 턴 강화학습을 통해 검증-수정 워크플로우를 구현한 새로운 프레임워크를 제안한다. 기존 방법과 달리 모델 자신의 검증 단계에서 오류를 명시적으로 감지할 때만 답변을 수정하므로 모델 붕괴를 완화하고 추론과 검증 능력을 함께 향상시킨다."
tags:
  - "cat/Reinforcement_Learning_Control_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Reinforcement_Learning_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jiang et al._2025_PAG Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier.pdf"
---

# PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier

> **저자**: Yuhua Jiang, Yuwen Xiong, Yufeng Yuan, Chao Xin, Wenyuan Xu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2506.10406](https://doi.org/10.48550/arXiv.2506.10406)

---

## Essence

![Figure 1](figures/fig1.webp) 
*상단 좌측: 다양한 수학 추론 데이터셋에서 PAG의 최첨단 자기 수정 성능. 하단: SCoRe는 신뢰도와 관계없이 항상 두 번째 시도를 생성하지만, PAG는 자기 검증을 통한 선택적 수정을 수행*

대형 언어모델(LLM)의 자기 수정(self-correction) 능력을 강화하기 위해, 정책(policy)과 검증자(verifier) 역할을 전환하며 다중 턴 강화학습을 통해 검증-수정 워크플로우를 구현한 새로운 프레임워크를 제안한다. 기존 방법과 달리 모델 자신의 검증 단계에서 오류를 명시적으로 감지할 때만 답변을 수정하므로 모델 붕괴를 완화하고 추론과 검증 능력을 함께 향상시킨다.

## Motivation

- **Known**: LLM은 복잡한 추론 작업에서 인상적인 성능을 보이지만, 자신의 출력 정확성을 안정적으로 검증하는 데 어려움을 겪는다. 기존 해결 방법은 분리된 검증 모델(separate verifier models)을 요구하거나 다단계 자기 수정 훈련 파이프라인(multi-stage self-correction training pipeline)을 필요로 한다.

- **Gap**: SCoRe와 같은 기존 다중 턴 RL 방법은 모델 신뢰도와 관계없이 항상 두 번째 시도를 생성하며, 이로 인해 "모델 붕괴(model collapse)" 현상이 발생한다. 이를 완화하기 위해 복잡한 워밍업 단계와 다단계 훈련 프로토콜이 필요하다.

- **Why**: 검증 단계를 명시적으로 도입하면 모델이 표면적인 언어 변경이 아닌 진정한 자기 반성을 하도록 유도할 수 있으며, 생성 검증자(generative verifier)와 정책의 역할 전환을 통해 두 능력을 함께 개선할 수 있다.

- **Approach**: 단일 LLM이 생성 검증자 역할(자체 답변 평가)과 정책 역할(솔루션 생성)을 번갈아 수행하는 통합 다중 턴 RL 프레임워크 제안. 검증에서 오류가 감지될 때만 수정을 진행하는 선택적 수정 메커니즘 도입.

## Achievement

![Figure 2](figures/fig2.webp)
*PAG 프레임워크 개요: LLM이 정책 역할(솔루션 생성)과 생성 검증자 역할(자체 솔루션 평가)을 다중 턴 프로세스에서 번갈아 수행하며, 자기 검증이 정확하거나 최대 턴 수에 도달할 때까지 반복*

1. **자기 수정 성능 향상**: 다양한 수학 추론 벤치마크(GSM8K, MATH, Olympiad 등)에서 직접 생성 정확도와 자기 수정 정확도를 동시에 개선. Qwen-2.5-7B-Instruct에서 기저 모델(base model)보다 약 4-5% 향상.

2. **단순화된 훈련 프로세스**: 복잡한 워밍업 단계나 다단계 훈련 프로토콜 없이 기존 명령어 튜닝된(instruction-tuned) LLM에서 직접 다중 턴 RL을 적용 가능. 훈련 효율성이 향상되고 구현이 단순화됨.

3. **우수한 생성 검증 능력**: 자기 검증 기반 Best-of-N(BoN) 전략이 다수결 투표(majority voting)를 초과 성능. 단일 모델 내에서 여러 자체 생성 시도 중 최적의 후보 자동 선택.

4. **모델 붕괴 완화**: 검증-수정 워크플로우가 표면적 언어 변경을 억제하고 진정한 자기 반성을 촉진하여 더 실질적인 개선 달성.

## How

![Figure 3](figures/fig3.webp)
*PAG 훈련 메커니즘: 보상 신호 설계 및 다중 턴 RL 최적화 과정*

- **역할 전환 메커니즘(Role-Switching)**: LLM이 첫 시도 생성(정책 역할) → 자기 검증(검증자 역할) → 검증 결과에 따른 조건부 수정 → 재검증을 반복하는 구조로, 동일 파라미터 θ를 공유하면서 문맥(context)을 통해 역할 구분.

- **선택적 수정(Selective Revision)**: 검증자가 "The answer is wrong"을 명시적으로 생성할 때만 정책이 수정된 시도를 생성. 이는 기존의 무조건적 재시도와 구별되어 실질적 개선 유도.

- **이중 보상 신호(Dual Reward Signal)**: 
  - 시도에 대한 보상: Ry(ŷi, x) = 1 (정답), 0 (오답)
  - 검증에 대한 보상: Rv(v̂j, ŷj-1, x) = 1 (검증 정확), 0 (검증 오류)
  
- **다중 턴 RL 최적화**: 궤적(trajectory) τx = (x, ŷ1, v̂2, ŷ2, v̂3, ...) 전체에 대해 누적 보상을 최대화하도록 정책 그래디언트(policy gradient) 기반 RL 알고리즘 적용.

- **종료 조건**: 자기 검증이 "correct"를 반환하거나 최대 턴 수(Tmax)에 도달할 때까지 반복.

## Originality

- **통합 프레임워크**: 기존 연구가 정책 최적화와 검증자 훈련을 분리된 모델이나 단계로 다룬 반면, PAG는 단일 모델 내에서 두 능력을 동시에 공동 진화(co-evolve)시키는 통합 다중 턴 RL 프레임워크 제안.

- **검증-수정 패러다임**: "검증 후 수정(verify-then-revise)" 원칙 도입으로 기존의 "무조건적 재시도(unconditional re-attempt)" 접근방식과 근본적으로 차별화. 이는 모델 붕괴 문제를 우아하게 해결.

- **워밍업 불필요**: SCoRe의 다단계 훈련과 달리, 기존 instruction-tuned LLM에서 직접 PAG를 적용 가능하여 훈련 복잡도 대폭 감소.

- **생성 검증의 활용**: 검증을 차별적 분류(discriminative classification)가 아닌 생성적 추론(generative reasoning)으로 구현하여 모델의 사고 과정을 명시적으로 표현하고, 이를 자동으로 최적화.

- **Best-of-N 선택 통합**: 생성 검증 능력을 활용하여 다수결 투표보다 효과적인 자기 검증 기반 후보 선택 전략 제시.

## Limitation & Further Study

- **최대 턴 수 제약**: 알고리즘이 Tmax에 도달하면 종료되므로, 매우 복잡한 문제의 경우 충분한 자기 수정 기회를 갖지 못할 가능성. 동적 종료 조건 학습 필요.

- **검증 정확도 의존성**: 모든 과정이 모델의 자기 검증 정확도에 의존하므로, 검증이 실패하면 수정이 일어나지 않을 가능성. 검증 신뢰도 개선 방법 탐구 필요.

- **계산 비용**: 다중 턴 프로세스로 인한 추론 시 계산 오버헤드 증가. 효율적인 조기 종료(early stopping) 메커니즘 개발 필요.

- **제한된 작업 평가**: 주로 수학 추론 작업에 집중. 코드 생성, 자연어 이해 등 다양한 추론 작업에 대한 일반화 가능성 평가 필요.

- **후속 연구 방향**:
  - 검증자 신뢰도 추정(confidence estimation) 메커니즘 도입
  - 계산 예산에 따른 동적 다중 턴 제어
  - 더 복잡한 추론 작업으로의 확대 적용
  - 다양한 LLM 크기에서의 확장성 연구

## Evaluation

- **Novelty**: 4.5/5
  - 검증-수정 패러다임의 명확한 차별성과 단일 모델 내 역할 전환의 우아한 설계
  - 다만 RL 기반 자기 수정 자체는 선행 연구가 있어 부분 감점

- **Technical Soundness**: 4.5/5
  - 이중 보상 신호와 다중 턴 RL 설계가 명확하고 논리적
  - 실험 설계와 비교가 충실함
  - 검증 정확도에 대한 민감도 분석 추가 가능

- **Significance**: 4/5
  - 훈련 단순화와 추론 성능 향상 동시 달성은 실질적 의미
  - 생성 검증의 실질적 활용 제시
  - 다만 새로운 기술적 난제(예: 검증 신뢰도) 해결 필요

- **Clarity**: 4.5/5
  - 전체 구조와 알고리즘이 명확하게 설명됨
  - Figure 2의 프레임워크 시각화가 직관적
  - 기술 세부사항은 충분히 상세함

- **Overall**: 4.3/5

**총평**: PAG는 검증-수정 원칙을 통해 LLM 자기 수정의 모델 붕괴 문제를 우아하게 해결하며, 훈련 복잡도를 크게 감소시키면서도 성능을 향상시킨다. 단일 모델 내 역할 전환을 활용한 효율적인 설계가 돋보이나, 검증 신뢰도 향상과 다양한 작업으로의 일반화가 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/683_RM-R1_Reward_Modeling_as_Reasoning/review]] — 자기수정을 정책 레벨에서 구현하는 것과 보상 모델에 추론을 통합하는 서로 다른 접근법이다.
- 🔗 후속 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 자발적으로 개발되는 자기 검증 패턴을 명시적인 다중턴 프레임워크로 체계화한다.
- 🏛 기반 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — 생성-검증 갭 문제를 다중턴 강화학습을 통해 해결하려는 구체적인 방법론을 제시한다.
- 🧪 응용 사례: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 자기수정 메커니즘이 편향 완화를 위한 추론 시간 개입으로 활용될 수 있다.
- 🔗 후속 연구: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 자발적으로 개발되는 자기 검증 패턴이 명시적인 다중턴 자기수정 프레임워크로 발전될 수 있다.
- 🔄 다른 접근: [[papers/683_RM-R1_Reward_Modeling_as_Reasoning/review]] — 보상 모델에 추론을 통합하는 것과 정책 자체에 검증-수정을 통합하는 서로 다른 접근법이다.
- 🔄 다른 접근: [[papers/447_Iterative_self-incentivization_empowers_large_language_model/review]] — 정보 검색에서의 자기개선과 일반적 자가수정을 서로 다른 도메인에서 접근하는 방법이다.
- 🏛 기반 연구: [[papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/review]] — 개선된 정책 최적화가 다중턴 자기수정 프레임워크의 기반이 될 수 있다.
- 🔄 다른 접근: [[papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/review]] — 자연어 비판 통합과 다중턴 자기수정을 서로 다른 방식으로 추론 능력을 향상시킨다.
- 🔄 다른 접근: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — 자기검증 대신 정책 집계를 통한 자기교정으로 LLM의 신뢰성을 확보하는 다른 접근법을 제시한다.
- 🔄 다른 접근: [[papers/296_Dynamic_Search_for_Inference-Time_Alignment_in_Diffusion_Mod/review]] — 둘 다 추론 시간 최적화를 다루지만 Dynamic Search는 확산 모델에, PAG는 강화학습 기반 자기수정에 적용됨
- 🔄 다른 접근: [[papers/249_Curriculum_Reinforcement_Learning_from_Easy_to_Hard_Tasks_Im/review]] — 커리큘럼 강화학습과 정책 집계를 통한 다중 턴 강화학습이 서로 다른 방식으로 단계적 학습 최적화 문제를 해결한다.
- 🏛 기반 연구: [[papers/538_Mind_the_gap_Examining_the_self-improvement_capabilities_of/review]] — 생성-검증 갭이 다중턴 자기수정 프레임워크가 필요한 이유를 설명한다.
- 🧪 응용 사례: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 다중턴 자기수정 메커니즘이 편향 출력을 실시간으로 식별하고 완화하는 데 활용될 수 있다.
- 🏛 기반 연구: [[papers/665_Remor_Automated_peer_review_generation_with_llm_reasoning_an/review]] — 정책 집계를 통한 다중 턴 강화학습의 기초적인 방법론을 학술 심사평 생성에 적용한다.
