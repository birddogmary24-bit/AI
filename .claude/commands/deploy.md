프로젝트를 GCP Cloud Run에 배포합니다. 인자로 프로젝트명 또는 환경을 받습니다: $ARGUMENTS (예: tving-newsletter, production 등)

## 사전 조건 확인

```bash
export PATH="/opt/homebrew/bin:$PATH"
gcloud auth list        # GCP 인증 확인
```

인증이 안 되어 있으면 사용자에게 안내하고 중단합니다.

## GCP 프로젝트 매핑

| 프로젝트 | GCP Project ID | Cloud Run 서비스 | 리전 |
|----------|---------------|-----------------|------|
| tving-newsletter | `****` | `****` | asia-northeast3 |
| mealcouponfriend | `****` | `****` | asia-northeast3 |
| appstorereview | `****` | `****` | asia-northeast3 |
| Opnion News Letter | `****` | `****` | us-central1 |
| tving-review-analysis | `****` | `****` | asia-northeast3 |

**배포 불가 프로젝트** (로컬 전용):
- util_dailycheckin (Flutter 모바일 앱 → 앱스토어 배포는 별도)
- budongsanxray1 (데이터 아카이브)

## 수행 순서

### Phase 1: 프로젝트 식별 및 확인

1. `$ARGUMENTS` 또는 현재 디렉토리로 프로젝트 판별
2. 매핑 테이블에서 GCP 프로젝트, 서비스명, 리전 확인
3. 배포 불가 프로젝트인 경우 안내 후 중단

AskUserQuestion으로 확인:
- 배포 대상 프로젝트/서비스 맞는지
- 배포 환경 (production이 기본)

### Phase 2: 사전 체크

**2-1. 코드 품질 확인**
프로젝트 유형에 따라:
- **Express/Node**: `npm run lint && npm test` (test 없으면 lint만)
- **Next.js**: `npm run lint && npm run build`
- **Python**: `ruff check . && pytest` (pytest 없으면 ruff만)

실패하면 사용자에게 알리고 중단 여부 확인

**2-2. Git 상태 확인**
```bash
git status --short
git log origin/main..HEAD --oneline 2>/dev/null
```
- 커밋되지 않은 변경사항이 있으면 경고
- 미푸시 커밋이 있으면 알림

**2-3. 환경변수 확인**
```bash
# Cloud Run 서비스의 현재 환경변수 확인
gcloud run services describe <서비스명> --project=<프로젝트ID> --region=<리전> --format='value(spec.template.spec.containers[0].env)' 2>/dev/null
```

### Phase 3: 배포 실행

**사용자 확인 필수**: 아래 내용을 보여주고 승인 받기
```
🚀 배포 정보:
- 프로젝트: <프로젝트명>
- GCP: <GCP Project ID>
- 서비스: <서비스명>
- 리전: <리전>
- 소스: <현재 디렉토리>
```

승인 후 실행:
```bash
gcloud run deploy <서비스명> \
  --project=<프로젝트ID> \
  --region=<리전> \
  --source=. \
  --allow-unauthenticated
```

배포 타임아웃: 10분 (--timeout 600000)

### Phase 4: 배포 후 검증

**4-1. 서비스 상태 확인**
```bash
gcloud run services describe <서비스명> --project=<프로젝트ID> --region=<리전> --format='value(status.url)'
```

**4-2. 헬스체크**
```bash
# 배포된 URL에 GET 요청
curl -s -o /dev/null -w "%{http_code}" <서비스URL>
```
- 200: ✅ 정상
- 그 외: ⚠️ 경고 (서비스 확인 필요)

**4-3. 최근 로그 확인** (에러 유무)
```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=<서비스명> AND severity>=ERROR" \
  --project=<프로젝트ID> --limit=5 --format='table(timestamp,textPayload)' 2>/dev/null
```

### Phase 5: Notion 배포 이력 기록

해당 프로젝트의 "기타" 서브페이지에 배포 이력 추가:
```
### 배포 이력
| 날짜 | 버전/커밋 | 서비스 | 상태 | 비고 |
```

"버전 히스토리" 서브페이지에도 배포 표시:
```
### YYYY-MM-DD
- 🚀 프로덕션 배포 (커밋: <short-hash>)
```

### Phase 6: 최종 요약

```
📋 배포 결과:
- ✅ 코드 품질: lint/test 통과
- ✅ 배포: <서비스명> → <리전>
- ✅ 헬스체크: HTTP <상태코드>
- ✅ Notion: 배포 이력 기록됨
- 🔗 URL: <서비스URL>
```

## 롤백 안내

배포에 문제가 있을 경우:
```bash
# 이전 리비전 목록 확인
gcloud run revisions list --service=<서비스명> --project=<프로젝트ID> --region=<리전> --limit=5

# 특정 리비전으로 트래픽 이동
gcloud run services update-traffic <서비스명> --to-revisions=<리비전명>=100 --project=<프로젝트ID> --region=<리전>
```

## 규칙

- 배포 실행 전 반드시 사용자 확인
- 환경변수 값은 로그에 출력하지 않음
- 배포 실패 시 자동 롤백하지 않음 (사용자에게 롤백 안내만)
- 개인정보/계정정보 마스킹 규칙 준수 (앞2+뒤2)
- 한국어로 안내
