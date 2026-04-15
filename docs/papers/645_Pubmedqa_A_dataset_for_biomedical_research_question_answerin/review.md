---
title: "645_Pubmedqa_A_dataset_for_biomedical_research_question_answerin"
authors:
  - "Qiao Jin"
  - "Bhuwan Dhingra"
  - "Zhengping Liu"
  - "William Cohen"
  - "Xinghua Lu"
date: "2019"
doi: "미제공"
arxiv: ""
score: 4.25
essence: "생의학 분야의 연구 논문 초록을 이용하여 yes/no/maybe로 답변하는 질문응답 데이터셋을 제안한다. 1,000개의 전문가 주석 데이터, 61,200개의 미표지 데이터, 211,300개의 자동생성 데이터로 구성되며, 정량적 추론이 필요한 최초의 생의학 QA 데이터셋이다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "sub/Scholarly_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2019_Pubmedqa A dataset for biomedical research question answering.pdf"
---

# PubMedQA: A Dataset for Biomedical Research Question Answering

> **저자**: Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William Cohen, Xinghua Lu | **날짜**: 2019 | **DOI**: [미제공](https://arxiv.org/abs/1909.06146)

---

## Essence

![Figure 1](https://imgur.com/placeholder) *PubMedQA 데이터셋 인스턴스 예시: 질문은 원문의 제목이며, 맥락은 결론을 제외한 구조화된 초록이고, 장답변은 결론, 최종 답변은 yes/no/maybe*

생의학 분야의 연구 논문 초록을 이용하여 yes/no/maybe로 답변하는 질문응답 데이터셋을 제안한다. 1,000개의 전문가 주석 데이터, 61,200개의 미표지 데이터, 211,300개의 자동생성 데이터로 구성되며, 정량적 추론이 필요한 최초의 생의학 QA 데이터셋이다.

## Motivation

- **Known**: 일반 도메인의 대규모 QA 데이터셋(SQuAD, HotpotQA 등)은 풍부하지만, 생의학 분야의 QA 데이터셋은 극히 제한적이다. 기존 BioASQ는 3,000개 미만의 훈련 인스턴스만 보유하고 있으며, 자동생성 생의학 QA 데이터셋들은 단순 인수 추출 문제 중심이다.

- **Gap**: 생의학 텍스트의 정량적 내용과 논리적 추론을 요구하는 대규모 고품질 QA 데이터셋이 부재하다.

- **Why**: 생의학 연구 질문에 답변하기 위해서는 초록의 결과, 방법론, 통계 데이터 등을 종합적으로 이해하고 추론하는 능력이 필수적이다.

- **Approach**: PubMed의 약 760,000개 질문 제목을 가진 논문 중에서 구조화된 초록(Introduction, Methods, Results, Conclusions 등)을 가진 약 120,000개 논문을 활용하여, 결론을 제외한 초록을 맥락으로, 결론을 장답변으로, 그리고 yes/no/maybe 답변으로 구성한 데이터셋을 구축한다.

## Achievement

![Figure 2](https://imgur.com/placeholder) *PubMedQA 데이터셋 구조: PQA-Labeled(1k), PQA-Unlabeled(61.2k), PQA-Artificial(211.3k)의 세 가지 부분집합으로 구성*

1. **데이터셋 규모 및 다양성**: 전문가 주석 1,000개, 반준지도학습용 미표지 61,200개, 사전훈련용 자동생성 211,300개의 총 273,500개 인스턴스 구축. PubMed의 MeSH(Medical Subject Headings) 분류에 따라 인간 연구, 치료 결과, 위험 요소 등 다양한 의학 주제 포괄.

2. **추론 요구 특성**: PQA-Labeled에서 두 명의 주석자를 활용한 이중 주석 프로세스(Algorithm 1)로, 장답변 없이 순수 맥락만으로 추론이 필요한 데이터 검증. 사람의 단일 성능은 78.0%, 다수결 베이스라인은 55.2%로, 상당한 개선 여지를 시사.

3. **모델 성능**: BioBERT의 다단계 미세조정(multi-phase fine-tuning)과 장답변의 bag-of-word 통계를 추가 지도신호로 활용하여 68.1% 정확도 달성. 이는 인간 성능(78.0%)과의 9.9% 격차를 보이며 시스템의 한계를 명시적으로 드러냄.

## How

![Figure 3](https://imgur.com/placeholder) *PubMedQA 데이터셋의 MeSH 주제 분포: 인간 연구, 여성, 남성, 중년 등의 용어가 높은 빈도로 나타남*

**데이터 수집 방법론**:
- **PQA-Labeled(1k) & PQA-Unlabeled(61.2k) 수집**: PubMed에서 질문 제목(물음표 포함)과 구조화된 초록을 가진 논문 검색. 두 명의 MD 후보자가 주석: 주석자1은 맥락+장답변 활용(추론 불필요), 주석자2는 맥락만 활용(추론 필수). 불일치 시 합의 과정 거쳐 최종 라벨 결정. PQA-U는 규칙 기반 필터링(의문사 제거, 다항선택 제외)으로 yes/no/maybe 가능 질문 자동 식별(주석자1과 93% 이상 일치).

- **PQA-Artificial(211.3k) 생성**: 서술형 제목(NP-(VBP/VBZ) POS 패턴)을 질문으로 변환하고, 동사의 부정 상태에 따라 yes/no 라벨 자동 할당. 예: "...predict X"→"yes", "...do not have X"→"no".

**모델 아키텍처**:
- BioBERT 기반 다단계 미세조정: (1) PQA-A로 사전훈련, (2) PQA-U에서 반준지도학습, (3) PQA-L에서 최종 미세조정
- 장답변의 bag-of-word 통계(단어 빈도, TF-IDF)를 추가 지도신호로 활용하여 모델이 중요 단어에 주목하도록 유도

## Originality

- **최초의 추론 요구 생의학 QA 데이터셋**: 기존 생의학 QA들은 단순 인수 추출 또는 사실 검색이었으나, PubMedQA는 통계적 결과 해석, 결론 도출 등 고차 추론 능력을 명시적으로 요구.

- **자연적 데이터 일관성**: 일반 QA 데이터셋과 달리 질문과 맥락이 동일 저자에 의해 작성되어 질문-맥락 간 완벽한 관련성 보장. 크라우드 주석의 자의성 문제 회피.

- **삼중 구조의 다층 활용**: 전문가 주석, 반준지도학습용 미표지, 자동생성 데이터를 계층적으로 제공함으로써 지도학습, 반준지도학습, 사전훈련 모두 가능하게 설계.

- **yes/no/maybe의 삼진 분류**: 일반 yes/no 문제를 확장하여 '불확실함(maybe)'을 명시적으로 포함(PQA-L의 11%), 현실의 의학적 불확실성 반영.

## Limitation & Further Study

**한계**:
- **자동생성 데이터 품질**: PQA-A의 자동 라벨링은 단순 부정 휴리스틱만 사용하여 복잡한 논리적 부정이나 맥락 의존적 답변을 놓칠 수 있음. 이는 211.3k 인스턴스 중 92.8% yes, 7.2% no의 심각한 클래스 불균형으로 나타남.

- **제한된 전문가 주석 규모**: 1,000개는 현대 대규모 모델 훈련에는 상대적으로 적으며, 두 명의 주석자만으로는 주석 다양성 부족. 주석자1과 주석자2 간 합의 불가능한 경우의 인스턴스 제거로 실제 데이터 손실.

- **인간-모델 성능 격차**: 78.0% vs 68.1%의 9.9% 차이는 현재 모델이 생의학 추론 능력에서 여전히 상당히 부족함을 시사하나, 개선 방향에 대한 명확한 분석 부족.

**후속 연구 방향**:
- BioBERT 외 다른 사전훈련 언어모델(SciBERT, PubMedBERT 등) 평가 필요.
- 주의 메커니즘(Attention) 분석을 통해 모델이 어떤 근거에 의존하는지 해석 가능성 향상.
- 다단계 추론 또는 외부 지식 그래프 통합으로 더욱 복잡한 생의학 추론 능력 개발.
- 자동생성 데이터의 품질 개선을 위한 더 정교한 휴리스틱 개발 또는 약한 지도(weak supervision) 기법 적용.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4.5/5
- Overall: 4.25/5

**총평**: PubMedQA는 생의학 텍스트 기반 추론이 필수적인 첫 대규모 QA 데이터셋으로, PubMed의 자연적 구조를 창의적으로 활용한 점과 삼층 구조의 체계적 설계가 돋보인다. 다만 자동생성 부분집합의 품질 한계와 인간-모델 성능 격차 분석의 부족이 보완되어야 할 점이다.

## Related Papers

- 🔄 다른 접근: [[papers/715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific/review]] — SciDQA는 과학 논문의 깊이 있는 독해 이해를 평가하는 데이터셋으로, PubMedQA의 생의학 특화 접근과 대비되는 범용 과학 QA 평가를 제공한다
- 🏛 기반 연구: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 자연어 yes/no 질문의 어려움을 체계적으로 분석한 연구로, PubMedQA의 yes/no/maybe 답변 체계 설계의 이론적 근거를 제공한다
- 🔗 후속 연구: [[papers/701_Scholarchemqa_Unveiling_the_power_of_language_models_in_chem/review]] — 화학 분야에 특화된 질의응답 데이터셋으로, PubMedQA의 생의학 분야 접근을 화학 도메인으로 확장한 연구 방향을 보여준다
- 🔗 후속 연구: [[papers/730_Sciqag_A_framework_for_auto-generated_science_question_answe/review]] — 생의학 질의응답 데이터셋으로 과학 QA 자동 생성을 의학 분야로 확장한다.
- 🔄 다른 접근: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 생의학 분야의 질문 답변 데이터셋으로, 일반 도메인 예/아니오 질문과 전문 의료 분야 질문의 차이를 비교할 수 있습니다.
- 🔄 다른 접근: [[papers/715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific/review]] — PubMedQA는 생의학 분야에 특화된 질의응답 데이터셋으로, SciDQA의 범용 과학 논문 이해와 다른 도메인별 접근법을 보여준다
- 🏛 기반 연구: [[papers/424_Improving_health_question_answering_with_reliable_and_time-a/review]] — 생의학 연구 질의응답 데이터셋이 건강 관련 질문 답변 시스템의 기초 훈련 및 평가 자료를 제공한다.
- 🔄 다른 접근: [[papers/711_Sciclaims_An_end-to-end_generative_system_for_biomedical_cla/review]] — 생의학 연구에서 질문 답변과 주장 검증이라는 서로 다른 지식 처리 접근법을 비교할 수 있다.
