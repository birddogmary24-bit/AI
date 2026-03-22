# 개발 환경 설정 가이드

> 다른 컴퓨터에서 재설치 시 참고용

## 1. CLI 도구 설치

### Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### GitHub CLI
```bash
brew install gh
gh auth login
```

### Google Cloud SDK
```bash
brew install --cask gcloud-cli
gcloud auth login
```

### Node.js
```bash
# v24.x (fnm 또는 nvm 권장)
brew install node
```

### Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```

---

## 2. Claude Code 글로벌 설정

### `~/.claude/settings.json`
```json
{
  "permissions": {
    "allow": [
      "Read(//Users/wayne/**)",
      "Bash(done)",
      "WebFetch(domain:discuss.ai.google.dev)",
      "Bash(git clone:*)",
      "Bash(brew install:*)",
      "mcp__claude_ai_Notion__notion-fetch",
      "Bash(gcloud auth:*)",
      "WebSearch",
      "Bash(npm run:*)"
    ],
    "additionalDirectories": []
  },
  "permissionMode": "bypassPermissions",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/check-git-push.sh"
          }
        ]
      }
    ]
  }
}
```

> `additionalDirectories`는 프로젝트에 맞게 수정

### `~/.claude/hooks/check-git-push.sh`
```bash
#!/bin/bash
# git push 전에 코드리뷰를 강제하는 hook
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if echo "$COMMAND" | grep -q "git push"; then
  echo "git push 전에 /requesting-code-review 스킬을 실행해서 코드리뷰 결과를 보여주세요. 리뷰 후 사용자 확인 없이 바로 push를 진행하세요." >&2
  exit 2
fi

exit 0
```
```bash
chmod +x ~/.claude/hooks/check-git-push.sh
```

---

## 3. Claude Code Skills (Superpowers)

### 설치된 글로벌 스킬 (`~/.claude/skills/`)

| 스킬 | 용도 | 트리거 |
|------|------|--------|
| brainstorming | 기능 설계 전 브레인스토밍 | 기능 추가/수정 전 |
| writing-plans | 구현 계획 작성 | 스펙/요구사항 있을 때 |
| executing-plans | 계획 실행 (체크포인트 포함) | 계획 문서 있을 때 |
| subagent-driven-development | 서브에이전트로 병렬 개발 | 독립 태스크 여러 개 |
| dispatching-parallel-agents | 병렬 에이전트 조율 | 독립 조사 여러 개 |
| systematic-debugging | 4단계 체계적 디버깅 | 버그/에러 발생 시 |
| test-driven-development | TDD (RED-GREEN-REFACTOR) | 기능 구현 전 |
| requesting-code-review | AI 코드리뷰 요청 | 코드 완성 후, push 전 |
| receiving-code-review | 코드리뷰 피드백 대응 | 리뷰 받았을 때 |
| verification-before-completion | 완료 전 검증 | 작업 완료 선언 전 |
| finishing-a-development-branch | 브랜치 완료 처리 | 구현 완료 후 |
| using-git-worktrees | 격리된 워크트리 생성 | 기능 개발 시작 시 |
| using-superpowers | 스킬 사용법 메타 스킬 | 대화 시작 시 |
| writing-skills | 새 스킬 작성 | 커스텀 스킬 만들 때 |
| deploy-gcp | GCP Cloud Run 배포 | GCP 배포 시 |

### 설치 방법
Superpowers는 Claude Code 플러그인으로 설치:
```
Claude Code 내에서: /install-plugin superpowers
```
또는 수동으로 `~/.claude/skills/` 디렉토리에 각 스킬의 `SKILL.md` 파일 배치

### 커스텀 명령어 (`~/.claude/commands/`)
| 파일 | 용도 |
|------|------|
| brainstorm.md | 브레인스토밍 (deprecated → brainstorming 스킬) |
| write-plan.md | 계획 작성 (deprecated → writing-plans 스킬) |
| execute-plan.md | 계획 실행 (deprecated → executing-plans 스킬) |
| retrospect-prompt.md | 프롬프트 엔지니어링 회고 |
| retrospect-ai-tech.md | AI 기술 활용 회고 |

---

## 4. MCP 서버 연동 (claude.ai)

Claude Code VSCode 확장에서 자동 연결되는 MCP 서비스:

| 서비스 | 용도 |
|--------|------|
| Notion | 페이지 조회/생성/수정 |
| Google Calendar | 일정 관리 |
| Figma | 디자인 컨텍스트 |
| Amplitude | 프로덕트 분석 |
| Vercel | 배포/로그 관리 |
| Context7 | 라이브러리 문서 조회 |

> MCP 서버는 claude.ai 계정에 연결되어 있어 별도 설치 불필요

---

## 5. 프로젝트별 설정

### A증권사 AI 브리핑 (securitya)

#### GitHub Actions Secrets
| Secret | 용도 |
|--------|------|
| `FINNHUB_API_KEY` | Finnhub 데이터 수집 |
| `GEMINI_API_KEY` | Gemini AI 분석 생성 |
| `SUPABASE_URL` | Supabase 프로젝트 URL |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase 서버 키 |
| `CRON_SECRET` | Cron 엔드포인트 인증 |

#### Vercel 환경 변수
| 변수 | 용도 |
|------|------|
| `GEMINI_API_KEY` | Gemini 2.5 Flash/Lite |
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase URL (클라이언트) |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase 서버 키 |
| `CRON_SECRET` | Cron 인증 |
| `FINNHUB_API_KEY` | Finnhub API |

#### GitHub Actions Cron
| 워크플로우 | 스케줄 | 내용 |
|-----------|--------|------|
| `cron-finnhub.yml` | `30 21 * * *` UTC (06:30 KST) | Finnhub 수집 + AI 분석 생성 |
| `cron-sec.yml` | `30 22 * * *` UTC (07:30 KST) | SEC EDGAR 공시 수집 |

#### Supabase
- 프로젝트 URL: Vercel 환경 변수 참조
- 15개 테이블 (상세: 프로젝트 `docs/DATA-CATALOG.md`)
- 마이그레이션: `app/supabase/migrations/` 디렉토리

#### Vercel
- 플랜: Hobby (무료)
- 배포: GitHub `main` push → 자동 빌드/배포
- URL: https://securitya.vercel.app

---

## 6. 재설치 체크리스트

### 기본 도구
- [ ] Homebrew 설치
- [ ] `brew install gh` → `gh auth login`
- [ ] `brew install --cask gcloud-cli` → `gcloud auth login`
- [ ] Node.js 설치 (v24.x)
- [ ] `npm install -g @anthropic-ai/claude-code`
- [ ] `jq` 설치 확인 (`brew install jq` — hook 스크립트에서 사용)

### Claude Code 설정
- [ ] `~/.claude/settings.json` 복사 (위 내용 참조)
- [ ] `~/.claude/hooks/check-git-push.sh` 생성 + `chmod +x`
- [ ] Superpowers 플러그인 설치
- [ ] `~/.claude/commands/` 커스텀 명령어 복사

### 프로젝트
- [ ] GitHub 레포 클론
- [ ] Vercel 프로젝트 연결 + 환경 변수 설정
- [ ] Supabase 프로젝트 연결
- [ ] GitHub Actions Secrets 설정
- [ ] `cd app && npm install`
