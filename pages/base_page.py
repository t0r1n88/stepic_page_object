from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
class BasePage():

    """
    Базовый класс
    Конструктор экземпляра класса принимает на вход:
    browser: объект драйвера нужного браузера
    url: ссылка на страницу которую нужно открыть
    """
    def __init__(self,browser,url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def go_to_login_page(self):
        """
        Метод осуществляющий поиск и нажатие кнопки логина
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    def should_be_login_link(self):
        """
        Проверка налиичия ссылки
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
        
        
    def open(self):
        """
        метод открывающий страницу по ссылке
        """
        self.browser.get(self.url)
	
	
    
    def is_element_present(self,how,what):
        """
        Метод в котором будем перехватывать исключения где
        how: как искать (css, id, xpath и тд)
        what: что искать (строку-селектор)
        """
        try:
            self.browser.find_element(how,what)
        except   NoSuchElementException:
            return False
        return True	
		
	
		
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert

        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

			
    def is_not_element_present(self, how, what, timeout=4):
	    try:
	        WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))
	    except TimeoutException:
	    	return True
	    return False
		
    def is_disappeared(self, how, what, timeout=4):
	    try:
	        WebDriverWait(self.browser, timeout , 1, TimeoutException).until_not(EC.presence_of_element_located((how,what)))
	    except TimeoutException:
		    return False
	    return True
			
    def click_an_item(self,css_selector):
        """
        Метод осуществляющий клик по переданному элементу
        """
        item = self.browser.find_element(*css_selector)
        item.click()
    def should_be_authorized_user(self):
        """
        Проверка залогинен ли пользователь
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON),"User icon is not presented," \
                                                                 " probably unauthorised user"
        