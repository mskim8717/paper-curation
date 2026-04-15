---
title: "128_Automatically_evaluating_the_paper_reviewing_capability_of_l"
authors:
  - "Mourad Ouzzani"
  - "Hossam M. Hammady"
  - "Zbys Fedorowicz"
  - "Ahmed K. Elmagarmid"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "LLM이 생성한 논문 리뷰가 인간 전문가 리뷰어와 동일한 중요 측면에 집중하는지 평가하기 위해 focus-level 평가 프레임워크를 제안하고, LLM들이 기술적 타당성에는 과도하게 집중하면서 새로움(novelty) 평가를 간과한다는 것을 발견했다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ouzzani et al._2025_Automatically evaluating the paper reviewing capability of large language models.pdf"
---

# Automatically evaluating the paper reviewing capability of large language models

> **저자**: Mourad Ouzzani, Hossam M. Hammady, Zbys Fedorowicz, Ahmed K. Elmagarmid | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2502.17086](https://arxiv.org/abs/2502.17086)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: We introduce a focus-level evaluation frame-*

LLM이 생성한 논문 리뷰가 인간 전문가 리뷰어와 동일한 중요 측면에 집중하는지 평가하기 위해 focus-level 평가 프레임워크를 제안하고, LLM들이 기술적 타당성에는 과도하게 집중하면서 새로움(novelty) 평가를 간과한다는 것을 발견했다.

## Motivation

- **Known**: 기존 연구들은 LLM 리뷰를 표면 수준(BLEU, ROUGE), 내용 수준(구체성, 사실 정확성), 결정 수준(accept/reject 분류 정확도)에서 평가해왔다. 하지만 LLM 리뷰가 전문가가 중시하는 논문의 강점과 약점을 균형있게 다루는지에 대한 체계적 평가는 부족하다.
- **Gap**: 기존 평가 방법들은 LLM 리뷰가 논문 평가의 핵심 차원(novelty, clarity, validity 등)을 균형있게 다루는지 여부를 종합적으로 평가하지 못한다. LLM 리뷰의 blind spot과 편향을 체계적으로 파악할 수 있는 프레임워크가 필요하다.
- **Why**: 논문 리뷰에서 focus의 불균형은 정확한 내용에도 불구하고 부실한 피드백을 초래할 수 있으며, 후배 리뷰어들에게 잘못된 판단 기준을 전파할 수 있다. LLM 리뷰의 blind spot을 파악하는 것은 인간 리뷰어가 LLM을 효과적으로 활용하고 LLM 개선을 위한 구체적 방향을 제시할 수 있게 한다.
- **Approach**: ICLR 컨퍼런스 676개 논문의 3,657개 전문가 강점/약점 데이터를 활용하여, target(problem, method, experiment 등 7개)과 aspect(validity, clarity, novelty 등 5개) facet을 정의하고 자동 annotator를 개발했다. 이를 통해 인간과 LLM의 focus 분포를 비교하는 평가 파이프라인을 구축했다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4: A visualization of focus distributions by target/aspect and strength/weakness, in a descending order of*

- **Focus-level 평가 프레임워크 제안**: 정규화된 attention 분포로 LLM 리뷰의 facet별 집중도를 체계적으로 분석하는 프레임워크 개발
- **자동 annotator 개발**: target과 aspect에 대해 Cohen's kappa 0.81, 0.79의 인간 합의도를 달성한 자동 annotation 시스템 구축", '**LLM 편향성 발견**: 8개 LLM 모두에서 기술적 validity에는 과도하게 집중하면서 novelty 평가는 심각하게 간과하는 일관된 패턴 발견
- **Fine-tuning 효과 입증**: fine-tuned GPT-4o가 prompting 방식의 LLM들보다 인간 focus 분포에 더 가까운 결과 생성
- **대규모 데이터셋 공개**: 676개 논문, 인간 리뷰, 3,657개 전문가 강점/약점, 8개 LLM의 43,042개 강점/약점 및 자동 annotation 데이터 공개

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The overall process of automated focus-level evaluation. We first extracted strengths and weaknesses*

- ICLR 2021-2024 논문 및 OpenReview 메타리뷰에서 강점/약점 자동 추출
- 9개 AI 컨퍼런스 가이드라인과 선행 문헌 검토를 통해 7개 target facet(Paper, Prior Research, Problem, Method, Theory, Experiment, Conclusion)과 5개 aspect facet(Validity, Clarity, Novelty, Impact, Reproducibility) 정의
- BERT 기반 자동 annotator 개발으로 각 강점/약점에 target과 aspect 레이블 할당
- 인간과 LLM(GPT-4, GPT-4o, Llama-70B, Llama-405B, DeepSeek-V3, DeepSeek-R1)의 focus 분포(frequency 정규화)를 계산하고 비교
- MARG와 fine-tuned GPT-4o를 포함한 다양한 모델 및 프롬프팅 전략 평가
- text similarity(BLEU, ROUGE 등)와 focus 분포 비교를 통한 holistic 평가

## Originality

- **Novel 평가 관점**: 기존의 표면/내용/결정 수준 평가를 넘어 focus-level 평가라는 새로운 차원 도입
- **체계적 facet 정의**: 컨퍼런스 가이드라인 기반의 target과 aspect 분리로 리뷰 분석의 구조화된 프레임워크 제공
- **자동화된 평가 파이프라인**: 인간 annotation 비용을 최소화하면서도 substantial agreement를 달성하는 자동 평가 시스템 구축
- **LLM blind spot의 구체적 규명**: 개별 metric 개선이 아닌 LLM의 근본적 편향성(novelty 간과)을 체계적으로 드러냄

## Limitation & Further Study

- **자동 annotator의 한계**: F1 0.373은 여전히 제한적이며, 복잡한 강점/약점에서 target과 aspect 할당의 오류가 누적될 수 있음
- **단일 도메인 평가**: ICLR 컨퍼런스만 대상으로 하여 다른 분야(NLP, Vision 등) 리뷰의 일반화 가능성 불명확
- **Facet 정의의 상대성**: target과 aspect의 7+5 구분이 최적인지, 다른 granularity가 더 유용할 수 있는지 검토 필요
- **인간 리뷰의 노이즈**: 메타리뷰 기반 추출로 인한 bias와 일부 중요한 강점/약점 누락 가능성
- **후속 연구**: LLM focus 개선을 위한 구체적 intervention 전략(prompt engineering, fine-tuning 최적화 등) 개발 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 LLM 리뷰 평가에 새로운 focus-level 관점을 도입하여 기존 평가의 맹점을 보완하고, 자동화된 프레임워크를 통해 대규모 분석을 가능하게 했다. 특히 LLM들의 일관된 novelty 간과 패턴 발견은 학술 리뷰 품질 문제를 구체적으로 드러내며, 공개 데이터셋은 후속 연구에 중요한 기여를 할 것으로 기대된다.

## Related Papers

- 🔗 후속 연구: [[papers/664_RelevAI-Reviewer_A_Benchmark_on_AI_Reviewers_for_Survey_Pape/review]] — LLM의 논문 심사 능력 평가와 조사 논문용 AI 심사자 벤치마크를 결합하면 다양한 학술 문서 유형에 대한 포괄적 심사 능력 평가가 가능하다.
- 🏛 기반 연구: [[papers/678_ReviewerGPT_An_Exploratory_Study_on_Using_Large_Language_Mod/review]] — 대형 언어모델을 활용한 논문 심사 탐색 연구가 LLM 논문 심사 능력의 체계적 평가 방법론 개발의 선행 연구 기반을 제공한다.
- 🧪 응용 사례: [[papers/537_Mind_the_blind_spots_A_focus-level_evaluation_framework_for/review]] — LLM의 논문 리뷰 능력 자동 평가 연구에서 focus-level 프레임워크가 실제 성능 측정에 적용된다.
