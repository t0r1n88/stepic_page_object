from .base_page import BasePage
from selenium.webdriver.common.by import By





class MainPage(BasePage):
    """
    Класс связаный с главной страницей
    """
    def __init__(self,*args,**kwargs):
        super(MainPage,self).__init__(*args,**kwargs)