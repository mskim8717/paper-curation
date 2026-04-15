---
title: "833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for"
authors:
  - "Lei Wang"
  - "Chen Ma"
  - "Xueyang Feng"
  - "Zeyu Zhang"
  - "Hao Yang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.4
essence: "OpenAI-o1과 DeepSeek-R1 같은 추론 대형언어모델(RLLMs)의 성공은 장문의 체인오브쏘트(Long CoT) 특성에 기인하며, 본 논문은 Long CoT와 전통적 Short CoT의 구별, 핵심 특성, 그리고 관련 현상들에 대한 최초의 종합적 분석을 제공한다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Retrieval-Augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Towards reasoning era A survey of long chain-of-thought for reasoning large language models.pdf"
---

# Towards reasoning era: A survey of long chain-of-thought for reasoning large language models

> **저자**: Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp) *Long CoT와 Short CoT의 구별: 깊은 추론(Deep Reasoning), 광범위한 탐색(Extensive Exploration), 실현 가능한 반성(Feasible Reflection)의 세 가지 핵심 특성*

OpenAI-o1과 DeepSeek-R1 같은 추론 대형언어모델(RLLMs)의 성공은 장문의 체인오브쏘트(Long CoT) 특성에 기인하며, 본 논문은 Long CoT와 전통적 Short CoT의 구별, 핵심 특성, 그리고 관련 현상들에 대한 최초의 종합적 분석을 제공한다.

## Motivation

- **Known**: 최근 OpenAI-o1, DeepSeek-R1 등 RLLMs는 수학, 코딩 등 복잡한 도메인에서 뛰어난 성능을 보이며, 추론 시간 스케일링(inference-time scaling)을 활용한 Long CoT가 핵심 요소임이 입증되고 있음.

- **Gap**: Long CoT에 대한 포괄적 종합 분석이 부재하여, Short CoT와의 명확한 구별이 없고, "과도한 사고(overthinking)"와 "추론 시간 스케일링"에 대한 논의가 정리되지 않음.

- **Why**: Long CoT의 특성, 출현 메커니즘, 관련 현상들(emergence, overthinking, "Aha Moment" 등)을 체계적으로 이해할 필요가 있음.

- **Approach**: Long CoT를 형식화하고, Short CoT와의 차이를 수식으로 정의한 후, 세 가지 핵심 특성(deep reasoning, extensive exploration, feasible reflection)으로 분류하여 관련 연구를 조직화함.

## Achievement

![Figure 1](figures/fig1.webp) *지난 3년간 선택된 Long CoT의 진화: 깊은 추론, 실현 가능한 반성, 광범위한 탐색의 세 가지 특성을 색상 분기로 표현*

![Figure 3](figures/fig3.webp) *Long CoT의 분류법: 깊은 추론 형성(자연어, 구조화된 언어, 잠재 공간), 깊은 추론 학습(모방학습, 자기학습), 실현 가능한 반성(전체 피드백, 프로세스 피드백), 광범위한 탐색(탐색 스케일링, 내부/외부 탐색)*

1. **체계적 구별**: Long CoT를 형식적으로 정의하고 Short CoT와의 차이를 수식화함. 
   - Short CoT: $\text{CoT}_S = R(\{n_i\}^k_{i=1}|(k \leq B_s) \land (j=1 \Leftrightarrow \forall i \leq k, n_i \to n_{i+j}) \land (\forall i \neq j \leq k, n_i \neq n_j))$
   - Long CoT는 경계 $B_l \gg B_s$로 확장하며, 깊이 제약을 완화함

2. **세 가지 핵심 특성 정의**:
   - **Deep Reasoning**: 복잡한 구조 전반에서 엄밀한 논리적 분석을 수행하는 능력
   - **Extensive Exploration**: 평행 불확실 노드 생성 및 알려진 논리에서 미지의 논리로의 전환
   - **Feasible Reflection**: 논리적 연결의 피드백 및 정제

3. **핫 현상의 체계적 분석**: overthinking, inference-time scaling, "Aha Moment" 등의 출현 메커니즘 설명

## How

![Figure 5](figures/fig5.webp) *깊은 추론의 세 가지 주요 형식: 자연어(CoT, MathPrompter), 구조화된 언어(PoT, CoC), 잠재 공간(Quiet-STaR, PlanningTokens)*

**Deep Reasoning Formation (깊은 추론 형성)**:
- **자연어 형식**: 자연 언어로 단계별 추론을 명시적으로 표현 (CoT, MathPrompter, CodeI/O)
- **구조화된 언어**: 프로그래밍 언어나 형식 논리로 표현하여 검증성 강화 (PoT, CoC, ENVISIONS)
- **잠재 공간**: 모델의 내부 표현 공간에서 추론 수행 (Quiet-STaR, RecurrentBlock, LTMs)

**Deep Reasoning Learning (깊은 추론 학습)**:
- **모방학습**: 장문 추론 데이터셋으로 감독학습 (GSM8K, AceMath, STILL-2)
- **자기학습**: 강화학습/자기보상을 통한 자동 개선 (STaR, ReST, CPO, BOLT)

