현재 세션의 작업을 정리하고 Notion + MEMORY.md에 기록합니다. 인자로 프로젝트명을 받습니다: $ARGUMENTS (예: util_dailycheckin, tving-newsletter 등. 없으면 현재 디렉토리 기준)

## 왜 이 스킬이 필요한가

이 스킬은 **실행하면 더 좋지만, 안 해도 연속성은 유지**됩니다:
- 실행 O → Notion + MEMORY.md에 깔끔하게 기록
- 실행 X → MEMORY.md + git log로 `/session-start`가 복원 가능

단, 실행하면 **"다음 할 일"이 명시적으로 기록**되어 다음 세션 복원이 훨씬 정확합니다.

## Notion 프로젝트 ID 매핑

| 프로젝트 | Notion Page ID |
|----------|---------------|
| util_dailycheckin | `****` |
| tving-newsletter | `****` |
| mealcouponfriend | `****` |
| budongsanxray1 | `****` |
| appstorereview | `****` |
| Opnion News Letter | `****` |
| tving-review-analysis | `****` |

## 수행 순서

### Step 1: 프로젝트 식별

1. `$ARGUMENTS`가 있으면 해당 프로젝트 사용
2. 없으면 현재 작업 디렉토리의 폴더명으로 프로젝트 판별
3. 위 매핑 테이블에서 Notion Page ID 확인
4. Notion에서 해당 프로젝트 페이지를 fetch하여 서브페이지 ID들 확인

### Step 2: 이번 세션 작업 내역 수집

```bash
# 오늘 날짜의 커밋 확인
git log --oneline --since="$(date +%Y-%m-%d) 00:00" --until="$(date -v+1d +%Y-%m-%d) 00:00" 2>/dev/null || git log --oneline -20

# 변경된 파일 요약
git diff --stat HEAD~5 HEAD 2>/dev/null || git status --short

# 현재 브랜치
git branch --show-current
```

### Step 3: 사용자에게 세션 요약 확인

AskUserQuestion으로 확인:
- 이번 세션에서 한 작업을 자동 요약하여 보여줌
- 추가할 내용이 있는지 질문
- **다음에 이어서 할 작업이 있는지 질문** (핵심!)
- Decision Log에 기록할 기술 결정이 있었는지 질문

### Step 4: MEMORY.md 업데이트 (최우선 — 창 닫혀도 살아남음)

프로젝트의 MEMORY.md 파일에 "현재 진행 상황" 섹션을 업데이트:

```markdown
## 현재 진행 상황
- **마지막 세션**: YYYY-MM-DD
- **브랜치**: feature/xxx
- **상태**: [완료 항목 요약]
- **다음 할 일**:
  1. [TODO 1]
  2. [TODO 2]
  3. [TODO 3]
```

**이 단계가 가장 중요**: MEMORY.md는 매 세션 시작 시 자동 로드되므로, 창을 닫아도 다음 세션에서 즉시 복원됩니다.

### Step 5: Notion 업데이트 (병렬 실행)

**5-1. 버전 히스토리 업데이트**
- 프로젝트의 "버전 히스토리" 서브페이지 fetch
- 기존 내용의 **맨 위**에 오늘 날짜 섹션 추가 (역순 정렬)
- 형식:
  ```
  ### YYYY-MM-DD
  - 작업 내용 1
  - 작업 내용 2
  - 작업 내용 3
  ```
- 같은 날짜가 이미 있으면 기존 항목에 추가 (중복 날짜 헤더 생성 금지)

**5-2. Session Log 업데이트**
- 프로젝트의 "Session Log" 서브페이지 fetch
- 기존 내용의 **맨 위**에 세션 기록 추가
- 형식:
  ```
  ### YYYY-MM-DD HH:MM 세션
  **브랜치**: feature/xxx
  **커밋 수**: N개
  **주요 변경**:
  - 변경 내용 1
  - 변경 내용 2
  **변경 파일**: 파일1, 파일2, ... (주요 파일만)
  **다음 할 일**:
  - [ ] TODO 1
  - [ ] TODO 2
  - [ ] TODO 3
  ```

**5-3. Decision Log 업데이트** (해당 시)
- 사용자가 기술 결정사항이 있다고 한 경우에만
- 형식:
  ```
  ### YYYY-MM-DD: [결정 제목]
  **결정**: 무엇을 결정했는지
  **이유**: 왜 이 결정을 했는지
  **대안**: 고려했던 다른 방안
  ```

**5-4. 기능정의서 업데이트** (해당 시)
- 새 화면이나 기능이 추가된 경우에만
- 기존 기능정의서에 새 섹션 추가 또는 기존 섹션 수정
- 상세 작성 7항목 기준 준수 (화면별 기능 명세, 데이터 모델, 상태 관리 등)

### Step 6: 코드 품질 확인

프로젝트 유형에 따라 실행:
- **Flutter**: `flutter analyze`
- **Express/Node**: `npm run lint`
- **Next.js**: `npm run lint && npm run build`
- **Python**: `ruff check .`

경고/에러가 있으면 사용자에게 알림 (자동 수정하지 않음)

### Step 7: 최종 요약

완료 후 사용자에게 보여줌:
- ✅ MEMORY.md 업데이트됨 (다음 세션 자동 복원)
- ✅ 버전 히스토리 업데이트됨
- ✅ Session Log 기록됨 (다음 할 일 포함)
- ✅/⬜ Decision Log (해당 시)
- ✅/⬜ 기능정의서 (해당 시)
- ✅/⚠️ 코드 품질 (깨끗함 / 경고 N개)
- 미푸시 커밋 수 (있으면 안내)

## 규칙

- **MEMORY.md 업데이트를 Notion보다 먼저 실행** (Notion 실패해도 MEMORY.md는 남아야 함)
- Notion 업데이트 전 반드시 기존 내용을 fetch하여 확인 (덮어쓰기 방지)
- 날짜 형식: YYYY-MM-DD (ISO 8601)
- 한국어로 작성
- 기존 내용을 절대 삭제하지 않음 (추가만 함)
- 개인정보/계정정보는 마스킹 규칙 준수 (앞2+뒤2)
- insert_content_after 또는 replace_content_range 사용 (replace_content 사용 금지)
