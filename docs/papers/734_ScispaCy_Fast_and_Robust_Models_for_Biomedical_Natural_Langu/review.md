---
title: "734_ScispaCy_Fast_and_Robust_Models_for_Biomedical_Natural_Langu"
authors:
  - "Mark Neumann"
  - "Daniel King"
  - "Iz Beltagy"
  - "Waleed Ammar"
date: "2019.08"
doi: "10.18653/v1/W19-5034"
arxiv: ""
score: 4.0
essence: "biomedical 및 scientific 텍스트 처리를 위해 spaCy를 기반으로 한 scispaCy 라이브러리를 개발하여 POS tagging, dependency parsing, NER 등의 작업에서 robust하고 빠른 성능을 제공한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Neumann et al._2019_ScispaCy Fast and Robust Models for Biomedical Natural Language Processing.pdf"
---

# ScispaCy: Fast and Robust Models for Biomedical Natural Language Processing

> **저자**: Mark Neumann, Daniel King, Iz Beltagy, Waleed Ammar | **날짜**: 2019-08 | **DOI**: [10.18653/v1/W19-5034](https://doi.org/10.18653/v1/W19-5034)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Unlabeled attachment score (UAS) perfor-*

biomedical 및 scientific 텍스트 처리를 위해 spaCy를 기반으로 한 scispaCy 라이브러리를 개발하여 POS tagging, dependency parsing, NER 등의 작업에서 robust하고 빠른 성능을 제공한다.

## Motivation

- **Known**: NLP의 최근 진전에도 불구하고 대부분의 통계 모델은 domain shift에서 성능이 급격히 저하된다. biomedical 및 clinical 텍스트 처리는 중요하지만 robust하고 실용적인 public 모델이 부족하다.
- **Gap**: 기존 biomedical NLP 도구들(MetaMap, GENIA tagger)은 entity recognition에만 집중하거나 최신 neural network 기반 혁신을 활용하지 않는다. comprehensive한 biomedical NLP pipeline이 필요하다.
- **Why**: biomedical 과학 분야의 출판 증가로 인한 정보 overload 문제를 해결하기 위해 automated knowledge extraction이 필수적이고, 이를 위한 robust하고 practical한 도구가 필요하다.
- **Approach**: spaCy 라이브러리를 기반으로 biomedical 텍스트 관련 데이터셋(GENIA 1.0, OntoNotes 5.0)으로 POS tagger, dependency parser, NER 모델을 재학습하고, tokenization 모듈을 biomedical 특성에 맞게 개선한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Unlabeled attachment score (UAS) perfor-*

- **Universal Dependencies 변환 데이터셋 공개**: GENIA 1.0 corpus를 Universal Dependencies v1.0로 변환하고 원본 PubMed 텍스트와 정렬하여 공개
- **경쟁력 있는 성능**: POS tagging에서 98.51%, dependency parsing에서 LAS 88.79%를 달성하여 state-of-the-art와 비교 가능한 수준
- **뛰어난 처리 속도**: 추상(abstract) 당 33ms의 처리 속도로 C++/Java 기반 도구들과 경쟁력 있는 성능 제공
- **Domain robustness**: OntoNotes 5.0의 web 데이터를 혼합 학습하여 biomedical 성능 저하 없이 일반 텍스트에 대한 robustness 향상
- **9개 NER 모델 벤치마크**: 더 특화된 entity 추출 작업에서 강력한 baseline들과 경쟁력 있는 성능 제시

## How


- spaCy의 arc-eager transition-based parser with dynamic oracle를 기반으로 biomedical 데이터로 재학습
- CNN 기반 feature representation을 사용하여 POS tagging과 dependency parsing을 jointly 학습
- GENIA 1.0 treebank를 Stanford Dependency Converter로 Universal Dependencies v1.0로 변환
- OntoNotes 5.0과의 혼합 학습으로 domain shift에 대한 robustness 강화
- 두 가지 패키지 제공: en_core_sci_sm(작은 vocabulary, word vector 없음)과 en_core_sci_md(큰 vocabulary, 98,131개 word vector 포함)
- biomedical 특화 tokenization 규칙 추가로 약물명, 화학식 등의 처리 개선

## Originality

- spaCy라는 popular framework을 기반으로 biomedical domain에 특화된 통합 NLP pipeline 제공
- GENIA 1.0을 Universal Dependencies로 변환하고 원본 텍스트와 정렬하여 재사용 가능한 자원으로 공개
- 생산 환경에서 사용 가능한 수준의 속도와 성능 균형을 달성
- web data 혼합을 통한 systematic한 robustness 개선 방법론 제시

## Limitation & Further Study

- Dependency parsing에서 Biafﬁne parser에 2-3% 성능 차이로 인한 trade-off 존재
- NLP4J와 같은 순수 production 시스템보다는 느림 (Python 기반의 trade-off)
- 주로 PubMed 초록에 기반한 학습으로 clinical notes나 의료 기록의 다양한 형식에 대한 일반화 가능성 미검증
- 후속 연구: 추가 biomedical 특화 NER 모델 개발, clinical text 성능 특화, entity linking 통합

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: biomedical NLP의 실용적 문제를 해결하기 위해 잘 설계된 library를 제시하며, 공개 자원과 벤치마크를 제공함으로써 community에 의미 있는 기여를 한다. 성능과 속도의 균형을 잘 유지하고 있어 실무 적용 가능성이 높다.

## Related Papers

- 🔄 다른 접근: [[papers/161_BioBERT_a_pre-trained_biomedical_language_representation_mod/review]] — 생의학 자연어 처리에서 spaCy 기반과 BERT 기반이라는 서로 다른 아키텍처 접근법을 비교할 수 있다.
- 🔗 후속 연구: [[papers/167_Biomedlm_A_27_b_parameter_language_model_trained_on_biomedic/review]] — 생의학 언어 모델의 기초 위에 scispaCy의 구조화된 NLP 파이프라인을 통합하여 더 포괄적인 처리가 가능하다.
- 🏛 기반 연구: [[papers/344_Foundation_models_in_bioinformatics/review]] — 생명정보학에서 파운데이션 모델의 기초적인 이론과 방법론을 실용적인 NLP 도구로 구현한다.
