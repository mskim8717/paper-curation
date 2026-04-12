---
title: "1051_Unsupervised_Word_Embeddings_Capture_Latent_Knowledge_from_M"
authors:
  - "Vahe Tshitoyan"
  - "John Dagdelen"
  - "Leigh Weston"
  - "Alexander Dunn"
  - "Ziqin Rong"
date: "2019"
doi: "10.1038/s41586-019-1335-8"
arxiv: ""
score: 4.0
essence: "비지도 학습 방식의 Word2vec를 재료과학 문헌 330만 개 초록에 적용하여 화학적 지식을 명시적으로 부여하지 않고도 주기율표 구조와 물성-구조 관계 등 잠재 지식을 포착할 수 있음을 보여줌."
tags:
  - "cat/AI-Assisted_Scientific_Discovery"
  - "sub/Knowledge_Graphs_and_Data_Integration"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tshitoyan et al._2019_Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature.pdf"
---

# Unsupervised Word Embeddings Capture Latent Knowledge from Materials Science Literature

> **저자**: Vahe Tshitoyan, John Dagdelen, Leigh Weston, Alexander Dunn, Ziqin Rong, Olga Kononova, Kristin A. Persson, Gerbrand Ceder, Anubhav Jain | **날짜**: 2019 | **DOI**: [10.1038/s41586-019-1335-8](https://doi.org/10.1038/s41586-019-1335-8)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Word2vec skip-gram and analogies. a, Target words ‘LiCoO2’*

비지도 학습 방식의 Word2vec를 재료과학 문헌 330만 개 초록에 적용하여 화학적 지식을 명시적으로 부여하지 않고도 주기율표 구조와 물성-구조 관계 등 잠재 지식을 포착할 수 있음을 보여줌.

## Motivation

- **Known**: Word2vec 및 GloVe 같은 단어 임베딩 기술은 텍스트 코퍼스에서 단어의 공동 출현(co-occurrence)을 학습하여 의미론적·통사론적 관계를 벡터로 인코딩할 수 있다는 것이 알려져 있다.
- **Gap**: 과학 문헌에 포함된 방대한 지식은 구조화된 데이터베이스에 비해 기계 해석이 어려우며, 기존 지도 학습 기반 자연어처리(NLP) 방법은 대규모 수작업 라벨링 데이터셋을 요구하는 문제가 있다.
- **Why**: 재료과학 문헌에 내재된 미발견 물질의 잠재 지식을 자동으로 추출할 수 있다면 새로운 기능성 재료의 발견을 가속화할 수 있으며, 감독되지 않은 방식으로 대규모 과학 문헌을 체계적으로 활용할 수 있는 일반화된 접근법을 제시할 수 있다.
- **Approach**: 1922~2018년 재료 과학 저널 1,000여 개에서 330만 개의 초록을 수집하여 50만 단어 어휘를 구성하고, Word2vec의 skip-gram 모델을 200차원 임베딩으로 학습하여 재료과학 개념과 물질-응용 관계를 포착함.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3 | Validation of the predictions. a, Results of prediction of*

- **주기율표 구조 자동 포착**: 화학적 지식을 명시적으로 삽입하지 않았음에도 임베딩의 2차원 투영에서 원소들이 주기율표와 일관된 배치를 보임
- **물질 유사성 및 유추 인식**: LiCoO2와 가장 유사한 5개 물질이 모두 리튬이온 캐소드 소재이며, NiFe:ferromagnetic = IrMn:antiferromagnetic 같은 도메인 특정 유추를 자동으로 해결
- **열전 소재 미래 예측**: 2001~2018년 각 연도별 historical 코퍼스로 학습하여 이후 5년간 열전 소재 발견을 예측했을 때, 상위 50개 예측 물질이 무작위 선택 물질 대비 8배, DFT 밴드갭 예측 대비 3배 더 높은 성공률을 달성
- **구체적 사례**: CuGaTe2는 실제 발표 4년 전에 상위 5개 예측에 포함되었고, ReS2와 CdIn2Te4는 각각 8~9년 전에 예측됨

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Word2vec skip-gram and analogies. a, Target words ‘LiCoO2’*

- 1922~2018년 간 1,000여 재료 관련 저널에서 330만 개 과학 초록 수집 및 전처리
- Word2vec skip-gram 모델 적용으로 200차원 단어 임베딩 학습 (컨텍스트 단어 예측 기반)
- 임베딩의 코사인 유사도(cosine similarity)로 물질 간 유사성 및 응용 키워드와의 관계 정량화
- 주성분분석(PCA)을 통한 고차원 임베딩의 2차원 투영으로 시각화
- 벡터 덧셈·뺄셈·투영 연산을 통한 도메인 특정 유추(analogy) 검증
- 역사적 코퍼스(historical corpus) 구성으로 매년 재학습하여 미래 재료 발견 예측 성능 검증
- DFT 계산 데이터 및 실험 데이터와의 순위 상관계수(rank correlation) 비교

## Originality

- **감독되지 않은 대규모 문헌 마이닝**: 수작업 라벨링 없이 330만 초록에서 자동으로 재료과학 지식 추출하는 첫 시도
- **미래 예측 검증 프레임워크**: historical corpus를 이용한 시간 경화된 예측 평가로 인과성 추론 강화
- **도메인 특정 벡터 연산**: 화학 조성·결정 구조·기능성 응용 등 이질적 개념 간의 일관된 벡터 연산 가능성 입증
- **임베딩 기반 특성 벡터의 우월성**: 원소 임베딩이 형성 에너지 예측에서 기존 큐레이션된 특성 벡터를 능가

## Limitation & Further Study

- 임베딩 유사도가 높은 물질도 명시적으로 해당 응용 키워드와 함께 발표되지 않은 경우가 있어, 예측의 위양성(false positive) 위험 존재
- Word2vec은 단순한 단어 수준의 공동 출현만 학습하므로, 복잡한 다중-단어 관계나 문맥의 미묘한 뉘앙스를 놓칠 수 있음
- 1922~2018년 출판 편향(publication bias)과 저널 선택 편향이 임베딩에 반영될 가능성
- **후속 연구 방향**: (1) transformer 기반 모델(BERT, SciBERT)로 문장 수준 문맥 포착 강화, (2) 설명 가능성(interpretability) 개선을 위한 어텐션 메커니즘 분석, (3) 멀티모달 학습으로 구조 정보·실험 데이터 통합, (4) 동적 임베딩으로 시간에 따른 개념 진화 추적

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 연구는 감독되지 않은 단어 임베딩으로 대규모 과학 문헌에서 숨겨진 재료과학 지식을 효과적으로 추출하며, 특히 미래 발견을 시간 경화된 방식으로 성공적으로 예측함으로써 과학 문헌 마이닝의 실제 가치를 입증하는 획기적인 사례를 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 컴퓨터과학 논문에서 구축한 지식그래프와 재료과학 문헌의 Word2vec 임베딩은 서로 다른 도메인에서 잠재 지식 추출을 위한 상호 보완적 접근법이다.
- 🔗 후속 연구: [[papers/978_Introducing_the_open_biomedical_map_of_science/review]] — 생의학 과학 지도 구축 방법론을 재료과학 도메인에 적용하여 더 포괄적인 과학 지식 구조 분석이 가능하다.
- 🔄 다른 접근: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 재료과학의 Word2vec 임베딩과 컴퓨터과학의 지식그래프는 서로 다른 학문 분야에서 잠재 지식 추출을 위한 상호 보완적 접근법이다.
- 🏛 기반 연구: [[papers/982_Mapping_Knowledge_Topic_Analysis_of_Science_Locates_Research/review]] — 비지도 단어 임베딩의 잠재 지식 포착 방법론을 바탕으로 연구자의 인식론적 위치를 의미론적으로 규명한다.
- 🏛 기반 연구: [[papers/1175_Figures_as_Interfaces_Toward_LLM-Native_Artifacts_for_Scient/review]] — 의료 언어에서 잠재 지식을 포착하는 임베딩 기술이 과학 도형의 기계 판독 가능한 표현 생성에 이론적 기반을 제공한다.
