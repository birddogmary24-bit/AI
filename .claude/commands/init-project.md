새 프로젝트 초기 세팅을 체계적으로 진행합니다. 인자로 프로젝트 유형을 받을 수 있습니다: $ARGUMENTS (예: flutter, express, next 등)

## 사전 조건 확인

먼저 아래 도구들의 상태를 확인합니다:
```bash
export PATH="/opt/homebrew/bin:$PATH"
gh auth status          # GitHub CLI 인증 확인
gcloud auth list        # GCP 인증 확인
```

인증이 안 되어 있으면 사용자에게 안내하고 중단합니다.

## 수행 순서

### Phase 1: 프로젝트 기본 정보 수집

사용자에게 아래 정보를 확인합니다 (AskUserQuestion 사용):
- 프로젝트 이름 (GitHub repo 이름, 영문 소문자+하이픈)
- 프로젝트 유형 ($ARGUMENTS가 없으면 질문): flutter / express / next / python 등
- 프로젝트 한줄 설명 (한국어)
- 공개/비공개 여부 (기본: 비공개)
- GCP 프로젝트 필요 여부 (기본: 예)
- GCP 결제 계정 선택:
  - `****` (My Billing Account - 기본)
  - `****` (mealcouponfriend)
  - `****` (openclaw)
  - `****` (appstorereview)
- CI/CD 필요 여부 (기본: 예)
- Notion 프로젝트 페이지 생성 여부 (기본: 예)

### Phase 2: GitHub 저장소 세팅

1. **Git 초기화** (이미 되어있으면 스킵):
   ```bash
   git init
   git branch -M main
   ```

2. **GitHub 저장소 생성**:
   ```bash
   gh repo create <GitHub-계정>/<프로젝트명> --private/--public --source=. --remote=origin --description="<한줄설명>"
   ```

3. **.gitignore 생성/확인**: 프로젝트 유형에 맞는 .gitignore
   - 공통: `.env`, `.env.local`, `.env.production`, `*.pem`, `*-sa-key.json`
   - Flutter: `.dart_tool/`, `build/`, `.flutter-plugins*`
   - Node.js: `node_modules/`, `.next/`, `dist/`, `.vercel`
   - Python: `__pycache__/`, `venv/`, `.venv/`, `*.pyc`

4. **CLAUDE.md 생성**: 프로젝트 루트에 프로젝트별 CLAUDE.md 작성
   - Git 브랜치 규칙 (main 직접 push 금지, feature 브랜치 필수)
   - 프로젝트 기본 정보 (framework, 언어, 아키텍처)
   - 빌드/테스트/검증 명령어
   - 파일 구조
   - 프로젝트 고유 주의사항

5. **README.md 생성**: 아래 표준 템플릿 사용
   ```markdown
   # <프로젝트명>
   <한줄 설명>

   ## 서비스 개요
   - (핵심 기능 3-5줄)

   ## 기술 스택
   | 영역 | 기술 |
   |---|---|
   | 프레임워크 | ... |
   | 언어 | ... |

   ## 프로젝트 구조
   (주요 디렉토리 트리)

   ## 로컬 개발
   (설치 및 실행 명령어)

   ## 배포
   (배포 명령어)

   ## 환경변수
   `.env.local` 필요:
   (KEY=value placeholder)
   ```

6. **초기 커밋 & Push**:
   ```bash
   git add .
   git commit -m "Initial project setup"
   git push -u origin main
   ```

### Phase 3: GCP 프로젝트 세팅 (선택)

사용자가 필요하다고 한 경우에만 진행:

1. **GCP 프로젝트 생성**:
   ```bash
   gcloud projects create <프로젝트ID> --name="<프로젝트명>"
   ```

2. **결제 계정 연결**:
   ```bash
   gcloud billing projects link <프로젝트ID> --billing-account=<선택한 결제계정>
   ```

