---
title: "206_ChatGPT_outperforms_crowd_workers_for_text-annotation_tasks"
authors:
  - "Fabrizio Gilardi"
  - "Meysam Alizadeh"
  - "Maël Kubli"
date: "2023.07"
doi: "10.1073/pnas.2305016120"
arxiv: ""
score: 4.5
essence: "ChatGPT는 텍스트 주석 작업에서 크라우드 워커(crowd workers)를 평균 25 percentage point 초과하는 정확도로 능가하며, 훈련된 주석자 수준의 코더 간 합의도를 달성하면서도 MTurk 대비 약 30배 저렴한 비용으로 수행 가능함을 입증하는 연구이다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Cross-Modal_Data_Augmentation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gilardi et al._2023_ChatGPT outperforms crowd workers for text-annotation tasks.pdf"
---

# ChatGPT outperforms crowd workers for text-annotation tasks

> **저자**: Fabrizio Gilardi, Meysam Alizadeh, Maël Kubli | **날짜**: 2023-07-25 | **DOI**: [10.1073/pnas.2305016120](https://doi.org/10.1073/pnas.2305016120)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 네 가지 데이터셋에서 ChatGPT의 영점 샷(zero-shot) 텍스트 주석 성능 비교. ChatGPT의 정확도(accuracy)는 대부분의 작업에서 MTurk를 능가하며, 모든 작업에서 코더 간 합의도(intercoder agreement)가 MTurk와 훈련된 주석자를 초과함.*

ChatGPT는 텍스트 주석 작업에서 크라우드 워커(crowd workers)를 평균 25 percentage point 초과하는 정확도로 능가하며, 훈련된 주석자 수준의 코더 간 합의도를 달성하면서도 MTurk 대비 약 30배 저렴한 비용으로 수행 가능함을 입증하는 연구이다.

## Motivation

- **Known**: NLP 응용 프로그램에는 분류기 훈련이나 비감독 모델 성능 평가를 위해 고품질의 수동 텍스트 주석이 필수적임. 기존에는 훈련된 주석자(연구보조원) 또는 MTurk 크라우드 워커 두 가지 주석 방식이 주로 사용됨.

- **Gap**: 훈련된 주석자는 고품질이지만 비용이 높고, 크라우드 워커는 저렴하지만 품질이 낮으며(특히 복잡한 작업이나 영어 이외 언어의 경우), MTurk의 데이터 품질 저하 우려와 CrowdFlower 같은 대체 플랫폼의 폐쇄 문제가 발생함.

- **Why**: 대규모 언어 모델(Large Language Models, LLMs)의 출현이 새로운 가능성을 제시하는 시점에, ChatGPT가 기존 주석 방식을 대체할 수 있는지 체계적으로 평가할 필요가 있음.

- **Approach**: 6,183개의 트윗과 뉴스 기사로 구성된 4개 데이터셋을 활용하여 관련성(relevance), 입장(stance), 주제(topics), 프레임 감지(frame detection) 등 5가지 주석 작업에서 ChatGPT, MTurk 워커, 훈련된 주석자의 성능을 비교.

## Achievement

1. **정확도 우월성**: ChatGPT의 영점 샷 정확도는 4개 데이터셋 전반에서 MTurk를 평균 약 25 percentage point 초과. 관련성 작업(2개 클래스)의 경우 70-83% 정확도 달성(2023년 샘플 제외).

2. **코더 간 합의도 최고 성능**: ChatGPT(온도=0.2)는 평균 97% 합의도로, 훈련된 주석자(79%), MTurk(56%)를 모두 초과. 온도 파라미터 조정을 통해 일관성 향상 가능함을 입증.

3. **획기적 비용 절감**: 주석당 비용 $0.003(약 $0.003 이하)으로 MTurk 대비 약 30배 저렴하면서도 더 높은 품질 제공.

4. **일관된 성능**: 다양한 텍스트 유형(트윗, 뉴스 기사)과 시간 범위(2017-2023)에서 일관되게 우수한 성능 입증. ChatGPT 정확도와 훈련된 주석자의 코더 간 합의도 간 양의 상관(r=0.46)으로, 더 어려운 작업에서 더 큰 우월성 발휘.

## How

- **데이터셋 구성**: (1) 2020-2021 콘텐츠 중재 트윗 2,382개, (2) 2017-2022 미국 의회 트윗 1,856개, (3) 2020-2021 뉴스 기사 1,606개, (4) 2023년 1월 콘텐츠 중재 트윗 500개(339개 영문)

- **주석 작업**: 관련성(2진 분류), 주제 감지(6개 클래스), 입장 감지(3진 분류), 일반 프레임 감지(2개 클래스), 정책 프레임 감지(14개 클래스)

- **ChatGPT 설정**: 동일한 지시사항(codebook) 사용, 온도 파라미터 1.0과 0.2 두 가지 조건 실험, 각 조건당 2회 반복 수행하여 코더 간 합의도 계산

- **MTurk 워커 선정**: "MTurk Masters" 인증, 90% 이상의 승인률, 미국 거주자로 필터링하여 고품질 워커 확보

- **기준선 설정**: 훈련된 정치학 대학원생 3명이 일관된 지시사항으로 독립적으로 주석 수행, 이를 "gold standard"로 설정하여 정확도 평가

## Originality

- **처음으로 체계적 평가**: 기존 연구들이 ChatGPT의 주석 수행 가능성을 제시했으나, 본 연구는 6,183개 문서의 대규모 데이터셋과 다중 메트릭을 통한 첫 체계적 평가 제공.

- **다차원 성능 비교**: 정확도, 코더 간 합의도, 비용을 동시에 평가하여 실용적 가치 입증. 특히 기존 기준선(훈련된 주석자)과의 비교를 포함한 완전한 평가.

- **온도 파라미터 영향 분석**: ChatGPT의 온도 파라미터가 코더 간 합의도에 미치는 영향을 실증적으로 분석, 실무적 최적화 방안 제시.

- **혼동 요인 통제**: 2023년 새로운 샘플 추가로 모델 훈련 데이터에의 암기(memorization) 우려 해소.

## Limitation & Further Study

- **한계**: 
  - 영어 중심 평가(특히 2023년 샘플은 339개만 영문)로 다언어 성능 미검증
  - 온도=0.2에서 높은 합의도는 낮은 다양성을 의미할 수 있으므로 과도한 일관성이 품질 손실로 이어질 가능성
  - 2023년 샘플의 관련성 작업에서 성능 저하(59%)로 프롬프트 품질의 중요성 강조되었으나 최적화 미흡
  - 개인적 주석자의 특성(편향, 기술)을 모델이 완벽히 모방할 수 없음

- **후속 연구 방향**:
  - 다언어 환경에서의 성능 평가 필수
  - 소수 샷 학습(few-shot learning) 구현을 통한 추가 성능 향상 검토
  - 사람의 피드백을 활용한 반자동화 데이터 레이블링 시스템(semiautomated labeling systems) 구축
  - 체인 오브 싱크(chain of thought) 프롬프팅 등 고급 전략으로 영점 샷 추론 성능 증대
  - GPT-4, Claude 등 다양한 LLM 모델 간 비교 분석

## Evaluation

- **Novelty**: 4.5/5
  - 최초의 체계적 대규모 평가이고 다층적 메트릭을 활용했으나, ChatGPT 주석 가능성 자체는 이미 알려진 개념

- **Technical Soundness**: 4.5/5
  - 견고한 실험 설계(gold standard 기준선, 온도 파라미터 조건, 기억력 테스트)이지만 프롬프트 최적화 부족과 2023년 샘플의 불완전한 언어 표현

- **Significance**: 4.5/5
  - NLP 실무에 즉각적인 영향을 미칠 수 있는 획기적인 비용-성능 트레이드오프 제시이지만, 다언어/장기 신뢰성에 대한 검증 필요

- **Clarity**: 4.5/5
  - 명확한 구조와 효과적인 시각화이나, 프롬프트 전문(exact wording)이 부록에만 제시되어 재현성 제한

- **Overall**: 4.5/5

**총평**: 본 논문은 ChatGPT가 텍스트 주석 작업에서 크라우드 소싱을 실질적으로 대체 가능함을 최초로 체계적으로 입증한 중요한 실증 연구로, NLP 연구 커뮤니티의 실무 방식 전환을 촉발할 시사점이 있으나, 다언어 성능과 장기적 신뢰성에 대한 추가 검증이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/905_If_in_a_Crowdsourced_Data_Annotation_Pipeline_a_GPT-4__Proce/review]] — 크라우드소싱 데이터 주석에서 GPT-4의 성능을 더 자세히 분석하여, ChatGPT 연구의 후속 발전을 보여줍니다.
- ⚖️ 반론/비판: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — ChatGPT 사용자의 정확도 과신 문제를 지적하여, 텍스트 주석 작업에서의 높은 성능에 대한 균형잡힌 시각을 제공합니다.
- 🏛 기반 연구: [[papers/878_What_ChatGPT_and_generative_AI_mean_for_science/review]] — 생성 AI가 과학에 미치는 광범위한 영향을 논의하여, 텍스트 주석 작업의 맥락을 제공합니다.
- 🏛 기반 연구: [[papers/511_LLMs_Outperform_Outsourced_Human_Coders_on_Complex_Textual_A/review]] — 텍스트 어노테이션 작업에서 ChatGPT의 성능 연구가 LLM이 복잡한 언어 분석에서 인간을 능가할 수 있다는 증거의 기초
- 🔗 후속 연구: [[papers/905_If_in_a_Crowdsourced_Data_Annotation_Pipeline_a_GPT-4__Proce/review]] — 텍스트 주석 작업에서 크라우드소싱과 GPT 비교를 라벨 집계까지 포함하여 확장한다
- 🔗 후속 연구: [[papers/611_People_who_frequently_use_ChatGPT_for_writing_tasks_are_accu/review]] — 텍스트 주석 작업에서 ChatGPT의 우수성 연구를 AI 생성 텍스트 탐지라는 역방향 문제로 확장한다.
