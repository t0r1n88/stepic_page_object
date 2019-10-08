class BasePage():
    """
    Базовый класс
    Конструктор экземпляра класса принимает на вход:
    browser: объект драйвера нужного браузера
    url: ссылка на страницу которую нужно открыть
    """
    def __init__(self,browser,url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)