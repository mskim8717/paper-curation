---
title: "1127_MMSD20_Towards_a_Reliable_Multi-modal_Sarcasm_Detection_Syst"
authors:
  - "Mayur Wankhade"
  - "Annavarapu Chandra Sekhara Rao"
  - "Chaitanya Kulkarni"
date: "2023"
doi: ""
arxiv: ""
score: 4.0
essence: "MMSD 벤치마크의 허위 신호(spurious cues)와 불합리한 주석을 제거한 MMSD2.0 데이터셋과 다중 관점 CLIP 프레임워크를 제안하여 신뢰할 수 있는 멀티모달 풍자 탐지 시스템 구축."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Cross-Modal_Data_Augmentation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wankhade et al._2023_MMSD2.0 Towards a Reliable Multi-modal Sarcasm Detection System.pdf"
---

# MMSD2.0: Towards a Reliable Multi-modal Sarcasm Detection System

> **저자**: Mayur Wankhade, Annavarapu Chandra Sekhara Rao, Chaitanya Kulkarni | **날짜**: 2023 | **URL**: [https://arxiv.org/abs/2307.07135](https://arxiv.org/abs/2307.07135)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: Overall process of construction MMSD2.0 dataset. Given the example in (a), Spurious Cues Removal*

MMSD 벤치마크의 허위 신호(spurious cues)와 불합리한 주석을 제거한 MMSD2.0 데이터셋과 다중 관점 CLIP 프레임워크를 제안하여 신뢰할 수 있는 멀티모달 풍자 탐지 시스템 구축.

## Motivation

- **Known**: 멀티모달 풍자 탐지는 텍스트와 이미지의 관계를 모델링하는 작업으로, 최근 그래프 기반 접근법이 좋은 성과를 보이고 있다. 기존 MMSD 벤치마크가 표준으로 사용되어 왔다.
- **Gap**: MMSD 벤치마크에 해시태그와 이모지 같은 허위 신호가 불균형하게 분포하고 있으며, 해시태그 없는 샘플을 무조건 부정 샘플로 처리하는 것이 부적절하다. RoBERTa 텍스트 모델이 멀티모달 최신 모델을 6.6% 능가하는 이상 현상이 발생.
- **Why**: 신뢰할 수 있는 멀티모달 풍자 탐지 시스템 개발을 위해서는 모델이 진정한 모달리티 간 관계를 학습해야 하며, 허위 신호에 의존하지 않아야 한다. 벤치마크의 품질은 후속 연구의 방향성을 결정하므로 중요하다.
- **Approach**: MMSD에서 해시태그와 이모지를 제거하여 허위 신호를 제거하고, 50% 이상의 부정 샘플을 크라우드소싱으로 재주석 처리. 사전학습된 CLIP 모델을 기반으로 텍스트, 이미지, 텍스트-이미지 상호작용 3가지 관점에서 멀티뷰 정보 추출.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: Overall process of construction MMSD2.0 dataset. Given the example in (a), Spurious Cues Removal*

- **MMSD2.0 데이터셋**: 허위 신호(해시태그, 이모지) 제거 및 50% 이상 샘플의 크라우드소싱 재주석으로 신뢰성 있는 벤치마크 구축
- **Multi-view CLIP 프레임워크**: 텍스트, 이미지, 텍스트-이미지 상호작용 관점에서 다중 단위 신호 활용으로 기존 최신 모델 능가
- **문제 지적**: MMSD의 허위 신호 문제를 최초로 지적하여 멀티모달 풍자 탐지 연구의 신뢰성 재검토 제안
- **효율성**: 복잡한 그래프 구조나 객체 탐지 전처리 불필요한 간단한 구조로 CLIP 지식 활용

## How


- 해시태그 제거: MMSD에서 해시태그 단어 수의 불균형(긍정 1.9개 vs 부정 0.55개)을 분석하여 모두 제거
- 이모지 제거: 80.7%의 이모지가 한 유형의 샘플에만 나타나는 불균형 분석 후 제거
- 샘플 선택: #sarcasm 해시태그 없는 모든 부정 샘플을 선택하여 재주석 대상으로 결정
- 크라우드소싱 재주석: 각 샘플에 대해 풍자/비풍자/판정불가 레이블 할당, 판정불가는 3명 전문가 재검토
- Multi-view CLIP: 사전학습된 CLIP에서 텍스트 뷰, 이미지 뷰, 상호작용 뷰의 정보 추출 후 집계

## Originality

- 벤치마크의 허위 신호 문제를 최초로 체계적으로 분석하고 지적
- 단순 해시태그 기반이 아닌 크라우드소싱을 통한 세밀한 재주석 방식 도입
- CLIP 기반 멀티뷰 프레임워크로 복잡한 그래프 구조 대신 간단하면서도 효과적인 접근법 제시
- 50% 이상 샘플 변경으로 기존 벤치마크의 신뢰성 문제에 직접 대응

## Limitation & Further Study

- 크라우드소싱 재주석의 일관성 평가(Cohen's kappa 등) 정보 부재", '판정불가 샘플의 최종 결정 과정에서의 불일치 해결 메커니즘 미상세
- 다른 언어의 멀티모달 풍자 데이터셋으로의 확장 가능성 논의 부족
- 멀티뷰 CLIP의 각 관점별 기여도 분석(ablation study) 결과 제시 필요
- 후속 연구: 다언어 멀티모달 풍자 데이터셋 구축, 모달리티별 기여도 분석 심화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 멀티모달 풍자 탐지 연구의 기초가 되는 벤치마크의 근본적인 문제를 최초로 지적하고 이를 체계적으로 개선한 MMSD2.0을 제시한 점이 매우 가치있다. 제안된 Multi-view CLIP은 간결하면서도 우수한 성능을 보여주며, 충분히 신뢰할 수 있는 벤치마크와 방법을 제공함으로써 향후 연구의 발전에 크게 기여할 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/092_Align_then_Fusion_Generalized_Large-scale_Multi-view_Cluster/review]] — 멀티모달 풍자 탐지의 허위 신호 제거와 멀티뷰 클러스터링의 앵커 정렬 모두 데이터의 잘못된 연결 문제를 해결한다.
- 🏛 기반 연구: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 멀티모달 언어모델의 차트-텍스트 정렬 기법이 풍자 탐지에서 텍스트-이미지 정렬 문제 해결의 기반을 제공한다.
- 🔗 후속 연구: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 차트 읽기에서의 다중 관점 분석을 멀티모달 풍자 탐지의 다양한 관점 통합으로 확장하여 적용할 수 있다.
- 🧪 응용 사례: [[papers/200_Chartist_Task-driven_Eye_Movement_Control_for_Chart_Reading/review]] — 작업 기반 시각적 주의 제어 메커니즘이 멀티모달 풍자 탐지에서 중요한 시각적 단서 식별에 직접 응용될 수 있다.
- 🏛 기반 연구: [[papers/196_ChartAssisstant_A_Universal_Chart_Multimodal_Language_Model/review]] — 차트 멀티모달 언어모델의 텍스트-시각 정렬 기법이 멀티모달 풍자 탐지에서 모달리티 간 정렬 문제 해결의 기반을 제공한다.
- 🔄 다른 접근: [[papers/092_Align_then_Fusion_Generalized_Large-scale_Multi-view_Cluster/review]] — 멀티뷰 데이터 처리에서 앵커 정렬과 멀티모달 풍자 탐지 모두 서로 다른 관점의 정보를 정확히 연결하는 문제를 다룬다.
