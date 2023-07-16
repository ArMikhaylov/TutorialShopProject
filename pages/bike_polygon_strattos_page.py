"""Library import"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Define class Bike_polygon_strattos_page"""
class Bike_polygon_strattos_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    xl_filter = "//*[@id='bx_117848907_47584_prop_105_list']/li[2]"
    basket_button = "//div[@id='bx_117848907_47584_basket_actions']"
    move_to_basket_button = "//div[@class='wrap_icon wrap_basket baskets line-block__item top_basket']"
    product_articul = "//*[@id='bx_117848907_47584']/div[1]/div/div[1]/div/div[2]/div/span[2]"
    product_price = "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/span[1]/span[1]"

    # Getters

    def get_xl_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xl_filter)))
    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))
    def get_move_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.move_to_basket_button)))
    def get_product_articul(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_articul)))
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
    def save_product_articul(self):
        self.value_product_articul = self.get_product_articul().text
        print("Product article is '" + value_product_articul + "'")
    def save_product_price(self):
        value_product_price = self.get_product_price().text
        print("Product price is '" + value_product_price + "'")

    # Methods

    def check_bike_polygon_strattos_page_link(self):
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/shosseynye/shosseynyy/strattos_s5d/?oid=47586')

    def polygon_strattos_bike(self):
        self.click_xl_filter()
        self.click_basket_button()
        time.sleep(1)
        self.click_move_to_basket_button()

    def product_articul_method(self):
        self.save_product_articul()
        # print("Product article is '" + value_product_articul + "'")

    def product_price_method(self):
        self.save_product_price()
