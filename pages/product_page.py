from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import ProductPageLocators



class ProductPage(BasePage):
	"""
	Page object страницы товара
	"""
	def add_product_to_basket(self):
		"""
		Метод отвечающий за поиск и нажатие кнопки добавления товара
		"""

		btn_add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
		btn_add_product_to_basket.click()
		
	def check_correct_add_product_to_basket(self):
		"""
		Метод проверяющий корректность добавления товара в корзину 
		и правильное отображение цены(в данном случае,так как при большом количестве товаров нужно будет слаживать их цены)
		"""
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message_add_product_to_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_TO_BASKET).text
		assert product_name in message_add_product_to_basket, 'Что то пошло не так, имя товара не найдено в сообщении о добавлении в корзину. Омниссия недоволен'
	
		
		price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		price_basket_after_add_product = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_AFTER_ADD_PRODUCT).text
		assert price_product in price_basket_after_add_product, 'Стоимость товара отличается'

	
		

