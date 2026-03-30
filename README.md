# Steam QA 자동화 테스트 프로젝트

## 프로젝트 개요
Steam 웹스토어 검색 기능을 대상으로 테스트케이스를 설계하고
Selenium POM 구조로 자동화한 QA 포트폴리오 프로젝트입니다.

## 프로젝트 목적
반복적인 검색 기능 테스트를 자동화하여 QA 효율성을 높이고,
엣지 케이스 입력을 통해 실제 서비스에서 발생 가능한 버그를 탐지하는 것을 목표로 합니다.

## 테스트 대상
- Steam 웹스토어 검색 기능 (store.steampowered.com)

## 테스트 설계 기준
- 정상 흐름: 일반적인 게임 검색 시나리오 검증
- 예외 입력: 빈 값, 특수문자, 긴 문자열
- 실제 사용자 패턴: 한글 + 영어 혼합 검색
- 경계값 테스트: 입력 길이 제한 확인

## 발견한 버그
| 버그 ID | 내용 | 심각도 |
|---------|------|--------|
| BUG-001 | 100자 이상 입력 시 ERR_EMPTY_RESPONSE 서버 무응답 | Critical |
| BUG-002 | 한글+영어 혼합 검색 시 게임 본체 미노출, 사운드트랙만 노출 | Major |

## 프로젝트 구조
```
steam_qa/
  conftest.py          # 경로 설정
  pages/
    search_page.py     # Page Object Model — 페이지 요소 및 동작
  tests/
    test_search.py     # 테스트 케이스
```

## 테스트 항목
| TC-ID | 항목 | 결과 |
|-------|------|------|
| TC-001 | 빈 검색어 입력 | PASS |
| TC-002 | 특수문자 입력 (!@#$%) | PASS |
| TC-004 | 정상 게임명 검색 | PASS |
| TC-008 | 100자 이상 긴 텍스트 입력 (Critical 버그 재현) | PASS |

## 실행 방법
```bash
pip install selenium pytest pytest-html
pytest tests/test_search.py -v --html=report.html --self-contained-html
```

## 사용 기술
- Python 3.14
- Selenium 4.41.0
- pytest / pytest-html
- Page Object Model 패턴
