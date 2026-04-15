---
title: "889_Xtragpt_Llms_for_human-ai_collaboration_on_controllable_acad"
authors:
  - "Nuo Chen"
  - "Andre Huikai Lin"
  - "Jiaying Wu"
  - "Junyi Hou"
  - "Zining Zhang"
date: "2025"
doi: "arXiv:2505.11336"
arxiv: ""
score: 4.0
essence: "본 논문은 맥락 인식(context-aware)과 제어 가능한(controllable) 학술 논문 수정을 위한 인간-AI 협업 프레임워크를 제안하며, 이를 구현한 XtraGPT 모델군(1.5B~14B)을 소개한다. 140,000개의 지도 학습 쌍으로 구성된 ReviseQA 데이터셋을 구축하여 섹션 단위의 정교한 학술 논문 수정을 지원한다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/Scientific_Research_Capability_Evaluation"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/Academic_Writing_Assistance"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/CHANGKUI_2025_Xtragpt Llms for human-ai collaboration on controllable academic paper revision.pdf"
---

# XtraGPT: Llms for human-ai collaboration on controllable academic paper revision

> **저자**: Nuo Chen, Andre Huikai Lin, Jiaying Wu, Junyi Hou, Zining Zhang, Qian Wang, Xidong Wang, Bingsheng He | **날짜**: 2025 | **DOI**: [arXiv:2505.11336](https://arxiv.org/abs/2505.11336)

---

## Essence

![Figure 1](figures/fig1.webp) *학술 논문 수정 워크플로우 비교 (좌) 및 proprietary LLM의 부족한 수정 예시 (우)*

본 논문은 맥락 인식(context-aware)과 제어 가능한(controllable) 학술 논문 수정을 위한 인간-AI 협업 프레임워크를 제안하며, 이를 구현한 XtraGPT 모델군(1.5B~14B)을 소개한다. 140,000개의 지도 학습 쌍으로 구성된 ReviseQA 데이터셋을 구축하여 섹션 단위의 정교한 학술 논문 수정을 지원한다.

## Motivation

- **Known**: 
  - 대규모 언어 모델(LLM)이 학술 워크플로우에 점점 더 많이 채택되고 있음
  - GPT-4o 같은 proprietray 모델을 통한 논문 수정이 일반적으로 사용됨

- **Gap**: 
  - 기존 LLM 기반 시스템은 표면 수준의 문법 교정에만 효과적
  - 개념적 일관성(conceptual coherence), 학술적 엄격성(academic rigor) 같은 심화된 요구를 충족하지 못함
  - 학술 작문의 반복적(iterative) 특성을 지원하는 메커니즘 부재
  - 사용자 지시(user instruction)와 작문 기준(writing criteria)에 대한 제어성(controllability) 부족

- **Why**: 
  - 학술 논문 수정은 일회성 생성이 아닌 다중 라운드의 맥락 민감한(context-sensitive) 과정
  - 상위 학회(ICLR 등)의 검수자 가이드라인 같은 체계적 기준이 존재하나 활용되지 않음
  - 일반 목적의 LLM은 학술 작문의 구조와 수사적 전략을 명시적으로 모델링하지 못함

- **Approach**: 
  - 20개의 섹션 단위 작문 기준(writing criteria)을 정의
  - 7,000개 학술지 논문으로부터 140,000개의 지도(instruction-revision) 쌍 수집
  - 제어 지향 사후 훈련(post-training)을 통해 맥락 인식과 지시 추종 능력 강화
  - 맥락(T), 문단(p), 지시(q)를 모두 입력으로 하는 모델 설계

## Achievement

![Figure 2](figures/fig2.webp) *사후 훈련 파이프라인 개요 - 제어 가능한 섹션 단위 정교한 논문 수정 가능*

1. **데이터셋 구축**: ReviseQA - 상위 학회 7,000개 논문에서 추출한 140,000개 고품질 지도-수정 쌍
   - 20개 섹션 단위 작문 기준에 따라 체계적으로 주석 처리
   - 경험 많은 AI 연구자들의 전문 수정을 통해 현실성 확보

2. **모델 성능**: XtraGPT 모델군(1.5B~14B)
   - 동일 규모 베이스라인 대비 현저히 우수한 성능
   - 7B 모델: GPT-4o-mini 수준 달성
   - 14B 모델: GPT-4o-mini 초과 성능
   - LLM-as-a-Judge 자동 평가에서 원본 초안 대비 지속적으로 선호됨

3. **인간 평가 검증**: 
   - 사용자가 채택하려는 의도를 가진 의도-정렬(intent-aligned) 개선 생성
   - 논문 품질 점수 증가: 6.08 → 6.73 (p<0.001, Δ=0.65±0.15)
   - 제어성 구현: 사용자 지시에 따른 동적 수정 가능

## How

![Figure 2](figures/fig2.webp) *제안된 프레임워크의 주요 설계 원칙과 기술적 구현*

**문제 정의 (Problem Formulation)**:
- 입력: 전체 논문 초안 T, 수정 대상 문단 p, 사용자 지시 q
- 출력: 지시를 만족하면서 전역 맥락과 일관성 유지하는 수정 문단 p̂
- 모델 매핑: p̂ = Model_θ(p, q, T)

**핵심 설계 원칙**:

1. **기준 지향 의도 정렬 (Criteria-Guided Intent Alignment)**
   - 저자 지시를 "명확화 강화", "기여도 강화" 같은 학술 작문 기준으로 구조화
   - 20개 섹션별 기준으로 고수준 지시를 실행 가능한 구체적 수정으로 전환
   - 훈련 데이터의 지시-수정 쌍을 기준에 명시적으로 링크

2. **맥락 인식 모델링 (Context-Aware Modeling)**
   - 전체 논문 맥락 T를 훈련 및 추론 시 명시적 입력으로 포함
   - 문단의 기능(motivation vs. analysis)을 문서 구조 내에서 파악
   - 전역 서술, 용어, 논리 구조에 조건화된 표현 학습 강제

3. **인간-AI 협업 철학 (Human-AI Collaboration)**
   - LLM을 완전 자동화 도구가 아닌 저자 능력 증강 조수로 위치
   - 인간: 지적 핵심(아이디어, 주장, 초안 작성)
   - AI: 지시 기반 정교한 맥락 인식 개선 제공
   - 저자 제어권 보존으로 독창성 훼손 방지

**훈련 전략**:
- 사후 훈련(post-training)을 통해 문맥 내 학습(ICL) 강화
- 장이상 제어 LLM-as-a-Judge로 제어성과 효과성 평가 프레임워크 제공
- 반복적 수정 사이클에서 이전 수정 기록 유지 및 추적 가능

**평가 방법**:
- 자동 평가: 길이 제어된 승률(length-controlled win rate)
- 인간 평가: 채택 의도, 논문 품질 점수 변화, 전체 평점 예측

## Originality

- **학술 논문 수정의 체계적 정의**: 기존 연구(완전 생성, 아이디어 생성, 검수 보조)와 달리 구조화된 반복적 수정 프로세스에 중점
  
- **기준 기반 지시 정렬**: 학회 가이드라인과 검수자 기준을 명시적으로 모델 훈련에 통합하는 혁신적 접근
  
- **맥락 조건화의 강조**: 전체 논문 맥락을 입력으로 명시하는 설계로 일관성 있는 수정 가능
  
- **대규모 전문가 주석 데이터셋**: 상위 학회 7,000개 논문 × 20개 기준 = 140,000개 쌍의 체계적 구성
  
- **제어 가능성의 형식화**: "in-context following, 사용자 지시, 기준 준수"의 3가지 제어 차원을 명시적으로 정의

## Limitation & Further Study

- **데이터셋 언어 제약**: ReviseQA가 주로 영문 학술지 기반이므로 타 언어 일반화 가능성 미검증
  
- **모델 규모**: 최대 14B 매개변수로 GPT-4o 같은 초대형 모델과의 근본적 격차 존재
  
- **기준의 보편성**: 20개 기준이 주로 NLP/ML 학회 중심이므로 타 분야(의학, 화학 등) 특수성 미반영
  
- **윤리적 고려**: 논문 생성 윤리 문제(Appendix 6에서 언급)에 대한 깊이 있는 논의 부재
  
- **실제 사용 접근성**: 모델 평가에서 기술 실무자 중심이므로 비기술 학자의 사용성 검증 필요
  
- **후속 연구 방향**:
  - 다언어 학술 논문으로의 확장
  - 실시간 협업 인터페이스 개발 (코드 에디터 모듈화 원칙 적용)
  - 학제 간(interdisciplinary) 기준 확대
  - 장기 수정 사이클에서의 저자 만족도 추적 연구

## Evaluation

- **Novelty**: 4.5/5
  - 학술 논문 수정을 체계적 반복 프로세스로 형식화한 점에서 높은 독창성
  - 기준 기반 지시 정렬은 창의적이나, 맥락 조건화는 관련 분야에서 알려진 기법

- **Technical Soundness**: 4/5
  - 문제 정의, 설계 원칙, 구현이 논리적으로 일관성 있음
  - 데이터셋 구축 방법론이 신중하고 전문가 주석의 신뢰성 보장
  - 평가 방법론이 종합적(자동+인간 평가, LLM-as-Judge)이나 통계 신뢰도 표기 부분적

- **Significance**: 4/5
  - 학술 커뮤니티에 실질적 가치: 반복적 논문 개선을 위한 실용적 도구 제공
  - 범용 LLM의 한계를 구체적으로 실증하고 개선안 제시
  - 공개 소스 모델 제공으로 재현성과 접근성 높음
  - 다만 기술적 한계(규모, 언어)로 인해 전면적 실무 대체는 아직 제한적

- **Clarity**: 4/5
  - 논문 구조가 명확하고 동기 설명이 구체적(Figure 1 예시 효과적)
  - HAC 철학과 기술적 구현 간의 연결이 잘 설명됨
  - 다만 ReviseQA 데이터셋 구축의 상세 프로토콜이 본문보다 Appendix에 과도하게 배치

- **Overall**: 4/5

**총평**: 본 논문은 학술 논문 수정을 인간-AI 협업의 관점에서 체계적으로 접근한 실용성 높은 연구이며, 기준 기반 지시 정렬과 맥락 인식 모델링이라는 명확한 설계 원칙 아래 140,000개 쌍의 전문가 주석 데이터셋과 XtraGPT 모델군을 제시했다. 자동/인간 평가에서 GPT-4o-mini 수준의 성능을 달성하고 실제 논문 품질 개선을 입증했으나, 모델 규모와 언어 다양성 면에서의 한계가 향후 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/595_Overleafcopilot_Empowering_academic_writing_in_overleaf_with/review]] — 학술 논문 작성을 위한 LLM 활용에서 다른 기술적 구현과 사용자 인터페이스를 제시한다
- 🏛 기반 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 개인화된 학술 글쓰기를 위한 사용자 맥락 활용의 기본 방법론을 제공한다
- 🔗 후속 연구: [[papers/228_CoAuthor_Designing_a_Human-AI_Collaborative_Writing_Dataset/review]] — 인간-AI 협업 글쓰기를 위한 더 정교한 제어 가능한 시스템으로 확장한다
- 🔄 다른 접근: [[papers/595_Overleafcopilot_Empowering_academic_writing_in_overleaf_with/review]] — 학술 논문 작성을 위한 LLM 통합에서 다른 기술적 접근법과 사용자 경험을 제시한다
- 🧪 응용 사례: [[papers/281_Dlpo_Towards_a_robust_efficient_and_generalizable_prompt_opt/review]] — 견고한 프롬프트 최적화가 인간-AI 협업에서 제어 가능한 학술 콘텐츠 생성에 활용될 수 있다.
- 🧪 응용 사례: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — 제어 가능한 학술 글쓰기를 위한 인간-AI 협업 시스템으로, 이 논문의 작문 피드백 생성을 실제 글쓰기 도구로 응용한 사례다
- 🔗 후속 연구: [[papers/775_Step-back_profiling_Distilling_user_history_for_personalized/review]] — 제어 가능한 학술 논문 수정을 위한 더 정교한 맥락 인식 기법을 활용한다
