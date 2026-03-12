# birddogmary24-bit 로컬 프로젝트 구조 가이드

## 권장 디렉토리 구조

```
~/projects/
├── AI/                        # 이 레포 (개발 환경 설정 등)
├── ai-calculator-proxy/       # GCP Cloud Run AI 계산기 프록시 서버
├── appstorereview/            # 앱스토어 리뷰 관련
├── mealcouponfriend/          # 밀쿠폰 친구 앱
├── new-ott-curation/          # AI 기반 OTT 콘텐츠 큐레이션 (Flutter + Node.js + PostgreSQL)
├── opinionnewsletter/         # 오피니언 뉴스레터
├── tving-newsletter/          # 티빙 뉴스레터
├── tving-review-analysis/     # 티빙 리뷰 분석
├── tvingplayground/           # 티빙 플레이그라운드
└── util_dailcheckin/          # 데일리 체크인 유틸
```

---

## 최초 세팅 방법

### 방법 1: 자동 스크립트 사용 (권장)

```bash
# AI 레포를 먼저 클론
git clone https://github.com/birddogmary24-bit/AI.git ~/projects/AI

# 스크립트 실행 권한 부여 후 실행
chmod +x ~/projects/AI/setup_projects.sh

# ~/projects/ 아래에 모든 레포 클론
~/projects/AI/setup_projects.sh ~/projects
```

### 방법 2: 수동으로 하나씩 클론

```bash
mkdir -p ~/projects && cd ~/projects

git clone https://github.com/birddogmary24-bit/AI.git
git clone https://github.com/birddogmary24-bit/ai-calculator-proxy.git
git clone https://github.com/birddogmary24-bit/appstorereview.git
git clone https://github.com/birddogmary24-bit/mealcouponfriend.git
git clone https://github.com/birddogmary24-bit/new-ott-curation.git
git clone https://github.com/birddogmary24-bit/opinionnewsletter.git
git clone https://github.com/birddogmary24-bit/tving-newsletter.git
git clone https://github.com/birddogmary24-bit/tving-review-analysis.git
git clone https://github.com/birddogmary24-bit/tvingplayground.git
git clone https://github.com/birddogmary24-bit/util_dailcheckin.git
```

---

## 이미 클론된 레포 전체 업데이트

```bash
# ~/projects/ 하위 모든 레포를 한번에 pull
for dir in ~/projects/*/; do
  if [ -d "$dir/.git" ]; then
    echo "🔄 업데이트: $dir"
    git -C "$dir" pull
  fi
done
```

또는 스크립트를 다시 실행하면 자동으로 pull 처리됩니다:

```bash
~/projects/AI/setup_projects.sh ~/projects
```

---

## VS Code에서 한번에 열기 (멀티 루트 워크스페이스)

`~/projects/birddogmary24-bit.code-workspace` 파일 생성:

```json
{
  "folders": [
    { "name": "AI", "path": "AI" },
    { "name": "ai-calculator-proxy", "path": "ai-calculator-proxy" },
    { "name": "appstorereview", "path": "appstorereview" },
    { "name": "mealcouponfriend", "path": "mealcouponfriend" },
    { "name": "new-ott-curation", "path": "new-ott-curation" },
    { "name": "opinionnewsletter", "path": "opinionnewsletter" },
    { "name": "tving-newsletter", "path": "tving-newsletter" },
    { "name": "tving-review-analysis", "path": "tving-review-analysis" },
    { "name": "tvingplayground", "path": "tvingplayground" },
    { "name": "util_dailcheckin", "path": "util_dailcheckin" }
  ]
}
```

그 다음:
```bash
code ~/projects/birddogmary24-bit.code-workspace
```

---

## 새 레포가 생겼을 때

1. GitHub에서 레포 생성
2. `setup_projects.sh`의 `REPOS` 배열에 추가
3. `project-structure.md` 목록 업데이트
4. 스크립트 다시 실행
