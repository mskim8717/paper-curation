---
title: "471_Large_Language_Models_Cannot_Self-Correct_Reasoning_Yet"
authors:
  - "Jie Huang"
  - "Xinyun Chen"
  - "Swaroop Mishra"
  - "Huaixiu Steven Zheng"
  - "Adams Wei Yu"
date: "2023"
doi: "10.48550/arXiv.2310.01798"
arxiv: ""
score: 4.5
essence: "대규모 언어 모델(LLM)들은 외부 피드백 없이 자신의 추론 오류를 자동으로 수정하지 못하며, 오히려 자기 수정(self-correction) 후 성능이 저하된다는 것을 실증적으로 증명한다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Automated_Scientific_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2023_Large Language Models Cannot Self-Correct Reasoning Yet.pdf"
---

# Large Language Models Cannot Self-Correct Reasoning Yet

> **저자**: Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2310.01798](https://doi.org/10.48550/arXiv.2310.01798)

---

## Essence

대규모 언어 모델(LLM)들은 외부 피드백 없이 자신의 추론 오류를 자동으로 수정하지 못하며, 오히려 자기 수정(self-correction) 후 성능이 저하된다는 것을 실증적으로 증명한다.

## Motivation

- **Known**: 최근 연구들에서 LLM의 자기 수정(self-correction) 능력이 추론 성능을 크게 향상시킨다고 주장하고 있음. 예를 들어, RCI는 GSM8K에서 7% 개선, CommonSenseQA에서 15% 개선을 보고함.

- **Gap**: 그러나 기존 연구들은 정답 라벨(oracle labels)을 사용하여 수정을 유도하고 있으며, 실제 응용 환경에서 이러한 외부 피드백 없이 LLM이 진정으로 자신의 오류를 인식하고 수정할 수 있는지는 명확하지 않음.

- **Why**: 근본적인 질문: "만약 LLM이 자기 수정 능력이 있다면, 처음부터 왜 올바른 답을 제시하지 않는가?" 이 역설을 해결하기 위해 외부 피드백 없는 **내재적 자기 수정(intrinsic self-correction)**에 대한 엄격한 평가가 필요함.

- **Approach**: 세 가지 관점에서 기존 자기 수정 방법 평가: (1) 오라클 라벨 의존성, (2) 동등한 추론 비용 기준 비교, (3) 프롬프트 설계의 영향.

## Achievement

![Figure 1](https://arxiv.org/html/2310.01798v2/x1.png) *두 라운드의 자기 수정 후 답변 변화 분석: 변화 없음, 올바른→잘못된, 잘못된→올바른 범주별 비율*

1. **오라클 라벨 문제**: GSM8K, CommonSenseQA, HotpotQA에서 오라클 라벨을 사용한 자기 수정은 상당한 성능 개선(7-15%)을 보이지만, 외부 피드백 없는 내재적 자기 수정에서는 **모든 모델과 데이터셋에서 성능 저하** 관찰 (GPT-3.5: GSM8K 75.9%→75.1%, CommonSenseQA 75.8%→38.1%; GPT-4: 95.5%→91.5%, 82.0%→79.5%).

2. **다중 에이전트 토론의 한계**: 여러 LLM 인스턴스가 서로의 답을 비판하는 다중 에이전트 토론(Multi-Agent Debate)은 동등한 응답 수를 기준으로 자기일관성(self-consistency)보다 나은 성능을 보이지 못함.

3. **프롬프트 설계 문제**: 일부 기존 연구의 개선 효과는 초기 응답 생성 시 부최적(sub-optimal) 프롬프트를 사용한 것에서 비롯됨. 피드백을 초기 지시사항에 통합하면 자기 수정을 사용한 것보다 더 좋은 결과를 얻음.

## How

- **실험 설정**: GSM8K, CommonSenseQA, HotpotQA에서 GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, Llama-2-70b-chat 모델 평가

- **세 단계 프롬프트 전략 적용**: (1) 초기 생성, (2) 이전 생성 검토 및 피드백 생성, (3) 피드백을 포함한 원래 질문에 다시 답변. 최대 2라운드 자기 수정 수행

- **오라클 라벨 조건**: 정답 라벨로 수정 프로세스 결정 (기존 연구 재현)

- **내재적 자기 수정**: 라벨 제거, LLM이 독립적으로 수정 중단 여부 결정

- **다양한 프롬프트 평가**: "이 답이 올바를 수도 있고 잘못될 수도 있다고 가정하세요. 신중하게 검토하고 발견한 심각한 문제를 보고하세요"와 같은 다양한 피드백 프롬프트 테스트

- **정성적 분석**: 답변 변화 유형 분류 (No Change, Correct→Incorrect, Incorrect→Correct) 및 구체적 사례 분석

## Originality

- **"내재적 자기 수정"의 엄격한 정의**: 외부 피드백과 명확하게 구분하여, 실제 응용 가능성 있는 설정 제시

- **기존 주장에 대한 체계적 재검증**: 오라클 라벨의 영향을 명확히 드러내고, 기존 논문들의 평가 문제점을 구조적으로 정리(Table 1)

- **공평한 비교 기준 수립**: 동일한 모델 호출 수를 기준으로 비교하여, 자기일관성 vs 다중 에이전트 토론의 진정한 효과 측정

- **프롬프트 설계의 중요성 강조**: 자기 수정 개선이 실제로는 프롬프트 개선의 결과일 수 있음을 증명

## Limitation & Further Study

- **샘플 크기 제약**: 비용 절감으로 GPT-4-Turbo와 Llama-2는 200개 샘플(HotpotQA 100개)에서만 평가. 전체 데이터셋 재평가 필요.

- **모델 범위 제한**: OpenAI 모델 중심 평가. 더 다양한 오픈소스 모델(Llama-2 외) 포함 필요.

- **자기 수정 라운드 수**: 최대 2라운드만 평가. 더 많은 라운드의 효과 미조사.

- **후속 연구 방향**: 
  - 외부 도구(코드 실행, 검증 함수 등)를 활용한 피드백 메커니즘 개발
  - LLM의 실제 오류 인식 메커니즘 분석
  - 진정한 자기 수정을 가능하게 하는 모델 아키텍처 또는 학습 방법 연구
  - 도메인별 자기 수정 효과 차이 조사


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 5/5
- Overall: 4.5/5

**총평**: 이 논문은 LLM의 자기 수정 능력에 대한 기존 낙관적 주장들을 체계적으로 비판하고 실제 한계를 입증함으로써, 이 분야의 평가 기준을 높이고 향후 연구 방향을 재설정하는 중요한 기여를 한다. 특히 외부 피드백 없는 실제 조건에서의 성능 평가는 실용적 가치가 높다.

## Related Papers

- 🏛 기반 연구: [[papers/041_Aaar-10_Assessing_ais_potential_to_assist_research/review]] — LLM의 자기 수정 한계가 AI의 연구 지원 능력 평가에서 중요한 제약 요소임을 시사한다.
- ⚖️ 반론/비판: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — LLM의 자기 수정 불가능성과 도구 지원을 통한 자기 수정 가능성 사이의 대조를 보여준다.
- ⚖️ 반론/비판: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — LLM의 자기 개선 능력에 대한 상반된 관점을 제시하여 한계와 가능성을 균형있게 이해할 수 있다.
- ⚖️ 반론/비판: [[papers/907_Is_AI_ready_to_mass-produce_lay_summaries_of_research_articl/review]] — LLM이 추론 자체를 자가 수정할 수 없다는 한계가 요약 품질 개선의 근본적 제약임을 보여준다
- 🏛 기반 연구: [[papers/182_Can_language_models_falsify_evaluating_algorithmic_reasoning/review]] — 대규모 언어모델의 추론 자기 교정 불가능성이 언어모델의 반례 생성 능력 한계의 근본적 원인을 제시한다
- ⚖️ 반론/비판: [[papers/397_Hallucinations_can_improve_large_language_models_in_drug_dis/review]] — LLM이 추론에서 자기 교정할 수 없다는 연구와 환각이 오히려 도움된다는 발견은 LLM 오류에 대한 상반된 관점을 제시한다.
- ⚖️ 반론/비판: [[papers/396_Hallucination_mitigation_using_agentic_ai_natural_language-b/review]] — 대규모 언어모델의 자기교정 불가능성이 에이전트 기반 환각 완화의 필요성을 더욱 강조한다.
- ⚖️ 반론/비판: [[papers/148_Axolotl_fairness_through_assisted_self-debiasing_of_large_la/review]] — LLM의 자기교정 능력에 대한 한계를 지적하여 편향 완화 접근법의 근본적 제약을 보여준다.
- ⚖️ 반론/비판: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM의 자기 수정 능력 한계를 보여주며 공유된 환각의 지속성 문제를 뒷받침한다
