
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = "//input[@id='USER_LOGIN_POPUP']"
    password = "//input[@id='USER_PASSWORD_POPUP']"
    login_button = "//button[@name='Login1']"
    lk_word = "//h1[@id='pagetitle']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_lk_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_word)))


    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login_button")

    # Methods

    def authorization(self):

        auth_url = 'https://www.desporte.ru/auth/'
        personal_url = 'https://www.desporte.ru/personal/'
        self.driver.get(auth_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("desporte_user@rambler.ru")
        self.input_password("VCencF3MNmEJgsAgi9PF")
        self.click_login_button()
        self.driver.get(personal_url)
        print("Moved to https://www.desporte.ru/personal/")
        self.assert_word(self.get_lk_word(), 'Личный кабинет')

    def open_direct_link(self):
        bikes_filtered_url = 'https://www.desporte.ru/catalog/bikes/filter/price-base-to-200000/brand-is-poligon/code_type-is-shosseynyy-velosiped/style-is-bb70115eb856c8dd957fd528270f2365/whill-is-700%D1%81/itb_sex-is-uniseks/year-is-2021/apply/'
        self.driver.get(bikes_filtered_url)
        self.driver.maximize_window()
        print("Direct link to filtered bikes is open")