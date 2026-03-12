#!/bin/bash
# =============================================================
# birddogmary24-bit GitHub 레포 로컬 구조 세팅 스크립트
# 실행 위치: 이 스크립트를 원하는 상위 디렉토리에서 실행하세요
# 예시: ~/projects/ 에서 실행하면 ~/projects/<레포명>/ 으로 클론됩니다
# =============================================================

GITHUB_USER="birddogmary24-bit"
BASE_DIR="${1:-$HOME/projects}"

REPOS=(
  "AI"
  "ai-calculator-proxy"
  "appstorereview"
  "mealcouponfriend"
  "new-ott-curation"
  "opinionnewsletter"
  "tving-newsletter"
  "tving-review-analysis"
  "tvingplayground"
  "util_dailcheckin"
)

echo "📁 베이스 디렉토리: $BASE_DIR"
mkdir -p "$BASE_DIR"

for REPO in "${REPOS[@]}"; do
  REPO_PATH="$BASE_DIR/$REPO"
  REPO_URL="https://github.com/$GITHUB_USER/$REPO.git"

  if [ -d "$REPO_PATH/.git" ]; then
    echo "🔄 [$REPO] 이미 존재 → git pull"
    git -C "$REPO_PATH" pull origin "$(git -C "$REPO_PATH" symbolic-ref --short HEAD)" 2>&1 | tail -1
  else
    echo "⬇️  [$REPO] 클론 중..."
    git clone "$REPO_URL" "$REPO_PATH"
  fi
done

echo ""
echo "✅ 완료! 구조:"
ls -1 "$BASE_DIR"
