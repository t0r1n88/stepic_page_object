import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

@pytest.mark.skip
@pytest.mark.parametrize('link', [0,1,2,3,5,6,
									pytest.param(7, marks=pytest.mark.xfail(reason='wrong value')),
									8,9])
						  
def test_guest_can_add_product_to_basket(browser,link):
	"""
	Тест для тестирования возможности добавления товара в корзину
	"""
	# Открываем страницу товара
	link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{link}'

	# Инициализируем PageObject и передаем туда обьект браузера и линк
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()

	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	
	#Считаем результат  математического выражения для получения ответа
	page.solve_quiz_and_get_code()
	

	# Проверки на ожидаемый результат
	
	page.check_correct_name_product_in_basket(ProductPageLocators.PRODUCT_NAME)
	page.check_correct_price_product_in_basket(ProductPageLocators.PRICE_PRODUCT)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	"""
	Проверяем, что нет сообщения об успехе при добавлении товара в корзину
	"""
	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	# Инициализируем PageObject и передаем туда обьект браузера и линк
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
	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	# Инициализируем PageObject и передаем туда обьект браузера и линк
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	"""
	Проверяем, что нет сообщения об успехе с помощью is_disappeared
	"""
	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	# Инициализируем PageObject и передаем туда обьект браузера и линк
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()
	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	#Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page.should_not_be_success_message_is_disappeared()
	
