import pytest
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
	"""
	Тест для тестирования возможности добавления товара в корзину
	"""
	# Открываем страницу товара
	#link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
	# Инициализируем PageObject и передаем туда обьект браузера и линк
	page = ProductPage(browser,link)
	# Открываем страницу
	page.open()

	# Нажимаем кнопку добавить в корзину
	page.add_product_to_basket()
	
	#Считаем результат  математического выражения для получения ответа
	page.solve_quiz_and_get_code()
	

	# Проверки на ожидаемый результат
	page.check_correct_add_product_to_basket()
	time.sleep(150)