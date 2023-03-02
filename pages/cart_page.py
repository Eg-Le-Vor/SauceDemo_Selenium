from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base):

    check = "Checkout: Your Information"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    checkout_button_locator = "//button[@id='checkout']"
    check_word_locator = "//span[@class='title']"


    """Геттеры"""

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button_locator)))


    """Действия"""

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Нажата кнопка CHECKOUT.')


    """Методы"""

    def checkout(self):
        self.get_current_url()
        self.click_checkout_button()
        self.check_word(self.get_check_word(self.check_word_locator), self.check)