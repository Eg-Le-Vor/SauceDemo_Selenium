import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод получения текущего URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий URL: {get_url}.', end=' ')
    

    """Метод получения ключевого слова"""

    def get_check_word(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))


    """Метод проверки страницы по ключевому слову"""

    def check_word(self, word, result):
        assert word.text == result
        print('Переход на новую страницу успешен.\n')
    

    """Метод создания скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(f'../screenshots/{screenshot_name}')
        print('Скриншот текущей страницы сохранён.')


    """Метод проверки URL"""

    def check_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL корректный.')