---
title: "107_Artificial_intelligence_tools_expand_scientists_impact_but_c"
authors:
  - "Qianyue Hao"
  - "Fengli Xu"
  - "Yong Li"
  - "James Evans"
date: "2026.01"
doi: "10.1038/s41586-025-09922-y"
arxiv: ""
score: 4.0
essence: "AI 도구 채택이 개별 과학자의 생산성과 영향력을 크게 증가시키지만, 집단 과학의 탐색 범위를 축소시키는 역설적 현상을 41.3백만 논문 데이터로 실증적으로 규명했다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/AI_Human_Science_Collaboration"
  - "cat/Academic_Publishing_Quality_Assurance"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hao et al._2026_Artificial intelligence tools expand scientists’ impact but contract science’s focus 1.pdf"
---

# Artificial intelligence tools expand scientists’ impact but contract science’s focus

> **저자**: Qianyue Hao, Fengli Xu, Yong Li, James Evans | **날짜**: 2026-01-29 | **DOI**: [10.1038/s41586-025-09922-y](https://doi.org/10.1038/s41586-025-09922-y)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Increasing prevalence of AI adoption in science. a, Increasing*

AI 도구 채택이 개별 과학자의 생산성과 영향력을 크게 증가시키지만, 집단 과학의 탐색 범위를 축소시키는 역설적 현상을 41.3백만 논문 데이터로 실증적으로 규명했다.

## Motivation

- **Known**: AI가 과학 발견을 가속화하고 있으며 개별 과학자의 생산성 향상에 기여하고 있다는 것이 알려져 있다. 그러나 AI 채택이 집단 과학 전체에 미치는 영향에 대한 대규모 실증 분석이 부족한 상태다.
- **Gap**: 개별 과학자의 AI 사용 효과와 집단 과학 수준에서의 영향 간의 관계, 특히 AI 채택이 과학적 초점을 어떻게 변화시키는지에 대한 대규모 정량적 분석이 결여되어 있다.
- **Why**: AI 과학에의 급속한 확산으로 개인적 이익과 집단적 과학 진보 간의 긴장 관계를 이해하는 것이 중요하며, 이는 과학 정책과 연구 방향 설정에 중요한 함의를 갖는다.
- **Approach**: OpenAlex 데이터베이스의 41.3백만 논문(1980-2025)을 대상으로 미세조정된 BERT 언어 모델을 이용해 AI 활용 논문을 식별하고(F1-score 0.875), 개별 과학자 경력과 집단 과학 초점의 변화를 분석했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | AI enlarges paper impact and enhances researcher careers.*

- **개별 과학자의 성과 증폭**: AI 활용 연구자는 비활용 연구자 대비 3.02배 많은 논문 발표, 4.84배 많은 인용, 1.37년 앞당긴 프로젝트 리더 진출
- **집단 과학의 초점 축소**: AI 채택으로 연구 주제의 집단 부피 4.63% 감소, 연구자 간 상호작용 22% 감소
- **방법론적 신뢰성**: 인간 전문가의 높은 합의도(Fleiss' κ = 0.964)와 모델의 높은 식별 정확도로 검증", '**시대별 일관성**: 머신러닝, 딥러닝, 생성형 AI 시대 전반에 걸쳐 개인 확대-집단 축소 패턴의 일관성 확인

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Increasing prevalence of AI adoption in science. a, Increasing*

- OpenAlex 데이터베이스에서 생물학, 화학, 지질학, 재료과학, 의학, 물리학 6개 분야의 41.3백만 논문 추출
- AI 마일스톤 기술 기반으로 머신러닝(ML), 딥러닝(DL), 생성형 AI(GAI) 세 시대로 시간 분할
- BERT 언어 모델의 2단계 미세조정: 제목 기반 모델과 초록 기반 모델 독립 학습 후 앙상블
- 인간 전문가 팀의 샘플링 검증으로 모델 정확도 평가(Fleiss' κ, F1-score)", 'Knowledge extent(벡터 공간상 경로의 직경) 지표로 집단 과학 초점 측정
- 논문-인용 네트워크 분석으로 후속 참여도(follow-on engagement) 정량화

## Originality

- 41.3백만 논문을 아우르는 대규모 종단 분석으로 개인-집단 수준의 상충하는 AI 영향을 동시에 규명한 혁신
- 미세조정된 BERT를 활용한 자동화된 AI 논문 식별 방법으로 수십만 개 논문의 수작업 검증이 대규모 분석에 적용될 수 있음을 시연
- Knowledge extent와 follow-on engagement 지표를 통해 '과학의 범위 축소' 현상을 정량화한 새로운 관점", '생성형 AI 시대의 초기 데이터를 포함해 AI 발전의 세 시대를 포괄적으로 비교 분석

## Limitation & Further Study

- 생성형 AI(GAI) 시대의 데이터가 현재까지 제한적으로, 장기적 패턴이 확립되지 않았으므로 예비적 분석 수준
- 컴퓨터과학과 수학 등 AI 방법론을 직접 개발하는 학문은 제외되어 AI 생태계의 완전한 이해에 제약
- 인과 관계 규명 부족: AI 채택이 초점 축소를 야기하는지, 아니면 축소된 분야에서 AI 채택이 증가하는지의 방향성 규명 필요
- 학제 간 편차: 데이터 풍부한 분야와 그렇지 않은 분야 간 AI 채택 패턴의 차이 심화 가능성에 대한 심층 분석 부재
- 후속 연구 방향: (1) 인과 추론 모델을 통한 메커니즘 규명, (2) 생성형 AI 영향에 대한 장기 추적, (3) 주변화되는 연구 주제에 대한 정성적 분석

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 AI 과학 활용의 개인-집단 수준 영향의 역설을 대규모 실증 데이터로 처음 규명하여 과학 정책의 중요한 함의를 제시하며, 방법론적으로도 자동화된 대규모 분석의 신뢰성을 입증한 고도로 창의적이고 중요한 연구다.

## Related Papers

- ⚖️ 반론/비판: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — AI 도구가 과학자의 탐색 범위를 축소시킨다는 발견과 LLM이 더 참신한 연구 아이디어를 생성한다는 결과가 대조적인 관점을 제시한다.
- 🔗 후속 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — AI 도구 채택의 집단적 영향 분석을 개별 아이디어의 혁신성 평가로 확장하여 더 세밀한 분석을 가능하게 한다.
- 🏛 기반 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI 과학자 시스템의 자동화된 과학 발견이 과학자들의 AI 도구 채택 패턴에 미치는 영향을 이해하는 기반을 제공한다.
- ⚖️ 반론/비판: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — LLM이 인간보다 참신한 연구 아이디어를 생성한다는 발견이 AI 도구가 탐색 범위를 축소시킨다는 결과와 상반된 관점을 제시한다.
- 🏛 기반 연구: [[papers/313_Enabling_ai_scientists_to_recognize_innovation_A_domain-agno/review]] — AI 도구가 과학자 집단의 탐색 범위에 미치는 영향 분석이 개별 아이디어의 혁신성 자동 평가 시스템 개발의 기반을 제공한다.
