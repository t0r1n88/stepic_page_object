from selenium.common.exceptions import NoSuchElementException
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
          
    
    