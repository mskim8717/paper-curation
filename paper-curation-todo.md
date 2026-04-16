# paper-curation TODO — 실행 순서 기반

작성일: 2026-04-15 (재정렬: 착수 순서 기준)
배경: `run_update_force.py`의 플래그(`--local`, `--update`, `--update-force`, `--timeline`, `--category`)가 MECE하지 않아 Recipe A~H로 분기되고, ai4s에 139편 규모의 PDF↔review 오매칭이 존재.

**원칙**: 피해를 키우지 않는 순서 → 재발 방지 순서 → 정비 순서.

---

## Phase 1 — 출혈 멈추기 (진행 중 피해 차단)

지금 이 순간에도 `run_update_force.py`가 돌면 약한 `find_pdf()`가 또 오매칭을 만들 수 있음. 다른 모든 것보다 먼저 잡는다.

### 1. `find_pdf()` ID-first 리팩터링
- [ ] 우선순위 재정의: ① Zotero itemKey ② DOI ③ arXiv ID ④ title SHA1 ⑤ (최후) fuzzy title
- [ ] `register_zotero.py`: Zotero Web API의 attachment path를 직접 받아 slug에 저장 (제목 탐색 경로 제거)
- [ ] `_papers_index.json`에 `pdf_sha256`, `pdf_first_page_hash`, `doi_verified`, `zotero_item_key` 필드 추가
- [ ] 리뷰 생성 직전 sanity prompt: PDF에서 title/DOI/authors 추출 → Zotero metadata 비교, 불일치 시 중단·경고
- **검증**: 기존 정상 슬러그 10편·문제 슬러그 10편으로 매칭 결과 회귀 테스트

### 2. 오매칭 전수 탐지 (`audit_matching.py`)
- [ ] 스크립트 신규 작성 — 아래 검사 축
  - DOI/arXiv 교차검증 (review.md 본문 ↔ index)
  - PDF 첫 페이지 OCR 제목 ↔ index 제목 cosine sim < 0.7
  - Figure 개수/번호 이상치
  - `_search_index.json` 청크 ↔ Zotero abstract 임베딩 sim < 0.5
  - 2개 이상 플래그된 논문에 Sonnet 1-shot 판정
- [ ] 출력: `docs/ai4s/_audit_report.json` (low/medium/high confidence)
- [ ] ai4s 전수 1회 실행 → `high_confidence_mismatch` 규모 확정 (예상 139편 수렴 확인)
- **검증**: 이미 알려진 몇 개의 오매칭 슬러그가 high confidence로 잡히는지

---

## Phase 2 — 다음 대량 실행 안전 확보

Phase 1에서 근본 원인은 잡혔고 현황도 파악됨. 이제 "다음 실행"이 기존 자산을 해치지 않도록 한다.

### 3. 플래그 재설계 (MECE 3축)
- [ ] `--mode {curate|rebuild|reclassify|retime|deploy}` (argparse `choices=`, 필수)
- [ ] `--source {web|zotero}` (default `web`)
- [ ] `--images {skip|changed|all}` (default: curate=skip, retime=all, rebuild=all)
- [ ] 보조: `--topic`, `--days`, `--max-papers`, `--concurrency`, `--also-reclassify`, `--slugs`
- [ ] 단일 엔트리포인트 `run_mode(mode, source, images, **kwargs)` 함수로 Recipe A~H 통합
- [ ] 구 플래그 → 신규 매핑 + `DeprecationWarning`
- [ ] 조합 검증: `deploy`에 `source/images` 경고, `retime --source web` 경고 등
- **검증**: 13개 시나리오 표의 각 커맨드가 기대 스크립트 시퀀스를 출력하는지 (`--dry-run` 통과)

### 4. 파괴적 동작 보호
- [ ] `--dry-run`: 실행 예정 스크립트 시퀀스 + 예상 변경 파일 수 출력, 쓰기 0
- [ ] `rebuild` 모드는 기본 `--confirm` 요구, `--yes`로 우회
- [ ] `rebuild` 직전 `_papers_index.json` → `_papers_index.backup.json` 자동 스냅샷
- [ ] `rebuild` 전 샘플 5편의 PDF↔review 매칭 결과 미리 출력 (오매칭 조기 탐지)
- **검증**: `rebuild --yes`가 실제로 백업 파일을 남기는지, `--dry-run`이 변경 0인지

