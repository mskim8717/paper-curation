---
title: "551_MMC_Advancing_Multimodal_Chart_Understanding_with_Large-scal"
authors:
  - "Fuxiao Liu"
  - "Xiaoyang Wang"
  - "Wenlin Yao"
  - "Jianshu Chen"
  - "Kaiqiang Song"
date: "2024.04"
doi: "10.48550/arXiv.2311.10774"
arxiv: ""
score: 4.5
essence: "대규모 멀티모달 차트 명령어 튜닝(600k 인스턴스)을 통해 차트 이해에 특화된 LMM(대규모 멀티모달 모델)을 개발하고, 9가지 하위 작업으로 구성된 포괄적 벤치마크를 제시하는 연구이다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Scientific_Reasoning_Evaluation_Methods"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "sub/Cross-lingual_Language_Model_Pretraining"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2024_MMC Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning.pdf"
---

# MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning

> **저자**: Fuxiao Liu, Xiaoyang Wang, Wenlin Yao, Jianshu Chen, Kaiqiang Song, Sangwoo Cho, Yaser Yacoob, Dong Yu | **날짜**: 2024-04-15 | **DOI**: [10.48550/arXiv.2311.10774](https://doi.org/10.48550/arXiv.2311.10774)

---

## Essence

![Figure 1](figures/fig1.webp) *MMC의 9가지 구별되는 작업, 다양한 주제(비즈니스, 건강, 생물학 등), 다양한 차트 유형(막대, 히스토그램, 선형, 산점도, 히트맵 등)으로 구성된 인간 주석 데이터셋*

대규모 멀티모달 차트 명령어 튜닝(600k 인스턴스)을 통해 차트 이해에 특화된 LMM(대규모 멀티모달 모델)을 개발하고, 9가지 하위 작업으로 구성된 포괄적 벤치마크를 제시하는 연구이다.

## Motivation

- **Known**: LLM 기반의 LMM(LLaVA, MiniGPT-4 등)은 일반 이미지 이해에서 우수한 성능을 보임
- **Gap**: 차트 이미지는 추상적 요소(범례, 추세선, 축 레이블 등)를 포함하므로 자연장면(natural scene) 이미지와 본질적으로 다르며, 기존 LMM들은 차트 특화 도메인 학습 부족으로 차트 이해에서 성능 저하
- **Why**: 데이터 분석, 학술 연구, 비즈니스 인텔리전스 등 다양한 실제 응용 분야에서 정확한 차트 이해 능력이 필수적
- **Approach**: (1) 600k 규모의 대규모 차트 명령어 튜닝 데이터셋 구축, (2) 이를 기반으로 차트 특화 LMM 개발, (3) 9가지 작업 포함 포괄적 인간 주석 벤치마크 제안

## Achievement

![Figure 2](figures/fig2.webp) *MMCA의 전체 아키텍처*

1. **MMC-Instruction 데이터셋**: 기존 공개 데이터셋(FigureQA 180k, DVQA 300k, PlotQA 224k, ChartQA 21.9k)보다 규모(600k), 다양성(주제, 언어 스타일, 차트 유형), 품질이 우수. 자유형식(free-form) 질문과 개방형(open-ended) 답변으로 인간 인지와 일치

2. **MMCA 모델**: 기존 오픈소스 LMM들을 능가하는 최첨단 성능 달성. 기존 차트 QA 벤치마크에서 우수한 성능 입증

3. **MMC-Benchmark**: 차트 정보 추출, 차트 추론, 문맥적 이해, 다중 차트 이해, 차트 유형 분류, 차트 주제 분류, 차트-데이터테이블 변환, 차트-JSON 변환, 주식 차트 분석 등 9가지 작업 포함. GPT-4V를 포함한 최신 모델들도 상당한 도전에 직면, 특히 Chart-to-Datatable/JSON 작업에서 제한적 성능

## How

![Figure 3](figures/fig3.webp) *GPT-4V의 실패 사례(빨강)와 정정 답안(파랑) 비교*

- **Chart-Text Alignment Data (400k)**: 
  - arXiv 학술논문(2010-2020)에서 추출한 Scientific Chart-Caption 데이터(210k): LaTeX 소스와 이미지 파일 활용하여 고품질 유지
  - 기존 5개 공개 데이터셋(Statista, PlotQA, VisText, ChartInfo, Unichart)에서 190k 이미지-텍스트 쌍 필터링

- **Chart Instruction-Tuning Data (200k)**:
  - GPT-4를 활용하여 차트 설명 텍스트로부터 다양한 언어 스타일과 작업 유형의 질문-답변 쌍 자동 생성
  - 5가지 작업: (1) 차트 정보 추출(20단어 이하 답변), (2) 차트 추론, (3) 과학 차트 이해, (4) 차트-데이터테이블 변환, (5) 차트-JSON 변환
  - 명령어 튜닝 형식: "Human: {질문} AI: {답변}"

- **MMC-Benchmark 구축**:
  - 총 2,063개 이미지, 2,126개 질문(자유형식 851개 + 객관식 1,275개) 포함
  - 9가지 작업별로 Statista, arXiv, 웹 크롤, VisText, Google Bard 등 다양한 소스에서 이미지 수집
  - 모든 데이터에 인간 주석 적용
  - 두 가지 정량적 평가 방법: (1) GPT-4 기반 자유형식 평가, (2) 객관식 형식 평가

- **모델 아키텍션**:
  - 기존 LMM 아키텍처에 명령어 튜닝 적용
  - 통일된 지시 따름(instruction-following) 능력으로 다양한 차트 작업 수행

## Originality

- **최초 대규모 차트 특화 명령어 튜닝 데이터셋**: 기존 데이터셋 대비 3배 규모(600k)이며, 템플릿 기반이 아닌 GPT-4 기반 자유형식 생성으로 자연스러운 언어 다양성 확보
- **인간 인지 기반 포괄적 벤치마크**: 차트 이해를 9가지 세분화된 작업으로 평가하는 최초의 인간 주석 벤치마크 제안
- **GPT-4V 포함 광범위한 실증**: 최신 멀티모달 모델(GPT-4V)까지 포함한 실험으로 현재 기술의 한계를 명확히 입증
- **학술 차트 기반 데이터 활용**: LaTeX 소스 파일 기반의 과학 논문 차트 추출로 고품질 데이터셋 구축

## Limitation & Further Study

- **데이터 품질 문제**: GPT-4로 생성된 질문-답변 쌍에서 환각(hallucination) 가능성 존재. 저자들은 20단어 이하 제한을 두었지만 근본적 해결 부재
- **평가 방법의 제약**: 자유형식 답변의 경우 GPT-4 기반 평가에 의존하므로 평가 자체의 신뢰성 문제 가능
- **차트 유형 편향**: 실제 사용 분포와 벤치마크 분포의 불일치 가능성
- **후속 연구**: 
  - 다중 모달리티(시계열, 도메인 특화 정보) 통합 연구
  - 사용자 피드백 기반의 반복적 데이터 정제
  - 더 강력한 자동 평가 메트릭 개발
  - 실시간 차트 스트림 처리 능력 확대

## Evaluation

- **Novelty**: 4.5/5 - 차트 특화 대규모 데이터셋과 포괄적 벤치마크는 신규성이 높으나, 기술적 혁신(모델 아키텍처)보다는 데이터셋/벤치마크 기여에 중점
- **Technical Soundness**: 4/5 - 방법론이 명확하고 실험이 체계적이나, GPT-4 기반 데이터 생성에서 환각 문제 미해결
- **Significance**: 5/5 - 차트 이해는 실제 응용 가치가 높으며, 포괄적 벤치마크는 향후 연구의 기준점이 될 것
- **Clarity**: 4.5/5 - 데이터셋 구축과 실험이 명확하게 기술되었으나, 일부 세부 메서드(GPT-4 프롬프트 설계 등)는 부록 의존
- **Overall**: 4.5/5

**총평**: 본 논문은 차트 이해라는 중요한 하위 도메인에서 대규모 고품질 데이터셋과 포괄적 벤치마크를 제시함으로써 멀티모달 AI의 실제 응용 확대에 기여하는 의미 있는 작업이다. 기술적 혁신보다는 데이터셋/평가 자산의 가치가 높으며, GPT-4V 포함 광범위한 실증을 통해 현재 모델들의 한계를 명확히 드러낸 점이 강점이다.

## Related Papers

- 🔄 다른 접근: [[papers/198_ChartGemma_Visual_Instruction-tuning_for_Chart_Reasoning_in/review]] — 차트 이해를 위한 다른 접근법으로, 대규모 명령어 튜닝과 시각적 명령어 튜닝의 방법론적 차이를 비교할 수 있습니다.
- 🧪 응용 사례: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — 차트에서 코드 생성으로 확장한 연구로, 멀티모달 차트 이해를 실제 프로그래밍 작업에 적용한 발전된 사례입니다.
- 🔗 후속 연구: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — 과학 분야 멀티모달 벤치마크로, 차트 이해 능력을 과학적 그림과 데이터 해석까지 확장하여 평가합니다.
- 🏛 기반 연구: [[papers/315_Enhancing_chart-to-code_generation_in_multimodal_large_langu/review]] — MMC 데이터셋의 대규모 차트 이해 데이터는 차트-to-코드 생성 모델 훈련에 필요한 기초 자원을 제공한다
- 🔗 후속 연구: [[papers/566_Multimodal_deepresearcher_Generating_text-chart_interleaved/review]] — 멀티모달 차트 이해 데이터셋과 함께 활용하면 텍스트-차트 통합 보고서 생성의 성능을 더욱 향상시킬 수 있다.
- 🔗 후속 연구: [[papers/841_Tree-of-table_Unleashing_the_power_of_llms_for_enhanced_larg/review]] — 대규모 멀티모달 차트 데이터셋을 Tree-of-Table 방법론과 결합하면 복잡한 테이블-차트 관계 분석 성능을 크게 향상시킬 수 있다.
- 🔄 다른 접근: [[papers/198_ChartGemma_Visual_Instruction-tuning_for_Chart_Reasoning_in/review]] — 차트 이해를 위한 다른 접근법으로, 대규모 명령어 튜닝 데이터셋 구축 방식의 차이점을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/201_ChartLlama_A_Multimodal_LLM_for_Chart_Understanding_and_Gene/review]] — 차트 이해 모델 개발을 위한 대규모 멀티모달 데이터셋과 벤치마크 기반
- 🏛 기반 연구: [[papers/737_Sciverse_Unveiling_the_knowledge_comprehension_and_visual_re/review]] — 대규모 차트 이해 데이터셋을 통해 다중모달 과학 문제 해결의 시각적 추론 기반을 제공한다.
- 🏛 기반 연구: [[papers/204_Chartx__chartvlm_A_versatile_benchmark_and_foundation_model/review]] — 대규모 멀티모달 차트 이해 데이터셋으로, ChartX 벤치마크와 ChartVLM 모델 개발에 필요한 훈련 데이터의 기초를 제공한다
- 🔄 다른 접근: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — ChartAssistant의 범용 차트 이해와 MMC의 대규모 차트 데이터셋 기반 접근법이 차트 AI의 서로 다른 발전 방향을 제시한다.
- 🏛 기반 연구: [[papers/709_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges/review]] — 대규모 멀티모달 차트 이해의 기초적인 방법론을 과학 도형 캡션 생성에 적용한다.
- 🔄 다른 접근: [[papers/783_Synchart_Synthesizing_charts_from_language_models/review]] — 차트 생성과 이해라는 동일한 문제를 LLM 기반 합성 vs 대규모 멀티모달 데이터셋으로 다르게 접근한다
- 🔗 후속 연구: [[papers/802_The_mighty_torr_A_benchmark_for_table_reasoning_and_robustne/review]] — MMC의 차트 이해 벤치마크를 표 데이터 추론과 견고성 평가로 확장하여 구조화된 데이터 이해의 다른 측면을 탐구한다.
- 🔄 다른 접근: [[papers/399_Helm_Highlighted_evidence_augmented_language_model_for_enhan/review]] — 대규모 차트 이해 데이터셋과 테이블 증거 강조 방법은 모두 구조화된 데이터의 핵심 정보 추출을 다른 방식으로 접근한다.
- 🔗 후속 연구: [[papers/657_Reading_and_Reasoning_over_Chart_Images_for_Evidence-based_A/review]] — 대규모 차트 이해 데이터셋을 활용하여 차트 기반 자동 팩트 체킹의 성능을 크게 향상시킬 수 있다.
