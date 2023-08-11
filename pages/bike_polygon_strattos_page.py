"""Library import"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Define class Bike_polygon_strattos_page"""
class Bike_polygon_strattos_page(Base):

    # Locators

    xl_filter = "//li[@data-treevalue='105_1465']"
    basket_button = "//div[@id='bx_117848907_47584_basket_actions']"
    move_to_basket_button = "//div[@class='wrap_icon wrap_basket baskets line-block__item top_basket']"
    product_vendor_code = "//span[@class='article__value']"
    product_price = "(//span[@class='price_value'])[3]"

    # Getters

    def get_xl_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xl_filter)))
    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))
    def get_move_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.move_to_basket_button)))
    def get_product_vendor_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_vendor_code)))
    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    # Actions

    def click_xl_filter(self):
        self.get_xl_filter().click()
        print("Click XL filter")
    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click basket button")
    def click_move_to_basket_button(self):
        self.get_move_to_basket_button().click()
        print("Click move to basket button")
    def save_product_vendot_code(self):
        self.value_product_vendor_code = self.get_product_vendor_code().text
        print("Product vendors code is '" + self.value_product_vendor_code + "'")

    def save_product_price(self):
        self.value_product_price = self.get_product_price().text
        print("Product price is '" + self.value_product_price + "'")

    # Methods

    def check_bike_polygon_strattos_page_link(self):
        Logger.add_start_step(method="check_bike_polygon_strattos_page_link")
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/shosseynye/shosseynyy/strattos_s5d/?oid=47586')
        Logger.add_end_step(url=self.driver.current_url, method="check_bike_polygon_strattos_page_link")

    def polygon_strattos_bike(self):
        Logger.add_start_step(method="polygon_strattos_bike")
        self.click_xl_filter()
        self.click_basket_button()
        time.sleep(1)
        self.click_move_to_basket_button()
        Logger.add_end_step(url=self.driver.current_url, method="polygon_strattos_bike")

    """Product vendor code saving method"""
    def product_vendor_code_method(self):
        Logger.add_start_step(method="product_vendor_code_method")
        self.save_product_vendot_code()
        Logger.add_end_step(url=self.driver.current_url, method="product_vendor_code_method")

    """Product price saving method"""
    def product_price_method(self):
        Logger.add_start_step(method="product_price_method")
        self.save_product_price()
        Logger.add_end_step(url=self.driver.current_url, method="product_price_method")
