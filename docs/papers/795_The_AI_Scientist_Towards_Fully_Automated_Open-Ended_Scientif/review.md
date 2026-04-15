---
title: "795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif"
authors:
  - "Chris Lu"
  - "Cong Lu"
  - "Robert Tjarko Lange"
  - "Jakob Foerster"
  - "Jeff Clune"
date: "2024"
doi: "10.48550/ARXIV.2408.06292"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)을 기반으로 하는 완전 자동화된 과학 연구 수행 시스템으로, 아이디어 생성에서 실험 수행, 논문 작성, 동료 검토까지 전체 과학 연구 프로세스를 자동으로 처리할 수 있다. 한 편의 논문 생성에 15달러 미만의 비용이 소요되며, 자동 리뷰 시스템이 인간 수준에 가까운 성능으로 논문 품질을 평가한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Research_Concept_Extraction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lu et al._2024_The AI Scientist Towards Fully Automated Open-Ended Scientific Discovery.pdf"
---

# The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

> **저자**: Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha | **날짜**: 2024 | **DOI**: [10.48550/ARXIV.2408.06292](https://doi.org/10.48550/ARXIV.2408.06292)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: The AI Scientist의 개념도 - 아이디어 생성부터 논문 작성 및 자동 리뷰까지의 전체 파이프라인*

대규모 언어모델(LLM)을 기반으로 하는 완전 자동화된 과학 연구 수행 시스템으로, 아이디어 생성에서 실험 수행, 논문 작성, 동료 검토까지 전체 과학 연구 프로세스를 자동으로 처리할 수 있다. 한 편의 논문 생성에 15달러 미만의 비용이 소요되며, 자동 리뷰 시스템이 인간 수준에 가까운 성능으로 논문 품질을 평가한다.

## Motivation

- **Known**: 최신 LLM들(GPT-4, Claude, Gemini 등)은 개별 연구 작업(논문 작성, 코딩, 아이디어 브레인스토밍)에서 인간 과학자의 보조 역할로 우수한 성능을 보이고 있음

- **Gap**: 그러나 기존 연구는 과학 연구 프로세스의 일부분만 자동화하였으며, 아이디어 생성부터 논문 작성까지 **전체 연구 사이클을 완전 자동화한 사례는 없음**. 기존 자동화 연구도 사전에 정의된 탐색 공간에 제한됨

- **Why**: 1970년대부터 과학 발견의 자동화를 목표로 해온 학문적 전통이 있으며, 최근 LLM의 코딩 능력 향상(Aider 등)이 이를 가능하게 함

- **Approach**: 
  1. LLM의 체인-오브-싱킹(chain-of-thought)과 자기성찰(self-reflection) 활용
  2. 자동화 코딩 어시스턴트(Aider)를 통한 실험 구현
  3. 진화 연산과 개방형 탐색(open-endedness) 원칙 적용
  4. 자동 논문 리뷰 시스템을 통한 품질 평가

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: ICLR 2022 OpenReview 데이터를 사용한 자동 리뷰 시스템의 성능 평가*

1. **완전 자동화 파이프라인 구현**: 아이디어 생성→실험 설계→코드 작성→실험 실행→논문 작성→자동 리뷰까지 인간 개입 없이 전체 프로세스를 자동화

2. **고품질 자동 리뷰 시스템**: ICLR 2022 데이터 기반 평가에서 65% vs 66% 균형잡힌 정확도(balanced accuracy)로 인간 리뷰어와 유사한 성능 달성

3. **비용 효율성**: 논문 1편당 $15 미만의 저비용으로 수백 편의 중간 품질 논문을 일주일 내에 생성 가능

4. **실제 논문 생성**: 확산 모델(diffusion modeling), 언어모델(language modeling), 그로킹(grokking) 등 3개 분야에서 실제 학회 수용 기준을 초과하는 논문 생성 달성

## How

![Figure 3](figures/fig3.webp)
*Figure 3: AI Scientist가 자동으로 생성한 "Adaptive Dual-Scale Denoising" 논문의 미리보기*

**3단계 주요 프로세스:**

### 1단계: 아이디어 생성 (Idea Generation)
- 기본 코드 템플릿에서 출발하여 다양한 연구 방향을 반복 생성
- 진화 연산 원칙에 따라 아이디어 아카이브를 누적
- 각 아이디어: 설명(description), 실험 계획(experiment plan), 재미(interestingness)/참신성(novelty)/실행가능성(feasibility) 점수 포함
- Semantic Scholar API를 통한 문헌 검색으로 참신성 검증

### 2단계: 실험 수행 (Experimental Iteration)
- Aider를 활용하여 아이디어를 실제 코드로 구현
- LLM이 지정한 계획에 따라 기본 템플릿 수정
- 실험 실행 결과 수집 (수치 점수 및 시각화 자료)
- 재현성과 해석 가능성 확보

### 3단계: 논문 작성 (Paper Write-up)
- LLM이 실험 결과를 바탕으로 LaTeX 형식의 전체 과학 논문 작성
- 표준 기계학습 학회 포맷 준수
- 결과 해석 및 토의 자동 생성

### 4단계: 자동 리뷰 및 평가
- LLM 기반 동료 리뷰 프로세스 실행
- 기준 초과 아이디어를 지속적인 발전을 위한 아카이브에 추가
- 피드백 기반 반복 개선 가능

## Originality

- **최초 성과**: 기존 연구는 하이퍼파라미터 탐색, 아키텍처 검색 등 특정 부분만 자동화하였으나, 본 논문은 **아이디어 생성부터 논문 작성까지 전체 과학 연구 사이클의 완전 자동화 달성**

- **LLM 에이전트 프레임워크의 혁신적 활용**: 체인-오브-싱킹, 자기성찰, 자동화 코딩(Aider)을 통합하여 과학적 창의성과 실행 능력을 동시에 구현

- **진화적 아이디어 아카이브**: 과거 연구 결과를 바탕으로 새로운 아이디어를 조건부로 생성하는 개방형 탐색 방식으로, 인간 과학 공동체의 누적 발전 프로세스를 모방

- **자동 리�뷰 시스템의 검증**: 실제 학회 데이터(ICLR 2022)로 자동 리뷰의 신뢰성을 입증 (인간 수준 성능)

- **실용적 적용 가능성**: 단순한 개념 증명이 아닌, 실제 작동하는 시스템으로 다수의 논문 생성

## Limitation & Further Study

- **실험 규모의 제한**: 계산 효율성을 위해 소규모 실험에 제한되어 있으나, 원칙적으로는 대규모 실험으로 확장 가능

- **도메인 의존성**: 현재 기계학습 분야에만 적용되었으며, 실험 자동 실행이 어려운 분야(실험 생물학, 재료 과학 등)의 확장에는 별도 기술 필요

- **논문 품질의 편차**: 수백 편의 논문 중 유의미한 기여도를 가진 논문의 비율, 완전히 새로운 발견의 정도에 대한 상세 분석 부재

- **자동 리뷰의 한계**: ICLR과 같은 특정 학회 데이터로 훈련되어 다른 분야나 학회 리뷰 기준으로의 일반화 가능성 불명확

- **윤리적 고려사항**: 대규모 자동 논문 생성으로 인한 학술출판 시스템 부담, 저작권, 과학적 엄밀성 기준에 대한 충분한 논의 필요

- **향후 연구 방향**:
  - 다양한 과학 분야로의 확장 (생물학, 물리학, 화학 등)
  - 인간 과학자와의 협업 시스템 개발
  - 자동 논문의 학술 출판 가능성 검증
  - 다단계 검증 메커니즘 강화

## Evaluation

- **Novelty (참신성)**: 4.5/5
  - 과학 발견의 완전 자동화는 처음 시도이나, 개별 기술들(LLM, 코드 생성, 자동 리뷰)은 기존 기술의 통합

- **Technical Soundness (기술적 건전성)**: 4/5
  - 시스템은 잘 설계되었으나, 논문 품질 평가 메트릭의 객관성과 충분성에 의문 여지 있음
  - 자동 리뷰의 ICLR 특정 데이터 의존성으로 인한 일반화 우려

- **Significance (중요도)**: 4.5/5
  - 과학 연구 자동화의 새로운 가능성을 제시하며, 저비용 대량 생성의 실현
  - 그러나 생성 논문의 실제 과학적 가치와 인용도에 대한 장기 검증 필요

- **Clarity (명확성)**: 4/5
  - 전체 파이프라인이 명확하게 설명되었으나, 실패 사례, 생성된 논문의 편향성에 대한 상세 분석 부족

- **Overall: 4.25/5**

**총평**: 본 논문은 대규모 언어모델의 능력을 과학 연구의 완전 자동화로 확장한 획기적 시도로, 저비용 고속도의 자동 연구 수행 가능성을 입증하였다. 다만, 생성 논문의 실제 학술적 가치, 다양한 도메인으로의 일반화 가능성, 과학 출판 시스템에 미칠 윤리적 영향에 대한 심층 분석이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — 노벨 튜링 챌린지의 거대한 비전이 AI Scientist의 구체적 구현을 위한 목표와 방향성을 제시한다
- ⚖️ 반론/비판: [[papers/081_Ai_scientists_fail_without_strong_implementation_capability/review]] — AI 과학자의 구현 능력 부족 지적이 완전 자동화 과학 발견 시스템의 현실적 한계를 비판적으로 제시한다
- 🔗 후속 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI Scientist-v2의 워크샵 수준 자동화가 기존 AI Scientist의 확장된 능력을 보여준다
- 🔗 후속 연구: [[papers/353_From_Automation_to_Autonomy_A_Survey_on_Large_Language_Model/review]] — AI의 과학적 자율성 발전을 이론적 분석에서 실제 구현 단계로 확장시킨다.
- 🔗 후속 연구: [[papers/857_Unlocking_the_Potential_of_AI_Researchers_in_Scientific_Disc/review]] — 완전 자동화된 과학 발견을 위한 AI 과학자의 구체적인 구현 사례를 제시한다
- 🧪 응용 사례: [[papers/749_Sequence_modeling_and_design_from_molecular_to_genome_scale/review]] — Evo의 genomic modeling 능력을 실제 과학적 발견에 적용하는 자동화된 연구 시스템의 사례이다.
- 🔗 후속 연구: [[papers/064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha/review]] — 자동화된 과학 발견을 완전 자율적이고 개방형 과학 연구로 확장하는 발전된 비전을 제시한다
- 🧪 응용 사례: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — AI Scientist의 완전 자동화된 과학 발견 접근법이 AIRS-Bench 벤치마크 검증에 실제 적용될 수 있다.
- 🏛 기반 연구: [[papers/086_AI-Researcher_Autonomous_Scientific_Innovation/review]] — 완전 자동화된 과학 발견의 기반이 되는 AI 과학자 시스템을 제시한다
- 🔗 후속 연구: [[papers/038_A_vision_for_auto_research_with_llm_agents/review]] — 완전 자동화된 과학적 발견으로 자동 연구 비전을 구체적으로 구현한 연구이다.
- 🧪 응용 사례: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — RL로 훈련된 추론 능력이 자동화된 과학 연구에서 실제로 활용될 수 있는 가능성을 보여준다.
- 🧪 응용 사례: [[papers/066_Agentic_Personas_for_Adaptive_Scientific_Explanations_with_K/review]] — 에이전틱 페르소나 기반 적응형 설명이 자동화된 과학 발견에서 실제로 활용될 수 있다.
- 🧪 응용 사례: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — 완전 자동화된 과학 연구에서 자기검증 메커니즘이 AI 과학자의 신뢰성 확보에 직접 적용될 수 있다.
- 🔗 후속 연구: [[papers/718_Scientific_discovery_in_the_age_of_artificial_intelligence/review]] — AI 시대 과학적 발견의 현재 상황을 완전 자동화된 미래 과학자로 발전시킨 비전
- 🔗 후속 연구: [[papers/137_Autonomous_Agents_for_Scientific_Discovery_Orchestrating_Sci/review]] — 과학 발견 자율 에이전트의 이론적 프레임워크가 완전 자동화된 과학 연구 시스템으로 구체화됨
- 🔗 후속 연구: [[papers/044_Accelerating_Scientific_Research_with_Gemini_Case_Studies_an/review]] — Gemini를 활용한 과학 연구 협력 사례가 완전 자동화된 AI 과학자 시스템으로 발전함
- 🔗 후속 연구: [[papers/089_Aigs_Generating_science_from_ai-powered_automated_falsificat/review]] — AIGS의 반증 기반 자율 연구 방법론을 실제 과학 발견에 완전히 적용한 발전된 형태의 AI 과학자 시스템이다
- 🔗 후속 연구: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — 완전 자동화된 오픈 엔디드 과학 발견 연구가 LLM을 통한 과학 변환의 구체적인 구현 사례로 발전되었다
- 🧪 응용 사례: [[papers/1093_The_fifth_era_of_science_Artificial_scientific_intelligence/review]] — 과학의 새로운 패러다임 이론을 완전 자동화된 과학적 발견이라는 구체적 구현 사례로 보여준다
- 🔗 후속 연구: [[papers/056_Advancing_the_scientific_method_with_large_language_models_F/review]] — 과학 방법론 지원에서 완전 자동화된 과학 발견으로 발전하는 궁극적 목표를 제시한다
- 🔗 후속 연구: [[papers/575_Nobel_Turing_Challenge_creating_the_engine_for_scientific_di/review]] — AI Scientist의 구체적 구현이 노벨 튜링 챌린지의 실현 가능성을 입증하는 중요한 이정표 역할을 한다
- 🔄 다른 접근: [[papers/834_Towards_Scientific_Discovery_with_Generative_AI_Progress_Opp/review]] — 생성형 AI의 과학 발견 진전과 기회 분석이 AI Scientist의 구체적 구현과 상호보완적 관점을 제공한다
- ⚖️ 반론/비판: [[papers/081_Ai_scientists_fail_without_strong_implementation_capability/review]] — AI Scientist의 강한 구현 능력 부족 지적이 완전 자동화 과학 발견 시스템의 한계를 비판적으로 분석한다
- ⚖️ 반론/비판: [[papers/321_Evaluating_Sakanas_AI_Scientist_Bold_Claims_Mixed_Results_an/review]] — Sakana AI Scientist의 원본 시스템에 대한 체계적 평가로 자율적 연구의 현실적 한계를 드러낸다
- ⚖️ 반론/비판: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 완전 자동화된 과학 발견과 대조적으로, 인간 의료진과의 협력이 필수인 의료 AI의 한계를 보여준다.
- 🏛 기반 연구: [[papers/352_From_AI_for_Science_to_Agentic_Science_A_Survey_on_Autonomou/review]] — 완전 자동화된 과학 연구의 원본 시스템으로서 에이전틱 사이언스의 실제 구현 기반을 제공한다
- 🔄 다른 접근: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 완전 자동화된 오픈엔드 과학 발견에 대한 다른 시각과 접근을 제시하여, AI Scientist 시스템과 비교 분석 가능
- 🔗 후속 연구: [[papers/326_Exp-bench_Can_ai_conduct_ai_research_experiments_arXiv_prepr/review]] — 완전 자동화된 과학 연구 시스템으로, EXP-Bench에서 평가한 실험 수행 능력의 한계를 극복하는 더 발전된 AI 과학자 구현을 보여준다
- 🔗 후속 연구: [[papers/825_Towards_an_AI_co-scientist/review]] — 완전 자동화된 과학적 발견을 다루는 AI Scientist의 연구 범위를 다중 에이전트 협업과 가설 생성-개선 사이클로 더욱 정교하게 발전시킴
- 🔄 다른 접근: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — AI 과학자의 완전 자동화라는 공통 목표를 가지지만 수학 vs 일반 과학 연구라는 다른 도메인에 특화된 접근법을 사용한다.
- 🏛 기반 연구: [[papers/059_Agent_Laboratory_Using_LLM_Agents_as_Research_Assistants/review]] — 완전 자동화된 과학 발견의 이론적 기반을 바탕으로 인간의 연구 아이디어 실행을 지원하는 실용적 프레임워크를 구현한다
- 🔗 후속 연구: [[papers/1094_Towards_a_Medical_AI_Scientist/review]] — 완전 자동화된 과학 발견에서 임상 의학 연구에 특화된 AI 과학자로의 도메인별 특화 발전을 보여준다
- 🔗 후속 연구: [[papers/578_Novelseek_When_agent_becomes_the_scientistbuilding_closed-lo/review]] — AI Scientist의 완전 자동화 과학 발견을 NovelSeek이 다중 에이전트 협력을 통해 실용적으로 구현한 확장
- 🔄 다른 접근: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — 두 시스템 모두 완전 자동화된 과학 발견을 목표로 하지만 v2는 워크숍 수준, 원래 AI Scientist는 기초 수준을 다룬다.
- 🔗 후속 연구: [[papers/436_InternAgent_When_Agent_Becomes_the_Scientist_--_Building_Clo/review]] — AI Scientist의 완전 자동화 과학 발견 비전을 InternAgent가 다중 에이전트와 인간 피드백을 통해 실용적으로 구현함
- 🧪 응용 사례: [[papers/146_Autosdt_Scaling_data-driven_discovery_tasks_toward_open_co-s/review]] — 완전 자동화된 과학 연구 시스템으로, 데이터 주도 발견 능력을 실제 과학 연구에 적용한 사례입니다.
- 🧪 응용 사례: [[papers/601_PaperBanana_Automating_Academic_Illustration_for_AI_Scientis/review]] — AI 과학자의 시각화 병목 문제를 해결하기 위해 에이전트 기반 자동 일러스트레이션 생성이라는 구체적 솔루션을 제공한다.
- 🔗 후속 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — AI Scientist는 완전 자동화된 과학 연구를 목표로 하여, ResearchGym에서 발견한 능력-신뢰성 격차를 해결하는 더 발전된 시스템을 제시한다
- 🏛 기반 연구: [[papers/550_MLRC-Bench_Can_Language_Agents_Solve_Machine_Learning_Resear/review]] — AI 과학자의 실제 연구 능력 평가를 위한 기초적인 벤치마킹 방법론을 제공한다.
- 🔗 후속 연구: [[papers/021_A_Review_on_Scientific_Knowledge_Extraction_using_Large_Lang/review]] — 의료 문헌 분석에서 완전 자동화된 과학 발견으로 확장된 미래 비전을 보여준다.
- 🧪 응용 사례: [[papers/1087_Gpt4_is_slightly_helpful_for_peer-review_assistance_A_pilot/review]] — 완전 자동화된 과학 발견에서 GPT-4의 피어리뷰 보조 기능이 실제로 적용되는 사례를 제공한다.
