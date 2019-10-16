from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from faker import Faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # Проверка  что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),'Login form not presented'

    def should_be_register_form(self):
        # Проверка  что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM),'Registration form not presented'
    
    def register_new_user(self,email,password):
        """
        Метод регистрирующий нового пользователя
        """
        #Вводим email
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        # Вводим пароль
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        # Повторяем пароль
        password_repeat_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_INPUT)
        password_repeat_input.send_keys(password)
        # Нажимаем кнопку зарегистрироваться
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
        
    def generate_data_for_new_user(self):
        # Генерируем email с помощью библиотеки Faker
        fake = Faker()
        email = fake.email()
        password ='4rfv5tgb6yhn'
        return email,password
        
        
        