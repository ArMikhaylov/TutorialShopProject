"""Library import"""
import datetime
from utilities.logger import Logger

"""Define class Base"""
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):

        Logger.add_start_step(method="get_current_url")
        get_url = self.driver.current_url
        print("Current url " + get_url)
        Logger.add_end_step(url=self.driver.current_url, method="get_current_url")

    """Method assert word"""
    def assert_word(self, word, result):

        Logger.add_start_step(method="assert_word")
        value_word = word.text
        try:
            assert value_word == result
            print("Good value_word")
        except AssertionError:
            print("Value in main_word is not equal to Products")
        Logger.add_end_step(url=self.driver.current_url, method="assert_word")

    """Method getting screenshot"""
    def get_screenshot(self):

        Logger.add_start_step(method="get_screenshot")
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('..\\screen\\' + name_screenshot)
        Logger.add_end_step(url=self.driver.current_url, method="get_screenshot")

    """Method assert url"""
    def assert_url(self, result):

        Logger.add_start_step(method="assert_url")
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
        Logger.add_end_step(url=self.driver.current_url, method="assert_url")
