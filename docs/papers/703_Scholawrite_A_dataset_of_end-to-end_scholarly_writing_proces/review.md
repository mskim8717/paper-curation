---
title: "703_Scholawrite_A_dataset_of_end-to-end_scholarly_writing_proces"
authors:
  - "Linghe Wang"
  - "Minhwa Lee"
  - "R. Volkov"
  - "L. Chau"
  - "Dongyeop Kang"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "학술 논문 작성의 전체 과정을 키스트로크(keystroke) 로깅과 인지적 주석을 통해 추적한 첫 대규모 데이터셋으로, 초안부터 최종 원고까지 4개월에 걸친 61K개 텍스트 변경을 포함한다. 이를 통해 인간의 비선형적 저술 과정과 현재 대규모언어모델(LLM)의 능력 간 격차를 실증적으로 규명한다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Academic_Writing_Assistance"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Scholawrite A dataset of end-to-end scholarly writing process.pdf"
---

# Scholawrite: A dataset of end-to-end scholarly writing process

> **저자**: Linghe Wang, Minhwa Lee, R. Volkov, L. Chau, Dongyeop Kang | **날짜**: 2025 | **DOI**: N/A

---

## Essence

학술 논문 작성의 전체 과정을 키스트로크(keystroke) 로깅과 인지적 주석을 통해 추적한 첫 대규모 데이터셋으로, 초안부터 최종 원고까지 4개월에 걸친 61K개 텍스트 변경을 포함한다. 이를 통해 인간의 비선형적 저술 과정과 현재 대규모언어모델(LLM)의 능력 간 격차를 실증적으로 규명한다.

## Motivation

- **Known**: 기존 연구들은 완성된 논문의 버전 비교(revision logs)나 단기 저술 작업(30분 키스트로크 분석)에 집중해왔으며, LLM은 자동회귀(autoregressive) 방식으로 좌에서 우로만 텍스트를 생성한다.

- **Gap**: 실제 학술 저술은 계획-번역-검토의 비선형적 순환 과정이지만, 수개월에 걸친 시간적·인지적 역학관계가 장기 데이터셋에서 포착되지 않았다. 따라서 인간의 인지 과정과 진정으로 정렬된 저술 지원 도구를 개발하기 어렵다.

- **Why**: 과학자들의 실제 저술 방식을 이해해야만, 인간의 인지를 지원(대체 아님)하는 저술 보조 도구를 설계할 수 있다.

- **Approach**: Overleaf에서 작동하는 Chrome 확장 프로그램으로 자연스러운 환경에서 키스트로크를 수집하고, 15개 범주로 구성된 인지적 저술 의도 분류체계(taxonomy)를 개발하여 각 변경사항에 주석을 달아 종단 데이터셋을 구축한다.

## Achievement

![Figure 1](figure1_writing_process.png) 
*그림 1: 주석이 달린 저술 의도를 포함한 학술 저술 과정의 예시. 반복적이고 비선형적이며 긴 시간에 걸쳐 여러 활동, 도구, 의도 간 빈번한 전환*

1. **ScholaWrite 데이터셋**: 컴퓨터과학 대학원생 10명으로부터 수집한 5개 논문 전본(full manuscripts)에서 4개월간 61,885개 텍스트 변경을 추적. 각 키스트로크는 인지적 의도(생각 발상, 명확성 개선 등) 주석이 달려 있어 저술 인지 모델링에 최적화됨.

2. **재사용 가능한 저술 포착 도구 및 분류체계**: Overleaf용 Chrome 확장 프로그램이 프라이버시를 보호하면서 실시간 키스트로크를 기록하고, 15개 세부 의도 범주를 통해 학술 저술의 인지적 기제를 체계적으로 분석 가능하게 함.

3. **인간-LLM 간극의 실증적 통찰**: 저술의 57.4%는 텍스트 생산, 명확성·유창성 개선에 집중되며, 절반 이상의 세션에서 3개 이상의 복합 의도가 얽혀 있음을 발견. GPT-4, Qwen 등 현재 LLM은 표면 수준의 편집은 모방하나 다음 의도 예측이나 인지적으로 복잡한 수정을 지속하는 데 실패.

## How

![Figure 1 (Table 1)](table1_taxonomy.png)
*표 1: 세 가지 대범주(계획, 구현, 검토) 하에 15개 세부 의도 분류체계 (예: 생각 발상 7.0%, 텍스트 생산 57.4%, 유창성 개선 등)*

**데이터 수집 및 주석 파이프라인:**

- **Overleaf 키스트로크 로깅**: Chrome 확장이 key-up 이벤트마다 visible text를 캡처하고 Google의 diff_match_patch로 변경사항 추출, 타임스탐프·파일명·저자 ID 메타데이터 저장

