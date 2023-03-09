import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page


CHROMEDRIVE_PATH = "utils/chromedriver.exe"


@allure.description('Переход на страницу ABOUT')
def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service(CHROMEDRIVE_PATH)
    driver = webdriver.Chrome(options=options, service=g)

    print('\n\nНачало теста.\n')

    login = Login_page(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_menu_about()

    print('\nКонец теста.\n')