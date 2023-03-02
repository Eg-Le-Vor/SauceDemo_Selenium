from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    check = "Your Cart"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    cart_button_locator = "//div[@id='shopping_cart_container']"
    product_1_button_locator = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    check_word_locator = "//span[@class='title']"


    """Геттеры"""

    def get_product_1_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1_button_locator)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_locator)))


    """Действия"""

    def click_product_1_button(self):
        self.get_product_1_button().click()
        print('Товар №1 добавлен в корзину.')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Нажата кнопка перехода в корзину.')


    """Методы"""

    def select_product(self):
        self.get_current_url()
        self.click_product_1_button()
        self.click_cart_button()
        self.check_word(self.get_check_word(self.check_word_locator), self.check)