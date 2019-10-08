from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс связаный с главной страницей
    """
    def go_to_login_page(self):
        """
        Метод осуществляющий поиск и нажатие кнопки логина
        """
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
    
    def should_be_login_link(self):
        """
        Проверка налиичия ссылки
        """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK),'Login link is not presented'