3. **프로젝트 설정**:
   ```bash
   gcloud config set project <프로젝트ID>
   ```

4. **필수 API 활성화** (프로젝트 유형별):
   - 공통: `cloudbuild.googleapis.com`, `run.googleapis.com`, `secretmanager.googleapis.com`
   - Firebase 필요시: `firebase.googleapis.com`
   ```bash
   gcloud services enable <api> --project=<프로젝트ID>
   ```

5. **서비스 계정 생성** (CI/CD용):
   ```bash
   gcloud iam service-accounts create github-actions --display-name="GitHub Actions" --project=<프로젝트ID>
   ```

6. **.env 템플릿 생성**: placeholder 값으로 `.env.example` 파일 생성

### Phase 4: Notion 프로젝트 페이지 생성 (선택)

사용자가 필요하다고 한 경우에만 진행 (Notion MCP 사용):

1. **Project Hub 데이터베이스에 항목 추가**:
   - 프로젝트명, 상태: "In Progress", 기술 스택, GitHub URL, GCP Project ID, 시작일

2. **프로젝트 표준 서브페이지 6개 생성** (데이터베이스 항목 하위):

   **PRD** - Product Requirements Document
   - 프로젝트 개요, 타겟 사용자, 핵심 목표
   - 기술 스택 테이블
   - 아키텍처 다이어그램 (mermaid)
   - 비용 구조

   **기능정의서** - Feature Spec (상세 작성 필수)
   아래 항목을 **화면/모듈별**로 상세히 작성:

   **1) 화면별 기능 명세**
   - 각 화면(Screen/Page)마다 별도 섹션 (`## 화면명`)
   - 화면 목적, 진입 경로 (라우트), 접근 권한
   - UI 구성 요소 목록 (버튼, 입력, 카드 등)
   - 각 구성 요소의 동작 스펙 (탭/클릭/스와이프 시 동작)
   - 상태별 UI 변화 (로딩, 빈 데이터, 에러, 성공)
   - 유효성 검증 규칙 (입력 필드가 있는 경우)

   **2) 데이터 모델**
   - DB 테이블/컬렉션 스키마 (필드명, 타입, 제약조건)
   - 테이블 간 관계 (FK, 1:N, N:M)
   - 마이그레이션 히스토리 (버전별 변경사항)

   **3) API/서비스 레이어** (해당 시)
   - API 엔드포인트 목록 (Method, Path, 설명)
   - Request/Response 형식 (JSON 예시)
   - 에러 코드 정의

   **4) 상태 관리 흐름**
   - Provider/Store 목록과 역할
   - 주요 상태 전이 흐름 (예: 체크인→타이머→체크아웃)
   - 비동기 처리 패턴 (로딩/에러/성공)

   **5) 파일 구조** (코드 블록)
   - 전체 디렉토리 트리 (`lib/` 또는 `src/`)
   - 각 주요 파일/폴더의 역할 설명

   **6) 디자인 시스템 / UI 스펙**
   - 컬러 팔레트 (Light/Dark)
   - 타이포그래피 스케일
   - 공통 컴포넌트 (버튼, 카드, 다이얼로그 등)
   - 반응형/적응형 레이아웃 규칙

   **7) 외부 연동**
   - 사용 중인 외부 서비스/SDK 목록
   - 권한 요청 (카메라, 위치, 알림 등)
   - 플랫폼별 설정 (iOS Info.plist, Android Manifest)

   **버전 히스토리** - 일별 업데이트 기록
   - 날짜별로 묶어서 작업 내용 기록
   - 형식: `### YYYY-MM-DD` + bullet list
   - 최신이 위로 오도록 역순 정렬

   **Decision Log** - 기술 의사결정 기록
   - 날짜, 결정사항, 이유, 대안

   **Session Log** - 세션별 작업 이력
   - 각 개발 세션의 작업 내역

   **기타** - 서비스 URL, 환경변수, 참고사항
   - 서비스 URL: 웹, 어드민, API 문서 등
   - 앱 링크: Play Store / App Store (미출판 시 TBD)
   - GitHub repo 정보
   - GCP 프로젝트 정보 (프로젝트ID, 리전, 서비스)
   - 환경변수 목록 (값 제외, 키만)
   - 기타 참고사항

