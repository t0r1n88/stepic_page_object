from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import ProductPageLocators



class ProductPage(BasePage):
	"""
	Page object страницы товара
	"""
	def extract_text(self,name_element):
		"""
		Метод для извлечения текста заданного элемента
		name_element - это кортеж который мы распаковываем
		"""
		text = self.browser.find_element(*name_element).text
		if text:
			return text
		else:
			return False
			
	def add_product_to_basket(self):
		"""
		Метод отвечающий за поиск и нажатие кнопки добавления товара
		"""

		btn_add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
		btn_add_product_to_basket.click()
		
	def check_correct_name_product_in_basket(self,product_name):
		"""
		Проверка совпадения имени товара с именем того товара который мы действительно добавили 
		"""
		product_name = self.extract_text(product_name)
		# Так как имя книги в сообщении о добавлении, выделяется тегом strong, мы забираем только имя книги)
		message_add_product_to_basket = self.extract_text(ProductPageLocators.MESSAGE_ADD_PRODUCT_TO_BASKET)
		
		# text = self.browser.find_element(By.CSS_SELECTOR, '.alert-success > .alertinner strong').text
		# print(text)
		print(product_name)
		print()
		print(message_add_product_to_basket)
		assert  product_name == message_add_product_to_basket, 'Что то пошло не так, имя товара не совпадает с именем товара добавленного  в корзину. Омниссия недоволен'
	
	def check_correct_price_product_in_basket(self,price_product):
		"""
		Проверка совпадения цены товар с ценой корзины(только если товар один)
		Да я знаю что нужно сравнивать цифры ,а не строки. Чтобы избежать ситуаций вроде 10 и 1000000 в строковом виде.
		"""
		#Получаем цену товара в виде строки
		string_price_product = self.extract_text(price_product)
		#Конвертируем строку во float, предварительно отделив цифры от знака валюты с помощью split
		#price_product = float(string_price_product.split()[0])
		# Получаем цену корзины
		price_basket_after_add_product = self.extract_text(ProductPageLocators.PRICE_BASKET_AFTER_ADD_PRODUCT)
		# #Конвертируем строку во float, предварительно отделив цифры от знака валюты с помощью split
		#price_basket_after_add_product = float(string_price_basket_after_add_product.split()[0])
		print(string_price_product)
		print()
		print(price_basket_after_add_product)
		

		
		assert price_product == price_basket_after_add_product, 'Стоимость товара отличается'
		


	
		

