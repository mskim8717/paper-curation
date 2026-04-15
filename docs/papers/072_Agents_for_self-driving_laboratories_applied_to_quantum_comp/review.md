---
title: "072_Agents_for_self-driving_laboratories_applied_to_quantum_comp"
authors:
  - "Shuxiang Cao"
  - "Zijian Zhang"
  - "Mohammed Alghadeer"
  - "Simone D Fasciati"
  - "Michèle Piscitelli"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "k-agents 프레임워크는 대규모 언어 모델 기반 에이전트를 활용하여 실험실 지식을 체계적으로 관리하고 자동화된 실험 수행을 가능하게 하며, 초전도 양자 프로세서 캘리브레이션에 성공적으로 적용되었다."
tags:
  - "cat/AI_Scientific_Research_Infrastructure"
  - "sub/Multi-Domain_Experimental_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cao et al._2024_Agents for self-driving laboratories applied to quantum computing.pdf"
---

# Agents for self-driving laboratories applied to quantum computing

> **저자**: Shuxiang Cao, Zijian Zhang, Mohammed Alghadeer, Simone D Fasciati, Michèle Piscitelli, Mustafa Bakr, Peter Leek, Alán Aspuru‐Guzik | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2412.07978](https://arxiv.org/abs/2412.07978)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: (a) Overview of the k-agents framework. Given a procedure in natural language, the execution agent first*

k-agents 프레임워크는 대규모 언어 모델 기반 에이전트를 활용하여 실험실 지식을 체계적으로 관리하고 자동화된 실험 수행을 가능하게 하며, 초전도 양자 프로세서 캘리브레이션에 성공적으로 적용되었다.

## Motivation

- **Known**: LLM 기반 에이전트는 텍스트와 이미지 처리 능력이 우수하며, 다중 에이전트 시스템을 통해 복잡한 작업 수행이 가능하다. 기존 자동화 방식은 전문가가 실험실 지식을 수동으로 코드로 번역해야 하는 한계가 있다.
- **Gap**: 전유 실험실 지식의 접근 불가성, 표준 RAG 방법의 이질적이고 다중모드 실험실 지식 적용의 어려움, 장시간 다단계 작업 자동화를 위한 확장 가능한 메모리 시스템 부재가 핵심 문제이다.
- **Why**: 자동화된 자체 구동 실험실은 반복 작업을 감소시켜 과학적 발견을 가속화할 수 있으며, 특히 양자 컴퓨팅 같은 복잡한 실험에서 인간 수준의 성능 달성이 중요하다.
- **Approach**: 실험실 지식을 캡슐화하는 knowledge agents를 설계하고, execution agent가 다단계 실험 절차를 agent 기반 state machine으로 분해하여 inspection agents의 결과 분석을 통해 상태 전이를 제어하는 폐루프 피드백 구조를 도입했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: (a) Translation agents. Translation agents are responsible for translating an incoming instruction into*

- **k-agents 프레임워크 개발**: 실험실 지식의 다중모드 특성을 처리하고 fine-tuning 없이 지식을 통합하는 확장 가능한 시스템 구축
- **Execution agent 설계**: 자연어 실험 절차를 agent 기반 state machine으로 자동 분해하고 단계별 실행 및 결과 분석을 통한 폐루프 제어 실현
- **양자 프로세서 자동 캘리브레이션**: 초전도 양자 프로세서의 단일 및 이중 큐비트 게이트 파라미터 자동 발견 및 entangled quantum state 생성 성공
- **번역 에이전트 성능**: 17개의 code translation agents로 표준 RAG 방법 대비 우수한 정확도 달성 (80개 지시문 테스트셋)

## How

![Figure 1](figures/fig1.webp)

*Figure 1: (a) Overview of the k-agents framework. Given a procedure in natural language, the execution agent first*

- Knowledge agents: 실험실 작업의 개별 실험부터 복잡한 절차까지 망라하는 지식 보유 및 결과 검사 능력 제공
- Translation agents: 벡터 유사도 기반 선택적 활성화를 통해 들어오는 지시문을 executable code로 변환
- Execution agent: 절차 분해, 단계별 코드 생성, 결과 분석, state 전이 결정을 조율
- Visual inspection agents: 실험 결과 이미지를 텍스트 리포트로 변환하여 multimodal 정보 처리
- Agent-based state machine: 각 단계의 독립적 지시문 보유 및 transition rule 기반 상태 관리

## Originality

- 다중모드 실험실 지식의 체계적 통합을 위해 knowledge agents의 선택적 활성화 메커니즘 도입
- 자연어 절차를 명시적 state machine 구조로 자동 변환하여 장시간 다단계 작업의 context window 제약 극복
- Vector-based agent selection 방식으로 표준 RAG 대비 이질적 에이전트 간 협업 능력 향상
- 양자 컴퓨팅 영역에 LLM 기반 자동화 에이전트를 처음 성공적으로 적용

## Limitation & Further Study

- LLM의 hallucination 위험성 및 파라미터 설정 오류 가능성에 대한 견고성 검증 부재
- 지금까지 단일 실험실 환경과 특정 양자 프로세서 플랫폼에서만 검증됨
- 실험 절차 분해 및 state machine 설계의 수동 개입 필요도 존재
- 여러 실험실 환경과 학문 분야에 대한 일반화 가능성 검토 필요
- 에이전트 간 조율 오류 발생 시 자가 복구 메커니즘의 한계

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: k-agents는 multimodal 실험실 지식의 체계적 통합과 장시간 자동화 실험 수행을 위한 혁신적 프레임워크를 제시하며, 양자 컴퓨팅 분야에서 인간 수준의 성능 달성으로 자동 과학 발견의 실질적 가능성을 입증했다.

## Related Papers

- 🏛 기반 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 동일한 k-agents 프레임워크를 기반으로 하여 양자 컴퓨팅 실험 자동화의 기본 원리를 제공한다
- 🔗 후속 연구: [[papers/501_LLM-based_Multi-Agent_Copilot_for_Quantum_Sensor/review]] — 양자 컴퓨팅 실험 자동화를 다중 에이전트 협력 시스템으로 확장한 발전된 접근법이다
- 🔄 다른 접근: [[papers/533_Meta-designing_quantum_experiments_with_language_models/review]] — 양자 시스템에서 실험 설계와 메타 설계라는 서로 다른 차원의 접근법을 보여준다
- 🧪 응용 사례: [[papers/744_Self-Driving_Laboratories_for_Chemistry_and_Materials_Scienc/review]] — 양자 컴퓨팅 분야의 자율 실험실 구현 사례를 통해 SDL의 실제 적용 가능성과 한계를 구체적으로 확인할 수 있다.
- 🔗 후속 연구: [[papers/133_Automating_quantum_computing_laboratory_experiments_with_an/review]] — 동일한 k-agents 프레임워크를 실험실 자동화에서 양자 컴퓨팅 실험이라는 특화 도메인으로 확장했다
- 🧪 응용 사례: [[papers/533_Meta-designing_quantum_experiments_with_language_models/review]] — 양자 컴퓨팅 실험실 자동화 연구에서 제시된 방법론을 메타 솔루션 발견이라는 더 추상적 수준으로 적용한다.
- 🧪 응용 사례: [[papers/501_LLM-based_Multi-Agent_Copilot_for_Quantum_Sensor/review]] — 양자 컴퓨팅 실험실 자동화 에이전트가 양자 센서 개발과 유사한 양자 시스템 제어 도메인을 다룬다
