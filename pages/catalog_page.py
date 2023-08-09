"""Library import"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Define class Catalog_page"""
class Catalog_page(Base):

    # Locators

    catalog_link = "(//i[@class='svg inline  svg-inline-icon_catalog'])[2]"
    bikes_page_link = "//div[@class='section_item item bordered box-shadow']"

    # Getters

    def get_catalog_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_link)))

    def get_bikes_page_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bikes_page_link)))

    # Actions

    def click_catalog_link(self):
        self.get_catalog_link().click()
        print("Click catalog link")

    def click_bikes_page_link(self):
        self.get_bikes_page_link().click()
        print("Click bikes page link")

    # Methods

    """Catalog migration method"""
    def method_catalog_link(self):
        self.get_catalog_link()
        self.click_catalog_link()

    """Bikes page migration method"""
    def method_bikes_page_link(self):
        self.get_bikes_page_link()
        self.click_bikes_page_link()

    """Bikes page checking method"""
    def check_bikes_page_link(self):
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/')
