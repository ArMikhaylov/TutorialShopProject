"""Library import"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.bike_polygon_strattos_page import Bike_polygon_strattos_page

"""Define class Basket_page"""
class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket_product_articul = "//span[@data-entity='basket-item-name']"
    basket_product_price = "//div[@data-entity='basket-total-price']"
    clear_button = "//span[@class='delete_all colored_theme_hover_text remove_all_basket']"

    # Getters

    def get_basket_product_articul(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_product_articul)))
    def get_basket_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_product_price)))
    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_button)))

    # Actions

    def save_basket_product_articul(self):
        self.basket_product_articul = self.get_basket_product_articul().text
        self.correct_basket_product_articul = ((self.basket_product_articul.partition(': ')[2]).split(' штрих:')[0])
        print("Product articul in a basket is '" + self.correct_basket_product_articul + "'")
    def save_basket_product_price(self):
        self.basket_product_price = self.get_basket_product_price().text
        self.correct_basket_product_price = self.basket_product_price.split(' руб.')[0]
        print("Product price in a basket is '" + self.correct_basket_product_price + "'")
    def click_clear_button(self):
        self.get_clear_button().click()
        print("Click clear button")

    # Methods

    def check_basket_page_link(self):
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/basket/')

    def basket_product_articul_method(self):
        self.save_basket_product_articul()

    def basket_product_price_method(self):
        self.save_basket_product_price()

    def assert_basket_product_articul(self, article, basket_article):
        try:
            assert article == basket_article
            print("It's the same article: " + basket_article)
        except AssertionError:
            print("Probably the article is wrong. '" + article + "' is not the same as '" + basket_article + "'")

    def assert_basket_product_price(self, price, correct_price):
        try:
            assert price == correct_price
            print("It's the same price: " + correct_price)
        except AssertionError:
            print("Probably the price is wrong. " + price + " is not the same as " + correct_price + ".")

    def click_clear_button_method(self):
        self.get_screenshot()
        self.click_clear_button()