### 5. `validate_papers.py` 강화 — 배포 게이트
- [ ] 모든 figure 참조 실 파일 존재
- [ ] `classifications[topic]` schema 검증
- [ ] 카테고리 이름이 `CATEGORIES_BY_TOPIC` 소속 여부
- [ ] **카테고리 ↔ `category_timeline_{slug}.png` mismatch 탐지** (physical-ai 사건 근본)
- [ ] **DOI 교차검증 게이트** (Phase 1 결과 재발 방지)
- [ ] `--strict`에서 실패 시 non-zero exit
- **검증**: 현재 ai4s·physical-ai를 통과 못 시키는 항목이 보고되는지

---

## Phase 3 — 오매칭 139편 정리

안전 장치 설치 후 본격 복구. 이전 단계 없이 하면 또 오매칭을 만들 수 있음.

### 6. 복구 파이프라인
- [ ] `pipeline/fix_matching.py` — audit 리포트 기반 슬러그 단위 review/figure 삭제 + Zotero 재링크
- [ ] `run_update_force.py`에 `--slugs 001,047,...` 화이트리스트 옵션 추가
- [ ] 복구 시퀀스 실행:
  1. `audit_matching.py --topic ai4s` (최신 상태 재확인)
  2. `fix_matching.py --slugs ...` (high confidence만 우선)
  3. `run_update_force.py --mode curate --source zotero --slugs ...`
  4. `validate_papers.py --strict` + audit 재실행
  5. `--mode deploy`
- [ ] medium confidence는 10~20편 단위 배치로 분할 실행
- **검증**: audit report의 high → 0, medium이 배치마다 감소하는지 추적

---

## Phase 4 — 상시 가동 기반

복구까지 끝난 상태를 유지하기 위한 장치들.

### 7. 실행 안정성
- [ ] 모든 index/summary/narrative 쓰기를 `*.tmp` + `os.replace()` 원자 교체
- [ ] checkpoint를 모든 mode에 확장 (실패 슬러그 기록 → 자동 재시도)
- [ ] Anthropic/OpenAI 호출에 `tenacity` 3회 지수 백오프
- [ ] `pipeline/_logs/{timestamp}_{mode}.log` 자동 생성

### 8. 관측성
- [ ] `pipeline/_runs/{timestamp}.json` manifest: mode/source/images/duration/스크립트별 성공실패/파일 변경 수
- [ ] `prepare_deploy.py` push 전 diff 요약 (N changed, M new, K deleted + 삭제 목록)

### 9. Cloudflare 배포 검증
- [ ] `prepare_deploy.py --push` 후 `curl -I https://.../{topic}/` 10초 간격 최대 5분 폴링, 새 커밋 hash 반영 확인
- [ ] 네트워크 HTML 크기(<200KB면 경고), 타임라인 이미지 HTTP 200 확인

### 10. Drift 감지
- [ ] `cleanup.py`에 카테고리명 ↔ 타임라인 파일명 mismatch 탐지 추가
- [ ] `curate` 실행 후 "신규 카테고리 생김/사라짐" 배너 + 다음 실행에 `--images changed` 권장

---

## Phase 5 — 문서화·자동화

모든 것이 확정된 후. SKILL.md를 먼저 손대면 구현이 바뀌며 다시 써야 하므로 마지막에.

### 11. SKILL.md 재작성 (~330줄 → ~180줄)
- [ ] `<Execution_Policy>`: "모드 결정" 표 제거, 축 3개 의미만 기술
- [ ] `<Recipes>` Recipe A~H 삭제, 단일 엔트리포인트 + 파이프라인 플로우 1장
- [ ] `<Parameters>`: 축 3개 표 + 보조 파라미터 표
- [ ] `<Examples>`: 13개 시나리오 ↔ 단일 커맨드 표
- [ ] `<Flag_Migration>` 신규 — 구→신 매핑 (1릴리스 유지 후 제거)
- [ ] `<Reliability>` 신규 — Phase 2·4 요약
- [ ] `<Audit_Recovery>` 신규 — Phase 1·3 복구 워크플로우

