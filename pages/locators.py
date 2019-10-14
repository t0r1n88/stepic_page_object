from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Локаторы для главной страницы сайта
    """
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')
    
class LoginPageLocators():
	#Локаторы для страницы логина и регистрации
	
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	
	
class ProductPageLocators():
	"""
		Локаторы для страницы товара
	"""
	BUTTON_ADD_TO_BASKET = (By.CLASS_NAME,'btn-add-to-basket')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.alert-success > .alertinner')
	PRICE_PRODUCT = (By.CSS_SELECTOR,'.product_main > .price_color')
	PRICE_BASKET_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, '.alert-info > .alertinner p')
	