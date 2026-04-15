---
title: "541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist"
authors:
  - "Max Glockner"
  - "Yufang Hou"
  - "Iryna Gurevych"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "현재의 NLP 기반 사실확인(fact-checking) 접근법은 반박 증거(counter-evidence)의 존재를 가정하지만, 실제 미정보(misinformation)는 신뢰할 만한 증거가 부족한 환경에서 발생하기 때문에 현실적이지 않다. 본 논문은 기존 사실확인 데이터셋들이 모두 현실적 요구사항을 만족하지 못함을 보이고, 모델들이 누출된(leaked) 증거에 의존함을 실증한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Automated_Fact_Checking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Glockner et al._2022_Missing counter-evidence renders nlp fact-checking unrealistic for misinformation.pdf"
---

# Missing counter-evidence renders nlp fact-checking unrealistic for misinformation

> **저자**: Max Glockner, Yufang Hou, Iryna Gurevych | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: PolitiFact의 거짓 주장. 반박 증거를 찾기 어려운 경우, 사실확인자들은 주장의 근거가 된 가정을 반박함으로써 거짓을 증명한다.*

현재의 NLP 기반 사실확인(fact-checking) 접근법은 반박 증거(counter-evidence)의 존재를 가정하지만, 실제 미정보(misinformation)는 신뢰할 만한 증거가 부족한 환경에서 발생하기 때문에 현실적이지 않다. 본 논문은 기존 사실확인 데이터셋들이 모두 현실적 요구사항을 만족하지 못함을 보이고, 모델들이 누출된(leaked) 증거에 의존함을 실증한다.

## Motivation

- **Known**: NLP 커뮤니티는 지난 몇 년간 PolitiFact, Snopes 등 사실확인 기관의 데이터를 활용한 다양한 사실확인 데이터셋을 구축했으며, 기존의 FCNLP(NLP Fact-Checking Framework)는 증거 검색(evidence retrieval), 판정 예측(verdict prediction), 정당화 생성(justification production)으로 사실확인 과정을 구조화했다.

- **Gap**: FCNLP는 반박 증거가 항상 존재한다고 가정하지만, 실제 미정보는 신뢰할 만한 정보의 공백에서 발생한다. 예를 들어 "COVID-19 백신 제조를 위해 50만 마리의 상어가 살해될 수 있다"는 주장은 true라면 신뢰할 만한 출처가 보도했을 것이기에 반박 증거가 없다. 전문 사실확인자들은 이러한 상황에서 주장의 근거가 된 가정을 반박함으로써 거짓을 증명한다.

- **Why**: FCNLP의 가정은 실제 사실확인 워크플로우와 괴리가 있으며, 사실확인 기사에서 누출된 증거에 의존하면 새로운 미정보에 대한 실제 적용이 불가능하다.

- **Approach**: (1) 전문 사실확인자들의 검증 전략을 분석하여 현실적 사실확인의 조건 도출, (2) FCNLP가 이를 만족하지 못함을 보이고, (3) 기존 데이터셋들이 실제 조건을 위반함을 체계적으로 검토, (4) 모델이 누출된 증거에 의존하는 실험적 증거 제시.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: PolitiFact의 연도별 판정 비율. 2016년 이후 거짓 주장에 대한 사실확인이 증가하는 추세를 보임.*

1. **두 가지 현실적 조건 도출**: 전문 사실확인자들의 검증 과정 분석으로부터 (1) Source Guarantee—증거가 주장자의 근거를 구성하거나 그것을 지칭해야 함, (2) Context Availability—주장의 원본 환경을 파악할 수 있어야 함 등 두 가지 조건을 도출했다.

2. **현존 데이터셋의 현실성 부재 입증**: PolitiFact와 Snopes의 100개 미정보 주장을 분석한 결과, 65.3%가 Source Guarantee를 필요로 하는 검증 전략(Local Counter-Evidence 또는 Non-Credible Source)을 사용하나, 기존 FCNLP 기반 데이터셋들은 이를 만족하는 증거를 제공하지 못한다.

3. **누출 증거 의존성 실증**: 대규모 데이터셋(MULTIFC)에서 학습한 모델들이 사실확인 기사에서 누출된 증거에 의존하며, 이는 실제 미정보 대응에 부적합함을 보였다.

## How

- **인간 검증 전략 분석**: 100개 미정보 주장(PolitiFact/Snopes에서 각 50개)을 두 단계로 분석
  - 1단계: Source Guarantee 여부 판단
  - 2단계: 4가지 주요 전략 분류
    - Global Counter-Evidence (GCE): 주장 자체를 직접 반박 (26.7%)
    - Local Counter-Evidence (LCE): 근거 보장 필요 (46.7%)
    - Non-Credible Source (NCS): 신뢰할 수 없는 출처 (18.7%)
    - No Evidence Available (NEA): 이용 가능한 증거 없음 (6.7%)

