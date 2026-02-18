Express 프로젝트에 Swagger UI (OpenAPI 3.0) API 문서를 자동 생성합니다.

## 수행 순서

1. **프로젝트 분석**: `server.js` 또는 Express 라우트 파일들을 탐색하여 모든 API 엔드포인트를 찾습니다.
   - HTTP 메서드 (GET, POST, PUT, DELETE, PATCH)
   - 경로 (path params 포함)
   - 미들웨어 (인증 여부)
   - 요청 body / 응답 스키마

2. **의존성 설치**: `swagger-ui-express` 패키지를 설치합니다.
   ```bash
   npm install swagger-ui-express
   ```

3. **OpenAPI 스펙 파일 생성**: `src/swagger.js` (또는 프로젝트 구조에 맞는 위치)에 OpenAPI 3.0 스펙을 JS 객체로 정의합니다.
   - info: 프로젝트 package.json에서 name, description, version 참조
   - servers: 배포 URL이 있으면 포함, 없으면 localhost
   - tags: 엔드포인트를 논리적 그룹으로 분류
   - components/securitySchemes: 인증 방식이 있으면 정의 (Bearer, API Key 등)
   - paths: 모든 엔드포인트의 요청/응답 스키마 정의
     - 각 응답 상태 코드별 스키마
     - 예시 값 포함
     - path/query 파라미터 정의

4. **서버에 마운트**: Express 앱에 Swagger UI 미들웨어를 등록합니다.
   - `swagger-ui-express`와 스펙 파일을 import
   - **SPA 폴백이나 catch-all 라우트보다 위에** 마운트: `app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec))`
   - static 미들웨어보다도 위에 배치하는 것을 권장

5. **검증**: 서버를 실행하여 `/api-docs` 경로에서 Swagger UI가 정상 로드되는지 확인합니다.

## 규칙

- 기존 코드 패턴과 폴더 구조를 따를 것
- 한글 description이 사용된 프로젝트면 한글로, 영문이면 영문으로 작성
- 인증이 있는 엔드포인트는 반드시 security 속성을 설정
- 실제 코드의 응답 구조를 그대로 반영 (추측하지 말 것)
- package.json의 기존 정렬 순서를 유지
