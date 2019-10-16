from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.locators import BasketPageLocators

import pytest
import time

@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK_MAIN_PAGE
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    
    page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
@pytest.mark.skip   
def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_login_page_present(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
  
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка корзины, если мы переходим туда с главной страницы, не добавляя ничего в нее
    """
    link = MainPageLocators.LINK_MAIN_PAGE
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    # Нажимаем на кнопку корзины
    page.click_an_item(BasketPageLocators.BASKET_LINK)
    # инициализируем Page Object страницы с корзиной
    basket_page = BasketPage(browser,browser.current_url)
    # Проверяем что в корзине нет товаров
    basket_page.not_should_be_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_empty_basket()
    
    
    
    
    
    
    
    