- **참여자 모집**: 미국 R1 대학 컴퓨터과학 대학원생 10명, 2023년 11월~2024년 2월 4개월 추적, IRB 승인 확보, 자발적이고 자연스러운 환경에서 수집

- **인지 의도 주석**: 
  - 인터랙티브 인터페이스로 타임라인 내 키스트로크 탐색 및 의도 범위 식별
  - Flower & Hayes(1981)와 최근 개정 연구(Du et al., 2022b; Koo et al., 2023)를 기반으로 두 명 주석자가 귀납적 개방 코딩 진행
  - 인지 언어학자와 다회차 토의로 라벨 정의 정제
  - 1K 키스트로크 부분집합에서 가중 F1 점수 0.71 달성(강한 신뢰도 확인)

- **후처리**: 개인 식별 정보 제거, 비정보적 인공물(스크롤링 등) 필터링, 의도 스팬 분할로 분석 및 모델 학습 준비

## Originality

- **첫 월단위 종단 데이터셋**: 기존 연구는 버전 수준 비교 또는 30분 단기 세션에 국한했으나, 본 연구는 완성된 논문으로 이어지는 4개월 전체 주기를 실시간 키스트로크로 추적

- **Overleaf 전용 키스트로크 로거**: MS Word 등 폐쇄 생태계용 기존 도구(Inputlog 등)와 달리, LaTeX 기반 학술 저술의 표준 플랫폼인 Overleaf에서 안전하고 장기간 데이터 수집

- **세밀한 인지 주석 분류체계**: 선행 이론과 경험적 검증(inter-annotator agreement)을 결합한 15개 범주 분류체계로, 저술의 **미시적 의도**(idea generation 7.0% → text production 57.4% → revision 등)를 정량화

- **인간 인지 대 LLM 역량 분석**: 표면 수준 편집 능력 외에 **의도 예측**, **다중 의도 추적**, **인지 복잡성 유지** 측면에서 LLM의 근본적 한계를 처음 실증적으로 입증

## Limitation & Further Study

- **표본 크기 제약**: 단일 대학의 컴퓨터과학 대학원생 10명, 5개 논문만 포함되어 학문 분야, 경험 수준, 언어별 다양성 부재. 향후 다학제, 다국가, 다언어 확대 필요.

- **Overleaf 플랫폼 한정**: 다른 저술 도구(Google Docs, MS Word 등) 사용자는 포함 불가. 플랫폼 간 저술 인지 차이 검토 필요.

- **주석자 바이어스**: 두 명 주석자만 참여했고, 인지 의도 해석의 주관성 가능성. 다중 주석자 간 신뢰도 재검증 권장.

- **모델 평가 범위**: 현재 GPT-4, Qwen만 평가. Claude, Gemini 등 다양한 LLM 및 최신 버전(GPT-o1 등)에서의 성능 분석 필요.

- **후속 연구 방향**: 
  - 저술 의도 예측 모델 개발(next-intention forecasting)
  - 인지적으로 정렬된 저술 도구 설계 및 사용자 평가
  - 의도 기반 피드백 생성(intention-aware feedback)
  - 분야별·언어별 저술 인지 차이 비교 분석


## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.5/5

**총평**: 이 논문은 학술 저술의 인지 과정을 장기 추적하는 첫 대규모 데이터셋을 제시하여 "저술을 과학으로" 접근할 기초를 마련했으며, 인간 인지와 현재 LLM 간 근본적 차이를 실증적으로 입증함으로써 향후 인간-중심의 저술 보조 도구 개발에 명확한 방향을 제시한다. 다만 표본 다양성 제약과 모델 평가 범위 한정이 일반화 가능성을 저해할 수 있는 점이 아쉽다.

## Related Papers

- 🔗 후속 연구: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — 실제 학술 글쓰기 과정의 세밀한 분석과 LLM 협력 글쓰기 패턴 분석이 상호보완적 통찰을 제공한다.
- 🏛 기반 연구: [[papers/228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset/review]] — 인간-AI 협력 글쓰기 데이터셋 구축의 방법론적 기초를 제공한다.
- 🔄 다른 접근: [[papers/414_Human-llm_coevolution_Evidence_from_academic_writing/review]] — 학술 글쓰기에서 인간과 LLM의 상호작용을 서로 다른 관점에서 체계적으로 분석한다.
- 🔗 후속 연구: [[papers/641_Prototypical_human-ai_collaboration_behaviors_from_llm-assis/review]] — LLM 보조 글쓰기의 협력 패턴 분석이 전체 학술 글쓰기 과정 연구로 확장될 수 있다.
