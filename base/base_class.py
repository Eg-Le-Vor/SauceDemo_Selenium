class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод получения текущего URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий URL: {get_url}')
    

    """Метод проверки текста"""

    def check_text(self, word, result):
        assert word.text == result
        print('Проверка страницы успешна.')