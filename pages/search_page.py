from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchPage:
    URL = "https://store.steampowered.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def search(self, keyword):
        search_box = self.driver.find_element(By.NAME, "term")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

    def get_result_titles(self):
        results = self.driver.find_elements(By.CLASS_NAME, "title")
        return [r.text for r in results if r.text]