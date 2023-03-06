import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.user_information_page import User_information_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


CHROMEDRIVE_PATH = "utils/chromedriver.exe"

users = {"standard_user": "standard_user",
         "locked_out_user": "locked_out_user",
         "problem_user": "problem_user",
         "performance_glitch_user": "performance_glitch_user"}
password = "secret_sauce"
first_name = "Egor"
last_name = "Chaika"
zip_code = "124365"


# @pytest.mark.run(order=3)
def test_select_product_1(set_group, set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.authorization(users["standard_user"], password)

    main_page = Main_page(driver)
    main_page.select_product_1()

    cart_page = Cart_page(driver)
    cart_page.checkout()

    user_information_page = User_information_page(driver)
    user_information_page.enter_data(first_name, last_name, zip_code)

    payment_page = Payment_page(driver)
    payment_page.confirm_payment()

    finish_page = Finish_page(driver)
    finish_page.finish()

    driver.quit()


# # @pytest.mark.run(order=1)
# def test_select_product_2(set_group, set_up):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     g = Service(CHROMEDRIVE_PATH)
#     driver = webdriver.Chrome(options=options, service=g)

#     login = Login_page(driver)
#     login.authorization(users["standard_user"], password)

#     main_page = Main_page(driver)
#     main_page.select_product_2()

#     cart_page = Cart_page(driver)
#     cart_page.checkout()

#     driver.quit()


# # @pytest.mark.run(order=2)
# def test_select_product_3(set_group, set_up):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     g = Service(CHROMEDRIVE_PATH)
#     driver = webdriver.Chrome(options=options, service=g)

#     login = Login_page(driver)
#     login.authorization(users["standard_user"], password)

#     main_page = Main_page(driver)
#     main_page.select_product_3()

#     cart_page = Cart_page(driver)
#     cart_page.checkout()

#     driver.quit()