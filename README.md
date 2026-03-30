# Steam QA 자동화 테스트 프로젝트

## 프로젝트 개요
Steam 웹스토어 검색 기능을 대상으로 테스트케이스를 설계하고
Selenium POM 구조로 자동화한 QA 포트폴리오 프로젝트입니다.

## 테스트 대상
- Steam 웹스토어 검색 기능 (store.steampowered.com)

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
