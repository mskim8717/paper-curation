---
title: "1142_Beyond_Retractions_Forensic_Scientometrics_Techniques_to_Ide"
authors:
  - "Leslie D. McIntosh"
  - "A. Sinclair"
  - "Simon Linacre"
date: "2026"
doi: "10.48550/arXiv.2602.14793"
arxiv: ""
score: 4.0
essence: "Pharmakon Neuroscience Research Network라는 위조 연구 집단의 사례 분석을 통해 학술 출판 시스템에 내재된 취약점을 노출하고, 논문 철회를 넘어 부정행위를 적극적으로 탐지하기 위한 forensic scientometrics 기법을 제시한다."
tags:
  - "cat/Science_Policy_and_Research_Dynamics"
  - "cat/Computational_Bibliometric_Analysis"
  - "sub/Research_Reproducibility_Crisis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Beyond Retractions Forensic Scientometrics Techniques to Identify Research Misco.pdf"
---

# Beyond Retractions: Forensic Scientometrics Techniques to Identify Research Misconduct, Citation Leakage, and Funding Anomalies

> **저자**: Leslie D. McIntosh, A. Sinclair, Simon Linacre | **날짜**: 2026 | **DOI**: [10.48550/arXiv.2602.14793](https://doi.org/10.48550/arXiv.2602.14793)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Number of articles published per year by Pharmakon Neuroscience Network from*

Pharmakon Neuroscience Research Network라는 위조 연구 집단의 사례 분석을 통해 학술 출판 시스템에 내재된 취약점을 노출하고, 논문 철회를 넘어 부정행위를 적극적으로 탐지하기 위한 forensic scientometrics 기법을 제시한다.

## Motivation

- **Known**: 학술 출판에서 paper mills, 피어 리뷰 조작, 표절 등의 부정행위가 발생하며, 특히 GenAI의 발전으로 이러한 문제가 심화되고 있다는 것이 알려져 있다.
- **Gap**: 기존 연구는 개별 사례 연구나 메타 분석에 주로 집중했으나, 대규모 위조 연구 네트워크가 정당한 출판 채널에 어떻게 내재되는지, 그리고 철회되지 않은 채 지속되는 'citation leakage'를 체계적으로 탐지하는 방법론이 부족하다.
- **Why**: 연간 700만 개 이상의 논문이 출판되는 현황에서 저시성 부정행위가 수정되지 않으면 과학 기록의 무결성이 심각하게 훼손되고, 공적 자금 117백만 달러 이상이 위조 연구와 연계될 수 있기 때문이다.
- **Approach**: Trust markers 분석을 통한 초기 의심 신호 포착, Dimensions 데이터베이스를 활용한 네트워크 전문 검색, 시간적 출판 활동의 계층적 군집 분석(hierarchical clustering), 자금 추적을 통한 시스템적 위험 평가를 종합적으로 수행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: The country location of the 312 authors of PNRN papers.*

- **포괄적 네트워크 매핑**: 2019-2022년 활동 기간 동안 56개 저널, 12개 주요 출판사에 걸쳐 120개의 연구 및 리뷰 논문을 식별했으며, 40개국 232개 기관의 312명의 저자가 관여했음을 확인
- **시간적 저자 프로필 분류**: 네트워크 활동 전후 기간의 출판 행동 분석으로 4가지 서로 다른 시간적 출판 아키타입을 도출하여 네트워크와 긴밀하게 결합된 저자들을 식별
- **자금 추적 및 위험 평가**: 부정행위와 연계된 공적 자금 규모(117백만 달러 이상)를 정량화하고 시스템적 위험을 평가
- **Citation Leakage 현상 입증**: 대부분의 PNRN 관련 논문이 철회되지 않고 인용되는 'citation leakage' 메커니즘을 실증적으로 입증

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Funding statement from one of the PNRN publications exemplifying an unknown funding*

- Trust markers 프레임워크를 적용하여 개별 논문의 저자, 투명성, 재현성 요소 검토
- 이상 신호(비정상적인 이메일 형식, GRID에 미등록된 펀더 등)를 통해 초기 의심 사항 포착
- Dimensions 데이터베이스에서 'Pharmakon Neuroscience' 전문(full-text) 검색 수행", '2015-2018년(활동 전), 2019-2022년(활동 중), 2023-2025년(활동 후) 세 기간으로 나누어 비율 기반(proportional) 출판 활동의 계층적 군집 분석 실시
- 저자-기관-국가 네트워크 구조 시각화 및 공동 저자 패턴 분석
- 공개 자금 데이터베이스를 활용한 PNRN 참여 저자들의 자금 연계 추적

## Originality

- 기존 case study 중심의 접근을 벗어나, 대규모 위조 네트워크의 시간적 다층성을 체계적으로 분석하는 forensic scientometrics 방법론 개발
- Trust markers와 네트워크 분석, 자금 추적을 통합한 다층적 탐지 프레임워크 제시
- Citation leakage라는 새로운 개념을 정의하고, 논문 철회로 해결되지 않는 부정행위의 지속성을 정량적으로 증명
- 저자의 시간적 출판 프로필(temporal publication archetype)을 동적으로 분류하여 네트워크 결합도를 측정하는 신규 방법론 제안

## Limitation & Further Study

- 시간적 출판 패턴 분석만으로는 저자의 의도나 인식을 판단할 수 없으며, 부정행위에 무의식적으로 참여한 저자를 식별할 수 없는 한계가 있음
- Dimensions 데이터베이스에 의존하므로, 특정 저널이나 출판사가 데이터베이스에 미포함될 경우 네트워크의 전체 규모 추정이 과소될 수 있음
- PNRN 사례 이후 유사 네트워크의 위장 전략 변화에 대응하기 위해 trust markers의 지속적 업데이트 필요
- 자금 추적 시 간접적 연계만 파악 가능하며, 실제 자금 이체 및 사용 추적은 제도적 감시 강화가 필요함을 시사

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 학술 출판의 구조적 취약점을 적나라하게 드러내며, 기술적 방법론을 통해 실제 위조 네트워크를 식별한 중요한 사례 연구이다. 특히 forensic scientometrics라는 학제적 접근을 통해 단순 철회를 넘어 '살아 있는' 부정행위의 지속성을 조명함으로써, 향후 연구 무결성 감시 체계 강화를 위한 실용적이고 영향력 있는 근거를 제공한다.

## Related Papers

- 🔗 후속 연구: [[papers/988_Misconduct_Accounts_for_the_Majority_of_Retracted_Scientific/review]] — 단순한 부정행위 통계를 넘어서 사기 집단을 능동적으로 탐지하는 포렌식 방법론으로 발전시켰습니다.
- 🏛 기반 연구: [[papers/925_1500_scientists_lift_the_lid_on_reproducibility/review]] — 과학 연구의 재현성 문제에 대한 광범위한 조사 결과가 포렌식 과학계량학의 필요성을 뒷받침합니다.
- 🧪 응용 사례: [[papers/1079_REFORMS_Consensus-based_Recommendations_for_Machine-learning/review]] — 기계학습 연구의 타당성 보장을 위한 체크리스트와 연계하여 부정행위 예방의 사전적 접근법을 제시한다.
- 🧪 응용 사례: [[papers/1079_REFORMS_Consensus-based_Recommendations_for_Machine-learning/review]] — 연구 부정행위 탐지를 위한 실증적 사례로 REFORMS 체크리스트의 필요성을 구체적으로 보여준다.
- 🧪 응용 사례: [[papers/988_Misconduct_Accounts_for_the_Majority_of_Retracted_Scientific/review]] — 철회를 넘어선 포렌식 과학계량학 기법으로 부정행위 탐지 방법론을 확장할 수 있음
- 🔗 후속 연구: [[papers/1214_The_Story_is_Not_the_Science_Execution-Grounded_Evaluation_o/review]] — 연구 부정 탐지를 위한 포렌식 과학계량학 기법과 코드/데이터 검증을 통한 연구 문제 발견을 통합적으로 활용할 수 있다.
