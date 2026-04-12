---
title: "1033_The_Empowerment_of_Science_of_Science_by_Large_Language_Mode"
authors:
  - "Guoqiang Liang"
  - "Jingqian Gong"
  - "Mengxuan Li"
  - "Gege Lin"
  - "Shuo Zhang"
date: "2025.11"
doi: "10.48550/arXiv.2511.15370"
arxiv: ""
score: 3.0
essence: "대규모언어모델(LLM)의 핵심 기술(프롬프트 엔지니어링, RAG, 파인튜닝 등)을 정리하고 과학계량학(SciSci) 분야에의 적용 가능성을 제시하는 종합 리뷰 논문이다."
tags:
  - "cat/AI-Assisted_Scientific_Discovery"
  - "sub/Science_of_Science_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liang et al._2025_The Empowerment of Science of Science by Large Language Models New Tools and Methods.pdf"
---

# The Empowerment of Science of Science by Large Language Models: New Tools and Methods

> **저자**: Guoqiang Liang, Jingqian Gong, Mengxuan Li, Gege Lin, Shuo Zhang | **날짜**: 2025-11-19 | **DOI**: [10.48550/arXiv.2511.15370](https://doi.org/10.48550/arXiv.2511.15370)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. Parameters and classification of notable LLMs*

대규모언어모델(LLM)의 핵심 기술(프롬프트 엔지니어링, RAG, 파인튜닝 등)을 정리하고 과학계량학(SciSci) 분야에의 적용 가능성을 제시하는 종합 리뷰 논문이다.

## Motivation

- **Known**: LLM은 자연어 처리, 이미지 인식, 멀티모달 작업에서 우수한 성능을 보이고 있으며, GPT 시리즈의 발전을 통해 Transformer 아키텍처 기반의 모델이 주류를 이루고 있다. 과학계량학은 인용 분석, 토픽 모델링, 그래프 신경망 등 전통적 방법에서 AI 기반 방법으로 진화하고 있다.
- **Gap**: LLM의 핵심 기술 체계(프롬프트, RAG, 파인튜닝, 사전훈련, 도구 학습)가 과학계량학 분야에 어떻게 구체적으로 통합될 수 있는지에 대한 통합적 로드맵이 부재하다. AI 에이전트 기반 과학평가 모델의 실제 구현 방법과 신흥 연구 분야 탐지 및 지식 그래프 구축의 LLM 기반 방법론이 명확하지 않다.
- **Why**: LLM은 현재 AI 분야의 인프라로 작용하며 전 산업에 영향을 미치고 있으므로, 학문 평가와 과학 정책 수립이 이루어지는 과학계량학에 LLM을 효과적으로 도입하는 것은 미래 과학 생태계 구축에 필수적이다.
- **Approach**: LLM의 기술 아키텍처와 개념을 사용자 관점에서 체계적으로 분류하고 설명한 후, 과학계량학의 역사적 발전 과정을 추적하여 LLM의 잠재적 적용 영역을 도출한다. 이를 통해 AI 에이전트 기반 과학평가 모델, 신흥 연구 탐지, 지식 그래프 구축 방법을 제안한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. Parameters and classification of notable LLMs*

- **LLM 기술 체계 정리**: Transformer와 MoE 아키텍처 분류, 일반 목적 모델과 수직 모델의 구분, 프롬프트 엔지니어링, RAG, 파인튜닝, 사전훈련, 도구 학습 등 5대 핵심 기술 설명
- **과학계량학 진화 추적**: 인용 분석에서 BERT, GCN, 지식 그래프 등 AI 기반 방법으로의 패러다임 전환 기록
- **LLM의 SciSci 응용 전망 제시**: AI 에이전트 기반 과학평가 모델 구상, 신흥 연구 분야 탐지 및 지식 그래프 구축 방법론 제안
- **용어 체계화**: 토크나이제이션, 임베딩, AI 에이전트 등 개념 간 관계를 도식화하여 LLM 이해도 향상

## How

![Figure 2](figures/fig2.webp)

*Figure 2. The common terminology and relation of LLMs*

- LLM 분류 기준의 다층적 분석: 입력 데이터 유형(언어/시각/멀티모달), 아키텍처(Transformer/MoE), 적용 영역(일반/수직)
- GPT 시리즈(GPT-1부터 ChatGPT-4)의 진화 과정을 파라미터, 레이어, 학습 데이터 규모 지표로 정량화
- 과학계량학의 방법론 변화를 시간대별로 정렬: 전통적 방법(인용 분석, 단어 빈도)→기계학습(동적 토픽 모델, Word2Vec)→딥러닝(BERT, GCN, 지식 그래프)
- LLM 기술의 SciSci 영역별 맵핑을 통한 구체적 활용 시나리오 제시

## Originality

- 과학계량학 분야에 대한 LLM의 체계적 적용 가능성을 최초로 종합적으로 검토한 리뷰
- 사용자 관점의 LLM 기술 설명으로 학제간 접근성 강화 (기술 깊이보다 활용성 중심)
- 전통적 과학계량학 방법론에서 AI 기반 방법론으로의 패러다임 전환을 역사적 맥락에서 명확화
- AI 에이전트 기반 과학평가 모델이라는 새로운 개념 도입으로 과학 거버넌스 혁신 가능성 시사

## Limitation & Further Study

- 제시된 LLM 적용 사례들(신흥 연구 탐지, 지식 그래프 구축)이 구체적인 구현 세부사항, 성능 평가 지표, 검증 결과 없이 고수준의 개념 수준에 머물러 있음
- AI 에이전트 기반 과학평가 모델의 윤리적 우려(학자 평가의 자동화로 인한 편향, 투명성 부족)에 대한 논의 부재
- LLM의 환각(hallucination) 문제, 학습 데이터 편향(미국 61개 vs 중국 15개 모델의 격차)이 과학계량학 적용 시 야기할 수 있는 문제에 대한 분석 불충분
- 후속 연구: 실제 SciSci 데이터셋을 사용한 LLM 기반 방법론의 벤치마크 성능 평가 필요. AI 에이전트의 과학평가 활용에 대한 규제 프레임워크 개발. 다국어 과학 문헌 처리를 위한 비영어권 LLM의 역할 확대 연구

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 3/5

**총평**: 본 논문은 LLM의 핵심 기술을 명확하게 정리하고 과학계량학의 미래 방향을 제시하는 가치 있는 리뷰이나, 제안된 적용 방법론들이 개념 수준에서 구체적 구현 사례와 검증 결과로 뒷받침되지 못하여 실제 임팩트 평가가 어렵다.

## Related Papers

- 🔗 후속 연구: [[papers/1041_The_Rise_of_Large_Language_Models_and_the_Direction_and_Impa/review]] — 대규모언어모델이 과학 연구 방향과 영향에 미치는 변화를 과학계량학 관점에서 체계적으로 분석할 수 있다.
- 🧪 응용 사례: [[papers/1078_Quantifying_the_use_and_potential_benefits_of_artificial_int/review]] — 인공지능 사용량 정량화 연구에 LLM 기반 과학계량학 분석 도구를 적용하여 더 정확한 측정이 가능하다.
- 🏛 기반 연구: [[papers/1124_The_Science_of_Science/review]] — 과학의 과학 연구 분야에 LLM 기술을 통합하는 이론적이고 방법론적 토대를 공유한다.
- 🧪 응용 사례: [[papers/1124_The_Science_of_Science/review]] — LLM이 과학의 과학 연구를 어떻게 강화할 수 있는지 구체적 활용 방안을 제시한다.
- 🔗 후속 연구: [[papers/1072_Embracing_Foundation_Models_for_Advancing_Scientific_Discove/review]] — LLM이 과학의 과학 분야에 미치는 전반적 영향력을 기초 모델 활용으로 구체화함
- 🏛 기반 연구: [[papers/1074_OLMo_Accelerating_the_Science_of_Language_Models/review]] — LLM의 과학 연구 영향력 분석에 필요한 오픈 모델 인프라를 제공함
- 🔗 후속 연구: [[papers/963_Forecasting_the_future_of_artificial_intelligence_with_machi/review]] — AI 연구 방향 예측을 위한 Science4Cast 벤치마크와 대규모 언어 모델이 과학의 과학을 강화하는 방법이 상호 보완적 발전을 이룹니다.
- 🏛 기반 연구: [[papers/1192_Large_language_models_and_responsible_research_evaluation_an/review]] — LLM을 과학계량학에 활용할 때 필요한 책임 있는 평가 원칙의 이론적 기반을 공유한다.
