프로젝트의 REST API 설계 시 표준 원칙을 적용합니다. API 엔드포인트 생성, 리뷰, 리팩토링 시 이 원칙을 참고합니다.

## 1. Request & Response

- 쓰기 요청(POST/PUT/PATCH): `Content-Type: application/json`, UTF-8
- 필드명: 프로젝트 컨벤션 통일 (camelCase 또는 snake_case)
- 날짜: ISO 8601 (`YYYY-MM-DDTHH:mm:ssZ`)
- HTTP Status Code로 성공/실패 전달 (200, 201, 400, 404 등)
- 에러 응답: `{"error_code": "INVALID_PARAMETER", "message": "..."}`
- Content/Metadata 분리:
```json
{
  "fruits": [{"name": "apple", "count": 5}],
  "offset": 5, "limit": 2, "total_count": 30
}
```

## 2. URI Structure

- **명사형 자원**: 동사 금지, HTTP Method로 행위 표현
  - Bad: `POST /createUser` → Good: `POST /users`
- **계층 구조**: `/{collection}/{id}/{sub-collection}/{id}`
  - `/products/p001/reviews/rev99`
- **복수형 = 배열 응답**: `GET /payments` → `[...]`, `GET /payments/T01` → `{...}`

## 3. Meta-Classifier

자원 식별자 뒤에 성격별 메타 분류어 사용:

- **attrs**: 속성 조회/수정 (전체 객체 대신 속성만)
  - `GET /members/m_123/attrs`, `PATCH /members/m_123/attrs`
- **methods**: CRUD 이상의 비즈니스 로직
  - `POST /payments/pay_abc/methods/approve`
  - `POST /accounts/u_789/methods/lock`
- **events**: 상태 변화 이력 (Audit Log)
  - `GET /deliveries/deliv_99/events`

## 4. Query Params

필터링/정렬/페이지네이션 용도로만 사용:
- `/tickets?status=open&priority=high`
- `/products?sort=price_asc`
- `/logs?offset=20&limit=10`

---

위 원칙을 기반으로 API를 설계/리뷰하라. 새 엔드포인트는 이 규칙에 맞게, 기존 API는 위반 사항을 식별하여 개선안을 제시하라.
