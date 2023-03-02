from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payment_page(Base):

    check = "Checkout: Complete!"
    check_link = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    finish_button_locator = "//button[@id='finish']"
    check_word_locator = "//span[@class='title']"


    """Геттеры"""

    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_button_locator)))


    """Действия"""

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Нажата кнопка FINISH.')


    """Методы"""

    def confirm_payment(self):
        self.get_current_url()
        self.check_url(self.check_link)
        self.click_finish_button()
        self.check_word(self.get_check_word(self.check_word_locator), self.check)