---
title: "240_Crispr-gpt_An_llm_agent_for_automated_design_of_geneediting"
authors:
  - "Yuanhao Qu"
  - "Kaixuan Huang"
  - "Ming Yin"
  - "Kanghong Zhan"
  - "Dyllan Liu"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "CRISPR-GPT는 LLM 에이전트에 도메인 지식과 외부 도구를 통합하여 CRISPR 기반 유전자 편집 실험의 설계 과정을 자동화하고 향상시키는 시스템이다. 이는 비전문가 연구자도 가이드 RNA 설계부터 검증 실험까지 전체 프로세스를 수행할 수 있도록 지원한다."
tags:
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/CRISPR_and_Drug_Discovery_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qu et al._2024_Crispr-gpt An llm agent for automated design of geneediting experiments.pdf"
---

# Crispr-gpt: An llm agent for automated design of geneediting experiments

> **저자**: Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, Henry C. Cousins, William A. Johnson, Mengdi Wang, Mihir Shah, Russ B. Altman, Denny Zhou, Mengdi Wang, Le Cong | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2404.18021](https://arxiv.org/abs/2404.18021)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of CRISPR-GPT Agent.*

CRISPR-GPT는 LLM 에이전트에 도메인 지식과 외부 도구를 통합하여 CRISPR 기반 유전자 편집 실험의 설계 과정을 자동화하고 향상시키는 시스템이다. 이는 비전문가 연구자도 가이드 RNA 설계부터 검증 실험까지 전체 프로세스를 수행할 수 있도록 지원한다.

## Motivation

- **Known**: LLM은 광범위한 언어 능력을 보유하고 있으며, 최근 연구는 외부 도구 통합을 통해 문제 해결 능력을 향상시켰다. 그러나 일반 목적의 LLM은 CRISPR 설계 같은 전문 생물학 영역에서 환각(hallucination) 문제와 정확한 도메인 지식 부재로 인해 실패한다.
- **Gap**: 일반 목적의 LLM은 가이드 RNA 서열 설계에서 잘못된 정보를 고신뢰도로 제시하고, 오프타겟 효과 예측, 전달 방법 선택 등 복잡한 CRISPR 실험 설계에 필요한 구체적이고 최신의 도메인 지식이 부족하다.
- **Why**: CRISPR 기술의 접근성을 높이고 비전문가도 정확한 실험 설계가 가능하도록 함으로써 생의학 연구 가속화 및 치료법 개발을 촉진할 수 있다.
- **Approach**: LLM의 추론 능력에 Broad Institute의 gRNA 라이브러리, CRISPRPick toolkit 등의 계산 도구와 전문가 지식을 통합한 에이전트 기반 시스템을 구축하여, chain-of-thought 추론과 상태 머신을 활용해 단계적으로 실험 설계를 자동화한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Components of CRISPR-GPT enable human-AI collaboration to automate*

- **CRISPR 시스템 선택**: 실험 요구사항에 맞는 CRISPR 시스템(Cas9, CRISPRa/i, prime editing, base editing)을 자동으로 선택
- **gRNA 설계 최적화**: Broad Institute의 금표준 라이브러리 및 CRISPRPick toolkit을 활용하여 효율성과 특이성이 높은 가이드 RNA 서열 설계
- **세포 전달 방법 추천**: 표적 세포에 CRISPR 성분을 효과적으로 도입하는 최적의 방법 제시
- **오프타겟 효과 예측**: 의도하지 않은 DNA 변화 가능성을 체계적으로 평가
- **실험 프로토콜 자동 작성**: 목표에 맞춘 단계별 실험 절차 제공
- **검증 방법 및 프라이머 설계**: 편집 결과 검증을 위한 방법과 관련 프라이머 자동 설계
- **자유형 Q&A 및 심화 분석**: ad hoc 질의 응답과 사전 설계된 gRNA에 대한 심층 오프타겟 분석 제공

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Task decomposition process and state machine implementation algorithm.*

- LLM 기반의 설계 및 계획 엔진을 중심으로 구성하여 전문가 지식과 최근 문헌 검토를 통합
- gRNA 라이브러리 및 CRISPRPick과 같은 계산 toolkit을 에이전트에 통합하여 도구 호출 기능 제공
- Chain-of-thought 추론 모델 및 상태 머신을 활용하여 복잡한 설계 프로세스를 관리 가능한 단계로 단순화
- NCBI BLAST와 같은 외부 데이터베이스와의 연계를 통해 생성된 서열의 유효성 검증
- Interactive module을 통해 사용자와의 협업적 반복 개선 지원
- 실제 사용 사례를 통한 에이전트 유효성 검증

## Originality

- 일반 목적 LLM의 생물학적 hallucination 문제를 명시적으로 식별하고 이를 해결하기 위한 체계적 접근
- 도메인 특화 도구(CRISPRPick, gRNA 라이브러리)와 LLM의 추론 능력을 처음 통합한 CRISPR 설계 에이전트
- Chain-of-thought 추론과 상태 머신을 결합하여 생물학 실험 설계의 복잡성을 자동화하는 새로운 프레임워크
- 비전문가를 위한 진입 장벽을 낮추는 동시에 도메인 정확성을 유지하는 혁신적 접근

## Limitation & Further Study

- 일반 목적 LLM의 hallucination 완전 제거 불가능 - 지속적 모니터링 및 검증 필요
- 도구 통합이 Broad Institute 라이브러리 및 CRISPRPick 등 제한된 리소스에 의존
- 윤리 및 규제 고려사항에 대한 심층 논의 부재 - 자동화 유전자 편집 설계의 책임 있는 사용에 대한 추가 지침 필요
- 실제 실험 수행 단계의 자동화 미포함 - 설계 단계만 자동화
- 다양한 생물 시스템(식물, 미생물 등)에 대한 적용 범위 제한 가능성
- 후속 연구: 더 많은 실제 사용 사례를 통한 검증, 추가 도메인 도구 통합, 윤리 프레임워크 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: CRISPR-GPT는 LLM의 추론 능력과 도메인 특화 도구를 창의적으로 결합하여 유전자 편집 실험 설계를 민주화하는 중요한 기여이다. 일반 목적 LLM의 한계를 명확히 식별하고 체계적으로 해결한 점과 실제 사용성을 갖춘 통합 시스템을 제시한 점이 높이 평가된다.

## Related Papers

- 🔄 다른 접근: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — 동일한 CRISPR-GPT 시스템에 대한 다른 관점의 연구로 유전자 편집 실험 자동화의 완전한 이해를 제공한다
- 🔗 후속 연구: [[papers/290_DrugAgent_Automating_AI-aided_Drug_Discovery_Programming_thr/review]] — CRISPR 유전자 편집 자동화에서 AI 기반 약물 발견 프로그래밍이라는 더 광범위한 생물의학 자동화로 발전한다
- 🏛 기반 연구: [[papers/144_AutoProteinEngine_A_Large_Language_Model_Driven_Agent_Framew/review]] — 단백질 엔지니어링을 위한 LLM 기반 에이전트 프레임워크를 CRISPR 실험 설계의 기반 기술로 활용한다
- 🔄 다른 접근: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — CRISPR 유전자 편집 실험 자동화에서 동일한 시스템을 다른 관점에서 접근한 연구로 상호 보완적인 이해를 제공한다
