import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_page


BASE_URL = "https://www.saucedemo.com/"
CHROMEDRIVE_PATH = "utils/chromedriver.exe"
PASSWORD = "secret_sauce"
LOGIN_STANDARD_USER = "standard_user"


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    print('\nНачало теста.\n')

    login = Login_page(driver)
    login.authorization()

    cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
    cart.click()
    success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
    assert success_test.text == 'Your Cart'
    print('Совершён переход в корзину.')

    print('\nКонец теста.')