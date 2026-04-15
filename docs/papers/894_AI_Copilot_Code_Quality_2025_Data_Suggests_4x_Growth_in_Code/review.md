---
title: "894_AI_Copilot_Code_Quality_2025_Data_Suggests_4x_Growth_in_Code"
authors:
  - "Hongjing Shao"
  - "Qian Luo"
  - "Jiayi Xia"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "2024년 211백만 줄의 코드 변경 분석을 통해 AI Copilot 도입이 단기 생산성은 증대하지만 코드 복제(code clones)가 4배 증가하며 장기 유지보수성을 악화시키고 있음을 실증적으로 입증했다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Reinforcement_Learning_Control_Systems"
  - "sub/Cross-lingual_Language_Model_Pretraining"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shao et al._AI Copilot Code Quality 2025 Data Suggests 4x Growth in Code Clones - GitClear.pdf"
---

# AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones - GitClear

> **저자**: Hongjing Shao, Qian Luo, Jiayi Xia | **날짜**:  | **URL**: [https://www.gitclear.com/ai_assistant_code_quality_2025_research](https://www.gitclear.com/ai_assistant_code_quality_2025_research)

---

## Essence


2024년 211백만 줄의 코드 변경 분석을 통해 AI Copilot 도입이 단기 생산성은 증대하지만 코드 복제(code clones)가 4배 증가하며 장기 유지보수성을 악화시키고 있음을 실증적으로 입증했다.

## Motivation

- **Known**: AI 코드 어시스턴트 도입으로 개발 생산성이 증가하고 있으며, Stack Overflow 2024 조사에서 63%의 전문 개발자가 AI를 사용하고 있다. 그러나 코드 품질 메트릭스의 장기적 영향에 대한 체계적 분석이 부족했다.
- **Gap**: AI 생성 코드가 단기 생산성 증대와 장기 유지보수성 악화 간의 트레이드오프를 정량적으로 평가하는 대규모 종단 연구가 필요했다. 특히 코드 복제와 리팩토링 감소 패턴에 대한 실증적 데이터가 부족했다.
- **Why**: 개발팀의 장기적 생산성 유지를 위해서는 DRY 원칙과 모듈화가 필수적이므로, AI 도입이 코드 품질에 미치는 실제 영향을 정량화하고 대응책을 모색해야 한다.
- **Approach**: 2020-2024년간 211백만 줄의 코드 변경 데이터를 GitClear의 구조화된 데이터베이스에서 추출하여, Added, Deleted, Updated, Moved, Copy/pasted, Find/replaced, Churn 등 7가지 코드 품질 메트릭스를 연도별로 분석했다.

## Achievement


- **Copy/Paste 빈도 초과**: 2024년이 역사상 처음으로 Copy/Pasted 라인이 Moved 라인을 초과했으며, Moved 라인은 2020년 24.1%에서 2024년 9.5%로 60% 감소했다.
- **코드 복제 급증**: 5줄 이상 중복된 코드 블록의 빈도가 2024년 8배 증가하여, AI 도입과 강한 상관관계를 보였다.
- **예측 정확성**: 2024년 Google DORA 벤치마크가 AI 도입 증가에 따른 결함률 상승을 입증하여 연구진의 예측을 검증했다.
- **신규 코드 증가**: 새로 추가되는 코드 비율이 39.2%에서 46.2%로 증가하면서 코드 리팩토링 대비 신규 작성이 우세하게 되었다.
- **Churn 상승**: 코드 변동성(Churn)이 3.1%에서 5.7%로 상승하여 코드 안정성 저하를 시사했다.

## How


- GitClear의 대규모 구조화된 코드 변경 데이터베이스(211m lines)를 이용해 연도별 코드 작업 빈도 추적
- 7가지 코드 변경 유형(Added, Deleted, Updated, Moved, Copy/pasted, Find/replaced, Churn)의 상대적 비율을 2020-2024년 추이로 분석
- Type 1, 2, 3 코드 클론 분류 체계를 적용하여 중복 코드 블록 검출(A5 참고)
- Google DORA 2024 벤치마크와 교차 검증을 통해 AI 도입률과 결함률 간의 상관관계 확인
- 2024년 예측값과 실제값 비교를 통해 변화의 크기와 방향성 검증

## Originality

- 211백만 줄이라는 산업 최대 규모의 구조화된 코드 변경 데이터를 5년간 종단 분석한 최초 연구
- Copy/Pasted 라인이 Moved 라인을 초과한 첫 번째 연도 기록 — 코드 리팩토링 문화의 전환점을 실증적으로 포착
- AI 도입 시점(2022-2023)과 코드 품질 지표 악화 타이밍의 정확한 상관관계 규명
- 개발 생산성 메트릭(커밋 수, 라인 추가)과 장기 유지보수성 비용 간의 불일치를 정량화하여 경영 의사결정 문제로 제시

## Limitation & Further Study

- 분석 대상이 GitClear 플랫폼을 사용하는 개발팀으로 제한되어 샘플 편향 가능성 존재
- 코드 품질 저하의 원인이 AI 도입인지 다른 조직적 변화(원격근무 증가, 개발 속도 강조 등)인지 인과관계 확실하지 않음
- Type 1, 2, 3 코드 클론 분류의 자동화 정확도 및 context window 크기의 영향 정량화 부족
- 향후 연구로 AI 모델 버전별(GPT-3.5, GPT-4, Claude 등) 코드 품질 차이 비교 필요
- 정성적 코드 리뷰 데이터와 결함 발생률 추적을 통한 장기 추적 연구 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: AI 코드 어시스턴트의 생산성 향상과 코드 품질 악화 간의 트레이드오프를 대규모 실증 데이터로 명확히 입증한 산업 보고서로, 개발팀과 조직 리더십이 AI 도입 전략을 수립할 때 참고할 중요한 근거를 제시한다. 다만 인과관계 규명과 모델별 차이 분석은 향후 연구 과제로 남아있다.