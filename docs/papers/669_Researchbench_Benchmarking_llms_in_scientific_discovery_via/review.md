---
title: "669_Researchbench_Benchmarking_llms_in_scientific_discovery_via"
authors:
  - "Yujie Liu"
  - "Zonglin Yang"
  - "Tong Xie"
  - "Jinjie Ni"
  - "Ben Gao"
date: "2025"
doi: "arXiv:2503.21248v2"
arxiv: ""
score: 4.2
essence: "본 논문은 과학적 발견 과정에서 LLM의 역량을 평가하기 위한 첫 번째 대규모 벤치마크 **ResearchBench**를 제시한다. 영감 검색(inspiration retrieval), 가설 구성(hypothesis composition), 가설 순위 결정(hypothesis ranking)의 세 가지 하위 작업으로 과학 발견 과정을 분해하고, 12개 분야의 1,386편 논문(2024년 발행)으로부터 자동 추출 프레임워크를 통해 벤치마크를 구축했다."
tags:
  - "cat/Scientific_Research_Capability_Evaluation"
  - "sub/Scientific_LLM_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zheng et al._2025_Researchbench Benchmarking llms in scientific discovery via inspiration-based task decomposition.pdf"
---

# ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition

> **저자**: Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, Erik Cambria, Dongzhan Zhou | **날짜**: 2025 | **DOI**: [arXiv:2503.21248v2](https://arxiv.org/abs/2503.21248)

---

## Essence

본 논문은 과학적 발견 과정에서 LLM의 역량을 평가하기 위한 첫 번째 대규모 벤치마크 **ResearchBench**를 제시한다. 영감 검색(inspiration retrieval), 가설 구성(hypothesis composition), 가설 순위 결정(hypothesis ranking)의 세 가지 하위 작업으로 과학 발견 과정을 분해하고, 12개 분야의 1,386편 논문(2024년 발행)으로부터 자동 추출 프레임워크를 통해 벤치마크를 구축했다.

## Motivation

- **Known**: LLM이 과학 연구의 보조 도구로서 가능성을 보여주고 있으며, 인지과학 연구에 따르면 창의적 아이디어는 서로 무관해 보이는 두 개 이상의 지식을 결합하여 생성된다 (Koestler, 1964).

- **Gap**: 기존 LLM 벤치마크(ChatBot Arena, MixEval 등)는 일반적인 능력을 평가하지만, **과학적 발견 능력을 구체적으로 평가할 수 있는 전문화된 벤치마크가 부재**하다. 또한 가설 형성 과정에 대한 이해 부족으로 인해 평가 방법론이 미확립되어 있다.

- **Why**: LLM이 과학 연구 협력자로 역할 하기 위해서는 새로운 가설 발견 능력이 필수적이며, 이를 측정하기 위한 체계적인 벤치마크 필요성이 높다.

- **Approach**: Yang et al. (2024c)의 과학 발견 분해 이론(배경 지식 b + 영감 지식 i들 → 가설 h)을 12개 분야로 확장하고, 자동화된 LLM 기반 에이전트 프레임워크로 2024년 출간 논문에서 연구 질문, 배경 조사, 영감, 가설을 추출하여 벤치마크 구성.

## Achievement

![Figure 1: Overview of the inspiration retrieval framework.](figures/fig1.webp)
*영감 검색 프레임워크: 논문에서 추출된 잠재적 영감을 필요성 검증(Necessary Checker)과 충분성 검증(Sufficient Checker)을 거쳐 확정*

1. **첫 번째 대규모 과학 발견 벤치마크 구축**: 12개 분야(화학, 물리학, 천문학, 생물학, 재료과학, 에너지과학, 환경과학, 비즈니스, 법학, 수학 등) 1,386편의 Nature/Science 급 논문으로 구성. 전문가 검증 결과 91.9% 정확도(주요 이슈만 고려) 달성.

2. **혁신적 LLM 기반 자동 추출 프레임워크**: 연구 질문, 배경 조사, 가설의 직접적 추출과 달리, 영감 추출을 위해 필요성/충분성 검증 이중 구조를 설계하여 정확도 향상. 향후 LLM 학습 데이터 커트오프 이후에도 자동 확장 가능한 설계.

3. **데이터 오염 방지 및 분포 외(OOD) 작업 발견**: 2024년 이후 논문만 선택하여 기존 LLM 사전학습 데이터와의 중복 최소화. 영감 검색이 본질적으로 OOD 작업임을 인식하고 평가—GPT-4o가 상위 4% 후보 중 지면 영감을 포함할 확률이 45.7%에 달하는 놀라운 성능 발견.

4. **LLM을 "연구 가설 채굴 기계(research hypothesis mines)"로 위치 지음**: 세 가지 기본 작업에서의 우수한 성능이 LLM을 대규모 혁신 과학 통찰 자동 생성 도구로서의 가능성을 제시.

## How

![Figure 1: Overview of the inspiration retrieval framework.](figures/fig1.webp)

### 벤치마크 구축 방법론

- **수학적 기초**: 가설 h는 배경 지식 b와 k개의 영감 i₁...iₖ의 함수로 표현 (h = f(b, i₁, ..., iₖ)). 이는 인지과학 이론에 기반.

- **자동 추출 에이전트**:
  - 연구 질문, 배경 조사, 가설: 신중한 프롬프트 설계와 반복적 자기개선(iterative self-refine) 적용
  - 영감 추출: 논문의 서론/관련 연구/방법론 섹션에서 "Motivated by" 형태로 기술된 참고문헌을 추출하고, Semantic Scholar/Crossref API로 초록 수집
  - 이중 검증 구조: 필요성 검증(중복 제거)과 충분성 검증(정보 범위 커버 확인)

- **음성 샘플(Negative Sample) 구성**:
  - 각 논문마다 3개 수준의 음성 영감 논문 구성 (거리 기반 분류)
  - 도메인 관련성, 시간적 근접성 등 다양한 혼동 요소 포함하여 LLM 성능의 심층적 분석 가능

- **Pairwise 평가 채택**: 가설 순위 결정 시 직접 점수화 대신 쌍 비교(R(hᵢ, hᵢ₊₁))를 사용하여 평가 견고성 향상.

- **시간적 오염 방지**: 2024년 이후 출간 논문만 사용 (각 모델의 학습 데이터 커트오프: Table 8 참조)

### 핵심 기술 특징

- 자동화 + 전문가 검증 혼합 접근(62편 무작위 표본 검증)
- OOD 영감 검색 능력의 정량적 평가 최초 시도
- 12개 다분야 확장으로 발견의 보편성 검증

## Originality

- **이론적 기여**: Yang et al. (2024c)의 화학/재료과학 한정 분해 이론을 12개 분야로 확장하여 **과학 발견의 보편적 원리** 입증

- **벤치마크 설계 혁신**:
  - IdeaBench(생의학 한정, 하위작업 부분 평가) 대비 **다분야, 전체 작업 포괄**
  - DiscoveryBench/ScienceAgentBench(20~44편 논문)보다 **1,386편 대규모 구축**
  - 규칙 기반 추출 대신 **LLM 기반 에이전트 프레임워크** 도입으로 정확도와 확장성 동시 달성

- **평가 관점의 혁신**: 
  - **OOD 영감 검색 평가** 도입—기존에 주목하지 않은 핵심 능력 규명
  - **음성 샘플 설계의 정교함**—진정한 혼동 사례로 LLM 능력의 미세한 차이 포착

- **실무적 통찰**: LLM을 "가설 채굴 기계"로 개념화하여 대규모 과학 발견의 자동화 가능성 제시

## Limitation & Further Study

- **추출 정확도 한계**: 91.9%(주요 이슈)/82.3%(주요+경미 이슈) 정확도는 벤치마크 신뢰도에 미세한 영향. 특히 복잡한 다중 영감 논문이나 암묵적 영감 표현에서 추출 오류 가능성.

- **"영감"의 정의 모호성**: 논문에서 영감의 명확한 정의 부재. 참고문헌 중 어느 것이 진정한 "영감"인지 vs. 단순 배경 지식인지의 경계 불명확—이는 음성 샘플 구성 시 논쟁 여지 존재.

- **선택 편향**: 상위 저널(Nature/Science 급)만 선택하여 **저널 등급 다양성 부족**. 일반적인 과학 발견 과정을 대표하지 못할 가능성.

- **언어 한계**: 논문이 영문 기반이므로 **비영어권 과학 공동체의 발견 패턴 미반영**.

- **평가 해석의 한계**: LLM의 우수한 성능(45.7%)이 진정한 "창의적 연관성 발견" 능력을 의미하는지, 아니면 "통계적 패턴 매칭"에 불과한지 불명확. 생성된 가설의 **과학적 타당성 검증 부재**.

### 향후 연구 방향

- 생성된 가설을 실제 과학자가 검증하여 **과학적 실질 가치** 평가
- 더 최근 모델(2024년 이후 출시 모델)에 대한 지속적 벤치마킹
- 영감 통합 방식의 명시화 및 가설 품질 평가 기준의 정량화
- 저널 다양성, 언어 다양성 확장을 통한 **보편성 강화**
- 인간과 LLM의 협력 시나리오에서 가설 생성 성능 평가


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: **ResearchBench**는 과학 발견에서 LLM의 역량을 평가하는 **첫 번째 체계적이고 대규모의 벤치마크**로서, 영감 검색의 OOD 능력 발견과 자동 추출 프레임워크의 설계에서 상당한 원창성을 보유하고 있다. 다만, 추출 정확도의 한계, "영감"의 철학적 정의 부재, 생성 가설의 과학적 타당성 검증 부재 등이 미해결 과제로 남아 있으며, 이들이 해소될 경우 과학 발견 자동화 연구의 중요한 기반이 될 수 있을 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea/review]] — 과학적 발견 평가에서 ResearchBench의 체계적 접근법과 LiveIdeaBench의 창의성 중심 평가는 상호보완적인 벤치마크 설계 방식이다.
- 🏛 기반 연구: [[papers/835_Towards_Scientific_Intelligence_A_Survey_of_LLM-based_Scient/review]] — LLM 기반 과학적 지능에 대한 종합적 조사가 ResearchBench 벤치마크 설계의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 과학적 발견을 위한 LLM 벤치마킹에서 AIRS-Bench와 ResearchBench는 서로 다른 평가 방법론을 제시한다.
- 🔗 후속 연구: [[papers/417_HypoBench_Towards_Systematic_and_Principled_Benchmarking_for/review]] — 과학 발견의 전반적인 능력 평가를 위한 벤치마크 확장을 제공합니다.
- 🔄 다른 접근: [[papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/review]] — LLM의 과학적 발견 벤치마킹을 위한 다른 접근으로, 언어 에이전트 평가와 일반적인 LLM 평가를 비교
- 🔄 다른 접근: [[papers/277_Discoverybench_Towards_data-driven_discovery_with_large_lang/review]] — 데이터 기반 발견과 과학적 발견 벤치마킹이라는 서로 다른 관점에서 LLM의 연구 능력을 평가한다
