import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class Login_page(Base):

    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    user_name_locator = "//input[@id='user-name']"
    password_locator = "//input[@id='password']"
    login_button_locator = "//input[@id='login-button']"

    users = {"standard_user": "standard_user",
         "locked_out_user": "locked_out_user",
         "problem_user": "problem_user",
         "performance_glitch_user": "performance_glitch_user"}
    password = "secret_sauce"

    """Геттеры"""

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name_locator)))
    
    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_locator)))
    
    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))


    """Действия"""

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Имя пользователя введено.')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Пароль введён.')
    
    def click_login_button(self):
        self.get_login_button().click()
        print('Нажата кнопка LOGIN.')


    """Методы"""

    def authorization(self):
        self.check_w = "Products"
        self.check_word_locator = "//span[@class='title']"
        
        with allure.step('authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.check_url(self.url)
            self.input_user_name(self.users["standard_user"])
            self.input_password(self.password)
            self.click_login_button()
            self.check_word(self.get_check_word(self.check_word_locator), self.check_w)
            Logger.add_end_step(url=self.driver.current_url, method='authorization')