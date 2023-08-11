"""Library import"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

"""Define class Bikes_page"""
class Bikes_page(Base):

    # Locators

    price_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[1]"
    max_price_filter = "//input[@id='MAX_SMART_FILTER_P1_MAX']"
    brand_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[2]"
    brand_polygon_filter = "//label[@data-role='label_MAX_SMART_FILTER_73_1626735240']"
    bikes_type_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[3]"
    bikes_type_road_filter = "//label[@data-role='label_MAX_SMART_FILTER_155_4014459541']"
    riding_style_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[4]"
    riding_style_aero_road_filter = "//label[@data-role='label_MAX_SMART_FILTER_180_1634310769']"
    wheels_diametr_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[5]"
    wheels_diametr_28_filter = "//label[@data-role='label_MAX_SMART_FILTER_126_2274021061']"
    gender_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[6]"
    gender_unisex_filter = "//label[@data-role='label_MAX_SMART_FILTER_166_308411424']"
    model_year_filter = "(//div[@class='bx_filter_parameters_box_title title rounded3 box-shadow-sm'])[7]"
    model_year_2021_filter = "//label[@data-role='label_MAX_SMART_FILTER_119_4122755967']"
    select_bike_polygon_strattos = "(//span[@class='section-gallery-wrapper flexbox'])[2]"

    # Getters

    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))
    def get_max_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price_filter)))
    def get_brand_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_filter)))
    def get_brand_polygon_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_polygon_filter)))
    def get_bikes_type_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bikes_type_filter)))
    def get_bikes_type_road_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bikes_type_road_filter)))
    def get_riding_style_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.riding_style_filter)))
    def get_riding_style_aero_road_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.riding_style_aero_road_filter)))
    def get_wheels_diametr_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wheels_diametr_filter)))
    def get_wheels_diametr_28_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wheels_diametr_28_filter)))
    def get_gender_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gender_filter)))
    def get_gender_unisex_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gender_unisex_filter)))
    def get_model_year_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model_year_filter)))
    def get_model_year_2021_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model_year_2021_filter)))
    def get_select_bike_polygon_strattos(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_bike_polygon_strattos)))

    # Actions

    def click_price_filter(self):
        self.get_price_filter().click()
        print("Click price filter")
    def input_max_price_filter(self, max_price_filter):
        self.get_max_price_filter().send_keys(max_price_filter)
        print("Input max price = 200000")
    def click_brand_filter(self):
        self.get_brand_filter().click()
        print("Click brand filter")
    def click_brand_polygon_filter(self):
        self.get_brand_polygon_filter().click()
        print("Click brand polygon filter")
    def click_bikes_type_filter(self):
        self.get_bikes_type_filter().click()
        print("Click bikes type filter")
    def click_bikes_type_road_filter(self):
        self.get_bikes_type_road_filter().click()
        print("Click bikes type road filter")
    def click_riding_style_filter(self):
        self.get_riding_style_filter().click()
        print("Click riding style filter")
    def click_riding_style_aero_road_filter(self):
        self.get_riding_style_aero_road_filter().click()
        print("Click riding style aero road filter")
    def click_wheels_diametr_filter(self):
        self.get_wheels_diametr_filter().click()
        print("Click wheels diametr filter")
    def click_wheels_diametr_28_filter(self):
        self.get_wheels_diametr_28_filter().click()
        print("Click wheels diametr 28 filter")
    def click_gender_filter(self):
        self.get_gender_filter().click()
        print("Click gender filter")
    def click_gender_unisex_filter(self):
        self.get_gender_unisex_filter().click()
        print("Click gender unisex filter")
    def click_model_year_filter(self):
        self.get_model_year_filter().click()
        print("Click model year filter")
    def click_model_year_2021_filter(self):
        self.get_model_year_2021_filter().click()
        print("Click model year 2021 filter")
    def click_select_bike_polygon_strattos(self):
        time.sleep(2)
        self.get_select_bike_polygon_strattos().click()
        print("Click bike from result")

    # Methods

    """Product choosing 1 method"""
    def product_1_choosing(self):
        Logger.add_start_step(method="product_1_choosing")
        self.get_current_url()
        self.click_price_filter()
        self.input_max_price_filter("200000")
        self.click_brand_filter()
        self.click_brand_polygon_filter()
        self.click_bikes_type_filter()
        self.click_bikes_type_road_filter()
        self.click_riding_style_filter()
        self.click_riding_style_aero_road_filter()
        self.click_wheels_diametr_filter()
        self.click_wheels_diametr_28_filter()
        self.click_gender_filter()
        self.click_gender_unisex_filter()
        self.click_model_year_filter()
        self.click_model_year_2021_filter()
        self.click_model_year_filter()
        self.click_select_bike_polygon_strattos()
        Logger.add_end_step(url=self.driver.current_url, method="product_1_choosing")

    """Product choosing 2 method"""
    def product_2_choosing(self):
        Logger.add_start_step(method="product_2_choosing")
        self.click_select_bike_polygon_strattos()
        Logger.add_end_step(url=self.driver.current_url, method="product_2_choosing")
