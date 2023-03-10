import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Локаторы"""

    cart_button_locator = "//div[@id='shopping_cart_container']"
    product_1_button_locator = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_2_button_locator = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    product_3_button_locator = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    menu_button_locator = "//button[@id='react-burger-menu-btn']"
    about_button_locator = "//a[@id='about_sidebar_link']"


    """Геттеры"""

    def get_product_1_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1_button_locator)))
    
    def get_product_2_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2_button_locator)))
    
    def get_product_3_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3_button_locator)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_locator)))
    
    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button_locator)))
    
    def get_about_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.about_button_locator)))


    """Действия"""

    def click_product_1_button(self):
        self.get_product_1_button().click()
        print('Товар №1 добавлен в корзину.')

    def click_product_2_button(self):
        self.get_product_2_button().click()
        print('Товар №2 добавлен в корзину.')

    def click_product_3_button(self):
        self.get_product_3_button().click()
        print('Товар №3 добавлен в корзину.')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Нажата кнопка перехода в корзину.')
    
    def click_menu_button(self):
        self.get_menu_button().click()
        print('Нажата кнопка меню.')
    
    def click_about_button(self):
        self.get_about_button().click()
        print('Нажата кнопка ABOUT.')


    """Методы"""

    def select_product_1(self):
        self.check_w = "Your Cart"
        self.check_u = "https://www.saucedemo.com/inventory.html"
        self.check_word_locator = "//span[@class='title']"

        with allure.step('select_product_1'):
            Logger.add_start_step(method='select_product_1')
            self.get_current_url()
            self.check_url(self.check_u)
            self.click_product_1_button()
            self.click_cart_button()
            self.check_word(self.get_check_word(self.check_word_locator), self.check_w)
            Logger.add_end_step(url=self.driver.current_url, method='select_product_1')

    def select_product_2(self):
        self.check_w = "Your Cart"
        self.check_u = "https://www.saucedemo.com/inventory.html"
        self.check_word_locator = "//span[@class='title']"

        with allure.step('select_product_2'):
            Logger.add_start_step(method='select_product_2')
            self.get_current_url()
            self.check_url(self.check_u)
            self.click_product_2_button()
            self.click_cart_button()
            self.check_word(self.get_check_word(self.check_word_locator), self.check_w)
            Logger.add_end_step(url=self.driver.current_url, method='select_product_2')

    def select_product_3(self):
        self.check_w = "Your Cart"
        self.check_u = "https://www.saucedemo.com/inventory.html"
        self.check_word_locator = "//span[@class='title']"

        with allure.step('select_product_3'):
            Logger.add_start_step(method='select_product_3')
            self.get_current_url()
            self.check_url(self.check_u)
            self.click_product_3_button()
            self.click_cart_button()
            self.check_word(self.get_check_word(self.check_word_locator), self.check_w)
            Logger.add_end_step(url=self.driver.current_url, method='select_product_3')
    
    def select_menu_about(self):
        self.check_u = "https://www.saucedemo.com/inventory.html"

        with allure.step('select_menu_about'):
            Logger.add_start_step(method='select_menu_about')
            self.get_current_url()
            self.check_url(self.check_u)
            self.click_menu_button()
            self.click_about_button()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_menu_about')