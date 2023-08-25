"""Library import"""
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page

"""Define Authorization Test"""
@allure.description("Test links")
def test_links(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Authorization Test")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.save_lk_page_text()
    lk_page_value = cp.lk_page_text_value
    cp.lk_page_text_check_method(lk_page_value)

    print("Finish Authorization Test")
    time.sleep(1)
    driver.quit()
