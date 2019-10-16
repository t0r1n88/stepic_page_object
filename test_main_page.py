from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.locators import BasketPageLocators
from .pages.locators import LoginPageLocators

import pytest
import time

@pytest.mark.guest_login
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        # Получаем ссылку на главную страницу из константы
        link = MainPageLocators.LINK_MAIN_PAGE
        # инициализируем Page Object, передаем в конструктор экземпляр браузера и url адрес
        page = MainPage(browser, link)
        # открываем страницу
        page.open()  
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page() 
        # инициализируем Page Object страницы логина, передаем в конструктор экземпляр браузера и url адрес 
        login_page = LoginPage(browser, browser.current_url)
        # Проверяем страницу с формами логина и регистрации
        login_page.should_be_login_page()
     
    def test_guest_should_see_login_link(self,browser):
        # Получаем ссылку на главную страницу из константы
        link = MainPageLocators.LINK_MAIN_PAGE
        # инициализируем Page Object, передаем в конструктор экземпляр браузера и url адрес 
        page = MainPage(browser, link)
        # открываем страницу
        page.open()
        # Проверяем наличие кнопки логина
        page.should_be_login_link()

    def test_login_page_present(self,browser):
        # Получаем ссылку на  страницу логина и регистрации из константы
        link = LoginPageLocators.LOGIN_URL
        # инициализируем Page Object, передаем в конструктор экземпляр браузера и url адрес
        page = LoginPage(browser, link)
        # открываем страницу
        page.open()
        # Проверяем страницу с формами логина и регистрации
        page.should_be_login_page()
     

     


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка корзины, если мы переходим туда с главной страницы, не добавляя ничего в нее
    """
    # Получаем ссылку на главную страницу из константы
    link = MainPageLocators.LINK_MAIN_PAGE
    # инициализируем Page Object, передаем в конструктор экземпляр браузера и url адрес
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
    
    
    
    
    
    
    
    