from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Локаторы для главной страницы сайта
    """
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')
    LINK_MAIN_PAGE = 'http://selenium1py.pythonanywhere.com/'
    
class LoginPageLocators():
	#Локаторы для страницы логина и регистрации
	
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	
	
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME,'btn-add-to-basket')
    PRICE_BASKET_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, '.alert-info > .alertinner p strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR,'.product_main > .price_color')
    MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.alert-success > .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    LINK_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'

    
   
    
class BasePageLocators():
    """
    Локаторы для базовой страницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class BasketPageLocators():
    """
    Локаторы для страницы корзины
    """
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > .btn.btn-default')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'basket-items')
    BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, '.content > #content_inner p')
    BASKET_FEATURE_EMPTY = (By.CSS_SELECTOR, '.content > #content_inner a')