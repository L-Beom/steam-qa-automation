import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    # 드라이버 설정
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

class TestSteamSearch:

    # TC-004: 정상 게임명 검색
    def test_normal_search(self, driver):
        page = SearchPage(driver)
        page.open()
        page.search("Eternal Return")
        titles = page.get_result_titles()
        assert len(titles) > 0, "검색 결과가 없습니다"

    # TC-001: 빈 검색어 입력
    def test_empty_search(self, driver):
        page = SearchPage(driver)
        page.open()
        page.search("")
        titles = page.get_result_titles()
        assert len(titles) > 0, "빈 검색 시 결과가 없습니다"

    # TC-002: 특수문자 입력
    def test_special_characters(self, driver):
        page = SearchPage(driver)
        page.open()
        page.search("!@#$%")
        titles = page.get_result_titles()
        # 특수문자 입력 시 전체 목록이 나오는 이슈 확인
        print(f"특수문자 검색 결과 수: {len(titles)}")

    # TC-008: 100자 이상 긴 텍스트 (Critical 버그 재현)
    def test_long_text_search(self, driver):
        page = SearchPage(driver)
        page.open()
        long_text = "가" * 100
        page.search(long_text)
        # 서버 무응답 여부 확인
        current_url = driver.current_url
        print(f"긴 텍스트 검색 후 URL: {current_url}")