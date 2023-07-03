"""Library import"""
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
    product_name = "//h1[@id='pagetitle']"
    product_price = "//span[@class='price_value']"

    # Getters

    def get_xl_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xl_filter)))
    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))
    def get_move_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.move_to_basket_button)))
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))
    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    # Actions

    def click_xl_filter(self):
        self.get_xl_filter().click()
        print("Click XL filter")
    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click basket button")
    def save_product_name(self):
        value_product_name = self.get_product_name().text
        # print("Product name is '" + value_product_name + "'")
    def save_product_price(self):
        value_product_price = self.get_product_price().text
        # print("Product price is '" + value_product_price + "'")

    # Methods

    def check_bike_polygon_strattos_page_link(self):
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/shosseynye/shosseynyy/strattos_s5d/?oid=47586')

    def polygon_strattos_bike(self):
        self.click_xl_filter()
        self.click_basket_button()
        self.click_move_to_basket_button()

    def info_product(self):
        # self.save_product_name()
        if value_product_name == "Шоссейный велосипед Polygon Strattos S5D (2021)":
            print("Product name is 'Шоссейный велосипед Polygon Strattos S5D (2021)'")
        else:
            print("Product name is '" + value_product_name + "'")
        if value_product_price == "168 000":
            print("Product price is 168 000")
        else:
            print("Product price is " + value_product_price)

