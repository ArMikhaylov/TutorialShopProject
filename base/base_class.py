import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_world(self, word, result):
        value_word = word.text
        try:
            assert value_word == result
            print("Good value_word")
        except AssertionError:
            print("Value in main_word is not equal to Products")

    """Method assert word"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Education\\Python\\Projects\\shop_project\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
