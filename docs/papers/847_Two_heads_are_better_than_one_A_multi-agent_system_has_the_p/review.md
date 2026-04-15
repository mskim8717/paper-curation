---
title: "847_Two_heads_are_better_than_one_A_multi-agent_system_has_the_p"
authors:
  - "Seyedali Mirjalili"
  - "Seyed Mohammad Mirjalili"
  - "Andrew Lewis"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "LLM 기반 multi-agent 시스템 VIRSCI를 제안하여 실제 과학 연구의 협업 특성을 모방함으로써 단일 에이전트 시스템보다 혁신적인 과학 아이디어 생성을 향상시킨다."
tags:
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Automated_Scientific_Analysis_Tools"
  - "sub/Scientific_Knowledge_Evaluation_LLMs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Mirjalili et al._2024_Two heads are better than one A multi-agent system has the potential to improve scientific idea gen.pdf"
---

# Two heads are better than one: A multi-agent system has the potential to improve scientific idea generation

> **저자**: Seyedali Mirjalili, Seyed Mohammad Mirjalili, Andrew Lewis | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2410.09403](https://arxiv.org/abs/2410.09403)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The proposed LLM-based multi-agent system, VIRSCI, includes five key steps: Collaborator Selection,*

LLM 기반 multi-agent 시스템 VIRSCI를 제안하여 실제 과학 연구의 협업 특성을 모방함으로써 단일 에이전트 시스템보다 혁신적인 과학 아이디어 생성을 향상시킨다.

## Motivation

- **Known**: LLM을 기반으로 한 AI Scientist, ResearchTown, HypoGen 등의 자동 과학 발견 도구들이 가설 생성과 실험 설계를 수행하고 있다. 그러나 대부분 단일 에이전트 시스템이거나 과도하게 단순화된 협업 프레임워크를 사용한다.
- **Gap**: 기존 방법들이 실제 과학 연구의 역동적인 팀 협업과 복잡한 관계를 제대로 반영하지 못하며, multi-agent 협업 메커니즘에 대한 충분한 통찰이 부족하다.
- **Why**: 과학 진전의 가속화를 위해 혁신적인 도구가 필요하며, 실제 과학 연구는 다양한 전문가가 팀을 이루어 협력하는 특성을 가지고 있기 때문에 이를 반영한 자동 발견 시스템이 중요하다.
- **Approach**: Virtual Scientists(VIRSCI)라는 LLM 기반 multi-agent 시스템을 제안하여, 실제 과학자의 배경과 발표 논문을 기반으로 생성한 virtual scientist들이 협업 선택, 주제 토론, 아이디어 생성, 참신성 평가, 초록 생성의 5단계를 거쳐 과학 아이디어를 생성한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: Evaluation of abstracts using our overall nov-*

- **multi-agent 시스템 성능**: 단일 에이전트 대비 contemporary research와의 alignment에서 +13.8%, 잠재적 영향력에서 +44.1% 향상
- **과학 연구 생태계 구축**: 실제 과학자 데이터를 기반으로 한 digital twin으로서 과거 논문 데이터베이스와 현대 논문 데이터베이스를 포함
- **혁신적 평가 메트릭**: 과거 논문과의 비유사성, 연구 트렌드 정렬도, 현대 연구에 대한 잠재적 영향력의 3가지 관점에서 참신성 평가
- **협업 메커니즘 분석**: inter-team과 intra-team 토론 메커니즘을 통해 에이전트 간 커뮤니케이션 위상을 개선하고 실제 과학 협업과의 정렬 검증

## How

![Figure 1](figures/fig1.webp)

*Figure 1: The proposed LLM-based multi-agent system, VIRSCI, includes five key steps: Collaborator Selection,*

- **Collaborator Selection**: 팀 리더가 협업 이력과 학술 소셜 네트워크를 활용하여 기존 공동 저자 중에서 선택(exploit)하고 관심사가 일치하는 새로운 협력자 탐색(explore)
- **Topic Selection**: 팀원들이 공통 관심 주제에 대해 토론하며, 합의가 이루어질 때까지 진행되거나 관심 없는 팀원은 자유롭게 퇴출 가능
- **Idea Generation**: 과거 논문 데이터베이스에서 관련 논문 검색 후 inter-team(외부 에이전트에게 조언 요청)과 intra-team(팀 내 토론) 토론을 반복적으로 수행
- **Novelty Assessment**: 생성된 아이디어들을 투표를 통해 평가하고 가장 참신한 아이디어 선택
- **Abstract Generation**: 선택된 아이디어를 종합적인 초록으로 발전시키되, 과거 논문과의 유사도를 검사하여 자가 평가
- **Scientific Research Ecosystem**: 특정 시점(예: 2024년 1월 1일)의 연구 커뮤니티의 digital twin으로서 virtual scientist들, 과거 논문 데이터베이스, 현대 논문 데이터베이스 포함

## Originality

- **첫 번째 multi-agent 과학 협업 시스템**: 실제 데이터 기반 role-playing 및 객관적 평가가 가능한 scientific research ecosystem과 함께 제안된 첫 번째 종합적 multi-agent 시스템
- **inter- 및 intra-team 토론 메커니즘**: 기존 group discussion과 달리 'Invitation Mechanism'을 통해 팀 외부의 전문가 조언을 활용하면서도 팀 내 다양성을 균형있게 유지", '**과학 생태계 기반 평가**: 과거 논문과의 비교뿐만 아니라 미래 논문(contemporary research)과의 정렬도를 평가하여 아이디어의 실제 영향력과 참신성 검증
- **Science of Science 원리 검증**: 팀 구성, 토론 횟수 등의 요인이 아이디어 생성에 미치는 영향을 체계적으로 분석하고 Science와 Nature 등의 top venue 연구 결과와 정렬 확인

## Limitation & Further Study

- **Scope의 제한**: 현재 실험이 computer science 등 특정 분야에 집중되어 있을 가능성이 있으며, 자연과학이나 실험 과학으로의 확장 가능성 검토 필요
- **Virtual scientist의 대표성**: 실제 과학자의 배경을 기반으로 하지만, LLM의 hallucination이나 편향이 가상 과학자의 특성에 영향을 미칠 수 있음
- **평가 메트릭의 객관성**: 참신성 평가가 자동으로 이루어지지만, 실제 과학 커뮤니티의 정성적 판단과의 차이 가능성
- **Long-term collaboration 미모델링**: 현재 시스템은 단기 프로젝트를 가정하며, 장기간의 팀 진화와 축적된 협업 경험 반영 부족
- **후속 연구**: (1) 다양한 학문 분야로 VIRSCI 적용 확대, (2) 실제 생성된 아이디어의 과학 커뮤니티 수용도 평가, (3) 팀 다양성과 성과의 최적 조합 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 multi-agent 시스템을 통해 실제 과학 협업을 현실적으로 모방하고, 혁신적인 아이디어 생성을 입증한 의미 있는 연구이다. 특히 실제 데이터 기반의 평가 생태계와 협업 메커니즘이 독창적이며, Science of Science 원리와의 정렬이 시스템의 신뢰성을 강화한다.

## Related Papers

- 🔗 후속 연구: [[papers/518_Many_Heads_Are_Better_Than_One_Improved_Scientific_Idea_Gene/review]] — 과학 아이디어 생성에서 다중 에이전트 협력의 효과를 더욱 발전시킨 연구이다.
- 🔄 다른 접근: [[papers/038_A_vision_for_auto_research_with_llm_agents/review]] — LLM 에이전트 기반 자동 연구의 다른 접근법으로 다중 에이전트 협력을 제시한다.
- 🏛 기반 연구: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — 다중 에이전트 애플리케이션의 기반 프레임워크를 제공한다.
- 🔄 다른 접근: [[papers/038_A_vision_for_auto_research_with_llm_agents/review]] — 자동 연구의 다른 접근법으로 다중 에이전트 협력을 통한 과학 아이디어 생성을 제시한다.
