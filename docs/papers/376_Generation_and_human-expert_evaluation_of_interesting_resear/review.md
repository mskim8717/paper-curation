---
title: "376_Generation_and_human-expert_evaluation_of_interesting_resear"
authors:
  - "Anil K. Jain"
  - "M. Narasimha Murty"
  - "Patrick J. Flynn"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "SciMuse는 5,800만 개의 과학논문으로부터 구축한 knowledge graph와 GPT-4를 활용하여 개인화된 연구 아이디어를 생성하고, 100명 이상의 연구 그룹 리더의 평가를 통해 AI 생성 아이디어의 질을 검증하는 대규모 시스템이다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Research_Concept_Extraction"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jain et al._2024_Generation and human-expert evaluation of interesting research ideas using knowledge graphs and larg.pdf"
---

# Generation and human-expert evaluation of interesting research ideas using knowledge graphs and large language models

> **저자**: Anil K. Jain, M. Narasimha Murty, Patrick J. Flynn | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2405.17044](https://arxiv.org/abs/2405.17044)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. SciMuse suggests research ideas or collaborations using a knowledge graph and GPT-4. (a), Knowledge*

SciMuse는 5,800만 개의 과학논문으로부터 구축한 knowledge graph와 GPT-4를 활용하여 개인화된 연구 아이디어를 생성하고, 100명 이상의 연구 그룹 리더의 평가를 통해 AI 생성 아이디어의 질을 검증하는 대규모 시스템이다.

## Motivation

- **Known**: AI 시스템이 인간이 단독으로 생각하지 못한 새로운 연구 아이디어를 영감을 줄 수 있으며, knowledge graph를 사용하여 미래 연구 방향을 예측하거나 신흥 연구의 잠재적 영향을 평가할 수 있다는 것이 알려져 있다.
- **Gap**: 기존 연구는 소규모 평가(6-10명의 PhD 학생)만 수행했으므로, 실제 연구 프로젝트를 정의하고 평가하는 경험 많은 연구 리더들의 관점이 부족했다.
- **Why**: 과학 논문의 급속한 증가로 인해 연구자들이 새로운 학제간 아이디어를 발견하기 어려워지고 있으며, 경험 있는 연구자들의 평가를 통해 AI 생성 아이디어의 실제 가치를 검증하는 것이 AI의 과학 발견 활용 가능성을 이해하는 데 중요하다.
- **Approach**: 123,128개의 과학 개념으로 이루어진 대규모 knowledge graph를 구축하고, 각 연구자의 최근 출판물로부터 개인화된 부분 그래프를 추출한 후, GPT-4의 self-reflection 기법을 활용하여 두 연구자 간의 협력 연구 아이디어를 생성한다. 생성된 4,451개의 아이디어를 110명의 Max Planck 연구 리더가 평가하고, 이 데이터를 통해 supervised neural network와 zero-shot LLM 랭킹으로 관심도를 예측한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Large-scale human evaluation within the Max Planck Society. (a)-(b), The map of Germany, based on the*

- **대규모 인간 평가 데이터셋 구축**: 100명 이상의 경험 많은 연구 리더가 4,451개의 개인화된 연구 아이디어를 평가하여, 전체 1,107개(약 25%)가 흥미도 4-5점을 받았다.
- **Knowledge graph 특성과 관심도의 관계 규명**: 노드/엣지 특성, 인용 지표, 의미적 거리 등 8가지 그래프 특성이 아이디어의 흥미도와 어떻게 상관관계를 가지는지 시각화 분석했다.
- **효과적인 예측 모델 개발**: supervised neural network와 zero-shot LLM 예측을 모두 구현하여, 인간 평가 데이터가 없을 때도 새로운 아이디어의 관심도를 정확하게 예측할 수 있음을 보였다.
- **학제간 협력 기회 발굴**: 같은 분야 내 협력뿐만 아니라 서로 다른 분야 간의 예상치 못한 연구 협력 기회를 체계적으로 제안할 수 있음을 입증했다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. SciMuse suggests research ideas or collaborations using a knowledge graph and GPT-4. (a), Knowledge*

- RAKE algorithm과 GPT, Wikipedia 기반 수동 검수를 통해 2.44백만 개 논문의 제목/초록으로부터 123,128개 과학 개념 추출
- OpenAlex의 58백만 개 논문에서 개념의 동시 출현과 인용 데이터를 활용하여 knowledge graph의 노드와 엣지 구축
- 각 연구자의 최근 2년간 출판물을 분석하여 개인화된 부분 그래프(subgraph) 생성
- GPT-4의 self-reflection 기법(3개 아이디어 생성 → 2회 반복 개선 → 최적 선택)을 사용한 협력 연구 아이디어 프롬프트 생성
- Knowledge graph 특성 정규화(z-score) 후 50개 동일 구간으로 분할하여 관심도와의 상관관계 분석
- 영향도 예측을 위해 reference [12]의 계산 방법을 적용하여 concept pair의 예상 인용도 추정

## Originality

- 과학 논문에서의 개념 동시 출현과 인용 데이터를 결합한 진화 knowledge graph 구축은 기존 접근보다 더 풍부한 정보를 담는다.
- 100명 이상의 경험 많은 연구 리더의 대규모 평가는 기존의 6-10명 규모 평가를 크게 확장하여 실무적 신뢰성을 확보한다.
- Knowledge graph 특성 분석을 통해 어떤 종류의 concept pair와 그래프 특성이 흥미로운 연구 아이디어와 연관되는지 체계적으로 규명하는 것은 새로운 시도이다.
- Supervised와 unsupervised (zero-shot) 예측 방법을 모두 제시함으로써 실제 상황에서의 적용 가능성을 높인다.

## Limitation & Further Study

- 평가자의 대부분(104/110)이 자연과학 분야에서만 왔으므로, 사회과학과 인문학 분야의 관점이 충분하지 않다.
- Concept 추출에 RAKE 알고리즘을 기본으로 사용하기 때문에 미묘한 개념이나 새로운 용어 포착에 제한이 있을 수 있다.
- Knowledge graph의 데이터 cutoff가 2023년 2월이므로 더 최신의 연구 트렌드를 반영하지 못한다.
- 연구 아이디어의 '흥미로움'이 평가자의 주관적 판단에 의존하므로, 실제 연구 성과 창출 여부와의 인과관계는 검증되지 않았다.", '두 연구자 간의 협력만 고려했으므로 3명 이상의 다중 협력 아이디어 생성 확장이 필요하다.
- 후속 연구에서는 생성된 아이디어 중 일부를 실제로 수행했을 때의 성과를 추적하여 예측 모델 검증이 필요하다.

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 대규모 knowledge graph와 LLM을 결합하여 개인화된 연구 아이디어를 생성하고, 100명 이상의 경험 많은 연구자 평가를 통해 검증한 매우 의미 있는 연구이다. 특히 graph 특성과 관심도의 관계 분석 및 두 가지 예측 방법 제시는 독창적이며, 과학 공동체의 실제 필요를 직접 반영한 대규모 평가 데이터는 학문적 가치가 크다.

## Related Papers

- 🔄 다른 접근: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 동일한 SciMuse 시스템을 다룬 논문으로 지식 그래프와 LLM을 활용한 개인화 연구 아이디어 생성의 핵심 내용을 공유한다.
- 🔗 후속 연구: [[papers/419_Hypothesis_Generation_with_Large_Language_Models/review]] — 데이터 기반 가설 생성 알고리즘을 대규모 지식 그래프와 결합하여 더 체계적이고 검증된 연구 아이디어 생성으로 발전시켰다.
- 🏛 기반 연구: [[papers/079_Ai_idea_bench_2025_Ai_research_idea_generation_benchmark/review]] — AI 연구 아이디어 생성 벤치마크는 SciMuse 같은 시스템의 성능을 객관적으로 평가할 수 있는 표준을 제공한다.
- 🧪 응용 사례: [[papers/186_Can_large_language_models_unlock_novel_scientific_research_i/review]] — LLM의 과학 연구 잠재력 탐구 연구에서 실제 연구자 평가를 통해 검증된 구체적인 응용 사례로 활용된다.
- 🔗 후속 연구: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — LLM 아이디어 생성 능력 평가를 전문가 평가와 결합하여 더 포괄적인 연구 아이디어 품질 평가 시스템을 구축한다.
- 🔄 다른 접근: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 동일한 SciMuse 시스템을 다룬 논문으로 지식 그래프 기반 개인화 연구 아이디어 생성의 핵심 내용과 평가 결과를 공유한다.
- 🏛 기반 연구: [[papers/419_Hypothesis_Generation_with_Large_Language_Models/review]] — 대규모 지식 그래프 기반 연구 아이디어 생성의 실제 검증 사례로서 가설 생성 알고리즘의 효용성을 입증한다.
