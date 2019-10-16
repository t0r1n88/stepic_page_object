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
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTER = (By.CSS_SELECTOR,"[name='registration_submit']")

	
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME,'btn-add-to-basket')
    PRICE_BASKET_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, '.alert-info > .alertinner p strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR,'.product_main > .price_color')
    MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.alert-success > .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    LINK_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
    TEST_LINK_PRODUCT_NOT_OFFER = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    TEST_LINK_PRODUCT_OFFER = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    
   
    
class BasePageLocators():
    """
    Локаторы для базовой страницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators():
    """
    Локаторы для страницы корзины
    """
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > .btn.btn-default')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'basket-items')
    BASKET_TEXT_EMPTY = (By.CSS_SELECTOR, '.content > #content_inner p')
    BASKET_FEATURE_EMPTY = (By.CSS_SELECTOR, '.content > #content_inner a')