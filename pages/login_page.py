from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    url = "https://www.saucedemo.com/"
    check = "Products"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    user_name_locator = "//input[@id='user-name']"
    password_locator = "//input[@id='password']"
    login_button_locator = "//input[@id='login-button']"
    check_word_locator = "//span[@class='title']"


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
        print('Нажата кнопка входа.')


    """Методы"""

    def authorization(self, user_name, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name(user_name)
        self.input_password(password)
        self.click_login_button()
        self.check_word(self.get_check_word(self.check_word_locator), self.check)