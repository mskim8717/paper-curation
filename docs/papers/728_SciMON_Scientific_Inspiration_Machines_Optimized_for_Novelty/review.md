---
title: "728_SciMON_Scientific_Inspiration_Machines_Optimized_for_Novelty"
authors:
  - "Qingyun Wang"
  - "Doug Downey"
  - "Heng Ji"
  - "Tom Hope"
date: "2024"
doi: "10.18653/v1/2024.acl-long.18"
arxiv: ""
score: 4.0
essence: "과학 논문에서 자동으로 추출한 맥락을 기반으로 문헌에 근거한 새로운 과학적 아이디어를 생성하는 SCIMON 프레임워크를 제시하며, 반복적인 참신성(novelty) 최적화를 통해 LLM의 아이디어 생성 능력을 향상시킨다."
tags:
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Research_Literature_Analysis_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2024_SciMON Scientific Inspiration Machines Optimized for Novelty.pdf"
---

# SciMON: Scientific Inspiration Machines Optimized for Novelty

> **저자**: Qingyun Wang, Doug Downey, Heng Ji, Tom Hope | **날짜**: 2024 | **DOI**: [10.18653/v1/2024.acl-long.18](https://doi.org/10.18653/v1/2024.acl-long.18)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: SCIMON takes background context and gen-*

과학 논문에서 자동으로 추출한 맥락을 기반으로 문헌에 근거한 새로운 과학적 아이디어를 생성하는 SCIMON 프레임워크를 제시하며, 반복적인 참신성(novelty) 최적화를 통해 LLM의 아이디어 생성 능력을 향상시킨다.

## Motivation

- **Known**: 기존 Literature-Based Discovery(LBD) 연구는 약물-질병 같은 개념 쌍 사이의 이진 링크 예측에만 초점을 맞춰왔으며, 최근 GPT-4 같은 LLM들의 과학 분야 성능 향상에도 불구하고 개방형 아이디어 생성에서는 제한적이다.
- **Gap**: 기존 LBD 방식은 과학자들이 고려하는 문제 맥락, 제약조건, 동기 등 뉘앙스 있는 맥락을 포착하지 못하며, LLM의 생성 아이디어의 참신성(novelty)과 기술적 깊이(technical depth)를 명시적으로 최적화하지 않는다.
- **Why**: 과학적 진전을 위해 기존 문헌에 근거하면서도 충분히 참신한 아이디어 생성이 필수적이며, 이는 인간 과학자의 사고 과정을 모방하여 AI 기반 연구 지원 시스템을 구축할 수 있게 한다.
- **Approach**: 배경 맥락에서 문헌의 '영감(inspirations)'을 동적으로 검색하고, 생성된 아이디어를 기존 연구와 반복적으로 비교하여 참신성이 충분해질 때까지 아이디어를 갱신하는 프레임워크를 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Architecture overview. Our models retrieve inspirations and then pass the background input and retrieved*

- **새로운 문제 설정 제안**: 이진 링크 예측을 넘어 자연어 아이디어 생성이라는 개방형 문제 설정 도입
- **자동 학습 데이터 수집**: 정보 추출(IE) 모델을 활용하여 과학 논문에서 문제-아이디어 쌍 자동 추출
- **반복적 참신성 최적화**: 생성 아이디어를 기존 문헌과 비교하고 피드백을 통해 반복적으로 참신성 향상
- **포괄적 인간 평가**: 도메인 전문가를 통한 관련성(relevance), 유용성(utility), 참신성(novelty), 기술적 깊이(technical depth) 평가
- **실증적 한계 도출**: GPT-4가 생성한 아이디어가 여전히 참신성과 깊이에서 실제 과학 논문에 미치지 못함을 입증

## How

![Figure 2](figures/fig2.webp)

*Figure 2: Architecture overview. Our models retrieve inspirations and then pass the background input and retrieved*

- 정보 추출(IE)을 이용한 자동 데이터 수집: 배경 문맥(문제/동기)과 타겟 아이디어를 논문에서 추출
- 동적 영감 검색(Inspiration Retrieval): 의미적 이웃, 지식그래프(KG) 이웃, 인용 이웃 등 세 가지 방식으로 관련 논문 검색
- LLM 미세 조정(Fine-tuning) 및 인-컨텍스트 학습: 추출된 데이터로 언어 모델 학습
- 반복적 참신성 부스팅: 생성 아이디어가 기존 연구와 겹치는지 확인하고 더 참신하도록 갱신하는 루프 실행
- 인-컨텍스트 대조 학습(Contrastive In-Context Learning): 배경 맥락과 대비되는 아이디어 생성 장려

## Originality

- 기존의 이진 링크 예측 방식을 자연어 생성 문제로 재설정하여 근본적인 패러다임 전환
- 과학 논문에서 문제-아이디어 쌍을 자동 추출하는 체계적 데이터 수집 방법론 개발
- 생성 후 피드백을 통한 반복적 참신성 최적화라는 새로운 모델링 기법 제안
- AI/NLP 영역에서 포괄적 인간 평가 기준을 통해 과학 아이디어 생성 능력 첫 종합 평가 수행

## Limitation & Further Study

- 생성된 아이디어가 여전히 실제 과학 논문에 비해 참신성, 깊이, 유용성이 현저히 낮음
- 평가가 AI/NLP 분야에 치중되어 있으며 생물의학 도메인으로의 일반화 검증이 부분적
- 참신성 임계값(novelty threshold) 설정이 휴리스틱 기반으로 보임
- 후속 연구: (1) 참신성 최적화 메커니즘의 더 정교한 설계, (2) 다양한 과학 분야로의 확장, (3) 인간과의 상호작용을 통한 반복적 개선, (4) 생성된 아이디어의 실제 과학적 검증 가능성 탐색

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 기존 LBD의 근본적 한계를 인식하고 개방형 자연어 아이디어 생성으로 문제를 재설정한 매우 참신한 연구이며, 반복적 참신성 최적화라는 새로운 기법을 도입했으나, 생성된 아이디어 품질이 여전히 실무적 수준에 미치지 못하는 것이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — 과학적 아이디어의 참신성 평가를 위한 다른 접근 방식을 제시합니다.
- 🧪 응용 사례: [[papers/585_Openai_o1_system_card/review]] — OpenAI o1의 고급 추론 능력을 참신성 최적화에 활용합니다.
- 🏛 기반 연구: [[papers/391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a/review]] — 지식 그래프 기반 아이디어 생성의 참신성 최적화에 활용됩니다.
- 🔗 후속 연구: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — 과학적 영감 기계 최적화를 통해 Nova의 반복적 아이디어 생성 방법론을 참신성뿐만 아니라 과학적 영감까지 포함하는 더 포괄적인 시스템으로 확장함
- 🔄 다른 접근: [[papers/494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea/review]] — 발산적 사고 평가와 신성 최적화가 서로 다른 관점에서 과학적 창의성을 측정한다
- 🔗 후속 연구: [[papers/391_Graph_of_ai_ideas_Leveraging_knowledge_graphs_and_llms_for_a/review]] — 참신성 최적화된 아이디어 생성을 위한 지식 그래프 활용 방안을 확장합니다.
- 🏛 기반 연구: [[papers/729_Scipip_An_llm-based_scientific_paper_idea_proposer/review]] — 참신성 최적화된 아이디어 생성의 방법론적 기반을 제공합니다.
- ⚖️ 반론/비판: [[papers/820_Toward_Reliable_Scientific_Hypothesis_Generation_Evaluating/review]] — 참신성 추구와 신뢰성 확보 간의 균형점을 찾는 대조적 관점을 제시합니다.
- 🏛 기반 연구: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — 아이디어 생성 능력 평가에서 참신성 최적화 방법론의 기반을 제공합니다.
- 🔄 다른 접근: [[papers/777_Structuring_scientific_innovation_A_framework_for_modeling_a/review]] — 문제-방법 구조 분석과 신성 최적화가 서로 다른 방식으로 과학적 혁신을 측정한다
- 🏛 기반 연구: [[papers/585_Openai_o1_system_card/review]] — 참신성 최적화를 위한 고급 추론 능력의 기반을 제공합니다.
- 🔗 후속 연구: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 참신성에 최적화된 과학적 영감 머신이 지식 그래프 기반 아이디어 생성을 참신성 중심으로 발전시킨 접근법이다.
