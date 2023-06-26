import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.bikes_page import Bikes_page
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page
from pages.bike_polygon_strattos_page import Bike_polygon_strattos_page

@pytest.mark.run(order=2)
def test_buy_product_1(set_up, set_group):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    cp = Catalog_page(driver)
    cp.method_catalog_link()
    cp.method_bikes_page_link()
    cp.check_bikes_page_link()

    bp = Bikes_page(driver)
    bp.product_1_choosing()

    bpsp = Bike_polygon_strattos_page(driver)
    bpsp.check_bike_polygon_strattos_page_link()
    bpsp.polygon_strattos_bike()

    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # p = Payment_page(driver)
    # p.click_finish_button()
    #
    # f = Finish_page(driver)
    # f.finish()

    print("Finish Test 1")
    time.sleep(1)
    # driver.quit()

@pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test 2")

    login = Login_page(driver)
    login.open_direct_link()

    bp = Bikes_page(driver)
    bp.product_2_choosing()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
    print("Finish Test 2")
    time.sleep(1)
#     driver.quit()
#
#
# # @pytest.mark.run(order=2)
# def test_buy_product_3(set_up, set_group):
#
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options, service=Service())
#
#     print("Start Test 3")
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_products_3()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#     print("Finish Test 3")
#     time.sleep(1)
#     driver.quit()