- **증거 기준 정의**: 현실적 사실확인을 위한 두 가지 증거 기준
  - Sufficiency: 주장을 반박하기에 충분
  - No Leakage: 기존 사실확인 기사에서 누출되지 않음

- **데이터셋 조사**: FEVER, MULTIFC, X-FACT, AVeriTeC 등 기존 사실확인 데이터셋들이 위 기준을 만족하지 못함을 확인

- **실증 실험**: 누출된 증거 패턴을 식별하고 모델의 의존성을 정량화

## Originality

- **현실-이론 괴리 최초 지적**: NLP 사실확인 연구와 전문 사실확인자의 실제 워크플로우 간 근본적인 차이를 체계적으로 분석한 최초 연구

- **저널리즘 검증 프레임워크 도입**: 기술 중심의 FCNLP가 아닌 저널리즘적 관점에서 사실확인의 조건을 도출

- **미정보의 본질 강조**: 미정보가 신뢰할 만한 정보의 공백에서 발생한다는 기본적이나 간과된 통찰

- **구체적 증거 기준 제시**: 현실적 사실확인 데이터셋 구축을 위한 명확한 두 가지 증거 기준 제안

## Limitation & Further Study

- **분석 범위의 제한**: 100개 미정보 주장 분석은 통계적으로 제한적이며, PolitiFact와 Snopes에만 초점
  
- **멀티모달 추론 제외**: 조작된 이미지 등 다중 양식 미정보는 범위에서 제외

- **해결책 부재**: 현존 FCNLP의 문제를 지적하지만, 이를 극복하기 위한 구체적 방법론 제시 부족

- **후속 연구 과제**:
  - Source Guarantee와 Context Availability를 만족하는 데이터셋 구축 방법론 개발
  - 누출되지 않은 증거만으로 사실확인 가능한 모델 설계
  - 시계열적(temporal) 미정보 대응 전략 개발
  - 다국어/다문화 미정보 검증 확대


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4.5/5
- Overall: 4.5/5

**총평**: 본 논문은 NLP 사실확인 연구의 근본적인 현실성 문제를 명확히 지적하고, 저널리즘 관점의 검증 전략 분석을 통해 구체적 기준을 제시함으로써 해당 분야에 중요한 비판적 기여를 한다. 단, 제시된 문제의 해결책 부재는 아쉬운 점이다.

## Related Papers

- 🔄 다른 접근: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 멀티모달 팩트체킹 시스템으로, 텍스트만의 사실확인 한계를 이미지까지 포함한 종합적 접근으로 해결합니다.
- 🔗 후속 연구: [[papers/333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs/review]] — 지식 그래프를 활용한 사실 검증으로, 반박 증거 부족 문제를 구조화된 지식을 통해 보완하는 접근법을 제시합니다.
- 🧪 응용 사례: [[papers/832_Towards_llm-based_fact_verification_on_news_claims_with_a_hi/review]] — 뉴스 클레임에 특화된 사실 검증 시스템으로, NLP 사실확인의 실제 미정보 대응 분야 적용 사례입니다.
- ⚖️ 반론/비판: [[papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/review]] — 반박 증거 누락으로 인한 NLP 사실 확인의 비현실성을 지적한 연구가 SciClaimHunt의 포괄적인 증거 기반 검증 접근법에 대한 반대 관점을 제시한다
- 🏛 기반 연구: [[papers/852_Understanding_fine-grained_distortions_in_reports_of_scienti/review]] — 팩트체킹의 한계점 분석이 과학 보도 왜곡 연구의 이론적 기반을 제공한다
- 🔄 다른 접근: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 멀티모달 팩트체킹의 발전된 접근법으로, 텍스트 중심의 NLP 사실확인 한계를 이미지까지 포함하여 해결합니다.
- 🔗 후속 연구: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — NLP 팩트 체킹의 반박 증거 부족 문제를 언어모델 증류를 통한 무감독 학습으로 해결하는 방법론을 제시한다.
- ⚖️ 반론/비판: [[papers/192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m/review]] — NLP 사실 확인에서 반박 증거의 부족 문제를 지적하여, CCHall의 포괄적 환각 평가 접근법의 한계와 개선 방향을 제시한다
- 🔄 다른 접근: [[papers/394_Grounding_fallacies_misrepresenting_scientific_publications/review]] — 팩트 체킹에서 논리적 오류 탐지와 반증 증거 누락 문제라는 서로 다른 관점을 제시한다.
- 🏛 기반 연구: [[papers/441_Investigating_zero-and_few-shot_generalization_in_fact_verif/review]] — NLP 기반 팩트체킹의 현실적 한계에 대한 이론적 기반을 제공하여 zero-shot 일반화 연구의 동기를 설명한다.
