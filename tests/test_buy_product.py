import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page


BASE_URL = "https://www.saucedemo.com/"
CHROMEDRIVE_PATH = "utils/chromedriver.exe"
PASSWORD = "secret_sauce"
LOGIN_STANDARD_USER = "standard_user"

users = {"standard_user": "standard_user",
         "locked_out_user": "locked_out_user",
         "problem_user": "problem_user",
         "performance_glitch_user": "performance_glitch_user"}
password = "secret_sauce"


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
    login.authorization(users["standard_user"], password)

    print()

    main_page = Main_page(driver)
    main_page.select_product()

    print('\nКонец теста.')