"""Library import"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Define class Catalog_page"""
class Catalog_page(Base):

    # Locators

    catalog_link = "(//i[@class='svg inline  svg-inline-icon_catalog'])[2]"
    bikes_page_link = "//div[@class='section_item item bordered box-shadow']"
    lk_page_text = "//h1[@id='pagetitle']"

    # Getters

    def get_catalog_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_link)))

    def get_bikes_page_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bikes_page_link)))

    def get_lk_page_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_page_text)))

    # Actions

    def click_catalog_link(self):
        self.get_catalog_link().click()
        print("Click catalog link")

    def click_bikes_page_link(self):
        self.get_bikes_page_link().click()
        print("Click bikes page link")

    def save_lk_page_text(self):
        self.lk_page_text_value = self.get_lk_page_text().text
        print("Text in locator is '" + self.lk_page_text_value + "'")

    # Methods

    """Catalog migration method"""
    def method_catalog_link(self):

        Logger.add_start_step(method="method_catalog_link")
        self.get_catalog_link()
        self.click_catalog_link()
        Logger.add_end_step(url=self.driver.current_url, method="method_catalog_link")

    """Bikes page migration method"""
    def method_bikes_page_link(self):

        Logger.add_start_step(method="method_bikes_page_link")
        self.get_bikes_page_link()
        self.click_bikes_page_link()
        Logger.add_end_step(url=self.driver.current_url, method="method_bikes_page_link")

    """Bikes page checking method"""
    def check_bikes_page_link(self):

        Logger.add_start_step(method="check_bikes_page_link")
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/')
        Logger.add_end_step(url=self.driver.current_url, method="check_bikes_page_link")

    """LK text page checking method"""

    def lk_page_text_check_method(self, lk_text):
        Logger.add_start_step(method="check_lk_page_text")
        try:
            assert lk_text == 'Личный кабинет'
            print("Nice work. You are in your personal account!")
        except AssertionError:
            print("Sorry, you are probably not on the personal account page :(")
        Logger.add_end_step(url=self.driver.current_url, method="check_lk_page_text")

    def lk_page_link_check_method(self):

        Logger.add_start_step(method="lk_page_link_check_method")
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/personal/')
        Logger.add_end_step(url=self.driver.current_url, method="lk_page_link_check_method")