---
title: "024_A_sober_look_at_llms_for_material_discovery_Are_they_actuall"
authors:
  - "Agustinus Kristiadi"
  - "Felix Strieth‐Kalthoff"
  - "Marta Skreta"
  - "Pascal Poupart"
  - "Alán Aspuru‐Guzik"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)이 분자 공간에서의 베이지안 최적화(BO)에 실제로 유용한지를 엄밀하게 평가하며, 베이지안 서로게이트 모델을 통해 원칙적인 불확실성 정량화를 제공한다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kristiadi et al._2024_A sober look at llms for material discovery Are they actually good for bayesian optimization over m.pdf"
---

# A sober look at llms for material discovery: Are they actually good for bayesian optimization over molecules? arXiv preprint arXiv:2402.05015, 2024.

> **저자**: Agustinus Kristiadi, Felix Strieth‐Kalthoff, Marta Skreta, Pascal Poupart, Alán Aspuru‐Guzik, Geoff Pleiss | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2402.05015](https://arxiv.org/abs/2402.05015)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. The surrogates we consider in this work. “PEFT” refers to parameter efficient finetuning which adds a (proport*

본 논문은 대규모 언어모델(LLM)이 분자 공간에서의 베이지안 최적화(BO)에 실제로 유용한지를 엄밀하게 평가하며, 베이지안 서로게이트 모델을 통해 원칙적인 불확실성 정량화를 제공한다.

## Motivation

- **Known**: 베이지안 최적화는 재료 발견에 광범위하게 사용되며, LLM은 다양한 과학 도메인에서 사전학습된 지식을 활용하는 잠재력을 보여주고 있다. 그러나 기존 LLM 기반 BO 연구는 휴리스틱 불확실성 추정에만 의존해왔다.
- **Gap**: LLM을 원칙적인 베이지안 프레임워크 내에서 분자 최적화를 위한 서로게이트 모델로 사용할 때의 실제 효용성이 불명확하며, 사전학습된 LLM 임베딩이 도메인 특화 지식 없이 화학 문제에 충분한지 미검증되었다.
- **Why**: 재료 발견은 비용이 높고 시간이 오래 걸리는 문제이므로, LLM이 효과적인 BO 가속화에 기여할 수 있는지 엄밀하게 평가하는 것은 자동화된 과학 발견의 실현에 필수적이다.
- **Approach**: 고정 특징 추출기로서의 LLM과 매개변수 효율적 미세조정(PEFT) + 라플라스 근사를 통한 적응 특징 LLM 서로게이트 모델을 제시하고, 8개의 실제 화학 문제와 8개의 LLM에 대해 광범위한 실험을 수행한다.

## Achievement

![Figure 4](figures/fig4.webp)

*Figure 4. Summarized performance of the results in Figure 3 in*

- **원칙적 베이지안 서로게이트 구성**: 기존의 점 추정 기반 비베이지안 LLM 대신 적절한 후분포(posterior)를 보유한 베이지안 신경망 기반 서로게이트 모델 제시
- **LLM 유용성의 조건부 결론**: LLM은 도메인 특화 데이터로 사전학습되거나 미세조정되었을 때만 분자 공간 BO에서 유용함을 입증
- **PEFT+베이지안 추론의 효율성**: 매개변수 효율적 미세조정과 라플라스 근사를 결합하여 계산 효율성과 원칙성을 동시에 달성
- **실용적 소프트웨어 라이브러리**: 이산 공간 BO용 오픈소스 라이브러리 제공으로 재현성 및 접근성 확보

## How

![Figure 2](figures/fig2.webp)

*Figure 2. The surrogates we consider in this work. “PEFT” refers to parameter efficient finetuning which adds a (proport*

- LLM의 마지막 계층 임베딩을 고정된 특징 추출기로 사용하여 표준 BO 서로게이트(GP, 베이지안 신경망)의 입력으로 활용
- LoRA, Adapter 등 PEFT 기법을 통해 LLM의 일부 가중치만 미세조정 가능하도록 설정
- 라플라스 근사(Laplace Linear Approximation)를 적용하여 미세조정 가중치 및 회귀 헤드에 대한 근사 후분포 계산
- 기대 개선(EI), 상신뢰도(UCB) 등 획득 함수를 통해 다음 평가 분자 선택
- 8개 화학 문제(약 분자 성질 예측)에서 반복적 BO 루프 실행 및 수렴 곡선 비교

## Originality

- LLM을 원칙적인 베이지안 프레임워크 내에 통합한 첫 시도로, 기존의 점 추정 기반 접근과 구별
- PEFT와 라플라스 근사의 조합을 통해 LLM 미세조정 시 계산-정확도 트레이드오프 해결
- 도메인 특화 사전학습의 중요성을 정량적으로 입증하는 체계적 실험 설계 (일반 LLM vs 화학 특화 LLM 비교)
- 화학 도메인에서 '스토캐스틱 패럿' 가설의 실증적 검증으로 LLM의 실제 이해력 vs 패턴 매칭 구분

## Limitation & Further Study

- **연속 공간 BO 미포함**: 논문은 사전정의된 분자 풀에서의 이산 공간 BO에만 집중하며, 연속 분자 표현 공간 최적화는 미래 과제
- **도메인 제한**: 화학 도메인만 연구 대상이며, 다른 과학 분야(생물학, 재료과학 등)로의 일반화 가능성 미검증
- **LLM 크기 및 종류**: 논문에서 평가한 LLM 종류가 제한적일 수 있으며, 더 대규모 또는 새로운 아키텍처에 대한 평가 필요
- **계산 비용 분석 부족**: PEFT+라플라스 근사의 상대적 계산 오버헤드에 대한 상세 분석 제공 필요
- **후속 연구 방향**: 멀티모달 LLM 활용, 더 효율적인 근사 베이지안 방법 탐색, 더 큰 분자 풀에서의 스케일링

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM 기반 분자 최적화에 대한 과장된 주장을 비판적으로 검토하면서 원칙적인 베이지안 프레임워크를 제시하는 매우 중요한 기여를 한다. 광범위한 실험과 실용적 라이브러리 제공으로 과학 발견의 자동화 분야에 높은 영향을 미칠 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/153_Best_humans_still_outperform_artificial_intelligence_in_a_cr/review]] — 재료 발견에서 LLM의 실용성과 창의성 영역에서 인간과 AI 비교라는 서로 다른 관점을 제시한다.
- 🔗 후속 연구: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 베이지안 최적화를 활용한 재료 발견에서 LLM 평가와 타겟 재료 발견이 상호 보완적 접근법을 보여준다.
- 🏛 기반 연구: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 재료 발견과 설계에서 LLM을 활용한 가설 생성이 베이지안 최적화 평가의 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/025_A_Survey_of_AI_for_Materials_Science_Foundation_Models_LLM_A/review]] — 재료 과학에서 AI 조사와 LLM의 실제 유용성 평가가 재료 발견 분야의 포괄적 이해를 제공한다.
- 🔄 다른 접근: [[papers/153_Best_humans_still_outperform_artificial_intelligence_in_a_cr/review]] — 창의성 영역에서 인간과 AI 비교와 재료 발견에서 LLM 실용성 평가라는 서로 다른 AI 능력 평가 접근법을 보여준다.
