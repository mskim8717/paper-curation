---
title: "486_Lego-prover_Neural_theorem_proving_with_growing_libraries"
authors:
  - "Huajian Xin"
  - "Haiming Wang"
  - "Chuanyang Zheng"
  - "Lin Li"
  - "Zhengying Liu"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "대규모 언어모델(LLM)을 이용한 신경 정리 증명(Neural Theorem Proving)에서 검증된 보조정리(lemma)를 재사용 가능한 기술(skill)로 활용하는 성장 가능한 라이브러리를 도입함으로써, 모듈식 증명 구성을 통해 증명 능력을 대폭 향상시킨다. 이를 통해 miniF2F 벤치마크에서 최첨단 성능을 달성하고 22,532개의 검증된 기술을 자동 생성한다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Retrieval-Augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Xin et al._2023_Lego-prover Neural theorem proving with growing libraries.pdf"
---

# Lego-prover: Neural theorem proving with growing libraries

> **저자**: Huajian Xin, Haiming Wang, Chuanyang Zheng, Lin Li, Zhengying Liu, Qingxing Cao, Yinya Huang, Jing Xiong, Han Shi, Enze Xie, Jian Yin, Zhenguo Li, Xiaodan Liang, Heng Liao | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1(a) and (b)](figures/fig1.webp)
*LEGO-Prover의 구조: (a) Plain prover와의 비교 - LEGO-Prover는 모듈식 증명 구성, (b) 프로버(Prover)와 에볼버(Evolver)로 이루어진 전체 프레임워크*

대규모 언어모델(LLM)을 이용한 신경 정리 증명(Neural Theorem Proving)에서 검증된 보조정리(lemma)를 재사용 가능한 기술(skill)로 활용하는 성장 가능한 라이브러리를 도입함으로써, 모듈식 증명 구성을 통해 증명 능력을 대폭 향상시킨다. 이를 통해 miniF2F 벤치마크에서 최첨단 성능을 달성하고 22,532개의 검증된 기술을 자동 생성한다.

## Motivation

- **Known**: 기존 신경 정리 증명 방법들(step-by-step proof generation, single-pass proof generation)은 순차적으로 전체 증명을 직접 생성하는 "plain prover" 방식을 사용하며, ChatGPT/GPT-4의 도움에도 불구하고 장거리 연쇄(long-chain) 증명에서 실패한다.

- **Gap**: Plain prover들은 고정된 정리 라이브러리를 가정하고, 이전에 증명된 보조정리들을 재활용하지 못하며, 새로운 유용한 정리/이론 생성이 결여되어 있다. 또한 문제별 증명 통찰력 공유 메커니즘이 부족하다.

- **Why**: 수학에서 새로운 유용한 정리나 이론의 창조는 더 어려운 결과를 증명하기 위해 필수적이며, LEGO 블록처럼 모듈식으로 구성된 재사용 가능한 기술 라이브러리는 복잡한 문제 해결을 체계적으로 촉진할 수 있다.

- **Approach**: 성장 가능한 기술 라이브러리를 중심으로 프로버(정리 증명 수행)와 에볼버(생성된 기술의 일반화 및 재사용성 향상)로 구성된 LEGO-Prover를 제안한다.

## Achievement

![Figure 3](figures/fig3.webp)
*성장하는 기술 라이브러리의 효과: LEGO-Prover의 증명 성공률 변화*

1. **벤치마크 성능 향상**: miniF2F-valid에서 48.0% → 57.0%, miniF2F-test에서 45.5% → 50.0%로 기존 최첨단 대비 평균 6.75% 절대 개선

2. **대규모 기술 라이브러리 자동 구성**: 증명 과정 중 20,532개 이상의 검증된 보조정리/정리(skill) 자동 생성 및 라이브러리 구축

3. **기술 라이브러리의 검증된 효과**: 기술 라이브러리 활용에 따른 성공률 47.1% → 50.4% 개선을 통해 새로 추가된 기술들의 실질적 유용성 입증

4. **증명 간극 감소**: 생성된 기술 라이브러리가 인간 증명과 형식 증명(formal proof) 간 격차를 완화하여 누락된 단계 추론 용이성 향상

## How

![Figure 2](figures/fig2.webp)
*LEGO-Prover의 작동 흐름: (a) 프로버의 3단계 증명 과정 (b) 스킬 라이브러리와의 상호작용*

**1. 프로버(Prover) 모듈**:
- 형식 정리 명제(formal statement)로부터 비형식 증명(informal proof) 기반 보조정리 필요성 식별
- 라이브러리로부터 관련 기술 검색 및 검색된 기술 활용하여 모듈식 증명 구성
- 증명 과정에서 새로운 보조정리 자동 생성 및 라이브러리에 누적

**2. 에볼버(Evolver) 모듈**:
- 프로버에서 생성된 문제별 기술들의 일반성(generality) 향상
- 방향성 변환(directional transformer)을 통해 기술의 재사용성 및 복잡도 개선
- 검증된 발전 기술을 라이브러리에 역피드백

**3. 기술 라이브러리(Skill Library)**:
- 검증된 보조정리/정리 저장소로 기능
- 임베딩 기반 유사성 검색(embedding-based similarity search)으로 관련 기술 효율적 검색
- 지속적으로 성장하며 새로운 증명 문제에 활용

