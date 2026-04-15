---
title: "132_Automating_psychological_hypothesis_generation_with_AI_when"
authors:
  - "Song Tong"
  - "Kai Mao"
  - "Zhen Huang"
  - "Yukun Zhao"
  - "Kaiping Peng"
date: "2024"
doi: "10.1057/s41599-024-03407-5"
arxiv: ""
score: 4.2
essence: "본 연구는 대규모 언어 모델(LLM)과 인과 지식 그래프(Causal Knowledge Graph)를 결합하여 심리학 분야의 자동화된 가설 생성을 수행했다. 43,312개 심리학 논문을 분석한 결과, LLM 단독보다 우월한 신규성을 가진 130개의 웰빙 관련 가설을 생성할 수 있음을 입증했다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tong et al._2024_Automating psychological hypothesis generation with AI when large language models meet causal graph.pdf"
---

# Automating psychological hypothesis generation with AI: when large language models meet causal graph

> **저자**: Song Tong, Kai Mao, Zhen Huang, Yukun Zhao, Kaiping Peng | **날짜**: 2024 | **DOI**: [10.1057/s41599-024-03407-5](https://doi.org/10.1057/s41599-024-03407-5)

---

## Essence

![Figure 1](figures/fig1.webp)
*LLMCG 알고리즘을 기반한 가설 생성 프레임워크: 문헌 검색, 인과 관계 쌍 추출, 가설 생성의 세 단계*

본 연구는 대규모 언어 모델(LLM)과 인과 지식 그래프(Causal Knowledge Graph)를 결합하여 심리학 분야의 자동화된 가설 생성을 수행했다. 43,312개 심리학 논문을 분석한 결과, LLM 단독보다 우월한 신규성을 가진 130개의 웰빙 관련 가설을 생성할 수 있음을 입증했다.

## Motivation

- **Known**: 심리학 연구는 전통적으로 이론 중심의 방법론에 의존해왔으며, 가설 생성은 연구자의 창의성과 기존 이론 틀 내에서 수행된다. 최근 GPT-4 등의 LLM이 인과 관계 추론 능력을 보여주고 있다.

- **Gap**: LLM 단독으로는 방대한 문헌에서 추출한 인과 관계의 체계적 통합이 어렵고, 인과 그래프 구축의 노동 집약성은 다학제적 알고리즘 개발 전문성을 요구한다. LLM의 해석 가능성 문제도 해결되지 않고 있다.

- **Why**: 심리학의 발전을 위해 AI 기반 데이터 중심 연구 패러다임으로의 전환이 필요하며, 이를 통해 방대한 심리학 문헌에서 숨겨진 인과 관계를 자동 발굴할 수 있다.

- **Approach**: LLM의 의미론적 추출 능력과 인과 그래프의 체계적 사고를 결합한 LLMCG(LLM-based Causal Graph) 프레임워크를 제안하고, 링크 예측(link prediction) 알고리즘으로 새로운 가설을 자동 생성한다.

## Achievement

![Figure 2](figures/fig2.webp)
*집단 간 비교 분석: (a) 신규성(novelty)과 (b) 유용성(usefulness) 분포를 보여주는 박스 플롯*

1. **가설 생성의 효과성**: LLMCG 프레임워크로 생성한 130개의 웰빙 관련 가설이 박사 과정생(novice experts)의 아이디어와 유사한 수준의 신규성을 보였다 (t(59) = 3.34, p = 0.007). LLM 단독 방식을 명확히 능가했다 (t(59) = 4.32, p < 0.001).

2. **의미론적 우월성**: 심층 의미 분석(deep semantic analysis) 결과, LLMCG 알고리즘이 더 깊이 있는 개념 통합과 광범위한 의미 스펙트럼을 보유함을 입증했다. BERT 공간에서의 의미적 거리 분석으로 이를 정량적으로 확인했다.

## How

![Figure 3](figures/fig3.webp)
*BERT 공간에서의 의미 표현 t-SNE 시각화: (a) 신규성 점수와 (b) 유용성 점수 비교*

**3단계 LLMCG 프레임워크**:

- **Step 1 - 문헌 검색**: PMC Open Access Subset에서 심리학 관련 키워드("psychol", "clin psychol" 등)를 포함한 약 140,000개 논문 검색. 저널명에 "Psychol"을 포함한 43,312개 논문 최종 선정 (1975-2023년)

- **Step 2 - 인과 쌍 추출**:
  - (2-1) 논문 선별 및 비용 분석: 처리 가능성 검토
  - (2-2) 텍스트 추출 및 정제: PyPDF2 라이브러리로 제목, 초록, 본문 추출. 정규표현식으로 참고문헌 섹션 제거
  - (2-3) 인과 지식 추출: GPT-4를 사용하여 텍스트에서 인과 관계 탐지, 분류, 표준화
  - (2-4) 그래프 데이터베이스 저장: 구조화된 저장 및 관계 분석 지원

- **Step 3 - 가설 생성**: 노드 임베딩(node embedding)과 유사도 기반 링크 예측 알고리즘으로 숨겨진 인과 관계 발굴 및 가설 자동 생성

- **검증 방법**: 웰빙 관련 130개 가설을 ①박사 과정생 아이디어, ②LLM 단독 생성 가설과 신규성/유용성 면에서 비교 평가

## Originality

- 심리학 분야 최초의 대규모 인과 지식 그래프 구축(43,312개 논문 기반): 기존 물리학 분야의 의미 네트워크 연구(Krenn & Zeilinger, 2020)를 심리학에 확장 적용

- LLM과 인과 그래프의 보완적 강점 결합: LLM의 세밀한 의미 분석과 그래프의 전역적 인과성 관점을 통해 상호 해석 가능성 문제 해결

- 인간 전문가 수준 성과 달성: 신규 AI 시스템이 novice experts의 아이디어와 동등한 수준을 달성한 최초의 심리학 분야 사례

- 이론 중심 방법론과 데이터 중심 연구의 가교 역할: 전통적 심리학 연구 패러다임과 현대 AI 기반 자동 발굴의 통합

## Limitation & Further Study

- **작업 기억(working memory) 제약 미흡**: HyGene 모델에서 강조한 인간의 작업 기억 제약을 완전히 모사하지 못하며, 이는 인간 가설 생성의 인지 메커니즘 이해에 한계

- **GPT-4 의존성**: 특정 LLM 모델에 의존하여 다른 모델의 성능 비교나 모델 독립적 결과 일반화 미흡

- **웰빙 영역 제한**: 검증이 웰빙 주제에만 한정되어 심리학 전 영역에 대한 프레임워크의 효과성 미입증

- **인과 관계 추출 정확도**: GPT-4의 인과 관계 추출 과정에서 거짓 양성(false positive), 인과 방향 오인(reverse causality) 등의 오류 가능성에 대한 상세 검토 부족

- **후속 연구 방향**:
  - 다양한 심리학 주제 영역(임상, 발달, 조직심리학 등)에 대한 확대 적용
  - 생성된 가설의 실증적 검증 연구 수행
  - 인간 심리학자와 AI의 협업 프레임워크 개발
  - 다국어 문헌으로 확장하여 국제적 인과 지식 그래프 구축

## Evaluation

- **Novelty**: 4.5/5
  - 심리학에 인과 지식 그래프와 LLM 결합은 매우 혁신적이나, 개별 기술의 신규성은 각각 기존 연구에서 입증됨

- **Technical Soundness**: 4/5
  - 3단계 프레임워크의 논리적 설계는 견고하나, 인과 관계 추출의 정확도 검증(precision, recall 등)이 상세히 기술되지 않음. 비용 분석(Appendix A 참조)과 비교 평가 방법은 적절함

- **Significance**: 4.5/5
  - 심리학 분야의 자동 가설 생성 이론의 변환점이 될 잠재력이 높으며, 43,312개 논문 기반의 대규모 인과 그래프는 학문적 자산. 다만 현장 적용 사례나 생성 가설의 실제 실험적 검증이 부재

- **Clarity**: 4/5
  - 전반적으로 명확하고 논리적 구성이 우수하나, 링크 예측 알고리즘의 구체적 수식과 하이퍼파라미터 설정이 본문에서 상세하지 않음. 용어 설명(HyGene 모델 등)이 충분

- **Overall**: 4.2/5

**총평**: 본 논문은 심리학 분야의 자동 가설 생성에 대한 선도적 시도로, LLM과 인과 그래프의 상승효과를 실증적으로 입증했다. 대규모 문헌 분석과 신뢰성 있는 비교 평가는 강점이지만, 인과 추출의 정확도 검증과 생성 가설의 실제 실험적 검증이 향후 연구에서 보완되어야 한다.

## Related Papers

- 🧪 응용 사례: [[papers/492_Literature_meets_data_A_synergistic_approach_to_hypothesis_g/review]] — 문헌과 데이터를 통합한 가설 생성 방법론을 심리학 분야에 구체적으로 적용한 실증 사례로, 일반적 접근법의 실제 활용 예시다
- 🔄 다른 접근: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 지식 그래프 기반의 과학적 아이디어 생성 접근법으로, 이 논문의 인과 지식 그래프 결합 방법과 유사하지만 더 범용적인 접근을 보여준다
- 🔗 후속 연구: [[papers/518_Many_Heads_Are_Better_Than_One_Improved_Scientific_Idea_Gene/review]] — 다수의 관점을 통합한 과학 아이디어 생성 연구로, 이 논문의 LLM과 지식 그래프 결합 접근을 다중 에이전트 협업으로 확장한다
- 🔄 다른 접근: [[papers/188_Can_we_automatize_scientific_discovery_in_the_cognitive_scie/review]] — AI를 통한 심리학 가설 생성 자동화가 인지과학 발견 자동화와는 다른 접근으로 행동과학 연구를 자동화한다
- 🧪 응용 사례: [[papers/123_Automated_Hypothesis_Validation_with_Agentic_Sequential_Fals/review]] — AI를 통한 심리학 가설 생성 자동화 연구로, 순차적 반박을 통한 가설 검증의 심리학 분야 적용
- 🧪 응용 사례: [[papers/149_Bayes-Entropy_Collaborative_Driven_Agents_for_Research_Hypot/review]] — 심리학적 가설 생성 자동화에 베이지안-엔트로피 협력 방법론을 적용하여 인문사회과학 연구에서도 활용할 수 있다
- 🧪 응용 사례: [[papers/492_Literature_meets_data_A_synergistic_approach_to_hypothesis_g/review]] — 심리학 분야에서 LLM과 인과 지식 그래프를 결합한 가설 생성 사례로, 이 논문의 문헌-데이터 통합 방법론의 구체적 적용 예시다
