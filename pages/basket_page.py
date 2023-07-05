"""Library import"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Define class Basket_page"""
class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish_button = "//button[@id='finish']"
    basket_product_articul = "//*[@id='basket-item-height-aligner-17249']/div[2]/h2/a/span/text()"
    basket_product_price = "//div[@data-entity='basket-total-price']"
    clear_button = "//span[@class='delete_all colored_theme_hover_text remove_all_basket']"

    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    # Methods

    def payment(self):

        self.get_current_url()
        self.click_finish_button()
