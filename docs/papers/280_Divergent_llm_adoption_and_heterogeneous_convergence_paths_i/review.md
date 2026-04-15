---
title: "280_Divergent_llm_adoption_and_heterogeneous_convergence_paths_i"
authors:
  - "Wu Zhu"
  - "Cong Lin"
date: "2025"
doi: "Not"
arxiv: ""
score: 4.7
essence: "ChatGPT 공개 이후 학술 논문 작성에서 LLM 활용이 급증하고 있으나, 그 실제 사용 패턴과 영향을 체계적으로 분석한 연구는 부재했다. 본 논문은 arXiv의 627,384개 논문을 분석하여 학문 분야, 성별, 모국어 여부, 경력 단계에 따른 이질적 LLM 채택 패턴과 이로 인한 학술 글쓰기 수렴 현상을 최초로 대규모로 규명한다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Academic_Writing_Assistance"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu and Lin_2025_Divergent llm adoption and heterogeneous convergence paths in research writing.pdf"
---

# Divergent LLM Adoption and Heterogeneous Convergence Paths in Research Writing

> **저자**: Wu Zhu, Cong Lin | **날짜**: 2025 (arXiv:2504.13629v1) | **DOI**: [Not provided](https://doi.org/)

---

## Essence

ChatGPT 공개 이후 학술 논문 작성에서 LLM 활용이 급증하고 있으나, 그 실제 사용 패턴과 영향을 체계적으로 분석한 연구는 부재했다. 본 논문은 arXiv의 627,384개 논문을 분석하여 학문 분야, 성별, 모국어 여부, 경력 단계에 따른 이질적 LLM 채택 패턴과 이로 인한 학술 글쓰기 수렴 현상을 최초로 대규모로 규명한다.

## Motivation

- **Known**: 
  - ChatGPT 등 LLM이 과학 연구에 미치는 영향은 긍정적(생산성 향상, 명확성 개선)과 부정적(할루시네이션, 윤리 문제)이 공존
  - 기존 연구는 주로 LLM이 생성한 텍스트 탐지(detection)에 집중

- **Gap**: 
  - 실제 연구자들이 어떻게 LLM을 사용하는지에 대한 체계적 분석 부족
  - 다양한 배경의 연구자 집단 간 이질적 채택 패턴 미파악
  - LLM 사용이 학술 글쓰기 스타일에 미치는 수렴 효과 미규명

- **Why**: 
  - LLM의 광범위한 채택이 학술 출판 생태계와 과학적 표현의 다양성에 미치는 장기적 영향 이해 필요
  - 연구자 집단별 채택 격차가 학술 출판 불평등을 심화시키거나 완화할 수 있음

- **Approach**: 
  - GPT-3.5로 명확성(clarity), 형식성(formality), 객관성, 가독성, 문법 등 5개 차원의 초록 수정본 생성
  - 2022년 11월 이전 논문을 인간 작성 텍스트 기준(ground truth)으로 설정
  - 48개 분야·프롬프트별 미세조정 모델 학습 → 96% 초과의 정확도로 GPT 수정 텍스트 식별
  - 차분-차분(difference-in-differences) 분석으로 글쓰기 수렴 효과 측정

## Achievement

1. **이질적 LLM 채택 패턴 규명**:
   - 컴퓨터과학: 22%, 전기공학: 21%, 금융: 18%, 통계: 15% → 수학: 3.5%
   - 주니어 연구자, 영어 비모국어자, 기관 접근성 낮은 연구자의 채택률 현저히 높음
   - 시간 경과에 따라 부분 수정(명확성/간결성)에서 포괄적 수정(27.7%)으로 진화

2. **LLM 수정의 글쓰기 품질 효과**:
   - 단어 수 25% 이상 감소로 간결성 극대화
   - 현재형 선호, 형용사/부사/수식어(hedge word) 최소화로 중립적·형식적 톤 강화
   - 선임 연구자의 구조화된 글쓰기 선호도와 높은 일치도

3. **글쓰기 스타일 수렴 현상 입증**:
   - ChatGPT 공개 후 LLM 채택자의 주니어-시니어 간 글쓰기 스타일 급격한 수렴
   - 남성 연구자, 비모국어 사용자의 수렴도 더 높음
   - 비채택자는 안정적 글쓰기 패턴 유지
   - 코사인 유사성(cosine similarity) 메트릭으로 정량화

## How

- **분류 프레임워크 구축**:
  - 제로샷 프롬핑으로 GPT-3.5가 인간 작성 초록을 5개 차원별로 수정
  - 인간-GPT 수정본 쌍 데이터셋으로 분야·프롬프트별 미세조정 모델 학습
  - 계층적 교차검증(stratified cross-validation)으로 과대적합 방지

- **글쓰기 품질 측정**:
  - 10개 핵심 글쓰기 원칙 정량화 (간결성, 명확성, 시제 선호도 등)
  - 기사 수준 고정효과(article-level fixed effects) 회귀모델로 인과효과 추정
  - 선택 편향(selection bias) 통제

- **수렴 분석**:
  - 원본 vs. GPT 수정본 초록의 코사인 유사성 계산
  - 경력 단계, 성별, 모국어 여부별 차분-차분 설계 적용
  - 2022년 11월 전후 시점 비교로 정책 변화(ChatGPT 공개)의 인과효과 식별

## Originality

- **최초성**: 
  - LLM 탐지 대신 '사용 방식'을 체계적으로 분석한 첫 대규모 연구
  - 67만 개 논문 규모의 포괄적 데이터셋으로 소규모 사례 연구·설문 한계 극복

- **방법론 혁신**:
  - 분야·프롬프트 특화 미세조정 모델 앙상블로 96% 초과 정확도 달성
  - 2022년 11월 이전 논문을 오염되지 않은 기준점으로 설정하는 영리한 식별 전략
  - 차분-차분 설계로 채택 여부 외생변수성(exogeneity) 확보

- **다차원 이질성 분석**:
  - 학문 분야, 성별, 언어 배경, 경력 단계 등 교차 분석
  - 시간 경과에 따른 사용 방식 진화 추적

## Limitation & Further Study

- **한계**:
  - 초록(abstract) 분석에 집중 → 본문(body text) 영향 미파악
  - 연구자의 의도적 LLM 사용 여부와 무의식적 스타일 영향 구분 불가
  - 비(非)arXiv 저널(Nature, Science 등)의 채택 패턴 불명확
  - 모델이 특정 유형의 수정(예: 극도로 정교한 인간 수정)은 위양성 가능성

- **후속 연구 방향**:
  - 본문 텍스트 분석으로 초록 이외 영역의 LLM 영향 조사
  - 논문 인용도, 다운로드 수 등과 글쓰기 수렴의 관계 분석
  - 글쓰기 다양성 감소가 과학적 혁신에 미치는 장기적 영향 평가
  - 비영어 논문, 폐쇄 학술지의 LLM 채택 패턴 조사
  - 후속 LLM 버전(GPT-4, Claude 등)의 탐지 및 영향 분석


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4.5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.7/5

**총평**: 본 논문은 ChatGPT 이후 학술 글쓰기 변화를 최초로 대규모로 계량 분석하여, LLM의 글쓰기 품질 개선과 스타일 동질화라는 이중 효과를 규명했다. 특히 경력·성별·언어 배경별 이질적 채택과 수렴을 보여주어, 기술 채택의 불평등이 반드시 심화되지 않을 수 있음을 시사한다. 다만 초록 한정 분석과 인과기제에 대한 심화 탐색이 후속 과제다.

## Related Papers

- 🔗 후속 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — LLM 사용이 학술 글쓰기 다양성에 미치는 영향을 실험적으로 검증한 연구의 대규모 실증 확장판이다.
- 🔄 다른 접근: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — AI 노출이 창의성과 다양성에 미치는 영향을 개별 vs 집단 차원에서 상호보완적으로 분석한다.
- 🏛 기반 연구: [[papers/478_Large_language_models_penetration_in_scholarly_writing_and_p/review]] — LLM이 학술 논문 작성에 미치는 광범위한 영향을 이해하기 위한 기초 분석을 제공한다.
- 🧪 응용 사례: [[papers/154_Best_Practices_for_Using_AI_When_Writing_Scientific_Manuscri/review]] — AI 논문 작성 도구의 영향을 실제 학술 환경에서의 수용과 수렴 패턴으로 분석
- 🔗 후속 연구: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — AI 에이전트 사용 패턴 분석이 LLM 채택 패턴 연구의 방법론적 확장을 제공한다.
- 🔄 다른 접근: [[papers/409_How_ai_ideas_affect_the_creativity_diversity_and_evolution_o/review]] — AI가 창의성과 다양성에 미치는 영향을 실험적 접근과 대규모 실증 분석으로 상호 검증한다.
- 🏛 기반 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — 언어모델 협력 글쓰기의 다양성 영향이 LLM 채택 패턴의 대규모 분석으로 확장 검증된다.
- 🔗 후속 연구: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — LLM 채택이 학술 저술에 미치는 영향을 더 광범위한 분야에서 분석한다
