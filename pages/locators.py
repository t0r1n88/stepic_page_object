from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Локаторы для главной страницы сайта
    """
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')
    
class LoginPageLocators():
	"""
	Локаторы для страницы логина и регистрации
	"""
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	
class ProductPagelocators():
		"""
		Локаторы для страницы товара
		"""
	