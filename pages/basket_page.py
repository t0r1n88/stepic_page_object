from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    """
    Page Object описывающий корзину
    """
    def not_should_be_items_in_basket(self):
        """
        Проверяем что корзина пуста
        (то есть отсутствует элемент с классом basket-items,
        который содержит в себе содержимое корзины)
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Корзина не пуста!!!'
    
    def should_be_text_empty_basket(self):
        """
        Проверяем что есть текст о том что корзина пуста
        """
        text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT_EMPTY).text
        assert 'Your basket is empty.' in text, ' Не найдено сообщение о том что корзина пуста'
        # Небольшое дополнение, ведь в пустой корзине на всех языках у нас всегда есть ссылка
        # на главную страницу, правда наличие это ссылки наверное надо проверять отдельным тестом
        assert self.is_element_present(*BasketPageLocators.BASKET_FEATURE_EMPTY)