---
title: "608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R"
authors:
  - "Cheng Tan"
  - "Dongxin Lyu"
  - "Siyuan Li"
  - "Zhangyang Gao"
  - "Jingxuan Wei"
date: "2024.06"
doi: "10.48550/arXiv.2406.05688"
arxiv: ""
score: 4.2
essence: "대규모언어모델(LLM)의 학술 논문 피어리뷰 과정을 단순한 정적 검토 생성에서 저자-검토자-의사결정자 간의 동적 다중턴 대화로 재정의하고, 92,017개의 검토문을 포함한 대규모 데이터셋(ReviewMT)을 구축했다."
tags:
  - "cat/Academic_Publishing_Quality_Assurance"
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "sub/AI-Enhanced_Peer_Review"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions.pdf"
---

# Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions

> **저자**: Cheng Tan, Dongxin Lyu, Siyuan Li, Zhangyang Gao, Jingxuan Wei, Siqi Ma, Zicheng Liu, Stan Z. Li | **날짜**: 2024-06-09 | **DOI**: [10.48550/arXiv.2406.05688](https://doi.org/10.48550/arXiv.2406.05688)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 기존 LLM 피어리뷰 접근법과 개선된 프레임워크 비교*

대규모언어모델(LLM)의 학술 논문 피어리뷰 과정을 단순한 정적 검토 생성에서 저자-검토자-의사결정자 간의 동적 다중턴 대화로 재정의하고, 92,017개의 검토문을 포함한 대규모 데이터셋(ReviewMT)을 구축했다.

## Motivation

- **Known**: LLM이 개별 논문에 대한 정적 검토문 생성에서 우수한 성능을 보임이 입증됨
- **Gap**: 기존 연구는 단일턴 검토 생성에만 초점을 맞추고, 실제 피어리뷰의 동적·반복적 특성(저자의 재반박, 검토자의 재검토, 의사결정 과정)을 포착하지 못함
- **Why**: 실제 학술 출판 시스템은 검토자-저자 간 상호작용과 최종 의사결정을 포함한 다단계 프로세스이며, 이를 정확히 시뮬레이션해야 LLM의 실용적 적용 가능성을 평가할 수 있음
- **Approach**: (1) 다중턴 대화 구조로 피어리뷰 과정 재정의, (2) ICLR과 Nature Communications에서 26,841개 논문의 92,017개 검토문 수집, (3) 각 역할별 평가 메트릭스 제시

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: ReviewMT 데이터셋 데이터 처리 파이프라인 개요*

1. **종합 데이터셋 구축**: 26,841개 논문, 92,017개 검토문으로 구성된 ReviewMT 데이터셋 공개. ICLR(2017-2024)과 Nature Communications(2023)의 이질적 검토 프로세스를 ReviewMT-ICLR, ReviewMT-NC 두 부분집합으로 분할하여 제공

2. **역할기반 다중턴 프레임워크**: 4단계 상호작용 구조 공식화
   - 1턴: 검토자 초기 검토(P → Ri)
   - 2턴: 저자 재반박(Ri → Ai)
   - 3턴: 검토자 최종 검토(Ai → R'i)
   - 4턴: 의사결정자 최종 판정({Ri, Ai, R'i} → D)

3. **평가 메트릭스 제시**: 각 역할의 성능 평가를 위한 다차원 지표 제안(응답의 유효성, 텍스트 품질, 점수 평가, 의사결정 평가)

## How

![Figure 3](figures/fig3.webp)
*그림 3: ReviewMT-ICLR 데이터셋의 ICLR 논문과 검토문 통계*

- **데이터 수집**: OpenReview API(ICLR), Requests 라이브러리를 통한 웹 크롤링(Nature Communications)으로 체계적 수집. Robots 프로토콜 준수
- **텍스트 처리**: PDF-to-text 변환 시 Marker 소프트웨어를 활용하여 마크다운 형식 유지로 구조적 충실성 확보
- **구조화**: JSON 형식으로 각 턴의 필드를 체계적으로 저장
  - 1턴: "Summary", "Strengths", "Weaknesses", "Questions"
  - 2턴: "Response"
  - 3턴: "Final comment", "Score"
  - 4턴: "Meta review", "Final decision"
- **적응적 처리**: 연도별·저널별 검토 프로세스 변화에 대응(예: 초기 평점 미제공 논문은 최종 평점만 사용)

![Figure 4](figures/fig4.webp)
*그림 4: ReviewMT 데이터셋의 키워드 워드클라우드*

## Originality

- **프레임워크 혁신**: 피어리뷰를 단순 텍스트 생성 과제에서 복합 역할기반 다중턴 대화로 재정의하는 개념적 전환
- **장문맥 대화 데이터셋**: 기존 명령어 튜닝 데이터셋(Dolly, Alpaca 등)이 단일턴 상호작용 중심인 반면, 실제 학술 환경의 다단계 상호작용을 충실히 반영
- **이질적 소스 통합**: ICLR(컨퍼런스)과 Nature Communications(저널)의 서로 다른 검토 프로세스를 체계적으로 통합하여 다양성 확보
- **역할별 평가체계**: 검토자, 저자, 의사결정자 각각의 역할에 맞춘 맞춤형 평가 메트릭스 고안

## Limitation & Further Study

- **데이터셋 규모의 한계**: 26,841개 논문은 충분하지만, 전체 학술 출판 영역의 대표성 측면에서 특정 분야(AI/ML 중심)에 편중
- **자동 검토 품질 검증 부재**: 현재까지 논문에서 LLM의 실제 검토 성능 평가 결과가 제시되지 않음. 향후 GPT-4, LLaMA 등 다양한 모델의 평가 필요
- **재반박-재검토 품질 편차**: Nature Communications의 경우 공식 재반박 구조가 ICLR과 다르므로, 데이터 정규화 과정에서 정보 손실 가능성
- **윤리적 고려사항 미흡**: 실제 피어리뷰 자동화 시 검토자의 역할 축소, 이해상충 탐지 능력 등에 대한 논의 부족
- **후속 연구 방향**: 
  - 소규모 언어모델(7B-13B 파라미터)의 파인튜닝 성능 비교
  - 검토 품질의 자동 평가 메트릭 개발(기존 BLEU/ROUGE 보다 의미론적 신뢰도 중시)
  - 거부 논문의 공통 문제점 분석을 통한 검토자 훈련 활용

## Evaluation

- **Novelty**: 4.5/5 - 피어리뷰의 다중턴 대화 재정의는 신선하나, 개별 컴포넌트(명령어 튜닝, 검토 생성)는 기존 연구 활용
- **Technical Soundness**: 4/5 - 데이터 수집·처리 방법론은 타당하나, 평가 메트릭스의 구체적 구현 상세 부족. 논문 초안 단계로 완전한 검증 데이터 미제시
- **Significance**: 4.5/5 - 학술 출판 시스템의 구조적 문제 해결에 기여 잠재력이 높고, 공개 데이터셋은 커뮤니티 자산으로 가치 높음. 다만 실제 도입 시 인간 검토자 역할 축소 우려
- **Clarity**: 4/5 - 프레임워크와 데이터셋 구성은 명확하나, 평가 메트릭스 정의와 실험 결과 섹션이 본문 범위에서 불완전
- **Overall**: 4.2/5

**총평**: 이 논문은 대규모언어모델의 학술 피어리뷰 적용을 현실적 다중턴 대화 구조로 혁신적으로 재설정하고, 이를 뒷받침하는 대규모 고품질 데이터셋을 공개함으로써 학술 AI 응용의 중요한 기초를 제공한다. 다만 LLM 성능 평가 결과의 부재와 자동 평가 메트릭스의 미성숙이 시급한 과제이며, 실제 학술 생태계에 미치는 영향에 대한 심층 논의가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — 다중턴 대화 기반 피어리뷰와 AI 생성 리뷰 평가 프레임워크가 상호 보완적인 리뷰 시스템을 구성한다.
- 🏛 기반 연구: [[papers/385_Glimpse_Pragmatically_informative_multi-document_summarizati/review]] — 다중 문서 요약 기법이 피어리뷰 프로세스에서 여러 검토자 의견의 통합적 분석을 위한 토대를 제공한다.
- 🔄 다른 접근: [[papers/677_Reviewer2_Optimizing_Review_Generation_Through_Prompt_Genera/review]] — 역할 기반 다중턴 대화와 프롬프트 최적화라는 서로 다른 AI 리뷰 생성 전략을 보여준다.
- 🧪 응용 사례: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 인간과 유사한 리뷰 생성에서 다중턴 대화 접근법의 실제 적용 사례를 제시한다.
- 🏛 기반 연구: [[papers/679_Revieweval_An_evaluation_framework_for_ai-generated_reviews/review]] — 다중턴 대화 기반 피어리뷰 시스템이 AI 생성 리뷰의 신뢰성 평가를 위한 데이터와 방법론을 제공한다.
- 🧪 응용 사례: [[papers/385_Glimpse_Pragmatically_informative_multi-document_summarizati/review]] — 차별적 다중 문서 요약 기법이 피어리뷰 프로세스에서 검토자 의견 분석에 실제 적용된다.
- 🔗 후속 연구: [[papers/452_L-citeeval_Do_longcontext_models_truly_leverage_context_for/review]] — 다중 턴 장문맥 대화로서의 동료 심사가 L-CiteEval의 평가 범위를 확장한다
- 🔄 다른 접근: [[papers/173_Bridging_social_psychology_and_llm_reasoning_Conflict-aware/review]] — 학술 심사에서 인지편향 완화 접근법과 다중턴 대화 기반 접근법은 서로 다른 관점에서 심사 품질 향상을 추구한다.
- 🔗 후속 연구: [[papers/883_When_reviewers_lock_horn_Finding_disagreement_in_scientific/review]] — 리뷰어 간 모순 탐지를 다중 턴 대화 형태의 피어 리뷰 시스템으로 발전시킨다
- 🔄 다른 접근: [[papers/184_Can_large_language_models_provide_useful_feedback_on_researc/review]] — 다중 턴 대화 형태의 동료 리뷰로 LLM 피드백의 다른 접근법을 보여준다.
- 🧪 응용 사례: [[papers/877_What_Can_Natural_Language_Processing_Do_for_Peer_Review/review]] — 동료 심사에서 NLP 활용을 다중 턴 대화와 장문맥 처리라는 구체적 방법으로 적용
- 🔄 다른 접근: [[papers/629_Pre_A_peer_review_based_large_language_model_evaluator/review]] — 둘 다 LLM을 활용한 동료 평가 시스템이지만, PRE는 다중 LLM 평가자 활용에, 다른 논문은 다중 턴 대화 구조에 집중한다
- 🏛 기반 연구: [[papers/654_Re_2_A_consistency-ensured_dataset_for_full-stage_peer_revie/review]] — 피어리뷰를 다중 턴 장기 맥락 대화로 보는 관점과 일관성 보장 피어리뷰 데이터셋은 상호 보완적인 리뷰 시스템 연구이다.
- 🔄 다른 접근: [[papers/664_RelevAI-Reviewer_A_Benchmark_on_AI_Reviewers_for_Survey_Pape/review]] — 다중 턴 대화 기반 피어 리뷰와 관련성 기반 분류가 각각 다른 리뷰 자동화 접근법이다
- 🔄 다른 접근: [[papers/070_Agentreview_Exploring_peer_review_dynamics_with_llm_agents/review]] — 보상 기반 다중 턴 대화로서 동료 검토를 모델링하는 다른 접근으로, 에이전트 시뮬레이션과 실제 검토 과정을 비교
- 🔗 후속 연구: [[papers/698_Scaling_Reproducibility_An_AI-Assisted_Workflow_for_Large-Sc/review]] — 멀티턴 동료심사 시스템이 대규모 재현성 분석의 품질 평가 메커니즘으로 활용될 수 있다.
- 🔄 다른 접근: [[papers/481_Lazyreview_a_dataset_for_uncovering_lazy_thinking_in_nlp_pee/review]] — 다중 턴 장문 맥락 대화로서의 동료 검토 연구로, 게으른 사고 탐지와 다른 관점에서 검토 과정을 분석
- 🔗 후속 연구: [[papers/843_Treereview_A_dynamic_tree_of_questions_framework_for_deep_an/review]] — 다중턴 대화 형태의 동료평가를 계층적 질문 트리 구조로 발전시켜 더 체계적이고 효율적인 평가 방법론을 제시한다.
- 🔗 후속 연구: [[papers/083_AI-Driven_Review_Systems_Evaluating_LLMs_in_Scalable_and_Bia/review]] — 편향 인식 리뷰 시스템이 다중 턴 대화 기반 피어 리뷰로 발전될 수 있다.
- 🔗 후속 연구: [[papers/778_Summarizing_multiple_documents_with_conversational_structure/review]] — 다중 턴 장문맥 대화로서의 동료 평가를 통해 메타리뷰 생성 과정을 더욱 정교하게 모델링할 수 있다.
- 🔄 다른 접근: [[papers/022_A_sentiment_consolidation_framework_for_meta-review_generati/review]] — 동료 평가에서의 감정 분석이라는 공통 관심사를 가지지만 메타리뷰 생성 vs 다중 턴 대화라는 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 다중턴 장문맥 대화로서의 피어 리뷰를 체크리스트 기반 메타리뷰로 체계화하여 더 구조적인 리뷰 종합을 제시한다.
- 🔗 후속 연구: [[papers/776_Streamlining_the_review_process_Ai-generated_annotations_in/review]] — 멀티턴 대화 기반 피어리뷰를 통해 AI 어노테이션의 상호작용성을 더욱 발전시킬 수 있다.
