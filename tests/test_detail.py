import pytest
from selenium import webdriver 
from pages.game_detail_page import GameDetailPage

# 테스트에 사용할 Steam 게임 URL
# 이터널 리턴 (무료 게임)
FREE_GAME_URL = "https://store.steampowered.com/app/1049590/Eternal_Return/"
# Cyberpunk 2077 (유료 게임 — 미소유)
PAID_GAME_URL = "https://store.steampowered.com/app/294100/RimWorld/"

@pytest.fixture
def driver():
    # 디버그 모드로 열린 크롬에 연결 — 로그인 상태 유지
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    yield driver
    # 디버그 모드 연결 시 브라우저 종료 안 함
    # driver.quit() 하면 열어놓은 크롬까지 닫혀버림

class TestGameDetail:

    # TC-005: 유료 장바구니 버튼 확인
    def test_paid_game_has_cart_button(self, driver):
        # 유료 게임 상세 페이지에 장바구니 버튼이 있어야 함
        page = GameDetailPage(driver)
        page.open(PAID_GAME_URL)
        assert page.has_add_to_cart_button(), "유료 게임에 장바구니 버튼이 없습니다."

    # TC-006: 무료 게임 버튼 분기 확인
    def test_free_game_has_free_button(self, driver):
        # 무료 게임에는 장바구니 대신 무료/플레이 버튼이 있어야 함
        page = GameDetailPage(driver)
        page.open(FREE_GAME_URL)
        assert page.has_free_button(), "무료 게임에 무료 버튼이 없습니다."

    # TC-011: 찜 목록 버튼 항상 존재 확인
    def test_wishlist_button_always_exists(self, driver):
        # 유료/무료 관계없이 찜 목록 버튼은 항상 있어야 함
        page = GameDetailPage(driver)
        page.open(PAID_GAME_URL)
        assert page.has_wishlist_button(), "찜 목록 버튼이 없습니다."

    # TC-012: 게임 제목 노출 확인
    def test_game_title_is_displayed(self, driver):
        # 상세 페이지 진입 시 게임 제목이 정상 노출되어야 함
        page = GameDetailPage(driver)
        page.open(PAID_GAME_URL)
        title = page.get_game_title()
        assert title != "", "게임 제목이 비어 있습니다."
        print(f"게임 제목: {title}")

    # TC-013: 게임 태그 노출 확인
    def test_game_tags_exist(self, driver):
        # 상세 페이지에 장르 태그가 1개 이상 있어야 함
        page = GameDetailPage(driver)
        page.open(PAID_GAME_URL)
        tags = page.get_game_tags()
        assert len(tags) > 0, "게임 태그가 없습니다."
        print(f"태그 목록: {tags}")

    # TC-007: 언어 변경 확인
    def test_language_change_to_english(self, driver):
        # 언어를 영어로 변경했을 때 URL에 ?l=english 가 포함되어야 함
        page = GameDetailPage(driver)
        page.open(PAID_GAME_URL)
        page.change_language("english")
        current_url = page.get_current_url()
        assert "l=english" in current_url, "언어 변경 후 URL에 english 파라미터가 없습니다."
        print(f"언어 변경 후 URL: {current_url}")