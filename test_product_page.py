import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from .pages.locators import LoginPageLocators
import time



@pytest.mark.user_login
class TestUserAddToBasketFromProductPage():
    """
    Класс для тестирования зарегистрированного пользователя
    """
    @pytest.fixture(scope='function', autouse=True)
    def setup(self,browser):
        
       
        # Создаем PageObject страницы с регистрацией
        page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        # Открываем страницу
        page.open()
        # Генерируем email и пароль
        email,password = page.generate_data_for_new_user()
        # Регистрируем нового пользователя используя полученные данные
        page.register_new_user(email,password)
        # Проверяем залогинен ли пользователь
        page.should_be_authorized_user()
    

    def test_user_cant_see_success_message(self,browser):
        """
        Проверяем, что нет сообщения об успешном добавлении при открытии страницы товара
        если мы его не добавляли
        """
        # Получаем ссылку на страницу продукта из локатора
        link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
        # Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
        page = ProductPage(browser,link)
        # Открываем страницу
        page.open()
        # Проверяем, что нет сообщения об успешном добавлени товара в корзину с помощью is_not_element_present
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        """
        Тест для тестирования возможности добавления товара в корзину
        """
        # Открываем страницу товара
        link = ProductPageLocators.TEST_LINK_PRODUCT_OFFER

        # Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
        page = ProductPage(browser,link)
        # Открываем страницу
        page.open()

        # Нажимаем кнопку добавить в корзину
        page.add_product_to_basket()
        
        #Считаем результат  математического выражения для получения ответа
        page.solve_quiz_and_get_code()
        

        # Проверки на ожидаемый результат
        # Проверяем совпадает ли название продукта, с названием продукта в корзине
        page.check_correct_name_product_in_basket(ProductPageLocators.PRODUCT_NAME)
        # Проверяем совпадает ли цена продукта с ценой продукта в корзине
        page.check_correct_price_product_in_basket(ProductPageLocators.PRICE_PRODUCT)
        


@pytest.mark.parametrize('link', [0,1,2,3,5,6,
									pytest.param(7, marks=pytest.mark.xfail(reason='wrong value')),
									8,9])
@pytest.mark.need_review						  
def test_guest_can_add_product_to_basket(browser,link):
	"""
	Тестирование возможности добавления товара незарегистрированным пользователем в корзину
	"""
	# Открываем страницу товара
	link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{link}'

	# Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()

	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	
	#Считаем результат  математического выражения для получения ответа
	page.solve_quiz_and_get_code()
	

	# Проверки на ожидаемый результат
	# Проверяем совпадает ли название продукта, с названием продукта в корзине
	page.check_correct_name_product_in_basket(ProductPageLocators.PRODUCT_NAME)
    # Проверяем совпадает ли цена продукта с ценой продукта в корзине
	page.check_correct_price_product_in_basket(ProductPageLocators.PRICE_PRODUCT)
@pytest.mark.xfail(reason='Этот тест должен падать по заданию 4_3_6')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	"""
	Проверяем, что нет сообщения об успехе при добавлении товара в корзину
	"""
	link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
	# Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()

	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()
	

def test_guest_cant_see_success_message(browser):
	"""
	Проверяем, что нет сообщения об успехе при открытии страницы товара
	"""
	link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
	# Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()
@pytest.mark.xfail(reason='Этот тест должен падать по заданию 4_3_6')
def test_message_disappeared_after_adding_product_to_basket(browser):
	"""
	Проверяем, что нет сообщения об успехе с помощью is_disappeared
	"""
	link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
	# Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()
	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	#Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page.should_not_be_success_message_is_disappeared()
   
def test_guest_should_see_login_link_on_product_page(browser):
    """
    Тест проверяющий наличие кнопки логина на странице товара
    """
    link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
    # Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
    page = ProductPage(browser, link)
    # Открываем страницу
    page.open()
    # Проверяем есть ли элемент при нажатии на который мы попадаем на страницу логина и регистрации
    page.should_be_login_link()
@pytest.mark.need_review	
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Тест проверяющий возможность перехода на страницу ввода логина
    """
    link = ProductPageLocators.TEST_LINK_PRODUCT_NOT_OFFER
    # Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
    page = ProductPage(browser, link)
    # Открываем страницу
    page.open()
    # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page() 
    # Инициализируем PageObject и передаем туда экземпляр браузера и url адрес
    login_page = LoginPage(browser, browser.current_url)
    # Проверяем работоспособность страницы логина    
    login_page.should_be_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверка корзины, если мы переходим туда со страницы товара, не добавляя ничего в нее
    """
    link = ProductPageLocators.LINK_PRODUCT_PAGE
    # инициализируем Page Object, передаем в конструктор экземпляр браузера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()  
    # Нажимаем на кнопку корзины
    page.click_an_item(BasketPageLocators.BASKET_LINK)
    # инициализируем Page Object страницы с корзиной
    basket_page = BasketPage(browser,browser.current_url)
    # Проверяем что в корзине нет товаров
    basket_page.not_should_be_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_empty_basket()
