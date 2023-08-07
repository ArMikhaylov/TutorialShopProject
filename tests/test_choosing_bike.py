"""Library import"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.basket_page import Basket_page
from pages.bikes_page import Bikes_page
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page
from pages.bike_polygon_strattos_page import Bike_polygon_strattos_page

"""Define Test 1"""
@pytest.mark.run(order=1)
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
    bpsp.product_vendor_code_method()
    bpsp.product_price_method()
    test_value_vendor_code = bpsp.value_product_vendor_code
    test_value_price = bpsp.value_product_price
    bpsp.polygon_strattos_bike()
    time.sleep(1)

    bsp = Basket_page(driver)
    bsp.check_basket_page_link()
    bsp.basket_product_vendor_code_method()
    bsp.basket_product_price_method()
    test_value_basket_vendor_code = bsp.correct_basket_product_vendor_code
    test_value_basket_price = bsp.correct_basket_product_price
    bsp.assert_basket_product_vendor_code(test_value_vendor_code, test_value_basket_vendor_code)
    bsp.assert_basket_product_vendor_code(test_value_price, test_value_basket_price)
    bsp.click_clear_button_method()

    print("Finish Test 1")
    time.sleep(1)
    driver.quit()

"""Define Test 2"""
@pytest.mark.run(order=2)
def test_buy_product_2(set_up, set_group):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test 2")

    login = Login_page(driver)
    login.open_direct_link()

    bp = Bikes_page(driver)
    bp.product_2_choosing()

    bpsp = Bike_polygon_strattos_page(driver)
    bpsp.check_bike_polygon_strattos_page_link()
    bpsp.product_vendor_code_method()
    bpsp.product_price_method()
    test_2_value_vendor_code = bpsp.value_product_vendor_code
    test_2_value_price = bpsp.value_product_price
    bpsp.polygon_strattos_bike()
    time.sleep(1)

    bsp = Basket_page(driver)
    bsp.check_basket_page_link()
    bsp.basket_product_vendor_code_method()
    bsp.basket_product_price_method()
    test_2_value_basket_vendor_code = bsp.correct_basket_product_vendor_code
    test_2_value_basket_price = bsp.correct_basket_product_price
    bsp.assert_basket_product_vendor_code(test_2_value_vendor_code, test_2_value_basket_vendor_code)
    bsp.assert_basket_product_vendor_code(test_2_value_price, test_2_value_basket_price)
    bsp.click_clear_button_method()

    print("Finish Test 2")
    time.sleep(1)
    driver.quit()
