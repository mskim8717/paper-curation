---
title: "267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e"
authors:
  - "Tobias Braun"
  - "Mark Rothermel"
  - "Marcus Rohrbach"
  - "Anna Rohrbach (Technical University of Darmstadt & hessian.AI)"
date: "2025"
doi: "arXiv:2412.10510"
arxiv: ""
score: 4.4
essence: "본 논문은 텍스트와 이미지를 모두 포함하는 클레임(주장)을 검증하는 DEFAME이라는 멀티모달 팩트체킹 시스템을 제안한다. 6단계 동적 파이프라인을 통해 외부 도구와 멀티모달 LLM을 활용하여 증거를 검색하고 평가하며, 설명 가능한 검증 보고서를 생성한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Automated_Fact_Checking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tonglet et al._2024_Defame Dynamic evidencebased fact-checking with multimodal experts.pdf"
---

# DEFAME: Dynamic Evidence-based Fact-checking with Multimodal Experts

> **저자**: Tobias Braun, Mark Rothermel, Marcus Rohrbach, Anna Rohrbach (Technical University of Darmstadt & hessian.AI) | **날짜**: 2025 | **DOI**: [arXiv:2412.10510](https://arxiv.org/abs/2412.10510)

---

## Essence

![Figure 1](figures/fig1.webp)
*DEFAME의 개요: 멀티모달 클레임을 멀티모달 증거로 검증하여 상세한 인간친화적 보고서를 생성*

본 논문은 텍스트와 이미지를 모두 포함하는 클레임(주장)을 검증하는 DEFAME이라는 멀티모달 팩트체킹 시스템을 제안한다. 6단계 동적 파이프라인을 통해 외부 도구와 멀티모달 LLM을 활용하여 증거를 검색하고 평가하며, 설명 가능한 검증 보고서를 생성한다.

## Motivation

- **Known**: 전자 혐오정보(disinformation)의 급증으로 신뢰할 수 있는 팩트체킹이 필수적이며, 전문가 팩트체커가 처리하는 클레임의 약 80%가 멀티모달 형태임. 그러나 기존 자동 팩트체킹(AFC) 시스템은 대부분 텍스트만 처리함.

- **Gap**: 
  - 기존 멀티모달 AFC 시스템은 멀티모달 클레임과 멀티모달 증거를 동시에 처리할 수 없음
  - 증거 검색 기능이 부재하거나, 설명 가능성이 부족함
  - 대부분의 방법이 특정 영역이나 서브태스크에만 집중된 분산된 접근
  - 매개변수 지식(parametric knowledge)에만 의존하여 최신 클레임 검증 실패

- **Why**: 멀티모달 혐오정보는 시각적 정보를 "증거"로 해석하게 하여 특히 설득력이 높기 때문에 멀티모달 검증이 시급함.

- **Approach**: MLLM(멀티모달 대형언어모델)을 핵심으로 하는 6단계 동적 파이프라인을 설계하여, 웹 검색, 역이미지 검색 등 외부 도구를 활용한 동적 증거 검색과 멀티모달 처리를 통합하고 설명 가능한 보고서를 생성함.

## Achievement

![Figure 2](figures/fig2.webp)
*DEFAME의 6단계 파이프라인: Plan → Execute → Summarize → Develop → Judge → Justify*

1. **최첨단 성능 달성**: 
   - AVERITEC에서 65.6% → 70.5% (정확도 개선)
   - MOCHEG에서 +10.6% 정확도 개선
   - VERITE에서 True/False 정확도 +25.9% 개선

2. **새로운 벤치마크 구축 및 우수성 입증**: 
   - GPT-4O의 지식 한계(knowledge cutoff) 이후의 클레임으로 구성된 CLAIMREVIEW2024+ 벤치마크 개발
   - 이 벤치마크에서 DEFAME이 GPT-4O 기준 대비 현저히 우수하며 시간적 일반화 능력 시연
   - 인간 평가자들이 DEFAME의 보고서를 GPT-4O 출력보다 선호

## How

![Figure 3](figures/fig3.webp) ![Figure 4](figures/fig4.webp)
*CLAIMREVIEW2024+ 데이터셋의 예시와 GPT-4O 대비 DEFAME의 혼동 행렬*

**6단계 동적 파이프라인:**

- **Stage 1 (Plan)**: MLLM이 클레임 분석 후 필요한 검색 도구와 깊이 결정
- **Stage 2 (Execute)**: 웹 검색, 이미지 검색, 역이미지 검색(RIS), 지정보학(geolocation) 등 외부 도구 동적 활용
- **Stage 3 (Summarize)**: 검색된 증거 요약 및 정제
- **Stage 4 (Develop)**: 다중 홉(multi-hop) 추론을 통해 증거 추가 개발
- **Stage 5 (Judge)**: 증거 기반 최종 판단 (Supported/Conflicting/Refuted/NEI)
- **Stage 6 (Justify)**: 구조화된 멀티모달 팩트체크 보고서 생성

**핵심 설계 원칙:**

- Retrieval-Augmented Generation(RAG) 기반 접근으로 외부 증거 동적 검색
- 매개변수 지식 대신 검색된 증거에 의존하여 할루시네이션 위험 감소
- 각 단계마다 현재 보고서 상태를 컨텍스트로 포함하여 맥락 인식 능력 강화
- 멀티모달 처리: 클레임과 증거의 텍스트와 이미지를 모두 처리

**외부 도구 스위트:**
- Web Search, Google Search, Image Search, Google Image Search
- Reverse Image Search(RIS), Google Vision, GeoCLIP(지정보학)

## Originality

- **최초 통합 솔루션**: 멀티모달 클레임과 멀티모달 증거를 동시에 네이티브하게 처리하는 첫 번째 end-to-end AFC 프레임워크

- **동적 증거 검색**: 클레임 유형에 따라 도구와 검색 깊이를 자동으로 선택하는 적응형 메커니즘

- **설명 가능성**: 인간 팩트체커 워크플로우를 모방하여 구조화된 멀티모달 보고서 생성으로 투명성 확보

- **벤치마크 기여**: 데이터 누수 방지를 위해 GPT-4O 지식 한계 이후의 클레임으로 구성한 새로운 평가 세트 제공

- **기존 접근법과의 차이**: 
  - 기존 MLLM 기반 방법(예: RAGAR)은 텍스트 기반 증거만 검색하고 이미지를 텍스트 설명으로 변환하여 정보 손실 유발
  - 본 논문은 원본 이미지를 직접 처리하여 시각적 맥락 보존

## Limitation & Further Study

- **처리 시간**: 6단계 파이프라인과 다중 외부 도구 호출로 인한 지연 시간이 실제 운영 환경에서 도전 과제 될 수 있음

- **외부 도구 의존성**: 웹 검색 및 이미지 검색 API의 가용성과 정확도에 의존하며, 도구 오류 전파 가능성 존재

- **도메인 특화 성능**: 일반 도메인에 우수하나 특정 전문 분야(의학, 법률 등)에서의 성능 평가 부재

- **다국어 처리**: 현재 주로 영문 클레임과 증거에 초점을 두고 있으며 다국어 확장 필요

- **향후 연구 방향**:
  - 파이프라인 최적화를 통한 처리 시간 단축
  - 도메인 특화 모델 개발
  - 다언어 벤치마크 구축
  - 디ープ페이크 및 생성 이미지 검증 기능 확대


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: DEFAME은 멀티모달 팩트체킹의 분산된 연구를 통합하는 최초의 end-to-end 솔루션으로, 동적 도구 선택, 멀티모달 증거 처리, 설명 가능한 보고서 생성 측면에서 높은 독창성을 보여준다. 세 가지 주요 벤치마크에서 최첨단 성능을 달성하고 새로운 평가 세트를 제공한 점은 학계에 중요한 기여이다. 다만 처리 시간 및 도메인 특화 성능에 대한 평가가 추가되면 실용성이 더욱 강화될 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 멀티모달 팩트체킹의 발전된 접근법으로, 텍스트 중심의 NLP 사실확인 한계를 이미지까지 포함하여 해결합니다.
- 🔗 후속 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 프로그램 기반 추론을 활용한 복합 클레임 팩트체킹으로, DEFAME의 동적 파이프라인과 유사한 구조적 검증 접근법을 제시합니다.
- 🧪 응용 사례: [[papers/610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De/review]] — 비전-언어 모델의 환각 교정 시스템으로, 멀티모달 팩트체킹의 핵심 기술인 클레임 검증을 실제 모델 신뢰성 향상에 적용합니다.
- 🔄 다른 접근: [[papers/117_Augmenting_the_veracity_and_explanations_of_complex_fact_che/review]] — 복합적 사실 검증에서 동적 증거 증강 방식과 다중모달 증거 기반 접근법은 서로 다른 관점에서 검증 신뢰성을 향상시킨다.
- 🔗 후속 연구: [[papers/710_Sciclaimhunt_A_large_dataset_for_evidence-based_scientific_c/review]] — 다중모달 증거 기반 사실 확인 연구가 SciClaimHunt의 과학 논문 기반 주장 검증 데이터셋으로 구체화되었다
- 🧪 응용 사례: [[papers/852_Understanding_fine-grained_distortions_in_reports_of_scienti/review]] — 멀티모달 팩트체킹 기술을 과학 보도의 시각적 왜곡 감지에 적용할 수 있다
- 🔄 다른 접근: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 멀티모달 팩트체킹 시스템으로, 텍스트만의 사실확인 한계를 이미지까지 포함한 종합적 접근으로 해결합니다.
- 🔗 후속 연구: [[papers/183_Can_large_language_models_detect_misinformation_in_scientifi/review]] — 과학 뉴스의 오보 탐지가 다중모달 사실 확인으로 확장되어 더 포괄적인 검증이 가능하다.
- 🔗 후속 연구: [[papers/192_Cchall_A_novel_benchmark_for_joint_cross-lingual_and_cross-m/review]] — 동적 증거 기반 다중모달 사실 확인 시스템으로, CCHall에서 발견한 교차-언어/모달 환각 문제를 해결하는 구체적 솔루션을 제시한다
- 🧪 응용 사례: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 동적 증거 기반 다중모달 사실 확인 시스템으로, 프로그램 가이드 추론 방법론을 실제 다중모달 환경에 적용한 구체적 사례다
- 🧪 응용 사례: [[papers/394_Grounding_fallacies_misrepresenting_scientific_publications/review]] — 논리적 오류 탐지 방법을 다중 모달 팩트 체킹 시스템에 적용할 수 있는 실용적 연결점을 제공한다.
- 🏛 기반 연구: [[papers/610_Pelican_Correcting_Hallucination_in_Vision-LLMs_via_Claim_De/review]] — 멀티모달 증거 기반 팩트 체킹의 기초적인 방법론을 시각 언어 모델 환각 보정에 적용한다.
- 🏛 기반 연구: [[papers/657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A/review]] — 멀티모달 증거를 활용한 동적 팩트 체킹의 기초적인 방법론을 차트 영역에 적용한다.
- 🔗 후속 연구: [[papers/685_Robust_claim_verification_through_fact_detection/review]] — 멀티모달 팩트체킹을 텍스트 기반 사실 검출로 보완하여 확장한다
- 🧪 응용 사례: [[papers/057_aedfact_Scientific_fact-checking_made_easier_via_semi-automa/review]] — 멀티모달 팩트체킹을 위한 구체적인 시스템 구현 사례를 보여준다
- 🏛 기반 연구: [[papers/221_Claimver_Explainable_claim-level_verification_and_evidence_a/review]] — 멀티모달 증거 기반 팩트체킹을 위한 기본적인 증거 귀속 방법론을 제공한다