### 12. README.md 동기화 (SKILL.md와 동시에)
- [ ] Quick Start 커맨드를 신규 3축(`--mode/--source/--images`)으로 교체
- [ ] "주간 운영" 예시: `run_update_force.py --topic ai4s --days 7 --images changed`
- [ ] "전체 재생성" 예시: `--mode rebuild --source {web|zotero} --yes`
- [ ] "배포만": `--mode deploy`
- [ ] 플래그 마이그레이션 안내 박스 (구→신 매핑, Deprecation 일정)
- [ ] Reliability 요약 (dry-run·confirm·backup·audit 한 단락)
- [ ] 복구 워크플로우 링크 (`audit_matching.py` → `fix_matching.py` → `--slugs` 재리뷰)
- [ ] CLAUDE.md의 "Common Commands" 섹션도 같은 커맨드로 정렬 (SKILL.md/README/CLAUDE.md 3자 일치)
- **검증**: Quick Start 커맨드를 그대로 복붙해 실행 → `--dry-run` 통과

### 13. CI/훅 (선택)
- [ ] pre-push git hook: `validate_papers.py --strict` + API 키 누출 정규식
- [ ] GitHub Actions on master: `build_papers_index.py` dry-run으로 index schema drift 감지
- [ ] 주간 cron: Cloudflare 페이지 HEAD 200 + 네트워크 HTML 크기 + `audit_matching.py` 자동 실행

---

## 의존 그래프

```
Phase 1 ─ 1(매칭 수정) ─┬─► 2(audit) ──┐
                        └──────────────┤
Phase 2 ─ 3(재설계) ─┬─► 4(보호 장치)   │
                     └─► 5(validate) ◄─┤ (DOI 교차검증)
                                        │
Phase 3 ─ 6(복구) ◄────────────────────┘
                │
                └─► (재검증 via 2·5)
Phase 4 ─ 7,8,9,10 (7은 3 이후 어디든)
Phase 5 ─ 11(SKILL.md) ↔ 12(README+CLAUDE.md 동시), 13(CI, 8·9·10 재사용)
```

## 우선순위 재정렬 근거

1. **Phase 1이 최우선인 이유**: 재설계를 먼저 해도 `find_pdf()`가 약하면 `curate --source web` 기본 동작에서 또 오매칭 발생. 출혈부터 막는다.
2. **Phase 2가 Phase 3 앞**: 재설계·dry-run·validate 없이 139편을 재리뷰하면 중간 실패나 또다른 오매칭을 감지 못함.
3. **Phase 3가 Phase 4 앞**: 관측성·CF 검증·drift 감지는 "정상 상태 유지"용. 비정상 상태(139편)인 지금은 효용이 낮음.
4. **Phase 5가 마지막**: SKILL.md는 1~10 확정 뒤 작성해야 재작업 없음.

## 체크포인트 (Phase 완료 기준)

| Phase | 완료 기준 |
|-------|---------|
| 1 | `find_pdf()` 회귀 테스트 통과 + `_audit_report.json` 생성, high confidence 규모 확정 |
| 2 | 13개 시나리오 `--dry-run` 통과 + `validate_papers.py --strict`가 현재 repo에서 유의미한 이슈 보고 |
| 3 | audit high confidence = 0, medium 배치 소거 추적 가능 |
| 4 | 최근 5회 실행의 manifest 파일 생성 + CF 배포 검증 자동 실행 기록 |
| 5 | SKILL.md 180줄 이하 + README·CLAUDE.md 3자 커맨드 일치 + 구 플래그 1릴리스 후 제거 PR |

---

## MEMORY 연동

- `pending_pdf_matching_bug.md` — 139편 오매칭. **Phase 1·3**로 해결.
- `pending_workflow_diagram.md` — 본 TODO와 무관, 병행 처리.
