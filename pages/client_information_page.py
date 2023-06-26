
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_zip(self, zip):
        self.get_zip().send_keys(zip)
        print("Input zip")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    # Methods

    def input_information(self):

        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_zip("123456")
        self.click_continue_button()