3. **문서 내용 자동 채우기**:
   프로젝트 디렉토리의 기존 문서(PRD.md, README.md, TECHNICAL_SPEC.md, package.json 등)를
   Explore 에이전트로 조사한 후, 조사 결과를 기반으로 6개 Notion 서브페이지에 실제 내용을 채움.
   - PRD: 기존 PRD.md + README.md 기반
   - 기능정의서: 소스코드 구조 분석 (화면별 위젯/컴포넌트, DB 스키마, Provider/Store, 라우터) + README.md 기반. 반드시 화면별 상세 스펙, 데이터 모델, 상태 관리 흐름까지 포함
   - 버전 히스토리: git log 또는 기존 문서 기반
   - 기타: gcloud run services list 로 URL 조회, package.json에서 환경변수 확인

### Phase 5: CI/CD 파이프라인 (선택)

사용자가 필요하다고 한 경우에만 진행:

1. **GitHub Actions 워크플로우 생성**: `.github/workflows/ci.yml`

   프로젝트 유형별 기본 템플릿:

   **Flutter:**
   - actions/checkout@v4 + subosito/flutter-action@v2
   - flutter pub get
   - dart run build_runner build --delete-conflicting-outputs (Drift 사용시)
   - flutter analyze
   - flutter test
   - flutter build apk --debug

   **Express/Node:**
   - actions/checkout@v4 + actions/setup-node@v4 (node 20)
   - npm ci
   - npm run lint
   - npm test

   **Next.js:**
   - actions/checkout@v4 + actions/setup-node@v4 (node 20)
   - npm ci
   - npm run lint
   - npm run build
   - npm test

   **Python:**
   - actions/checkout@v4 + actions/setup-python@v5
   - pip install -r requirements.txt
   - ruff check .
   - pytest

2. **Cloud Run 배포 워크플로우** (GCP 사용시): `.github/workflows/deploy.yml`
   - google-github-actions/auth@v2 (Workload Identity 또는 SA 키)
   - google-github-actions/deploy-cloudrun@v2
   - 리전: asia-northeast3

3. **GitHub Secrets 설정 안내**:
   ```bash
   gh secret set GCP_SA_KEY < path/to/sa-key.json
   ```

### Phase 6: 최종 검증 체크리스트

TodoWrite로 체크리스트를 생성하고 하나씩 확인합니다:

- [ ] GitHub repo 접근 가능 확인 (`gh repo view`)
- [ ] .gitignore에 민감 파일 포함 확인 (.env, 키 파일, .g.dart 등)
- [ ] CLAUDE.md 생성 및 규칙 정의 완료
- [ ] README.md 표준 템플릿으로 작성 완료
- [ ] GCP 프로젝트 생성 및 결제 연결 확인 (해당시)
- [ ] Notion Project Hub에 프로젝트 등록 확인 (해당시)
- [ ] CI/CD 워크플로우 파일 존재 확인 (해당시)
- [ ] 빌드 정상 통과 확인
- [ ] git push 정상 확인

## 규칙

- 모든 외부 서비스 연동(GitHub repo 생성, push 등)은 실행 전 사용자 확인 필수
- API 키, 시크릿 등 민감 정보는 절대 코드에 하드코딩하지 않음
- .env 파일은 .gitignore에 반드시 포함
- git remote URL에 PAT 포함 금지 (gh auth setup-git 사용)
- 사용자의 기존 프로젝트 구조와 컨벤션을 존중
- 프로젝트 유형을 모르면 추측하지 말고 질문할 것
- 한국어로 안내하되, 코드/설정 파일은 영문으로 작성
