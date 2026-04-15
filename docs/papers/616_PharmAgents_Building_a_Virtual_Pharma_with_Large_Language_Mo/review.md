---
title: "616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo"
authors:
  - "Bowen Gao"
  - "Yanwen Huang"
  - "Yiqiao Liu"
  - "Wenxuan Xie"
  - "Weiying Ma"
date: "2025"
doi: "10.48550/arXiv.2503.22164"
arxiv: ""
score: 4.0
essence: "PharmAgents는 대규모 언어모델(LLM) 기반의 다중 에이전트 시스템으로 신약 발견의 전체 파이프라인(타겟 발굴부터 전임상 평가까지)을 자동화하고 설명 가능하게 구현한 가상 제약사 플랫폼이다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Multi-Agent_System_Design"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2025_PharmAgents Building a Virtual Pharma with Large Language Model Agents.pdf"
---

# PharmAgents: Building a Virtual Pharma with Large Language Model Agents

> **저자**: Bowen Gao, Yanwen Huang, Yiqiao Liu, Wenxuan Xie, Weiying Ma | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.22164](https://doi.org/10.48550/arXiv.2503.22164)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. The Virual Pharma (PharmAgents) simulates the drug discovery process from target discovery to preclinical*

PharmAgents는 대규모 언어모델(LLM) 기반의 다중 에이전트 시스템으로 신약 발견의 전체 파이프라인(타겟 발굴부터 전임상 평가까지)을 자동화하고 설명 가능하게 구현한 가상 제약사 플랫폼이다.

## Motivation

- **Known**: 기존의 ML 모델들(binding affinity prediction, virtual screening, molecule generation, toxicity assessment 등)은 각각의 작업에서 높은 성능을 보이지만 독립적으로 작동하며 설명 가능성이 부족하여 자동화와 신뢰에 한계가 있다.
- **Gap**: 현존하는 AI 기반 신약 발견 도구들은 전체 파이프라인을 통합하지 못하고, 설명 가능성 부족으로 인해 전문가의 검증과 규제 환경에서의 수용이 어렵다는 문제가 있다.
- **Why**: 신약 개발은 시간과 비용이 많이 드는 복잡한 학제적 과정이므로, 이를 자동화하고 설명 가능하게 만들면 개발 속도를 획기적으로 단축하고 신뢰도를 높일 수 있기 때문에 중요하다.
- **Approach**: PharmAgents는 MetaGPT의 역할 기반 전략에 영감을 받아 신약 발견 프로세스를 4단계(target discovery, lead identification, lead optimization, preclinical evaluation)로 분해하고, 각 단계별로 LLM 기반 전문화된 에이전트를 설계한 후 구조화된 협업 프레임워크로 통합했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. The Virual Pharma (PharmAgents) simulates the drug discovery process from target discovery to preclinical*

- **타겟 발굴 정확성**: 무작위 테스트 질병에서 18개 중 16개의 타겟이 전문가에 의해 적절하다고 판단되어 신뢰성 높은 타겟 선정 능력 입증
- **분자 생성 및 최적화**: 질병별 뉘앙스를 포착하여 동일 타겟에 대해 상이한 특성의 화합물 설계 가능하며, 최신 기법보다 약물 개발 메트릭 성공률을 15.72%에서 37.94%로 향상
- **전임상 평가 견고성**: 대사 및 독성 평가에서 낮은 과소평가 위험(12%)을 유지하면서 합성 가능성을 정량 메트릭(Pearson correlation 0.645)과 잘 맞춘 해석 가능한 근거 제시
- **자기 진화 능력**: 과거 경험을 학습하여 미래 출력을 개선하는 메커니즘으로 성공률을 30%에서 36%로 증가

## How

![Figure 2](figures/fig2.webp)

*Figure 2. Overall workflow of the PharmAgents.*

- LLM 에이전트를 4개의 전문화된 모듈(타겟 발굴, 리드 확인, 리드 최적화, 전임상 평가)로 설계하고 각각에 domain-specific ML 모델과 computational tools 통합
- 구조화된 prompt engineering과 명확한 작업 분해로 coherent한 에이전트 간 협업 실현
- LLM의 광범위한 지식과 추론 능력을 보충하기 위해 고정밀 ML 모델들과 계산 플랫폼 활용 (특히 3D 구조 이해 등 LLM의 한계 보완)
- agent interaction과 knowledge exchange를 통한 self-evolvement 메커니즘으로 과거 경험에 기반한 반복 개선
- 각 단계별 명확한 책임 정의와 workflow 통합으로 개별 역량을 극대화하면서도 시스템 수준의 일관성 보장

## Originality

- 다중 에이전트 LLM 시스템을 신약 발견 전체 파이프라인에 처음으로 적용한 통합 프레임워크 제시
- MetaGPT의 역할 기반 전략을 제약 산업에 맞게 재해석하여 4단계 모듈로 구조화한 창의적 설계
- LLM의 설명 가능성을 활용하면서도 ML 모델의 정확성을 보충하는 하이브리드 접근법으로 투명성과 성능의 균형 달성
- 자기 진화 및 경험 학습 메커니즘으로 autonomous하고 scalable한 약물 발견 가능하게 한 점

## Limitation & Further Study

- 현재 프레임워크는 소분자 신약 발견에만 집중하며 생물학적 제제나 다른 형태의 약물로 확장 가능성에 대한 논의 부재
- 전문가 평가가 단일 질병의 무작위 테스트에만 제한되어 있으므로 광범위한 질병과 타겟에 대한 일반화 가능성 검증 필요
- 각 모듈별 에러 누적 메커니즘과 downstream 오류의 영향에 대한 상세한 분석 부족
- 임상 단계(clinical evaluation)로의 확장 경로와 규제 환경과의 실제 통합에 대한 구체적 로드맵 제시 필요
- 후속 연구로 comprehensive drug lifecycle management 달성을 위한 임상 및 시판 후 단계 통합 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: PharmAgents는 LLM 기반의 다중 에이전트 시스템을 신약 발견 파이프라인에 창의적으로 적용하여 자동화, 설명 가능성, 통합성을 동시에 달성한 매우 중요한 연구로, 자기 진화 능력과 실증된 성능 향상을 통해 AI 기반 제약 연구의 새로운 패러다임을 제시한다.

## Related Papers

- 🔄 다른 접근: [[papers/357_From_intention_to_implementation_automating_biomedical_resea/review]] — PharmAgents와 BioResearcher 모두 바이오메디컬 연구 자동화를 다루지만 각각 신약 발견과 포괄적 연구 파이프라인이라는 다른 범위에 집중함
- 🔗 후속 연구: [[papers/490_LIDDIA_Language-based_Intelligent_Drug_Discovery_Agent/review]] — LIDDIA의 언어 기반 신약 발견이 PharmAgents의 다중 에이전트 가상 제약사를 언어 모델 특화로 확장한 형태
- 🏛 기반 연구: [[papers/651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery/review]] — RAG 강화 협력 LLM 에이전트 연구가 PharmAgents의 다중 에이전트 신약 발견 시스템의 에이전트 협력 방식의 기반
- 🧪 응용 사례: [[papers/260_DeepCRE_Transforming_Drug_RD_via_AI-Driven_Cross-drug_Respon/review]] — LLM을 활용한 가상 제약회사 구축 연구가 DeepCRE의 신약 개발 후기 단계 약물 효과 비교 평가 시스템에 실제 적용되었다
- 🔗 후속 연구: [[papers/415_Hunt_Globally_Wide_Search_AI_Agents_for_Drug_Asset_Scouting/review]] — 가상 제약회사 구축과 글로벌 약물 자산 탐색은 모두 제약 산업의 AI 에이전트 활용이라는 공통 목표를 가진다.
- 🔗 후속 연구: [[papers/177_Can_ai_agents_design_and_implement_drug_discovery_pipelines/review]] — PharmAgents의 가상 제약회사 구축이 신약 발견 파이프라인 설계의 확장된 응용 시나리오를 제시한다
- 🔗 후속 연구: [[papers/350_Frame_Feedback-refined_agent_methodology_for_enhancing_medic/review]] — 가상 제약회사 구축 연구와 의료 연구 논문 생성을 결합하면 의약품 개발 전 과정의 자동화된 문서화 시스템을 구축할 수 있다.
- 🏛 기반 연구: [[papers/291_Drugclip_Contrastive_drug-disease_interaction_for_drug_repur/review]] — 가상 제약회사 구축을 위한 대규모 언어모델 에이전트가 약물 재창출 연구의 실제 응용과 상용화를 위한 기반을 제공한다.
- 🧪 응용 사례: [[papers/806_The_Virtual_Lab_AI_Agents_Design_New_SARS-CoV-2_Nanobodies_w/review]] — 가상 제약회사 구축을 위한 LLM 에이전트로, Virtual Lab 개념의 제약 산업 전반 확장 사례
- 🔄 다른 접근: [[papers/357_From_intention_to_implementation_automating_biomedical_resea/review]] — BioResearcher와 PharmAgents 모두 바이오메디컬 연구 자동화를 목표로 하지만 각각 드라이랩과 신약 발견에 특화된 접근법 사용
- 🔗 후속 연구: [[papers/663_Reinforcing_clinical_decision_support_through_multi-agent_sy/review]] — 가상 제약회사 시뮬레이션에서 윤리적 AI 거버넌스와 다중 에이전트 협력을 의료 환경으로 확장 적용
- 🔗 후속 연구: [[papers/351_FROGENT_An_End-to-End_Full-process_Drug_Design_Multi-Agent_S/review]] — 가상 제약회사 구축이 신약 설계 에이전트를 제약 산업 전체 시뮬레이션으로 확장한다
