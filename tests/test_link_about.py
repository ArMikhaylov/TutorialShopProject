import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page


def test_link_about(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Catalog_page(driver)
    mp.select_menu_about()

    time.sleep(1)