**Feasible Reflection (실현 가능한 반성)**:
- **전체 피드백**: 최종 답변의 정확성 평가 (Self-Critique, Critic-RM)
- **프로세스 피드백**: 중간 단계의 정확성 평가 (ReAct, Math-Shepherd, PRIME)

**Extensive Exploration (광범위한 탐색)**:
- **탐색 스케일링**: 추론 길이 증가로 성능 향상 (inference-time scaling)
- **내부 탐색**: 모델 내부에서 여러 경로 병렬 생성 (Self-Consistency, Tree of Thought)
- **외부 탐색**: 도구/환경과의 상호작용을 통한 탐색 (ReAct, Tool-use)

## Originality

- **최초의 종합 분석**: Long CoT에 대한 첫 번째 대규모 분석 설문지로, 2,000여 개의 관련 논문을 체계화함
- **형식적 정의와 분류**: Long CoT와 Short CoT를 수학적으로 구별하고, 세 가지 핵심 특성으로 통일된 분류 체계 제시
- **핫 현상의 설명**: overthinking과 inference-time scaling 같은 실제 현상들을 이론적으로 조직화하고 설명
- **실용적 리소스**: 오픈 소스 프레임워크와 데이터셋을 종합하여 후속 연구 기반 제공

## Limitation & Further Study

- **다중모달 추론**: 현재 분석이 텍스트 기반 추론에 집중되어 있으며, 이미지/비디오/오디오를 포함한 다중모달 Long CoT 확장 필요
- **효율성 개선**: Long CoT의 높은 계산 비용(긴 출력, 여러 경로 탐색)을 해결하기 위한 압축, 스케줄링, 조기 종료 기법 개발
- **지식 강화**: 외부 지식베이스, 검색, 도구 활용을 통한 Long CoT 강화 방향
- **이론적 이해**: overthinking의 경계(언제 추가 추론이 해로운가), 최적 탐색 깊이 분석
- **일반화성**: 현재 연구가 수학/코딩에 집중되어 있으며, 보다 다양한 도메인에서의 적용성 검증 필요
- **평가 지표**: Long CoT의 품질을 정량화할 새로운 메트릭 개발 (길이 vs. 정확도의 트레이드오프 측정)

## Evaluation

- **Novelty (창의성)**: 4.5/5 
  - Long CoT에 대한 최초의 종합 분석이며 형식적 구별 제시, 하지만 개별 기법들은 기존 연구임

- **Technical Soundness (기술적 건전성)**: 4/5
  - 수식화와 분류 체계가 합리적이나, 일부 현상(overthinking, Aha Moment)의 설명이 개념적 수준에 머물러 있음

- **Significance (중요성)**: 5/5
  - RLLMs의 성장과 맞춘 매우 시의적절한 설문이며, 연구 커뮤니티에 큰 기여 가능

- **Clarity (명확성)**: 4/5
  - 전반적으로 잘 조직되었으나, 세 가지 특성 간 상호작용과 경계가 다소 모호함

- **Overall**: 4.4/5

**총평**: 본 논문은 RLLMs의 중심 기술인 Long CoT를 처음으로 체계적으로 분석한 중요한 종합 설문으로, 명확한 분류 체계와 풍부한 사례를 제공하여 후속 연구의 지도를 제시한다. 다만 이론적 깊이와 일부 현상의 설명이 추가 발전의 여지를 남긴다.

## Related Papers

- 🧪 응용 사례: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — Long CoT의 추론 능력 분석이 OpenAI o1의 복잡한 추론 작업 성능 평가에 핵심적인 평가 기준을 제공함
- 🏛 기반 연구: [[papers/458_Language_agents_mirror_human_causal_reasoning_biases/review]] — Long CoT 추론 과정에서 나타나는 편향 패턴을 이해하기 위해 언어 에이전트의 인과관계 추론 편향 연구가 필수적임
- 🏛 기반 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1의 복잡한 추론 능력 평가를 위해 Long CoT 특성에 대한 체계적 분석이 필수적임
- 🧪 응용 사례: [[papers/458_Language_agents_mirror_human_causal_reasoning_biases/review]] — 언어 에이전트의 인과관계 추론 편향 분석이 Long CoT에서 나타나는 추론 패턴과 편향을 이해하는 핵심 도구로 활용됨
- 🔗 후속 연구: [[papers/028_A_survey_of_reasoning_with_foundation_models/review]] — 기본 추론을 넘어 복잡한 장기 추론 과정에 특화된 심화 연구로 발전한다
- 🔗 후속 연구: [[papers/036_A_survey_on_transformer_context_extension_Approaches_and_eva/review]] — 긴 사고 연쇄 추론을 통해 확장된 컨텍스트를 더욱 효과적으로 활용하여 복잡한 추론 과정을 수행할 수 있는 방법론을 제시한다.
