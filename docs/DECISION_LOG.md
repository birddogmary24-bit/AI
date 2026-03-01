# Decision Log

---

### [2026-03-01] Claude Code 권한 허용 범위 설정 방식
**상태**: 확정
**결정 내용**: 전역 설정(`~/.claude/settings.json`)에서 코딩 관련 도구를 광범위하게 allow 처리
**배경**: Claude Code가 파일 편집, 검색, 웹 조회 등 기본 코딩 작업마다 권한 확인을 요청하여 작업 흐름이 끊김
**검토한 대안들**:
- 대안 A: 프로젝트별 `.claude/settings.json`에 설정 → 매 프로젝트마다 반복 설정 필요하므로 기각
- 대안 B: `--dangerously-skip-permissions` CLI 플래그 → 매번 입력 필요하고 보안 위험 높아 기각
- 대안 C: `defaultMode: "bypassPermissions"` → 모든 권한을 무시하므로 과도, 기각
**최종 선택 이유**: 전역 `permissions.allow`에 필요한 도구만 명시적으로 등록하면 보안과 편의성 균형이 가장 적절
**영향 범위**: 모든 Claude Code 프로젝트의 권한 동작