**4. 기술 활용 방식**:
- **직접 사용(Direct use)**: 검색된 기술을 증명에 직접 복사 사용
- **참조(Referee)**: 검색된 기술을 모델의 추론 가이드로 활용

## Originality

- **신경-기호 하이브리드 접근의 혁신**: 신경 정리 증명에 성장 가능한 검증된 보조정리 라이브러리를 최초로 통합하여 기존의 순차적 증명 생성 방식을 모듈식 구성으로 전환

- **이중 루프 학습 메커니즘**: 프로버-에볼버 구조를 통해 문제별 기술 생성과 일반화된 기술 추출을 동시에 수행하는 이중 루프 최적화 도입

- **스킬 기반 에이전트의 형식 수학 적용**: AI 에이전트의 동적 스킬 축적 패러다임을 형식 수학 증명 영역에 처음으로 체계적으로 적용

- **인간 증명과의 간극 축소**: 생성된 라이브러리가 인간 비형식 증명(informal proof)과 기계 검증 형식 증명(formal proof) 간 구간(gap) 해소에 기여하는 구체적 메커니즘 제시

## Limitation & Further Study

- **라이브러리 초기화 문제**: 초기 라이브러리가 공집합인 경우 부트스트랩 효율성 및 초기 성능 저하 가능성에 대한 상세 분석 부재

- **에볼버의 일반화 한계**: 방향성 변환기(directional transformer)의 일반화 메커니즘이 특정 수학 영역에 편향될 가능성 및 영역 간 전이 가능성 미검토

- **계산 비용**: 프로버와 에볼버의 반복 실행으로 인한 누적 계산 비용(computational overhead) 분석 및 실행 시간 메트릭 부재

- **후속 연구 방향**:
  - 다양한 형식 정리 증명기(Lean, Isabelle, Coq 등)에 대한 일반화 및 적용
  - 외부 자동 정리 증명기(ATP)와의 협력 강화
  - 기술 라이브러리의 의미론적 구조화 및 메타 정보 활용 고도화
  - 장거리 의존성을 가진 복잡한 증명에서의 성능 향상 방안

## Evaluation

- **Novelty**: 4.5/5 — 성장 가능한 라이브러리 기반 모듈식 증명은 신경 정리 증명 분야에서 신선한 패러다임 제시하나, 개별 기술들(검색, 에볼버)은 기존 기술의 응용

- **Technical Soundness**: 4/5 — 전체 프레임워크 설계와 실험 방법론은 타당하나, 에볼버의 일반화 메커니즘 및 기술 검색 알고리즘의 이론적 정당성에 대한 심화 분석 부족

- **Significance**: 4.5/5 — miniF2F 벤치마크에서 6.75% 절대 개선 달성 및 22,500+ 기술 자동 생성은 형식 수학 자동화에 실질적 기여, 다만 더 복잡한 대학원 수준 정리로의 확장 가능성 미명확

- **Clarity**: 4/5 — 전반적으로 명확하게 설명되었으나, 에볼버의 상세 알고리즘 및 기술 검색 메커니즘의 구현 세부사항이 다소 추상적

- **Overall**: 4.2/5

**총평**: LEGO-Prover는 신경 정리 증명에 성장 가능한 검증된 보조정리 라이브러리를 도입하는 창의적 접근으로 명확한 성능 향상을 달성하였으며, 생성된 대규모 기술 라이브러리의 실용적 가치를 입증했다. 다만 더 복잡한 수학 문제로의 확장성과 계산 비용 효율성에 대한 추가 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/568_Mustard_Mastering_uniform_synthesis_of_theorem_and_proof_dat/review]] — 둘 다 정리 증명을 위한 데이터셋과 방법론을 다루지만, Lego-prover는 성장 가능한 라이브러리에, MUSTARD는 균일한 합성에 집중한다
- 🔗 후속 연구: [[papers/264_Deepseek-prover_Advancing_theorem_proving_in_llms_through_la/review]] — LLM의 대규모 정리 증명 학습 연구가 Lego-prover의 성장 가능한 기술 라이브러리를 활용한 모듈식 증명 구성으로 발전되었다
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 스케치 기반 정리 증명 방법론이 Lego-prover의 검증된 보조정리를 재사용 가능한 기술로 활용하는 시스템의 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/257_Decomposing_the_enigma_Subgoal-based_demonstration_learning/review]] — 형식 정리 증명의 구조화된 학습이 일반적인 라이브러리 기반 정리 증명의 기반이 된다.
- 🔄 다른 접근: [[papers/568_Mustard_Mastering_uniform_synthesis_of_theorem_and_proof_dat/review]] — 형식 정리 증명을 대규모 LLM 대신 성장하는 라이브러리를 활용한 다른 신경망 접근법
- 🧪 응용 사례: [[papers/379_Generative_language_modeling_for_automated_theorem_proving/review]] — 신경망 기반 정리 증명기의 실제 구현으로, 생성 언어모델을 활용한 형식 수학의 발전된 응용 사례입니다.
- 🏛 기반 연구: [[papers/288_Draft_sketch_and_prove_Guiding_formal_theorem_provers_with_i/review]] — 신경망 정리 증명의 기반 위에서 라이브러리 확장과 비형식적 증명 활용이라는 발전된 방법론을 구축한다.
