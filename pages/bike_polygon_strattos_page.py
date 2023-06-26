
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Bike_polygon_strattos_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    xl_filter = "//*[@id='bx_117848907_47584_prop_105_list']/li[2]"
    basket_button = "//div[@id='bx_117848907_47584_basket_actions']"
    move_to_basket_button = "//div[@class='wrap_icon wrap_basket baskets line-block__item top_basket']"

    # Getters

    def get_xl_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xl_filter)))
    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))
    def get_move_to_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.move_to_basket_button)))

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

    # Methods

    def check_bike_polygon_strattos_page_link(self):
        self.get_current_url()
        self.assert_url('https://www.desporte.ru/catalog/bikes/shosseynye/shosseynyy/strattos_s5d/?oid=47586')

    def polygon_strattos_bike(self):
        self.click_xl_filter()
        self.click_basket_button()
        self.click_move_to_basket_button()
