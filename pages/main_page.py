from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    Класс связаный с главной страницей
    """
    def got_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR,'login_link')
        link.click()
        