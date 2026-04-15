---
title: "880_What_makes_medical_claims_un_verifiable_analyzing_entity_and"
authors:
  - "Amelie Wührl"
  - "Yarik Menchaca Resendiz"
  - "Lara Grimminger"
  - "Roman Klinger"
date: "2024"
doi: "10.48550/arXiv.2402.01360"
arxiv: ""
score: 4.0
essence: "생의학 주장(biomedical claims)의 검증 가능성을 결정하는 요인을 분석하기 위해, 엔티티(entity)와 관계(relation) 속성에 중점을 두고 447개의 검증 불가능한 사례를 포함한 BEAR-FACT 코퍼스를 구축한 연구이다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Automated_Fact_Checking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Foley_2024_What makes medical claims (un) verifiable analyzing entity and relation properties for fact verific.pdf"
---

# What makes medical claims (un) verifiable? analyzing entity and relation properties for fact verification

> **저자**: Amelie Wührl, Yarik Menchaca Resendiz, Lara Grimminger, Roman Klinger | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2402.01360](https://doi.org/10.48550/arXiv.2402.01360)

---

## Essence

생의학 주장(biomedical claims)의 검증 가능성을 결정하는 요인을 분석하기 위해, 엔티티(entity)와 관계(relation) 속성에 중점을 두고 447개의 검증 불가능한 사례를 포함한 BEAR-FACT 코퍼스를 구축한 연구이다.

## Motivation

- **Known**: 선행 연구에 따르면 깔끔하게 추출된 주장이 사용자 생성 콘텐츠의 주장보다 검증에 더 강건하다는 것이 알려져 있음
- **Gap**: 생의학 주장의 어떤 속성이 검증 가능성(verifiability)에 영향을 미치는지에 대한 체계적 이해가 부족하며, 엔티티-관계 주석과 검증 결과를 동시에 포함하는 코퍼스가 존재하지 않음
- **Why**: 사실 검증 시스템의 성능 향상을 위해서는 검증 불가능한 주장의 특성을 파악하는 것이 필수적임
- **Approach**: 훈련된 주석자들이 PubMed에서 증거를 찾는 과정을 관찰하고, 엔티티-관계 패턴과 검증 가능성 간의 연관성을 분석하며, 중중 전문가와 일반인의 주석 품질을 비교

## Achievement

![Figure 1: Pairwise co-occurrence of verdicts in BEAR-FACT tweets with more than one claim](figures/fig1.webp) 
*다중 주장을 포함하는 트윗에서 검증 결과의 쌍별 공존 관계*

1. **BEAR-FACT 코퍼스 구축**: 1,448개의 사실 검증된 생의학 주장, 증거 문서, 구조화된 엔티티/관계 정보를 포함하는 첫 번째 트위터 데이터셋 제시 (30.9%가 검증 불가능)

2. **부정 관계의 검증 어려움**: 긍정 관계(예: cause-of)를 포함한 주장이 부정 관계(not-cause-of)보다 더 쉽게 검증되며, 더 높은 비율로 SUPPORTED 판정을 받음을 발견

3. **주석자 행동 패턴**: 사용자들이 주로 엔티티를 표준명으로 정규화하고 검색 쿼리에 제약조건을 추가하는 방식으로 검색을 개선함을 관찰

4. **도메인 전문성의 영향 제한**: 의료 전문가와 일반인 간 주석 신뢰도에 유의미한 차이가 없음을 확인

5. **검증 가능성 예측**: RoBERTa 모델을 미세조정하여 검증 가능한 주장 예측은 .82 F1로 높은 성능을 보였으나, 검증 불가능한 주장 탐지는 .27 F1로 저조함

## How

![Figure 2: Verdict distribution across claim relation and entity types](figures/fig2.webp)
*주장의 관계 및 엔티티 유형에 따른 검증 결과 분포*

- **데이터 구축**: BEAR 코퍼스(생의학 엔티티-관계 주석이 포함된 트윗)에서 주장을 포함하며 의료 관계를 가진 646개 문서 선별 → 엔티티-관계-엔티티 삼중항(triplet) 추출 → 수동 필터링 및 문법 수정을 통해 1,532개 주장 확보

- **주석 과정**: 2명의 훈련된 주석자가 PubMed를 사용하여 각 주장에 대해 증거 탐색 → 초기 쿼리(AND 연산자로 연결된 엔티티)에서 시작 → 최대 3분간 쿼리 개선 → 증거 발견 시 PMID 및 관련 문장 기록, 미발견 시 UNVERIFIABLE 레이블 부여

- **평가 메트릭**: 검증 결과 판정에 대한 Cohen's κ 스코어 (완벽한 일치=1.0), 증거 문서 검색에 대한 Jaccard 유사도 계산

- **모델 실험**: RoBERTa 미세조정을 통한 검증 가능성 분류 수행

## Originality

- **첫 번째 멀티모달 주석**: 생의학 엔티티-관계 구조와 사실 검증 결과를 동시에 주석한 최초의 코퍼스 제시
- **주석자 행동 관찰**: 실제 사실 검증 과정에서 주석자들의 쿼리 개선 방식을 체계적으로 분석하여 검색 쿼리 정규화 패턴 발견
- **포괄적 비교 분석**: 훈련된 전문 주석자, 의료 전문가, 일반인의 주석 품질을 직접 비교하여 도메인 전문성의 실제 영향 검토
- **부정 관계의 특수성 강조**: 언어학적으로 부정이 부가된 주장의 검증 어려움을 경험적으로 입증

## Limitation & Further Study

- **시간 제약의 영향**: 검증 불가능 판정이 3분 시간 제한에 의해 편향될 수 있으며, 실제로는 더 오래 찾으면 증거가 있을 수 있음 (주석자의 'evidence exists confidence' 점수로 부분 보정)

- **낮은 검증 불가능 예측 성능**: 검증 불가능한 주장 탐지의 F1이 .27에 불과해 실제 응용에는 제한적 (검증 가능한 주장은 .82 F1)

- **코퍼스 규모**: 1,532개 중 1,448개만 완성하여 리소스 부족으로 인한 미완성 상태

- **증거 문서 일치도 저조**: 동일 검증 결과에서도 Jaccard 유사도가 0.29에 불과해 주석자 간 증거 선택의 다양성이 높음

- **후속 연구 방향**: (1) 더 정교한 언어모델을 활용한 검증 불가능 판정 개선, (2) 부정 관계 처리를 위한 특화된 방법론 개발, (3) 크라우드소싱 규모 확대를 통한 신뢰도 검증, (4) 다언어 생의학 주장 검증 확대


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 생의학 사실 검증의 검증 불가능성 문제에 초점을 맞추어 체계적인 분석과 새로운 코퍼스를 제공한 의미 있는 연구이나, 검증 불가능 주장 예측의 낮은 성능과 시간 제약의 편향 문제는 실제 응용 측면에서의 한계를 보여준다.

## Related Papers

- 🔗 후속 연구: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 의료 주장 검증에서 검증가능성 분석으로 한 단계 더 깊이 있는 연구로 확장한다
- 🏛 기반 연구: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — 의료 도메인 LLM의 기반 기술이 의료 주장 분석에 필수적인 토대를 제공한다
- 🧪 응용 사례: [[papers/225_Clinicalgpt-r1_Pushing_reasoning_capability_of_generalist_di/review]] — 임상 추론 능력을 의료 주장의 검증가능성 판단이라는 구체적 작업에 적용한다
- 🧪 응용 사례: [[papers/226_ClinicalGPT_Large_Language_Models_Finetuned_with_Diverse_Med/review]] — 임상 특화 LLM을 의료 주장 검증이라는 구체적 작업에 적용한다
- 🔄 다른 접근: [[papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/review]] — 과학 연구의 검증 가능성을 철회된 논문 분석과 의료 주장 분석으로 다각도로 접근한다.
- 🏛 기반 연구: [[papers/328_Explainable_biomedical_claim_verification_with_large_languag/review]] — 의료 주장 검증 연구가 검증가능성 분석의 실용적 기반을 제공한다
