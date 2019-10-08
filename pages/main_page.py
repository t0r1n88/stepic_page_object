from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    Класс связаный с главной страницей
    """
    def go_to_login_page(self):
        """
        Метод осуществляющий поиск и нажатие кнопки логина
        """
        link = self.browser.find_element(By.CSS_SELECTOR,'#login_link')
        link.click()
    
    def should_be_login_link(self):
        """
        Проверка налиичия ссылки
        """
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"),'Login link is not presented'