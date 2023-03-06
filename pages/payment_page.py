import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    finish_button_locator = "//button[@id='finish']"


    """Геттеры"""

    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_button_locator)))


    """Действия"""

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Нажата кнопка FINISH.')


    """Методы"""

    def confirm_payment(self):
        self.check_w = "Checkout: Complete!"
        self.check_u = "https://www.saucedemo.com/checkout-step-two.html"
        self.check_word_locator = "//span[@class='title']"

        with allure.step('confirm_payment'):
            Logger.add_start_step(method='confirm_payment')
            self.get_current_url()
            self.check_url(self.check_u)
            self.click_finish_button()
            self.check_word(self.get_check_word(self.check_word_locator), self.check_w)
            Logger.add_end_step(url=self.driver.current_url, method='confirm_payment')