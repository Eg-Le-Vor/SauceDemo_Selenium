from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class User_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    first_name_locator = "//input[@id='first-name']"
    last_name_locator = "//input[@id='last-name']"
    zip_code_locator = "//input[@id='postal-code']"
    continue_button_locator = "//input[@id='continue']"


    """Геттеры"""

    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))
    
    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))
    
    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip_code_locator)))
    
    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button_locator)))


    """Действия"""

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Имя введено.')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Фамилия введена.')

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('Почтовый индекс введён.')
    
    def click_continue_button(self):
        self.get_continue_button().click()
        print('Нажата кнопка CONTINUE.')


    """Методы"""

    def enter_data(self, first_name, last_name, zip_code):
        self.check_w = "Checkout: Overview"
        self.check_u = "https://www.saucedemo.com/checkout-step-one.html"
        self.check_word_locator = "//span[@class='title']"

        self.get_current_url()
        self.check_url(self.check_u)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_zip_code(zip_code)
        self.click_continue_button()
        self.check_word(self.get_check_word(self.check_word_locator), self.check_w)