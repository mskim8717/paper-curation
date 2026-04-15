---
title: "790_Teaching_Large_Language_Models_to_Self-Debug"
authors:
  - "Xinyun Chen"
  - "Maxwell Lin"
  - "Nathanael Schärli"
  - "Denny Zhou"
date: "2023"
doi: "10.48550/arXiv.2304.05128"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어 모델(LLM)이 몇 가지 시연(few-shot demonstration)을 통해 자신이 생성한 코드를 자동으로 디버깅하도록 가르치는 SELF-DEBUGGING 기법을 제시한다. 외부 피드백 없이 코드 설명과 실행 결과 분석을 통해 오류를 식별하는 \"러버덕 디버깅(rubber duck debugging)\" 방식의 자체 수정이 가능함을 보인다."
tags:
  - "cat/Scientific_Knowledge_Processing_Systems"
  - "cat/Autonomous_Scientific_Discovery_Agents"
  - "cat/Reinforcement_Learning_Control_Systems"
  - "sub/Self-Clarifying_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2023_Teaching Large Language Models to Self-Debug.pdf"
---

# Teaching Large Language Models to Self-Debug

> **저자**: Xinyun Chen, Maxwell Lin, Nathanael Schärli, Denny Zhou | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2304.05128](https://doi.org/10.48550/arXiv.2304.05128)

---

## Essence

![Figure 1](figures/fig1.webp)
*SELF-DEBUGGING의 반복적 디버깅 프로세스: 코드 생성(Step 1) → 코드 실행(Step 2) → 코드 설명(Step 3) → 피드백 생성 단계*

본 논문은 대규모 언어 모델(LLM)이 몇 가지 시연(few-shot demonstration)을 통해 자신이 생성한 코드를 자동으로 디버깅하도록 가르치는 SELF-DEBUGGING 기법을 제시한다. 외부 피드백 없이 코드 설명과 실행 결과 분석을 통해 오류를 식별하는 "러버덕 디버깅(rubber duck debugging)" 방식의 자체 수정이 가능함을 보인다.

## Motivation

- **Known**: 최근 LLM은 코드 생성에서 인상적인 성능을 달성했으나, 복잡한 프로그래밍 작업에서 단일 시도로 정확한 코드를 생성하기는 어렵다. 기존 연구들은 다중 샘플 생성 후 재순위화(reranking)하거나 별도의 코드 수정 모델을 학습하는 방식을 제안했다.

- **Gap**: 기존 코드 수정 접근법들은 추가 학습이 필요하거나, 단위 테스트나 인간의 명확한 피드백 없이는 LLM이 코드를 수정할 수 없다고 알려져 있었다. NLP 및 추론 분야에서 피드백 생성의 효과가 입증되었지만 코드 생성 분야에서는 미검증 상태였다.

- **Why**: 인간 프로그래머는 잘못된 코드를 완전히 버리지 않고, 실행 결과를 검토하며 자신의 설명을 통해 오류를 식별한다. 이러한 "러버덕 디버깅" 개념을 LLM에 적용하면 추가 학습 없이도 효과적인 자체 디버깅이 가능할 수 있다.

- **Approach**: Few-shot 프롬프팅을 통해 LLM에게 (1) 코드 생성 → (2) 코드 실행 → (3) 코드 설명 생성 → (4) 피드백 기반 수정 의 반복적 디버깅 프로세스를 학습시킨다. 단위 테스트가 없는 경우 순수 코드 설명으로, 있는 경우 실행 결과 피드백과 함께 설명을 활용한다.

## Achievement

![Figure 3](figures/fig3.webp)
*텍스트-SQL 생성을 위한 SELF-DEBUGGING 프롬프트 예시*

1. **다중 도메인 최고 성능 달성**: 
   - Spider(텍스트-SQL): 기준선 대비 2-3% 일관적 개선, 난이도 높은 쿼리에서 9% 개선
   - TransCoder(코드 번역): 단위 테스트 활용 시 최대 12% 정확도 향상
   - MBPP(텍스트-Python): 최대 12% 성능 개선

2. **샘플 효율성 개선**: 10배 이상 많은 후보 프로그램을 생성하는 기준선 모델과 동등하거나 우수한 성능 달성

3. **피드백 타입별 효과 검증**: 단위 테스트 피드백(UT) > 코드 설명 피드백(Expl) > 단순 피드백 순서로 성능 향상

4. **모델 일반성**: GPT 계열(code-davinci-002, gpt-3.5-turbo, gpt-4)과 오픈소스 모델(StarCoder) 모두에서 효과 입증

## How

![Figure 5](figures/fig5.webp)
*코드 번역을 위한 SELF-DEBUGGING 프롬프트 예시와 단위 테스트 피드백*

- **3단계 반복 프로세스**:
  1. **Generation (생성)**: 문제 설명 기반 코드 후보 생성
  2. **Explanation (설명)**: 생성된 코드를 자연어로 설명하거나 실행 추적(execution trace) 작성
  3. **Feedback (피드백)**: 코드 정확성에 대한 피드백 메시지 생성

- **다양한 피드백 유형**:
  - **Simple Feedback**: 단순 정/오 판정만 제공
  - **Unit Test Feedback (UT)**: 런타임 오류 및 실패한 테스트의 입출력 결과 포함
  - **Code Explanation Feedback (Expl)**: 러버덕 디버깅 방식의 코드 설명 (단위 테스트 불필요)
  - **Execution Trace Feedback (Trace)**: 코드의 라인별 실행 단계 설명

- **최대 디버깅 턴 종료 조건**: 피드백이 정확성을 확인하거나 최대 반복 횟수 도달 시 종료

- **코드 선택 전략**: 여러 샘플 중 실행 오류를 피하면서 가장 빈번한 실행 결과를 나타내는 코드 선택 후 디버깅 적용

## Originality

- **첫 외부 피드백 없는 자체 디버깅**: 단위 테스트나 인간 지침 없이 LLM의 자가 설명만으로 오류 식별이 가능함을 실증적으로 입증

- **러버덕 디버깅의 형식화**: 인간 프로그래밍 관행의 "러버덕 디버깅" 개념을 LLM 프롬프팅에 체계적으로 적용

- **추가 학습 불필요**: 기존 코드 수정 연구와 달리 사전학습된 모델에 few-shot 프롬프팅만으로 구현 가능

- **다양한 피드백 타입의 체계적 비교**: 단위 테스트, 코드 설명, 실행 추적 등 여러 피드백 형식의 효과를 정량적으로 분석

- **샘플 효율성 개선**: 동일한 모델에서 생성 횟수를 증가시키는 것보다 반복적 수정이 더 효율적임을 입증

## Limitation & Further Study

- **최대 반복 횟수 제한**: 디버깅 턴의 상한선이 설정되어 있어 매우 복잡한 버그는 수정하지 못할 가능성

- **LLM 자체 설명의 정확성 의존**: 러버덕 디버깅의 효과가 모델의 추론 및 설명 능력에 크게 좌우되며, 약한 모델에서는 효과 제한적

- **정적 분석 미활용**: 코드 실행 없이 수행할 수 있는 정적 분석 기법과의 결합 미탐색

- **에러 메시지 생성 능력**: 단위 테스트 없는 환경에서 모델이 스스로 생성한 오류 메시지의 정확성 및 유용성에 대한 심층 분석 부족

- **후속 연구**: (1) 더 복잡한 프로그래밍 작업에 대한 적용, (2) 다단계 추론이 필요한 버그에 대한 능력 향상, (3) 자동으로 유용한 피드백 생성 방법 개선


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 외부 피드백 없이 LLM의 자가 설명을 통한 코드 자체 수정을 체계적으로 입증하고, 다중 도메인에서 최고 성능을 달성한 의미 있는 연구이다. 추가 학습이 불필요하면서도 샘플 효율성을 개선한다는 점에서 실무 적용 가치가 높으나, 디버깅 기법의 일반화 한계와 모델 능력 의존성에 대한 더 심층적인 분석이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자기 개선이라는 공통 목표를 코드 디버깅 vs 일반적인 자기 개선으로 다르게 접근한다
- 🔗 후속 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — LLM의 자기 검증 능력을 코드 디버깅이라는 구체적 도메인으로 확장하여 적용한다
- 🧪 응용 사례: [[papers/263_Deepseek-coder_When_the_large_language_model_meets_programmi/review]] — 프로그래밍 도메인에서 LLM의 자기 디버깅 능력을 실제 코딩 작업에 적용한다
- 🧪 응용 사례: [[papers/482_Lean-star_Learning_to_interleave_thinking_and_proving/review]] — 대규모 언어모델의 자기 디버깅 학습 방법이 형식 증명에서 사고-증명 결합 학습에 실제 적용된다.
- 🔗 후속 연구: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 자기 디버깅 방법론을 일반적인 출력 개선으로 확장하여 외부 도구 없이 LLM만으로 성능 향상을 달성한다.
- 🔗 후속 연구: [[papers/227_Closing_the_loop_Learning_to_generate_writing_feedback_via_l/review]] — 대형언어모델의 자기 디버깅 학습 방법으로, 작문 피드백 생성에서 사용한 반복적 개선 접근법을 코드 개선 영역으로 확장한다
