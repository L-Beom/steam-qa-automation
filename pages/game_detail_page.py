from selenium.webdriver.common.by import By
import time

class GameDetailPage:

    def __init__(self, driver):
        # 생성자 — 이 클래스를 사용할 때 드라이버를 받아서 저장
        # driver: Selenium WebDriver 객체 (크롬 브라우저 제어)
        self.driver = driver

    def open(self, url):
        # 지정한 URL로 브라우저 이동
        # url: 이동할 Steam 게임 상세 페이지 주소
        # time.sleep(3): 페이지가 완전히 로드될 때까지 3초 대기
        self.driver.get(url)
        time.sleep(3)

    def get_game_title(self):
        # 게임 상세 페이지에서 게임 제목 텍스트를 가져옴
        # apphub_AppName: Steam 상세 페이지의 게임 제목 class명
        # 요소를 못 찾으면 빈 문자열 반환 (크래시 방지)
        try:
            return self.driver.find_element(By.CLASS_NAME, "apphub_AppName").text
        except:
            return ""
        
    def has_add_to_cart_button(self):
        # 유료 게임 여부 확인 — "장바구니 담기" 버튼 존재 여부 반환
        # is_displayed(): 버튼이 화면에 실제로 보이는지 확인
        # True: 버튼 있음 (유료 게임), False: 없음
        try:
            btn = self.driver.find_element(By.CLASS_NAME, "btn_addtocart")
            return btn.is_displayed()
        except:
            return False
    
    def has_free_button(self):
        # 무료 게임 여부 확인 — "무료" 또는 "Free" 텍스트 포함 버튼 탐색
        # game_purchase_action: 구매 버튼 영역 class명
        # 한국어/영어 둘 다 처리하기 위해 두 텍스트 모두 확인
        try:
            btns = self.driver.find_elements(By.CLASS_NAME, "game_purchase_action")
            for btn in btns:
                if "무료" in btn.text or "Free" in btn.text or "Play" in btn.text:
                    return True
            return False
        except:
            return False
        
    def has_wishlist_button(self):
        # 찜 목록 추가 버튼 존재 여부 확인
        # 유료/무료 모든 게임에 항상 있어야 하는 버튼 — TC-006 검증용
        try:
            btn = self.driver.find_element(By.ID, "add_to_wishlist_area")
            return btn.is_displayed()
        except:
            return False
        
    def get_game_tags(self):
        # 게임 태그 목록 가져오기 (예: 전략, RPG, 멀티플레이어 등)
        # app_tag: Steam 태그 각각의 class명
        # strip(): 태그 텍스트 앞뒤 공백 제거
        try:
            tags = self.driver.find_elements(By.CLASS_NAME, "app_tag")
            return [t.text.strip() for t in tags if t.text.strip()]
        except:
            return []
        
    def change_language(self, lang_code):
        # URL에 언어 파라미터를 붙여서 페이지 언어 변경
        # lang_code 예시: "english", "koreana"
        # ?l=english 형태로 URL 뒤에 붙이면 Steam이 해당 언어로 페이지를 보여줌
        # 이미 언어 파라미터가 있으면 교체, 없으면 새로 추가
        current_url = self.driver.current_url
        if "?l=" in current_url:
            new_url = current_url.split("?l=")[0] + f"?l={lang_code}"
        else:
            new_url = current_url + f"?l={lang_code}"
        self.driver.get(new_url)
        time.sleep(3)

    def get_current_url(self):
        # 현재 브라우저 URL 반환
        # 언어 변경 후 URL이 올바르게 바뀌었는지 확인할 때 사용
        return self.driver.current_url