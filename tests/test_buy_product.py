import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.user_information_page import User_information_page


BASE_URL = "https://www.saucedemo.com/"
CHROMEDRIVE_PATH = "utils/chromedriver.exe"
PASSWORD = "secret_sauce"
LOGIN_STANDARD_USER = "standard_user"

users = {"standard_user": "standard_user",
         "locked_out_user": "locked_out_user",
         "problem_user": "problem_user",
         "performance_glitch_user": "performance_glitch_user"}
password = "secret_sauce"
first_name = "Egor"
last_name = "Chaika"
zip_code = "124365"


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    print('\n\nНачало теста.\n')

    login = Login_page(driver)
    login.authorization(users["standard_user"], password)

    main_page = Main_page(driver)
    main_page.select_product()

    cart_page = Cart_page(driver)
    cart_page.checkout()

    user_information_page = User_information_page(driver)
    user_information_page.enter_data(first_name, last_name, zip_code)

    print('Конец теста.')